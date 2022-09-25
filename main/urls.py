from django.urls import path
from .views import *
import re


urlpatterns = [
    path("", start),
]