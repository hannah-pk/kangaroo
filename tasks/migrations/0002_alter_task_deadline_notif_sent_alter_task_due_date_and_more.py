# Generated by Django 4.2.6 on 2023-12-14 13:08

import datetime
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import django.db.models.query
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='deadline_notif_sent',
            field=models.DateField(default=datetime.date(2023, 12, 13)),
        ),
        migrations.AlterField(
            model_name='task',
            name='due_date',
            field=models.DateTimeField(default=django.utils.timezone.now, validators=[django.core.validators.MinValueValidator(limit_value=datetime.datetime(2023, 12, 14, 13, 8, 31, 411463, tzinfo=datetime.timezone.utc), message='Datetime must be in the future.')]),
        ),
        migrations.AlterField(
            model_name='task',
            name='lane',
            field=models.ForeignKey(default=django.db.models.query.QuerySet.first, on_delete=django.db.models.deletion.CASCADE, to='tasks.lane'),
        ),
    ]
