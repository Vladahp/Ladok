from unicodedata import category

from django.shortcuts import render



def index(request):
    return render(request, 'main/index.html')

def about(request):
    return render(request, 'main/about.html')

def catalog(request):
    categories = ['Категорія 1','Категорія 2','Категорія 3']
    return render(request, 'main/catalog.html', {'categories': categories})
