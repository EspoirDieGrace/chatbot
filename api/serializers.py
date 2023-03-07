from rest_framework import serializers
from .models import User, UserType, Materiel
from django.db import models

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model=User
        fields = ('__all__')


class UsertypeSerializer(serializers.Serializer):
    usertypeLib=serializers.CharField(max_length=30)
    usertypedesc=serializers.CharField(max_length=200)
    usertypedatecreation = serializers.DateTimeField()
    class Meta:
        model=UserType
        fields = ('usertypeLib','usertypedesc','usertypedatecreation')

class MaterielSerializer(serializers.ModelSerializer):
    class Meta:
        model=Materiel
        fields = ('__all__')