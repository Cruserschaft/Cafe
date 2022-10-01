# Generated by Django 4.1.1 on 2022-10-01 19:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0010_testimonials'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contacts',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('location1', models.CharField(max_length=50)),
                ('location2', models.CharField(blank=True, max_length=50)),
                ('open_hours1', models.CharField(max_length=50)),
                ('open_hours2', models.CharField(blank=True, max_length=50)),
                ('email1', models.CharField(max_length=50)),
                ('email2', models.CharField(blank=True, max_length=50)),
                ('call1', models.CharField(max_length=50)),
                ('call2', models.CharField(blank=True, max_length=50)),
            ],
            options={
                'verbose_name': 'Контакти',
                'verbose_name_plural': 'Контакти',
            },
        ),
        migrations.AlterModelOptions(
            name='testimonials',
            options={'ordering': ('test_order',), 'verbose_name': 'Програмісти сайту?', 'verbose_name_plural': 'Програмісти сайту?'},
        ),
    ]
