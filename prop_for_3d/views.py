from django.shortcuts import render
from django.views import generic
from .models import Prop
# from django.http import HttpResponse

# Create your views here.

class PropList(generic.ListView):
    model = Prop

# def index(request):
#     return HttpResponse('Hello, addictive!')



