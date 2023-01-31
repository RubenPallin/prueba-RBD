from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .models import Tclases

def prueba_API(request):
  return HttpResponse("<h1>Hola</h1>");

def obtener_listado_clases(request):
      lista = Tclases.objects.all()
      respuesta_final = []
      for fila_sql in lista:
          diccionario = {}
          diccionario['id'] = fila_sql.id
          diccionario['nombre'] = fila_sql.nombre
          diccionario['horarios'] = fila_sql.horarios
          respuesta_final.append(diccionario)
      return JsonResponse(respuesta_final, safe=False)





# Create your views here.
