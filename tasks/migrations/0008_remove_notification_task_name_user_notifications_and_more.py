# Generated by Django 4.2.6 on 2023-12-07 15:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0007_task_priority'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='notification',
            name='task_name',
        ),
        migrations.AddField(
            model_name='user',
            name='notifications',
            field=models.ManyToManyField(to='tasks.notification'),
        ),
        migrations.CreateModel(
            name='TaskNotification',
            fields=[
                ('notification_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='tasks.notification')),
                ('notification_type', models.CharField(choices=[('AS', 'Assignment'), ('DL', 'Deadline')], default='AS', max_length=2)),
                ('task', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tasks.task')),
            ],
            bases=('tasks.notification',),
        ),
        migrations.CreateModel(
            name='InviteNotification',
            fields=[
                ('notification_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='tasks.notification')),
                ('invite', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tasks.invite')),
            ],
            bases=('tasks.notification',),
        ),
    ]