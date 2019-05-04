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
    Sid = models.CharField(max_length=20)  # 外键还没加方便起见以后再加
    Sname = models.CharField(max_length=20)
    Pname = models.CharField(max_length=20)
    Plevel = models.CharField(max_length=20)
    state = models.CharField(max_length=20)
    Anote = models.CharField(max_length=200)


class School(models.Model):
    Schname = models.CharField(max_length=20)  # 学院

    def __str__(self):
        return self.Schname


class Teacher(models.Model):
    Tid = models.IntegerField()  # 教工号
    Tname = models.CharField(max_length=20)  # 教师姓名
    Tpsword = models.CharField(max_length=20)  # 登录密码
    Tschool = models.ForeignKey("School", on_delete=models.DO_NOTHING, null=True, blank=True)  # 学院 外键


class Record(models.Model):
    Rid = models.IntegerField()
    Sid = models.IntegerField()
    Tid = models.IntegerField()
    Aid = models.IntegerField()
    Time = models.DateTimeField()
    astate = models.CharField(max_length=500)
    bstate = models.CharField(max_length=500)
    Rnote = models.CharField(max_length=500)
   

