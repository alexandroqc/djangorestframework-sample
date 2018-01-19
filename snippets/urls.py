from django.urls import path, re_path, include
from rest_framework.urlpatterns import format_suffix_patterns
from snippets import views
from snippets.views import SnippetViewSet, UserViewSet, api_root
from rest_framework import renderers

snippet_list = SnippetViewSet.as_view({
    'get': 'list',
    'post': 'create'
})
snippet_detail = SnippetViewSet.as_view({
    'get': 'retrieve',
    'put': 'update',
    'patch': 'partial_update',
    'delete': 'destroy'
})
snippet_highlight = SnippetViewSet.as_view({
    'get': 'highlight'
}, renderer_classes=[renderers.StaticHTMLRenderer])
user_list = UserViewSet.as_view({
    'get': 'list'
})
user_detail = UserViewSet.as_view({
    'get': 'retrieve'
})

urlpatterns = [
    path('',
        api_root),
    path('snippets/',
        snippet_list,
        name='snippet-list'),
    re_path('snippets/(?P<pk>[0-9]+)/',
        snippet_detail,
        name='snippet-detail'),
    re_path('snippets/(?P<pk>[0-9]+)/highlight/',
        snippet_highlight,
        name='snippet-highlight'),
    path('users/',
        user_list,
        name='user-list'),
    re_path('users/(?P<pk>[0-9]+)/',
        user_detail,
        name='user-detail'),
    path('api-auth/', include('rest_framework.urls')),
]

## Format suffixes: http://www.django-rest-framework.org/api-guide/format-suffixes/
urlpatterns = format_suffix_patterns(urlpatterns, allowed=['json', 'html', 'api'])
