from django.shortcuts import render,get_object_or_404,redirect
from django.http import FileResponse 
from django.contrib.auth.models import User,Group
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from . import models
# Create your views here.

def list_in(list1,list2):
        if list1:
            for e in list1:
                if e not in list2:
                    return False
            else:
                return True
        else:
            return False

def download(request,error_message):
    # if error_message:
    #     context = {}    
    #     files = models.Download_file.objects.all().order_by('-upload_date')
    #     pages = Paginator(files, 5) 
    #     current_page = request.GET.get("page",1)
    #     context['files'] =  pages.page(current_page)
    #     context['page'] = pages.get_page(current_page)
    #     context['error_message'] = 'true'
    #     return render(request,'download.html',context)
    # else:
        #error_message = request.POST.get("error_message",'false')
        context = {}    
        files = models.Download_file.objects.all().order_by('-upload_date')
        pages = Paginator(files, 5) 
        current_page = request.GET.get("page",1)
        context['files'] =  pages.page(current_page)
        context['page'] = pages.get_page(current_page)
        context['error_message'] = error_message
        return render(request,'download.html',context)





    # context = {}    
    # files = models.Download_file.objects.all().order_by('-upload_date')
    # pages = Paginator(files, 5) # Show 25 contacts per page
    # current_page = request.GET.get("page",1)
    # context['files'] =  pages.page(current_page)
    # context['page'] = pages.get_page(current_page)
    # context['error_message'] = error_message
    # return render(request,'download.html',context)

def file_download(request,file_pk):
    download_file = get_object_or_404(models.Download_file,pk = file_pk)

    user_group = []
    file_group = []
    if request.user.is_authenticated:
        for e in get_object_or_404(User,username = request.user).groups.all():
            user_group.append(e.name)    
    for e in download_file.download_permission.all():
        file_group.append(e.name)

    #print(user_group,file_group)
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
        error_message = 'true'
        return download(request,error_message)
        # error_message = 'true'
        # flag = True
        # return redirect(download,error_message='true')


