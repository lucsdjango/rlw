# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rlw', '0002_textpage_txt'),
    ]

    operations = [
        migrations.AlterField(
            model_name='textpage',
            name='txt',
            field=models.TextField(max_length=200),
        ),
    ]
