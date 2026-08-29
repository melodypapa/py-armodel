"""Writer/reader round-trip tests for TcpOptionFilterSet (R4.3.1 Table 6.130, p.326)
and TcpOptionFilterList (R4.3.1 Table 6.131, p.326).

Verifies that a TcpOptionFilterSet created on an ARPackage survives a full
set -> save -> reload cycle, including the empty-wrapper case.
"""

import pytest

from armodel.models import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    PositiveInteger,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Ethernet.EthernetCommunication import (
    TcpOptionFilterList,
    TcpOptionFilterSet,
)
from armodel.parser.arxml_parser import ARXMLParser
from armodel.writer.arxml_writer import ARXMLWriter


@pytest.fixture(autouse=True)
def reset_autosar():
    AUTOSAR.getInstance().new()
    yield
    AUTOSAR.getInstance().new()


@pytest.fixture
def writer():
    AUTOSAR.getInstance().new()
    document = AUTOSAR.getInstance()
    document.setARRelease("R23-11")
    return ARXMLWriter()


@pytest.fixture
def parser():
    return ARXMLParser(options={"warning": True})


def _reload(parser, path):
    AUTOSAR.getInstance().new()
    document = AUTOSAR.getInstance()
    document.setARRelease("R23-11")
    parser.load(path, document)
    return document


def _option(value):
    option = PositiveInteger()
    option.setValue(str(value))
    return option


def test_round_trip_full(writer, parser, tmp_path):
    pkg = AUTOSAR.getInstance().createARPackage("Pkg")
    tcp_set = pkg.createTcpOptionFilterSet("FilterSet")
    list1 = tcp_set.createTcpOptionFilterList("List1")
    list1.addAllowedTcpOption(_option(2))
    list1.addAllowedTcpOption(_option(8))
    list2 = tcp_set.createTcpOptionFilterList("List2")
    list2.addAllowedTcpOption(_option(3))

    out_file = str(tmp_path / "tcp_option_filter_set.arxml")
    writer.save(out_file, AUTOSAR.getInstance())

    document = _reload(parser, out_file)
    re_pkg = document.find("Pkg")
    assert re_pkg is not None

    re_set = re_pkg.getElement("FilterSet", TcpOptionFilterSet)
    assert re_set is not None
    assert isinstance(re_set, TcpOptionFilterSet)

    lists = re_set.getTcpOptionFilterLists()
    assert len(lists) == 2

    re_list1 = re_set.getElement("List1", TcpOptionFilterList)
    assert re_list1 is not None
    assert isinstance(re_list1, TcpOptionFilterList)
    assert [int(option.getValue()) for option in re_list1.getAllowedTcpOptions()] == [2, 8]

    re_list2 = re_set.getElement("List2", TcpOptionFilterList)
    assert re_list2 is not None
    assert [int(option.getValue()) for option in re_list2.getAllowedTcpOptions()] == [3]


def test_round_trip_empty(writer, parser, tmp_path):
    pkg = AUTOSAR.getInstance().createARPackage("Pkg")
    tcp_set = pkg.createTcpOptionFilterSet("EmptySet")
    tcp_set.createTcpOptionFilterList("EmptyList")

    out_file = str(tmp_path / "tcp_option_filter_set_empty.arxml")
    writer.save(out_file, AUTOSAR.getInstance())

    document = _reload(parser, out_file)
    re_pkg = document.find("Pkg")

    re_set = re_pkg.getElement("EmptySet", TcpOptionFilterSet)
    assert re_set is not None
    assert len(re_set.getTcpOptionFilterLists()) == 1

    re_list = re_set.getElement("EmptyList", TcpOptionFilterList)
    assert re_list is not None
    assert re_list.getAllowedTcpOptions() == []
