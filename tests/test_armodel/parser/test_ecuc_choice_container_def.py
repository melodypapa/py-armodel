"""Parser tests for EcucChoiceContainerDef (Table 2.5, p.41).

XSD group ECUC-CHOICE-CONTAINER-DEF (AUTOSAR_00052.xsd) element order:
CHOICES (wrapper, ECUC-PARAM-CONF-CONTAINER-DEF).
"""

import xml.etree.ElementTree as ET

import pytest

from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.ECUCParameterDefTemplate import EcucChoiceContainerDef

NS = "http://autosar.org/schema/r4.0"


@pytest.fixture(autouse=True)
def reset_autosar():
    AUTOSAR.getInstance().new()
    yield
    AUTOSAR.getInstance().new()


def _snip(inner: str, root_tag: str = "ECUC-CHOICE-CONTAINER-DEF") -> ET.Element:
    return ET.fromstring(f"<{root_tag} xmlns='{NS}'>{inner}</{root_tag}>")


class TestReadEcucChoiceContainerDef:
    def test_read_choices(self, parser):
        container = EcucChoiceContainerDef(AUTOSAR.getInstance(), "Choice")
        element = _snip(
            "<SHORT-NAME>Choice</SHORT-NAME>"
            "<CHOICES>"
            "<ECUC-PARAM-CONF-CONTAINER-DEF><SHORT-NAME>C1</SHORT-NAME></ECUC-PARAM-CONF-CONTAINER-DEF>"
            "<ECUC-PARAM-CONF-CONTAINER-DEF><SHORT-NAME>C2</SHORT-NAME></ECUC-PARAM-CONF-CONTAINER-DEF>"
            "</CHOICES>"
        )
        parser.readEcucChoiceContainerDef(element, container)
        assert container.getShortName() == "Choice"
        choices = container.getChoices()
        assert [c.getShortName() for c in choices] == ["C1", "C2"]

    def test_read_empty(self, parser):
        container = EcucChoiceContainerDef(AUTOSAR.getInstance(), "Choice")
        element = _snip("")
        parser.readEcucChoiceContainerDef(element, container)
        assert container.getChoices() == []
