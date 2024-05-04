from rest_framework import serializers

class TaskSerialazer(serializers.Serializer):
    title = serializers.CharField()
    description = serializers.CharField()
    completed = serializers.BooleanField()
    created = serializers.DateTimeField()