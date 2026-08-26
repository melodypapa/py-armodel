"""Writer/reader round-trip tests for SomeipServiceVersion (Table F.118, p.2059).

SomeipServiceVersion is an inline ARObject value type (Base: ARObject) consumed by
ConsumedServiceInstance.blocklistedVersion. It is serialized inside the parent
CONSUMED-SERVICE-INSTANCE element as BLOCKLISTED-VERSIONS > SOMEIP-SERVICE-VERSION.
"""

import xml.etree.cElementTree as ET

import pytest

from armodel.models import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import PositiveInteger
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Ethernet.ServiceInstances import (
    ApplicationEndpoint,
    ConsumedServiceInstance,
    SocketAddress,
    SomeipServiceVersion,
)
from armodel.parser.arxml_parser import ARXMLParser
from armodel.writer.arxml_writer import ARXMLWriter

NS = "http://autosar.org/schema/r4.0"


@pytest.fixture(autouse=True)
def reset_autosar():
    AUTOSAR.getInstance().new()
    yield
    AUTOSAR.getInstance().new()


@pytest.fixture
def writer():
    AUTOSAR.getInstance().new()
    return ARXMLWriter()


@pytest.fixture
def parser():
    AUTOSAR.getInstance().new()
    return ARXMLParser()


def _parent():
    return ET.Element("PARENT")


def _pos_int(text):
    val = PositiveInteger()
    val.setValue(text)
    return val


def _serialize_and_wrap(parent: ET.Element) -> ET.Element:
    inner = ET.tostring(parent).decode("utf-8")
    root = ET.fromstring(f"<AUTOSAR xmlns='{NS}'>{inner}</AUTOSAR>")
    return root[0][0]


def _new_consumed_service_instance():
    endpoint = ApplicationEndpoint(parent=SocketAddress(parent=AUTOSAR.getInstance(), short_name="sa"), short_name="ae")
    return ConsumedServiceInstance(parent=endpoint, short_name="csi")


def _add_version(instance, major, minor):
    version = SomeipServiceVersion()
    version.setMajorVersion(_pos_int(str(major)))
    version.setMinorVersion(_pos_int(str(minor)))
    instance.getBlocklistedVersions().append(version)
    return version


class TestWriteSomeipServiceVersion:
    def test_write_all_fields(self, writer):
        instance = _new_consumed_service_instance()
        _add_version(instance, 1, 2)

        parent = _parent()
        writer.writeConsumedServiceInstance(parent, instance)

        csi = parent.find("CONSUMED-SERVICE-INSTANCE")
        assert csi is not None
        versions = csi.find("BLOCKLISTED-VERSIONS")
        assert versions is not None
        items = versions.findall("SOMEIP-SERVICE-VERSION")
        assert len(items) == 1
        assert items[0].find("MAJOR-VERSION").text == "1"
        assert items[0].find("MINOR-VERSION").text == "2"

    def test_write_multiple_versions(self, writer):
        instance = _new_consumed_service_instance()
        _add_version(instance, 1, 2)
        _add_version(instance, 3, 4)

        parent = _parent()
        writer.writeConsumedServiceInstance(parent, instance)

        items = parent.find("CONSUMED-SERVICE-INSTANCE/BLOCKLISTED-VERSIONS").findall("SOMEIP-SERVICE-VERSION")
        assert len(items) == 2
        assert items[0].find("MAJOR-VERSION").text == "1"
        assert items[0].find("MINOR-VERSION").text == "2"
        assert items[1].find("MAJOR-VERSION").text == "3"
        assert items[1].find("MINOR-VERSION").text == "4"

    def test_write_empty_versions_omits_wrapper(self, writer):
        instance = _new_consumed_service_instance()

        parent = _parent()
        writer.writeConsumedServiceInstance(parent, instance)

        csi = parent.find("CONSUMED-SERVICE-INSTANCE")
        assert csi.find("BLOCKLISTED-VERSIONS") is None


class TestSomeipServiceVersionRoundTrip:
    def test_round_trip_preserves_all_values(self, writer, parser):
        instance = _new_consumed_service_instance()
        _add_version(instance, 1, 2)

        parent = _parent()
        writer.writeConsumedServiceInstance(parent, instance)
        element = _serialize_and_wrap(parent)

        recovered = _new_consumed_service_instance()
        parser.readConsumedServiceInstance(element, recovered)

        versions = recovered.getBlocklistedVersions()
        assert len(versions) == 1
        assert isinstance(versions[0], SomeipServiceVersion)
        assert versions[0].getMajorVersion().getValue() == 1
        assert versions[0].getMinorVersion().getValue() == 2

    def test_round_trip_multiple_versions(self, writer, parser):
        instance = _new_consumed_service_instance()
        _add_version(instance, 1, 2)
        _add_version(instance, 3, 4)

        parent = _parent()
        writer.writeConsumedServiceInstance(parent, instance)
        element = _serialize_and_wrap(parent)

        recovered = _new_consumed_service_instance()
        parser.readConsumedServiceInstance(element, recovered)

        versions = recovered.getBlocklistedVersions()
        assert len(versions) == 2
        assert [v.getMajorVersion().getValue() for v in versions] == [1, 3]
        assert [v.getMinorVersion().getValue() for v in versions] == [2, 4]

    def test_reader_empty_fields(self, parser):
        element = ET.fromstring("<CONSUMED-SERVICE-INSTANCE xmlns='%s'><SHORT-NAME>csi</SHORT-NAME></CONSUMED-SERVICE-INSTANCE>" % NS)
        instance = _new_consumed_service_instance()
        parser.readConsumedServiceInstance(element, instance)
        assert instance.getBlocklistedVersions() == []
