This is dischargesummary - an [OPAL](https://github.com/openhealthcare/opal) plugin.


## ! Important Notice !

This plugin is no longer actively maintiained - as it depends on a version of django that is no longer supported by OPAL


[![Build
Status](https://travis-ci.org/openhealthcare/opal-dischargesummary.png?branch=v0.5.0)](https://travis-ci.org/openhealthcare/opal-dischargesummary)

#### Creating a modal summary: 

    class MySummary(DischargeTemplate):
        name = 'my name'
        template = 'my_template_path.html'
        button_display = 'Discharge Text'

### Rendering the button for a modal summary

    {% load modalsummary %}
    {% modalsummary 'my name' %}
