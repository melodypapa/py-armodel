"""Tests for the ARPackage `element` aggregation (Table 4.1). Round-trip counterpart: tests/test_armodel/writer/test_writer_arpackage_dispatch.py"""

import xml.etree.ElementTree as ET

import pytest

from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ARPackage import (
    DiagnosticFimAliasEvent,
    SwBaseType,
)
from armodel.parser.arxml_parser import ARXMLParser

NS = "http://autosar.org/schema/r4.0"


@pytest.fixture(autouse=True)
def reset_autosar():
    """Reset AUTOSAR singleton before each test."""
    AUTOSAR.getInstance().new()
    yield
    AUTOSAR.getInstance().new()


@pytest.fixture
def parser():
    """Create ARXML parser instance."""
    AUTOSAR.getInstance().new()
    return ARXMLParser()


def _package():
    return AUTOSAR.getInstance().createARPackage("Pkg")


class TestReadARPackageElements:
    """Test the ELEMENTS block of ARPackage (Table 4.1)."""

    def test_elements_populate_the_typed_list(self, parser):
        """Test that ELEMENTS children land in the dedicated elements list."""
        package = _package()
        element = ET.fromstring(
            f"""<AR-PACKAGE xmlns='{NS}'>
                <SHORT-NAME>Pkg</SHORT-NAME>
                <ELEMENTS>
                    <SW-BASE-TYPE>
                        <SHORT-NAME>Base</SHORT-NAME>
                    </SW-BASE-TYPE>
                </ELEMENTS>
            </AR-PACKAGE>"""
        )

        parser.readARPackage(element, package)

        elements = package.getElements()
        assert len(elements) == 1
        assert isinstance(elements[0], SwBaseType)
        assert elements[0].getShortName() == "Base"

    def test_multiple_elements_keep_xml_order(self, parser):
        """Test that several ELEMENTS children are all aggregated."""
        package = _package()
        element = ET.fromstring(
            f"""<AR-PACKAGE xmlns='{NS}'>
                <SHORT-NAME>Pkg</SHORT-NAME>
                <ELEMENTS>
                    <SW-BASE-TYPE>
                        <SHORT-NAME>Base1</SHORT-NAME>
                    </SW-BASE-TYPE>
                    <SW-BASE-TYPE>
                        <SHORT-NAME>Base2</SHORT-NAME>
                    </SW-BASE-TYPE>
                </ELEMENTS>
            </AR-PACKAGE>"""
        )

        parser.readARPackage(element, package)

        assert [e.getShortName() for e in package.getElements()] == ["Base1", "Base2"]

    def test_diagnostic_fim_alias_event_is_read(self, parser):
        """Test that DIAGNOSTIC-FIM-ALIAS-EVENT is dispatched and aggregated."""
        package = _package()
        element = ET.fromstring(
            f"""<AR-PACKAGE xmlns='{NS}'>
                <SHORT-NAME>Pkg</SHORT-NAME>
                <ELEMENTS>
                    <DIAGNOSTIC-FIM-ALIAS-EVENT>
                        <SHORT-NAME>Alias</SHORT-NAME>
                    </DIAGNOSTIC-FIM-ALIAS-EVENT>
                </ELEMENTS>
            </AR-PACKAGE>"""
        )

        parser.readARPackage(element, package)

        aliases = [e for e in package.getElements() if isinstance(e, DiagnosticFimAliasEvent)]
        assert len(aliases) == 1
        assert aliases[0].getShortName() == "Alias"
