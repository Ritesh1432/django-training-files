from django.urls import path
from . import views
app_name = 'market'

urlpatterns = [
    path('',views.market_view,name='market'),
    path('add/',views.add_view,name='add'),
    path('delete/',views.delete_view,name='delete')

]