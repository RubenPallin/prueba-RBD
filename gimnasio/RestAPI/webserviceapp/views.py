from django.shortcuts import render
from django.http import HttpResponse

def prueba_API(request):
  return HttpResponse("<h1>Hola</h1>");
# Create your views here.
