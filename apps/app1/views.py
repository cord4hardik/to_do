from rest_framework import viewsets
from .models import Todo, AccessLog
from .serializers import TodoSerializer, AccessLogSerializer
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status


class TodoViewSet(viewsets.ModelViewSet):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def list(self, request):
        try:
            queryset = Todo.objects.all()
        except Todo.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializer = TodoSerializer(queryset, many=True)
        return Response(
                {"Success": True, "data": serializer.data},
                status=status.HTTP_200_OK,
            )
    
    def create(self, request):
        serializer = TodoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(
                {"Success": True, "data": serializer.data},
                status=status.HTTP_201_CREATED,
            )

    def retrieve(self, request, pk=None):
        try:
            queryset = Todo.objects.get(id=pk)
        except Todo.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializer = TodoSerializer(queryset)
        return Response(
                {"Success": True, "data": serializer.data},
                status=status.HTTP_200_OK,
            )
    
    def partial_update(self, request, pk=None):
        try:
            queryset = Todo.objects.get(id=pk)
        except Todo.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializer = TodoSerializer(queryset, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(
                {"Success": True, "data": serializer.data},
                status=status.HTTP_201_CREATED,
            )        
        
    def destroy(self, request, pk=None):
        try:
            queryset = Todo.objects.get(id=pk)
        except Todo.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        queryset.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class AccessLogViewSet(viewsets.ModelViewSet):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    def list(self, request):
        try:
            queryset = AccessLog.objects.all()
        except AccessLog.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializer = AccessLogSerializer(queryset, many=True)
        return Response(
                {"Success": True, "data": serializer.data},
                status=status.HTTP_200_OK,
            )
    
    def create(self, request):
        serializer = AccessLogSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(
                {"Success": True, "data": serializer.data},
                status=status.HTTP_201_CREATED,
            )

    def retrieve(self, request, pk=None):
        try:
            queryset = AccessLog.objects.get(id=pk)
        except AccessLog.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializer = AccessLogSerializer(queryset)
        return Response(
                {"Success": True, "data": serializer.data},
                status=status.HTTP_200_OK,
            )
    
    def partial_update(self, request, pk=None):
        try:
            queryset = AccessLog.objects.get(id=pk)
        except AccessLog.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializer = AccessLogSerializer(queryset, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(
                {"Success": True, "data": serializer.data},
                status=status.HTTP_201_CREATED,
            )        
        
    def destroy(self, request, pk=None):
        try:
            queryset = AccessLog.objects.get(id=pk)
        except AccessLog.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        queryset.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)