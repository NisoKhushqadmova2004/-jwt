from rest_framework import status
from rest_framework.decorators import api_view,permission_classes
from rest_framework.permissions import IsAuthenticated,AllowAny
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken
from .serializers import *
from django.contrib.auth import authenticate,login,logout
from accounts.serializers import  RegisterSerialaizer
from rest_framework_simplejwt.serializers import TokenRefreshSerializer

# Create your views here.

@api_view(['POST'])
@permission_classes([AllowAny])
def register_view(request):
    serializers =  RegisterSerialaizer(data = request.data)
    serializers.is_valid(raise_exception=True)
    serializers.save()
    return Response({'messege':'user refister seccessfull'},status=status.HTTP_201_CREATED)

@api_view(['POST'])
@permission_classes([AllowAny])
def login_view(request):
    username = request.data.get('username')
    password = request.data.get('password')

    if not username or not password:
         return Response({'error':'username and password are requaired'},status=status.HTTP_400_BAD_REQUEST)
    user = authenticate(request,username = username, password=password)

    if user is not None:
        refresh = RefreshToken.for_user(user)
        return Response({
            'refresh':str(refresh),
            'access':str(refresh.access_token),
            'user':{'id':user.id, 'username':user.username}},status=status.HTTP_200_OK)

    else:
        return Response({'error':"INvailed"},status=status.HTTP_201_CREATED)

@api_view(['POST'])
@permission_classes([AllowAny])
def refresh_token_view(request):
    serializers = TokenRefreshSerializer(data = request.data)
    try:
        serializers.is_valid(raise_exception=True)

    except Exception as err:
        return Response({'error':str(err)},status=400)
    return Response(serializers.data, status=status.HTTP_200_OK)

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def logout_view(request):
    try:
        token = request.data.get('refresh')
        refresh = RefreshToken(token)
        refresh.blacklist()
        return Response({'message': 'Logout successful'})

    except Exception:
        return Response({'error': 'Invalid token'}, status=status.HTTP_400_BAD_REQUEST)