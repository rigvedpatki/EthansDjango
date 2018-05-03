from django.shortcuts import render
from .models import Question, Option
from .serializers import QuestionSerializer, OptionSerializer
from rest_framework import viewsets, generics
# Create your views here.


class QuestionViewSet (viewsets.ModelViewSet):
    queryset = Question.objects.all()  # pylint: disable
    serializer_class = QuestionSerializer


class OptionViewSet (viewsets.ModelViewSet):
    queryset = Option.objects.all()
    serializer_class = OptionSerializer

    def get_queryset(self):
        queryset = Option.objects.all()
        question = self.request.query_params.get('question', None)
        if question is not None:
            queryset = queryset.filter(question=question)
        return queryset


""" 
class OptionViewList (generics.ListAPIView):
    serializer_class = OptionSerializer

    def get_queryset(self):
        queryset = Option.objects.all()
        question = self.request.query_params.get('question', None)
        if question is not None:
            queryset = queryset.filter(option__question=question)
        return queryset """
