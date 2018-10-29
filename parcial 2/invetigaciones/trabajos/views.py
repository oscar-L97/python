from django.shortcuts import render
from .models import Trabajo
from .forms import DocumentForm
from django.views import generic
# Create your views here.

def index(request):
    context={
    "mensaje": "hola k ase",
    }
    return render(request,"tweets/index.html",context)

class Create(generic.CreateView):
    template_name = "trabajo/create.html"
    model = Trabajo
    fields = ["documento","categoria","titulo","autor"]
    success_url = "/allList/"

class AllList(generic.ListView):
    template_name = "trabajo/allList.html"
    model = Trabajo

class ListComp(generic.ListView):
    template_name = "trabajo/ListComp.html"
    model = Trabajo

class ListMed(generic.ListView):
    template_name = "trabajo/ListMed.html"
    model = Trabajo

class ListNat(generic.ListView):
    template_name = "trabajo/ListNat.html"
    model = Trabajo

class ListSoc(generic.ListView):
    template_name = "trabajo/ListSoc.html"
    model = Trabajo

class ListTierra(generic.ListView):
    template_name = "trabajo/ListTierra.html"
    model = Trabajo

class UpdateTrabajo(generic.UpdateView):
    template_name = "trabajo/update.html"
    model = Trabajo
    fields = ["categoria","titulo", "autor"]
    success_url = "/allList/"

class DeleteTrabajo(generic.DeleteView):
    template_name = "trabajo/delete.html"
    model = Trabajo
    success_url = "/allList/"
