from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView, \
    RetrieveUpdateDestroyAPIView

from .models import ContactForm
from .serializers import ContactFormSerializer


# Create your views here.

class ContactFormView(ListCreateAPIView):
    queryset = ContactForm.objects.all()
    serializer_class = ContactFormSerializer

    def perform_create(self, serializer):
        serializer.save()


class SingleMessageView(RetrieveUpdateDestroyAPIView):
    queryset = ContactForm.objects.all()
    serializer_class = ContactFormSerializer
