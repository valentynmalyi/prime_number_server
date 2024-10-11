from django.core.handlers.wsgi import HttpRequest
from django.http.response import JsonResponse
from rest_framework.views import APIView

from apps.number.serializers import NumSerializer
from apps.number.services import PrimeService


class PrimeView(APIView):
    # noinspection PyMethodMayBeStatic
    def get(self, request: HttpRequest, num: int):
        serializer = NumSerializer(data={"num": num})
        serializer.is_valid(raise_exception=True)
        num = serializer.validated_data["num"]
        is_prime = PrimeService.is_prime(num)
        return JsonResponse(data={'is_prime': is_prime})
