# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('reports', '0005_auto_20170516_1008'),
    ]

    operations = [
        migrations.AlterField(
            model_name='g2cservicereport',
            name='mode_of_storage',
            field=models.CharField(max_length=12, choices=[(b'Local', b'Local'), (b'Central', b'Central')]),
        ),
    ]
