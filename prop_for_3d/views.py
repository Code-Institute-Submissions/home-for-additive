from django.views.generic import TemplateView, ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Prop
from django.urls import reverse_lazy


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


# Classes for pages with dynamic content:


class PropsView(ListView):
    """
    Shows page with all proposals in the list.
    Returns all published posts in :model:`blog.Post`
    and displays them in a page of six posts.
    **Context**

    ``queryset``
        All published instances of :model:`blog.Post`
    ``paginate_by``
        Number of posts per page.

    **Template:**

    :template:`blog/index.html
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
    template_name = "prop_for_3d/edit_prop.html"
    fields = ('title', 'keywords', 'content')


class DeletePropView(DeleteView):
    """
    Delete selected proposal. Check if the user is authorised
    """
    model = Prop
    success_url = reverse_lazy('proposals')
    template_name = "prop_for_3d/delete.html"



