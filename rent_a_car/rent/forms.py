from django.core.exceptions import ValidationError
from django.core.validators import MinValueValidator, MaxValueValidator
from django.db.models import PositiveIntegerField
from django.forms import (
    CharField, DateField, Form, DecimalField
)

from .models import Car


class CarForm(Form):
    brand = CharField(max_length=32)
    model = CharField(max_length=32)
    vin = CharField(max_length=32)
    number_plate = CharField(max_length=32)
    year = DecimalField(max_digits=4)
    deposit = DecimalField(max_digits=6, decimal_places=2)
    price = DecimalField(max_digits=6, decimal_places=2)

    def clean_vin(self):
        vin = self.cleaned_data['vin']
        if Car.objects.filter(vin=vin).exists():
            raise ValidationError('Vin already exists')
        return vin

    def clean_number_plate(self):
        number_plate = self.cleaned_data['number_plate']
        if Car.objects.filter(number_plate=number_plate).exists():
            raise ValidationError('Vin already exists')
        return number_plate

    def clean_year(self):
        year = self.cleaned_data['year']
        if year < 2017 or year > 2023:
            raise ValidationError('The car must not be older than 2017 and younger than 2023')
        return year

    def save(self):
        data = self.cleaned_data
        car = Car.objects.create(
            brand=data['brand'],
            model=data['model'],
            vin=data['vin'],
            number_plate=data['number_plate'],
            year=data['year'],
            deposit=data['deposit'],
            price=data['price']
        )
        return car
