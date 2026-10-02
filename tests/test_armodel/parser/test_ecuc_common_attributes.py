"""Parser tests for EcucCommonAttributes (Table 2.8, p.49, abstract — via concrete subclass).

XSD group ECUC-COMMON-ATTRIBUTES (AUTOSAR_00052.xsd l.51349) element order:
MULTIPLICITY-CONFIG-CLASSES, ORIGIN, POST-BUILD-VARIANT-MULTIPLICITY,
POST-BUILD-VARIANT-VALUE, REQUIRES-INDEX, VALUE-CONFIG-CLASSES
(configurationClassAffection and implementationConfigClass are
atp.Status="removed" and not modeled).
"""

import xml.etree.ElementTree as ET

import pytest

from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.ECUCParameterDefTemplate import EcucIntegerParamDef, EcucMultiplicityConfigurationClass, EcucValueConfigurationClass

NS = "http://autosar.org/schema/r4.0"


@pytest.fixture(autouse=True)
def reset_autosar():
    AUTOSAR.getInstance().new()
    yield
    AUTOSAR.getInstance().new()


def _snip(inner: str, root_tag: str = "ECUC-INTEGER-PARAM-DEF") -> ET.Element:
    return ET.fromstring(f"<{root_tag} xmlns='{NS}'>{inner}</{root_tag}>")


class TestReadEcucCommonAttributes:
    def _make_obj(self):
        return EcucIntegerParamDef(AUTOSAR.getInstance(), "Param")

    def test_read_sets_all_fields(self, parser):
        obj = self._make_obj()
        element = _snip(
            "<SHORT-NAME>Param</SHORT-NAME>"
            "<MULTIPLICITY-CONFIG-CLASSES>"
            "<ECUC-MULTIPLICITY-CONFIGURATION-CLASS/>"
            "</MULTIPLICITY-CONFIG-CLASSES>"
            "<ORIGIN>AUTOSAR Ecuc Definition Collection</ORIGIN>"
            "<POST-BUILD-VARIANT-MULTIPLICITY>true</POST-BUILD-VARIANT-MULTIPLICITY>"
            "<POST-BUILD-VARIANT-VALUE>false</POST-BUILD-VARIANT-VALUE>"
            "<REQUIRES-INDEX>true</REQUIRES-INDEX>"
            "<VALUE-CONFIG-CLASSES>"
            "<ECUC-VALUE-CONFIGURATION-CLASS/>"
            "</VALUE-CONFIG-CLASSES>"
        )
        parser.readEcucCommonAttributes(element, obj)
        assert len(obj.getMultiplicityConfigClasses()) == 1
        assert isinstance(obj.getMultiplicityConfigClasses()[0], EcucMultiplicityConfigurationClass)
        assert obj.getOrigin().getValue() == "AUTOSAR Ecuc Definition Collection"
        assert obj.getPostBuildVariantMultiplicity().getValue() is True
        assert obj.getPostBuildVariantValue().getValue() is False
        assert obj.getRequiresIndex().getValue() is True
        assert len(obj.getValueConfigClasses()) == 1
        assert isinstance(obj.getValueConfigClasses()[0], EcucValueConfigurationClass)

    def test_read_empty(self, parser):
        obj = self._make_obj()
        element = _snip("")
        parser.readEcucCommonAttributes(element, obj)
        assert obj.getMultiplicityConfigClasses() == []
        assert obj.getOrigin() is None
        assert obj.getPostBuildVariantMultiplicity() is None
        assert obj.getPostBuildVariantValue() is None
        assert obj.getRequiresIndex() is None
        assert obj.getValueConfigClasses() == []
