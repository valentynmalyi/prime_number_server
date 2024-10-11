from django.core.handlers.wsgi import HttpRequest
from django.http.response import JsonResponse
from django.views.generic import DetailView


class PrimeView(DetailView):
    # noinspection PyMethodOverriding
    def get(self, request: HttpRequest, num: int):
        for x in range(2, num):
            if num % x == 0:
                return JsonResponse(data={'is_prime': False})
        return JsonResponse(data={'is_prime': True})
