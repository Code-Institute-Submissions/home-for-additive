from . import views
from django.urls import path
from .views import HomeView, TeamView, FacilityView, PropsView
from .views import SingleView, CreatePropView, UpdatePropView, DeletePropView

urlpatterns = [
    path('', HomeView.as_view(), name="home"),
    path('team/', TeamView.as_view(), name="team"),
    path('facility/', FacilityView.as_view(), name="facility"),
    path('proposals/', PropsView.as_view(), name="proposals"),
    path('proposal/<int:pk>', SingleView.as_view(), name="prop_single"),
    path('proposals/create_new', CreatePropView.as_view(), name="create_new"),
    path('proposal/edit/<int:pk>', UpdatePropView.as_view(), name="edit"),
    path('proposal/delete/<int:pk>', DeletePropView.as_view(), name="delete"),
    ]
