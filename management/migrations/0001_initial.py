# Generated by Django 4.2.7 on 2023-11-19 03:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="RoomType",
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
                ("name", models.CharField(max_length=300)),
            ],
        ),
        migrations.CreateModel(
            name="Service",
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
                ("name", models.CharField(max_length=300)),
                ("description", models.TextField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name="Room",
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
                ("room_no", models.CharField(max_length=300)),
                ("floor", models.CharField(max_length=300)),
                ("description", models.TextField(null=True)),
                ("bed_count", models.IntegerField()),
                (
                    "status",
                    models.CharField(
                        choices=[
                            ("Available", "Available"),
                            ("Unavailable", "Unavailable"),
                            ("In use", "In use"),
                        ],
                        max_length=300,
                    ),
                ),
                (
                    "type",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        to="management.roomtype",
                    ),
                ),
            ],
        ),
    ]
