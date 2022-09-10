from pyexpat import model
from django.db import models
from datetime import date

class Video(models.Model):
    title = models.CharField(max_length=30)
    description = models.TextField(max_length=256)
    video_file = models.FileField(upload_to='videos', blank=True, null=True)
    released = models.DateField(default=date.today)

    def __str__(self):
        return self.title
