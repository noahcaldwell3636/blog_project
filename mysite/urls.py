from django.conf.urls import url, include
from django.conf.urls.static import static
from django.urls import path
from django.contrib import admin
# from django.contrib.auth import urls as auth_urls
from blog.views import PostListView as blog_post_list
from django.conf import settings

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url('blog/', include('blog.urls'), name="blog_urls"),
    url('social/', include('social.urls'), name="social_urls"),
    url(r'^', blog_post_list.as_view(), name="homepage"),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
