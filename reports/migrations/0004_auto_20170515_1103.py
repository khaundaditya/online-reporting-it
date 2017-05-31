# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('reports', '0003_auto_20170407_0614'),
    ]

    operations = [
        migrations.AddField(
            model_name='cscreport',
            name='report_month',
            field=models.CharField(default=b'201704', max_length=20),
        ),
        migrations.AddField(
            model_name='dlreport',
            name='report_month',
            field=models.CharField(default=b'201704', max_length=20),
        ),
        migrations.AddField(
            model_name='g2cservicereport',
            name='report_month',
            field=models.CharField(default=b'201704', max_length=20),
        ),
        migrations.AddField(
            model_name='hardwarereport',
            name='report_month',
            field=models.CharField(default=b'201704', max_length=20),
        ),
        migrations.AddField(
            model_name='manpowerreport',
            name='report_month',
            field=models.CharField(default=b'201704', max_length=20),
        ),
        migrations.AddField(
            model_name='nofnreport',
            name='report_month',
            field=models.CharField(default=b'201704', max_length=20),
        ),
        migrations.AddField(
            model_name='servicetransreport',
            name='report_month',
            field=models.CharField(default=b'201704', max_length=20),
        ),
        migrations.AddField(
            model_name='softwarereport',
            name='report_month',
            field=models.CharField(default=b'201704', max_length=20),
        ),
        migrations.AddField(
            model_name='swanreport',
            name='report_month',
            field=models.CharField(default=b'201704', max_length=20),
        ),
    ]
