# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rlw', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='textpage',
            name='txt',
            field=models.CharField(default='hej', max_length=200),
            preserve_default=False,
        ),
    ]
