from django.shortcuts import render
from django.http import HttpResponse
from django.http import Http404

items = [
   {"id": 1, "name": "Кроссовки abibas" ,"quantity":5},
   {"id": 2, "name": "Куртка кожаная" ,"quantity":2},
   {"id": 5, "name": "Coca-cola 1 литр" ,"quantity":12},
   {"id": 7, "name": "Картофель фри" ,"quantity":0},
   {"id": 8, "name": "Кепка" ,"quantity":124},
]

author = [
    {"Имя": "Максим"},
    {"Отчество": "Борисович"}, 
    {"Фамилия": "Левченко"},
    {"Телефон": "8-800-555-35-35"},
    {"email": "ya@bk.ru"}
]
# Create your views here.
def main(request):
    context = {
        "name": "Levchenko Maksim",
        "email": "ya@bk.ru",
        "phone": "88005553535"
    }
    return render(request, "index.html", context)

def about(request):
    context = {
        "author":author
    }
    return render(request, "about.html", context)

def items_list(request):
    return render(request, 'items.html', context={'items': items})

def item_page(request, item_id):
    # Ищем товар
    for item in items:
        if item['id'] == item_id:
            return render(request, 'item.html', context={'item': item})
    
    raise Http404(f"Товар с id={item_id} не найден")
    



    