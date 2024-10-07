from django.urls import path
from . import views
from .views import *

urlpatterns = [
    path('', views.Index, name="Index"),
    path('results/', Results.as_view(), name="results"),
]