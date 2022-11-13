from distutils.command.upload import upload
from django.db import models
from imagekit.models import ProcessedImageField
from imagekit.processors import Thumbnail


# Create your models here.
class Movie(models.Model):
    title = models.CharField(max_length=20)
    audience = models.IntegerField()
    release_date = models.DateField(null=True)
    genre = models.CharField(max_length=30)
    score = models.FloatField()
    poster_url = models.TextField()
    description = models.TextField()
    image = ProcessedImageField(
        blank=True,
        upload_to='thumbnails/',
        format='JPEG',
        options={'quality': 90}
    )

    def __str__(self):
        return self.title