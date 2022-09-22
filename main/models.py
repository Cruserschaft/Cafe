from django.db import models


class DishType(models.Model):
    dish_type_name = models.TextField()


class Menu(models.Model):
    dish_name = models.TextField()
    dish_type = models.ForeignKey(DishType, on_delete=models.CASCADE)
    dish_comp = models.TextField(blank=True)
    dish_cost = models.PositiveIntegerField()
    dish_access = models.BooleanField()
    dish_image = models.ImageField(upload_to="images")


class Events(models.Model):
    event_title = models.TextField()
    event_cost = models.PositiveIntegerField()
    event_about_start = models.TextField()
    event_about1 = models.TextField(blank=True)
    event_about2 = models.TextField(blank=True)
    event_about3 = models.TextField(blank=True)
    event_about_finish = models.TextField(blank=True)


class About(models.Model):
    about_title = models.TextField()
    about_start_text = models.TextField()
    about_p1 = models.TextField()
    about_p2 = models.TextField(blank=True)
    about_p3 = models.TextField(blank=True)
    about_end = models.TextField(blank=True)


