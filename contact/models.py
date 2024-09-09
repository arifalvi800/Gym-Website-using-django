from django.db import models

# Create your models here.
class Contact(models.Model):
    name=models.CharField(max_length=100,default="")
    email=models.EmailField(max_length=40,default="")
    phone=models.CharField(max_length=15,default="")
    subject=models.CharField(max_length=100,default="")
    message=models.TextField()

