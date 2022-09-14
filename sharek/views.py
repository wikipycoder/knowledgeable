# from django.shortcuts import render
# from rest_framework.views import APIView
# from rest_framework.response import Response
# from rest_framework.status import HTTP_201_CREATED, HTTP_404_NOT_FOUND, HTTP_400_BAD_REQUEST, HTTP_204_NO_CONTENT
# from rest_framework import generics

# from sharek.serializers import PostSerializer, AnswerHistorySerializer
# from .models import Post, AnswerHistory


# class PostInsertAPIView(APIView):

#     def get(self, request):
#         posts = Post.objects.all()
#         post_serializer = PostSerializer(posts, many=True)    
#         return Response(post_serializer.data)
    

#     def post(self, request):

#         post_serializer = PostSerializer(data=request.data, context={"request": request})
#         if post_serializer.is_valid():
#             post_serializer.save()
#             return Response(post_serializer.data, status=HTTP_201_CREATED)
        
#         return Response(post_serializer.errors)



# class PostDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    
#     queryset = Post.objects.all()
#     serializer_class = PostSerializer


# class AnswerHistoryAPIView(APIView):

#     def get(self, request, *args, **kwargs):

#         answer_history = AnswerHistory.objects.all()
#         serializer = AnswerHistorySerializer(answer_history, many=True)
#         return Response(serializer.data)


#     def post(self, request, *args, **kwargs):

#         serializer = AnswerHistorySerializer(data=request.data, context={"request": request})
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=HTTP_201_CREATED)
        
#         return Response(serializer.errors)





