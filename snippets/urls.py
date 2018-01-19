from django.urls import path, re_path, include
from rest_framework.urlpatterns import format_suffix_patterns
from snippets import views

urlpatterns = [
    path('',
        views.api_root),
    path('snippets/',
        views.SnippetList.as_view(),
        name='snippet-list'),
    re_path('snippets/(?P<pk>[0-9]+)/',
        views.SnippetDetail.as_view(),
        name='snippet-detail'),
    re_path('snippets/(?P<pk>[0-9]+)/highlight/',
        views.SnippetHighlight.as_view(),
        name='snippet-highlight'),
    path('users/',
        views.UserList.as_view(),
        name='user-list'),
    re_path('users/(?P<pk>[0-9]+)/',
        views.UserDetail.as_view(),
        name='user-detail'),
    path('api-auth/', include('rest_framework.urls')),
]

## Format suffixes: http://www.django-rest-framework.org/api-guide/format-suffixes/
urlpatterns = format_suffix_patterns(urlpatterns, allowed=['json', 'html', 'api'])
