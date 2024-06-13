from django.shortcuts import render
from .models import Producto
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from .serializers import ProductoSerializer


# Create your views here.


class ProductoviewSet(viewsets.ModelViewSet):
    queryset = Producto.objects.all()
    serializer_class = ProductoSerializer

    @action(detail=False, methods=['post'], url_path='crear_producto')
    def crear_producto(self, request):
        serializer = ProductoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response('ok, producto guardado correctamente', status=201)
        return Response(serializer.errors, status=400)

    @action(detail=False, methods=['put'], url_path='editar_producto/(?P<id_producto>\d+)/?')
    def editar_producto(self, request, id_producto=None):
        producto = Producto.objects.filter(id=id_producto).first()
        if not producto:
            return Response('Producto no encontrado', status=404)
        serializer = self.get_serializer(
            producto, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response('Producto actualizado correctamente', status=200)
        return Response(serializer.errors, status=400)

    @action(detail=False, methods=['delete'], url_path='eliminar_producto/(?P<id_producto>\d+)/?')
    def eliminar_producto(self, request, id_producto=None):
        producto = Producto.objects.filter(id=id_producto).first()
        if not producto:
            return Response('Producto no encontrado', status=404)
        producto.delete()
        return Response('Producto eliminado correctamente', status=204)


# endpoints:

# obtener todos los productos:
# GET http://localhost:8000/productos/

# obtener un producto especifico
# GET http://localhost:8000/productos/id/

# crear producto nuevo
# POST http://localhost:8000/productos/crear_producto/
    # enviar información:
    # {"nombre": "producto 1",
    #  "precio": 100,
    #  "descripcion": "descripción del producto"
    #  }

# editar Producto
# PUT http://localhost:8000/productos/editar_producto/{id}/
     # {"nombre": "producto editado"
    #  }

# eliminar Producto
# DELETE http://localhost:8000/productos/eliminar_producto/{id}/
