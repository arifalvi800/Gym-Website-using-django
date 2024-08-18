from django.shortcuts import render,HttpResponse
from about.models import About
# Create your views here.
def index(request):   
    return render(request,'index.html')
def about(request):
    AboutData=About.objects.all()
    data={
        'AboutData': AboutData,   
    }
    return render(request,'about.html',data)
def programs(request):
    return render(request,'programs.html')
def trainers(request):
    return render(request,'trainers.html')
def contact(request):
    return render(request,'contact.html')