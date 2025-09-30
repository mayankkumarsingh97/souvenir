from django.urls import path
from django.urls import path, re_path
from . import views

app_name = 'home'
urlpatterns = [
    path('', views.home, name="homepage"),
    path('aboutus', views.aboutus, name="aboutus"),
    path('online_support', views.online_support, name="online_support"),
   ]