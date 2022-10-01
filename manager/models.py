from django.db import models


# Create your models here.
class UserReservations(models.Model):
    name = models.CharField(max_length=30)
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    date_order = models.DateField()
    time_order = models.TimeField()
    of_people = models.PositiveSmallIntegerField()
    message = models.TextField(max_length=300)
    is_processed = models.BooleanField(default=False)
    date = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('-date',)
        verbose_name = "Замовлення"
        verbose_name_plural = "Замовлення"

    def __str__(self):
        return f"{self.name}: {self.phone}: {self.message[:20]}..."

