from django.shortcuts import render
from datetime import datetime
import os


def home(requests):

    definition = {
        'title': 'Главная страница'
    }

    return render(requests, 'base/home.html', definition)


def current_time(requests):
    time_now = datetime.now()
    definition = {
        'title': 'Страница со временем',
        'time_now': time_now,
    }
    return render(requests, 'base/current_time.html', definition)


def workdir(requests):
    my_list = os.listdir()
    my_list_number = []



    definition = {
        'my_list': my_list,
        'title': 'Страница со списком файлов',
    }
    return render(requests, 'base/workdir.html', definition)



