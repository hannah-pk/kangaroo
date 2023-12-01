# Generated by Django 4.2.6 on 2023-11-30 12:30

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Notification',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('task_name', models.CharField(max_length=50)),
            ],
        ),
        migrations.RemoveField(
            model_name='task',
            name='id',
        ),
        migrations.AddField(
            model_name='team',
            name='team_creator',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='created_teams', to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='invite',
            name='invite_message',
            field=models.TextField(blank=True, validators=[django.core.validators.MaxLengthValidator(100)]),
        ),
        migrations.RemoveField(
            model_name='invite',
            name='inviting_team',
        ),
        migrations.AlterField(
            model_name='task',
            name='created_at',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='task',
            name='name',
            field=models.CharField(max_length=30, primary_key=True, serialize=False, unique=True, validators=[django.core.validators.RegexValidator('^[0-9a-zA-Z]{3,}$', 'Must have 3 alphanumeric characters!')]),
        ),
        migrations.AlterField(
            model_name='team',
            name='description',
            field=models.TextField(blank=True, validators=[django.core.validators.MaxLengthValidator(200)]),
        ),
        migrations.AddField(
            model_name='invite',
            name='inviting_team',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='tasks.team'),
        ),
    ]