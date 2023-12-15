# Generated by Django 4.2.6 on 2023-12-15 15:19

import datetime
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import django.db.models.query
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0003_alter_task_due_date_alter_task_lane'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='due_date',
            field=models.DateTimeField(default=django.utils.timezone.now, validators=[django.core.validators.MinValueValidator(limit_value=datetime.datetime(2023, 12, 15, 15, 19, 53, 697526, tzinfo=datetime.timezone.utc), message='Datetime must be in the future.')]),
        ),
        migrations.AlterField(
            model_name='task',
            name='lane',
            field=models.ForeignKey(default=django.db.models.query.QuerySet.first, on_delete=django.db.models.deletion.CASCADE, to='tasks.lane'),
        ),
    ]
