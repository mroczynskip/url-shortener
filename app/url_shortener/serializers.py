from rest_framework import serializers

from url_shortener.models import URL


class URLSerializer(serializers.ModelSerializer):
    shortened = serializers.SerializerMethodField()

    class Meta:
        model = URL
        fields = ["original", "shortened"]

    def get_shortened(self, obj):
        request = self.context.get("request")
        return request.build_absolute_uri(obj.shortened)
