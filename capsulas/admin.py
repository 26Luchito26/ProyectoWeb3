from django.contrib import admin
from .models import Capsula

class CapsulaAdmin(admin.ModelAdmin):
    list_display = ('id_capsula', 'nombre_capsula', 'descripcion_capsula')
    search_fields = ('nombre_capsula', 'descripcion_capsula')
    actions = ['delete_selected']

admin.site.register(Capsula, CapsulaAdmin)