from rest_framework import serializers

from text_app.models import AboutUs


class AboutUsSerializer(serializers.ModelSerializer):
    class Meta:
        model = AboutUs
        fields = ('text',)


class PrivacySerializer(serializers.ModelSerializer):
    class Meta:
        model = AboutUs
        fields = ('text',)
