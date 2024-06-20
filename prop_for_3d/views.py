from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import TemplateView, ListView, DetailView, CreateView, UpdateView, DeleteView
#from django.contrib import messages
#from django.http import HttpResponseRedirect
from .models import Prop
from .forms import NewProposal


# Classes for static pages:

class HomeView(TemplateView):
    """
    Render and show starting ('Home') page
    """
    template_name = "prop_for_3d/index.html"


class TeamView(TemplateView):
    """
    Render and show 'Meet our team' page.
    """
    template_name = "prop_for_3d/team.html"


class FacilityView(TemplateView):
    """
    Render and show 'Facility' page.
    """
    template_name = "prop_for_3d/facility.html"


# Classes wit dynamic content:


class PropsView(ListView):
    """
    Shows page with all proposals in the list.
    """
    model = Prop
    template_name = "prop_for_3d/proposals.html"


class SingleView(DetailView):
    """
    Shows page with a single selected idea proposal.
    """
    model = Prop
    template_name = "prop_for_3d/prop_single.html"


class CreatePropView(CreateView):
    """
    Show a fillable form. The data can be stored in database as an entry.
    """
    model = Prop
    template_name = "prop_for_3d/new_prop.html"
    fields = ('title', 'keywords', 'student', 'content')



class UpdatePropView(UpdateView):
    """
    Update existing proposal.
    """
    model = Prop
    #template_name


class DelePropView():
    """
    Delete selected proposal. Check if the user is authorised
    """


