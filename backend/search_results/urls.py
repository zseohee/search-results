from django.urls import path

from .views.scraping import search_google
from .views.search import TagSearchView, multi_filter_search

urlpatterns = [
    path("search/<str:tag>/", TagSearchView.as_view(), name="tag_search"),
    path("search/", multi_filter_search, name="multi_filter_search"),
    path("search-google/", search_google, name="search_google"),
]
