from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Hobby
from .forms import HobbyForm
from django.template import loader


# Create your views here.
def index(request):
    hobby_list = Hobby.objects.all()
    #    template = loader.get_template('hobbies/index.html')
    context = {
        'hobby_list': hobby_list,
    }
    return render(request, 'hobbies/index.html', context)
    # return HttpResponse(template.render(context, request))


def item(request):
    return HttpResponse('<h1>This is an item view</h1>')


def detail(request, hobby_id):
    hobby = Hobby.objects.get(pk=hobby_id)
    context = {
        'hobby': hobby
    }
    return render(request, 'hobbies/detail.html', context)
