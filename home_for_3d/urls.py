from django.contrib import admin
from django.urls import path, include
# from prop_for_3d import views as index_views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('prop_for_3d.urls'), name='prop_for_3d'),
    path('summernote/', include('django_summernote.urls')),
    path("accounts/", include("allauth.urls")),      
]
