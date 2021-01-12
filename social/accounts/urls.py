from django.conf.urls import url
from django.contrib.auth import views as auth_views
from . import views as account_views

app_name = 'accounts'

urlpatterns = [ 
    url(r'my_account/$', account_views.my_account.as_view(), name='social-main'),
    url(r'login/$', auth_views.LoginView.as_view(template_name='accounts/login.html'), name='social-login'),
    url(r'logout/$', auth_views.LogoutView.as_view(template_name='accounts/logged_out.html'), name='social-logout'),
    url(r'signup/$', account_views.sign_up.as_view(), name='social-signup'),
]