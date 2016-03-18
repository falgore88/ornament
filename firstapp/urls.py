from django.conf.urls import url, include
from django.contrib import admin

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^basicview/', include('article.urls')),
    url(r'^settings/', include('settings.urls')),
    url(r'^products/', include('product.urls')),
    url(r'^auth/', include('loginsys.urls')),
    url(r'^', include('article.urls')),
]
