from django.contrib import admin
from program.models import Program
# Register your models here.
class ProgramData(admin.ModelAdmin):
    list_display=['program_heading']
    ordering=('id',)
admin.site.register(Program,ProgramData)
