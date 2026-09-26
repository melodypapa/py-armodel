"""Reader tests for FMConditionByFeaturesAndSwSystemconsts.

Spec: R23-11 AUTOSAR_FO_TPS_FeatureModelExchangeFormat, Table 7.4, p.63.
XSD 00052: complexType FM-CONDITION-BY-FEATURES-AND-SW-SYSTEMCONSTS (line
62046, mixed, abstract="false") composes AR-OBJECT + FORMULA-EXPRESSION +
SW-SYSTEMCONST-DEPENDENT-FORMULA + FM-FORMULA-BY-FEATURES-AND-SW-SYSTEMCONSTS
+ the own empty group (line 62037). No live dispatcher exists (the Aggregated-
by consumer FMFeatureMapAssertion is not yet modeled), so coverage is the
class's own helper pair pinned at element level (BlueprintFormula /
FMConditionByFeaturesAndAttributes precedent). The wire key for the class
element is FM-SYSCOND (consumer FMFeatureMapAssertion.fmSyscond, XSD L62276).
"""

import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.FeatureModelTemplate import FMConditionByFeaturesAndSwSystemconsts
from armodel.parser.arxml_parser import ARXMLParser

NS = "http://autosar.org/schema/r4.0"


class TestReadFMConditionByFeaturesAndSwSystemconsts:
    def test_read_full(self):
        xml = (
            "<FM-SYSCOND xmlns='%s'>feature_a == SYSC(sysc_b)"
            "<FEATURE-REF DEST='FM-FEATURE'>/FMFeatureModels/Model/FeatureA</FEATURE-REF>"
            "<SYSC-REF DEST='SW-SYSTEMCONST'>/SystemConstants/SyscB</SYSC-REF>"
            "<SYSC-STRING-REF DEST='SW-SYSTEMCONST'>/SystemConstants/SyscB</SYSC-STRING-REF>"
            "</FM-SYSCOND>" % NS
        )
        element = ET.fromstring(xml)

        formula = ARXMLParser().readFMConditionByFeaturesAndSwSystemconsts(element, FMConditionByFeaturesAndSwSystemconsts())

        assert formula.getMixedString() == "feature_a == SYSC(sysc_b)"
        assert formula.getFeatureRef().getValue() == "/FMFeatureModels/Model/FeatureA"
        assert formula.getFeatureRef().getDest() == "FM-FEATURE"
        assert formula.getSyscRef().getValue() == "/SystemConstants/SyscB"
        assert formula.getSyscStringRef().getValue() == "/SystemConstants/SyscB"

    def test_read_empty_element(self):
        xml = "<FM-SYSCOND xmlns='%s'></FM-SYSCOND>" % NS
        element = ET.fromstring(xml)

        formula = ARXMLParser().readFMConditionByFeaturesAndSwSystemconsts(element, FMConditionByFeaturesAndSwSystemconsts())

        assert formula.getMixedString() is None
        assert formula.getFeatureRef() is None
        assert formula.getSyscRef() is None
        assert formula.getSyscStringRef() is None
