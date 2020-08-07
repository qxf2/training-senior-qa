from django.db import models
from django.utils import timezone
# Create your models here.


class feedback(models.Model):
    user = models.CharField(max_length=200)
    submit_date = models.DateTimeField
    vote = models.CharField(max_length=200)


class comment(models.Model):
    user = models.ForeignKey(feedback, on_delete=models.CASCADE)
    comment_box = models.CharField(max_length=1000, default='SOME STRING')
