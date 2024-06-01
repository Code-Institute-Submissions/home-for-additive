from . import views
from django.urls import path

urlpatterns = [
    path('', views.PropList.as_view(), name="home")
]

