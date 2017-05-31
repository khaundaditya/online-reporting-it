# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('reports', '0004_auto_20170515_1103'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dlreport',
            name='district',
            field=models.CharField(blank=True, max_length=30, choices=[(b'BK', b'Baksa'), (b'BP', b'Barpeta'), (b'BS', b'Biswanath'), (b'BO', b'Bongaigaon'), (b'CA', b'Cachar'), (b'CD', b'Charaideo'), (b'CH', b'Chirang'), (b'DR', b'Darrang'), (b'DM', b'Dhemaji'), (b'DU', b'Dhubri'), (b'DI', b'Dibrugarh'), (b'GP', b'Goalpara'), (b'GG', b'Golaghat'), (b'HA', b'Hailakandi'), (b'HJ', b'Hojai'), (b'JO', b'Jorhat'), (b'KM', b'Kamrup Metropolitan'), (b'KU', b'Kamrup'), (b'KG', b'Karbi Anglong'), (b'KR', b'Karimganj'), (b'KJ', b'Kokrajhar'), (b'LA', b'Lakhimpur'), (b'MJ', b'Majuli'), (b'MA', b'Morigaon'), (b'NN', b'Nagaon'), (b'NB', b'Nalbari'), (b'NC', b'Dima Hasao'), (b'SV', b'Sivasagar'), (b'ST', b'Sonitpur'), (b'SM', b'South Salmara-Mankachar'), (b'TI', b'Tinsukia'), (b'UD', b'Udalguri'), (b'WK', b'West Karbi Anglong')]),
        ),
        migrations.AlterField(
            model_name='g2cservicereport',
            name='district',
            field=models.CharField(blank=True, max_length=30, choices=[(b'BK', b'Baksa'), (b'BP', b'Barpeta'), (b'BS', b'Biswanath'), (b'BO', b'Bongaigaon'), (b'CA', b'Cachar'), (b'CD', b'Charaideo'), (b'CH', b'Chirang'), (b'DR', b'Darrang'), (b'DM', b'Dhemaji'), (b'DU', b'Dhubri'), (b'DI', b'Dibrugarh'), (b'GP', b'Goalpara'), (b'GG', b'Golaghat'), (b'HA', b'Hailakandi'), (b'HJ', b'Hojai'), (b'JO', b'Jorhat'), (b'KM', b'Kamrup Metropolitan'), (b'KU', b'Kamrup'), (b'KG', b'Karbi Anglong'), (b'KR', b'Karimganj'), (b'KJ', b'Kokrajhar'), (b'LA', b'Lakhimpur'), (b'MJ', b'Majuli'), (b'MA', b'Morigaon'), (b'NN', b'Nagaon'), (b'NB', b'Nalbari'), (b'NC', b'Dima Hasao'), (b'SV', b'Sivasagar'), (b'ST', b'Sonitpur'), (b'SM', b'South Salmara-Mankachar'), (b'TI', b'Tinsukia'), (b'UD', b'Udalguri'), (b'WK', b'West Karbi Anglong')]),
        ),
        migrations.AlterField(
            model_name='hardwarereport',
            name='district',
            field=models.CharField(blank=True, max_length=30, choices=[(b'BK', b'Baksa'), (b'BP', b'Barpeta'), (b'BS', b'Biswanath'), (b'BO', b'Bongaigaon'), (b'CA', b'Cachar'), (b'CD', b'Charaideo'), (b'CH', b'Chirang'), (b'DR', b'Darrang'), (b'DM', b'Dhemaji'), (b'DU', b'Dhubri'), (b'DI', b'Dibrugarh'), (b'GP', b'Goalpara'), (b'GG', b'Golaghat'), (b'HA', b'Hailakandi'), (b'HJ', b'Hojai'), (b'JO', b'Jorhat'), (b'KM', b'Kamrup Metropolitan'), (b'KU', b'Kamrup'), (b'KG', b'Karbi Anglong'), (b'KR', b'Karimganj'), (b'KJ', b'Kokrajhar'), (b'LA', b'Lakhimpur'), (b'MJ', b'Majuli'), (b'MA', b'Morigaon'), (b'NN', b'Nagaon'), (b'NB', b'Nalbari'), (b'NC', b'Dima Hasao'), (b'SV', b'Sivasagar'), (b'ST', b'Sonitpur'), (b'SM', b'South Salmara-Mankachar'), (b'TI', b'Tinsukia'), (b'UD', b'Udalguri'), (b'WK', b'West Karbi Anglong')]),
        ),
        migrations.AlterField(
            model_name='nofnreport',
            name='district',
            field=models.CharField(blank=True, max_length=30, choices=[(b'BK', b'Baksa'), (b'BP', b'Barpeta'), (b'BS', b'Biswanath'), (b'BO', b'Bongaigaon'), (b'CA', b'Cachar'), (b'CD', b'Charaideo'), (b'CH', b'Chirang'), (b'DR', b'Darrang'), (b'DM', b'Dhemaji'), (b'DU', b'Dhubri'), (b'DI', b'Dibrugarh'), (b'GP', b'Goalpara'), (b'GG', b'Golaghat'), (b'HA', b'Hailakandi'), (b'HJ', b'Hojai'), (b'JO', b'Jorhat'), (b'KM', b'Kamrup Metropolitan'), (b'KU', b'Kamrup'), (b'KG', b'Karbi Anglong'), (b'KR', b'Karimganj'), (b'KJ', b'Kokrajhar'), (b'LA', b'Lakhimpur'), (b'MJ', b'Majuli'), (b'MA', b'Morigaon'), (b'NN', b'Nagaon'), (b'NB', b'Nalbari'), (b'NC', b'Dima Hasao'), (b'SV', b'Sivasagar'), (b'ST', b'Sonitpur'), (b'SM', b'South Salmara-Mankachar'), (b'TI', b'Tinsukia'), (b'UD', b'Udalguri'), (b'WK', b'West Karbi Anglong')]),
        ),
        migrations.AlterField(
            model_name='servicetransreport',
            name='district',
            field=models.CharField(blank=True, max_length=30, choices=[(b'BK', b'Baksa'), (b'BP', b'Barpeta'), (b'BS', b'Biswanath'), (b'BO', b'Bongaigaon'), (b'CA', b'Cachar'), (b'CD', b'Charaideo'), (b'CH', b'Chirang'), (b'DR', b'Darrang'), (b'DM', b'Dhemaji'), (b'DU', b'Dhubri'), (b'DI', b'Dibrugarh'), (b'GP', b'Goalpara'), (b'GG', b'Golaghat'), (b'HA', b'Hailakandi'), (b'HJ', b'Hojai'), (b'JO', b'Jorhat'), (b'KM', b'Kamrup Metropolitan'), (b'KU', b'Kamrup'), (b'KG', b'Karbi Anglong'), (b'KR', b'Karimganj'), (b'KJ', b'Kokrajhar'), (b'LA', b'Lakhimpur'), (b'MJ', b'Majuli'), (b'MA', b'Morigaon'), (b'NN', b'Nagaon'), (b'NB', b'Nalbari'), (b'NC', b'Dima Hasao'), (b'SV', b'Sivasagar'), (b'ST', b'Sonitpur'), (b'SM', b'South Salmara-Mankachar'), (b'TI', b'Tinsukia'), (b'UD', b'Udalguri'), (b'WK', b'West Karbi Anglong')]),
        ),
        migrations.AlterField(
            model_name='softwarereport',
            name='district',
            field=models.CharField(blank=True, max_length=30, choices=[(b'BK', b'Baksa'), (b'BP', b'Barpeta'), (b'BS', b'Biswanath'), (b'BO', b'Bongaigaon'), (b'CA', b'Cachar'), (b'CD', b'Charaideo'), (b'CH', b'Chirang'), (b'DR', b'Darrang'), (b'DM', b'Dhemaji'), (b'DU', b'Dhubri'), (b'DI', b'Dibrugarh'), (b'GP', b'Goalpara'), (b'GG', b'Golaghat'), (b'HA', b'Hailakandi'), (b'HJ', b'Hojai'), (b'JO', b'Jorhat'), (b'KM', b'Kamrup Metropolitan'), (b'KU', b'Kamrup'), (b'KG', b'Karbi Anglong'), (b'KR', b'Karimganj'), (b'KJ', b'Kokrajhar'), (b'LA', b'Lakhimpur'), (b'MJ', b'Majuli'), (b'MA', b'Morigaon'), (b'NN', b'Nagaon'), (b'NB', b'Nalbari'), (b'NC', b'Dima Hasao'), (b'SV', b'Sivasagar'), (b'ST', b'Sonitpur'), (b'SM', b'South Salmara-Mankachar'), (b'TI', b'Tinsukia'), (b'UD', b'Udalguri'), (b'WK', b'West Karbi Anglong')]),
        ),
        migrations.AlterField(
            model_name='swanreport',
            name='district',
            field=models.CharField(blank=True, max_length=30, choices=[(b'BK', b'Baksa'), (b'BP', b'Barpeta'), (b'BS', b'Biswanath'), (b'BO', b'Bongaigaon'), (b'CA', b'Cachar'), (b'CD', b'Charaideo'), (b'CH', b'Chirang'), (b'DR', b'Darrang'), (b'DM', b'Dhemaji'), (b'DU', b'Dhubri'), (b'DI', b'Dibrugarh'), (b'GP', b'Goalpara'), (b'GG', b'Golaghat'), (b'HA', b'Hailakandi'), (b'HJ', b'Hojai'), (b'JO', b'Jorhat'), (b'KM', b'Kamrup Metropolitan'), (b'KU', b'Kamrup'), (b'KG', b'Karbi Anglong'), (b'KR', b'Karimganj'), (b'KJ', b'Kokrajhar'), (b'LA', b'Lakhimpur'), (b'MJ', b'Majuli'), (b'MA', b'Morigaon'), (b'NN', b'Nagaon'), (b'NB', b'Nalbari'), (b'NC', b'Dima Hasao'), (b'SV', b'Sivasagar'), (b'ST', b'Sonitpur'), (b'SM', b'South Salmara-Mankachar'), (b'TI', b'Tinsukia'), (b'UD', b'Udalguri'), (b'WK', b'West Karbi Anglong')]),
        ),
    ]
