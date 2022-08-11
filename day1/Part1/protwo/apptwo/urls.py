from django.urls import path
from . import views

#127.0.0.1:8000/apptwo
urlpatterns = [
    path('', views.index, name='index'),
]