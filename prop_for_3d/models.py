from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from django.core.mail import send_mail
from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver

OPTIONS = (('Approved', 'Approved'), ('Decline', 'Decline'), )


class Prop(models.Model):
    title = models.CharField(max_length=200, unique=True)
    keywords = models.CharField(max_length=300, unique=True)
    student = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="proposal")
    content = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-created_on"]

    def __str__(self):
        return self.title + ' | ' + str(self.student)

    def get_absolute_url(self):
        return reverse('create_edit_confirm')


class Assessment(models.Model):
    assessment = models.OneToOneField(
        Prop, on_delete=models.CASCADE, related_name='assessment')
    supervisor = models.ForeignKey(
        User, on_delete=models.SET_NULL, null=True, related_name=(
            'supervisors_feedback'))
    content = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    approved = models.CharField(choices=OPTIONS, max_length=15, default='-')

    def __str__(self):
        return (
            f"Assessment for '{self.assessment.title}' "
            f"by {self.supervisor.username} | Status: {self.approved}"
        )


# Signal to send an email after an assessment is created or updated
@receiver(post_save, sender=Assessment)
def send_assessment_email(sender, instance, **kwargs):
    # Prepare email details
    subject = (
        f"Proposal {instance.assessment.title} has been {instance.approved}")
    message = (
        f"Dear {instance.assessment.student.username},\n\n"
        f"Your proposal titled '{instance.assessment.title}' has got status: "
        f"'{instance.approved}' by {instance.supervisor.username}.\n\n"
        f"Feedback:\n{instance.content}\n\n"
        f"If you have any questions, feel free to contact "
        f"your supervisor at: {instance.supervisor.email}\n\n"
        "Best regards,\nThe Supervisory Team"
    )

    # Send email to the student
    send_mail(
        subject,
        message,
        settings.DEFAULT_FROM_EMAIL,
        [instance.assessment.student.email],
        fail_silently=False,
    )
