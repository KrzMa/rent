from django.contrib import admin
from .models import Client, Car, Rental

admin.site.register(Car)
admin.site.register(Client)
admin.site.register(Rental)
