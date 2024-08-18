from django.contrib import admin
from django.urls import path
from home import views
from django.conf import settings
from django.conf.urls.static import static

admin.site.site_header="Gym Website"
admin.site.site_title="Gym Website"
admin.site.index_title=" Welcome to Gym Website Portal"

urlpatterns = [
    path('',views.index,name='index'),
    path('about',views.about,name='about'),
    path('programs',views.programs,name='programs'),
    path('trainers',views.trainers,name='trainers'),
    path('contact',views.contact,name='contact')
]

if settings.DEBUG:
    urlpatterns+=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    