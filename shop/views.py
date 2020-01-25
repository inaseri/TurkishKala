from django.shortcuts import render
from .models import AbstractUser, Object
from django.shortcuts import render


def index(request):

    return render(request, 'shop/home.html')
