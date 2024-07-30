"""
Contains the logic for processing requests and returning responses.
In a REST framework, this would typically include ViewSets or API views that handle CRUD operations for user-related data.
"""

from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets, permissions
from .models import CustomUser
from .serializers import CustomUserSerializer

class CustomUserViewSet(viewsets.ModelViewSet):
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_permissions(self):
        if self.action == 'create':
            return [permissions.AllowAny()]
        return super().get_permissions()