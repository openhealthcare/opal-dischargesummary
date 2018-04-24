"""
Template helpers for Modal Discharge Summaries
"""
from django import template

register = template.Library()

from dischargesummary import DischargeTemplate


@register.inclusion_tag('modal_summary_action.html')
def modalsummary(name):
    summary = DischargeTemplate.get(name)
    return {'name': summary.name, 'button_display': summary.button_display}
