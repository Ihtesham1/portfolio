from django.db import models


class Blog(models.Model):
    title = models.CharField(max_length=50)
    date = models.DateTimeField()
    summary = models.TextField(max_length=1000)
    image = models.ImageField(upload_to='images/')

    def __str__(self):
        return self.title

    def red_summary(self):
        return self.summary[:20]

    def red_date(self):
        return self.date.strftime('%b %d %Y')

