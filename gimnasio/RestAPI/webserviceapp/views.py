
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
<<<<<<< HEAD
	pedidos = Tpedidos.objects.all()
	respuesta_final = []
	for pedido in pedidos:
		diccionario = {}
		diccionario['fecha'] = pedido.fecha
		diccionario['cantidad'] = pedido.cantidad
	productos = Tproductos.objects.all()
	for producto in productos:
		diccionario = {}
		diccionario['nombre'] = producto.nombre
		diccionario['color'] = producto.color
		diccionario['precio'] = producto.precio
		respuesta_final.append(diccionario)
	return JsonResponse(respuesta_final, safe=False)
=======
        session_token = request.headers.get('SessionToken')
        if session_token != 'ASDFASDF':
            return JsonResponse({'error': 'Unauthorized'}, status=401)
        pedidos = [
            {
                "fecha": "2022-12-12T14:50:50Z",
                "items": [
                    {
                        "nombre": "Pantalón",
                        "cantidad": 1,
                        "precio": 16.99,
                        "productosId": 44
                    }
                ]
            },
            {
                "fecha": "2023-01-12T16:50:50Z",
                "items": [
                    {
                        "nombre": "Guantes de boxeo",
                        "cantidad": 3,
                        "precio": 12.99,
                        "productosId": 21
                    }
                ]
            },
        ]

        return JsonResponse({'pedidos': pedidos}, status=200)
>>>>>>> b50bab55b5e3e48b2ad2cb0feb713f8cd77b786a

@csrf_exempt
def get_clases(request, id_clase):
	if request.method == 'GET':
		lista = Tclases.objects.get(id = id_clase)
		respuesta_final = {
			"id": lista.id,
			"nombre": lista.nombre,
			"imagen": lista.imagen,
			"horarios": lista.horarios
}
		return JsonResponse(respuesta_final, safe=False)

@csrf_exempt
def reserva_clase(request):
      if request.method != 'POST':
              return HttpResponse(status=405)
      json_peticion = json.loads(request.body)
      clase = Tclases()
      clase.id = fila_sql.id
      clase.fecha = fila_sql.fecha
      clase.horarios = fila_sql.horarios
      if None in (id, horarios):
         return JsonResponse({"error": "faltan datos"})

      clase.save()
      return JsonResponse({"status": "ok"})

# Create your views here.
