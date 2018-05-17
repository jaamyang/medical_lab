from django.db import models
from django.contrib.auth.models import User
from django.db.models.fields import exceptions
from ckeditor_uploader.fields import RichTextUploadingField  
from download.models import  Download_file

# Create your models here.

class Type(models.Model):
    name = models.CharField(max_length = 30)    

    def __str__(self):
        return self.name

class Text(models.Model):
    title = models.CharField(max_length = 100)
    author = models.ForeignKey(User,on_delete = models.DO_NOTHING)
    text_type = models.ForeignKey(Type,null = True, on_delete = models.DO_NOTHING)
    content = RichTextUploadingField()
    file = models.ManyToManyField(Download_file,blank = True)
    created_time = models.DateTimeField(auto_now_add = True)
    last_updated = models.DateTimeField(auto_now = True)
    is_delete = models.BooleanField(default = False)

    def __str__(self):
        return '<文章：%s>' %self.title 

class read_num(models.Model):
    text = models.OneToOneField(Text,on_delete = models.DO_NOTHING)
    num = models.IntegerField(default = 0)


class User(models.Model):
    name = models.CharField(max_length = 20)
    password = models.CharField(max_length = 16)
    