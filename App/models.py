from django.db import models
from .constanta import *

# Create your models here.
class News(models.Model):
    title = models.CharField(max_length=200)
    text = models.TextField()
    link = models.CharField(max_length=600)
    file = models.FileField(upload_to = 'media/')
    data = models.DateField(auto_now=True)
    category = models.CharField(max_length=200, choices=Category)

    def __str__(self) -> str:
        return self.title +"-nomi " + str(self.data)
    

class Admins(models.Model):
    username = models.CharField(max_length=20)
    password = models.CharField(max_length=8)

    def __str__(self) -> str:
        return self.username
    

class Notification(models.Model):
    text = models.CharField(max_length=500)
    is_read = models.BooleanField(default=False)
    # b = models.De

    def __str__(self) -> str:
        return str(self.is_read)
    

