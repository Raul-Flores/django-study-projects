# Generated by Django 3.2.4 on 2021-06-29 22:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('napalmweb', '0003_alter_netdevice_password'),
    ]

    operations = [
        migrations.AlterField(
            model_name='netdevice',
            name='direccionip',
            field=models.CharField(max_length=40),
        ),
        migrations.AlterField(
            model_name='netdevice',
            name='password',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='netdevice',
            name='protocolo',
            field=models.CharField(max_length=15),
        ),
        migrations.AlterField(
            model_name='netdevice',
            name='puerto',
            field=models.EmailField(max_length=200),
        ),
    ]