"""Parser tests for EcucParamConfContainerDef (Table 2.4, p.39).

XSD group ECUC-PARAM-CONF-CONTAINER-DEF (AUTOSAR_00052.xsd l.53080) element order
(after the inherited ECUC-CONTAINER-DEF group): PARAMETERS, REFERENCES,
SUB-CONTAINERS. MULTIPLE-CONFIGURATION-CONTAINER carries atp.Status="removed"
and is not modeled.
"""

import xml.etree.ElementTree as ET

import pytest

from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.ECUCParameterDefTemplate import EcucParamConfContainerDef

NS = "http://autosar.org/schema/r4.0"


@pytest.fixture(autouse=True)
def reset_autosar():
    AUTOSAR.getInstance().new()
    yield
    AUTOSAR.getInstance().new()


def _snip(inner: str, root_tag: str = "ECUC-PARAM-CONF-CONTAINER-DEF") -> ET.Element:
    return ET.fromstring(f"<{root_tag} xmlns='{NS}'>{inner}</{root_tag}>")


class TestReadEcucParamConfContainerDef:
    def test_read_parameters_references_subcontainers(self, parser):
        container = EcucParamConfContainerDef(AUTOSAR.getInstance(), "Container")
        element = _snip(
            "<SHORT-NAME>Container</SHORT-NAME>"
            "<PARAMETERS>"
            "<ECUC-INTEGER-PARAM-DEF><SHORT-NAME>P1</SHORT-NAME></ECUC-INTEGER-PARAM-DEF>"
            "<ECUC-BOOLEAN-PARAM-DEF><SHORT-NAME>P2</SHORT-NAME></ECUC-BOOLEAN-PARAM-DEF>"
            "</PARAMETERS>"
            "<REFERENCES>"
            "<ECUC-REFERENCE-DEF><SHORT-NAME>R1</SHORT-NAME></ECUC-REFERENCE-DEF>"
            "<ECUC-FOREIGN-REFERENCE-DEF><SHORT-NAME>R2</SHORT-NAME></ECUC-FOREIGN-REFERENCE-DEF>"
            "</REFERENCES>"
            "<SUB-CONTAINERS>"
            "<ECUC-PARAM-CONF-CONTAINER-DEF><SHORT-NAME>S1</SHORT-NAME></ECUC-PARAM-CONF-CONTAINER-DEF>"
            "</SUB-CONTAINERS>"
        )
        parser.readEcucParamConfContainerDef(element, container)
        assert container.getShortName() == "Container"
        parameters = container.getParameters()
        assert [p.getShortName() for p in parameters] == ["P1", "P2"]
        references = container.getReferences()
        assert [r.getShortName() for r in references] == ["R1", "R2"]
        sub_containers = container.getSubContainers()
        assert [s.getShortName() for s in sub_containers] == ["S1"]

    def test_read_empty(self, parser):
        container = EcucParamConfContainerDef(AUTOSAR.getInstance(), "Container")
        element = _snip("")
        parser.readEcucParamConfContainerDef(element, container)
        assert container.getParameters() == []
        assert container.getReferences() == []
        assert container.getSubContainers() == []
