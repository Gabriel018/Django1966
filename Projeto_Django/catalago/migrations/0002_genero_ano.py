# Generated by Django 3.2.6 on 2021-11-20 12:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalago', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='genero',
            name='ano',
            field=models.DateField(blank=True, null=True),
        ),
    ]
