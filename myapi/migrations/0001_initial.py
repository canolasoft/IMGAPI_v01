# Generated by Django 3.1.7 on 2021-04-29 23:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Artista',
            fields=[
                ('id_a', models.BigAutoField(primary_key=True, serialize=False)),
                ('nombre_a', models.CharField(max_length=60)),
                ('imagen_a', models.ImageField(blank=True, null=True, upload_to='')),
                ('descripcion_a', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Datapp',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombreapp', models.CharField(max_length=20)),
                ('linkapp', models.CharField(max_length=150)),
                ('keyapp', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Redsocial',
            fields=[
                ('id_rs', models.BigAutoField(primary_key=True, serialize=False)),
                ('nombre_rs', models.CharField(max_length=30)),
                ('imagen_rs', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Wallpaper',
            fields=[
                ('id_w', models.BigAutoField(primary_key=True, serialize=False)),
                ('nombre_w', models.CharField(max_length=100)),
                ('imagen_w', models.ImageField(blank=True, null=True, upload_to='')),
                ('id_a', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='myapi.artista')),
            ],
        ),
        migrations.CreateModel(
            name='RedsocialArtista',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('url_rsa', models.CharField(max_length=150)),
                ('id_a', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='myapi.artista')),
                ('id_rs', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='myapi.redsocial')),
            ],
        ),
    ]
