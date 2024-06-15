from . import views
from django.urls import path

urlpatterns = [
    path('', views.PropList.as_view(), name="home"),
    path('index/', views.index, name="index"),
    path('team/', views.team, name="team"),
    path('facility/', views.facility, name="facility"),
    path('proposal', views.proposal, name="proposal"),
    path('<slug:slug>/', views.prop_single, name="prop_single"),
    path('proposal/new_prop', views.new_prop, name="new_prop")
    # path('proposal/<slug:slug>/', views.proposal, name='proposal'),
    ]

