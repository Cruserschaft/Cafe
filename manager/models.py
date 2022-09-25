from django.db import models
from django.core.validators import RegexValidator


# Create your models here.
class UserReservations(models.Model):
    mobile_valid = RegexValidator(regex=r"/^\([0-9]{3}\) [0-9]{3}-[0-9]{2}-[0-9]{2}/", message="Некоректний номер")
    name = models.CharField(max_length=30)
    email = models.EmailField()
    phone = models.CharField(max_length=15, validators=[mobile_valid])
    date_order = models.DateField()
    time_order = models.TimeField()
    of_people = models.PositiveSmallIntegerField()
    message = models.TextField(max_length=300)
    is_processed = models.BooleanField(default=False)
    date = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('-date',)
        verbose_name = "Замовлення"

    def __str__(self):
        return f"{self.name}: {self.phone}: {self.message[:20]}..."