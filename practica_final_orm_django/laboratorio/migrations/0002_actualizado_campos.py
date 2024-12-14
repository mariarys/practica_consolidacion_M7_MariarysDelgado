# Generated by Django 4.1.1 on 2024-12-14 14:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('laboratorio', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='directorgeneral',
            name='especialidad',
            field=models.CharField(default='', max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='laboratorio',
            name='ciudad',
            field=models.CharField(default='', max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='laboratorio',
            name='pais',
            field=models.CharField(default='EEUU', max_length=100),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='directorgeneral',
            name='laboratorio',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='laboratorio.laboratorio'),
        ),
        migrations.AlterField(
            model_name='laboratorio',
            name='nombre',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='producto',
            name='laboratorio',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='laboratorio.laboratorio'),
        ),
        migrations.AlterField(
            model_name='producto',
            name='nombre',
            field=models.CharField(max_length=255),
        ),
    ]
