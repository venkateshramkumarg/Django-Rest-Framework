from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Blog
from .serializers import BlogListSerializer, BlogCreateSerializer

class BlogListCreateView(APIView):
    def get(self, request):
        blogs = Blog.objects.all()
        serializer = BlogListSerializer(blogs, many=True)
        return Response(serializer.data)
    
    def post(self, request):
        serializer = BlogCreateSerializer(data=request.data)
        if serializer.is_valid():
            blog = serializer.save()
            response_serializer = BlogListSerializer(blog)
            return Response(response_serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class BlogDetailView(APIView):
    def get_object(self,id):
        blog_id=str(id)
        try:
            return Blog.objects.get(id=blog_id)
        except Blog.DoesNotExist:
            return None
    
    def get(self,request,id):
        blog=self.get_object(id)

        if blog:
            serializer=BlogListSerializer(blog)
            return Response(serializer.data)
        return Response(status=status.HTTP_404_NOT_FOUND)

    def put(self,request,id):
        blog=self.get_object(id)
        if blog:
            serializer=BlogCreateSerializer(blog,data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data,status=status.HTTP_204_NO_CONTENT)
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    def delete(self,request,id):
        blog=self.get_object(id)
        if blog:
            blog.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        return Response(status=status.HTTP_404_NOT_FOUND)
    