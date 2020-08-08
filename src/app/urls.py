from django.urls import path
from app.views import index

urlpatterns = [
    path('', index),
]
