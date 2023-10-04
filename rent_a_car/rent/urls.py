from django.urls import path
from .views import RentalListView, RentalDetailView, CarListView, CarDetailView, CarCreateView, CarUpdateView, HomeView

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('rentals/', RentalListView.as_view(), name='rentals'),
    path('rentals/<int:pk>', RentalDetailView.as_view(), name='rental_detail'),
    path('cars/', CarListView.as_view(), name='cars'),
    path('cars/<int:pk>', CarDetailView.as_view(), name='car_detail'),
    path('cars/create/', CarCreateView.as_view(), name='car_create'),
    path('cars/<int:pk>/update/', CarUpdateView.as_view(), name='car_update'),
]
