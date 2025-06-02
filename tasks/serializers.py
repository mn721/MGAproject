# filepath: c:\Users\Lenovo\Desktop\MGA\tasks\serializers.py
from rest_framework import serializers
from .models import Task, TaskHistory
from django.contrib.auth.models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username']

class TaskSerializer(serializers.ModelSerializer):
    assigned_user = serializers.SlugRelatedField(
        queryset=User.objects.all(),
        slug_field='username',
        required=False,
        allow_null=True
    )

    class Meta:
        model = Task
        fields = '__all__'

class TaskHistorySerializer(serializers.ModelSerializer):
    changed_by = serializers.SlugRelatedField(
        queryset=User.objects.all(),
        slug_field='username',
        required=False,
        allow_null=True
    )

    class Meta:
        model = TaskHistory
        fields = '__all__'

class UserRegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ['username', 'password']

    def create(self, validated_data):
        user = User.objects.create_user(
            username=validated_data['username'],
            password=validated_data['password']
        )
        return user