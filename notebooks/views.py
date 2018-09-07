from django.shortcuts import render
from django.http import HttpResponse

from .models import Notebook
# Create your views here.

def index(request):
    return HttpResponse("Notebooks view.")


# using only django
def detail(request, notebook_id):
    notebook = Notebook.objects.get(pk = notebook_id)
    return HttpResponse("You're looking at notebook %s." % notebook.description)