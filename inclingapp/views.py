from django.shortcuts import render
from rest_framework import viewsets

from .serializers import TileSerializer, TaskSerializer
from .models import Tile, Task


class TileViewSet(viewsets.ModelViewSet):
    queryset = Tile.objects.all().order_by('launch_date')
    serializer_class = TileSerializer


class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all().order_by('title')
    serializer_class = TaskSerializer
