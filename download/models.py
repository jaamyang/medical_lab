from django.db import models
from django.contrib.auth.models import Group

# Create your models here.

class Download_file(models.Model):
    file_name = models.CharField(max_length = 100)
    file = models.FileField(upload_to = 'files/%Y/%m/%d/',null = True,blank = True)
    upload_date = models.DateTimeField(auto_now_add = True)
    download_permission = models.ManyToManyField(Group)
    descript = models.TextField(null = True,blank = True)

    def __str__(self):
        return '<文件:%s>' %self.file_name

