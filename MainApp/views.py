from django.shortcuts import render
from django.http import HttpResponse

items = [
   {"id": 1, "name": "Кроссовки abibas" ,"quantity":5},
   {"id": 2, "name": "Куртка кожаная" ,"quantity":2},
   {"id": 5, "name": "Coca-cola 1 литр" ,"quantity":12},
   {"id": 7, "name": "Картофель фри" ,"quantity":0},
   {"id": 8, "name": "Кепка" ,"quantity":124},
]

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

def item_page(request, item_id):
    for item in items:
        if item["id"] == item_id:
            text = f"<h1>{item['name']}</h1><h2>Количество: {item['quantity']}</h2>"
            return HttpResponse(text) 