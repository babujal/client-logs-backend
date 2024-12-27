from .models import ClientLogs
from rest_framework import serializers
from django.contrib.auth.models import User

class ClientLogsSerializers(serializers.HyperlinkedModelSerializer):
    user=serializers.ReadOnlyField(source='user.username')
    class Meta:
        model=ClientLogs
        fields = '__all__'

class UserSerializers(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    class Meta:
        model=User
        fields=['username', 'password']
    def create(self, validated_data):
        user=User.objects.create_user(
            username=validated_data['username'],
            password=validated_data['password']
        )
        return user