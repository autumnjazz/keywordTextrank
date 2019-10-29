1. 프로젝트 설명
본 프로젝트는 자연어 텍스트 내에서 단어를 추출하여 다중 레벨 마인드맵을 만드는 것을 목표로 한다. 다중 레벨 마인드 맵이란, 각 레벨에 TextRank 로 선정된 텍스트의 핵심 키워드가 위치해 있고, 각 핵심 키워드 마다 Community Detection 을 적용하여, 소속된 community 내에서의 새로운 키워드를 Topic-Specific TextRank 를 통해 선정하여 마인드맵에 표현하는 것이다. 이 때 Topic-Specific TextRank 는 Topic-Specific PageRank 의 변형으로, 프로젝트에서 새로 제안하는 알고리즘이다. 

2. 데이터셋 및 그래프 모델
2.1. 데이터셋
2.1.1. 데이터셋 개요
데이터는 string 자료형의 자연어이며, 중간 과정에서는 영어로 된 하나의 신문 기사에 한정한다. 추후 여러 개의 글에도 적용할 수 있도록 확장할 수 있으며, 한국어 품사 분류의 정확도가 높다면 영어가 아닌 한국어에도 적용할 수 있다.

2.1.2. 데이터셋 전처리
영문 텍스트의 품사 분류를 하여 명사, 동사, 형용사만으로 키워드 추출을 한다. 품사 별로 분류된 데이터는 각 품사의 특성에 따라서 전처리 과정을 거친다. 명사의 경우 단수와 복수를 구분하지 않고 단수로 통일한다. 동사의 경우 활용형을 구분하지 않고 동사 원형으로 통일한다. 또한 형용사 역시 비교형, 최상형을 구분하지 않고 원형으로 통일할 수 있으나, 자연어에서 비교형과 최상형의 출현이 빈도가 높지 않으며 문맥 상 큰 의미를 주지 않기 때문에 프로젝트 일정에 맞춰서 유동적으로 전처리 과정을 선택한다. 

2.1.3. 매개변수 처리
기존 TextRank 알고리즘에서의 매개변수는 하나의 글인 string 을 받아 단어 별로 분류하거나 문장 별로 분류한 것이다. 그러나 본 프로젝트에서 각 함수가 처리할 매개변수는 문장 별로 구분을 하고, 각 문장 내의 단어 별로 구분을 한 것이다. 
Don't be fooled by the word "energy"! Some energy bars contain as much saturated fat as a Snickers bar. <원문>
[ 'fooled', 'word', 'energy', 'energy', 'bars', 'contain', 'saturated', 'fat', 'snickers', 'bar' ] <기존 방법>
[ ['fooled', 'word', 'energy'], ['energy', 'bars', 'contain', 'saturated', 'fat', 'snickers', 'bar'] ] <본 프로젝트에서의 방법>
즉, 문단과 문장 간 변화할 수 있는 글의 문맥을 고려하지 않았던 기존 방법에 비해, 본 프로젝트에서는 자연어를 수용할 때의 문맥을 고려했다. 이처럼 문장 별 단어를 구분하는 것이 프로젝트의 목적에 더 부합할 것이라고 생각하였다. 
매개변수를 2차원 배열로 전달함으로써 각 요소의 탐색 과정이 길어지고, 전체적인 알고리즘의 시간 복잡도가 높아지는 것에 대한 우려가 있다. 기존 방법에 비해 효율이 떨어지는 지에 대한 테스트가 필요하다.

2.2. 그래프 모델
2.2.1. 구현된 그래프 모델
그래프 모델은 undirected, unsigned 그래프를 기본으로 한다. 한편, 기존 PageRank 에서 unweighted 그래프 모델을 사용했던 것에 반해, TextRank 에서는 weighted 그래프를 사용할 수 있다. 그 이유로는, 텍스트 내의 단어들의 연관 관계가 여러 번 나타날 수 있기 때문이며, 이러한 관계는 가중치를 주어야 결과의 정확도가 높아질 것이다. 따라서 현재 구현한 그래프 모델은 서로 다른 vetex 를 추가하고, 두 vertex 간의 edge 를 중복 가능하게 추가한다. 이 중복된 edge 가 곧 가중치의 역할을 할 것이며, 그래프 시각화를 할 때에는 edge 를 여러 개 표현하기 보다 새로운 가중치 변수 w 를 두어 중복된 횟수에 따른 가중치를 표시할 것이다.

2.2.2. 추후 가능한 그래프 모델
undirect 과 unsigned 그래프 모델이 구현 가능해지면 결과물의 정확도는 높아질 것이다. 그러나 자연어의 특성 상 한 텍스트 내에서 단어 간의 direct, signed 관계를 구분하기란 매우 어렵다. direct 가 가능한 방법으로는 주어에서 목적어로 연결되는 관계이며, 문장 내 단어의 순서로서 파악할 수 있다. 그러나 순서만으로 주어와 목적어가 결정되지는 않는다는 점이 문제이다. signed 가 가능한 방법으로는 not 이 사용된 단어를 중심으로 전후 단어와 negative 한 관계를 맺는 것이다. 그러나 이 역시 순서만으로 결정되지 않으며, not 이외의 negative 한 단어들의 처리를 하기에는 매우 복잡해진다.

3. 그래프 알고리즘
3.1. TextRank
3.1.1. 개요
TextRank 는 PageRank 를 기반으로 한 알고리즘이다. PageRank 에서의 페이지 대신에 TextRank 에서는 vertex 로서 문장 또는 단어를 사용하고, 임의의 두 vertex 간의 유사도는 PageRank 에서 웹 페이지 간의 이동 확률과 같다. 
TextRank 는 먼저 텍스트 내의 단위를 정하고, 단위 별로 텍스트를 분류해서 그래프의 vertex 로 삼는다. 각 단위 간의 관계를 정하고, 이 관계에 따라 vertex 간의 edge 를 추가한다. 그리고 각 vertex 의 score 가 수렴할 때까지 TextRank 알고리즘을 적용한다. 마지막으로 결과 score 에 따라서 vertex 를 선정한다.

3.1.1.1. Keyword TextRank
(Mihalcea et al., 2004) 에서 소개된 텍스트 내의 단위는 단어 단위와 문장 단위이다. 본 프로젝트에서는 프로젝트 목적에 따라 단어 단위의 TextRank 를 진행하며, 이때 단어는 복합어가 아닌 단일어이다. 
키워드 추출을 위한 TextRank 에서 중요한 개념은 vertex 간의 관계, 즉 edge 의 설정이다. (Mihalcea et al., 2004) 에서는 co-occurrence 라는 개념을 사용하고 있다. co-occurrence 관계는 단어가 출현되는 지점 간 거리에 따른 관계 설정이다. 최대 N 개의 단어로 이루어진 window 를 설정하고, 이 window 안에서 동시에 단어가 출현했을 경우 그 단어는 연관되었다고 파악한다.

3.1.1.2. TextRank 알고리즘
G = (V,E) 를 vertex 의 집합 V 와 edge 의 집합 E 인 directed 그래프라고 하며, E 는 V x V 의 부분집합이다. Vi 에 대해 In(Vi) 는 Vi 로 들어오는 vertex 의 집합이며, Out(Vi) 는 Vi 에서 나가는(즉, Vi 가 가르키는) vertex 의 집합이다. Vi 의 score S(Vi) 는 다음과 같다. (Brin and Page, 1999)
 
이 때 d 는 보통 0.85 의 값을 갖는 0 에서 1 사이의 확률 값이다. 1 – d 의 값 만큼 무작위로 임의의 vertex 로 넘어간다. 초기화의 값은 수렴하는 최종 값에 영향을 주지 않으며, iteration 의 횟수만 영향을 준다.
프로젝트에서 사용할 그래프는 undirected weighted 그래프 모델이다. 따라서 기존 PageRank 식에서 in-degree 와 out-degree 를 구분없이 사용하며, Vi 와 Vj 간의 강도를 나타내는 가중치 wij 를 부여한다.
 

3.1.2. 예상 효과
TextRank 알고리즘을 사용하면, 프로젝트의 다중 레벨 마인드맵에서 각 레벨의 핵심 키워드를 선정할 수 있다. 특히 기존 TextRank 와 차이점을 두는 부분으로, 본 프로젝트에서는 문장 별 단어(word by sentence)를 window 탐색의 단위로 본다. 즉, 기존의 TextRank 에서는 문장이 나누어짐에 상관없이 문장 간 window 를 설정하는 것이 가능했으나, 프로젝트에서는 문장 내에서만 window 를 설정하고, 다른 문장으로 넘어갈 경우 새로 window 를 설정하게끔 구현하였다.

3.2. Community Detection
3.2.1 개요

3.2.2 예상 효과
Community Detection 은 TextRank 에 부가적으로 사용한다. TextRank 를 통해 선정된 키워드에 대해, 그 핵심 키워드가 소속된 community 를 파악한다. 파악된 community 내에서 Topic-Specific TextRank 를 적용한다. 이 때 Topic-Specific TextRank 는 기존의 Topic-Specific PageRank 를 변형한 것이다. 핵심 키워드와 연관된 새로운 community 내의 핵심 키워드를 일정 개수 추출하고, 그래프의 엣지로서 핵심 키워드와 연결한다. 

<참고문헌>
Page, L., Brin, S., Motwani, R., & Winograd, T. (1999). The PageRank citation ranking: Bringing order to the web. Stanford InfoLab
Mihalcea, R., & Tarau, P. (2004). Textrank: Bringing order into text. In Proceedings of the 2004 conference on empirical methods in natural language processing
