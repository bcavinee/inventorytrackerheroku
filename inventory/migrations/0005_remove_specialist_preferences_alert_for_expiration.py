# Generated by Django 3.2.6 on 2022-04-22 10:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0004_alter_specialist_preferences_alert_for_expiration'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='specialist_preferences',
            name='alert_for_expiration',
        ),
    ]
