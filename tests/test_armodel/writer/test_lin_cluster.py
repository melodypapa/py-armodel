"""Writer round-trip tests for LinCluster (Table 3.36, p.93).

Verifies that a LinCluster created on an ARPackage survives a full
set -> save -> reload cycle with its inherited CommunicationCluster
attributes intact, including the empty-wrapper case.
"""

import pytest

from armodel.models import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    ARLiteral,
    PositiveUnlimitedInteger,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Lin.LinTopology import LinCluster
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


def test_round_trip_full(writer, parser, tmp_path):
    pkg = AUTOSAR.getInstance().createARPackage("Pkg")
    cluster = pkg.createLinCluster("LinCluster")
    baudrate = PositiveUnlimitedInteger()
    baudrate.setValue("19200")
    cluster.setBaudrate(baudrate)
    protocol_name = ARLiteral()
    protocol_name.setValue("LIN")
    cluster.setProtocolName(protocol_name)
    protocol_version = ARLiteral()
    protocol_version.setValue("2.1")
    cluster.setProtocolVersion(protocol_version)

    out_file = str(tmp_path / "lin_cluster.arxml")
    writer.save(out_file, AUTOSAR.getInstance())

    document = _reload(parser, out_file)
    re_pkg = document.find("Pkg")
    assert re_pkg is not None
    assert len(re_pkg.getLinClusters()) == 1

    re_cluster = re_pkg.getElement("LinCluster", LinCluster)
    assert re_cluster is not None
    assert isinstance(re_cluster, LinCluster)
    assert re_cluster.getBaudrate().getValue() == 19200
    assert re_cluster.getProtocolName().getValue() == "LIN"
    assert re_cluster.getProtocolVersion().getValue() == "2.1"


def test_round_trip_empty(writer, parser, tmp_path):
    pkg = AUTOSAR.getInstance().createARPackage("Pkg")
    pkg.createLinCluster("EmptyCluster")

    out_file = str(tmp_path / "lin_cluster_empty.arxml")
    writer.save(out_file, AUTOSAR.getInstance())

    document = _reload(parser, out_file)
    re_pkg = document.find("Pkg")

    re_cluster = re_pkg.getElement("EmptyCluster", LinCluster)
    assert re_cluster is not None
    assert re_cluster.getBaudrate() is None
    assert re_cluster.getProtocolName() is None
    assert re_cluster.getProtocolVersion() is None
    assert re_cluster.getPhysicalChannels() == []
