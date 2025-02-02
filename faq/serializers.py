# filepath: /c:/Users/Murthy/Desktop/OWN_VS/BharatFD_project/myproject/faq/serializers.py
from rest_framework import serializers
from .models import FAQ


class FAQSerializer(serializers.ModelSerializer):
    class Meta:
        model = FAQ
        fields = ['id', 'question', 'answer']
