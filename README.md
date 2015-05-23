This is dischargesummary - an [OPAL](https://github.com/openhealthcare/opal) plugin.

#### Creating a modal summary: 

    class MySummary(DischargeTemplate):
        name = 'my name'
        template = 'my_template_path.html'
        button_display = 'Discharge Text'

### Rendering the button for a modal summary

    {% load modalsummary %}
    {% modalsummary 'my name' %}
