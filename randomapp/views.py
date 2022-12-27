from django.shortcuts import render
from randomapp.models import Random
# Create your views here.
def home(request):
    random  = Random.objects.all()
    context = {
        'random' : random,
    }
    return render(request,'home.html',context)