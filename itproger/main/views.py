from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return HttpResponse('<h3>Это главная страница</h4>')


def about(request):
    return HttpResponse('<h3>Страница про нас</h3><p>Наши последнии новости</p>')


def course(request):
    return HttpResponse('<h3>Страница курсов</h3><p>Это страница курсов!</p>')