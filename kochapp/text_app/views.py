from rest_framework import generics

from text_app.models import AboutUs, PrivacyText
from text_app.serializers import AboutUsSerializer, PrivacySerializer


class AboutUsView(generics.RetrieveAPIView):
    serializer_class = AboutUsSerializer

    def get_object(self):
        about_us = AboutUs.objects.first()
        return about_us


class PrivacyView(generics.RetrieveAPIView):
    serializer_class = PrivacySerializer

    def get_object(self):
        privacy = PrivacyText.objects.first()
        return privacy
