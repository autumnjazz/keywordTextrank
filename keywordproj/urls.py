from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
import showkeyword.views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', showkeyword.views.home, name="home"),
    path('count/', showkeyword.views.count, name="count"),
    path('textrank/', showkeyword.views.textrank, name="textrank"),
]
