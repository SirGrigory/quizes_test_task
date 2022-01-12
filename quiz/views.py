from rest_framework.generics import ListAPIView, CreateAPIView
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK
from django.shortcuts import get_list_or_404
from django.utils import timezone
from .serializers import QuizListSerializer, QuestionListSerializer, AnswerSerializer
from .models import Quiz, Question, Answer
from django_filters.rest_framework import DjangoFilterBackend
from .service import AnswerFilter


class QuizListView(ListAPIView):
    queryset = Quiz.objects.all().filter(end_date__gt=timezone.now())
    serializer_class = QuizListSerializer


class QuestionsListView(APIView):

    def get(self, request, pk):
        questions = get_list_or_404(Question, quiz_id=pk)
        serializer = QuestionListSerializer(instance=questions, many=True)
        return Response(data=serializer.data, status=HTTP_200_OK)


class AnswerView(APIView):

    def post(self, request, pk):
        request.data['quiz'] = pk
        serializer = AnswerSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(data=serializer.data, status=HTTP_200_OK)


class UserAnswersListView(ListAPIView):
    queryset = Answer.objects.all()
    serializer_class = AnswerSerializer
    filterset_class = AnswerFilter
