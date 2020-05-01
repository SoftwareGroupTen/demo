from django.db import models

from django.contrib.auth.models import User

from django.utils import timezone

class Homework(models.Model):
    #subject = models.ForeignKey(user, on_delete=models.CASCADE)
    Homework_text =models.TextField()
    courseNum = models.IntegerField()
    Pub_time = models.DateTimeField(default=timezone.now)
    deadline = models.DateTimeField()

    class Meta:
        ordering = ('-Pub_time',)
    
    def __str__(self):
        return self.Homework_text