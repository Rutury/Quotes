from django.db import models

# Create your models here.
class Quote(models.Model):
    quote = models.TextField(unique=True)
    author = models.CharField(max_length=60)
    source = models.CharField(max_length=60)
    weight = models.PositiveIntegerField(default=100)
    likes = models.PositiveIntegerField(default=0)
    dislikes = models.PositiveIntegerField(default=0)
    views = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.quote
