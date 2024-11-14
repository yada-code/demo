from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.register_license, name='register_license'),
]
