from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def homepage(request):
    text="""
    <h1>"Изучаем django"</h1>
    <strong>Автор</strong>: <i>Левченко М.Б.</i>
    """
    return HttpResponse(text)