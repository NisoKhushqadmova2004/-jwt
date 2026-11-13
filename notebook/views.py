from rest_framework.decorators import api_view,permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework import status
from .models import Debt
from .serializer import DebtSerializer

@api_view(['GET','POST'])
@permission_classes([AllowAny])
def debt_list(request):
    if request.method == 'GET':
        debts = Debt.objects.all()
        serializer = DebtSerializer(debts, many = True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = DebtSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET','PUT','DELETE']) 
@permission_classes([AllowAny]) 
def debt_detail(request,pk):
    try:
        debt = Debt.objects.get(id=pk)
    except Debt.DoesNotExist:
        return Response({'error': 'Debt not found'},status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = DebtSerializer(debt)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = DebtSerializer(debt, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        debt.delete()
        return Response({'message': 'Debt deleted successfully'},status=status.HTTP_204_NO_CONTENT)

