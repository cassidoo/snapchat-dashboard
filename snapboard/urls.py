from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', 'board.views.main'),
    url(r'^get_images', 'board.views.get_images'),

) + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
