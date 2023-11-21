from django.shortcuts import render
from rest_framework.decorators import api_view, permission_classes
from .models import Invoice
from rest_framework.response import Response
from .serializers import *
from rest_framework.generics import GenericAPIView
from django.shortcuts import get_object_or_404
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from django.contrib.auth import authenticate
from rest_framework.authtoken.models import Token
from core.permissions import CustomModelPermission
from django.contrib.auth.hashers import make_password

# Create your views here.
# @api_view(['GET','POST'])
# def invoice(request):
#     if request.method == 'GET':
#         queryset = Invoice.objects.all()
#         serializer = InvoiceSerializer(queryset,many=True)
#         return Response(serializer.data)
#     else:
#         data = request.data
#         serializer = InvoiceSerializer(data=data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response('data created!')
#         else:
#             return Response(serializer.errors)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def logout(request):
    request.user.auth_token.delete() # Reverse access and token related with the user is being queried and deleted
    return Response('Logout successfully!')

@api_view(['POST'])
def login(request):
    email = request.data.get('email')
    password = request.data.get('password')
    user = authenticate(username=email,password=password)
    if user == None:
        return Response('Email or Password is Invalid!')
    else:
        token , _ = Token.objects.get_or_create(user=user)
        return Response(token.key)

@api_view(['POST'])
@permission_classes([IsAuthenticated,IsAdminUser])
def register(request):
    email = request.data.get('email')
    password = request.data.get('password')
    hash_password = make_password(password)
    User.objects.create(email=email,password=hash_password)
    return Response('User created!')

class InvoiceApiView(GenericAPIView):
    queryset_model = Invoice
    permission_classes = [IsAuthenticated,CustomModelPermission]

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

    permission_classes = [IsAuthenticated]

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
