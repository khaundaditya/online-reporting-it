# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('reports', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='DigitalLiteracyReport',
            new_name='DLReport',
        ),
        migrations.RenameModel(
            old_name='edistrictTransactionReport',
            new_name='edistTransReport',
        ),
    ]
