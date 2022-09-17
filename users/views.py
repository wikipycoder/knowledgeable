from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import RegisterSerializer, UpdateSerializer
from django.contrib.auth import authenticate, login, logout
# from rest_framework.authtoken.models import Token
# from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from knox.serializers import UserSerializer
from rest_framework.permissions import AllowAny, IsAuthenticated
from knox.views import LoginView as KnoxLoginView
from rest_framework.authtoken.serializers import AuthTokenSerializer
from .models import User


class UserProfilesAPIView(APIView):

    def get(self, request, *args, **kwargs):
        users = User.objects.all()
        serializer = RegisterSerializer(users, many=True)
        return Response(serializer.data)




class RegisterAPIView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        print("i'm being executed")
        serializer = RegisterSerializer(data=request.data)
        if serializer.is_valid():
            print("if executed")
            serializer.save()
            return Response(serializer.data)

        return Response(serializer.errors)


class UpdateUserAPIView(APIView):

    def put(self, request):

        serializer = UpdateSerializer(data=request.data, instance=request.user)
        if serializer.is_valid():
            user = serializer.save()
            response = {

                "first_name": user.first_name,
                "last_name": user.last_name,
                "username": user.username,
                "email": user.email
            }

            return Response(response, status=status.HTTP_200_OK)

        return Response(serializer.errors)




class LoginAPIView(KnoxLoginView):
    permission_classes = (AllowAny,)

    def post(self, request, format=None):
        serializer = AuthTokenSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        login(request, user)
        return super(LoginAPIView, self).post(request, format=None)
 


# class LogoutAPIView(APIView):

#     def get(self, request):
        
#         logout(request)
#         return Response({"success": "user successfully logged out"})


class TestingAPIView(APIView):

    # authentication_classes = [TokenAuthentication]
    # permission_classes = [AllowAny]

    def get(self, request):
        return Response({"msg": "hello world"})