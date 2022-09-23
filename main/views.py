from django.shortcuts import render
from django.http import HttpResponse


def start(request):
    print(render(request, "main/base.html", {"title": "Головна сторінка"}))
    return render(request, "main/base.html", {"title": "Головна сторінка"})