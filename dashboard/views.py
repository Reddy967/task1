from django.shortcuts import render, redirect
from .models import *
from django.db.models import Q
# Create your views here.
def dashboard(request):
    details = City.objects.filter()
    return render(request, 'dashboard.html', {'value':details})

def dashboard_delete(request,id):
    data = City.objects.filter(id=id).delete()
    return()

def country(request):
    details = Country.objects.filter()
    return render(request, 'country.html', {'value':details})

def Country_language(request):
    details = Countrylanguage.objects.filter()
    return render(request, 'Country_language.html', {'value':details})

def index(request):
    search_value = request.GET.get('search')
    if search_value:
        details = Country.objects.filter(Q(name__icontains=search_value) & Q(continent__icontains=search_value))
        return redirect('country')
    else:
        details = Country.objects.all()

    return render(request, 'index.html', {'value':details})

def search(request):
    return()