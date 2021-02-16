from social.views import HomePage
from django.conf.urls import url, include
from . import views

urlpatterns = [
    # url('', views.HomePage.as_view(), name='social-home'),
    url("accounts/", include('social.accounts.urls', namespace='accounts')),
    url("accounts/", include('django.contrib.auth.urls')),
    url("groups/", include('social.groups.urls', namespace='groups')),
    url("posts/", include('social.posts.urls', namespace='posts')),
]