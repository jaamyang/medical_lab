from django.urls import path
from . import views

urlpatterns = [
    path('',views.download,name = 'download'),
    path('<int:file_pk>',views.file_download,name = 'file_download'),
]