from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .models import Tclases, Tpedidos

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
          diccionario['imagen'] = fila_sql.imagen
          respuesta_final.append(diccionario)
      return JsonResponse(respuesta_final, safe=False)

def obtener_listado_pedidos(request):
        lista2 = Tpedidos.objects.all()
        respuesta_final = []
        for fila_sql in lista2:
            diccionario = {}
            diccionario['id'] = fila_sql.id
	    diccionario['fecha'] = fila_sql.fecha
            diccionario['cantidad'] = fila_sql.cantidad
            respuesta_final.append(diccionario)
        return JsonResponse(respuesta_final, safe=False)

# Create your views here.
