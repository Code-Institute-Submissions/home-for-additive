from django.views.generic import TemplateView, ListView, DetailView
from django.views.generic import CreateView, UpdateView, DeleteView
from .models import Prop
from django.urls import reverse_lazy

# Classes for static pages:


class HomeView(TemplateView):
    """
    Render and show starting ('Home') page.
    **Template:**
    :template:`prop_for_3d/index.html`
    """
    template_name = "prop_for_3d/index.html"


class TeamView(TemplateView):
    """
    Render and show 'Meet our team' page.
     **Template:**
    :template:`prop_for_3d/team.html`
    """
    template_name = "prop_for_3d/team.html"


class FacilityView(TemplateView):
    """
    Render and show 'Facility' page.
     **Template:**
    :template:`prop_for_3d/facility.html`
    """
    template_name = "prop_for_3d/facility.html"


# Classes for pages with dynamic content:


class PropsView(ListView):
    """
    Shows page with all proposals in the list.
    Returns all published proposals in :model:`prop_for_3d.Prop`.
    and displays them in a list page.
    Not paginated.
    **Context**
    ``queryset``
        All instances with 'submitted' status of :model:`prop_for_3d.Prop`.
    ``paginate_by``
        Not paginated.
    **Template:**
    :template:`prop_for_3d/proposals.html`
    """
    model = Prop
    template_name = "prop_for_3d/proposals.html"


class SingleView(DetailView):
    """
    Shows page with a single selected idea proposal :model:`prop_for_3d.Prop`.
    **Context**
    ``queryset``
        Instances with 'submitted' status and pk of :model:`prop_for_3d.Prop`.
    ``paginate_by``
        Not paginated.
    **Template:**
    :template:`prop_for_3d/prop_single.html`
    """
    model = Prop
    template_name = "prop_for_3d/prop_single.html"


class CreatePropView(CreateView):
    """
    View to create and submit a proposal.
    """
    model = Prop
    template_name = "prop_for_3d/new_prop.html"
    fields = ('title', 'keywords', 'student', 'content')


class UpdatePropView(UpdateView):
    """
    View to update and submit an updated proposal.
    """
    model = Prop
    template_name = "prop_for_3d/edit_prop.html"
    fields = ('title', 'keywords', 'content')


class DeletePropView(DeleteView):
    """
    View to delete proposal.
    """
    model = Prop
    success_url = reverse_lazy('proposals')
    template_name = "prop_for_3d/delete.html"
