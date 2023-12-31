# Generated by Django 4.2.4 on 2023-10-04 14:32

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("rent", "0002_alter_rental_price"),
    ]

    operations = [
        migrations.CreateModel(
            name="Location",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("create_at", models.DateTimeField(auto_now_add=True)),
                ("update_at", models.DateTimeField(auto_now=True)),
                ("city_key", models.CharField(default="XXX", max_length=3)),
                ("city_name", models.CharField(default="XXXXX", max_length=32)),
            ],
            options={
                "abstract": False,
            },
        ),
        migrations.AddField(
            model_name="car",
            name="car_seats",
            field=models.CharField(
                default="",
                max_length=12,
                validators=[
                    django.core.validators.MinValueValidator(1.0),
                    django.core.validators.MaxValueValidator(7.0),
                ],
            ),
        ),
        migrations.AddField(
            model_name="car",
            name="class_car",
            field=models.CharField(
                choices=[
                    ("", "Select class"),
                    ("A", "A"),
                    ("B", "B"),
                    ("B+", "B+"),
                    ("C", "C+"),
                    ("D", "D"),
                    ("D+", "D+"),
                    ("Combi", "COMBI"),
                    ("SUV", "SUV"),
                    ("CROSS", "CROSSOVER"),
                    ("PR", "PREMIUM"),
                ],
                default="",
                max_length=32,
            ),
        ),
        migrations.AddField(
            model_name="car",
            name="engine",
            field=models.FloatField(
                default="",
                validators=[
                    django.core.validators.MinValueValidator(1.0),
                    django.core.validators.MaxValueValidator(5.0),
                ],
            ),
        ),
        migrations.AddField(
            model_name="car",
            name="image",
            field=models.ImageField(default="", upload_to="car_pics/"),
        ),
        migrations.AddField(
            model_name="car",
            name="is_car_available",
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name="car",
            name="petrol",
            field=models.CharField(
                choices=[
                    ("", "Select petrol"),
                    ("PB", "Petrol"),
                    ("ON", "Diesel"),
                    ("LPG", "AutoGas"),
                    ("HEV", "Hybrid"),
                    ("PHEV", "Hybrid plug-in"),
                    ("EV", "Electric"),
                ],
                default="",
                max_length=32,
            ),
        ),
        migrations.CreateModel(
            name="Company",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("create_at", models.DateTimeField(auto_now_add=True)),
                ("update_at", models.DateTimeField(auto_now=True)),
                ("name", models.CharField(max_length=64)),
                (
                    "nip",
                    models.IntegerField(
                        validators=[
                            django.core.validators.MinValueValidator(10),
                            django.core.validators.MaxValueValidator(10),
                        ]
                    ),
                ),
                (
                    "city",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="rent.location"
                    ),
                ),
            ],
            options={
                "abstract": False,
            },
        ),
    ]
