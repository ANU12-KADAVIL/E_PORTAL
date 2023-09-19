from django.db import models

# Create your models here.
class Student(models.Model):
    std_id=models.IntegerField()
    std_name=models.CharField(max_length=250,default=False)
    attendance=models.CharField(max_length=250)
    mark=models.CharField(max_length=250)
    
class Faculty(models.Model):
    tec_id=models.IntegerField()
    tec_name=models.CharField(max_length=250,default=False)
    subject=models.CharField(max_length=250)
    salary=models.CharField(max_length=250)
    
class Attendance(models.Model):
    std_name=models.CharField(max_length=250,default=False) 
    attendance=models.CharField(max_length=250)
    check_attendance=models.BooleanField(default=False)
    
class Leave(models.Model):
    std_name=models.CharField(max_length=250,default=False) 
    leave=models.CharField(max_length=250)
    sanction_leave=models.BooleanField(default=False)