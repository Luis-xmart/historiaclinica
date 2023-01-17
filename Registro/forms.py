from django import forms
from .models import Paciente, Historia
from Registro.models import Departamento, Estado_civil, Municipio, Tipo_documento, Genero

class DatePickerInput(forms.DateInput):
        input_type = 'date'

class FormularioPaciente(forms.Form):
    nombre = forms.CharField(label='Nombre', max_length=100, required=True, widget=forms.TextInput(attrs={'class': 'form-control'}))
    apellido = forms.CharField(label='Apellido', max_length=100, required=True, widget=forms.TextInput(attrs={'class': 'form-control'}))
    tipo_documento = forms.ModelChoiceField(widget=forms.Select(attrs={'class': 'form-control'}),queryset=Tipo_documento.objects.all(), label = 'Tipo de Identificación')
    cedula = forms.CharField(label='Cedula',  max_length=100, required=True, widget=forms.TextInput(attrs={'class': 'form-control', 'id':'cedula'}))
    fecha_nacimiento = forms.DateField(widget=DatePickerInput(attrs={'class': 'form-control'}))
    eps = forms.CharField(label='EPS', max_length=100, required=True, widget=forms.TextInput(attrs={'class': 'form-control'}))
    genero = forms.ModelChoiceField(queryset=Genero.objects.all(), required=False, label = 'Genero',widget=forms.Select(attrs={'class': 'form-control'}))
    direccion = forms.CharField(label='Dirección', max_length=100, required=True, widget=forms.TextInput(attrs={'class': 'form-control'}))
    # departamento = forms.ModelChoiceField(queryset=Departamento.objects.all(),widget=ModelSelect2Widget(search_fields=['name_category__icontains'],attrs={'style': 'width:350px;', },))
    departamento = forms.ModelChoiceField(queryset=Departamento.objects.all(), label = 'Departamento',widget=forms.Select(attrs={'class': 'form-control'}))
    #departamentos = forms.ModelChoiceField(queryset=Departamento.objects.all(), empty_label='Seleccione un departamento', widget=forms.Select(attrs={'class': 'form-control'}))
    municipio = forms.ModelChoiceField(queryset=Municipio.objects.all(), label = 'Municipio',widget=forms.Select(attrs={'class': 'form-control'}))
    #municipios = forms.ModelChoiceField(queryset=Municipio.objects.none(), empty_label='Seleccione un municipio', widget=forms.Select(attrs={'class': 'form-control'}))
    celular = forms.CharField(label='Celular', max_length=100, required=True, widget=forms.TextInput(attrs={'class': 'form-control'}))
    correo = forms.CharField(label='Correo', max_length=100, required=True, widget=forms.TextInput(attrs={'class': 'form-control'}))
    estudios = forms.CharField(label='Estudios', max_length=100, required=False, widget=forms.TextInput(attrs={'class': 'form-control'}))
    origen = forms.CharField(label='Origen', max_length=100, required=False, widget=forms.TextInput(attrs={'class': 'form-control'}))
    ocupacion = forms.CharField(label='Ocupacion', max_length=100, required=False, widget=forms.TextInput(attrs={'class': 'form-control'}))
    estado_civil = forms.ModelChoiceField(widget=forms.Select(attrs={'class': 'form-control'}),queryset=Estado_civil.objects.all(), label = 'Estado Civil')
    religion = forms.CharField(label='Religión', max_length=100, required=False, widget=forms.TextInput(attrs={'class': 'form-control'}))
    datos_prog = forms.CharField(label='Datos de los Progenitores', max_length=100, required=False, widget=forms.TextInput(attrs={'class': 'form-control'}))
    antecedentes = forms.CharField(label='Antecedentes', max_length=100, required=False, widget=forms.TextInput(attrs={'class': 'form-control'}))
    # def __init__(self, *args, **kwargs):
    #     super().__init__(*args, **kwargs)
    #     self.fields['municipios'].queryset = Municipio.objects.none()
    # def clean_departamentos(self):
    #     departamento = self.cleaned_data.get("departamentos")
    #     if departamento and not Departamento.objects.filter(pk=departamento.pk).exists():
    #         raise forms.ValidationError("Escoja una opción válida. Esa opción no está entre las disponibles.")
    #     return departamento
    # def clean(self):
    #     cleaned_data = super().clean()
    #     departamento = cleaned_data.get("departamentos")
    #     municipio = cleaned_data.get("municipios")
    #     if municipio and municipio.departamento != departamento:
    #         raise forms.ValidationError("El municipio seleccionado no corresponde al departamento seleccionado")
class FormularioHistoria(forms.Form):
    motivo = forms.CharField(label='Motivo de la consulta:',  widget=forms.Textarea(attrs={'class': 'form-control'}), required=False)
    antecedentes_paciente = forms.CharField(label='Antecedentes del paciente:',  widget=forms.Textarea(attrs={'class': 'form-control'}), required=False)
    perfil = forms.CharField(label='Perfil social:',  widget=forms.Textarea(attrs={'class': 'form-control'}), required=False)
    personalidad = forms.CharField(label='Personalidad:',  widget=forms.Textarea(attrs={'class': 'form-control'}), required=False)
    historia_familiar = forms.CharField(label='Historia familiar:',  widget=forms.Textarea(attrs={'class': 'form-control'}), required=False)
    examen_mental = forms.CharField(label='Examen mental:',  widget=forms.Textarea(attrs={'class': 'form-control'}), required=False)
    estado_conciencia = forms.CharField(label='Estado de conciencia:',  widget=forms.Textarea(attrs={'class': 'form-control'}), required=False)
    estado_animo = forms.CharField(label='Estado de ánimo:',  widget=forms.Textarea(attrs={'class': 'form-control'}), required=False)
    actividad_motora = forms.CharField(label='Actividad motora:',  widget=forms.Textarea(attrs={'class': 'form-control'}), required=False)
    asociacion_ideas = forms.CharField(label='Asociación y flujo de ideas y características del lenguaje:',  widget=forms.Textarea(attrs={'class': 'form-control'}), required=False)
    contenido_ideas = forms.CharField(label='Contenido de ideas:',  widget=forms.Textarea(attrs={'class': 'form-control'}), required=False)
    sensibilidad = forms.CharField(label='Sensibilidad:',  widget=forms.Textarea(attrs={'class': 'form-control'}), required=False)
    memoria = forms.CharField(label='Memoria:',  widget=forms.Textarea(attrs={'class': 'form-control'}), required=False)
    pensamiento = forms.CharField(label='Pensamiento:',  widget=forms.Textarea(attrs={'class': 'form-control'}), required=False)
    resultado_examen = forms.CharField(label='Resultado del examen:',  widget=forms.Textarea(attrs={'class': 'form-control'}), required=False)
    diagnostico = forms.CharField(label='Diagnóstico:',  widget=forms.Textarea(attrs={'class': 'form-control'}), required=False)
    plan_psicologia = forms.CharField(label='Plan de orientación psicológica:',  widget=forms.Textarea(attrs={'class': 'form-control'}), required=False)

class FormularioPaciente2(forms.ModelForm):
    class Meta:
        model = Paciente
        fields = ('nombre', 'apellido', 'tipo_documento', 'cedula', 'fecha_nacimiento', 'eps', 'genero', 'direccion', 'departamento', 'municipio', 'celular', 'correo', 'estudios','origen', 'ocupacion', 'estado_civil', 'religion', 'datos_prog', 'antecedentes')
        labels = {'nombre': 'Nombre', 'apellido': 'Apellido', 'tipo_documento': 'Tipo de Documento', 'cedula': 'Cedula', 'fecha_nacimiento': 'Fecha de Nacimiento', 'eps': 'Eps', 'genero': 'Genero', 'direccion': 'Direccion', 'departamento': 'Departamento','municipio': 'Municipio', 'celular': 'Celular', 'correo': 'Correo', 'estudios': 'Estudios', 'origen': 'Origen', 'ocupacion':'Ocupación', 'estado_civil': 'Estado Civil', 'religion': 'Religión', 'datos_prog': 'Datos progenitores', 'antecedentes': 'Antecedentes'}
        widgets = {'nombre': forms.TextInput(attrs={'class': 'form-control'}),
                'apellido': forms.TextInput(attrs={'class': 'form-control'}), 
                'tipo_documento': forms.Select(attrs={'class': 'form-control'}),
                'cedula': forms.TextInput(attrs={'class': 'form-control'}),
                'fecha_nacimiento': forms.DateInput(attrs={'class': 'form-control'}),
                'eps': forms.TextInput(attrs={'class': 'form-control'}),
                'genero': forms.Select(attrs={'class': 'form-control'}),
                'direccion': forms.TextInput(attrs={'class': 'form-control'}),
                'departamento': forms.Select(attrs={'class': 'form-control'}),
                'municipio': forms.Select(attrs={'class': 'form-control'}),
                'celular': forms.TextInput(attrs={'class': 'form-control'}),
                'correo': forms.TextInput(attrs={'class': 'form-control'}),
                'estudios': forms.TextInput(attrs={'class': 'form-control'}),
                'origen': forms.TextInput(attrs={'class': 'form-control'}),
                'ocupacion': forms.TextInput(attrs={'class': 'form-control'}),
                'estado_civil': forms.Select(attrs={'class': 'form-control'}),
                'religion': forms.TextInput(attrs={'class': 'form-control'}),
                'datos_prog': forms.TextInput(attrs={'class': 'form-control'}),
                'antecedentes': forms.TextInput(attrs={'class': 'form-control'})  
                  
        }
class FormularioHistoria2(forms.ModelForm):
    class Meta:
        model = Historia
        fields = ('motivo', 'antecedentes_paciente', 'perfil', 'personalidad', 'historia_familiar', 'examen_mental', 'estado_conciencia', 'estado_animo', 'actividad_motora', 'asociacion_ideas', 'contenido_ideas', 'sensibilidad', 'memoria', 'pensamiento', 'resultado_examen', 'diagnostico', 'plan_psicologia')
        labels = {'motivo': 'Motivo', 'antecedentes_paciente': 'Antecedentes Paciente', 'perfil':'Perfil', 'personalidad':'Personalidad', 'historia_familiar':'Historia Familiar', 'examen_mental': 'Examen Mental', 'estado_conciencia': 'Estado Conciencia', 'estado_animo':'Estado Animo', 'actividad_motora': 'Actividad Motora', 'asociacion_ideas':'Asociacion Ideas', 'contenido_ideas':'Contenido Ideas', 'sensibilidad':'Sensibilidad', 'memoria':'Memoria', 'pensamiento':'Pensamiento', 'resultado_examen':'Resultado Examen', 'diagnostico':'Diagnostico', 'plan_psicologia':'Plan Psicologia'}
        widgets = {
                'motivo': forms.TextInput(attrs={'class': 'form-control'}), 
                'antecedentes_paciente': forms.TextInput(attrs={'class': 'form-control'}), 
                'perfil': forms.TextInput(attrs={'class': 'form-control'}), 
                'personalidad': forms.TextInput(attrs={'class': 'form-control'}), 
                'historia_familiar': forms.TextInput(attrs={'class': 'form-control'}), 
                'examen_mental': forms.TextInput(attrs={'class': 'form-control'}), 
                'estado_conciencia': forms.TextInput(attrs={'class': 'form-control'}), 
                'estado_animo': forms.TextInput(attrs={'class': 'form-control'}), 
                'actividad_motora': forms.TextInput(attrs={'class': 'form-control'}), 
                'asociacion_ideas': forms.TextInput(attrs={'class': 'form-control'}), 
                'contenido_ideas': forms.TextInput(attrs={'class': 'form-control'}), 
                'sensibilidad': forms.TextInput(attrs={'class': 'form-control'}), 
                'memoria': forms.TextInput(attrs={'class': 'form-control'}), 
                'pensamiento': forms.TextInput(attrs={'class': 'form-control'}), 
                'resultado_examen': forms.TextInput(attrs={'class': 'form-control'}), 
                'diagnostico': forms.TextInput(attrs={'class': 'form-control'}), 
                'plan_psicologia': forms.TextInput(attrs={'class': 'form-control'}), 
        } 
        
class RangoFechasReporte(forms.Form):
    start_date = forms.DateField(label='Fecha Inicial', required=True,widget=DatePickerInput(attrs={'class': 'form-control'}))
    end_date = forms.DateField(label='Fecha Final', required=True,widget=DatePickerInput(attrs={'class': 'form-control'}))