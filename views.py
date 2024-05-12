from django.shortcuts import render
from rest_framework import generics, status
from rest_framework.response import Response
from .models import Teknik, Computer, Elit
from .serializers import TeknikSerializers, ComputerSerializers, ElitSerializers


class TeknikListCreate(generics.ListCreateAPIView):
    queryset = Teknik.objects.all()
    serializer_class = TeknikSerializers

class TeknikRetrieveUpdateDestory(generics.RetrieveUpdateDestroyAPIView):
    queryset = Teknik.objects.all()
    serializer_class = TeknikSerializers
    lookup_field = "pk"
    
class ComputerListCreate(generics.ListCreateAPIView):
    queryset = Computer.objects.all()
    serializer_class = ComputerSerializers

    def delete(self, request):
        Computer.objects.all().delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class ComputerRetrieveUpdateDestory(generics.RetrieveUpdateDestroyAPIView):
    queryset = Computer.objects.all()
    serializer_class = ComputerSerializers
    lookup_field = "pk"   

class ElitListCreate(generics.ListCreateAPIView):
    queryset = Elit.objects.all()
    serializer_class = ElitSerializers

    def delete(self, request):
        Elit.objects.all().delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class ElitRetrieveUpdateDestory(generics.RetrieveUpdateDestroyAPIView):
    queryset = Elit.objects.all()
    serializer_class = ElitSerializers
    lookup_field = "pk"     
