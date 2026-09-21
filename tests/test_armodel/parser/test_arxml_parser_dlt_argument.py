"""Tests for the readDltArgument handler (R23-11 DltArgument, Table E.20, p.13)."""

import xml.etree.ElementTree as ET

import pytest

from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.LogAndTraceExtract import DltArgument
from armodel.parser.arxml_parser import ARXMLParser

NS = "http://autosar.org/schema/r4.0"


@pytest.fixture(autouse=True)
def reset_autosar():
    """Reset AUTOSAR singleton before each test and pin the R23-11 release."""
    AUTOSAR.getInstance().new()
    AUTOSAR.getInstance().setARRelease("R23-11")
    yield
    AUTOSAR.getInstance().new()


@pytest.fixture
def parser():
    """Fresh ARXMLParser instance running in strict mode."""
    AUTOSAR.getInstance().new()
    AUTOSAR.getInstance().setARRelease("R23-11")
    return ARXMLParser()


def _snip(inner: str, root_tag: str = "ROOT") -> ET.Element:
    """Wrap an inner XML fragment in a root element bound to the AUTOSAR NS."""
    return ET.fromstring(f"<{root_tag} xmlns='{NS}'>{inner}</{root_tag}>")


class TestReadDltArgument:
    """Tests for readDltArgument handler (R23-11 DltArgument, Table E.20, p.13)."""

    def test_read_dlt_argument_full(self, parser):
        element = _snip(
            """
                <SHORT-NAME>top_arg</SHORT-NAME>
                <DLT-ARGUMENT-ENTRYS>
                    <DLT-ARGUMENT>
                        <SHORT-NAME>struct_member</SHORT-NAME>
                        <OPTIONAL>true</OPTIONAL>
                    </DLT-ARGUMENT>
                    <DLT-ARGUMENT>
                        <SHORT-NAME>array_dimension</SHORT-NAME>
                        <LENGTH>4</LENGTH>
                        <VARIABLE-LENGTH>false</VARIABLE-LENGTH>
                    </DLT-ARGUMENT>
                </DLT-ARGUMENT-ENTRYS>
                <LENGTH>8</LENGTH>
                <NETWORK-REPRESENTATION>
                    <SW-DATA-DEF-PROPS-VARIANTS>
                        <SW-DATA-DEF-PROPS-CONDITIONAL>
                            <BASE-TYPE-REF DEST="SW-BASE-TYPE">/DataTypes/BaseTypes/uint8</BASE-TYPE-REF>
                        </SW-DATA-DEF-PROPS-CONDITIONAL>
                    </SW-DATA-DEF-PROPS-VARIANTS>
                </NETWORK-REPRESENTATION>
                <OPTIONAL>true</OPTIONAL>
                <PREDEFINED-TEXT>false</PREDEFINED-TEXT>
                <VARIABLE-LENGTH>true</VARIABLE-LENGTH>
            """,
            root_tag="DLT-ARGUMENT",
        )
        argument = DltArgument(None, "top_arg")
        parser.readDltArgument(element, argument)
        assert argument.getShortName() == "top_arg"
        entries = argument.getDltArgumentEntries()
        assert len(entries) == 2
        assert entries[0].getShortName() == "struct_member"
        assert entries[0].getOptional().getValue() is True
        assert entries[1].getShortName() == "array_dimension"
        assert entries[1].getLength().getValue() == 4
        assert entries[1].getVariableLength().getValue() is False
        assert argument.getLength().getValue() == 8
        assert argument.getNetworkRepresentation().getBaseTypeRef().getValue() == "/DataTypes/BaseTypes/uint8"
        assert argument.getNetworkRepresentation().getBaseTypeRef().getDest() == "SW-BASE-TYPE"
        assert argument.getOptional().getValue() is True
        assert argument.getPredefinedText().getValue() is False
        assert argument.getVariableLength().getValue() is True

    def test_read_dlt_argument_empty(self, parser):
        element = _snip(
            """
            """,
            root_tag="DLT-ARGUMENT",
        )
        argument = DltArgument(None, "top_arg")
        parser.readDltArgument(element, argument)
        assert argument.getDltArgumentEntries() == []
        assert argument.getLength() is None
        assert argument.getNetworkRepresentation() is None
        assert argument.getOptional() is None
        assert argument.getPredefinedText() is None
        assert argument.getVariableLength() is None
