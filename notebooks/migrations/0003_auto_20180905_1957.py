# Generated by Django 2.1.1 on 2018-09-05 19:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('notebooks', '0002_auto_20180905_0000'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='cpu',
            options={'ordering': ('core',)},
        ),
        migrations.AlterModelOptions(
            name='ram',
            options={'ordering': ('capacity',)},
        ),
    ]