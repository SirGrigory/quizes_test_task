from django.urls import path
from .views import QuizListView, QuestionsListView, AnswerView, UserAnswersListView
from rest_framework.documentation import include_docs_urls


urlpatterns = [
    path('', QuizListView.as_view(), name='quiz_list'),
    path('<int:pk>/', QuestionsListView.as_view(), name='qestion_list'),
    path('answer/<int:pk>/', AnswerView.as_view(), name='answer'),
    path('reports/', UserAnswersListView.as_view(), name='user_answers'),
    path('docs/', include_docs_urls(title='QuizAPI')),
]
