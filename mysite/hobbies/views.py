from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Hobby
from .forms import HobbyForm
from django.template import loader


# Create your views here.
def index(request):
    hobby_list= Hobby.objects.all()
    context={
        'hobby_list':hobby_list,
    }
    return render(request,'hobbies/index.html', context)

