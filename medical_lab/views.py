from django.shortcuts import render,get_object_or_404,HttpResponse,redirect
from homesite import models
from django.contrib import auth
from download.models import  Download_file

def home(request):
    context = {}
    #context ['type'] = models.Type.objects.all()
    news = get_object_or_404(models.Type,name = '新闻动态')
    achievements = get_object_or_404(models.Type,name = '科研成果')
    activity = get_object_or_404(models.Type,name = '学术活动')
    notice = get_object_or_404(models.Type,name = '通知公告')
    context ['news'] = models.Text.objects.filter(text_type = news,is_delete = False).order_by('-created_time')[:5]
    context ['activity'] = models.Text.objects.filter(text_type = activity).order_by('-created_time')[:5]
    context ['achievements'] = models.Text.objects.filter(text_type = achievements).order_by('-created_time')[:5]
    context ['notice'] = models.Text.objects.filter(text_type = notice).order_by('-created_time')[:5]
    context ['texts'] = models.Text.objects.filter(is_delete = False).order_by('-created_time')[:5]

    return render(request,'home.html',context)

def activities(request):
    context = {}
    news = get_object_or_404(models.Type,name = '新闻动态')
    achievements = get_object_or_404(models.Type,name = '科研成果')
    activity = get_object_or_404(models.Type,name = '学术活动')
    notice = get_object_or_404(models.Type,name = '通知公告')
    context ['news'] = models.Text.objects.filter(text_type = news,is_delete = False).order_by('-created_time')
    context ['activity'] = models.Text.objects.filter(text_type = activity).order_by('-created_time')
    context ['achievements'] = models.Text.objects.filter(text_type = achievements).order_by('-created_time')
    context ['notice'] = models.Text.objects.filter(text_type = notice).order_by('-created_time')
    context ['texts'] = models.Text.objects.filter(is_delete = False).order_by('-created_time')[:5]
    return render(request,'activities.html',context)

def intro(request):
    return render(request,'intro.html')

def members(request):
    return render(request,'members.html')

def achievements(request):
    context = {}
    news = get_object_or_404(models.Type,name = '新闻动态')
    achievements = get_object_or_404(models.Type,name = '科研成果')
    activity = get_object_or_404(models.Type,name = '学术活动')
    notice = get_object_or_404(models.Type,name = '通知公告')
    context ['news'] = models.Text.objects.filter(text_type = news,is_delete = False).order_by('-created_time')
    context ['activity'] = models.Text.objects.filter(text_type = activity).order_by('-created_time')
    context ['achievements'] = models.Text.objects.filter(text_type = achievements).order_by('-created_time')
    context ['notice'] = models.Text.objects.filter(text_type = notice).order_by('-created_time')
    context ['texts'] = models.Text.objects.filter(is_delete = False).order_by('-created_time')[:5]
    return render(request,'achievements.html',context)

def login(request):
    if request.method == 'POST':
        username = request.POST.get('username','')
        password = request.POST.get('password','')
        user = auth.authenticate(username = username,password = password)
        if user is not None:
            auth.login(request,user)
            return redirect('/')
        else:
            #raise forms.ValidationError(u"两次密码必须一致")
            #return render(request,'error.html',{'message':'用户名或密码错误!'})
            return render(request,'login.html',{'error_message':'true'})
    else:
        return render(request,'login.html')


def text_detail(request,text_pk):
    context = {}
    text = get_object_or_404(models.Text,pk = text_pk)
    context ['text'] = text
    return render(request,'detail.html',context) 
 