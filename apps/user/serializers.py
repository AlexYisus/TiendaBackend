from djoser.serializers import UserCreateSerializer as BaseUserCreateSerializer
from rest_framework import serializers
from django.contrib.auth import get_user_model

User = get_user_model()

class UserCreateSerializer(BaseUserCreateSerializer):#validación de datos
    class Meta(BaseUserCreateSerializer.Meta):
        model = User
        fields = (#Djoser procesa los datos
            'id',
            'email',
            'first_name',
            'last_name',
            'password',
            'get_full_name',
            'get_short_name'
        )
