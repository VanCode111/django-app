from rest_framework import routers, serializers, viewsets, status, pagination, generics, filters
from rest_framework.response import Response
from .models import Cleaning, City
from .serializers import CleaningSerializer, CitySerializer, CreateCleaningSerializer, CompletedSerializer
from django.db.models import Q
from rest_framework.decorators import action
from django_filters.rest_framework import DjangoFilterBackend

class CleaningsViewSet(viewsets.ModelViewSet):
    queryset = Cleaning.objects.all()
    action_serializers = {
        'change_completed': CompletedSerializer
    }
    def get_serializer_class(self):
        if self.request.method in ['POST', 'PUT']:
            return CreateCleaningSerializer
        return CleaningSerializer

    @action(methods=['GET'], detail=False)
    def completed(self, request):
        completed_cleanings = Cleaning.objects.all().filter(Q(completed=True) | Q(title='Выполнен'))

        page = self.paginate_queryset(completed_cleanings)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(completed_cleanings, many=True)
        return Response(serializer.data)

    @action(methods=['POST'], detail=True)
    def change_completed(self, request, pk=None):
        cleaning = self.get_object()
        serializer = CompletedSerializer(data=request.data)
        if (serializer.is_valid()):
            completed = serializer.validated_data['completed']
            cleaning.completed = completed
            cleaning.save()
            serializer = self.get_serializer(cleaning)
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    search_fields = ['$title']
    filterset_fields = ['city']


class CitiesViewSet(viewsets.ModelViewSet):
    queryset = City.objects.all()
    serializer_class = CitySerializer

