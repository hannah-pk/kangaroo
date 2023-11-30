# Generated by Django 4.2.6 on 2023-11-28 23:01

from django.db import migrations, models


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
        migrations.AddField(
            model_name='task',
            name='lane',
            field=models.CharField(blank=True, max_length=100),
        ),
    ]
