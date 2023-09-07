from django.db import models

# Create your models here.

class exercises(models.Model):
    ref_id = models.CharField(max_length=12)
    title =  models.CharField(max_length=100)
    subject = models.CharField(max_length=26)
    max_problem = models.IntegerField()
    perround_problem = models.IntegerField()
    time = models.IntegerField()
    color = models.CharField(max_length=7,null='#D9D9D9')
    image = models.ImageField(upload_to='media/images/exercise_cover_img/',blank=True,default=None)

class shortnote(models.Model):
    name = models.CharField(max_length=50,default=None)
    author = models.CharField(max_length=50)
    subject = models.CharField(max_length=10)
    cover = models.ImageField(upload_to='media/images/shortnote/shortnote_cover',default=None,blank=True)
    description = models.CharField(max_length=500,blank=True)
    time_stamp = models.DateTimeField(auto_now_add=True)

class shortnote_page(models.Model):
    shortnote_id = models.IntegerField()
    page = models.IntegerField()
    image = models.ImageField(upload_to='media/images/shortnote/shortnote_page',default=None,blank=True)
