from django.db import models

# Create your models here.
class Trainer(models.Model):
    trainer_heading=models.CharField(max_length=100, default="")
    trainer_name=models.CharField(max_length=100,default="")
    trainer_des=models.TextField()
    trainer_img=models.FileField(upload_to="gallery/", max_length=100, default="", blank=True, null=True)