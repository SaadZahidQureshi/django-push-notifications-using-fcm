# Generated by Django 5.1 on 2024-08-13 10:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('notificationsApp', '0006_notification'),
    ]

    operations = [
        migrations.AlterField(
            model_name='notification',
            name='recipient_type',
            field=models.CharField(choices=[('user', 'User'), ('admin', 'Admin')], max_length=10),
        ),
    ]
