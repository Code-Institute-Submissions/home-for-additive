from django.shortcuts import render
from django.views import generic
from .models import Prop
from django.http import HttpResponse

# Create your views here.

class PropList(generic.ListView):
    model = Prop

# def index(request):
#     return HttpResponse('Hello, addictive!')

class PropList(generic.ListView):
    queryset = Prop.objects.filter(status=1)
    # template_name = "prop_list.html"
    template_name = "prop_for_3d/index.html"


def index(request):
    return render(request, 'prop_for_3d/index.html')


def team(request):    
    return render(request, 'prop_for_3d/team.html')


def facility(request):
    return render(request, 'prop_for_3d/facility.html')


def proposal(request):
    return render(request, 'prop_for_3d/proposal.html')


