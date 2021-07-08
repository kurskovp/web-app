from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return HttpResponse("<img src='https://itproger.com/img/courses/1479108898.jpg'>")