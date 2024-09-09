from django.shortcuts import render,HttpResponse
from about.models import About
from contact.models import Contact
from about.models import Image
from about.models import Slogun
from program.models import Program
from trainer.models import Trainer
# Create your views here.
def index(request):   
    return render(request,'index.html')
def about(request):
    AboutData=About.objects.all()
    ImageData=Image.objects.all()
    SlogunData=Slogun.objects.all()
    data={
        'ImageData':ImageData,
        'AboutData': AboutData,
        'SlogunData': SlogunData,   
    }
    return render(request,'about.html',data)
def programs(request):
    ProgramData=Program.objects.all()
    data={
        'ProgramData':ProgramData
    }
    return render(request,'programs.html',data)
def trainers(request):
    TrainerData=Trainer.objects.all()
    data={
        'TrainerData':TrainerData
    }
    return render(request,'trainers.html',data)
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