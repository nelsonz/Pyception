from django.conf.urls.defaults import *
from django.views.generic.simple import direct_to_template
from treehack.views import *
from django.views.generic.create_update import *
from django.conf import settings

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Example:
    # (r'^TreeHack/', include('TreeHack.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    (r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    (r'^admin/', include(admin.site.urls)),
                       (r"^$", direct_to_template,
                        {'template': 'index.html'}, 'index'),
                       (r'(?P<my_arg>\d+)/$', direct_to_template,
                        {'template': 'results.html'}, 'results'),
                       (r'test/$', direct_to_template,
                        {'template': 'index1.html'}, 'index1'),
                       (r'about/$', direct_to_template,
                        {'template': 'about.html'}, 'about'),
                       (r'transferCode/$', GiveGetCode),
                       (r"^assets/(?P<path>.*)$", 'django.views.static.serve',
                             {'document_root': settings.STATIC_DOC_ROOT}),
)

if settings.DEBUG:
    urlpatterns += patterns((r"^assets/(?P<path>.*)$", 'django.views.static.serve',
                             {'document_root': settings.STATIC_DOC_ROOT}),
                            )
