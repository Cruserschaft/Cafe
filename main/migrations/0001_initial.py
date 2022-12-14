# Generated by Django 4.1.1 on 2022-09-24 09:02

from django.db import migrations, models
import django.db.models.deletion
import main.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='About',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('about_title', models.TextField()),
                ('about_start_text', models.TextField()),
                ('about_p1', models.TextField()),
                ('about_p2', models.TextField(blank=True)),
                ('about_p3', models.TextField(blank=True)),
                ('about_end', models.TextField(blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='DishType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dish_type_name', models.CharField(max_length=50, unique=True)),
                ('dish_type_order', models.PositiveIntegerField(unique=True)),
            ],
            options={
                'verbose_name': 'Категорії',
                'ordering': ('dish_type_order',),
            },
        ),
        migrations.CreateModel(
            name='Events',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('event_title', models.TextField()),
                ('event_cost', models.PositiveIntegerField()),
                ('event_about_start', models.TextField()),
                ('event_about1', models.TextField(blank=True)),
                ('event_about2', models.TextField(blank=True)),
                ('event_about3', models.TextField(blank=True)),
                ('event_about_finish', models.TextField(blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Menu',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dish_name', models.CharField(max_length=50, unique=True)),
                ('dish_cost', models.DecimalField(decimal_places=2, max_digits=8)),
                ('dish_ingredients', models.CharField(max_length=300)),
                ('dish_access', models.BooleanField(default=True)),
                ('dish_order', models.SmallIntegerField()),
                ('dish_is_special', models.BooleanField(default=False)),
                ('dish_image', models.ImageField(upload_to=main.models.Menu.get_file_name)),
                ('dish_about', models.TextField(blank=True)),
                ('dish_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.dishtype')),
            ],
            options={
                'verbose_name': 'Страви',
                'ordering': ('dish_order',),
            },
        ),
    ]
