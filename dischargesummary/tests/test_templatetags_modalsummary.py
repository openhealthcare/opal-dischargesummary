"""
Unittests for dischargesummary.templatetags.modalsummary
"""
from opal.core.test import OpalTestCase

from dischargesummary.templatetags import modalsummary

class ModalsummaryTestCase(OpalTestCase):
    def test_dict(self):
        resp = modalsummary.modalsummary('templatetagstester')
        self.assertEqual({'name': 'templatetagstester', 'button_display': 'test display'}, resp)
