"""Parser tests for EcucParamConfContainerDef (Table 2.4, p.39).

XSD group ECUC-PARAM-CONF-CONTAINER-DEF (AUTOSAR_00052.xsd) wrapper order:
PARAMETERS, REFERENCES, SUB-CONTAINERS (multipleConfigurationContainer is
atp.Status="removed" and not modeled).
"""

import xml.etree.ElementTree as ET

import pytest

from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.ECUCParameterDefTemplate import EcucBooleanParamDef, EcucParamConfContainerDef, EcucReferenceDef

NS = "http://autosar.org/schema/r4.0"


@pytest.fixture(autouse=True)
def reset_autosar():
    AUTOSAR.getInstance().new()
    yield
    AUTOSAR.getInstance().new()


def _snip(inner: str, root_tag: str = "ECUC-PARAM-CONF-CONTAINER-DEF") -> ET.Element:
    return ET.fromstring(f"<{root_tag} xmlns='{NS}'>{inner}</{root_tag}>")


class TestReadEcucParamConfContainerDef:
    def test_read_sets_all_fields(self, parser):
        container = EcucParamConfContainerDef(AUTOSAR.getInstance(), "Container")
        element = _snip(
            "<SHORT-NAME>Container</SHORT-NAME>"
            "<PARAMETERS>"
            "<ECUC-BOOLEAN-PARAM-DEF><SHORT-NAME>Param1</SHORT-NAME></ECUC-BOOLEAN-PARAM-DEF>"
            "</PARAMETERS>"
            "<REFERENCES>"
            "<ECUC-REFERENCE-DEF><SHORT-NAME>Ref1</SHORT-NAME></ECUC-REFERENCE-DEF>"
            "</REFERENCES>"
            "<SUB-CONTAINERS>"
            "<ECUC-PARAM-CONF-CONTAINER-DEF><SHORT-NAME>Sub1</SHORT-NAME></ECUC-PARAM-CONF-CONTAINER-DEF>"
            "</SUB-CONTAINERS>"
        )
        parser.readEcucParamConfContainerDef(element, container)
        assert container.getShortName() == "Container"
        parameters = container.getParameters()
        assert len(parameters) == 1
        assert isinstance(parameters[0], EcucBooleanParamDef)
        assert parameters[0].getShortName() == "Param1"
        references = container.getReferences()
        assert len(references) == 1
        assert isinstance(references[0], EcucReferenceDef)
        assert references[0].getShortName() == "Ref1"
        sub_containers = container.getSubContainers()
        assert len(sub_containers) == 1
        assert isinstance(sub_containers[0], EcucParamConfContainerDef)
        assert sub_containers[0].getShortName() == "Sub1"

    def test_read_empty(self, parser):
        container = EcucParamConfContainerDef(AUTOSAR.getInstance(), "Container")
        element = _snip("")
        parser.readEcucParamConfContainerDef(element, container)
        assert container.getParameters() == []
        assert container.getReferences() == []
        assert container.getSubContainers() == []
