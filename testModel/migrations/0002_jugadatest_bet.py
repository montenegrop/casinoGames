# Generated by Django 4.0.4 on 2022-05-20 05:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('testModel', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='jugadatest',
            name='bet',
            field=models.FloatField(default=0, verbose_name='bet'),
        ),
    ]
