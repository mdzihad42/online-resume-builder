from django.db import models
from django.contrib.auth.models import AbstractUser


class userModel(AbstractUser):
    def __str__(self):
        return self.username
    
class profileModel(models.Model):
    full_name=models.CharField(max_length=100,null=True)
    phone=models.CharField(max_length=30,null=True)
    address=models.TextField(null=True)
    profile_pic=models.ImageField(upload_to='media/img', blank=True, null=True)
    created_by=models.OneToOneField(userModel,on_delete=models.CASCADE , null=True,related_name='profile_info')
    
    def __str__(self):
        return self.full_name
    
class projectModel(models.Model):
    project_name=models.CharField(max_length=100,null=True)
    description=models.TextField(null=True)
    completed_date=models.DateField(null=True)
    created_by=models.ForeignKey(userModel,on_delete=models.CASCADE,null=True)
    
    def __str__(self):
        return self.project_name

class workExModel(models.Model):
    company_name=models.CharField(max_length=100,null=True)
    designation=models.CharField(max_length=100,null=True)
    start_date=models.DateField(null=True)
    end_date=models.DateField(null=True)
    created_by=models.ForeignKey(userModel,on_delete=models.CASCADE,null=True)
    
    def __str__(self):
        return self.company_name
    
class EduModel(models.Model):
    degree=models.CharField(max_length=100,null=True)
    institute=models.CharField(max_length=100,null=True)
    grade=models.CharField(max_length=20,null=True)
    passing_year=models.DateField(null=True)
    created_by=models.ForeignKey(userModel,on_delete=models.CASCADE,null=True)
    
    def __str__(self):
        return self.created_by.username
    
    