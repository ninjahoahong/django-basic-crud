from django.db import models

# Create your models here.


class Post(models.Model):
    last_updated = models.DateTimeField(auto_now=True)
    title = models.CharField(max_length=200)
    body = models.TextField()

    def __unicode__(self):
        return self.title
