from django.contrib import admin
from contact.models import contact
# Register your models here.
@admin.register(contact)
class contactAdmin(admin.ModelAdmin):
    list_display = ('name','created_at')
    search_fields = ('name',)
    ordering = ('name',)