# Generated by Django 5.2 on 2025-04-11 03:49

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pickle_app', '0002_location_player_delete_user'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='player',
            options={'ordering': ['-created_at']},
        ),
        migrations.RenameField(
            model_name='player',
            old_name='name',
            new_name='first_name',
        ),
        migrations.RenameField(
            model_name='player',
            old_name='username',
            new_name='last_name',
        ),
        migrations.RemoveField(
            model_name='player',
            name='skill_level',
        ),
        migrations.AddField(
            model_name='location',
            name='city',
            field=models.CharField(default='Unknown', max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='location',
            name='state',
            field=models.CharField(default='unknown', max_length=2),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='player',
            name='availability',
            field=models.JSONField(default=list),
        ),
        migrations.AddField(
            model_name='player',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='player',
            name='email',
            field=models.EmailField(default='unknown', max_length=254, unique=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='player',
            name='email_notifications',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='player',
            name='notifications_enabled',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='player',
            name='preferred_play',
            field=models.CharField(choices=[('Singles', 'Singles'), ('Doubles', 'Doubles'), ('Both', 'Both')], default='Both', max_length=10),
        ),
        migrations.AddField(
            model_name='player',
            name='push_notifications',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='player',
            name='skill_rating',
            field=models.DecimalField(decimal_places=1, default=3.0, max_digits=3),
        ),
        migrations.AddField(
            model_name='player',
            name='updated_at',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
