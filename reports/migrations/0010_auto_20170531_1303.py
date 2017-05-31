# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('reports', '0009_logactivity_message'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cscreport',
            name='connectivity_modes',
            field=models.CharField(max_length=2, choices=[(b'B', b'Broadband'), (b'3G', b'3G Dongle'), (b'4G', b'4G Dongle'), (b'2G', b'2G/GPRS')]),
        ),
        migrations.AlterField(
            model_name='g2cservicereport',
            name='name_of_application',
            field=models.CharField(max_length=10, choices=[(b'Dharitree', b'Dharitree'), (b'ePanjeeyan', b'ePanjeeyan'), (b'eSetu', b'eSetu'), (b'CCTNS', b'CCTNS'), (b'Vahan', b'Vahan'), (b'eDistrict', b'eDistrict'), (b'Sarathi', b'Sarathi'), (b'NA', b'NA')]),
        ),
        migrations.AlterField(
            model_name='nofnreport',
            name='nofn_pop_build_at',
            field=models.CharField(max_length=10, choices=[(b'GP', b'GP'), (b'Block', b'Block')]),
        ),
        migrations.AlterField(
            model_name='softwarereport',
            name='appl_nm',
            field=models.CharField(max_length=15, choices=[(b'Dharitree', b'Dharitree'), (b'ePanjeeyan', b'ePanjeeyan'), (b'eSetu', b'eSetu'), (b'CCTNS', b'CCTNS'), (b'Vahan', b'Vahan'), (b'eDistrict', b'eDistrict'), (b'Sarathi', b'Sarathi'), (b'NA', b'NA')]),
        ),
    ]
