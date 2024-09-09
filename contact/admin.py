from django.contrib import admin
from contact.models import Contact
# Register your models here.
class ContactData(admin.ModelAdmin):
    list_display=['name','email','phone']
    ordering=('id',)
admin.site.register(Contact,ContactData)



