from django.db import models

# Create your models here.

class Grades(models.Model):
    gname = models.CharField(max_length=20)
    gdate = models.DateTimeField()
    ggirlnum = models.IntegerField()
    gboynum = models.IntegerField()
    isDelete =models.BooleanField()
    def __str__(self):
        return "班级：%s "%(self.gname)

class Students(models.Model):

    sname = models.CharField(max_length=20)
    sgender = models.BooleanField(default=False)
    sage = models.IntegerField()
    scontend=models.CharField(max_length=20)
    isDelete = models.BooleanField(default=False)
    sgrade = models.ForeignKey("Grades",on_delete=models.CASCADE)
    def gender(self):
        if self.sgender:
            return "男"
        else:
            return "女"
    def __str__(self):
        return self.sname
