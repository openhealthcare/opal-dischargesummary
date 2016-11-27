"""
Plugin definition for the dischargesummary OPAL plugin
"""
from django.conf import settings
from opal.core import plugins
from opal.utils import stringport, camelcase_to_underscore

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

plugins.register(DischargesummaryPlugin)

# So we only do it once
IMPORTED_FROM_APPS = False

def import_from_apps():
    """
    Iterate through installed apps attempting to import app.dischargesummaries
    This way we allow our implementation, or plugins, to define their
    own discharge summary templates. 
    """
    for app in settings.INSTALLED_APPS:
        try:
            stringport(app + '.dischargesummaries')
        except ImportError:
            pass # not a problem
    global IMPORTED_FROM_APPS
    IMPORTED_FROM_APPS = True
    return

class DischargeTemplate(object):
    """
    Base Discharge Summary Template class - individal summaries should override this.
    """
    name         = 'Please name me Larry!'
    template     = None
    button_display = 'Discharge Summary'

    @classmethod
    def get(klass, name):
        """
        Return a specific referral route by slug
        """
        if not IMPORTED_FROM_APPS:
            import_from_apps()
            
        for sub in klass.__subclasses__():
            if sub.slug() == name:
                return sub

    @classmethod
    def list(klass):
        """
        Return a list of all ward rounds
        """
        if not IMPORTED_FROM_APPS:
            import_from_apps()
        return klass.__subclasses__()

    @classmethod
    def slug(klass):
        return camelcase_to_underscore(klass.name).replace(' ', '')
