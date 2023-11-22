# Generated by Django 4.2.6 on 2023-11-19 23:16

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0007_rename_users_team_team_members'),
    ]

    operations = [
        migrations.AddField(
            model_name='team',
            name='team_member_names',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='team',
            name='team_members',
            field=models.ManyToManyField(blank=True, to=settings.AUTH_USER_MODEL),
        ),
    ]
