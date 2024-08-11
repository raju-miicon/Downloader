from django.db import models

# Create your models here.

from django.db import models

class DownloadHistory(models.Model):
    url = models.URLField()
    download_date = models.DateTimeField(auto_now_add=True)
