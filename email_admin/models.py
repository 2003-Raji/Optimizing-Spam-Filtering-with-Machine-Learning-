from django.db import models

# Create your models here.
class SpamModel(models.Model):
    spam_category=models.CharField(max_length=250)
    spam_list=models.CharField(max_length=250)
