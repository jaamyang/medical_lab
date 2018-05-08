from django.urls import path
from . import views

urlpatterns = [
    path('',views.data_visualization,name = 'data_util'),
]