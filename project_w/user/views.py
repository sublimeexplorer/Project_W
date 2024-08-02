from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.authtoken.models import Token
from django.contrib.auth import authenticate, login, logout
from .models import Member


# Create your views here.
@api_view(['GET'])
def hello_world(request):
    return Response("Hello, World!", status=status.HTTP_200_OK)

@api_view(['POST'])
def register(request):
    if request.method == 'POST':
        email = request.data.get('email')
        password = request.data.get('password')

        if Member.objects.filter(email=email).exists():
            return Response({'error': 'Email already exists'}, status=status.HTTP_400_BAD_REQUEST)

        user = Member.objects.create_user(email=email, password=password)
        token, _ = Token.objects.get_or_create(user=user)
        return Response({'token': token.key}, status=status.HTTP_201_CREATED)

@api_view(['POST'])
def login(request):
    if request.method == 'POST':
        email = request.data.get('email')
        password = request.data.get('password')
        user = authenticate(request, email=email, password=password)
        if user:
            login(request, user)
            token, _ = Token.objects.get_or_create(user=user)
            return Response({'token': token.key}, status=status.HTTP_200_OK)
        else:
            return Response({'error': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def logout(request):
    if request.method == 'POST':
        request.user.auth_token.delete()
        logout(request)
        return Response({'message': 'Successfully logged out'}, status=status.HTTP_200_OK)
