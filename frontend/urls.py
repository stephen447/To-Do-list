from django.urls import path
from .views import index

urlpatterns = [
    path('', index),
    path('todolist', index),
    path('create', index),
    path('login', index)
]