"""Parser tests for EcucContainerDef (Table 2.3, p.37).

XSD group ECUC-CONTAINER-DEF (AUTOSAR_00052.xsd l.51599) element order:
DESTINATION-URI-REFS, MULTIPLICITY-CONFIG-CLASSES, ORIGIN,
POST-BUILD-VARIANT-MULTIPLICITY, REQUIRES-INDEX
(POST-BUILD-CHANGEABLE carries atp.Status="removed" and is not modeled).
"""

import xml.etree.ElementTree as ET

import pytest

from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.ECUCParameterDefTemplate import EcucContainerDef

NS = "http://autosar.org/schema/r4.0"


class _Concrete(EcucContainerDef):
    pass


@pytest.fixture(autouse=True)
def reset_autosar():
    AUTOSAR.getInstance().new()
    yield
    AUTOSAR.getInstance().new()


def _snip(inner: str, root_tag: str = "ECUC-PARAM-CONF-CONTAINER-DEF") -> ET.Element:
    return ET.fromstring(f"<{root_tag} xmlns='{NS}'>{inner}</{root_tag}>")


class TestReadEcucContainerDef:
    def test_read_sets_all_fields(self, parser):
        holder = _Concrete(AUTOSAR.getInstance(), "Holder")
        element = _snip(
            "<SHORT-NAME>Holder</SHORT-NAME>"
            "<DESTINATION-URI-REFS>"
            "<DESTINATION-URI-REF DEST='ECUC-DESTINATION-URI-DEF'>/EcucDestinationUriDefs/Uri1</DESTINATION-URI-REF>"
            "</DESTINATION-URI-REFS>"
            "<MULTIPLICITY-CONFIG-CLASSES>"
            "<ECUC-MULTIPLICITY-CONFIGURATION-CLASS>"
            "<CONFIG-CLASS>PostBuild</CONFIG-CLASS>"
            "<CONFIG-VARIANT>VARIANT-POST-BUILD</CONFIG-VARIANT>"
            "</ECUC-MULTIPLICITY-CONFIGURATION-CLASS>"
            "</MULTIPLICITY-CONFIG-CLASSES>"
            "<ORIGIN>VENDOR</ORIGIN>"
            "<POST-BUILD-VARIANT-MULTIPLICITY>true</POST-BUILD-VARIANT-MULTIPLICITY>"
            "<REQUIRES-INDEX>false</REQUIRES-INDEX>"
        )
        parser.readEcucContainerDef(element, holder)
        uri_refs = holder.getDestinationUriRefs()
        assert len(uri_refs) == 1
        assert uri_refs[0].getValue() == "/EcucDestinationUriDefs/Uri1"
        assert uri_refs[0].getDest() == "ECUC-DESTINATION-URI-DEF"
        cfg_classes = holder.getMultiplicityConfigClasses()
        assert len(cfg_classes) == 1
        assert cfg_classes[0].getConfigClass().getValue() == "PostBuild"
        assert cfg_classes[0].getConfigVariant().getValue() == "VARIANT-POST-BUILD"
        assert holder.getOrigin().getValue() == "VENDOR"
        assert holder.getPostBuildVariantMultiplicity().getValue() is True
        assert holder.getRequiresIndex().getValue() is False

    def test_read_empty(self, parser):
        holder = _Concrete(AUTOSAR.getInstance(), "Holder")
        element = _snip("")
        parser.readEcucContainerDef(element, holder)
        assert holder.getDestinationUriRefs() == []
        assert holder.getMultiplicityConfigClasses() == []
        assert holder.getOrigin() is None
        assert holder.getPostBuildVariantMultiplicity() is None
        assert holder.getRequiresIndex() is None
