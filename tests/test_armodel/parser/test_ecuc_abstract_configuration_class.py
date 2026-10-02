"""Parser tests for EcucAbstractConfigurationClass (Table 2.9, p.51, abstract — via concrete subclass).

XSD group ECUC-ABSTRACT-CONFIGURATION-CLASS element order: CONFIG-CLASS,
CONFIG-VARIANT.
"""

import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.ECUCParameterDefTemplate import EcucMultiplicityConfigurationClass

NS = "http://autosar.org/schema/r4.0"


def _snip(inner: str, root_tag: str = "ECUC-MULTIPLICITY-CONFIGURATION-CLASS") -> ET.Element:
    return ET.fromstring(f"<{root_tag} xmlns='{NS}'>{inner}</{root_tag}>")


class TestReadEcucAbstractConfigurationClass:
    def test_read_sets_all_fields(self, parser):
        cfg_class = EcucMultiplicityConfigurationClass()
        element = _snip("<CONFIG-CLASS>PostBuild</CONFIG-CLASS><CONFIG-VARIANT>VARIANT-POST-BUILD</CONFIG-VARIANT>")
        parser.readEcucAbstractConfigurationClass(element, cfg_class)
        assert cfg_class.getConfigClass().getValue() == "PostBuild"
        assert cfg_class.getConfigVariant().getValue() == "VARIANT-POST-BUILD"

    def test_read_empty(self, parser):
        cfg_class = EcucMultiplicityConfigurationClass()
        element = _snip("")
        parser.readEcucAbstractConfigurationClass(element, cfg_class)
        assert cfg_class.getConfigClass() is None
        assert cfg_class.getConfigVariant() is None
