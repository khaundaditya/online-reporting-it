# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('reviewer', '0009_comment_comment_to'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='reportsnapshot',
            unique_together=set([('district', 'owner', 'report_type')]),
        ),
    ]
