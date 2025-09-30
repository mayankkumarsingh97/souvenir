from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect, HttpResponse, JsonResponse
from django.shortcuts import render
from django.shortcuts import render, redirect
from . models import Catalog

# Create your views here.
def home(request):
    Cat=Catalog.objects.all()    
    context = {
        'Cat':Cat,
    }
    return render(request, "index.html",context)

def online_support(request):
    Cat=Catalog.objects.all()
    context = {
        'Cat':Cat,
    }
    return render(request, "thankyou.html",context)

def aboutus(request):
    Cat=Catalog.objects.all()    
    context = {
        'Cat':Cat,
    }
    return render(request, "aboutus.htm",context)




 

   

