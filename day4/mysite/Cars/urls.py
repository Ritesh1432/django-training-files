from django.urls import path
from . import views
app_name = 'Cars'

urlpatterns = [
    path('rentalreview/',views.rental_review,name='rentalreview'),
    path('thankyou/',views.thank_you,name='thankyou')
]