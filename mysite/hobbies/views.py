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

def create_hobby(request):
    form = HobbyForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect('hobbies:index')
    return render(request, 'hobbies/hobby-form.html', {'form':form})

def update_hobby(request, id):
    hobby = Hobby.objects.get(id=id)
    form = HobbyForm(request.POST or None, instance=hobby)

    if form.is_valid():
        form.save()
        return redirect('hobbies:index')
    return render(request, 'hobbies/hobby-form.html',{'form':form, 'hobby':hobby})

def delete_hobby(request, id):
    hobby=Hobby.objects.get(id=id)
    if request.method == 'POST':
        hobby.delete()
        return redirect('hobbies:index')
    return render(request, 'hobbies/hobby-delete.html', {'hobby':hobby})