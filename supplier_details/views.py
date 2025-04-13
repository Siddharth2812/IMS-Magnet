from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Supplier
from django.shortcuts import get_object_or_404
from django.core.serializers import serialize
import json

# Create your views here.

@api_view(['GET', 'POST'])
def supplier_list(request):
    if request.method == 'GET':
        suppliers = Supplier.objects.all()
        data = json.loads(serialize('json', suppliers))
        return Response(data)
    
    elif request.method == 'POST':
        try:
            supplier = Supplier.objects.create(**request.data)
            data = json.loads(serialize('json', [supplier]))[0]
            return Response(data, status=status.HTTP_201_CREATED)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def supplier_detail(request, pk):
    supplier = get_object_or_404(Supplier, pk=pk)
    
    if request.method == 'GET':
        data = json.loads(serialize('json', [supplier]))[0]
        return Response(data)
    
    elif request.method == 'PUT':
        try:
            for key, value in request.data.items():
                setattr(supplier, key, value)
            supplier.save()
            data = json.loads(serialize('json', [supplier]))[0]
            return Response(data)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)
    
    elif request.method == 'DELETE':
        try:
            supplier.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)
