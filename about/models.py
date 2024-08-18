from django.db import models

# Create your models here.
class About(models.Model):
    about_des=models.TextField()
    about_img=models.FileField(upload_to='about/',max_length=250, default="", blank=True, null=True)
