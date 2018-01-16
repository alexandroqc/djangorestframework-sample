from django.urls import path, re_path
from rest_framework.urlpatterns import format_suffix_patterns
from snippets import views

urlpatterns = [
    path('snippets/', views.snippet_list),
    re_path('snippets/(?P<pk>[0-9]+)/', views.snippet_detail),
]

## Format suffixes: http://www.django-rest-framework.org/api-guide/format-suffixes/
urlpatterns = format_suffix_patterns(urlpatterns, allowed=['json', 'html', 'api'])
