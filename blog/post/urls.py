from django.conf.urls import patterns, url

from .views import PostListing, PostCreateView, PostDetailView, PostUpdateView, PostDeleteView


urlpatterns = patterns(
    'post',
     url(r'^$', PostListing.as_view(), name='list'),
     url(r'^create/$', PostCreateView.as_view(), name='create'),
     url(r'^(?P<pk>\d+)/$', PostDetailView.as_view(), name='detail'),
     url(r'^(?P<pk>\d+)/update/$', PostUpdateView.as_view(), name='update'),
     url(r'^(?P<pk>\d+)/delete/$', PostDeleteView.as_view(), name='delete'),
)