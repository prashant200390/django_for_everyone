from django.contrib import admin
from .models import student
# Register your models here.
@admin.register(student)
class studentadmin(admin.ModelAdmin):
    list_display = ('name','age','city')
    search_fields = ('name','city')
    list_filter = ('name','city')
    ordering = ('name',)