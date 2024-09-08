from django.shortcuts import render,HttpResponse
from about.models import About
from contact.models import Contact
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
    if request.method=="POST":
        name=request.POST.get('name')
        email=request.POST.get('email')
        phone=request.POST.get('phone')
        subject=request.POST.get('subject')
        message=request.POST.get('message')
        contact=Contact(name=name,email=email,phone=phone,subject=subject,message=message)
        contact.save()
    return render(request,'contact.html')