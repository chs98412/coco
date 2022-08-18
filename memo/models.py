from django.db import models

# Create your models here.
class Memo(models.Model):
    username = models.CharField(max_length=1000,null=True)
    content = models.CharField(max_length=1000,null=True)



'''
영화 api
2명: 게시판+댓글
'''
