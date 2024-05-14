from django.db import models

class Features(models.Model):
    feature_icon = models.CharField(max_length=50)
    feature_title = models.CharField(max_length=50)
    feature_desc = models.TextField()
    
# Create your models here.
