from django.shortcuts import render,get_object_or_404
from django.http import FileResponse 
from django.contrib.auth.models import User,Group
from . import models
# Create your views here.

def list_in(list1,list2):
        for e in list1:
            if e not in list2:
                return False
        else:
            return True

def download(request,error_message):
    context = {}
    context['files'] = models.Download_file.objects.all()
    context['error_message'] = error_message
    return render(request,'download.html',context)

def file_download(request,file_pk):
    download_file = get_object_or_404(models.Download_file,pk = file_pk)

    user_group = []
    file_group = []
    for e in get_object_or_404(User,username = request.user).groups.all():
        user_group.append(e.name)    
    for e in download_file.download_permission.all():
        file_group.append(e.name)

    print(user_group,file_group)
    if '任何人' in file_group:
        file=open(download_file.file.path,'rb')  
        response =FileResponse(file)  
        response['Content-Type']='application/octet-stream'  
        response['Content-Disposition']='attachment;filename='+download_file.file.name
        return response  
    elif list_in(user_group,file_group):
        file=open(download_file.file.path,'rb')  
        response =FileResponse(file)  
        response['Content-Type']='application/octet-stream'  
        response['Content-Disposition']='attachment;filename='+download_file.file.name
        return response  
    else:
        #print(download_file.download_permission)
        #return render(request,'error.html',{'message':'您没有相关权限，请登录或切换用户后再试！'})
        error_message = 'true'
        return download(request,error_message)
        #return render(request,'download.html',{'error_message':'true'})

