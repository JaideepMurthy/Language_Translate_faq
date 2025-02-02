from django.core.cache import cache
from rest_framework import viewsets
from rest_framework.response import Response
from .models import FAQ
from .serializers import FAQSerializer

class FAQViewSet(viewsets.ModelViewSet):
    queryset = FAQ.objects.all()
    serializer_class = FAQSerializer

    def list(self, request, *args, **kwargs):
        lang = request.query_params.get('lang', 'en')
        cache_key = f'faqs_{lang}'
        faqs = cache.get(cache_key)
        if not faqs:
            faqs = self.queryset
            for faq in faqs:
                faq.question = faq.get_translated_question(lang)
            cache.set(cache_key, faqs, timeout=60*15)  # Cache for 15 minutes
        serializer = self.get_serializer(faqs, many=True)
        return Response(serializer.data)