from django.db import models
from django.contrib.auth.models import User

STATUS = ((0, "Draft"), (1, "Submitted"))

# Create your models here.
class Prop(models.Model):
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    keywords = models.CharField(max_length=300, unique=True)
    email = models.EmailField(max_length=200)
    student = models.ForeignKey(User, on_delete=models.CASCADE, related_name="proposals")
    content = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS, default=0)
    
    class Meta:
        ordering = ["-created_on"]
    
    def __str__(self):
        return f"The title of this proposal is {self.title}"

# class Assessment(models.Model):
#     proposal = models.ForeignKey(Prop, on_delete=models.CASCADE, related_name="assessors_reply")    
#     assessor = models.ForeignKey(User, on_delete=models.CASCADE, related_name="assessment")
#     comment = models.TextField()
#     approved_on = models.DateTimeField(auto_now_add=True)
#     status = models.IntegerField(choices=STATUS, default=0)
    


    




