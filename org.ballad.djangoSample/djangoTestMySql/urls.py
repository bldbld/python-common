from django.conf.urls.defaults import *

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    (r'^login/$', 'DjangoTestMySql.login.logout'),
    (r'^logout/$', 'DjangoTestMySql.login.logout'),
    (r'^add/$', 'DjangoTestMySql.add.index'),
    # Example:
    # (r'^DjangoTestMySql/', include('DjangoTestMySql.foo.urls')),

    # Uncomment the admin/doc line below and add 'django.contrib.admindocs' 
    # to INSTALLED_APPS to enable admin documentation:
    # (r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # (r'^admin/', include(admin.site.urls)),
)
