from rest_framework import serializers

from .models import ContactForm


class ContactFormSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContactForm
        fields = ('id', 'name', 'email', 'subject', 'message')

    def create(self, validated_data):
        return ContactForm.objects.create(**validated_data)
