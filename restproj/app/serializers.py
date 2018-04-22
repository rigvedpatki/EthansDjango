from rest_framework import serializers
from app.models import University, Student


class UniversitySerializer(serializers.ModelSerializer):
    class Meta:
        model = University
        exclude = ()


class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        exclude = ()
