from django.core.exceptions import ObjectDoesNotExist
from django.http import HttpResponseRedirect
from rest_framework.generics import ListCreateAPIView
from rest_framework.mixins import RetrieveModelMixin
from rest_framework.permissions import AllowAny
from rest_framework.response import Response

from url_shortener.models import URL
from url_shortener.serializers import URLSerializer


class URLView(RetrieveModelMixin, ListCreateAPIView):
    queryset = URL.objects.all()
    serializer_class = URLSerializer
    permission_classes = [AllowAny]

    def create(self, request, *args, **kwargs):
        try:
            instance = URL.objects.get(original=request.data.get("original"))
            serializer = self.get_serializer(instance)
            return Response(serializer.data)
        except ObjectDoesNotExist:
            return super().create(request, *args, **kwargs)


def redirect_to_original_url(request, short_url: str):
    url = URL.objects.get(shortened=short_url)
    return HttpResponseRedirect(redirect_to=url.original)
