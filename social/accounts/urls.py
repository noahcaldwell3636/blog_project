from django.conf.urls import url
from django.contrib.auth import views as auth_views
from . import views as account_views

app_name = 'accounts'

urlpatterns = [ 
    url('', account_views.TestPage.as_view(template_name='accounts/test.html'), name='social-main'),
    url(r'login/$', auth_views.LoginView.as_view(template_name='accounts/login.html'), name='login'),
    url(r'logout/$', auth_views.LogoutView.as_view(template_name='accounts/logout.html'), name='logout'),
    url(r'SignUp/$', account_views.SignUp.as_view(template_name='accounts/signup.html'), name='signup'),
]