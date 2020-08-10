from django.db import models

# Create your models here.
class rooms(models.Model):
    name = models.CharField(max_length=100)
    max = models.TextField()
    size = models.TextField()
    view = models.TextField()
    img = models.ImageField(upload_to='pics')
    bed = models.IntegerField()