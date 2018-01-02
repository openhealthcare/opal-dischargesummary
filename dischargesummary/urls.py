"""
Urls for the dischargesummary Opal plugin
"""
from django.conf.urls import url

from dischargesummary import views

urlpatterns = [
    url(r'^dischargesummary/modals/(?P<name>\w+)/?$',
        views.DischargeTemplateView.as_view()),
]
