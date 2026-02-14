from django.db import models

from django.db import models


class Job(models.Model):
    adzuna_id = models.CharField(max_length=50, unique=True)

    title = models.CharField(max_length=500)
    company = models.CharField(max_length=300, blank=True)
    location = models.CharField(max_length=300, blank=True)

    normalized_role = models.CharField(max_length=100, blank=True, null=True)

    posted_at = models.DateTimeField()
    ingested_at = models.DateTimeField(auto_now_add=True)

    raw_data = models.JSONField()

    def __str__(self):
        return f"{self.title} ({self.normalized_role})"
