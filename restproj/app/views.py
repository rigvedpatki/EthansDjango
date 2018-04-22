from django.shortcuts import render
from rest_framework import viewsets
from app.models import University, Student
from app.serializers import UniversitySerializer, StudentSerializer

# Create your views here.


class StudentViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer


class UniversityViewSet(viewsets.ModelViewSet):
    queryset = University.objects.all()
    serializer_class = UniversitySerializer
