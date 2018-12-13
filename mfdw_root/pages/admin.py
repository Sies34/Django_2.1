from django.contrib import admin
from .models import Page

class PageAdmin(admin.ModelAdmin):
    list_display = ('tittle', 'update_date')
    ordering = ('tittle',)
    search_fields = ('tittle',)

admin.site.register(Page, PageAdmin)
