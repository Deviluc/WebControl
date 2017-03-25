# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-01-26 16:44
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Credential',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=200)),
                ('private_key', models.CharField(max_length=4000)),
            ],
        ),
        migrations.CreateModel(
            name='Server',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('display_name', models.CharField(max_length=100)),
                ('ip_host_name', models.CharField(max_length=200, unique=True)),
                ('is_ip', models.BooleanField(default=True)),
            ],
        ),
        migrations.AddField(
            model_name='credential',
            name='server',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='tomcats.Server'),
        ),
    ]
