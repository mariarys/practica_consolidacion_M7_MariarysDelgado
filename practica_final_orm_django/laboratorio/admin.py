from django.contrib import admin
from .models import Laboratorio,DirectorGeneral, Producto

 
class LaboratorioAdmin(admin.ModelAdmin):
    list_display = ('id','nombre')
    search_fields = ('nombre',) 
    ordering = ('nombre',)

class DirectorGeneralAdmin(admin.ModelAdmin):
    list_display = ('id', 'nombre', 'laboratorio')
    list_filter = ('nombre','laboratorio',)
    search_fields = ('nombre', 'laboratorio')
    ordering = ('nombre',)
    
class ProductoAdmin(admin.ModelAdmin):
    list_display = ('id', 'nombre', 'laboratorio','get_year_fabricacion','p_costo','p_venta')
    list_filter = ('nombre','laboratorio',)
    search_fields = ('nombre', 'laboratorio')
    ordering = ('nombre',)

    def get_year_fabricacion(self, obj):
        return obj.f_fabricacion.year if obj.f_fabricacion else None
    get_year_fabricacion.short_description = 'Año de Fabricación'

admin.site.register(Laboratorio, LaboratorioAdmin)
admin.site.register(DirectorGeneral,DirectorGeneralAdmin)
admin.site.register(Producto, ProductoAdmin)