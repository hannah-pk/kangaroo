# Generated by Django 4.2.6 on 2023-12-01 13:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0006_tasknotification_notification_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tasknotification',
            name='task',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tasks.task'),
        ),
    ]
