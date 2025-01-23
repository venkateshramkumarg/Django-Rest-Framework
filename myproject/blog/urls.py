from django.urls import path
from .views import BlogListCreateView,BlogDetailView

urlpatterns = [
    path('blogs/',BlogListCreateView.as_view(),name='blog-list-create'),
    path('blogs/<str:id>/',BlogDetailView.as_view(),name='blog-detail')
]
