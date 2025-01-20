from rest_framework import serializers
from .models import User, Category, Professional, Client, Job, Apply, Booking
from django.utils.timezone import now


class BookingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Booking
        fields = '__all__'
        read_only_fields = ['created_at']

    def validate(self, data):
        if self.instance and self.instance.status in ['confirmed', 'rejected', 'cancelled']:
            raise serializers.ValidationError("No se puede modificar una reserva ya confirmada, rechazada o cancelada.")
        return data

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

class ApplySerializer(serializers.ModelSerializer):
    job = JobSerializer()
    professional = ProfessionalSerializer()

    class Meta:
        model = Apply
        fields = ['id', 'job', 'professional', 'message', 'created_at']
