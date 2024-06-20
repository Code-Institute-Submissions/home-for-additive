from . import views
from django.urls import path
from .views import UpdatePropView

urlpatterns = [
    path('', views.PropList.as_view(), name="home"),
    path('index/', views.index, name="index"),
    path('team/', views.team, name="team"),
    path('facility/', views.facility, name="facility"),
    path('proposal/', views.proposal, name="proposal"),
    path('<slug:slug>/', views.prop_single, name="prop_single"),
    path('proposal/new_prop/', views.submit_new_prop, name="new_prop"),
    path('new_prop/confirmation/', views.submit_new_prop, name="submit_new_prop"), # name="?" check
    path('update_prop/<int:pk>/', UpdatePropView.as_view(), name="update_prop")
         #views.prop_edit, name='edit_prop'),    
    ]

