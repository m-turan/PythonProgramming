# Generated by Django 4.2.10 on 2024-04-29 18:48

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('baseapp', '0002_alter_folder_id'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='contentblock',
            name='folder',
        ),
        migrations.RemoveField(
            model_name='customuser',
            name='groups',
        ),
        migrations.RemoveField(
            model_name='customuser',
            name='user_permissions',
        ),
        migrations.RemoveField(
            model_name='permission',
            name='folder',
        ),
        migrations.RemoveField(
            model_name='permission',
            name='user',
        ),
        migrations.RemoveField(
            model_name='tag',
            name='folders',
        ),
        migrations.RemoveField(
            model_name='usersettings',
            name='user',
        ),
        migrations.RemoveField(
            model_name='folder',
            name='owner',
        ),
        migrations.RemoveField(
            model_name='folder',
            name='parent',
        ),
        migrations.AddField(
            model_name='folder',
            name='title',
            field=models.CharField(default=django.utils.timezone.now, max_length=200),
            preserve_default=False,
        ),
        migrations.DeleteModel(
            name='Collaboration',
        ),
        migrations.DeleteModel(
            name='ContentBlock',
        ),
        migrations.DeleteModel(
            name='CustomUser',
        ),
        migrations.DeleteModel(
            name='Permission',
        ),
        migrations.DeleteModel(
            name='Tag',
        ),
        migrations.DeleteModel(
            name='UserSettings',
        ),
    ]