from django.urls import path
from . import views

urlpatterns = [
    path('',views.office_view,name='office'),
]