from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, HttpResponse
from django.contrib.auth.models import User  
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.views.defaults import page_not_found
from django.contrib import messages
# Create your views here.



def Paneles(request):
    return render(request, 'ProyectoWebApp/Paneles.html')

def index(request):

    return render(request, 'ProyectoWebApp/base.html')

def permisos(request):
    return render(request, 'ProyectoWebApp/sinpermiso.html')


# def nombreusuario(request):
#     usuario = User.objects.filter(id=id).first()
#     return


    
 
def mi_error_404(request):
    nombre_template = 'ProyectoWebApp/404.html'
    return render(request, template_name=nombre_template)

#class Error404view(TemplateView):
#    template_name='ProyectoWebApp/404.html'