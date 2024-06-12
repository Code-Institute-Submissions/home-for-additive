from . import views
from django.urls import path

urlpatterns = [
    path('', views.PropList.as_view(), name="home"),
    path('index/', views.index, name="index"),
    path('team/', views.team, name="team"),
    path('facility/', views.facility, name="facility"),
    path('proposal', views.proposal, name="proposal"),
    # path('<slug:slug>/', views.proposal, name='proposal'), #N.b. the slug field: is it in the model?
    # path('proposal/<slug:slug>/', views.proposal, name='proposal'),
    ]

