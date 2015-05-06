"""
Plugin definition for the dischargesummary OPAL plugin
"""
from django.conf import settings
from opal.core.plugins import OpalPlugin
from opal.utils import stringport, camelcase_to_underscore

from dischargesummary.urls import urlpatterns

class DischargesummaryPlugin(OpalPlugin):
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

    def restricted_teams(self, user):
        """
        Return any restricted teams for particualr users that our
        plugin may define.
        """
        return []

    def list_schemas(self):
        """
        Return any patient list schemas that our plugin may define.
        """
        return {}

    def flows(self):
        """
        Return any custom flows that our plugin may define
        """
        return {}

    def roles(self, user):
        """
        Given a (Django) USER object, return any extra roles defined
        by our plugin.
        """
        return {}


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
