from django.db import models

# Create your models here.

class News(models.Model):
    title=models.CharField(max_length=255,blank=False)
    body=models.TextField(max_length=255,blank=False)
    author_name=models.CharField(max_length=50,blank=False)