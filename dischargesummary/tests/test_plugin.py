"""
Unittest for plugin
"""
from opal.core.test import OpalTestCase

from dischargesummary import plugin

class PluginTestCase(OpalTestCase):
    def test_javascripts(self):
        j = plugin.DischargesummaryPlugin.javascripts
        self.assertIn(
            'js/dischargesummary/controllers/modal_discharge_summary.js',
            j['opal.controllers']
        )
