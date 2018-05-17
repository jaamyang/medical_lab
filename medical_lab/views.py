from django.shortcuts import render,get_object_or_404,HttpResponse,redirect
from homesite import models
from download import models as dlmod
from django.contrib.auth.models import User
from download.models import  Download_file


def get_text():
    cont = {}
    news = get_object_or_404(models.Type,name = '新闻动态')
    achievements = get_object_or_404(models.Type,name = '科研成果')
    activity = get_object_or_404(models.Type,name = '学术活动')
    notice = get_object_or_404(models.Type,name = '通知公告')
    cont ['news'] = models.Text.objects.filter(text_type = news,is_delete = False).order_by('-created_time')[:5]
    cont ['activity'] = models.Text.objects.filter(text_type = activity,is_delete = False).order_by('-created_time')[:5]
    cont ['achievements'] = models.Text.objects.filter(text_type = achievements,is_delete = False).order_by('-created_time')[:5]
    cont ['notice'] = models.Text.objects.filter(text_type = notice,is_delete = False).order_by('-created_time')[:5]
    cont ['texts'] = models.Text.objects.filter(is_delete = False).order_by('-created_time')[:5]
    return cont

def home(request):
    context = get_text()
    return render(request,'home.html',context)

def activities(request):
    context = get_text()
    return render(request,'activities.html',context)

def intro(request):
    context = {}
    context['intro'] = models.Text.objects.filter(text_type = get_object_or_404(models.Type,name = 'intor'))[0]
    return render(request,'intro.html',context)

def members(request):
    return render(request,'members.html')

def achievements(request):
    context = get_text()
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

def logout_view(request):
    auth.logout(request)
    return redirect(request.META.get('HTTP_REFERER', '/'))


def text_detail(request,text_pk):
    context = {}
    text = get_object_or_404(models.Text,pk = text_pk)
    context['pervious_text'] = models.Text.objects.filter(created_time__lt = text.created_time,is_delete = False).last()
    context['next_text'] = models.Text.objects.filter(created_time__gt = text.created_time,is_delete = False).first()
    context ['text'] = text
    return render(request,'detail.html',context) 
 
def search(request):
    search_key = request.GET.get('search_key')
    search_condition = request.GET.get('condition','title')
    print(search_key,search_condition)
    print(search_condition=='title')
    text_results = []
    file_results = []
    if search_condition =='title':
        text_results = models.Text.objects.filter(title__icontains = search_key)
    elif search_condition == 'author':
        author = get_object_or_404(User,username = search_key)
        text_results = models.Text.objects.filter(author = author)
    elif search_condition == 'content':
        text_results = models.Text.objects.filter(content__icontains = search_key)
    else:
        file_results = dlmod.Download_file.objects.filter(file_name__icontains = search_key)
    return render(request, 'search.html', {'text_results': text_results,'file_results':file_results})

    
