from django.shortcuts import render
from rest_framework import generics
from .models import Category, Professional, Client, Job, Application
from .serializers import (
    CategorySerializer,
    ProfessionalSerializer,
    ClientSerializer,
    JobSerializer,
    ApplicationSerializer,
)

class CategoryListView(generics.ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class ProfessionalListView(generics.ListAPIView):
    queryset = Professional.objects.filter(is_verified=True)
    serializer_class = ProfessionalSerializer

class JobListView(generics.ListCreateAPIView):
    queryset = Job.objects.all()
    serializer_class = JobSerializer

class JobDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Job.objects.all()
    serializer_class = JobSerializer

class ApplicationListView(generics.ListCreateAPIView):
    queryset = Application.objects.all()
    serializer_class = ApplicationSerializer