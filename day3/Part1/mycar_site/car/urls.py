from django.urls import path
from . import views

app_name="car"

urlpatterns = [
    path('',views.home_view,name='home'),
    path('list/',views.list_view,name='list'),
    path('add/',views.add_view,name='add'),
    path('delete/',views.delete_view,name='delete')
]