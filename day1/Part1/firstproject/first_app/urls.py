from django.urls import path
from first_app import views

#127.0.0.1:8000/first_app
urlpatterns = [
    path('', views.index, name='index'),
]