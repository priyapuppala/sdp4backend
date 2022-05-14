from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework import serializers
from django.contrib.auth import authenticate
from django.contrib.auth.models import update_last_login
from .models import *

class UserRegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User1
        fields = ('username', 'email','phone','subject','message')
        # extra_kwargs = {'password': {'write_only': True}}

class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = registerdata
        fields = "__all__"
