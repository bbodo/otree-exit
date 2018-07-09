import os
from os import environ

import dj_database_url
from boto.mturk import qualification

import otree.settings


BASE_DIR = os.path.dirname(os.path.abspath(__file__))
SITE_ROOT = os.path.abspath(os.path.dirname(__file__))

# the environment variable OTREE_PRODUCTION controls whether Django runs in
# DEBUG mode. If OTREE_PRODUCTION==1, then DEBUG=False
if environ.get('OTREE_PRODUCTION') not in {None, '', '0'}:
    DEBUG = False
else:
    DEBUG = True

ADMIN_USERNAME = 'admin'

# for security, best to set admin password in an environment variable
# ADMIN_PASSWORD = environ.get('OTREE_ADMIN_PASSWORD')
ADMIN_PASSWORD = 'blub'

# don't share this with anybody.
SECRET_KEY = 'klvw%!6@b+f1*39izl!amea_!vf-ax06hv73$k0=3-5ggz9*9-'

# To use a database other than sqlite,
# set the DATABASE_URL environment variable.
# Examples:
# postgres://USER:PASSWORD@HOST:PORT/NAME
# mysql://USER:PASSWORD@HOST:PORT/NAME

DATABASES = {
    'default': dj_database_url.config(
        default='sqlite:///' + os.path.join(BASE_DIR, 'db.sqlite3')
    )
}

# AUTH_LEVEL:
# If you are launching a study and want visitors to only be able to
# play your app if you provided them with a start link, set the
# environment variable OTREE_AUTH_LEVEL to STUDY.
# If you would like to put your site online in public demo mode where
# anybody can play a demo version of your game, set OTREE_AUTH_LEVEL
# to DEMO. This will allow people to play in demo mode, but not access
# the full admin interface.

# AUTH_LEVEL = environ.get('OTREE_AUTH_LEVEL')
AUTH_LEVEL = "STUDY"

# setting for integration with AWS Mturk
AWS_ACCESS_KEY_ID = environ.get('AWS_ACCESS_KEY_ID')
AWS_SECRET_ACCESS_KEY = environ.get('AWS_SECRET_ACCESS_KEY')


# e.g. EUR, CAD, GBP, CHF, CNY, JPY
REAL_WORLD_CURRENCY_CODE = 'USD'
USE_POINTS = True


# e.g. en, de, fr, it, ja, zh-hans
# see: https://docs.djangoproject.com/en/1.9/topics/i18n/#term-language-code
LANGUAGE_CODE = 'en'

# if an app is included in SESSION_CONFIGS, you don't need to list it here
INSTALLED_APPS = ['otree']

# SENTRY_DSN = ''

DEMO_PAGE_INTRO_TEXT = """
oTree games
"""

# from here on are qualifications requirements for workers
# see description for requirements on Amazon Mechanical Turk website:
# http://docs.aws.amazon.com/AWSMechTurk/latest/AWSMturkAPI/ApiReference_QualificationRequirementDataStructureArticle.html
# and also in docs for boto:
# https://boto.readthedocs.org/en/latest/ref/mturk.html?highlight=mturk#module-boto.mturk.qualification

mturk_hit_settings = {
    'keywords': ['easy', 'bonus', 'choice', 'study'],
    'title': 'Title for your experiment',
    'description': 'Description for your experiment',
    'frame_height': 500,
    'preview_template': 'global/MTurkPreview.html',
    'minutes_allotted_per_assignment': 60,
    'expiration_hours': 7*24,  # 7 days
    # 'grant_qualification_id': 'YOUR_QUALIFICATION_ID_HERE',# to prevent retakes
    'qualification_requirements': [
        # qualification.LocaleRequirement("EqualTo", "US"),
        # qualification.PercentAssignmentsApprovedRequirement("GreaterThanOrEqualTo", 50),
        # qualification.NumberHitsApprovedRequirement("GreaterThanOrEqualTo", 5),
        # qualification.Requirement('YOUR_QUALIFICATION_ID_HERE', 'DoesNotExist')
    ]
}

# if you set a property in SESSION_CONFIG_DEFAULTS, it will be inherited by all configs
# in SESSION_CONFIGS, except those that explicitly override it.
# the session config can be accessed from methods in your apps as self.session.config,
# e.g. self.session.config['participation_fee']

SESSION_CONFIG_DEFAULTS = {
    'real_world_currency_per_point': 0.000,
    'participation_fee': 0.00,
    'doc': "",
    'mturk_hit_settings': mturk_hit_settings,
}

ROOM_DEFAULTS = {}

ROOMS = [
    {
        'name': 'test',
        'display_name': 'test',
        'participant_label_file': 'test.txt',
    },
    {
        'name': 'econ_lab',
        'display_name': 'Experimental Economics Lab',
    },
]




SESSION_CONFIGS = [
    # {
    #     'name': '...',
    #     'display_name': '...',
    #     'num_demo_participants': ...,
    #     'app_sequence': ['...'],
    # }
    {
        'name': 'consent',
        'display_name': 'Consent',
        'num_demo_participants': 1,
        'app_sequence': ['consent_mturk'],
    },
    {
        'name': 'exit_codes',
        'display_name': "MTurk Exit Codes",
        'num_demo_participants': 1,
        'app_sequence': ['exit_codes'],
    },
    {
        'name': 'public_goods',
        'display_name': "Public Goods",
        'num_demo_participants': 3,
        'app_sequence': ['public_goods'],
    },
    {
        'name': 'public_goods_exit',
        'display_name': "Public Goods with MTurk Exit Codes",
        'num_demo_participants': 3,
        'app_sequence': ['public_goods', 'exit_codes'],
    },
    {
        'name': 'descilult',
        'display_name': "Ultimatum with Exit",
        'num_demo_participants': 2,
        'app_sequence': ['ultimatum_mturk', 'exit_codes'],
    },
    {
        'name': 'descilultchap',
        'display_name': "Ultimatum, Exit, using Chapkovkis Custom Mturk pages",
        'num_demo_participants': 4,
        'app_sequence': ['consent_mturk', 'mturk_grouping', 'ultimatum_mturk_chap', 'exit_codes'],
        'group_size': 2,
        'wait_time': 30,
        'use_strategy_method': False,
        'doc': """
        To set group size and wait time, you need to change these values in their 
        respective places in each relevant app.
        ########################################################################
        """
    },
    {
        'name': 'mturk_grouping',
        'display_name': "mturk_grouping",
        'num_demo_participants': 4,
        'app_sequence': ['mturk_grouping'],
        'group_size': 2,
        'wait_time': 30,
    },
    {
        'name': 'ultimatum',
        'display_name': "Ultimatum",
        'num_demo_participants': 2,
        'app_sequence': ['ultimatum',],
    },
]

CHANNEL_ROUTING = 'routing.channel_routing'

EXTENSION_APPS = [
    'otree_mturk_utils',
]


# anything you put after the below line will override
# oTree's default settings. Use with caution.
otree.settings.augment_settings(globals())
