from django.shortcuts import render

# Create your views here.
def index(request):    
    return HttpResponse('Главная страница')

def group_posts(request):
    return HttpResponse('Список мороженого')
