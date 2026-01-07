from django.shortcuts import render

# Create your views here.
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

import uuid

# Simulación de base de datos local en memoria
data_list = []

# Añadiendo algunos datos de ejemplo para probar el GET
data_list.append({'id': str(uuid.uuid4()), 'name': 'User01', 'email': 'user01@example.com', 'is_active': True})
data_list.append({'id': str(uuid.uuid4()), 'name': 'User02', 'email': 'user02@example.com', 'is_active': True})
data_list.append({'id': str(uuid.uuid4()), 'name': 'User03', 'email': 'user03@example.com', 'is_active': False}) # Ejemplo de item inactivo

class DemoRestApi(APIView):
    name = "Demo REST API"

    def get(self, request):

    # Filtra la lista para incluir solo los elementos donde 'is_active' es True
        active_items = [item for item in data_list if item.get('is_active', False)]
        return Response(active_items, status=status.HTTP_200_OK)

    def post(self, request):
      data = request.data

      # Validación mínima
      if 'name' not in data or 'email' not in data:
         return Response({'error': 'Faltan campos requeridos.'}, status=status.HTTP_400_BAD_REQUEST)

      data['id'] = str(uuid.uuid4())
      data['is_active'] = True
      data_list.append(data)

      return Response({'message': 'Dato guardado exitosamente.', 'data': data}, status=status.HTTP_201_CREATED)


class DemoRestApiItem(APIView):
    name = "Demo REST API Item"

    def put(self, request, id):

        data = request.data

        if 'id' not in data:
            return Response(
                {'error': 'El identificador (id) es obligatorio en el cuerpo de la solicitud.'},
                status=status.HTTP_400_BAD_REQUEST
            )

        # Buscar el elemento por id
        item = next((item for item in data_list if item['id'] == id), None)

        if item is None:
            return Response(
                {'error': f'Elemento con id {id} no encontrado.'},
                status=status.HTTP_404_NOT_FOUND
            )

        # Validar campos requeridos
        if 'name' not in data or 'email' not in data:
            return Response(
                {'error': 'Faltan campos requeridos: name, email.'},
                status=status.HTTP_400_BAD_REQUEST
            )

        # Reemplazar completamente los datos, manteniendo el id original
        item['name'] = data['name']
        item['email'] = data['email']
        item['is_active'] = data.get('is_active', True)

        return Response(
            {'message': 'Elemento actualizado completamente.', 'data': item},
            status=status.HTTP_200_OK
        )

    def patch(self, request, id):
        """
        Actualiza parcialmente los campos del elemento.
        Solo modifica los campos proporcionados, manteniendo los demás.
        """
        data = request.data

        # Buscar el elemento por id
        item = next((item for item in data_list if item['id'] == id), None)

        if item is None:
            return Response(
                {'error': f'Elemento con id {id} no encontrado.'},
                status=status.HTTP_404_NOT_FOUND
            )

        # Actualizar solo los campos proporcionados
        if 'name' in data:
            item['name'] = data['name']
        if 'email' in data:
            item['email'] = data['email']
        if 'is_active' in data:
            item['is_active'] = data['is_active']

        return Response(
            {'message': 'Elemento actualizado parcialmente.', 'data': item},
            status=status.HTTP_200_OK
        )

    def delete(self, request, id):
        """
        Elimina lógicamente un elemento marcándolo como inactivo.
        """
        # Buscar el elemento por id
        item = next((item for item in data_list if item['id'] == id), None)

        if item is None:
            return Response(
                {'error': f'Elemento con id {id} no encontrado.'},
                status=status.HTTP_404_NOT_FOUND
            )

        # Eliminación lógica: marcar como inactivo
        item['is_active'] = False

        return Response(
            {'message': 'Elemento eliminado lógicamente.', 'data': item},
            status=status.HTTP_200_OK
        )