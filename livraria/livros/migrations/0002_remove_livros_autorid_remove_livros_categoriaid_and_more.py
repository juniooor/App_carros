# Generated by Django 4.2.2 on 2023-06-08 00:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('categorias', '0001_initial'),
        ('autores', '0001_initial'),
        ('livros', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='livros',
            name='autorid',
        ),
        migrations.RemoveField(
            model_name='livros',
            name='categoriaid',
        ),
        migrations.AddField(
            model_name='livros',
            name='categorias',
            field=models.ManyToManyField(to='categorias.categoria'),
        ),
        migrations.AddField(
            model_name='livros',
            name='cutores',
            field=models.ManyToManyField(to='autores.autor'),
        ),
    ]
