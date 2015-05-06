"""
Unittests for dischargesummary
"""
from opal.core.test import OpalTestCase

import dischargesummary

class TestDischargeTemplate(dischargesummary.DischargeTemplate):
    name = 'Test template'

class DischargeTemplateTestCase(OpalTestCase):
    def test_get(self):
        tpl = dischargesummary.DischargeTemplate.get('testtemplate')
        self.assertEqual(TestDischargeTemplate, tpl)

    def test_slug(self):
        self.assertEqual('testtemplate', TestDischargeTemplate.slug())

    def test_list(self):
        self.assertEqual([TestDischargeTemplate], dischargesummary.DischargeTemplate.list())

