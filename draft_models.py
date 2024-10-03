from django.urls import reverse_lazy, reverse
from django.views.generic import TemplateView, ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView, FormMixin
from django.shortcuts import get_object_or_404, redirect
from .models import Prop, Assessment
from .forms import CommentOnProp
from django.contrib import messages
from django.core.mail import send_mail
from django.conf import settings

# Static and dynamic content views...

class ProposalAssessmentView(FormMixin, DetailView):
    """
    Shows the proposal and the form for the assessor to leave a comment and
    approve/decline it.
    """
    model = Prop
    template_name = "prop_for_3d/prop_assessment.html"
    context_object_name = 'proposal'
    form_class = CommentOnProp

    def get_success_url(self):
        return reverse('proposal_assessment', kwargs={'pk': self.object.pk})

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = self.get_form()
        return context

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()  # Get the current proposal
        form = self.get_form()
        if form.is_valid():
            return self.form_valid(form)
        else:
            return self.form_invalid(form)

    def form_valid(self, form):
        # Save the assessment
        assessment = form.save(commit=False)
        assessment.supervisor = self.request.user
        assessment.assessment = self.object
        assessment.save()

        # Send the email to the student
        subject = f"Proposal {self.object.title} has been {assessment.approved}"
        message = (
            f"Dear {self.object.student.username},\n\n"
            f"Your proposal titled '{self.object.title}' has been {assessment.approved} by {assessment.supervisor.username}.\n\n"
            f"Comments:\n{assessment.content}\n\n"
            f"If you have any questions, feel free to contact your supervisor at: {assessment.supervisor.email}\n\n"
            "Best regards,\nThe Supervisory Team"
        )

        send_mail(
            subject,
            message,
            settings.DEFAULT_FROM_EMAIL,
            [self.object.student.email],
            fail_silently=False,
        )

        # Display a success message
        messages.success(self.request, 'Assessment submitted successfully!')

        return super().form_valid(form)

    def form_invalid(self, form):
        messages.error(self.request, "There was an error with your submission. Please correct the fields and try again.")
        return self.render_to_response(self.get_context_data(form=form))

    def dispatch(self, request, *args, **kwargs):
        proposal = self.get_object()
        if hasattr(proposal, 'assessment'):
            messages.error(request, "This proposal has already been assessed.")
            return redirect('prop_single', pk=proposal.pk)
        return super().dispatch(request, *args, **kwargs)
