from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .models import Tclases, Tpedidos, Tproductos
from django.views.decorators.csrf import csrf_exempt
import json

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
      pedido = Tpedidos.objects.all()
      resultado = []
      for fila_sql in pedido:
          productos = Tproductos.objects.all()
          lista_productos = []
      for fila_sql in productos:
          diccionario = {}
          diccionario['id'] = fila_productos_sql.id
          diccionario['nombre'] = fila_prodyctos_sql.nombre
          diccionario['cantidad'] = fila_productos_sql.cantidad
          diccionario['color'] = fila_productos_sql.color
          lista_pedidos.append(diccionario)
      resultado.append({
          'id': pedido.id,
          'fecha': pedido.fecha,
          'items': lista_productos
                  })
      return JsonResponse(resultado, json_dumps_params={'ensure_ascii': False})

@csrf_exempt
def reserva_clase(request):
      if request.method != 'POST':
              return HttpResponse(status=405)

      json_peticion = json.loads(request.body)
      clase = Tclases()
      clase.id = json_peticion['1']
      clase.horarios = json_peticion['2023-01-10 18:00']
      if not clase.id or not clase.horario:
         return JsonResponse({"error": "faltan datos"})
      clase.save()
      return JsonResponse({"status": "ok"})

# Create your views here.
