from django.conf.urls import patterns, include, url
from django.contrib import admin
admin.autodiscover()
from template_test import views

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('', (r'^test/$', views.test), 
    (r'^admin/', admin.site.urls), 
    (r'^meta/$', views.display_meta),
    (r'^search-form/$', views.search_form),
    (r'^search/', views.search),
    # Examples:
    # url(r'^$', 'template_test.views.home', name='home'),
    # url(r'^template_test/', include('template_test.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
)
