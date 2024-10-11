from django.urls import path

from apps.number.views import PrimeView

urlpatterns = [
    path('<int:num>', PrimeView.as_view(), name='check_num'),
]
