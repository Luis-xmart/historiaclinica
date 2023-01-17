from django.db import models

# Create your models here.
class Departamento(models.Model):
    nombre = models.CharField(max_length=50)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.nombre

class Municipio(models.Model):
    nombre = models.CharField(max_length=50)
    departamento = models.ForeignKey(Departamento, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.nombre

class Tipo_documento (models.Model):
    nombre = models.CharField(max_length=100, verbose_name='Nombre')
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.nombre

class Genero (models.Model):
    nombre = models.CharField(max_length=100, verbose_name='Nombre')
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.nombre

class Estado_civil (models.Model):
    nombre = models.CharField(max_length=100, verbose_name='Nombre')
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.nombre

class Paciente(models.Model):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    tipo_documento = models.ForeignKey(Tipo_documento, null=True, blank=True, on_delete=models.CASCADE, verbose_name='Tipo')
    cedula = models.CharField(max_length=50)
    fecha_nacimiento = models.DateField()
    eps = models.CharField(max_length=100)
    genero = models.ForeignKey(Genero, null=True, blank=True, on_delete=models.CASCADE, verbose_name='Genero')
    direccion = models.TextField()
    departamento = models.ForeignKey(Departamento, on_delete=models.CASCADE, related_name='departamento', null=True)
    municipio = models.ForeignKey(Municipio, on_delete=models.CASCADE, related_name='municipio', null=True)
    celular = models.CharField(max_length=50)
    correo = models.EmailField(max_length=254)
    estudios = models.CharField(max_length=200)
    origen = models.CharField(max_length=100)
    ocupacion = models.CharField(max_length=80)
    estado_civil = models.ForeignKey(Estado_civil, null=True, blank=True, on_delete=models.CASCADE, verbose_name='Estado')
    religion = models.CharField(max_length=80)
    datos_prog = models.CharField(max_length=200)
    antecedentes = models.CharField(max_length=200)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.nombre

class Historia(models.Model):
    id_paciente = models.ForeignKey(Paciente, null=True, blank=True, on_delete=models.CASCADE, verbose_name='Paciente')
    motivo = models.CharField(max_length=250, null = True)
    antecedentes_paciente = models.CharField(max_length=250, null = True)
    perfil = models.CharField(max_length=250, null = True)
    personalidad = models.CharField(max_length=250, null = True)
    historia_familiar = models.CharField(max_length=250, null = True)
    examen_mental = models.CharField(max_length=250, null = True)
    estado_conciencia = models.CharField(max_length=250, null = True)
    estado_animo = models.CharField(max_length=250, null = True)
    actividad_motora = models.CharField(max_length=250, null = True)
    asociacion_ideas = models.CharField(max_length=250, null = True)
    contenido_ideas = models.CharField(max_length=250, null = True)
    sensibilidad = models.CharField(max_length=250, null = True)
    memoria = models.CharField(max_length=250, null = True)
    pensamiento = models.CharField(max_length=250, null = True)
    resultado_examen = models.CharField(max_length=250, null = True)
    diagnostico = models.CharField(max_length=250, null = True)
    plan_psicologia = models.CharField(max_length=250, null = True)
    