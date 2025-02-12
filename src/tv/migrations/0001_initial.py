# -*- coding: utf-8 -*-
# Generated by Django 1.11.28 on 2020-02-22 17:54
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Channel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uid', models.BigIntegerField(unique=True)),
                ('name', models.CharField(max_length=300)),
                ('country_code', models.CharField(choices=[('AFG', 'Afghanistan'), ('ALB', 'Albania'), ('DZA', 'Algeria'), ('ASM', 'American Samoa'), ('AND', 'Andorra'), ('AGO', 'Angola'), ('AIA', 'Anguilla'), ('ATA', 'Antarctica'), ('ATG', 'Antigua and Barbuda'), ('ARG', 'Argentina'), ('ARM', 'Armenia'), ('ABW', 'Aruba'), ('AUS', 'Australia'), ('AUT', 'Austria'), ('AZE', 'Azerbaijan'), ('BHS', 'Bahamas'), ('BHR', 'Bahrain'), ('BGD', 'Bangladesh'), ('BRB', 'Barbados'), ('BLR', 'Belarus'), ('BEL', 'Belgium'), ('BLZ', 'Belize'), ('BEN', 'Benin'), ('BMU', 'Bermuda'), ('BTN', 'Bhutan'), ('BOL', 'Bolivia'), ('BES', 'Bonaire'), ('BIH', 'Bosnia and Herzegovina'), ('BWA', 'Botswana'), ('BVT', 'Bouvet Island'), ('BRA', 'Brazil'), ('IOT', 'British Indian Ocean Territory'), ('BRN', 'Brunei Darussalam'), ('BGR', 'Bulgaria'), ('BFA', 'Burkina Faso'), ('BDI', 'Burundi'), ('KHM', 'Cambodia'), ('CMR', 'Cameroon'), ('CAN', 'Canada'), ('CPV', 'Cape Verde'), ('CYM', 'Cayman Islands'), ('CAF', 'Central African Republic'), ('TCD', 'Chad'), ('CHL', 'Chile'), ('CHN', 'China'), ('CXR', 'Christmas Island'), ('CCK', 'Cocos (Keeling) Islands'), ('COL', 'Colombia'), ('COM', 'Comoros'), ('COG', 'Congo'), ('COD', 'Democratic Republic of the Congo'), ('COK', 'Cook Islands'), ('CRI', 'Costa Rica'), ('HRV', 'Croatia'), ('CUB', 'Cuba'), ('CUW', 'Curacao'), ('CYP', 'Cyprus'), ('CZE', 'Czech Republic'), ('CIV', "Cote d'Ivoire"), ('DNK', 'Denmark'), ('DJI', 'Djibouti'), ('DMA', 'Dominica'), ('DOM', 'Dominican Republic'), ('ECU', 'Ecuador'), ('EGY', 'Egypt'), ('SLV', 'El Salvador'), ('GNQ', 'Equatorial Guinea'), ('ERI', 'Eritrea'), ('EST', 'Estonia'), ('ETH', 'Ethiopia'), ('FLK', 'Falkland Islands (Malvinas)'), ('FRO', 'Faroe Islands'), ('FJI', 'Fiji'), ('FIN', 'Finland'), ('FRA', 'France'), ('GUF', 'French Guiana'), ('PYF', 'French Polynesia'), ('ATF', 'French Southern Territories'), ('GAB', 'Gabon'), ('GMB', 'Gambia'), ('GEO', 'Georgia'), ('DEU', 'Germany'), ('GHA', 'Ghana'), ('GIB', 'Gibraltar'), ('GRC', 'Greece'), ('GRL', 'Greenland'), ('GRD', 'Grenada'), ('GLP', 'Guadeloupe'), ('GUM', 'Guam'), ('GTM', 'Guatemala'), ('GGY', 'Guernsey'), ('GIN', 'Guinea'), ('GNB', 'Guinea-Bissau'), ('GUY', 'Guyana'), ('HTI', 'Haiti'), ('HMD', 'Heard Island and McDonald Islands'), ('VAT', 'Holy See (Vatican City State)'), ('HND', 'Honduras'), ('HKG', 'Hong Kong'), ('HUN', 'Hungary'), ('ISL', 'Iceland'), ('IND', 'India'), ('IDN', 'Indonesia'), ('IRN', 'Iran, Islamic Republic of'), ('IRQ', 'Iraq'), ('IRL', 'Ireland'), ('IMN', 'Isle of Man'), ('ISR', 'Israel'), ('ITA', 'Italy'), ('JAM', 'Jamaica'), ('JPN', 'Japan'), ('JEY', 'Jersey'), ('JOR', 'Jordan'), ('KAZ', 'Kazakhstan'), ('KEN', 'Kenya'), ('KIR', 'Kiribati'), ('PRK', "Korea, Democratic People's Republic of"), ('KOR', 'Korea, Republic of'), ('KWT', 'Kuwait'), ('KGZ', 'Kyrgyzstan'), ('LAO', "Lao People's Democratic Republic"), ('LVA', 'Latvia'), ('LBN', 'Lebanon'), ('LSO', 'Lesotho'), ('LBR', 'Liberia'), ('LBY', 'Libya'), ('LIE', 'Liechtenstein'), ('LTU', 'Lithuania'), ('LUX', 'Luxembourg'), ('MAC', 'Macao'), ('MKD', 'Macedonia, the Former Yugoslav Republic of'), ('MDG', 'Madagascar'), ('MWI', 'Malawi'), ('MYS', 'Malaysia'), ('MDV', 'Maldives'), ('MLI', 'Mali'), ('MLT', 'Malta'), ('MHL', 'Marshall Islands'), ('MTQ', 'Martinique'), ('MRT', 'Mauritania'), ('MUS', 'Mauritius'), ('MYT', 'Mayotte'), ('MEX', 'Mexico'), ('FSM', 'Micronesia, Federated States of'), ('MDA', 'Moldova, Republic of'), ('MCO', 'Monaco'), ('MNG', 'Mongolia'), ('MNE', 'Montenegro'), ('MSR', 'Montserrat'), ('MAR', 'Morocco'), ('MOZ', 'Mozambique'), ('MMR', 'Myanmar'), ('NAM', 'Namibia'), ('NRU', 'Nauru'), ('NPL', 'Nepal'), ('NLD', 'Netherlands'), ('NCL', 'New Caledonia'), ('NZL', 'New Zealand'), ('NIC', 'Nicaragua'), ('NER', 'Niger'), ('NGA', 'Nigeria'), ('NIU', 'Niue'), ('NFK', 'Norfolk Island'), ('MNP', 'Northern Mariana Islands'), ('NOR', 'Norway'), ('OMN', 'Oman'), ('PAK', 'Pakistan'), ('PLW', 'Palau'), ('PSE', 'Palestine, State of'), ('PAN', 'Panama'), ('PNG', 'Papua New Guinea'), ('PRY', 'Paraguay'), ('PER', 'Peru'), ('PHL', 'Philippines'), ('PCN', 'Pitcairn'), ('POL', 'Poland'), ('PRT', 'Portugal'), ('PRI', 'Puerto Rico'), ('QAT', 'Qatar'), ('ROU', 'Romania'), ('RUS', 'Russian Federation'), ('RWA', 'Rwanda'), ('REU', 'Reunion'), ('BLM', 'Saint Barthelemy'), ('SHN', 'Saint Helena'), ('KNA', 'Saint Kitts and Nevis'), ('LCA', 'Saint Lucia'), ('MAF', 'Saint Martin (French part)'), ('SPM', 'Saint Pierre and Miquelon'), ('VCT', 'Saint Vincent and the Grenadines'), ('WSM', 'Samoa'), ('SMR', 'San Marino'), ('STP', 'Sao Tome and Principe'), ('SAU', 'Saudi Arabia'), ('SEN', 'Senegal'), ('SRB', 'Serbia'), ('SYC', 'Seychelles'), ('SLE', 'Sierra Leone'), ('SGP', 'Singapore'), ('SXM', 'Sint Maarten (Dutch part)'), ('SVK', 'Slovakia'), ('SVN', 'Slovenia'), ('SLB', 'Solomon Islands'), ('SOM', 'Somalia'), ('ZAF', 'South Africa'), ('SGS', 'South Georgia and the South Sandwich Islands'), ('SSD', 'South Sudan'), ('ESP', 'Spain'), ('LKA', 'Sri Lanka'), ('SDN', 'Sudan'), ('SUR', 'Suriname'), ('SJM', 'Svalbard and Jan Mayen'), ('SWZ', 'Swaziland'), ('SWE', 'Sweden'), ('CHE', 'Switzerland'), ('SYR', 'Syrian Arab Republic'), ('TWN', 'Taiwan'), ('TJK', 'Tajikistan'), ('TZA', 'United Republic of Tanzania'), ('THA', 'Thailand'), ('TLS', 'Timor-Leste'), ('TGO', 'Togo'), ('TKL', 'Tokelau'), ('TON', 'Tonga'), ('TTO', 'Trinidad and Tobago'), ('TUN', 'Tunisia'), ('TUR', 'Turkey'), ('TKM', 'Turkmenistan'), ('TCA', 'Turks and Caicos Islands'), ('TUV', 'Tuvalu'), ('UGA', 'Uganda'), ('UKR', 'Ukraine'), ('ARE', 'United Arab Emirates'), ('GBR', 'United Kingdom'), ('USA', 'United States'), ('UMI', 'United States Minor Outlying Islands'), ('URY', 'Uruguay'), ('UZB', 'Uzbekistan'), ('VUT', 'Vanuatu'), ('VEN', 'Venezuela'), ('VNM', 'Viet Nam'), ('VGB', 'British Virgin Islands'), ('VIR', 'US Virgin Islands'), ('WLF', 'Wallis and Futuna'), ('ESH', 'Western Sahara'), ('YEM', 'Yemen'), ('ZMB', 'Zambia'), ('ZWE', 'Zimbabwe'), ('N/A', 'Unknown')], default='N/A', max_length=3, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Program',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uid', models.BigIntegerField(unique=True)),
                ('original_title', models.CharField(blank=True, default='', max_length=300, null=True)),
                ('local_title', models.CharField(default='', max_length=300)),
                ('year', models.CharField(blank=True, default=None, max_length=4, null=True)),
                ('channel', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='programs', to='tv.Channel')),
            ],
        ),
        migrations.CreateModel(
            name='Showtime',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_time', models.DateTimeField(default=None, null=True)),
                ('end_time', models.DateTimeField(default=None, null=True)),
                ('program', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='showtimes', to='tv.Program')),
            ],
        ),
        migrations.AlterUniqueTogether(
            name='showtime',
            unique_together=set([('program', 'start_time', 'end_time')]),
        ),
    ]
