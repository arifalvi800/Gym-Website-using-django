from django.contrib import admin
from trainer.models import Trainer
# Register your models here.
class TrainerData(admin.ModelAdmin):
    list_display=['trainer_name','trainer_heading']
    ordering=('id',)
admin.site.register(Trainer,TrainerData)