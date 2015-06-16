"""
Standalone test runner for dischargesummary plugin
"""
import os
import sys
from opal.core import application

class Application(application.OpalApplication):
    pass

from django.conf import settings

settings.configure(DEBUG=True,
                   DATABASES={
                       'default': {
                           'ENGINE': 'django.db.backends.sqlite3',
                       }
                   },
                   OPAL_OPTIONS_MODULE = 'dischargesummary.tests.dummy_options_module',
                   ROOT_URLCONF='dischargesummary.urls',
                   STATIC_URL='/assets/',
                   INSTALLED_APPS=('django.contrib.auth',
                                   'django.contrib.contenttypes',
                                   'django.contrib.sessions',
                                   'django.contrib.staticfiles',
                                   'django.contrib.admin',
                                   'opal',
                                   'dischargesummary',))

import django
django.setup()

from django.test.runner import DiscoverRunner
test_runner = DiscoverRunner(verbosity=1)
if len(sys.argv) == 2:
    failures = test_runner.run_tests([sys.argv[-1], ])
else:
    failures = test_runner.run_tests(['dischargesummary', ])
if failures:
    sys.exit(failures)
