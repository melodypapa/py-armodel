"""Parser tests for EcucCommonAttributes (Table 2.8, p.49).

XSD group ECUC-COMMON-ATTRIBUTES (AUTOSAR_00052.xsd) element order:
MULTIPLICITY-CONFIG-CLASSES, ORIGIN, POST-BUILD-VARIANT-MULTIPLICITY,
POST-BUILD-VARIANT-VALUE, REQUIRES-INDEX, VALUE-CONFIG-CLASSES.
(CONFIGURATION-CLASS-AFFECTION and IMPLEMENTATION-CONFIG-CLASSES are absent
from the markdown table and are not modeled — Rule 0015.)
"""

import xml.etree.ElementTree as ET

import pytest

from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.ECUCParameterDefTemplate import EcucCommonAttributes

NS = "http://autosar.org/schema/r4.0"


class _Concrete(EcucCommonAttributes):
    pass


@pytest.fixture(autouse=True)
def reset_autosar():
    AUTOSAR.getInstance().new()
    yield
    AUTOSAR.getInstance().new()


def _snip(inner: str, root_tag: str = "ECUC-INTEGER-PARAM-DEF") -> ET.Element:
    return ET.fromstring(f"<{root_tag} xmlns='{NS}'>{inner}</{root_tag}>")


class TestReadEcucCommonAttributes:
    def test_read_sets_all_fields(self, parser):
        holder = _Concrete(AUTOSAR.getInstance(), "Holder")
        element = _snip(
            "<MULTIPLICITY-CONFIG-CLASSES>"
            "<ECUC-MULTIPLICITY-CONFIGURATION-CLASS>"
            "<CONFIG-CLASS>PostBuild</CONFIG-CLASS>"
            "</ECUC-MULTIPLICITY-CONFIGURATION-CLASS>"
            "</MULTIPLICITY-CONFIG-CLASSES>"
            "<ORIGIN>VENDOR</ORIGIN>"
            "<POST-BUILD-VARIANT-MULTIPLICITY>true</POST-BUILD-VARIANT-MULTIPLICITY>"
            "<POST-BUILD-VARIANT-VALUE>false</POST-BUILD-VARIANT-VALUE>"
            "<REQUIRES-INDEX>true</REQUIRES-INDEX>"
            "<VALUE-CONFIG-CLASSES>"
            "<ECUC-VALUE-CONFIGURATION-CLASS>"
            "<CONFIG-CLASS>PostBuild</CONFIG-CLASS>"
            "</ECUC-VALUE-CONFIGURATION-CLASS>"
            "</VALUE-CONFIG-CLASSES>"
        )
        parser.readEcucCommonAttributes(element, holder)
        assert len(holder.getMultiplicityConfigClasses()) == 1
        assert holder.getOrigin().getValue() == "VENDOR"
        assert holder.getPostBuildVariantMultiplicity().getValue() is True
        assert holder.getPostBuildVariantValue().getValue() is False
        assert holder.getRequiresIndex().getValue() is True
        assert len(holder.getValueConfigClasses()) == 1

    def test_read_empty(self, parser):
        holder = _Concrete(AUTOSAR.getInstance(), "Holder")
        element = _snip("")
        parser.readEcucCommonAttributes(element, holder)
        assert holder.getMultiplicityConfigClasses() == []
        assert holder.getOrigin() is None
        assert holder.getPostBuildVariantMultiplicity() is None
        assert holder.getPostBuildVariantValue() is None
        assert holder.getRequiresIndex() is None
        assert holder.getValueConfigClasses() == []
