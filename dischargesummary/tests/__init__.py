"""
Unittests package
"""
from dischargesummary import DischargeTemplate

class TestDisplayTemplate(DischargeTemplate):
    name = 'templatetagstester'
    button_display = 'test display'

class TestDischargeTemplate(DischargeTemplate):
    name = 'Test template'
