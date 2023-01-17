from django.contrib import admin
from .models import Tipo_documento, Genero, Estado_civil, Municipio, Departamento

# Register your models here.
class Tipo_documentoAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'created', 'updated')
    list_filter = ('nombre', 'created', 'updated')
    search_fields = ('nombre', 'created', 'updated')

class DepartamentoAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'created', 'updated')
    list_filter = ('nombre', 'created', 'updated')
    search_fields = ('nombre', 'created', 'updated')

class MunicipioAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'departamento', 'created', 'updated')
    list_filter = ('nombre', 'departamento', 'created', 'updated')
    search_fields = ('nombre', 'departamento', 'created', 'updated')

class GeneroAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'created', 'updated')
    list_filter = ('nombre', 'created', 'updated')
    search_fields = ('nombre', 'created', 'updated')

class Estado_civilAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'created', 'updated')
    list_filter = ('nombre', 'created', 'updated')
    search_fields = ('nombre', 'created', 'updated')

admin.site.register(Tipo_documento, Tipo_documentoAdmin)
admin.site.register(Departamento, DepartamentoAdmin)
admin.site.register(Municipio, MunicipioAdmin)
admin.site.register(Genero, GeneroAdmin)
admin.site.register(Estado_civil, Estado_civilAdmin)


