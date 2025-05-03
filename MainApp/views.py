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
def main(request):
    return render(request, "index.html")

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
    item = None
    for i in items:
        if i["id"] == item_id:
            item = i
            break

    if item is None:
        text = f"<h1>Товар с id={item_id} не найден</h1>"
        return HttpResponse(text)

    text = f"<h1>{item['name']}</h1><p>Количество: {item['quantity']}</p>"
    return HttpResponse(text)

def items_list(request):
    text = "<h1>Список товаров</h1><ol>"

    for item in items:
        text += f"<li>{item['name']}(осталось: {item['quantity']})</li>"

    text += "</ol>"

    return HttpResponse(text)

    