from django.db import models

# Create your models here.


class Simple (models.Model):
    text = models.CharField(max_length=200)
    number = models.IntegerField(default=0)
    url = models.URLField(default="www.examples.com")

    def __str__(self):
        return self.text
