"""
Plugin definition for the dischargesummary OPAL plugin
"""
from opal.core import plugins

from dischargesummary.urls import urlpatterns

class DischargesummaryPlugin(plugins.OpalPlugin):
    """
    Main entrypoint to expose this plugin to our OPAL application.
    """
    urls = urlpatterns
    javascripts = {
        # Add your javascripts here!
        'opal.controllers': [
            # 'js/dischargesummary/app.js',
            'js/dischargesummary/controllers/modal_discharge_summary.js',
            # 'js/dischargesummary/services/larry.js',
        ]
    }
