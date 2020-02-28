# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.utils.encoding import python_2_unicode_compatible


# Channel_country
"""The UN also uses 3-letter codes, and numerical codes to identify nations, and those are shown below."""
COUNTRY_CHOICES = [
    ('AFG', 'Afghanistan'),
    ('ALB', 'Albania'),
    ('DZA', 'Algeria'),
    ('ASM', 'American Samoa'),
    ('AND', 'Andorra'),
    ('AGO', 'Angola'),
    ('AIA', 'Anguilla'),
    ('ATA', 'Antarctica'),
    ('ATG', 'Antigua and Barbuda'),
    ('ARG', 'Argentina'),
    ('ARM', 'Armenia'),
    ('ABW', 'Aruba'),
    ('AUS', 'Australia'),
    ('AUT', 'Austria'),
    ('AZE', 'Azerbaijan'),
    ('BHS', 'Bahamas'),
    ('BHR', 'Bahrain'),
    ('BGD', 'Bangladesh'),
    ('BRB', 'Barbados'),
    ('BLR', 'Belarus'),
    ('BEL', 'Belgium'),
    ('BLZ', 'Belize'),
    ('BEN', 'Benin'),
    ('BMU', 'Bermuda'),
    ('BTN', 'Bhutan'),
    ('BOL', 'Bolivia'),
    ('BES', 'Bonaire'),
    ('BIH', 'Bosnia and Herzegovina'),
    ('BWA', 'Botswana'),
    ('BVT', 'Bouvet Island'),
    ('BRA', 'Brazil'),
    ('IOT', 'British Indian Ocean Territory'),
    ('BRN', 'Brunei Darussalam'),
    ('BGR', 'Bulgaria'),
    ('BFA', 'Burkina Faso'),
    ('BDI', 'Burundi'),
    ('KHM', 'Cambodia'),
    ('CMR', 'Cameroon'),
    ('CAN', 'Canada'),
    ('CPV', 'Cape Verde'),
    ('CYM', 'Cayman Islands'),
    ('CAF', 'Central African Republic'),
    ('TCD', 'Chad'),
    ('CHL', 'Chile'),
    ('CHN', 'China'),
    ('CXR', 'Christmas Island'),
    ('CCK', 'Cocos (Keeling) Islands'),
    ('COL', 'Colombia'),
    ('COM', 'Comoros'),
    ('COG', 'Congo'),
    ('COD', 'Democratic Republic of the Congo'),
    ('COK', 'Cook Islands'),
    ('CRI', 'Costa Rica'),
    ('HRV', 'Croatia'),
    ('CUB', 'Cuba'),
    ('CUW', 'Curacao'),
    ('CYP', 'Cyprus'),
    ('CZE', 'Czech Republic'),
    ('CIV', 'Cote d\'Ivoire'),
    ('DNK', 'Denmark'),
    ('DJI', 'Djibouti'),
    ('DMA', 'Dominica'),
    ('DOM', 'Dominican Republic'),
    ('ECU', 'Ecuador'),
    ('EGY', 'Egypt'),
    ('SLV', 'El Salvador'),
    ('GNQ', 'Equatorial Guinea'),
    ('ERI', 'Eritrea'),
    ('EST', 'Estonia'),
    ('ETH', 'Ethiopia'),
    ('FLK', 'Falkland Islands (Malvinas)'),
    ('FRO', 'Faroe Islands'),
    ('FJI', 'Fiji'),
    ('FIN', 'Finland'),
    ('FRA', 'France'),
    ('GUF', 'French Guiana'),
    ('PYF', 'French Polynesia'),
    ('ATF', 'French Southern Territories'),
    ('GAB', 'Gabon'),
    ('GMB', 'Gambia'),
    ('GEO', 'Georgia'),
    ('DEU', 'Germany'),
    ('GHA', 'Ghana'),
    ('GIB', 'Gibraltar'),
    ('GRC', 'Greece'),
    ('GRL', 'Greenland'),
    ('GRD', 'Grenada'),
    ('GLP', 'Guadeloupe'),
    ('GUM', 'Guam'),
    ('GTM', 'Guatemala'),
    ('GGY', 'Guernsey'),
    ('GIN', 'Guinea'),
    ('GNB', 'Guinea-Bissau'),
    ('GUY', 'Guyana'),
    ('HTI', 'Haiti'),
    ('HMD', 'Heard Island and McDonald Islands'),
    ('VAT', 'Holy See (Vatican City State)'),
    ('HND', 'Honduras'),
    ('HKG', 'Hong Kong'),
    ('HUN', 'Hungary'),
    ('ISL', 'Iceland'),
    ('IND', 'India'),
    ('IDN', 'Indonesia'),
    ('IRN', 'Iran, Islamic Republic of'),
    ('IRQ', 'Iraq'),
    ('IRL', 'Ireland'),
    ('IMN', 'Isle of Man'),
    ('ISR', 'Israel'),
    ('ITA', 'Italy'),
    ('JAM', 'Jamaica'),
    ('JPN', 'Japan'),
    ('JEY', 'Jersey'),
    ('JOR', 'Jordan'),
    ('KAZ', 'Kazakhstan'),
    ('KEN', 'Kenya'),
    ('KIR', 'Kiribati'),
    ('PRK', 'Korea, Democratic People\'s Republic of'),
    ('KOR', 'Korea, Republic of'),
    ('KWT', 'Kuwait'),
    ('KGZ', 'Kyrgyzstan'),
    ('LAO', 'Lao People\'s Democratic Republic'),
    ('LVA', 'Latvia'),
    ('LBN', 'Lebanon'),
    ('LSO', 'Lesotho'),
    ('LBR', 'Liberia'),
    ('LBY', 'Libya'),
    ('LIE', 'Liechtenstein'),
    ('LTU', 'Lithuania'),
    ('LUX', 'Luxembourg'),
    ('MAC', 'Macao'),
    ('MKD', 'Macedonia, the Former Yugoslav Republic of'),
    ('MDG', 'Madagascar'),
    ('MWI', 'Malawi'),
    ('MYS', 'Malaysia'),
    ('MDV', 'Maldives'),
    ('MLI', 'Mali'),
    ('MLT', 'Malta'),
    ('MHL', 'Marshall Islands'),
    ('MTQ', 'Martinique'),
    ('MRT', 'Mauritania'),
    ('MUS', 'Mauritius'),
    ('MYT', 'Mayotte'),
    ('MEX', 'Mexico'),
    ('FSM', 'Micronesia, Federated States of'),
    ('MDA', 'Moldova, Republic of'),
    ('MCO', 'Monaco'),
    ('MNG', 'Mongolia'),
    ('MNE', 'Montenegro'),
    ('MSR', 'Montserrat'),
    ('MAR', 'Morocco'),
    ('MOZ', 'Mozambique'),
    ('MMR', 'Myanmar'),
    ('NAM', 'Namibia'),
    ('NRU', 'Nauru'),
    ('NPL', 'Nepal'),
    ('NLD', 'Netherlands'),
    ('NCL', 'New Caledonia'),
    ('NZL', 'New Zealand'),
    ('NIC', 'Nicaragua'),
    ('NER', 'Niger'),
    ('NGA', 'Nigeria'),
    ('NIU', 'Niue'),
    ('NFK', 'Norfolk Island'),
    ('MNP', 'Northern Mariana Islands'),
    ('NOR', 'Norway'),
    ('OMN', 'Oman'),
    ('PAK', 'Pakistan'),
    ('PLW', 'Palau'),
    ('PSE', 'Palestine, State of'),
    ('PAN', 'Panama'),
    ('PNG', 'Papua New Guinea'),
    ('PRY', 'Paraguay'),
    ('PER', 'Peru'),
    ('PHL', 'Philippines'),
    ('PCN', 'Pitcairn'),
    ('POL', 'Poland'),
    ('PRT', 'Portugal'),
    ('PRI', 'Puerto Rico'),
    ('QAT', 'Qatar'),
    ('ROU', 'Romania'),
    ('RUS', 'Russian Federation'),
    ('RWA', 'Rwanda'),
    ('REU', 'Reunion'),
    ('BLM', 'Saint Barthelemy'),
    ('SHN', 'Saint Helena'),
    ('KNA', 'Saint Kitts and Nevis'),
    ('LCA', 'Saint Lucia'),
    ('MAF', 'Saint Martin (French part)'),
    ('SPM', 'Saint Pierre and Miquelon'),
    ('VCT', 'Saint Vincent and the Grenadines'),
    ('WSM', 'Samoa'),
    ('SMR', 'San Marino'),
    ('STP', 'Sao Tome and Principe'),
    ('SAU', 'Saudi Arabia'),
    ('SEN', 'Senegal'),
    ('SRB', 'Serbia'),
    ('SYC', 'Seychelles'),
    ('SLE', 'Sierra Leone'),
    ('SGP', 'Singapore'),
    ('SXM', 'Sint Maarten (Dutch part)'),
    ('SVK', 'Slovakia'),
    ('SVN', 'Slovenia'),
    ('SLB', 'Solomon Islands'),
    ('SOM', 'Somalia'),
    ('ZAF', 'South Africa'),
    ('SGS', 'South Georgia and the South Sandwich Islands'),
    ('SSD', 'South Sudan'),
    ('ESP', 'Spain'),
    ('LKA', 'Sri Lanka'),
    ('SDN', 'Sudan'),
    ('SUR', 'Suriname'),
    ('SJM', 'Svalbard and Jan Mayen'),
    ('SWZ', 'Swaziland'),
    ('SWE', 'Sweden'),
    ('CHE', 'Switzerland'),
    ('SYR', 'Syrian Arab Republic'),
    ('TWN', 'Taiwan'),
    ('TJK', 'Tajikistan'),
    ('TZA', 'United Republic of Tanzania'),
    ('THA', 'Thailand'),
    ('TLS', 'Timor-Leste'),
    ('TGO', 'Togo'),
    ('TKL', 'Tokelau'),
    ('TON', 'Tonga'),
    ('TTO', 'Trinidad and Tobago'),
    ('TUN', 'Tunisia'),
    ('TUR', 'Turkey'),
    ('TKM', 'Turkmenistan'),
    ('TCA', 'Turks and Caicos Islands'),
    ('TUV', 'Tuvalu'),
    ('UGA', 'Uganda'),
    ('UKR', 'Ukraine'),
    ('ARE', 'United Arab Emirates'),
    ('GBR', 'United Kingdom'),
    ('USA', 'United States'),
    ('UMI', 'United States Minor Outlying Islands'),
    ('URY', 'Uruguay'),
    ('UZB', 'Uzbekistan'),
    ('VUT', 'Vanuatu'),
    ('VEN', 'Venezuela'),
    ('VNM', 'Viet Nam'),
    ('VGB', 'British Virgin Islands'),
    ('VIR', 'US Virgin Islands'),
    ('WLF', 'Wallis and Futuna'),
    ('ESH', 'Western Sahara'),
    ('YEM', 'Yemen'),
    ('ZMB', 'Zambia'),
    ('ZWE', 'Zimbabwe'),
    ('N/A', 'Unknown')
]


@python_2_unicode_compatible
class Channel(models.Model):
    # Channel_id
    uid = models.BigIntegerField(unique=True)

    # Channel_name
    name = models.CharField(max_length=300)

    country_code = models.CharField(max_length=3, choices=COUNTRY_CHOICES, default='N/A', null=True)

    def __str__(self):
        return 'Channel: ' + self.name


@python_2_unicode_compatible
class Program(models.Model):
    # Program_id
    # Must exist only once in db
    uid = models.BigIntegerField(unique=True)

    # Program_original_title 
    # Can be blank, default blank
    original_title = models.CharField(max_length=300, blank=True, default='', null=True)

    # Program_local_title: 
    # Is required
    local_title = models.CharField(max_length=300, default='')

    # Program_year: 
    # Can be null blank or human readable 'n/a', max 4 digits
    year = models.CharField(blank=True, null=True, max_length=4, default=None)

    # Channel:
    # The channel where it is played
    channel = models.ForeignKey('Channel', related_name='programs', on_delete=models.CASCADE, null=True)

    def __str__(self):
        return 'Program: ' + self.local_title + 'with id ' + self.uid

    def __repr__(self):
        return "<{} {}: {}>".format(self.__class__.__name__, self.pk, self)


@python_2_unicode_compatible
class Showtime(models.Model):
    # Program
    # Programs have unique ids
    program = models.ForeignKey('Program', related_name='showtimes', on_delete=models.CASCADE, null=True)

    # Start Datetime 
    # Should be able to store at min 'YYYYmmdd - HH:mm:ss'
    start_time = models.DateTimeField(default=None, null=True)

    # End Datetime 
    # Should be able to store at min 'YYYYmmdd - HH:mm:ss'
    end_time = models.DateTimeField(default=None, null=True)

    class Meta:
        unique_together = ('program', 'start_time', 'end_time')

    def __str__(self):
        return 'Showtime on ' + str(self.start_time) + ' on ' + self.program

    def __repr__(self):
        return "<{} {}: {}>".format(self.__class__.__name__, self.pk, self)

