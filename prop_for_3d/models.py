from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

STATUS = ((0, "Draft"), (1, "Submitted"))


class Prop(models.Model):
    title = models.CharField(max_length=200, unique=True)    
    keywords = models.CharField(max_length=300, unique=True)
    email = models.EmailField(max_length=200)
    student = models.ForeignKey(User, on_delete=models.CASCADE, related_name="proposals")
    content = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS, default=1)
    
    class Meta:
        ordering = ["-created_on"]
    
    def __str__(self):
        return self.title + ' | ' + str(self.student)
    
    def get_absolute_url(self):
        return reverse('proposals')


