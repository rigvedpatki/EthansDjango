from rest_framework import serializers
from .models import Question, Option


class QuestionSerializer (serializers.ModelSerializer):
    class Meta:
        fields = ('id', 'question_text', 'pub_date')
        model = Question


class OptionSerializer (serializers.ModelSerializer):
    class Meta:
        fields = ('id', 'question', 'option_text', 'vote_count')
        model = Option
