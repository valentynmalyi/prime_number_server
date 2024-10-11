from django.urls import include, path

urlpatterns = [
    path('number/', include('apps.number.urls')),
]
