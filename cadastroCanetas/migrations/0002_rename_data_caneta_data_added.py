# Generated by Django 5.2.1 on 2025-05-19 18:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cadastroCanetas', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='caneta',
            old_name='data',
            new_name='data_added',
        ),
    ]
