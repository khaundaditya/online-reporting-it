# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CSCReport',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('omt_id', models.CharField(blank=True, max_length=50, null=True, validators=[django.core.validators.RegexValidator(b'^[0-9a-zA-Z]*$', b'Only alphanumeric characters are allowed.')])),
                ('vle_name', models.CharField(max_length=50, null=True, blank=True)),
                ('gaon_panchayat_name', models.CharField(max_length=100, null=True, blank=True)),
                ('address', models.CharField(max_length=100, null=True, blank=True)),
                ('mobile_number', models.CharField(max_length=12)),
                ('infra_details', models.CharField(max_length=100, null=True, blank=True)),
                ('connectivity_modes', models.CharField(max_length=2, choices=[(b'B', b'Broadband'), (b'3G', b'3G Dongle'), (b'4G', b'4G Dongle')])),
                ('num_g2c_and_g2g_services', models.IntegerField()),
                ('num_g2b_and_other_services', models.IntegerField()),
                ('remarks', models.CharField(max_length=100, null=True, blank=True)),
                ('district', models.CharField(blank=True, max_length=30, choices=[(b'BK', b'Baksa'), (b'BP', b'Barpeta'), (b'BS', b'Biswanath'), (b'BO', b'Bongaigaon'), (b'CA', b'Cachar'), (b'CD', b'Charaideo'), (b'CH', b'Chirang'), (b'DR', b'Darrang'), (b'DM', b'Dhemaji'), (b'DU', b'Dhubri'), (b'DI', b'Dibrugarh'), (b'GP', b'Goalpara'), (b'GG', b'Golaghat'), (b'HA', b'Hailakandi'), (b'HJ', b'Hojai'), (b'JO', b'Jorhat'), (b'KM', b'Kamrup Metropolitan'), (b'KU', b'Kamrup'), (b'KG', b'Karbi Anglong'), (b'KR', b'Karimganj'), (b'KJ', b'Kokrajhar'), (b'LA', b'Lakhimpur'), (b'MJ', b'Majuli'), (b'MA', b'Morigaon'), (b'NN', b'Nagaon'), (b'NB', b'Nalbari'), (b'NC', b'Dima Hasao'), (b'SV', b'Sivasagar'), (b'ST', b'Sonitpur'), (b'SM', b'South Salmara-Mankachar'), (b'TI', b'Tinsukia'), (b'UD', b'Udalguri'), (b'WK', b'West Karbi Anglong')])),
                ('updated_date', models.CharField(max_length=10)),
                ('user_name', models.CharField(default=b'', max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='DigitalLiteracyReport',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('lac_name', models.CharField(max_length=50, null=True, blank=True)),
                ('num_training_centres', models.IntegerField()),
                ('num_examination_centres_near_gp', models.CharField(max_length=100, null=True, blank=True)),
                ('num_beneficiaries_registered', models.IntegerField()),
                ('num_beneficiaries_under_training', models.IntegerField()),
                ('num_beneficiaries_trained', models.IntegerField()),
                ('num_beneficiaries_appeared_in_exam', models.IntegerField()),
                ('num_beneficiaries_passed_in_exam', models.IntegerField()),
                ('district', models.CharField(max_length=30, choices=[(b'BK', b'Baksa'), (b'BP', b'Barpeta'), (b'BS', b'Biswanath'), (b'BO', b'Bongaigaon'), (b'CA', b'Cachar'), (b'CD', b'Charaideo'), (b'CH', b'Chirang'), (b'DR', b'Darrang'), (b'DM', b'Dhemaji'), (b'DU', b'Dhubri'), (b'DI', b'Dibrugarh'), (b'GP', b'Goalpara'), (b'GG', b'Golaghat'), (b'HA', b'Hailakandi'), (b'HJ', b'Hojai'), (b'JO', b'Jorhat'), (b'KM', b'Kamrup Metropolitan'), (b'KU', b'Kamrup'), (b'KG', b'Karbi Anglong'), (b'KR', b'Karimganj'), (b'KJ', b'Kokrajhar'), (b'LA', b'Lakhimpur'), (b'MJ', b'Majuli'), (b'MA', b'Morigaon'), (b'NN', b'Nagaon'), (b'NB', b'Nalbari'), (b'NC', b'Dima Hasao'), (b'SV', b'Sivasagar'), (b'ST', b'Sonitpur'), (b'SM', b'South Salmara-Mankachar'), (b'TI', b'Tinsukia'), (b'UD', b'Udalguri'), (b'WK', b'West Karbi Anglong')])),
                ('updated_date', models.CharField(max_length=10)),
                ('user_name', models.CharField(default=b'', max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='edistrictTransactionReport',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('service_nm', models.CharField(max_length=60, choices=[(b'Next of Kin certificate', b'Next of Kin certificate'), (b'Senior Citizen Certificate', b'Senior Citizen Certificate'), (b'Delayed Birth Permission', b'Delayed Birth Permission'), (b'Delayed Death Permission', b'Delayed Death Permission'), (b'Issuance of Birth Certificate', b'Issuance of Birth Certificate'), (b'Issuance of Death Certificate', b'Issuance of Death Certificate'), (b'Permanent Resident Certificate', b'Permanent Resident Certificate'), (b'Renewal of Explosive License', b'Renewal of Explosive License'), (b'Permission for Special Events u/s 144 CrPC', b'Permission for Special Events u/s 144 CrPC'), (b'Permission for Fairs/Religious/ Cultural Festivals/Loud Speakers/ Rallies/Strikes', b'Permission for Fairs/Religious/ Cultural Festivals/Loud Speakers/ Rallies/Strikes'), (b'Income Certificate', b'Income Certificate'), (b'Bakijai Clearance Certificate', b'Bakijai Clearance Certificate'), (b'Application for Court Marriage', b'Application for Court Marriage'), (b'Application for Marriage Certificate', b'Application for Marriage Certificate'), (b'Application for Stamp Vendor License', b'Application for Stamp Vendor License'), (b'Submission of Application for Mutation', b'Submission of Application for Mutation'), (b'Certified Copy of Mutation Order', b'Certified Copy of Mutation Order'), (b'Issue of Land Valuation Certificate', b'Issue of Land Valuation Certificate'), (b'Issue of Record of Rights (Jamabandi)', b'Issue of Record of Rights (Jamabandi)'), (b'Issue of Non Encumbrance Certificate', b'Issue of Non Encumbrance Certificate'), (b'Issue of Land Holding Certificate', b'Issue of Land Holding Certificate'), (b'Application for Registration of Deeds, etc.', b'Application for Registration of Deeds, etc.'), (b'Permission for Transfer of Property by way of Mortgage, Lease, Gift, Sale, etc.', b'Permission for Transfer of Property by way of Mortgage, Lease, Gift, Sale, etc.'), (b'Assessment of Stamp Duty and Registration Fees', b'Assessment of Stamp Duty and Registration Fees'), (b'Certified Copies of cause list, judgements, etc', b'Certified Copies of cause list, judgements, etc'), (b'Registration of name in employment exchange', b'Registration of name in employment exchange'), (b'Application for change of name/ address/ age in employment exchange', b'Application for change of name/ address/ age in employment exchange'), (b'Application for transfer of enrollment to other district employment exchange', b'Application for transfer of enrollment to other district employment exchange'), (b'Surrender of Employment Exchange Card', b'Surrender of Employment Exchange Card'), (b'Issue of Duplicate Mark sheet', b'Issue of Duplicate Mark sheet'), (b'Issue of Duplicate Pass Certificate', b'Issue of Duplicate Pass Certificate'), (b'Issue of Migration Certificate', b'Issue of Migration Certificate'), (b'Issue of Duplicate Mark sheet', b'Issue of Duplicate Mark sheet'), (b'Issue of Duplicate Pass Certificate', b'Issue of Duplicate Pass Certificate'), (b'Issue of Migration Certificate', b'Issue of Migration Certificate'), (b'Non-Creamy layer Certificate', b'Non-Creamy layer Certificate'), (b'Caste Certificate for SC', b'Caste Certificate for SC'), (b'Application for Driving License', b'Application for Driving License'), (b'Application for Renewal of Driving License', b'Application for Renewal of Driving License'), (b'Application for Learners License', b'Application for Learners License'), (b'Application for Driving Test', b'Application for Driving Test'), (b'Application for grant of Fresh License to sell stock etc', b'Application for grant of Fresh License to sell stock etc'), (b'Application for grant of Renewal of License to sell stock etc', b'Application for grant of Renewal of License to sell stock etc'), (b'Application for Information under RTI', b'Application for Information under RTI'), (b'RTI Appeal', b'RTI Appeal'), (b'Certified Copy of Electoral Roll', b'Certified Copy of Electoral Roll')])),
                ('associated_line_department', models.CharField(max_length=20)),
                ('total_transactions', models.IntegerField()),
                ('service_charge', models.FloatField()),
                ('statutory_charge', models.FloatField()),
                ('total_revenue', models.FloatField()),
                ('district', models.CharField(max_length=30, choices=[(b'BK', b'Baksa'), (b'BP', b'Barpeta'), (b'BS', b'Biswanath'), (b'BO', b'Bongaigaon'), (b'CA', b'Cachar'), (b'CD', b'Charaideo'), (b'CH', b'Chirang'), (b'DR', b'Darrang'), (b'DM', b'Dhemaji'), (b'DU', b'Dhubri'), (b'DI', b'Dibrugarh'), (b'GP', b'Goalpara'), (b'GG', b'Golaghat'), (b'HA', b'Hailakandi'), (b'HJ', b'Hojai'), (b'JO', b'Jorhat'), (b'KM', b'Kamrup Metropolitan'), (b'KU', b'Kamrup'), (b'KG', b'Karbi Anglong'), (b'KR', b'Karimganj'), (b'KJ', b'Kokrajhar'), (b'LA', b'Lakhimpur'), (b'MJ', b'Majuli'), (b'MA', b'Morigaon'), (b'NN', b'Nagaon'), (b'NB', b'Nalbari'), (b'NC', b'Dima Hasao'), (b'SV', b'Sivasagar'), (b'ST', b'Sonitpur'), (b'SM', b'South Salmara-Mankachar'), (b'TI', b'Tinsukia'), (b'UD', b'Udalguri'), (b'WK', b'West Karbi Anglong')])),
                ('updated_date', models.CharField(max_length=10)),
                ('user_name', models.CharField(default=b'', max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='g2cServiceReport',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('service_nm', models.CharField(max_length=60, choices=[(b'Next of Kin certificate', b'Next of Kin certificate'), (b'Senior Citizen Certificate', b'Senior Citizen Certificate'), (b'Delayed Birth Permission', b'Delayed Birth Permission'), (b'Delayed Death Permission', b'Delayed Death Permission'), (b'Issuance of Birth Certificate', b'Issuance of Birth Certificate'), (b'Issuance of Death Certificate', b'Issuance of Death Certificate'), (b'Permanent Resident Certificate', b'Permanent Resident Certificate'), (b'Renewal of Explosive License', b'Renewal of Explosive License'), (b'Permission for Special Events u/s 144 CrPC', b'Permission for Special Events u/s 144 CrPC'), (b'Permission for Fairs/Religious/ Cultural Festivals/Loud Speakers/ Rallies/Strikes', b'Permission for Fairs/Religious/ Cultural Festivals/Loud Speakers/ Rallies/Strikes'), (b'Income Certificate', b'Income Certificate'), (b'Bakijai Clearance Certificate', b'Bakijai Clearance Certificate'), (b'Application for Court Marriage', b'Application for Court Marriage'), (b'Application for Marriage Certificate', b'Application for Marriage Certificate'), (b'Application for Stamp Vendor License', b'Application for Stamp Vendor License'), (b'Submission of Application for Mutation', b'Submission of Application for Mutation'), (b'Certified Copy of Mutation Order', b'Certified Copy of Mutation Order'), (b'Issue of Land Valuation Certificate', b'Issue of Land Valuation Certificate'), (b'Issue of Record of Rights (Jamabandi)', b'Issue of Record of Rights (Jamabandi)'), (b'Issue of Non Encumbrance Certificate', b'Issue of Non Encumbrance Certificate'), (b'Issue of Land Holding Certificate', b'Issue of Land Holding Certificate'), (b'Application for Registration of Deeds, etc.', b'Application for Registration of Deeds, etc.'), (b'Permission for Transfer of Property by way of Mortgage, Lease, Gift, Sale, etc.', b'Permission for Transfer of Property by way of Mortgage, Lease, Gift, Sale, etc.'), (b'Assessment of Stamp Duty and Registration Fees', b'Assessment of Stamp Duty and Registration Fees'), (b'Certified Copies of cause list, judgements, etc', b'Certified Copies of cause list, judgements, etc'), (b'Registration of name in employment exchange', b'Registration of name in employment exchange'), (b'Application for change of name/ address/ age in employment exchange', b'Application for change of name/ address/ age in employment exchange'), (b'Application for transfer of enrollment to other district employment exchange', b'Application for transfer of enrollment to other district employment exchange'), (b'Surrender of Employment Exchange Card', b'Surrender of Employment Exchange Card'), (b'Issue of Duplicate Mark sheet', b'Issue of Duplicate Mark sheet'), (b'Issue of Duplicate Pass Certificate', b'Issue of Duplicate Pass Certificate'), (b'Issue of Migration Certificate', b'Issue of Migration Certificate'), (b'Issue of Duplicate Mark sheet', b'Issue of Duplicate Mark sheet'), (b'Issue of Duplicate Pass Certificate', b'Issue of Duplicate Pass Certificate'), (b'Issue of Migration Certificate', b'Issue of Migration Certificate'), (b'Non-Creamy layer Certificate', b'Non-Creamy layer Certificate'), (b'Caste Certificate for SC', b'Caste Certificate for SC'), (b'Application for Driving License', b'Application for Driving License'), (b'Application for Renewal of Driving License', b'Application for Renewal of Driving License'), (b'Application for Learners License', b'Application for Learners License'), (b'Application for Driving Test', b'Application for Driving Test'), (b'Application for grant of Fresh License to sell stock etc', b'Application for grant of Fresh License to sell stock etc'), (b'Application for grant of Renewal of License to sell stock etc', b'Application for grant of Renewal of License to sell stock etc'), (b'Application for Information under RTI', b'Application for Information under RTI'), (b'RTI Appeal', b'RTI Appeal'), (b'Certified Copy of Electoral Roll', b'Certified Copy of Electoral Roll')])),
                ('associated_line_department', models.CharField(max_length=20)),
                ('delivery_channel', models.CharField(max_length=10, choices=[(b'Online', b'Online'), (b'Offline', b'Offline')])),
                ('name_of_application', models.CharField(max_length=10, choices=[(b'Dharitree', b'Dharitree'), (b'ePanjeeyan', b'ePanjeeyan'), (b'eSetu', b'eSetu'), (b'CCTNS', b'CCTNS'), (b'Vahan', b'Vahan'), (b'eDistrict', b'eDistrict')])),
                ('is_digitally_signed', models.BooleanField(default=True)),
                ('is_computerized', models.CharField(max_length=10, choices=[(b'Yes', b'Yes'), (b'No', b'No'), (b'Partially', b'Partially')])),
                ('language_of_submission', models.CharField(max_length=10, choices=[(b'Assamese', b'Assamese'), (b'English', b'English'), (b'Bengali', b'Bengali'), (b'Bodo', b'Bodo')])),
                ('is_legacy_data_digitized', models.BooleanField(default=True)),
                ('from_when', models.CharField(max_length=20)),
                ('mode_of_storage', models.CharField(max_length=10, choices=[(b'Local', b'Local'), (b'Centralized', b'Centralized')])),
                ('remarks', models.CharField(max_length=100)),
                ('district', models.CharField(max_length=30, choices=[(b'BK', b'Baksa'), (b'BP', b'Barpeta'), (b'BS', b'Biswanath'), (b'BO', b'Bongaigaon'), (b'CA', b'Cachar'), (b'CD', b'Charaideo'), (b'CH', b'Chirang'), (b'DR', b'Darrang'), (b'DM', b'Dhemaji'), (b'DU', b'Dhubri'), (b'DI', b'Dibrugarh'), (b'GP', b'Goalpara'), (b'GG', b'Golaghat'), (b'HA', b'Hailakandi'), (b'HJ', b'Hojai'), (b'JO', b'Jorhat'), (b'KM', b'Kamrup Metropolitan'), (b'KU', b'Kamrup'), (b'KG', b'Karbi Anglong'), (b'KR', b'Karimganj'), (b'KJ', b'Kokrajhar'), (b'LA', b'Lakhimpur'), (b'MJ', b'Majuli'), (b'MA', b'Morigaon'), (b'NN', b'Nagaon'), (b'NB', b'Nalbari'), (b'NC', b'Dima Hasao'), (b'SV', b'Sivasagar'), (b'ST', b'Sonitpur'), (b'SM', b'South Salmara-Mankachar'), (b'TI', b'Tinsukia'), (b'UD', b'Udalguri'), (b'WK', b'West Karbi Anglong')])),
                ('updated_date', models.CharField(max_length=10)),
                ('user_name', models.CharField(default=b'', max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='HardwareReport',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('hardware_nm', models.CharField(max_length=20, choices=[(b'Desktop', b'Desktop'), (b'Laptop', b'Laptop'), (b'Printers', b'Printers'), (b'Scanner', b'Scanner'), (b'UPS', b'UPS'), (b'Switch', b'Switch'), (b'Server Computer', b'Server Computer')])),
                ('quantity', models.IntegerField()),
                ('status', models.CharField(max_length=60)),
                ('hw_in_stock', models.CharField(max_length=60)),
                ('is_amc_avaialable', models.CharField(max_length=60)),
                ('remarks', models.CharField(max_length=100)),
                ('district', models.CharField(max_length=30, choices=[(b'BK', b'Baksa'), (b'BP', b'Barpeta'), (b'BS', b'Biswanath'), (b'BO', b'Bongaigaon'), (b'CA', b'Cachar'), (b'CD', b'Charaideo'), (b'CH', b'Chirang'), (b'DR', b'Darrang'), (b'DM', b'Dhemaji'), (b'DU', b'Dhubri'), (b'DI', b'Dibrugarh'), (b'GP', b'Goalpara'), (b'GG', b'Golaghat'), (b'HA', b'Hailakandi'), (b'HJ', b'Hojai'), (b'JO', b'Jorhat'), (b'KM', b'Kamrup Metropolitan'), (b'KU', b'Kamrup'), (b'KG', b'Karbi Anglong'), (b'KR', b'Karimganj'), (b'KJ', b'Kokrajhar'), (b'LA', b'Lakhimpur'), (b'MJ', b'Majuli'), (b'MA', b'Morigaon'), (b'NN', b'Nagaon'), (b'NB', b'Nalbari'), (b'NC', b'Dima Hasao'), (b'SV', b'Sivasagar'), (b'ST', b'Sonitpur'), (b'SM', b'South Salmara-Mankachar'), (b'TI', b'Tinsukia'), (b'UD', b'Udalguri'), (b'WK', b'West Karbi Anglong')])),
                ('updated_date', models.CharField(max_length=10)),
                ('user_name', models.CharField(default=b'', max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='ManpowerReport',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('person_name', models.CharField(max_length=30)),
                ('designation', models.CharField(max_length=20)),
                ('organization', models.CharField(max_length=40)),
                ('work_location', models.CharField(max_length=60)),
                ('mobile_number', models.CharField(max_length=12)),
                ('email_id', models.EmailField(max_length=254)),
                ('district', models.CharField(blank=True, max_length=30, choices=[(b'BK', b'Baksa'), (b'BP', b'Barpeta'), (b'BS', b'Biswanath'), (b'BO', b'Bongaigaon'), (b'CA', b'Cachar'), (b'CD', b'Charaideo'), (b'CH', b'Chirang'), (b'DR', b'Darrang'), (b'DM', b'Dhemaji'), (b'DU', b'Dhubri'), (b'DI', b'Dibrugarh'), (b'GP', b'Goalpara'), (b'GG', b'Golaghat'), (b'HA', b'Hailakandi'), (b'HJ', b'Hojai'), (b'JO', b'Jorhat'), (b'KM', b'Kamrup Metropolitan'), (b'KU', b'Kamrup'), (b'KG', b'Karbi Anglong'), (b'KR', b'Karimganj'), (b'KJ', b'Kokrajhar'), (b'LA', b'Lakhimpur'), (b'MJ', b'Majuli'), (b'MA', b'Morigaon'), (b'NN', b'Nagaon'), (b'NB', b'Nalbari'), (b'NC', b'Dima Hasao'), (b'SV', b'Sivasagar'), (b'ST', b'Sonitpur'), (b'SM', b'South Salmara-Mankachar'), (b'TI', b'Tinsukia'), (b'UD', b'Udalguri'), (b'WK', b'West Karbi Anglong')])),
                ('updated_date', models.CharField(max_length=10)),
                ('user_name', models.CharField(default=b'', max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='NOFNReport',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('gp_name', models.CharField(max_length=50, null=True, blank=True)),
                ('block_name', models.CharField(max_length=50, null=True, blank=True)),
                ('is_fibre_layered_upto_gp', models.BooleanField(default=False)),
                ('is_gpon_installed_at_block', models.BooleanField(default=True)),
                ('is_gpon_termination_done_at_GP', models.BooleanField(default=True)),
                ('nofn_pop_build_at', models.CharField(max_length=4, choices=[(b'GP', b'GP'), (b'Block', b'Block')])),
                ('is_network_access_available_at_village', models.BooleanField(default=True)),
                ('remarks', models.CharField(max_length=100, null=True, blank=True)),
                ('district', models.CharField(max_length=30, choices=[(b'BK', b'Baksa'), (b'BP', b'Barpeta'), (b'BS', b'Biswanath'), (b'BO', b'Bongaigaon'), (b'CA', b'Cachar'), (b'CD', b'Charaideo'), (b'CH', b'Chirang'), (b'DR', b'Darrang'), (b'DM', b'Dhemaji'), (b'DU', b'Dhubri'), (b'DI', b'Dibrugarh'), (b'GP', b'Goalpara'), (b'GG', b'Golaghat'), (b'HA', b'Hailakandi'), (b'HJ', b'Hojai'), (b'JO', b'Jorhat'), (b'KM', b'Kamrup Metropolitan'), (b'KU', b'Kamrup'), (b'KG', b'Karbi Anglong'), (b'KR', b'Karimganj'), (b'KJ', b'Kokrajhar'), (b'LA', b'Lakhimpur'), (b'MJ', b'Majuli'), (b'MA', b'Morigaon'), (b'NN', b'Nagaon'), (b'NB', b'Nalbari'), (b'NC', b'Dima Hasao'), (b'SV', b'Sivasagar'), (b'ST', b'Sonitpur'), (b'SM', b'South Salmara-Mankachar'), (b'TI', b'Tinsukia'), (b'UD', b'Udalguri'), (b'WK', b'West Karbi Anglong')])),
                ('updated_date', models.CharField(max_length=10)),
                ('user_name', models.CharField(default=b'', max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='SoftwareReport',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('appl_nm', models.CharField(max_length=15, choices=[(b'Dharitree', b'Dharitree'), (b'ePanjeeyan', b'ePanjeeyan'), (b'eSetu', b'eSetu'), (b'CCTNS', b'CCTNS'), (b'Vahan', b'Vahan'), (b'eDistrict', b'eDistrict')])),
                ('appl_owner', models.CharField(max_length=30)),
                ('appl_objective', models.CharField(max_length=100)),
                ('stakeholder_details', models.CharField(max_length=100)),
                ('date_of_commisioning', models.CharField(max_length=12)),
                ('name_of_application_developer', models.CharField(max_length=60)),
                ('appl_platform_details', models.CharField(max_length=60)),
                ('future_roadmap', models.CharField(max_length=100)),
                ('support_requirements', models.CharField(max_length=100)),
                ('district', models.CharField(max_length=30, choices=[(b'BK', b'Baksa'), (b'BP', b'Barpeta'), (b'BS', b'Biswanath'), (b'BO', b'Bongaigaon'), (b'CA', b'Cachar'), (b'CD', b'Charaideo'), (b'CH', b'Chirang'), (b'DR', b'Darrang'), (b'DM', b'Dhemaji'), (b'DU', b'Dhubri'), (b'DI', b'Dibrugarh'), (b'GP', b'Goalpara'), (b'GG', b'Golaghat'), (b'HA', b'Hailakandi'), (b'HJ', b'Hojai'), (b'JO', b'Jorhat'), (b'KM', b'Kamrup Metropolitan'), (b'KU', b'Kamrup'), (b'KG', b'Karbi Anglong'), (b'KR', b'Karimganj'), (b'KJ', b'Kokrajhar'), (b'LA', b'Lakhimpur'), (b'MJ', b'Majuli'), (b'MA', b'Morigaon'), (b'NN', b'Nagaon'), (b'NB', b'Nalbari'), (b'NC', b'Dima Hasao'), (b'SV', b'Sivasagar'), (b'ST', b'Sonitpur'), (b'SM', b'South Salmara-Mankachar'), (b'TI', b'Tinsukia'), (b'UD', b'Udalguri'), (b'WK', b'West Karbi Anglong')])),
                ('updated_date', models.CharField(max_length=10)),
                ('user_name', models.CharField(default=b'', max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='SWANReport',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('pop_names', models.CharField(max_length=50, null=True, blank=True)),
                ('distance_from_hq', models.CharField(max_length=10, null=True, blank=True)),
                ('offices_connected_with_pop', models.CharField(max_length=100, null=True, blank=True)),
                ('distance_from_pop', models.CharField(max_length=100, null=True, blank=True)),
                ('connectivity_types', models.CharField(max_length=4, choices=[(b'UTP', b'UTP'), (b'WiFi', b'WiFi'), (b'OFC', b'Optical Fibre')])),
                ('internet_bandwidth', models.CharField(max_length=50, null=True, blank=True)),
                ('is_functional', models.BooleanField(default=False)),
                ('when_last_up', models.CharField(max_length=15, null=True, blank=True)),
                ('pop_manpower', models.CharField(max_length=50, null=True, blank=True)),
                ('reasons_for_not_working', models.CharField(default=b'NA', max_length=50, null=True, blank=True)),
                ('remarks', models.CharField(max_length=100, null=True, blank=True)),
                ('district', models.CharField(max_length=30, choices=[(b'BK', b'Baksa'), (b'BP', b'Barpeta'), (b'BS', b'Biswanath'), (b'BO', b'Bongaigaon'), (b'CA', b'Cachar'), (b'CD', b'Charaideo'), (b'CH', b'Chirang'), (b'DR', b'Darrang'), (b'DM', b'Dhemaji'), (b'DU', b'Dhubri'), (b'DI', b'Dibrugarh'), (b'GP', b'Goalpara'), (b'GG', b'Golaghat'), (b'HA', b'Hailakandi'), (b'HJ', b'Hojai'), (b'JO', b'Jorhat'), (b'KM', b'Kamrup Metropolitan'), (b'KU', b'Kamrup'), (b'KG', b'Karbi Anglong'), (b'KR', b'Karimganj'), (b'KJ', b'Kokrajhar'), (b'LA', b'Lakhimpur'), (b'MJ', b'Majuli'), (b'MA', b'Morigaon'), (b'NN', b'Nagaon'), (b'NB', b'Nalbari'), (b'NC', b'Dima Hasao'), (b'SV', b'Sivasagar'), (b'ST', b'Sonitpur'), (b'SM', b'South Salmara-Mankachar'), (b'TI', b'Tinsukia'), (b'UD', b'Udalguri'), (b'WK', b'West Karbi Anglong')])),
                ('updated_date', models.CharField(max_length=10)),
                ('user_name', models.CharField(default=b'', max_length=20)),
            ],
        ),
        migrations.AlterUniqueTogether(
            name='swanreport',
            unique_together=set([('pop_names', 'updated_date', 'district')]),
        ),
        migrations.AlterUniqueTogether(
            name='softwarereport',
            unique_together=set([('appl_nm', 'updated_date', 'district')]),
        ),
        migrations.AlterUniqueTogether(
            name='nofnreport',
            unique_together=set([('gp_name', 'updated_date', 'district')]),
        ),
        migrations.AlterUniqueTogether(
            name='manpowerreport',
            unique_together=set([('person_name', 'updated_date', 'district')]),
        ),
        migrations.AlterUniqueTogether(
            name='hardwarereport',
            unique_together=set([('hardware_nm', 'updated_date', 'district')]),
        ),
        migrations.AlterUniqueTogether(
            name='g2cservicereport',
            unique_together=set([('service_nm', 'updated_date', 'district')]),
        ),
        migrations.AlterUniqueTogether(
            name='edistricttransactionreport',
            unique_together=set([('service_nm', 'updated_date', 'district')]),
        ),
        migrations.AlterUniqueTogether(
            name='digitalliteracyreport',
            unique_together=set([('lac_name', 'updated_date', 'district')]),
        ),
        migrations.AlterUniqueTogether(
            name='cscreport',
            unique_together=set([('omt_id', 'updated_date', 'district')]),
        ),
    ]
