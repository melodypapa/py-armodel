"""Writer round-trip tests for UserDefinedCluster (Table 3.129, p.179).

XML element order per XSD USER-DEFINED-CLUSTER (AUTOSAR_00052.xsd line 128538):
heritage groups (SHORT-NAME via writeIdentifiable) first, then the
USER-DEFINED-CLUSTER group's USER-DEFINED-CLUSTER-VARIANTS/
USER-DEFINED-CLUSTER-CONDITIONAL wrapper carrying the inherited
COMMUNICATION-CLUSTER content in sequenceOffset order (BAUDRATE,
PHYSICAL-CHANNELS, PROTOCOL-NAME, PROTOCOL-VERSION);
USER-DEFINED-CLUSTER-CONTENT is an empty sequence.
writeUserDefinedCluster calls writeIdentifiable on the outer element and the
reusable writeCommunicationCluster helper exactly once on the CONDITIONAL wrapper.

Verifies that a UserDefinedCluster created on an ARPackage survives a full
set -> save -> reload cycle with its inherited CommunicationCluster
attributes intact, including the empty-wrapper case.
"""

import xml.etree.ElementTree as ET

import pytest

from armodel.models import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    ARLiteral,
    PositiveUnlimitedInteger,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.CddSupport import UserDefinedCluster
from armodel.parser.arxml_parser import ARXMLParser
from armodel.writer.arxml_writer import ARXMLWriter

NS = "http://autosar.org/schema/r4.0"

CONDITIONAL_XSD_ORDER = [
    "BAUDRATE",
    "PROTOCOL-NAME",
    "PROTOCOL-VERSION",
]


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


def _full_cluster():
    pkg = AUTOSAR.getInstance().createARPackage("Pkg")
    cluster = pkg.createUserDefinedCluster("UserDefinedCluster")
    baudrate = PositiveUnlimitedInteger()
    baudrate.setValue("500000")
    cluster.setBaudrate(baudrate)
    protocol_name = ARLiteral()
    protocol_name.setValue("USER-DEFINED")
    cluster.setProtocolName(protocol_name)
    protocol_version = ARLiteral()
    protocol_version.setValue("1.0")
    cluster.setProtocolVersion(protocol_version)
    return cluster


def _new_cluster(name):
    pkg = AUTOSAR.getInstance().createARPackage("Pkg")
    return UserDefinedCluster(pkg, name)


def _write_user_defined_cluster(cluster):
    parent = ET.Element("PARENT")
    ARXMLWriter().writeUserDefinedCluster(parent, cluster)
    return parent


def _namespaced_first_child(parent):
    xml_text = ET.tostring(parent, encoding="unicode")
    namespaced = ET.fromstring(xml_text.replace(parent[0].tag, "%s xmlns='%s'" % (parent[0].tag, NS), 1))
    return namespaced[0]


class TestWriteUserDefinedCluster:
    def test_entry_point_emits_short_name_and_wrapper(self):
        parent = _write_user_defined_cluster(_full_cluster())
        user_defined_cluster = parent.find("USER-DEFINED-CLUSTER")

        assert user_defined_cluster.find("SHORT-NAME").text == "UserDefinedCluster"
        assert user_defined_cluster.find("USER-DEFINED-CLUSTER-VARIANTS/USER-DEFINED-CLUSTER-CONDITIONAL") is not None

    def test_entry_point_writes_inherited_levels_in_xsd_order_exactly_once(self):
        parent = _write_user_defined_cluster(_full_cluster())
        user_defined_cluster = parent.find("USER-DEFINED-CLUSTER")
        conditional = user_defined_cluster.find("USER-DEFINED-CLUSTER-VARIANTS/USER-DEFINED-CLUSTER-CONDITIONAL")

        assert [child.tag for child in conditional] == CONDITIONAL_XSD_ORDER

        all_tags = [child.tag for child in user_defined_cluster.iter()]
        for tag in CONDITIONAL_XSD_ORDER:
            assert all_tags.count(tag) == 1, tag

    def test_entry_point_writes_field_values(self):
        parent = _write_user_defined_cluster(_full_cluster())
        conditional = parent.find("USER-DEFINED-CLUSTER/USER-DEFINED-CLUSTER-VARIANTS/USER-DEFINED-CLUSTER-CONDITIONAL")

        assert conditional.find("BAUDRATE").text == "500000"
        assert conditional.find("PROTOCOL-NAME").text == "USER-DEFINED"
        assert conditional.find("PROTOCOL-VERSION").text == "1.0"

    def test_bare_cluster_emits_short_name_and_empty_wrapper(self):
        parent = _write_user_defined_cluster(_new_cluster("Cluster"))
        user_defined_cluster = parent.find("USER-DEFINED-CLUSTER")

        assert user_defined_cluster.find("SHORT-NAME").text == "Cluster"
        conditional = user_defined_cluster.find("USER-DEFINED-CLUSTER-VARIANTS/USER-DEFINED-CLUSTER-CONDITIONAL")
        assert conditional is not None
        assert len(conditional) == 0

    def test_round_trip_full_through_user_defined_cluster(self):
        parent = _write_user_defined_cluster(_full_cluster())
        reloaded = _new_cluster("UserDefinedCluster")
        ARXMLParser().readUserDefinedCluster(_namespaced_first_child(parent), reloaded)

        assert reloaded.getShortName() == "UserDefinedCluster"
        assert reloaded.getBaudrate().getValue() == 500000
        assert reloaded.getProtocolName().getValue() == "USER-DEFINED"
        assert reloaded.getProtocolVersion().getValue() == "1.0"
        assert reloaded.getPhysicalChannels() == []

    def test_round_trip_empty_through_user_defined_cluster(self):
        parent = _write_user_defined_cluster(_new_cluster("Cluster"))
        reloaded = _new_cluster("Cluster")
        ARXMLParser().readUserDefinedCluster(_namespaced_first_child(parent), reloaded)

        assert reloaded.getShortName() == "Cluster"
        assert reloaded.getBaudrate() is None
        assert reloaded.getProtocolName() is None
        assert reloaded.getProtocolVersion() is None
        assert reloaded.getPhysicalChannels() == []


def test_round_trip_full(writer, parser, tmp_path):
    pkg = AUTOSAR.getInstance().createARPackage("Pkg")
    cluster = pkg.createUserDefinedCluster("UserDefinedCluster")
    baudrate = PositiveUnlimitedInteger()
    baudrate.setValue("500000")
    cluster.setBaudrate(baudrate)
    protocol_name = ARLiteral()
    protocol_name.setValue("USER-DEFINED")
    cluster.setProtocolName(protocol_name)
    protocol_version = ARLiteral()
    protocol_version.setValue("1.0")
    cluster.setProtocolVersion(protocol_version)

    out_file = str(tmp_path / "user_defined_cluster.arxml")
    writer.save(out_file, AUTOSAR.getInstance())

    document = _reload(parser, out_file)
    re_pkg = document.find("Pkg")
    assert re_pkg is not None

    re_cluster = re_pkg.getReferrableElement("UserDefinedCluster", UserDefinedCluster)
    assert re_cluster is not None
    assert isinstance(re_cluster, UserDefinedCluster)
    assert re_cluster.getBaudrate().getValue() == 500000
    assert re_cluster.getProtocolName().getValue() == "USER-DEFINED"
    assert re_cluster.getProtocolVersion().getValue() == "1.0"


def test_round_trip_empty(writer, parser, tmp_path):
    pkg = AUTOSAR.getInstance().createARPackage("Pkg")
    pkg.createUserDefinedCluster("EmptyCluster")

    out_file = str(tmp_path / "user_defined_cluster_empty.arxml")
    writer.save(out_file, AUTOSAR.getInstance())

    document = _reload(parser, out_file)
    re_pkg = document.find("Pkg")

    re_cluster = re_pkg.getReferrableElement("EmptyCluster", UserDefinedCluster)
    assert re_cluster is not None
    assert re_cluster.getBaudrate() is None
    assert re_cluster.getProtocolName() is None
    assert re_cluster.getProtocolVersion() is None
    assert re_cluster.getPhysicalChannels() == []
