from django.urls import path
from .views import optimize_chip

urlpatterns = [
    path('', optimize_chip, name='optimize'),
]
