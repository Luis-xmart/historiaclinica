from django.shortcuts import render, redirect

from Registro.models import Paciente, Historia, Municipio

from .forms import FormularioPaciente, FormularioHistoria, FormularioPaciente2, FormularioHistoria2, RangoFechasReporte

from django.http import JsonResponse
from django.db.models import Q
# Create your views here.

def obtener_municipios(request, id_departamento):
    municipios = Municipio.objects.filter(departamento_id=id_departamento)
    municipios_data = [{'id': m.id, 'nombre': m.nombre} for m in municipios]
    return JsonResponse(municipios_data, safe=False)
def registro(request):
    # current_user = request.user
    paciente = Paciente.objects.all()
    formularioPaciente = FormularioPaciente()
    if request.method == 'POST':
        formularioPaciente = FormularioPaciente(request.POST)
        if formularioPaciente.is_valid():
            form_data = formularioPaciente.cleaned_data
            print('REQUEST', form_data)
            
            nombre = form_data.get('nombre')
            print(nombre)
            apellido = form_data.get('apellido')
            print(apellido)
            tipo_documento = form_data.get('tipo_documento')
            print(tipo_documento)
            cedula = form_data.get('cedula')
            print(cedula)
            fecha_nacimiento = form_data.get('fecha_nacimiento')
            print(fecha_nacimiento)
            eps = form_data.get('eps')
            print(eps)
            genero = form_data.get('genero')
            print(genero)
            direccion = form_data.get('direccion')
            print(direccion)
            # departamentos = formularioPaciente.cleaned_data['departamentos']
            departamento = form_data.get('departamento')
            # print(departamentos)
            municipio = form_data.get('municipio')
            print(municipio)
            celular = form_data.get('celular')
            correo = form_data.get('correo')
            estudios = form_data.get('estudios')
            origen = form_data.get('origen')
            ocupacion = form_data.get('ocupacion')
            estado_civil = form_data.get('estado_civil')
            religion = form_data.get('religion')
            datos_prog = form_data.get('datos_prog')
            antecedentes = form_data.get('antecedentes')
            # messages.success(request,"La Empresa se creo correctamente")
            Paciente.objects.create(nombre=nombre, apellido=apellido,
            tipo_documento=tipo_documento, cedula = cedula, fecha_nacimiento=fecha_nacimiento,
            eps = eps, genero = genero, direccion = direccion, departamento = departamento, municipio = municipio,
            celular = celular, correo = correo, estudios = estudios, origen = origen, ocupacion = ocupacion,
            estado_civil = estado_civil, religion = religion, datos_prog = datos_prog, antecedentes = antecedentes)
    #         formularioEmpresa = FormularioEmpresa()

    return render(request, 'Registro/registro.html', {'formulario': formularioPaciente, 'paciente': paciente})

def detallepaciente(request, id):
    formularioHistoria = FormularioHistoria()
    paciente = Paciente.objects.get(id=id)
    historia = Historia.objects.filter(id_paciente=id)
    print('HISTORIA', historia)
    # prod = Productos.objects.all()
    if request.method == 'POST':
        formularioHistoria = FormularioHistoria(request.POST)
        if formularioHistoria.is_valid():
            form_data = formularioHistoria.cleaned_data
            id_paciente = paciente.id
            motivo = form_data.get('motivo')
            antecedentes_paciente = form_data.get('antecedentes_paciente')
            perfil = form_data.get('perfil')
            personalidad = form_data.get('personalidad')
            historia_familiar = form_data.get('historia_familiar')
            examen_mental = form_data.get('examen_mental')
            estado_conciencia = form_data.get('estado_conciencia')
            estado_animo = form_data.get('estado_animo')
            actividad_motora = form_data.get('actividad_motora')
            asociacion_ideas = form_data.get('asociacion_ideas')
            contenido_ideas = form_data.get('contenido_ideas')
            sensibilidad = form_data.get('sensibilidad')
            memoria = form_data.get('memoria')
            pensamiento = form_data.get('pensamiento')
            resultado_examen = form_data.get('resultado_examen')
            diagnostico = form_data.get('diagnostico')
            plan_psicologia = form_data.get('plan_psicologia')
            Historia.objects.create(id_paciente_id=id_paciente, motivo=motivo, antecedentes_paciente=antecedentes_paciente, perfil=perfil, personalidad=personalidad,
            historia_familiar = historia_familiar, examen_mental = examen_mental, estado_conciencia = estado_conciencia,  estado_animo=estado_animo,
            actividad_motora = actividad_motora, asociacion_ideas = asociacion_ideas, contenido_ideas = contenido_ideas, sensibilidad = sensibilidad,
            memoria = memoria, pensamiento = pensamiento, resultado_examen = resultado_examen, diagnostico = diagnostico, plan_psicologia = plan_psicologia)
        # print('REQUEST', request.POST)
        # form = FormularioTareas(request.POST)
    return render(request, 'Registro/detallepaciente.html', {'formularioHC': formularioHistoria, 'paciente': paciente, 'historia': historia})

def editar(request, id):
    pac = Paciente.objects.filter(id=id).first()
    if request.method == 'GET':
        editarpac = FormularioPaciente2(instance=pac)
    else:
        editarpac = FormularioPaciente2(request.POST, instance=pac)
        if editarpac.is_valid():
            form_data = editarpac.cleaned_data
            nombre = form_data.get('nombre')
            apellido = form_data.get('apellido')
            tipo_documento = form_data.get('tipo_documento')
            cedula = form_data.get('cedula')
            fecha_nacimiento = form_data.get('fecha_nacimiento')
            eps = form_data.get('eps')
            genero = form_data.get('genero')
            direccion = form_data.get('direccion')
            departamento = form_data.get('departamento')
            municipio = form_data.get('municipio')
            celular = form_data.get('celular')
            correo = form_data.get('correo')
            estudios = form_data.get('estudios')
            origen = form_data.get('origen')
            ocupacion = form_data.get('ocupacion')
            estado_civil = form_data.get('estado_civil')
            religion = form_data.get('religion')
            datos_prog = form_data.get('datos_prog')
            antecedentes = form_data.get('antecedentes')
            pac = Paciente.objects.filter(id=id).update(nombre = nombre, apellido = apellido, tipo_documento = tipo_documento, cedula = cedula, fecha_nacimiento = fecha_nacimiento, eps = eps, genero = genero, direccion = direccion, departamento = departamento, municipio = municipio, celular = celular, correo = correo, estudios = estudios, origen = origen, ocupacion = ocupacion, estado_civil = estado_civil, religion = religion, datos_prog = datos_prog, antecedentes = antecedentes)
            return redirect('Registro')
    return render(request, 'Registro/editar.html', context={'paciente': editarpac})

def editarhistoria(request, id):
    his = Historia.objects.filter(id=id).first()
    if request.method == 'GET':
        editarhis = FormularioHistoria2(instance=his)
    else:
        editarhis = FormularioHistoria2(request.POST, instance=his)
        if editarhis.is_valid():
            form_data = editarhis.cleaned_data
            motivo = form_data.get('motivo')
            antecedentes_paciente = form_data.get('antecedentes_paciente')
            perfil = form_data.get('perfil')
            personalidad = form_data.get('personalidad')
            historia_familiar = form_data.get('historia_familiar')
            examen_mental = form_data.get('examen_mental')
            estado_conciencia = form_data.get('estado_conciencia')
            estado_animo = form_data.get('estado_animo')
            actividad_motora = form_data.get('actividad_motora')
            asociacion_ideas = form_data.get('asociacion_ideas')
            contenido_ideas = form_data.get('contenido_ideas')
            sensibilidad = form_data.get('sensibilidad')
            memoria = form_data.get('memoria')
            pensamiento = form_data.get('pensamiento')
            resultado_examen = form_data.get('resultado_examen')
            diagnostico = form_data.get('diagnostico')
            plan_psicologia = form_data.get('plan_psicologia')
            pac = Historia.objects.filter(id=id).update(motivo=motivo, antecedentes_paciente = antecedentes_paciente, perfil = perfil, personalidad = personalidad, historia_familiar = historia_familiar, examen_mental = examen_mental, estado_conciencia =estado_conciencia, estado_animo = estado_animo, actividad_motora = actividad_motora, asociacion_ideas = asociacion_ideas, contenido_ideas = contenido_ideas, sensibilidad = sensibilidad, memoria = memoria, pensamiento = pensamiento, resultado_examen = resultado_examen, diagnostico = diagnostico, plan_psicologia = plan_psicologia )
            return redirect('Registro')
    return render(request, 'Registro/editarhistoria.html', context={'historia': editarhis})

def eliminar(request, id):
    paciente = Paciente.objects.get(id=id)
    paciente.delete()
    return redirect('Registro')

def reportes(request):
    form = RangoFechasReporte()
    if request.method == 'POST':
        form = RangoFechasReporte(request.POST)
        # mod3 = Paciente.objects.filter(turnoAsig__conductor = request.user.id) and Guia.objects.filter(asignado=True)
        if form.is_valid():
            qs = Paciente.objects.filter(fecha_nacimiento__range=(
                form.cleaned_data['start_date'],
                form.cleaned_data['end_date']
            ))
            print('PRUEBA', qs)
        return render(request, 'Registro/reportes.html', {'form':form, 'env': qs})
    return render(request, 'Registro/reportes.html', {'form':form})

# def reportesdiag(request):
#     search_paciente = request.GET.get('search')
#     if search_paciente != None:
#         paciente = Paciente.objects.filter(cedula = search_paciente)
#         historia = Historia.objects.filter(id_paciente__cedula = search_paciente)
#         print('HISTORIA', historia.model)
#         return render(request, 'Registro/reportediag.html', {'hist':paciente})
        
#     else:
#         # If not searched, return default posts
#         return render(request, 'Registro/reportediag.html', )

def reportesdiag(request):
    search_paciente = request.GET.get('search')
    
    if search_paciente != None:
        paciente = Paciente.objects.filter(cedula=search_paciente).first()
        id = paciente.id
        historia_clinica = Historia.objects.filter(id_paciente=id).first()
        if historia_clinica != None:
            diagnostico = historia_clinica.diagnostico
            context = {'paciente': paciente, 'diagnostico': diagnostico}
            return render(request, 'Registro/reportediag.html', context)
        else:
            return render(request, 'Registro/reportediag.html')
            
    else:
        return render(request, 'Registro/reportediag.html')