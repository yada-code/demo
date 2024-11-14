from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),  # URL ที่ว่างจะเรียกใช้ view 'home'
    ]
