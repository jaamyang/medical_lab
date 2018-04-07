from django.contrib import admin
from django.contrib.admin import AdminSite
from download import models
from .models import Text,Type

# Register your models here.
@admin.register(Text)
class TextAdmin(admin.ModelAdmin):
    list_display = ('title','author','text_type','created_time','is_delete')
    search_fields = ('title',)
    filter_horizontal = ('file',)

@admin.register(Type)
class TypeAdmin(admin.ModelAdmin):
    list_display = ('name',)


class MyAdminSite(admin.AdminSite):
    site_header = '医疗大数据研究室管理'  # 此处设置页面显示标题
    site_title = '医疗大数据'  # 此处设置页面头部标题
 
admin_site = MyAdminSite(name='management')
admin_site.register(Type)
admin_site.register(Text)
admin_site.register(models.Download_file)