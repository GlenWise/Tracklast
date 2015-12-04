from django.conf.urls import patterns, include, url
from links.views import LinkListView, LinkCreateView, LinkDetailView
from django.contrib.auth.decorators import login_required as auth
from links.views import UserProfileEditView, UserProfileDetailView
# Uncomment the next two lines to enable the admin:
from links.views import LinkUpdateView
from links.views import LinkDeleteView
from links.views import VoteFormView

from django.contrib import admin
admin.autodiscover()
#Will this work?
urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'tracklast.views.home', name='home'),
    # url(r'^tracklast/', include('tracklast.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', LinkListView.as_view(), name='home'),
    url(r'^login/$', 'django.contrib.auth.views.login', {
    'template_name': 'login.html'}, name="login"),
    url(r'^logout/$', 'django.contrib.auth.views.logout_then_login',
        name="logout"),
    url(r'^edit_profile/$', auth(UserProfileEditView.as_view()), 
        name="edit_profile"),
    url(r'^accounts/', include('registration.backends.simple.urls')),
    url(r'^users/(?P<slug>\w+)/$', UserProfileDetailView.as_view(), 
        name="profile"),
    url(r'^link/create/$', auth(LinkCreateView.as_view()),
        name='link_create'),
    url(r'^link/(?P<pk>\d+)/$', LinkDetailView.as_view(),
        name='link_detail'),
    url(r'^link/update/(?P<pk>\d+)/$', auth(LinkUpdateView.as_view()),
        name='link_update'),
    url(r'^link/delete/(?P<pk>\d+)/$', auth(LinkDeleteView.as_view()),
        name='link_delete'),
    url(r'^comments/', include('django.contrib.comments.urls')),
    url(r'^vote/$', auth(VoteFormView.as_view()), name="vote"),

)