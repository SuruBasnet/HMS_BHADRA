from django.shortcuts import render
from rest_framework.decorators import api_view
from .models import Invoice
from rest_framework.response import Response
from .serializers import *
from rest_framework.generics import GenericAPIView
from django.shortcuts import get_object_or_404

# Create your views here.
@api_view(['GET','POST'])
def invoice(request):
    if request.method == 'GET':
        queryset = Invoice.objects.all()
        serializer = InvoiceSerializer(queryset,many=True)
        return Response(serializer.data)
    else:
        data = request.data
        serializer = InvoiceSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response('data created!')
        else:
            return Response(serializer.errors)

class InvoiceApiView(GenericAPIView):

    def get(self,request):
        queryset = Invoice.objects.all()
        serializer = InvoiceSerializer(queryset,many=True)
        return Response(serializer.data)
    
    def post(self,request):
        data = request.data
        serializer = InvoiceSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response('data created!')
        else:
            return Response(serializer.errors)
        
class InvoiceIdApiView(GenericAPIView):

    def get_invoice_object(self,pk):
        object = get_object_or_404(Invoice,id=pk)
        return object

    def get(self,request,pk):
        object = self.get_invoice_object(pk)
        serializer = InvoiceSerializer(object)
        return Response(serializer.data)
    
    def put(self,request,pk):
        object = self.get_invoice_object(pk)
        serializer = InvoiceSerializer(object,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response('data updated!')
        else:
            return Response(serializer.errors)
    
    def patch(self,request,pk):
        object = self.get_invoice_object(pk)
        serializer = InvoiceSerializer(object,data=request.data,partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response('data updated!')
        else:
            return Response(serializer.errors)
        
    def delete(self,request,pk):
        object = self.get_invoice_object(pk)
        object.delete()
        return Response('data deleted!')
