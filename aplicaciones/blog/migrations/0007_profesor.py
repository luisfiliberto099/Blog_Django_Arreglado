# Generated by Django 3.2.16 on 2022-11-07 23:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_auto_20221108_0000'),
    ]

    operations = [
        migrations.CreateModel(
            name='Profesor',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=255, verbose_name='Nombre del profesor')),
                ('apellidos', models.CharField(max_length=255, verbose_name='Apellidos del profesor')),
                ('fecha_creacion', models.DateField(auto_now_add=True, verbose_name='Fecha de creación del registro')),
                ('fecha_nacimineto', models.DateField(auto_now=True, verbose_name='Fecha de nacimiento')),
                ('su_pre', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blog.pre_universitario')),
            ],
        ),
    ]