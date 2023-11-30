from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def index(request):
    return render(request,'main/index.html')

def news(request):
    return render(request,'main/news.html')

def new(request,n):
    _url = f'main/new_{n}.html'
    return render(request,f'main/news_{n}.html')

def about(request):
    return HttpResponse('<h1> о нас </h1>')

def contacts(request):
    return HttpResponse('<h1> контакты </h1>')

def sidebar(request):
    return render(request,'main/sidebar.html')
def registration(request):
    return render(request,'main/registration.html')
def user_account(request):
    return render(request,'main/user_account.html')
def about(request):
    return render(request,'main/about.html')


def custom_404(request, exception):
    # return render(request,'main/sidebar.html')
    return HttpResponse(f'Введен неверный запрос, или страница еще в разработке:{exception}')