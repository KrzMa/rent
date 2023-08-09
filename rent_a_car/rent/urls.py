from django.urls import path
from .views import RentalListView, RentalDetailView, CarListView, CarDetailView

urlpatterns = [
    path('rentals/', RentalListView.as_view(), name='rentals'),
    path('rentals/<int:pk>', RentalDetailView.as_view(), name='rental_detail'),
    path('cars/', CarListView.as_view(), name='cars'),
    path('cars/<int:pk>', CarDetailView.as_view(), name='car_detail')
]
