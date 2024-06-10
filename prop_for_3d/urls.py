from . import views
from django.urls import path

urlpatterns = [
    path('', views.PropList.as_view(), name="home"),
    path('index/', views.index, name="home"),
    path('team/', views.team, name="team"),
    path('facility/', views.facility, name="facility"),
    path('proposal', views.proposal, name="proposal"),
    ]

