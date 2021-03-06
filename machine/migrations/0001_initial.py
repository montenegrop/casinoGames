# Generated by Django 4.0.4 on 2022-05-30 11:54

import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Machine',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('configuration', models.CharField(default='', max_length=10000)),
                ('reels_round', django.contrib.postgres.fields.ArrayField(base_field=models.CharField(blank=True, max_length=200), size=5)),
                ('payments', models.JSONField()),
                ('free_spins', django.contrib.postgres.fields.ArrayField(base_field=models.IntegerField(blank=True), size=5)),
            ],
        ),
    ]
