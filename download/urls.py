from django.urls import path
from . import views

urlpatterns = [
    path('',views.download,name = 'download'),
    path('file/',views.file_download,name = 'file_download'),
    path('test/',views.test,name = 'just_test'),
]