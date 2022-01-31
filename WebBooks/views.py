from django.shortcuts import render
from django.http import HttpResponse

# def index(request):
#     return render(request, 'WebBooks/index.html')


def index(request):
    return render(request, 'WebBooks/index.html')

def profile(request):
    return HttpResponse('<h1>this page profile</h1>')
