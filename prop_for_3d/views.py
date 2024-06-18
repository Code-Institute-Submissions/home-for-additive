from django.shortcuts import render, get_object_or_404, redirect
from django.views import generic
from django.contrib import messages
from .models import Prop
from django.http import HttpResponse
from .forms import NewProposal

# Create your views here.

# class PropList(generic.ListView):
#     model = Prop

# def index(request):
#     return HttpResponse('Hello, addictive!')

class PropList(generic.ListView):
    model = Prop
    queryset = Prop.objects.filter(status=1)
    template_name = "proposal.html"
    template_name = "prop_for_3d/index.html"


def index(request):
    return render(request, 'prop_for_3d/index.html')


def team(request):    
    return render(request, 'prop_for_3d/team.html')


def facility(request):
    return render(request, 'prop_for_3d/facility.html')


# def proposal(request):
#     return render(request, 'prop_for_3d/proposal.html')

# def proposal(request, slug):
#     queryset = Prop.objects.filter(status=1)
#     prop = get_object_or_404(queryset, slug=slug)
#     return render(request, "prop_for_3d/proposal.html", {"prop": prop},)

def proposal(request):
    proposals = Prop.objects.filter(status=1)
    print(proposals)
    return render(request, 'prop_for_3d/proposal.html', {'proposals': proposals})

def prop_single(request, slug):
    queryset = Prop.objects.filter(status=1)
    prop = get_object_or_404(queryset, slug=slug)    
    # new_proposal = NewProposal()
    return render(
        request,
        'prop_for_3d/prop_single.html',
        {
            "prop" : prop,
            #"new_proposal": new_proposal,
            },
        )

#def new_prop(request):
#    new_prop = NewProposal()
#    return render(request, 'prop_for_3d/new_prop.html', {"new_prop": new_prop,},)


#def submit_new_prop(request):
#    if request.method == "POST":
#        new_prop = NewProposal(data=request.POST)
#        print('new_prop')
#        if new_prop.is_valid():
#            new_prop.save()
#            messages.add_message(request, messages.SUCCESS, "Thanks for sharing your idea!")
#            new_prop = NewProposal()
#    return render(request, 'prop_for_3d/confirmation.html')

#def new_prop(request):
#    new_prop = NewProposal()
#    return render(request, 'prop_for_3d/new_prop.html', {"new_prop": new_prop,},)

def submit_new_prop(request):
    if request.method == "POST":
        new_prop = NewProposal(data=request.POST)
        new_prop.slag = 'rrr'
        print(new_prop)
        if new_prop.is_valid():
            new_prop.save()
            messages.add_message(request, messages.SUCCESS, "Thanks for sharing your idea!")
            new_prop = NewProposal()
            return redirect ('proposal')
    
    content = {"new_prop": NewProposal(),}
    print(content)
    return render (request, "prop_for_3d/new_prop.html", content)
        
        