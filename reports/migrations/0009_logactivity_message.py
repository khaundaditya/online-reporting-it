# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('reports', '0008_auto_20170524_1129'),
    ]

    operations = [
        migrations.AddField(
            model_name='logactivity',
            name='message',
            field=models.CharField(default=b'', max_length=100),
        ),
    ]
