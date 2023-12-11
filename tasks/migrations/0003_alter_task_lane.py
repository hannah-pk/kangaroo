# Generated by Django 4.2.6 on 2023-12-11 14:21

from django.db import migrations, models
import django.db.models.deletion
import django.db.models.query


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0002_task_dependencies_alter_task_lane'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='lane',
            field=models.ForeignKey(default=django.db.models.query.QuerySet.first, on_delete=django.db.models.deletion.CASCADE, to='tasks.lane'),
        ),
    ]
