#Указатели второго уровня
from django.urls import path
from . import views #  имортируем файл(views) с этого же каталога(.)

urlpatterns = [
    path('', views.home, name='blog-home'), #где views это файл а home функция которую мы вызываем,name это как бы сылка по которой можно к ней обращатся
    path('contact/', views.contact, name='blog-contact')
] # где '' это домашняя страница
