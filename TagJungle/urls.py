from django.conf.urls import include, url
from django.contrib import admin

from core.views import search, phone_number

urlpatterns = [
    # Examples:
    # url(r'^$', 'TagJungle.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^search/', search),
    url(r'^search/.*', search),
    url(r'^phone/', phone_number),
]
