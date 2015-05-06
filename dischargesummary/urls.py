"""
Urls for the dischargesummary OPAL plugin
"""
from django.conf.urls import patterns, url

from dischargesummary import views

urlpatterns = patterns(
    '',
    url(r'^dischargesummary/modals/(?P<name>\w+)/?$',
        views.DischargeTemplateView.as_view()),
)
