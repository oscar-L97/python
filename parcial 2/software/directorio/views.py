from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import software, depa
from .forms import RawSwForm, RawDeptForm
# Create your views here.
def index(request):

    todo = software.objects.all()

    context = {
        'titulo': 'Todo el Software',
        'todo': todo
    }

    return render(request, 'directorio/index.html', context)

def nuevo_dept(request):
    form = RawDeptForm()
    if request.method == "POST":
        form = RawDeptForm(request.POST)
        if form.is_valid():
            depa.objects.create(**form.cleaned_data)
            return HttpResponseRedirect('/directorio/')
        else:
            print(form.errors)
    context = {
        "form": form
    }
    return render(request, "directorio/nuevo_dept.html", context)

def index_filter(request, nombre):
    soft_filt = software.objects.filter(departamento=nombre)

    context = {
        'titulo': nombre+" Software",
        'swpkgs': soft_filt
    }

    return render(request, 'directorio/index.html', context)

def details(request, id):
    soft = software.objects.get(id=id)

    context = {
        'soft': soft
    }

    return render(request, 'directorio/details.html', context)

def nuevo_soft(request):
    form = RawSwForm()
    if request.method == "POST":
        form = RawSwForm(request.POST)
        if form.is_valid():
            software.objects.create(**form.cleaned_data)
            return HttpResponseRedirect('/directorio/')
        else:
            print(form.errors)
    context = {
        "form": form
    }
    return render(request, "directorio/nuevo_soft.html", context)
