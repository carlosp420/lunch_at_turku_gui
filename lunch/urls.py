from django.conf.urls import patterns, url

from . import views


urlpatterns = patterns(
    # url(r'^admin/', include(admin.site.urls)),
    url(r'', views.index, name='index'),
)
