from django.urls import path
from . import views

urlpatterns = [


    path("relationships", views.RelationshipAPIView.as_view(), name="relationships"),
    path("groups", views.ListCreateGroupAPIView.as_view(), name="groups"),
]
