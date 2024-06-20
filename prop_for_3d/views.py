from django.shortcuts import render, get_object_or_404, redirect
from django.views import generic
from django.contrib import messages
from django.views.generic import UpdateView
from django.http import HttpResponseRedirect
from .models import Prop
from .forms import NewProposal

# Create your views here.


class PropList(generic.ListView):
    """
    Model of proposal for proposed idea.
    Returns all published posts in :model:`prop_for_3d.Prop`.
    **Context**

    ``queryset``
        All published instances of :model:`prop_for_3d.Prop`

    **Template:**

    :template:`prop_for_3d/index.html`
    """

    model = Prop
    queryset = Prop.objects.filter(status=1)
    template_name = "prop_for_3d/index.html"

class UpdatePropView(UpdateView):
    model = Prop
    template_name = "prop_for_3d/update_prop.html"
    fields = ('title', 'keywords', 'content', )


def index(request):
    """
    Display static 'home' page.

    **Template:**

    :template:`prop_for_3d/index.html`

    """
    return render(request, 'prop_for_3d/index.html')


def team(request):
    """
    Display static 'team' page.

    **Template:**

    :template:`prop_for_3d/team.html`

    """
    return render(request, 'prop_for_3d/team.html')


def facility(request):
    """
    Display static 'facility' page.

    **Template:**

    :template:`prop_for_3d/facility.html`

    """
    return render(request, 'prop_for_3d/facility.html')


def proposal(request):
    """
    Display an individual :model:`prop_for_3d.Prop`.

    **Context**

    ``proposal``
        An instance of :model:`prop_for_3d.Prop`.

    **Template:**

    :template:`prop_for_3d/proposal.html`

    """
    proposals = Prop.objects.filter(status=1)
    print(proposals)
    return render(
        request,
        'prop_for_3d/proposal.html',
        {'proposals': proposals},
        )


def prop_single(request, slug):
    """
    Display an individual :model:`prop_for_3d.Prop`.

    **Context**

    ``prop``
        An instance of :model:`prop_for_3d.Prop`.

    **Template:**

    :template:`prop_for_3d/prop_single.html`

    """
    queryset = Prop.objects.filter(status=1)
    prop = get_object_or_404(queryset, slug)
    return render(
        request,
        'prop_for_3d/prop_single.html',
        {"prop": prop, },
        )


def submit_new_prop(request):
    """
    Display, fill and submit the 'new proposal' form.

    Form:
    ``new_prop``
    An instance of :form:`prop_for_3d/NewProposal`

    **Template:**

    :template:`prop_for_3d/prop_new_prop.html`
    """
    if request.method == "POST":
        new_prop = NewProposal(data=request.POST)
        #new_prop.slug = 'rrr' ## rrr - just testing
        print(new_prop)
        if new_prop.is_valid():
            new_prop.save()
            messages.add_message(
                request, messages.SUCCESS, "Thanks for sharing your idea!")
            new_prop = NewProposal()
            return redirect('team')

    content = {"new_prop": NewProposal(), }
    print(content)
    return render(request, 'prop_for_3d/new_prop.html', content)

"""
def prop_edit(request, slug):    
    proposal = get_object_or_404(Prop, slug=slug)
    if request.method == 'POST':
        proposal.title = request.POST.get('title')
        proposal.keywords = request.POST.get('keywords')
        proposal.content = request.POST.get('content')
        proposal.save()
        return redirect('home')
    context = {
        'proposal':proposal
    }
    return render (request, 'edit_prop.html', context)
        
    

    if request.method == "POST":
        queryset = Prop.objects.filter(status=1)
        proposal = get_object_or_404(queryset, slug=slug)
        prop_form = NewProposal(data=request.POST, instance=proposal)
        if prop_form.is_valid() and proposal.student == request.user: # .iser or .student?
            proposal = prop_form.save(commit=False)
            proposal.post = proposal
            #proposal.approved = True # True or False?
            proposal.save()
            messages.add_message(request, messages.SUCCESS, 'Poposal Updated!')
        else:
            messages.add_message(request, messages.ERROR, 'Error updating comment!')

    #return HttpResponseRedirect(reverse('prop_single', args=[slug]))
    return redirect('proposal')
    """