# Generated by Django 3.2.5 on 2021-07-21 16:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pedidos', '0002_alter_docente_nombres'),
    ]

    operations = [
        migrations.RenameField(
            model_name='curso',
            old_name='cocente',
            new_name='docente',
        ),
    ]