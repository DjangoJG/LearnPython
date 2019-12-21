from django.contrib import admin
# Register your models here.
from jgApp.models import Grades,Students

class StudentsExtra(admin.TabularInline):#StackedInline
    model=Students
    extra=1
class GradesAdmin(admin.ModelAdmin):
    # 列表页
    # list_display=[] 显示字段，为字段名称
    # list_filter=[] 过滤字段
    # search_fields=[] 搜索字段
    # list_per_page= 每页行数
    #根据上面StudentsExtra类 增加Grade同时增加Students
    inlines = [StudentsExtra]
    list_display = ['pk','gname','gdate','ggirlnum','gboynum','isDelete']
    list_filter = ['gname']
    search_fields = ['gname']
    search_fields = ['gname']
    list_per_page = 2
    #添加修改
    # fields=[] 增加页面的排序
    # fieldsets[]
    fields=['ggirlnum','gboynum','gname','isDelete','gdate']
admin.site.register(Grades,GradesAdmin)


class StudentsAadmin(admin.ModelAdmin):
    #把符号显示成男女

    #设置页面字段名称
    # sgender.short_description = "性别"
    list_display = ('pk','sname','sage','gender','scontend','sgrade','isDelete')
    search_fields=['sname','sgrade']
    #list_display = ['pk','sage','sgender','scontend','sgrade','isDelete']
    
    #list_per_page =10 
admin.site.register(Students,StudentsAadmin)