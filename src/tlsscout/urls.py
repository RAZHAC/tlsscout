from django.conf.urls import patterns, include, url
from django.contrib import admin

admin.autodiscover()

urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),
    url(r'^accounts/', include('allauth.urls')),
    url(r'^$', 'dashboard.views.dashboard', name='dashboard'),

    # profile
    url(r'^accounts/profile/$', 'userprofile.views.profile_show', name='profile_show'),
    url(r'^accounts/profile/edit/$', 'userprofile.views.profile_edit', name='profile_edit'),

    # sites
    url(r'^sites/$', 'tlssite.views.site_list', name='site_list'),
    url(r'^sites/add/$', 'tlssite.views.site_add_edit', name='site_add'),
    url(r'^sites/(?P<siteid>\w+)/$', 'tlssite.views.site_details', name='site_details'),
    url(r'^sites/(?P<siteid>\w+)/edit/$', 'tlssite.views.site_add_edit', name='site_edit'),
    url(r'^sites/(?P<siteid>\w+)/delete/$', 'tlssite.views.site_delete', name='site_delete'),
    url(r'^sites/(?P<siteid>\w+)/check/$', 'tlssite.views.site_check', name='site_check'),

    # groups
    url(r'^groups/$', 'group.views.group_list', name='group_list'),
    url(r'^groups/add/$', 'group.views.group_add_edit', name='group_add'),
    url(r'^groups/(?P<groupid>\w+)/edit/$', 'group.views.group_add_edit', name='group_edit'),
    url(r'^groups/(?P<groupid>\w+)/delete/$', 'group.views.group_delete', name='group_delete'),
    url(r'^groups/(?P<groupid>\w+)/$', 'group.views.group_details', name='group_details'),
    url(r'^groups/(?P<groupid>\w+)/check/$', 'group.views.group_check', name='group_check'),
 
    # tags
)

### import signals from signals.py (for profile autocreation on user creation)
import signals