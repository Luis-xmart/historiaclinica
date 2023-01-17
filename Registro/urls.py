from django.urls import path, re_path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('Registro/', views.registro, name='Registro'),
    path('Reportes/', views.reportes, name='Reportes'),
    path('Reportesdiag/', views.reportesdiag, name='Reportesdiag'),
    path('municipios/<int:id_departamento>/', views.obtener_municipios, name='obtener_municipios'),
    re_path(r'^paciente/(?P<id>\d+)$', views.detallepaciente, name='detallepaciente'),
    re_path(r'^editar/(?P<id>\d+)$', views.editar, name='editar'),
    re_path(r'^editarhistoria/(?P<id>\d+)$', views.editarhistoria, name='editarhistoria'),
    re_path(r'^eliminar/(?P<id>\d+)$', views.eliminar, name='eliminar'),
    

    # re_path(r'^empresa/editar/(?P<id>\d+)$', views.editarempresa, name='editarEmpresa'),
    # # path('empresa/', views.empresa, name='empresa'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)