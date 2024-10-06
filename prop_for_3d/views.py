from django.urls import reverse_lazy, reverse
from django.views.generic import TemplateView, ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView
from django.views.generic.edit import DeleteView, FormMixin
from django.shortcuts import get_object_or_404, redirect, render
from .models import Prop, Assessment
from .forms import CommentOnProp, NewProposal, CustomUserCreationForm
from django.contrib import messages
from django.core.mail import send_mail
from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login

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


class CreateEditConfirm(TemplateView):
    """
    Render and show 'Update confirmation' page.
     **Template:**
    :template:`prop_for_3d/update_confirm.html`
    """
    template_name = "prop_for_3d/create_edit_confirm.html"


class DeleteConfirmView(TemplateView):
    """
    Render and show 'Delete confirmation' page.
     **Template:**
    :template:`prop_for_3d/delete_confirm.html`
    """
    template_name = "prop_for_3d/delete_confirm.html"


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
    fields = ('title', 'keywords', 'content')

    def form_valid(self, form):
        form.instance.student = self.request.user
        return super().form_valid(form)


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
    success_url = reverse_lazy('delete_confirm')
    template_name = "prop_for_3d/delete.html"


class ProposalAssessmentView(FormMixin, DetailView):
    model = Prop
    template_name = "prop_for_3d/prop_assessment.html"
    context_object_name = 'proposal'
    form_class = CommentOnProp

    def get_success_url(self):
        return reverse('prop_single', kwargs={'pk': self.object.pk})

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        try:
            assessment = self.object.assessment
            context['already_assessed'] = True
        except Assessment.DoesNotExist:
            context['form'] = self.get_form()
            context['already_assessed'] = False
        return context

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        try:
            # Check if an assessment already exists
            assessment = self.object.assessment
            messages.error(
                self.request, "This proposal has already been assessed.")
            return redirect('prop_single', pk=self.object.pk)
        except Assessment.DoesNotExist:
            form = self.get_form()
            if form.is_valid():
                return self.form_valid(form)
            else:
                return self.form_invalid(form)

    def form_valid(self, form):
        assessment = form.save(commit=False)
        assessment.supervisor = self.request.user
        assessment.assessment = self.object
        assessment.save()

        # Send the email to the student
        subject = (
            f"Proposal {self.object.title} has got "
            f"the status: '{assessment.approved}'"
        )
        message = (
            f"Dear {self.object.student.username},\n\n"
            f"Your proposal titled '{self.object.title}' has got "
            f"status: '{assessment.approved}' by "
            f"{assessment.supervisor.username}.\n\n"
            f"Comments:\n{assessment.content}\n\n"
            f"If you have any questions, feel free to contact your "
            f"supervisor at: {assessment.supervisor.email}\n\n"
            "Best regards,\nThe Supervisory Team"
        )

        send_mail(
            subject,
            message,
            settings.DEFAULT_FROM_EMAIL,
            [self.object.student.email],
            fail_silently=False,
        )

        messages.success(self.request, 'Assessment submitted successfully!')
        return super().form_valid(form)


def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('proposals')
        else:
            print(form.errors)
    else:
        raise Exception('Error happened')
        form = CustomUserCreationForm()

    return render(request, 'registration/register.html', {'form': form})
