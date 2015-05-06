"""
Template helpers for Modal Discharge Summaries 
"""
from django import template

register = template.Library()

@register.inclusion_tag('modal_summary_action.html')
def modalsummary(name):
    return {'name': name}
