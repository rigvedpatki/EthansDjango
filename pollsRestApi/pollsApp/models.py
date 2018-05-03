from django.db import models
import datetime
from django.utils import timezone
# Create your models here.


class Question(models.Model):
    question_text = models.CharField(max_length=256)
    pub_date = models.DateField('date published')

    def was_published_recently(self):
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.pub_date <= now

    def __str__(self):
        return self.question_text


class Option(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    option_text = models.CharField(max_length=256)
    vote_count = models.IntegerField(default=0)

    def __str__(self):
        return self.option_text
