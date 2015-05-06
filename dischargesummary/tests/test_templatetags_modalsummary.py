"""
Unittests for dischargesummary.templatetags.modalsummary
"""
from opal.core.test import OpalTestCase

from dischargesummary import DischargeTemplate
from dischargesummary.templatetags import modalsummary

class TestTemplate(DischargeTemplate):
    name = 'templatetagstester'
    button_display = 'test dsiplay'

class ModalsummaryTestCase(OpalTestCase):
    def test_dict(self):
        resp = modalsummary.modalsummary('templatetagstester')
        self.assertEqual({'name': 'templatetagstester', 'button_display': 'test display'}, resp)
