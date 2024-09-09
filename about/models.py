from django.db import models

# Create your models here.
class About(models.Model):
    about_des=models.TextField()

class Image(models.Model):
    about_img=models.FileField(upload_to="faculty/", max_length=120, default="",blank=True,null=True)
class Slogun(models.Model):
    slogun_heading=models.CharField(max_length=100,default="")
    slogun_des=models.TextField()        
