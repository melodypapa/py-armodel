"""Reader tests for TcpOptionFilterList (R23-11 Table 6.123, p.457).

The allowedTcpOption attribute is a spec `*` `attr` serialized as a wrapper
(ALLOWED-TCP-OPTIONS) of ALLOWED-TCP-OPTION (AR:POSITIVE-INTEGER) items
(AUTOSAR_00052.xsd L120400-120419), read through the class's own helper
readTcpOptionFilterList via the spec-typed PositiveInteger list helper.
"""

import xml.etree.ElementTree as ET

import pytest

from armodel.models import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    PositiveInteger,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Ethernet.TcpOptionFilterSet import (
    TcpOptionFilterList,
)
from armodel.parser.arxml_parser import ARXMLParser

NS = 'xmlns="http://autosar.org/schema/r4.0"'


@pytest.fixture(autouse=True)
def reset_autosar():
    document = AUTOSAR.getInstance()
    document.new()
    document.setARRelease("R23-11")
    yield
    AUTOSAR.getInstance().new()


@pytest.fixture
def parser():
    return ARXMLParser(options={"warning": True})


def _read(parser, xml, obj):
    parser.readTcpOptionFilterList(ET.fromstring(xml), obj)


class TestTcpOptionFilterListReader:
    def test_read_wrapper_list_values(self, parser):
        obj = TcpOptionFilterList(None, "Filter")
        _read(
            parser,
            "<TCP-OPTION-FILTER-LIST %s>"
            "<SHORT-NAME>Filter</SHORT-NAME>"
            "<ALLOWED-TCP-OPTIONS>"
            "<ALLOWED-TCP-OPTION>7</ALLOWED-TCP-OPTION>"
            "<ALLOWED-TCP-OPTION>60</ALLOWED-TCP-OPTION>"
            "</ALLOWED-TCP-OPTIONS>"
            "</TCP-OPTION-FILTER-LIST>" % NS,
            obj,
        )
        options = obj.getAllowedTcpOptions()
        assert [int(option.getValue()) for option in options] == [7, 60]
        assert all(isinstance(option, PositiveInteger) for option in options)

    def test_read_without_wrapper_yields_empty(self, parser):
        obj = TcpOptionFilterList(None, "Empty")
        _read(parser, "<TCP-OPTION-FILTER-LIST %s><SHORT-NAME>Empty</SHORT-NAME></TCP-OPTION-FILTER-LIST>" % NS, obj)
        assert obj.getAllowedTcpOptions() == []

    def test_read_empty_wrapper_yields_empty(self, parser):
        obj = TcpOptionFilterList(None, "Empty")
        _read(
            parser,
            "<TCP-OPTION-FILTER-LIST %s><SHORT-NAME>Empty</SHORT-NAME>" "<ALLOWED-TCP-OPTIONS/></TCP-OPTION-FILTER-LIST>" % NS,
            obj,
        )
        assert obj.getAllowedTcpOptions() == []

    def test_read_rejects_negative_positive_integer(self, parser):
        obj = TcpOptionFilterList(None, "Bad")
        with pytest.raises(ValueError):
            _read(
                parser,
                "<TCP-OPTION-FILTER-LIST %s><SHORT-NAME>Bad</SHORT-NAME>" "<ALLOWED-TCP-OPTIONS>" "<ALLOWED-TCP-OPTION>-1</ALLOWED-TCP-OPTION>" "</ALLOWED-TCP-OPTIONS></TCP-OPTION-FILTER-LIST>" % NS,
                obj,
            )
