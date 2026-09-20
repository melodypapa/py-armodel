"""Tests for the readDltMessage handler (R23-11 DltMessage, Table F.50, p.12)."""

import xml.etree.ElementTree as ET

import pytest

from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.LogAndTraceExtract import DltMessage
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


class TestReadDltMessage:
    """Tests for readDltMessage handler (R23-11 DltMessage, Table F.50, p.12)."""

    def test_read_dlt_message_full(self, parser):
        element = _snip(
            """
                <SHORT-NAME>top_message</SHORT-NAME>
                <DLT-ARGUMENTS>
                    <DLT-ARGUMENT>
                        <SHORT-NAME>arg_one</SHORT-NAME>
                        <LENGTH>8</LENGTH>
                    </DLT-ARGUMENT>
                    <DLT-ARGUMENT>
                        <SHORT-NAME>arg_two</SHORT-NAME>
                        <PREDEFINED-TEXT>true</PREDEFINED-TEXT>
                    </DLT-ARGUMENT>
                </DLT-ARGUMENTS>
                <MESSAGE-ID>42</MESSAGE-ID>
                <MESSAGE-LINE-NUMBER>17</MESSAGE-LINE-NUMBER>
                <MESSAGE-SOURCE-FILE>logger.c</MESSAGE-SOURCE-FILE>
                <MESSAGE-TYPE-INFO>DLT_LOG_INFO</MESSAGE-TYPE-INFO>
                <PRIVACY-LEVEL>
                    <PRIVACY-LEVEL>2</PRIVACY-LEVEL>
                </PRIVACY-LEVEL>
            """,
            root_tag="DLT-MESSAGE",
        )
        message = DltMessage(None, "top_message")
        parser.readDltMessage(element, message)
        assert message.getShortName() == "top_message"
        arguments = message.getDltArguments()
        assert len(arguments) == 2
        assert arguments[0].getShortName() == "arg_one"
        assert arguments[0].getLength().getValue() == 8
        assert arguments[1].getShortName() == "arg_two"
        assert arguments[1].getPredefinedText().getValue() is True
        assert message.getMessageId().getValue() == 42
        assert message.getMessageLineNumber().getValue() == 17
        assert message.getMessageSourceFile().getValue() == "logger.c"
        assert message.getMessageTypeInfo().getValue() == "DLT_LOG_INFO"
        assert message.getPrivacyLevel().getPrivacyLevel().getValue() == 2

    def test_read_dlt_message_empty(self, parser):
        element = _snip(
            """
            """,
            root_tag="DLT-MESSAGE",
        )
        message = DltMessage(None, "top_message")
        parser.readDltMessage(element, message)
        assert message.getDltArguments() == []
        assert message.getMessageId() is None
        assert message.getMessageLineNumber() is None
        assert message.getMessageSourceFile() is None
        assert message.getMessageTypeInfo() is None
        assert message.getPrivacyLevel() is None
