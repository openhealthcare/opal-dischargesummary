"""
Unittests for dischargesummary.views
"""
from mock import patch
from opal.core.test import OpalTestCase

from dischargesummary import views

class DischargeTemplateViewTestCase(OpalTestCase):

    def setUp(self):
        self.v = views.DischargeTemplateView()
        self.request = self.rf.get('/template.html')
        self.v.request = self.request
        super(DischargeTemplateViewTestCase, self).setUp()

    def test_dispatch(self):
        with patch('dischargesummary.DischargeTemplate'):
            self.v.dispatch(self.request, name='thename')
            self.assertEqual('thename', self.v.name)
