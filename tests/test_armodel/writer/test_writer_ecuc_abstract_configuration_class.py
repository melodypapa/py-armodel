"""
Tests for writing EcucAbstractConfigurationClass content (Table 2.9, p.51,
abstract — via concrete subclass).

XSD group ECUC-ABSTRACT-CONFIGURATION-CLASS element order: CONFIG-CLASS,
CONFIG-VARIANT.

Round-trip counterpart: tests/test_armodel/parser/test_ecuc_abstract_configuration_class.py
"""

import xml.etree.ElementTree as ET

import pytest

from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.ECUCParameterDefTemplate import EcucConfigurationClassEnum, EcucConfigurationVariantEnum, EcucMultiplicityConfigurationClass
from armodel.writer.arxml_writer import ARXMLWriter


@pytest.fixture(autouse=True)
def reset_autosar():
    """Reset AUTOSAR singleton before each test."""
    AUTOSAR.getInstance().new()
    AUTOSAR.getInstance().setARRelease("R23-11")
    yield
    AUTOSAR.getInstance().new()


class TestWriteEcucAbstractConfigurationClass:
    """Tests for writeEcucAbstractConfigurationClass — own element field values (Table 2.9)."""

    def test_write_empty(self):
        """Test that a configuration class without values emits no own-field elements."""
        element = ET.Element("ECUC-MULTIPLICITY-CONFIGURATION-CLASS")
        ARXMLWriter().writeEcucAbstractConfigurationClass(element, EcucMultiplicityConfigurationClass())

        assert [c.tag for c in element] == []

    def test_write_fields_in_xsd_order(self):
        """Test that configClass and configVariant are emitted in XSD order with the spec values."""
        cfg_class = EcucMultiplicityConfigurationClass()
        cfg_class.setConfigClass(EcucConfigurationClassEnum().setValue(EcucConfigurationClassEnum.POST_BUILD))
        cfg_class.setConfigVariant(EcucConfigurationVariantEnum().setValue(EcucConfigurationVariantEnum.VARIANT_POST_BUILD))

        element = ET.Element("ECUC-MULTIPLICITY-CONFIGURATION-CLASS")
        ARXMLWriter().writeEcucAbstractConfigurationClass(element, cfg_class)

        assert [c.tag for c in element] == ["CONFIG-CLASS", "CONFIG-VARIANT"]
        assert element.find("CONFIG-CLASS").text == "PostBuild"
        assert element.find("CONFIG-VARIANT").text == "VARIANT-POST-BUILD"
