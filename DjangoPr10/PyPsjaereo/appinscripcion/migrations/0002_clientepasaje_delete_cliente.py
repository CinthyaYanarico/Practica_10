# Generated by Django 4.1.2 on 2022-11-01 04:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appinscripcion', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ClientePasaje',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Nombre', models.CharField(max_length=50)),
                ('Correo_Electronico', models.CharField(max_length=50)),
                ('Contraseña', models.CharField(max_length=50)),
                ('FechaNac', models.CharField(max_length=50)),
                ('Dirección', models.CharField(max_length=50)),
                ('Sexo', models.CharField(max_length=50)),
                ('Intereces', models.CharField(max_length=50)),
                ('Aficiones', models.CharField(max_length=50)),
                ('Precio', models.IntegerField()),
            ],
        ),
        migrations.DeleteModel(
            name='Cliente',
        ),
    ]
