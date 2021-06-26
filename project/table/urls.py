from django.urls import path
from . import views

urlpatterns = (
    path('', views.index),
    path("dump", views.dump),
    path("ajax", views.ajax),
)
