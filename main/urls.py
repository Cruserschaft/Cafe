from django.urls import path
from .views import *


urlpatterns = [
    path("", start),
    path("order/", get_order, name='order')
]