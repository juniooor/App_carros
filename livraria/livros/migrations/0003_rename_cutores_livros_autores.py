# Generated by Django 4.2.2 on 2023-06-08 00:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('livros', '0002_remove_livros_autorid_remove_livros_categoriaid_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='livros',
            old_name='cutores',
            new_name='autores',
        ),
    ]
