from django.db import models

class Post(models.Model):

    quote = models.TextField(blank=False)

    def __str__(self):
        return self.quote

