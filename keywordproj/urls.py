from django.contrib import admin
from django.urls import path
import showkeyword.views

urlpatterns = [
    path('admin/', admin.site.urls),
	path('',showkeyword.views.home, name="home"),
    path('count/',showkeyword.views.count, name="count"),
]
