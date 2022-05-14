from django.shortcuts import render
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from .serializers import  *
from django.conf import settings
import time
import os
import traceback
# Create your views here.
class UserRegisterView(APIView):
    permission_classes = (AllowAny,)
    serializer_class = UserRegisterSerializer

    def post(self, request):
     
        try:
            user = None
            serializer = self.serializer_class(data=request.data)
            serializer.is_valid(raise_exception=True)
            user = serializer.save()
            status_code = status.HTTP_201_CREATED
            response = {
                'success': 'true',
                'status code': status_code,
                'message': 'User registered successfully',
            }
        except Exception as e:
            print(str(traceback.format_exc()))
            if user!=None:
                user.delete()
            status_code = status.HTTP_400_BAD_REQUEST
            response = {
                'success': 'false',
                'status code': status_code,
                'message': "Something went wrong",
            }
        return Response(response, status=status_code)

class RegisterView(APIView):
    permission_classes = (AllowAny,)
    serializer_class = RegisterSerializer
    def post(self, request):
        try:
            user = None
            serializer = self.serializer_class(data=request.data)
            serializer.is_valid(raise_exception=True)
            user = serializer.save()
            status_code = status.HTTP_201_CREATED
            response = {
                'success': 'true',
                'status code': status_code,
                'message': 'User registered successfully',
            }
        except Exception as e:
            print(str(traceback.format_exc()))
            if user!=None:
                user.delete()
            status_code = status.HTTP_400_BAD_REQUEST
            response = {
                'success': 'false',
                'status code': status_code,
                'message': "Something went wrong",
            }
        return Response(response, status=status_code)

class LoginView(APIView):
    permission_classes = (AllowAny,)
    serializer_class = RegisterSerializer

    def post(self, request):
     
        try:
            user = None
            serializer = self.serializer_class(data=request.data)
            serializer.is_valid(raise_exception=True)
            user = serializer.save()
            status_code = status.HTTP_201_CREATED
            response = {
                'success': 'true',
                'status code': status_code,
                'message': 'User registered successfully',
            }
        except Exception as e:
            print(str(traceback.format_exc()))
            if user!=None:
                user.delete()
            status_code = status.HTTP_400_BAD_REQUEST
            response = {
                'success': 'false',
                'status code': status_code,
                'message': "Something went wrong",
            }
        return Response(response, status=status_code)
    