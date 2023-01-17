from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import handler404
#from ProyectoWebApp.views import Error404view
urlpatterns = [
    # path('Paneles/', views.Paneles, name='Paneles'),
    path('Base/', views.index, name='Base'),
    path('sinpermiso/', views.permisos, name='sinpermiso')
    ,path('error404/', views.mi_error_404, name='error404')
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
