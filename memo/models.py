from django.db import models

# Create your models here.
class Memo(models.Model):
    username = models.CharField(max_length=1000,null=True)
    content = models.CharField(max_length=1000,null=True)