from rest_framework import serializers
from django.contrib.auth.models import User

class UserSerializer(serializers.ModelSerializer):

    type = serializers.CharField(max_length=200, required=False, default='user.users')
    event = serializers.CharField(max_length=200, required=False, default="Nuevo usuario!") 

    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'groups', 'type', 'event']

