"""
Unittests for dischargesummary
"""
from opal.core.test import OpalTestCase

import dischargesummary
from dischargesummary.tests import TestDischargeTemplate, TestDisplayTemplate

class DischargeTemplateTestCase(OpalTestCase):
    def test_get(self):
        tpl = dischargesummary.DischargeTemplate.get('testtemplate')
        self.assertEqual(TestDischargeTemplate, tpl)

    def test_slug(self):
        self.assertEqual('testtemplate', TestDischargeTemplate.slug())

    def test_list(self):
        expected = [TestDisplayTemplate, TestDischargeTemplate]
        self.assertEqual(expected, dischargesummary.DischargeTemplate.list())

