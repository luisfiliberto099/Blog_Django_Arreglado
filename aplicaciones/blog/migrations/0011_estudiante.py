# Generated by Django 3.2.16 on 2022-11-07 23:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0010_alter_profesor_options'),
    ]

    operations = [
        migrations.CreateModel(
            name='Estudiante',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=255, verbose_name='Nombre del profesor')),
                ('apellidos', models.CharField(max_length=255, verbose_name='Apellidos del profesor')),
                ('fecha_creacion', models.DateField(auto_now_add=True, verbose_name='Fecha de creación del registro')),
                ('fecha_nacimineto', models.DateField(verbose_name='Fecha de nacimiento')),
                ('su_pre', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blog.pre_universitario')),
                ('su_profesor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blog.profesor')),
            ],
            options={
                'verbose_name': 'Estudiante',
                'verbose_name_plural': 'Estudiantes',
            },
        ),
    ]
