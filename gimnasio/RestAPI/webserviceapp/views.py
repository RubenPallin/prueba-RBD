
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
def reserva_clase(request):
      if not request.session.get('sessionToken'):
        return redirect('/login')
    else:
        headers = {'SessionToken': request.session.get('sessionToken')}
        data = {
            "id": request.POST.get('id'),
            "fecha": request.POST.get('fecha'),
            "horarios": request.POST.get('horarios')
        }
        response = requests.post('http://localhost:8000/calendar/' + str(id), data=data, headers=headers)
        if response.status_code == 401:
            return JsonResponse({'error': 'Invalid session token'})
        elif response.status_code == 400:
            return JsonResponse({'error': 'Error in data sent'})
        else:
            return JsonResponse(response.json())

# Create your views here.
