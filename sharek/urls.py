from django.urls import path
from . import views

urlpatterns = [

    path("posts", views.PostInsertAPIView.as_view(), name="posts"),
    path("post/<int:pk>", views.PostDetailAPIView.as_view(), name="post"),
    path("answer_history", views.AnswerHistoryAPIView.as_view(), name="answer_history"),
]
