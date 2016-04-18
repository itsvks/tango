from django.shortcuts import render

# Create your views here.
from rest_framework import generics
from rest_framework import permissions

from crud.models import Person
from crud.serializers import PersonSerializer


class PersonListV1(generics.ListCreateAPIView):
    permission_classes = (permissions.IsAuthenticated,)
    queryset = Person.objects.all()
    serializer_class = PersonSerializer


class PersonDetailV1(generics.RetrieveUpdateDestroyAPIView):
    queryset = Person.objects.all()
    serializer_class = PersonSerializer


class PersonListV2(generics.ListCreateAPIView):
    queryset = Person.objects.all()
    serializer_class = PersonSerializer


class PersonDetailV2(generics.RetrieveUpdateDestroyAPIView):
    queryset = Person.objects.all()
    serializer_class = PersonSerializer
