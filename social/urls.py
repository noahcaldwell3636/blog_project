from social.views import HomePage
from django.conf.urls import url, include
from . import views

urlpatterns = [
    url('', views.HomePage.as_view(), name='social-home')    
]