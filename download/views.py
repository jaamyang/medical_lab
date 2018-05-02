#======================================================================
#
#        Copyright (C) 2018 medical_lab   
#        All rights reserved
#
#        filename :download.view
#
#        created by soaki at 2018.4.1
#
#======================================================================
from django.views.decorators.http import require_POST
from django.shortcuts import render,get_object_or_404,redirect
from django.http import FileResponse,JsonResponse,HttpResponse
from django.contrib.auth.models import User,Group
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib import messages
from django.urls import reverse
from . import models
# Create your views here.

def list_in(list1,list2):
        if list1:
            for e in list1:
                if e in list2:
                    return True
            return False
        else:
            return False

def download(request):
            context = {}    
            files = models.Download_file.objects.all().order_by('-upload_date')
            pages = Paginator(files, 8) 
            current_page = request.GET.get("page",1)
            context['files'] =  pages.page(current_page)
            context['page'] = pages.get_page(current_page)
            return render(request,'download.html',context)

def download_util(request,file_pk):
    download_file = get_object_or_404(models.Download_file,pk = file_pk)
    file=open(download_file.file.path,'rb') 
    response =FileResponse(file)  
    response['Content-Type']='application/octet-stream'  
    response['Content-Disposition']='attachment;filename='+"".join(download_file.file.name.split('/')[-1:]).encode('utf-8').decode('ISO-8859-1')
    return response  

@require_POST
def file_download(request):
    file_pk = request.POST["file_pk"]
    download_file = get_object_or_404(models.Download_file,pk = file_pk)

    user_group = []
    file_group = []
    if request.user.is_authenticated:
        for e in get_object_or_404(User,username = request.user).groups.all():
            user_group.append(e.name)    
    for e in download_file.download_permission.all():
        file_group.append(e.name)

    #print(user_group,file_group)
    if '任何人' in file_group or list_in(user_group,file_group):         
        return HttpResponse(reverse('whatthef', args=[file_pk]))     #download_util(download_file)
    else:
        return HttpResponse('true')

def test(request):
    return render(request,'test.html')

def test_download(request,file_pk):
    download_file = get_object_or_404(models.Download_file,pk = file_pk)
    return download_util(download_file)

