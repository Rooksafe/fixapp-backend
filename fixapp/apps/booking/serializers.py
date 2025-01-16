from rest_framework import serializers
from .models import User, Category, Professional, Client, Job, Application

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'role']

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name']

class ProfessionalSerializer(serializers.ModelSerializer):
    user = UserSerializer()

    class Meta:
        model = Professional
        fields = ['id', 'user', 'bio', 'category', 'is_verified', 'verification_status']

class ClientSerializer(serializers.ModelSerializer):
    user = UserSerializer()

    class Meta:
        model = Client
        fields = ['id', 'user', 'phone']

class JobSerializer(serializers.ModelSerializer):
    client = ClientSerializer()

    class Meta:
        model = Job
        fields = ['id', 'client', 'title', 'description', 'created_at', 'is_open']

class ApplicationSerializer(serializers.ModelSerializer):
    job = JobSerializer()
    professional = ProfessionalSerializer()

    class Meta:
        model = Application
        fields = ['id', 'job', 'professional', 'message', 'created_at']
