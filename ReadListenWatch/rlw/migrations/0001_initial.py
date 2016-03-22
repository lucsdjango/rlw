# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Condition',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Experiment',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=200)),
                ('instructions', models.TextField(max_length=2048, default='instruktioner')),
                ('welcomeText', models.CharField(max_length=200, default='welcome txt')),
                ('nParticipants', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Participant',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, primary_key=True, serialize=False)),
                ('age', models.IntegerField(default=0)),
                ('gender', models.CharField(choices=[('male', 'male'), ('female', 'female'), ('-', '-')], max_length=32, default='-')),
                ('hasFinished', models.BooleanField(default=False)),
                ('isExcluded', models.BooleanField(default=False)),
                ('condition', models.ForeignKey(to='rlw.Condition', related_name='participants')),
            ],
        ),
        migrations.CreateModel(
            name='Text',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, primary_key=True, serialize=False)),
                ('description', models.CharField(max_length=200, null=True, default=None, blank=True)),
                ('video', models.CharField(max_length=200, null=True, default=None, blank=True)),
                ('audio', models.CharField(max_length=200, null=True, default=None, blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='TextPage',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, primary_key=True, serialize=False)),
                ('idx', models.IntegerField(default=0)),
                ('startTime', models.FloatField(default=0.0)),
                ('group', models.ForeignKey(to='rlw.Text', related_name='pages')),
            ],
            options={
                'ordering': ['idx'],
            },
        ),
        migrations.AddField(
            model_name='condition',
            name='experiment',
            field=models.ForeignKey(to='rlw.Experiment', related_name='conditions'),
        ),
    ]
