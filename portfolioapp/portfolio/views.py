from django.shortcuts import render
from django.http.response import HttpResponse
from portfolio.models import About,Skill,Experience

# Create your views here.


def home(request):
    context={
        "about": About.objects.get(),
        "skills": Skill.objects.all(),
        "experiences":Experience.objects.all(),
    }
    
    return render(request,'index.html',context)
