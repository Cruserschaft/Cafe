from django.urls import path
from .views import *

app_name = "manager"

urlpatterns = [
    path("", reservation_list, name="reservation_list"),
    path("update/<int:pk>/", reservation_update, name="reservation_close"),

]