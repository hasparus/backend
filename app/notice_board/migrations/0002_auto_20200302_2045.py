# Generated by Django 3.0.3 on 2020-03-02 19:45

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('notice_board', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='guild',
            name='members',
            field=models.ManyToManyField(through='notice_board.GuildUser', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='guilduser',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='meeting',
            name='organizer',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='meeting',
            name='users',
            field=models.ManyToManyField(related_name='meetings', through='notice_board.MeetingUser', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='meetinguser',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='sphere',
            name='users',
            field=models.ManyToManyField(to=settings.AUTH_USER_MODEL),
        ),
    ]