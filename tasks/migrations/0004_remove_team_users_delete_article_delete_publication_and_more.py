# Generated by Django 4.2.6 on 2023-11-18 00:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0003_merge_0002_publication_team_article_0002_task'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='team',
            name='users',
        ),
        migrations.DeleteModel(
            name='Article',
        ),
        migrations.DeleteModel(
            name='Publication',
        ),
        migrations.DeleteModel(
            name='Team',
        ),
    ]