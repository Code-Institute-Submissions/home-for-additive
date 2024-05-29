from django.db import models
from django.contrib.auth.models import User

STATUS = ((0, "Draft"), (1, "Published"))

# Create your models here.
class Prop(models.Model):
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    student = models.ForeignKey(User, on_delete=models.CASCADE, related_name="proposals")
    content = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS, default=0)


class Assessment(models.Model):
    proposal = models.ForeignKey(Prop, on_delete=models.CASCADE, related_name="assessors_reply")
    # slug = models.SlugField(max_length=200, unique=True)
    assessor = models.ForeignKey(User, on_delete=models.CASCADE, related_name="assessment") # Must be someone else other than the 'User'?
    comment = models.TextField()
    approved_on = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS, default=0)

