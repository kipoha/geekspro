from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.generics import *
from . import serialazers, models
# Create your views here.

class GetData(ListAPIView):
    queryset = models.Task
    serializer_class = serialazers.TaskSerialazer

# class AddData(CreateAPIView):
#     queryset = models.Task()
#     serializer_class = serialazers.TaskSerialazer()

# class RemoveData(...):
#     queryset = models.Task()
#     serializer_class = serialazers.TaskSerialazer()
