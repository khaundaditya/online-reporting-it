# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('reports', '0002_auto_20170406_1212'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='edistTransReport',
            new_name='ServiceTransReport',
        ),
    ]
