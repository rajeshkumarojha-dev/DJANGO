from django.contrib import admin
from app1.models import *
# Register your models here.

@admin.register(Emp)
class EmpAdmin(admin.ModelAdmin):
    list_display=['empno','ename','job','sal']

# admin.site.register(Emp,EmpAdmin)
@admin.register(Student)
class studentAdmin(admin.ModelAdmin):
    list_display=['rollno','name']
