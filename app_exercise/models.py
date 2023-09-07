from django.db import models
from app_general.models import exercises
from django.contrib.auth.models import User
# Create your models here.

class exam(models.Model):
    ref_id = models.CharField(max_length=12 , null=True ,) 
    problem_text = models.CharField(max_length=200)
    choice1 = models.CharField(max_length=30)
    c_id1 = models.IntegerField(null=1)
    choice2 = models.CharField(max_length=30)
    c_id2 = models.IntegerField(null=2)
    choice3 = models.CharField(max_length=30)
    c_id3 = models.IntegerField(null=3)
    choice4 = models.CharField(max_length=30)
    c_id4 = models.IntegerField(null=4)
    correct_c_id = models.IntegerField()
    solution = models.ImageField(upload_to='media/images/solution/',default=None,blank=True)

class exercise_result(models.Model):
    doing_at = models.DateTimeField(auto_now_add=True)
    ref_id = models.CharField(max_length=12 , null=True ,)
    title =  models.CharField(max_length=100,null=True)
    subject = models.CharField(max_length=26,null=True)
    user_id = models.IntegerField(null=False,default=None)
    max_point = models.IntegerField(null=True)
    total_point = models.IntegerField(null=True)

class result(models.Model):
    doing_at = models.DateTimeField()
    user_id = models.IntegerField(null=False,default=0)
    number = models.IntegerField(null=True)
    problem_text = models.CharField(max_length=60)
    choose = models.IntegerField(null=True)
    correct_c_id = models.IntegerField(null=True)
    status = models.IntegerField(default=2,null=True)
