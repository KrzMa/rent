from .models import Car, Client, Rental
from django.views.generic import FormView, ListView, DetailView, DeleteView, UpdateView, CreateView


class RentalListView(ListView):
    template_name = 'rentals_list.html'
    model = Rental


class RentalDetailView(DetailView):
    template_name = 'rental.html'
    model = Rental

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(**kwargs)
        context['car'] = Car.objects.get(rentals=self.object)
        context['client'] = Client.objects.get(rentals=self.object)
        return context


class CarListView(ListView):
    template_name = 'car_list.html'
    model = Car


class CarDetailView(DetailView):
    model = Car
    template_name = 'car.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        print(context['car'].model)
        return context


