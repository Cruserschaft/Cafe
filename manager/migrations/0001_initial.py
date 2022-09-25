# Generated by Django 4.1.1 on 2022-09-25 17:23

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='UserReservations',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('email', models.EmailField(max_length=254)),
                ('phone', models.CharField(max_length=15, validators=[django.core.validators.RegexValidator(message='Некоректний номер', regex='/^\\([0-9]{3}\\) [0-9]{3}-[0-9]{2}-[0-9]{2}/')])),
                ('date_order', models.DateField()),
                ('time_order', models.TimeField()),
                ('of_people', models.PositiveSmallIntegerField()),
                ('message', models.TextField(max_length=300)),
                ('is_processed', models.BooleanField(default=False)),
                ('date', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'ordering': ('-date',),
            },
        ),
    ]
