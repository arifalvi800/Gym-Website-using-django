from django.db import models

# Create your models here.
class Program(models.Model):
    program_heading=models.CharField(max_length=100, default="")
    program_des=models.TextField()
    program_img=models.FileField(upload_to="gallery/", max_length=100, default="", blank=True, null=True)
