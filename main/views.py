from django.shortcuts import render
from django.http import HttpResponse


def start(request):
    return HttpResponse(f"<h1>Hello</h1>")