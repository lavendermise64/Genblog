from django.shortcuts import render
from .serializer import BlogSerializer
from .models import Blog
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.http import Http404


# Create your views here.
class BlogView(APIView):
    def get(self,request,format=None):
        blogs=Blog.objects.all()
        serializer=BlogSerializer(blogs,many=True)
        return Response(serializer.data)
    def post(self,request,format=None):  
        serializer=BlogSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.error,status=status.HTTP_400_BAD_REQUEST)
class SingleBlogView(APIView):
    def get_single_blog(self,id):
        try:
            return Blog.objects.get(id=id)
        except Blog.DoesNotExist:
            raise Http404
    def get(self,request,id):
        blog=self.get_single_blog(id)
        serializer=BlogSerializer(blog)
        return Response(serializer.data)
    def put(self,request,id):
        blog=self.get_single_blog(id)
        serializer=BlogSerializer(blog,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_200_OK)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    def delete(self,request,id):
        blog=self.get_single_blog(id)
        blog.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
        

