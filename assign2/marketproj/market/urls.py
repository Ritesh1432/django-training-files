from unicodedata import name
from django.urls import path
from . import views
app_name = 'market'

urlpatterns = [
    path('',views.market_view,name='market'),
    path('add/',views.add_view,name='add'),
    path('delete/',views.delete_view,name='delete'),
    path('sell/<int:item_id>',views.sell_view,name="sell"),
    path('purchase/<int:item_id>',views.purchase_view,name="purchase")

]