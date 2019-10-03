from django.db import models


class Job(models.Model):

    title = models.CharField(max_length=50)
    image = models.ImageField(upload_to='images/')
    summary = models.TextField(max_length=2000)

    def __str__(self):
        return self.title

    def red_summary(self):
        return self.summary[:20]