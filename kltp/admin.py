from django.contrib import admin
from .models import Chitiet,Nganhnghe

# Register your models here.
class NganhngheAdmin(admin.ModelAdmin):
    list_display= ['mangkinhdoanh', 'ngaytao', 'active']
    list_filter=['mangkinhdoanh','ngaytao']
    search_fields = ['mangkinhdoanh']

class ChitietAdmin(admin.ModelAdmin):
    list_display= ['mangkinhdoanh', 'nganhnghe','ngaytao']
    list_filter=['mangkinhdoanh','ngaytao']
    search_fields = ['mangkinhdoanh']
    prepopulated_fields= {'slug':('mangkinhdoanh',)}
admin.site.register(Nganhnghe,NganhngheAdmin)
admin.site.register(Chitiet,ChitietAdmin)