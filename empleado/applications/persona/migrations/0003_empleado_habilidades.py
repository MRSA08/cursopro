# Generated by Django 3.2.5 on 2021-08-20 16:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('persona', '0002_auto_20210820_1118'),
    ]

    operations = [
        migrations.AddField(
            model_name='empleado',
            name='Habilidades',
            field=models.ManyToManyField(to='persona.Habilidades'),
        ),
    ]