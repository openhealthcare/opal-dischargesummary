"""
Unittests for dischargesummary.templatetags.modalsummary
"""
from opal.core.test import OpalTestCase

from dischargesummary.templatetags import modalsummary

class ModalsummaryTestCase(OpalTestCase):
    def test_dict(self):
        resp = modalsummary.modalsummary('foo')
        self.assertEqual({'name': 'foo'}, resp)
