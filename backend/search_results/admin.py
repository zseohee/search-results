from django.contrib import admin

from .models import SearchResult

@admin.register(SearchResult)
class SearchResultAdmin(admin.ModelAdmin):
    list_display = ("title", "category", "state", "publish_date")
    list_filter = ("category", "state", "publish_date")
    search_fields = ("title", "summary", "source_url")
