from django.shortcuts import render

# Create your views here.
def data_visualization(request):
    return render(request,'data_visualization.html')