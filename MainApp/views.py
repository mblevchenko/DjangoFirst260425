from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def homepage(request):
    text="""
    <h1>"Изучаем django"</h1>
    <strong>Автор</strong>: <i>Левченко М.Б.</i>
    """
    return HttpResponse(text)

def about(request):
    text="""Имя: Максим <br>
Отчество: Борисович <br>
Фамилия: Левченко <br>
телефон: 8-800-555-35-35 <br>
email: ya@bk.ru <br>"""
    return HttpResponse(text)