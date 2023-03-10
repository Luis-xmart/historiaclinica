# Generated by Django 4.0.2 on 2022-11-14 21:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Departamento',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Estado_civil',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100, verbose_name='Nombre')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Genero',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100, verbose_name='Nombre')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Municipio',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('departamento', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Registro.departamento')),
            ],
        ),
        migrations.CreateModel(
            name='Tipo_documento',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100, verbose_name='Nombre')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Paciente',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
                ('apellido', models.CharField(max_length=50)),
                ('cedula', models.CharField(max_length=50)),
                ('fecha_nacimiento', models.DateField()),
                ('eps', models.CharField(max_length=100)),
                ('direccion', models.TextField()),
                ('celular', models.CharField(max_length=50)),
                ('correo', models.EmailField(max_length=254)),
                ('estudios', models.CharField(max_length=200)),
                ('origen', models.CharField(max_length=100)),
                ('ocupacion', models.CharField(max_length=80)),
                ('religion', models.CharField(max_length=80)),
                ('datos_prog', models.CharField(max_length=200)),
                ('antecedentes', models.CharField(max_length=200)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('departamento', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='departamento', to='Registro.departamento')),
                ('estado_civil', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Registro.estado_civil', verbose_name='Estado')),
                ('genero', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Registro.genero', verbose_name='Genero')),
                ('municipio', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='municipio', to='Registro.municipio')),
                ('tipo_documento', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Registro.tipo_documento', verbose_name='Tipo')),
            ],
        ),
        migrations.CreateModel(
            name='Historia',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('motivo', models.CharField(max_length=250, null=True)),
                ('antecedentes_paciente', models.CharField(max_length=250, null=True)),
                ('perfil', models.CharField(max_length=250, null=True)),
                ('personalidad', models.CharField(max_length=250, null=True)),
                ('historia_familiar', models.CharField(max_length=250, null=True)),
                ('examen_mental', models.CharField(max_length=250, null=True)),
                ('estado_conciencia', models.CharField(max_length=250, null=True)),
                ('estado_animo', models.CharField(max_length=250, null=True)),
                ('actividad_motora', models.CharField(max_length=250, null=True)),
                ('asociacion_ideas', models.CharField(max_length=250, null=True)),
                ('contenido_ideas', models.CharField(max_length=250, null=True)),
                ('sensibilidad', models.CharField(max_length=250, null=True)),
                ('memoria', models.CharField(max_length=250, null=True)),
                ('pensamiento', models.CharField(max_length=250, null=True)),
                ('resultado_examen', models.CharField(max_length=250, null=True)),
                ('diagnostico', models.CharField(max_length=250, null=True)),
                ('plan_psicologia', models.CharField(max_length=250, null=True)),
                ('id_paciente', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Registro.paciente', verbose_name='Paciente')),
            ],
        ),
    ]
