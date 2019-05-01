from django.db import models

# Create your models here.
class Student(models.Model):
    Sid = models.CharField(max_length=20)
    Spsword = models.CharField(max_length=15)
    Sname = models.CharField(max_length=20)
    Sclass = models.CharField(max_length=20)
    Sschool = models.CharField(max_length=50)
    Sscore = models.IntegerField()

class Application(models.Model):
    Sid = models.CharField(max_length=20) #外键还没加方便起见以后再加
    Sname = models.CharField(max_length=20)
    Pname = models.CharField(max_length=20)
    Plevel = models.CharField(max_length=20)
    state = models.CharField(max_length=20)
    Anote =models.CharField(max_length=200)

