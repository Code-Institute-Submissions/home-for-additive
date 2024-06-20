from . import views
from django.urls import path
from .views import HomeView, TeamView, FacilityView, PropsView, SingleView, CreatePropView, UpdatePropView, DelePropView

urlpatterns = [
    path('', HomeView.as_view(), name="home"),
    path('team/', TeamView.as_view(), name="team"),
    path('facility/', FacilityView.as_view(), name="facility"),
    path('proposals/', PropsView.as_view(), name="proposals"),
    path('proposal/<int:pk>', SingleView.as_view(), name="prop_single"),
    path('proposals/create_new', CreatePropView.as_view(), name="create_new"),
    ]




#path('index/', views.index, name="index"),
    #path('team/', views.team, name="team"),
    #path('facility/', views.facility, name="facility"),
    #path('proposals/', views.PropsView.as_view(), name="proposals"),
    #path('<slug:slug>/', views.prop_single, name="prop_single"),
    #path('proposal/new_prop/', views.submit_new_prop, name="new_prop"),
    #path('new_prop/confirmation/', views.submit_new_prop, name="submit_new_prop"), # name="?" check
    #path('update_prop/<int:pk>/', UpdatePropView.as_view(), name="update_prop")
         #views.prop_edit, name='edit_prop'), 