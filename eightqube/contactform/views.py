from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView

from .models import ContactForm
from .serializers import ContactFormSerializer


# Create your views here.

class ContactFormView(ListCreateAPIView):
    queryset = ContactForm.objects.all()
    serializer_class = ContactFormSerializer

    def perform_create(self, serializer):
        serializer.save()