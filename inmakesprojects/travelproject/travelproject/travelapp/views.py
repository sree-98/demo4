
from django.http import HttpResponse
from django.shortcuts import render
from . models import Place
from . models import people

# Create your views here.
def demo(request):
    obj = Place.objects.all()
    obj1 = people.objects.all()
    return render(request, "index.html", {'result': obj, 'result1': obj1})



