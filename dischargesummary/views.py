"""
Views for the dischargesummary OPAL Plugin
"""
from django.views.generic import TemplateView

class DischargeTemplateView(TemplateView):
    template_name = 'dischargesummary/modal_summary.html'
    
    def dispatch(self, *args, **kwargs):
        self.name = kwargs['name']
        return super(DischargeTemplateView, self).dispatch(*args, **kwargs)

    def get_context_data(self, **kwargs):
        from dischargesummary import DischargeTemplate

        ctx = super(DischargeTemplateView, self).get_context_data(**kwargs)
        summary = DischargeTemplate.get(self.name)
        ctx['content'] = summary.template
        ctx['heading'] = summary.button_display
        return ctx
