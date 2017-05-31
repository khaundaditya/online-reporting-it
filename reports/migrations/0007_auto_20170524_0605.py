# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('reports', '0006_auto_20170519_0633'),
    ]

    operations = [
        migrations.AlterField(
            model_name='g2cservicereport',
            name='language_of_submission',
            field=models.CharField(max_length=30),
        ),
    ]
