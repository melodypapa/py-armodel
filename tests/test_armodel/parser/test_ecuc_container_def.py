"""Parser tests for EcucContainerDef (Table 2.3, p.37, abstract — via concrete subclass).

XSD group ECUC-CONTAINER-DEF (AUTOSAR_00052.xsd) element order:
DESTINATION-URI-REFS, MULTIPLICITY-CONFIG-CLASSES, ORIGIN,
POST-BUILD-VARIANT-MULTIPLICITY, REQUIRES-INDEX (POST-BUILD-CHANGEABLE is
atp.Status="removed" and not modeled).
"""

import xml.etree.ElementTree as ET

import pytest

from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.ECUCParameterDefTemplate import EcucDestinationUriDefRefType, EcucMultiplicityConfigurationClass, EcucParamConfContainerDef

NS = "http://autosar.org/schema/r4.0"


@pytest.fixture(autouse=True)
def reset_autosar():
    AUTOSAR.getInstance().new()
    yield
    AUTOSAR.getInstance().new()


def _snip(inner: str, root_tag: str = "ECUC-PARAM-CONF-CONTAINER-DEF") -> ET.Element:
    return ET.fromstring(f"<{root_tag} xmlns='{NS}'>{inner}</{root_tag}>")


class TestReadEcucContainerDef:
    def _make_obj(self):
        return EcucParamConfContainerDef(AUTOSAR.getInstance(), "Container")

    def test_read_sets_all_fields(self, parser):
        container = self._make_obj()
        element = _snip(
            "<SHORT-NAME>Container</SHORT-NAME>"
            "<DESTINATION-URI-REFS>"
            '<DESTINATION-URI-REF DEST="ECUC-DESTINATION-URI-DEF">/AUTOSAR/UriDefs/Uri1</DESTINATION-URI-REF>'
            "</DESTINATION-URI-REFS>"
            "<MULTIPLICITY-CONFIG-CLASSES>"
            "<ECUC-MULTIPLICITY-CONFIGURATION-CLASS/>"
            "</MULTIPLICITY-CONFIG-CLASSES>"
            "<ORIGIN>AUTOSAR Ecuc Definition Collection</ORIGIN>"
            "<POST-BUILD-VARIANT-MULTIPLICITY>true</POST-BUILD-VARIANT-MULTIPLICITY>"
            "<REQUIRES-INDEX>false</REQUIRES-INDEX>"
        )
        parser.readEcucContainerDef(element, container)
        assert container.getShortName() == "Container"
        refs = container.getDestinationUriRefs()
        assert len(refs) == 1
        assert isinstance(refs[0], EcucDestinationUriDefRefType)
        assert refs[0].getValue() == "/AUTOSAR/UriDefs/Uri1"
        assert refs[0].getDest() == "ECUC-DESTINATION-URI-DEF"
        assert len(container.getMultiplicityConfigClasses()) == 1
        assert isinstance(container.getMultiplicityConfigClasses()[0], EcucMultiplicityConfigurationClass)
        assert container.getOrigin().getValue() == "AUTOSAR Ecuc Definition Collection"
        assert container.getPostBuildVariantMultiplicity().getValue() is True
        assert container.getRequiresIndex().getValue() is False

    def test_read_empty(self, parser):
        container = self._make_obj()
        element = _snip("")
        parser.readEcucContainerDef(element, container)
        assert container.getDestinationUriRefs() == []
        assert container.getMultiplicityConfigClasses() == []
        assert container.getOrigin() is None
        assert container.getPostBuildVariantMultiplicity() is None
        assert container.getRequiresIndex() is None
