from django.conf.urls import url, include
from django.conf.urls.static import static
from django.urls import path
from django.contrib import admin
from django.contrib.auth import urls as auth_urls
from django.conf import settings

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url('accounts/', include('django.contrib.auth.urls'), name="logout"),
    url(r'', include('blog.urls')),
    # url('social/', include('social.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
