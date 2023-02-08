
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
        if request.method == 'GET':
        session_token = request.headers.get('sessionToken')
        if session_token != 'sessionToken':
            return JsonResponse({'error': 'SessionToken inválido'}, status=401)
        
        # Obtener todos los pedidos de la base de datos
        pedidos = Tpedidos.objects.all()
        
        orders = []
        
        # Iterar sobre cada pedido y agregar la información necesaria al arreglo 'orders'
        for pedido in pedidos:
            items = []
            # Obtener todos los productos relacionados con el pedido actual
            productos = Tproductos.objects.filter(productosid=1)
            # Iterar sobre cada producto y agregar la información necesaria al arreglo 'items'
            for producto in productos:
                item = {
                    "name": producto.descripcion,
                    "quantity": producto.color,
                    "unitPrice": producto.descripcion,
                    "productId": producto.productosid
                }
                items.append(item)
            
            order = {
                "orderDate": pedido.fecha,
                "items": items
            }
            orders.append(order)
        
        return JsonResponse(orders, safe=False)

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
def reserva_clase(request, id):
    persisted_token = request.headers.get('SessionToken')
    if not persisted_token:
        return JsonResponse({'error': 'SessionToken not found'}, status=401)

    try:
        # Get calendar data with id=id
        calendar = Calendar.objects.get(id=id)
    except Calendar.DoesNotExist:
        return JsonResponse({'error': 'Calendar not found'}, status=400)

    # Validate SessionToken
    # ...

    # Update calendar data
    data = json.loads(request.body)
    calendar.fecha = data['fecha']
    calendar.horarios = data['horarios']
    calendar.save()

    return JsonResponse({'status': 'success'})

# Create your views here.
