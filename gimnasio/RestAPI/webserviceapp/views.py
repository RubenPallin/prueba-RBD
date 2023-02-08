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
        session_token = request.headers.get('SessionToken')
        if session_token != 'ASDFASDF':
            return JsonResponse({'error': 'Unauthorized'}, status=401)
        orders = [
            {
                "orderDate": "2022-12-12T14:50:50Z",
                "items": [
                    {
                        "name": "Pantalón",
                        "quantity": 1,
                        "unitPrice": 16.99,
                        "productId": 44
                    }
                ]
            },
            {
                "orderDate": "2023-01-12T16:50:50Z",
                "items": [
                    {
                        "name": "Guantes de boxeo",
                        "quantity": 3,
                        "unitPrice": 12.99,
                        "productId": 21
                    }
                ]
            },
        ]

        return JsonResponse({'orders': orders}, status=200)

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
