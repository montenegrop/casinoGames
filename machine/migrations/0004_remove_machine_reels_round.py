# Generated by Django 4.0.4 on 2022-05-31 13:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('machine', '0003_remove_machine_configuration_machine_bonus_reel_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='machine',
            name='reels_round',
        ),
    ]