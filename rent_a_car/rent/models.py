from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator


class BaseModel(models.Model):
    """ Base model """

    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    class Meta:
        """ Meta class """

        abstract = True


class Location(BaseModel):
    city_key = models.CharField(max_length=3, default="XXX", null=False)
    city_name = models.CharField(max_length=32, default="XXXXX", null=False)

    def __str__(self):
        return f"{self.city_name}"


class Client(BaseModel):
    """Create client profile"""
    name = models.CharField(max_length=32, null=False)
    surname = models.CharField(max_length=64, null=False)
    id_client = models.CharField(max_length=64, unique=True, null=False)
    driver_license = models.CharField(max_length=64, unique=True, null=False)
    mail = models.EmailField(max_length=64, null=True)
    phone = models.CharField(max_length=32, null=False, unique=True)
    street = models.CharField(max_length=64, null=False)

    def __str__(self):
        return self.name + " " + self.surname


class Car(BaseModel):
    """ Car Model"""

    PETROL_CHOICES = [
        ('', 'Select petrol'),
        ('PB', 'Petrol'),
        ('ON', 'Diesel'),
        ('LPG', 'AutoGas'),
        ('HEV', 'Hybrid'),
        ('PHEV', 'Hybrid plug-in'),
        ('EV', 'Electric')

    ]

    CLASS_CAR_CHOICES = [
        ('', 'Select class'),
        ('A', 'A'),
        ('B', 'B'),
        ('B+', 'B+'),
        ('C', 'C+'),
        ('D', 'D'),
        ('D+', 'D+'),
        ('Combi', 'COMBI'),
        ('SUV', 'SUV'),
        ('CROSS', 'CROSSOVER'),
        ('PR', 'PREMIUM'),
    ]

    brand = models.CharField(max_length=32, null=False)
    model = models.CharField(max_length=32, null=False)
    vin = models.CharField(max_length=32, unique=True, null=False)
    engine = models.FloatField(validators=[MinValueValidator(1.0), MaxValueValidator(5.0)], null=False, default='')
    petrol = models.CharField(max_length=32, choices=PETROL_CHOICES, null=False, blank=False, default="")
    class_car = models.CharField(max_length=32, choices=CLASS_CAR_CHOICES, null=False, blank=False, default="")
    number_plate = models.CharField(max_length=32, unique=True, null=False)
    year = models.PositiveIntegerField(validators=[MinValueValidator(2017), MaxValueValidator(2023)])
    car_seats = models.CharField(max_length=12, validators=[MinValueValidator(1.), MaxValueValidator(7.)], null=False, default='')
    deposit = models.DecimalField(max_digits=6, decimal_places=2, null=False)
    price = models.DecimalField(max_digits=6, decimal_places=2, null=False)
    image = models.ImageField(upload_to='car_pics/', default='')
    is_car_available = models.BooleanField(default=True)

    def __str__(self):
        return self.brand + ' ' + self.model


class Rental(BaseModel):
    """ Rental Model"""

    car = models.ForeignKey(Car, on_delete=models.CASCADE, related_name='rentals', null=False)
    client = models.ForeignKey(Client, on_delete=models.CASCADE, related_name='rentals', null=False)
    start_date = models.DateField(null=False)
    end_date = models.DateField()
    price = models.DecimalField(max_digits=6, decimal_places=2, blank=True)

    def __str__(self):
        return f"{self.car} - {self.client} - {self.start_date} - {self.end_date}"

    def save(self, *args, **kwargs):
        if not self.pk:
            self.price = self.car.price * (self.end_date - self.start_date).days
        super(Rental, self).save(*args, **kwargs)


class Company(BaseModel):
    name = models.CharField(max_length=64, null=False)
    city = models.ForeignKey(Location, on_delete=models.CASCADE)
    nip = models.IntegerField(validators=[MinValueValidator(10), MaxValueValidator(10)], null=False)

    def __str__(self):
        return f"{self.name}"



