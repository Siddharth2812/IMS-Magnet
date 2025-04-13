from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import MasterMaterial
from supplier_details.models import Supplier
from django.shortcuts import get_object_or_404
from django.core.serializers import serialize
import json

# Create your views here.

@api_view(['GET', 'POST'])
def material_list(request):
    if request.method == 'GET':
        materials = MasterMaterial.objects.all()
        data = json.loads(serialize('json', materials))
        return Response(data)
    
    elif request.method == 'POST':
        try:
            data = request.data.copy()
            # Get the supplier instance
            vendor_id = data.pop('vendor', None)
            if vendor_id is None:
                return Response({'error': 'vendor field is required'}, status=status.HTTP_400_BAD_REQUEST)
            
            supplier = get_object_or_404(Supplier, pk=vendor_id)
            
            # Create material with supplier instance
            material = MasterMaterial.objects.create(vendor=supplier, **data)
            response_data = json.loads(serialize('json', [material]))[0]
            return Response(response_data, status=status.HTTP_201_CREATED)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def material_detail(request, pk):
    material = get_object_or_404(MasterMaterial, pk=pk)
    
    if request.method == 'GET':
        data = json.loads(serialize('json', [material]))[0]
        return Response(data)
    
    elif request.method == 'PUT':
        try:
            data = request.data.copy()
            # Handle vendor update if present
            vendor_id = data.pop('vendor', None)
            if vendor_id is not None:
                supplier = get_object_or_404(Supplier, pk=vendor_id)
                material.vendor = supplier
            
            for key, value in data.items():
                setattr(material, key, value)
            material.save()
            response_data = json.loads(serialize('json', [material]))[0]
            return Response(response_data)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)
    
    elif request.method == 'DELETE':
        try:
            material.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)
