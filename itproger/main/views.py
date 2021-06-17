from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return HttpResponse('Проверка связи')

def about(request):
    return HttpResponse("Страница по нас")