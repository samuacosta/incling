from rest_framework import serializers

from .models import Tile, Task


class TileSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Tile
        fields = ('id', 'launch_date', 'status')


class TaskSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Task
        fields = ('id', 'title', 'order', 'description', 'type', 'tile')
