from . import views
from django.urls import path

urlpatterns = [
    path('', views.About_view, name='about'),
]