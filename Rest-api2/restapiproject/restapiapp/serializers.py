from rest_framework import serializers
from .models import loginmodel
class loginSerializer(serializers.ModelSerializer):
    class Meta:
        model=loginmodel
        fields=('username','password')