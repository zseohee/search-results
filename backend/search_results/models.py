from django.db import models

class SearchResult(models.Model):
    title = models.CharField(max_length=255)
    category = models.CharField(max_length=100, blank=True)
    state = models.CharField(max_length=100, blank=True)
    summary = models.TextField(blank=True)
    source_url = models.URLField()
    publish_date = models.DateField()
    tags = models.JSONField(default=list)

    def __str__(self):
        return self.title
