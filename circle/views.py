from django.shortcuts import render
from rest_framework.views import APIView

from circle.serializers import RelationshipSerializer, GroupSerializer
from .models import Relationship, Group
from rest_framework.response import Response
from rest_framework import generics


class RelationshipAPIView(APIView):

    def get(self, request, *args, **kwargs):
        relationships = request.user.relationship.all()
        serializer = RelationshipSerializer(relationships, many=True)
        return Response(serializer.data)
    
    def post(self, request, *args, **kwargs):
        serializer = RelationshipSerializer(data=request.data, context={"request": request})

        if serializer.is_valid():
            serializer.save()
            if request.data.get("unfollow"):
                serializer = RelationshipSerializer(request.user.relationship.all(), many=True)
            return Response(serializer.data)

        return Response(serializer.errors)




class ListCreateGroupAPIView(generics.ListCreateAPIView):

    queryset = Group.objects.all()
    serializer_class = GroupSerializer


    def get_queryset(self):
        user = self.request.user
        return Group.objects.filter(owner=user)

    
    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)





