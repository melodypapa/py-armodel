"""Writer tests for FMConditionByFeaturesAndSwSystemconsts.

Spec: R23-11 AUTOSAR_FO_TPS_FeatureModelExchangeFormat, Table 7.4, p.63.
XSD 00052: complexType FM-CONDITION-BY-FEATURES-AND-SW-SYSTEMCONSTS (line
62046, mixed, abstract="false") composes AR-OBJECT + FORMULA-EXPRESSION +
SW-SYSTEMCONST-DEPENDENT-FORMULA + FM-FORMULA-BY-FEATURES-AND-SW-SYSTEMCONSTS
+ the own empty group (line 62037). No live dispatcher exists (the Aggregated-
by consumer FMFeatureMapAssertion is not yet modeled), so coverage is the
class's own helper pair pinned at element level. The wire key for the class
element is FM-SYSCOND (consumer FMFeatureMapAssertion.fmSyscond, XSD L62276).
"""

import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.FeatureModelTemplate import FMConditionByFeaturesAndSwSystemconsts
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import RefType
from armodel.parser.arxml_parser import ARXMLParser
from armodel.writer.arxml_writer import ARXMLWriter

NS = "http://autosar.org/schema/r4.0"


class TestWriteFMConditionByFeaturesAndSwSystemconsts:
    def test_write_full(self):
        formula = FMConditionByFeaturesAndSwSystemconsts()
        formula.setMixedString("feature_a == SYSC(sysc_b)")
        feature_ref = RefType()
        feature_ref.setDest("FM-FEATURE")
        feature_ref.setValue("/FMFeatureModels/Model/FeatureA")
        formula.setFeatureRef(feature_ref)
        sysc_ref = RefType()
        sysc_ref.setDest("SW-SYSTEMCONST")
        sysc_ref.setValue("/SystemConstants/SyscB")
        formula.setSyscRef(sysc_ref)

        element = ET.Element("PARENT")
        ARXMLWriter().writeFMConditionByFeaturesAndSwSystemconsts(element, formula)

        written = element.find("FM-SYSCOND")
        assert written is not None
        assert written.text == "feature_a == SYSC(sysc_b)"
        feature_element = written.find("FEATURE-REF")
        assert feature_element is not None
        assert feature_element.attrib["DEST"] == "FM-FEATURE"
        assert feature_element.text == "/FMFeatureModels/Model/FeatureA"
        sysc_element = written.find("SYSC-REF")
        assert sysc_element is not None
        assert sysc_element.text == "/SystemConstants/SyscB"

    def test_write_none_emits_nothing(self):
        element = ET.Element("PARENT")
        ARXMLWriter().writeFMConditionByFeaturesAndSwSystemconsts(element, None)

        assert len(element) == 0

    def test_round_trip(self):
        formula = FMConditionByFeaturesAndSwSystemconsts()
        formula.setMixedString("feature_a")
        feature_ref = RefType()
        feature_ref.setDest("FM-FEATURE")
        feature_ref.setValue("/FMFeatureModels/Model/FeatureA")
        formula.setFeatureRef(feature_ref)

        element = ET.Element("PARENT")
        ARXMLWriter().writeFMConditionByFeaturesAndSwSystemconsts(element, formula)

        # the parser matches namespace-qualified tags; re-parse the written tree
        # with the ARXML namespace injected into the root (writer tests emit none)
        xml_str = ET.tostring(element).decode().replace("<PARENT>", "<PARENT xmlns='%s'>" % NS, 1)
        reparsed = ET.fromstring(xml_str)

        read_back = FMConditionByFeaturesAndSwSystemconsts()
        ARXMLParser().readFMConditionByFeaturesAndSwSystemconsts(reparsed.find("{%s}FM-SYSCOND" % NS), read_back)

        assert read_back.getMixedString() == "feature_a"
        assert read_back.getFeatureRef().getValue() == "/FMFeatureModels/Model/FeatureA"
        assert read_back.getFeatureRef().getDest() == "FM-FEATURE"
