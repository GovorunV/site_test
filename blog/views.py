from django.shortcuts import render
from math import pi
from .models import News

news = [
    {
        'title': "Первая запись",
        'text': 'Текст для первой записи',
        'date': '11 января',
        'avtor': 'Иванов В.В'
    },
    {
        'title': "Вторая запись",
        'text': 'Текст для первой второй',
        'date': '19 января 2019',
        'avtor': 'Сивро В.В'
    }
]
def home(request): #request обезательно
    date= {
        'news': News.objects.all(),
        'title': 'Гланая страница'
    }
    return render(request, 'blog/home.html', date)
def contact(request): #request обезательно
    return render(request, 'blog/contact.html', {'title': 'Страничка', 'pi': pi})
