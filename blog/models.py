from django.db import models


class Blog(models.Model):
    title = models.CharField(max_length=50)
    date = models.DateTimeField()
    summary = models.TextField(max_length=300)
    image = models.ImageField(upload_to='images/')


