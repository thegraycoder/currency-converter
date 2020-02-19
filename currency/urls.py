from django.urls import path, include
from .views import CurrencyConvert

urlpatterns = [
    path('convert', CurrencyConvert.as_view()),
]
