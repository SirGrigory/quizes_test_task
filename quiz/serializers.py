from rest_framework import serializers
from django.core.exceptions import ValidationError
from .models import Quiz, Question, Answer, Choice


class QuizListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Quiz
        fields = '__all__'


class ChoiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Choice
        fields = ('id', 'text')


class QuestionListSerializer(serializers.ModelSerializer):
    # choice = ChoiceSerializer(many=True, read_only=True)
    choice = serializers.StringRelatedField(many=True)
 

    class Meta:
        model = Question
        fields = ('id', 'text', 'q_type', 'choice')


class AnswerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Answer
        fields = '__all__'
        
    def create(self,validated_data):
        if not (validated_data.get('answer_text') or validated_data.get('answer_choice')):
            raise ValidationError('Answer or choice must be provided')
        return Answer.objects.create(**validated_data)
