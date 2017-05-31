# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('reports', '0007_auto_20170524_0605'),
    ]

    operations = [
        migrations.CreateModel(
            name='LogActivity',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('user', models.CharField(max_length=40)),
                ('report_name', models.CharField(max_length=40)),
                ('district', models.CharField(max_length=50)),
                ('submitted_time', models.DateTimeField()),
            ],
        ),
        migrations.AlterField(
            model_name='g2cservicereport',
            name='service_nm',
            field=models.CharField(max_length=150, choices=[(b'Next of Kin certificate', b'Next of Kin certificate'), (b'Senior Citizen Certificate', b'Senior Citizen Certificate'), (b'Delayed Birth Permission', b'Delayed Birth Permission'), (b'Delayed Death Permission', b'Delayed Death Permission'), (b'Issuance of Birth Certificate', b'Issuance of Birth Certificate'), (b'Issuance of Death Certificate', b'Issuance of Death Certificate'), (b'Permanent Resident Certificate', b'Permanent Resident Certificate'), (b'Renewal of Explosive License', b'Renewal of Explosive License'), (b'Permission for Special Events u/s 144 CrPC', b'Permission for Special Events u/s 144 CrPC'), (b'Permission for Fairs/Religious/ Cultural Festivals/Loud Speakers/ Rallies/Strikes', b'Permission for Fairs/Religious/ Cultural Festivals/Loud Speakers/ Rallies/Strikes'), (b'Income Certificate', b'Income Certificate'), (b'Bakijai Clearance Certificate', b'Bakijai Clearance Certificate'), (b'Application for Court Marriage', b'Application for Court Marriage'), (b'Application for Marriage Certificate', b'Application for Marriage Certificate'), (b'Application for Stamp Vendor License', b'Application for Stamp Vendor License'), (b'Submission of Application for Mutation', b'Submission of Application for Mutation'), (b'Certified Copy of Mutation Order', b'Certified Copy of Mutation Order'), (b'Issue of Land Valuation Certificate', b'Issue of Land Valuation Certificate'), (b'Issue of Record of Rights (Jamabandi)', b'Issue of Record of Rights (Jamabandi)'), (b'Issue of Non Encumbrance Certificate', b'Issue of Non Encumbrance Certificate'), (b'Issue of Land Holding Certificate', b'Issue of Land Holding Certificate'), (b'Application for Registration of Deeds, etc.', b'Application for Registration of Deeds, etc.'), (b'Permission for Transfer of Property by way of Mortgage, Lease, Gift, Sale, etc.', b'Permission for Transfer of Property by way of Mortgage, Lease, Gift, Sale, etc.'), (b'Assessment of Stamp Duty and Registration Fees', b'Assessment of Stamp Duty and Registration Fees'), (b'Certified Copies of cause list, judgements, etc', b'Certified Copies of cause list, judgements, etc'), (b'Registration of name in employment exchange', b'Registration of name in employment exchange'), (b'Application for change of name/ address/ age in employment exchange', b'Application for change of name/ address/ age in employment exchange'), (b'Application for transfer of enrollment to other district employment exchange', b'Application for transfer of enrollment to other district employment exchange'), (b'Surrender of Employment Exchange Card', b'Surrender of Employment Exchange Card'), (b'Issue of Duplicate Mark sheet', b'Issue of Duplicate Mark sheet'), (b'Issue of Duplicate Pass Certificate', b'Issue of Duplicate Pass Certificate'), (b'Issue of Migration Certificate', b'Issue of Migration Certificate'), (b'Issue of Duplicate Mark sheet', b'Issue of Duplicate Mark sheet'), (b'Issue of Duplicate Pass Certificate', b'Issue of Duplicate Pass Certificate'), (b'Issue of Migration Certificate', b'Issue of Migration Certificate'), (b'Non-Creamy layer Certificate', b'Non-Creamy layer Certificate'), (b'Caste Certificate for SC', b'Caste Certificate for SC'), (b'Application for Driving License', b'Application for Driving License'), (b'Application for Renewal of Driving License', b'Application for Renewal of Driving License'), (b'Application for Learners License', b'Application for Learners License'), (b'Application for Driving Test', b'Application for Driving Test'), (b'Application for grant of Fresh License to sell stock etc', b'Application for grant of Fresh License to sell stock etc'), (b'Application for grant of Renewal of License to sell stock etc', b'Application for grant of Renewal of License to sell stock etc'), (b'Application for Information under RTI', b'Application for Information under RTI'), (b'RTI Appeal', b'RTI Appeal'), (b'Certified Copy of Electoral Roll', b'Certified Copy of Electoral Roll')]),
        ),
        migrations.AlterField(
            model_name='servicetransreport',
            name='service_nm',
            field=models.CharField(max_length=150, choices=[(b'Next of Kin certificate', b'Next of Kin certificate'), (b'Senior Citizen Certificate', b'Senior Citizen Certificate'), (b'Delayed Birth Permission', b'Delayed Birth Permission'), (b'Delayed Death Permission', b'Delayed Death Permission'), (b'Issuance of Birth Certificate', b'Issuance of Birth Certificate'), (b'Issuance of Death Certificate', b'Issuance of Death Certificate'), (b'Permanent Resident Certificate', b'Permanent Resident Certificate'), (b'Renewal of Explosive License', b'Renewal of Explosive License'), (b'Permission for Special Events u/s 144 CrPC', b'Permission for Special Events u/s 144 CrPC'), (b'Permission for Fairs/Religious/ Cultural Festivals/Loud Speakers/ Rallies/Strikes', b'Permission for Fairs/Religious/ Cultural Festivals/Loud Speakers/ Rallies/Strikes'), (b'Income Certificate', b'Income Certificate'), (b'Bakijai Clearance Certificate', b'Bakijai Clearance Certificate'), (b'Application for Court Marriage', b'Application for Court Marriage'), (b'Application for Marriage Certificate', b'Application for Marriage Certificate'), (b'Application for Stamp Vendor License', b'Application for Stamp Vendor License'), (b'Submission of Application for Mutation', b'Submission of Application for Mutation'), (b'Certified Copy of Mutation Order', b'Certified Copy of Mutation Order'), (b'Issue of Land Valuation Certificate', b'Issue of Land Valuation Certificate'), (b'Issue of Record of Rights (Jamabandi)', b'Issue of Record of Rights (Jamabandi)'), (b'Issue of Non Encumbrance Certificate', b'Issue of Non Encumbrance Certificate'), (b'Issue of Land Holding Certificate', b'Issue of Land Holding Certificate'), (b'Application for Registration of Deeds, etc.', b'Application for Registration of Deeds, etc.'), (b'Permission for Transfer of Property by way of Mortgage, Lease, Gift, Sale, etc.', b'Permission for Transfer of Property by way of Mortgage, Lease, Gift, Sale, etc.'), (b'Assessment of Stamp Duty and Registration Fees', b'Assessment of Stamp Duty and Registration Fees'), (b'Certified Copies of cause list, judgements, etc', b'Certified Copies of cause list, judgements, etc'), (b'Registration of name in employment exchange', b'Registration of name in employment exchange'), (b'Application for change of name/ address/ age in employment exchange', b'Application for change of name/ address/ age in employment exchange'), (b'Application for transfer of enrollment to other district employment exchange', b'Application for transfer of enrollment to other district employment exchange'), (b'Surrender of Employment Exchange Card', b'Surrender of Employment Exchange Card'), (b'Issue of Duplicate Mark sheet', b'Issue of Duplicate Mark sheet'), (b'Issue of Duplicate Pass Certificate', b'Issue of Duplicate Pass Certificate'), (b'Issue of Migration Certificate', b'Issue of Migration Certificate'), (b'Issue of Duplicate Mark sheet', b'Issue of Duplicate Mark sheet'), (b'Issue of Duplicate Pass Certificate', b'Issue of Duplicate Pass Certificate'), (b'Issue of Migration Certificate', b'Issue of Migration Certificate'), (b'Non-Creamy layer Certificate', b'Non-Creamy layer Certificate'), (b'Caste Certificate for SC', b'Caste Certificate for SC'), (b'Application for Driving License', b'Application for Driving License'), (b'Application for Renewal of Driving License', b'Application for Renewal of Driving License'), (b'Application for Learners License', b'Application for Learners License'), (b'Application for Driving Test', b'Application for Driving Test'), (b'Application for grant of Fresh License to sell stock etc', b'Application for grant of Fresh License to sell stock etc'), (b'Application for grant of Renewal of License to sell stock etc', b'Application for grant of Renewal of License to sell stock etc'), (b'Application for Information under RTI', b'Application for Information under RTI'), (b'RTI Appeal', b'RTI Appeal'), (b'Certified Copy of Electoral Roll', b'Certified Copy of Electoral Roll')]),
        ),
    ]
