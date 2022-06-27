from django.urls import path
from webapp.views import index, create_task

urlpatterns = [
    path('', index),
    path('add/', create_task)
]
