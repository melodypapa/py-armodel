"""Tests for the readConsumedProvidedServiceInstanceGroup handler (R23-11 ConsumedProvidedServiceInstanceGroup, Table 6.174, p.523)."""

import xml.etree.ElementTree as ET

import pytest

from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ARPackage import ARPackage
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Ethernet.ServiceInstances import ConsumedProvidedServiceInstanceGroup
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


def _make_parent() -> ARPackage:
    autosar = AUTOSAR.getInstance()
    return ARPackage(parent=autosar, short_name="TestPkg")


def _snip(inner: str, root_tag: str = "ROOT") -> ET.Element:
    """Wrap an inner XML fragment in a root element bound to the AUTOSAR NS."""
    return ET.fromstring(f"<{root_tag} xmlns='{NS}'>{inner}</{root_tag}>")


def _group() -> ConsumedProvidedServiceInstanceGroup:
    return ConsumedProvidedServiceInstanceGroup(AUTOSAR.getInstance(), "group1")


class TestReadConsumedProvidedServiceInstanceGroup:
    """Tests for readConsumedProvidedServiceInstanceGroup handler (R23-11, Table 6.174, p.523)."""

    def test_read_full(self, parser):
        element = _snip(
            """
                <SHORT-NAME>Group1</SHORT-NAME>
                <CONSUMED-SERVICE-INSTANCES>
                    <CONSUMED-SERVICE-INSTANCE-REF-CONDITIONAL>
                        <CONSUMED-SERVICE-INSTANCE-REF DEST="CONSUMED-SERVICE-INSTANCE">/ServiceInstances/ConsumedServiceInstance1</CONSUMED-SERVICE-INSTANCE-REF>
                    </CONSUMED-SERVICE-INSTANCE-REF-CONDITIONAL>
                    <CONSUMED-SERVICE-INSTANCE-REF-CONDITIONAL>
                        <CONSUMED-SERVICE-INSTANCE-REF DEST="CONSUMED-SERVICE-INSTANCE">/ServiceInstances/ConsumedServiceInstance2</CONSUMED-SERVICE-INSTANCE-REF>
                    </CONSUMED-SERVICE-INSTANCE-REF-CONDITIONAL>
                </CONSUMED-SERVICE-INSTANCES>
                <PROVIDED-SERVICE-INSTANCES>
                    <PROVIDED-SERVICE-INSTANCE-REF-CONDITIONAL>
                        <PROVIDED-SERVICE-INSTANCE-REF DEST="PROVIDED-SERVICE-INSTANCE">/ServiceInstances/ProvidedServiceInstance1</PROVIDED-SERVICE-INSTANCE-REF>
                    </PROVIDED-SERVICE-INSTANCE-REF-CONDITIONAL>
                </PROVIDED-SERVICE-INSTANCES>
            """,
            root_tag="CONSUMED-PROVIDED-SERVICE-INSTANCE-GROUP",
        )
        group = _group()
        parser.readConsumedProvidedServiceInstanceGroup(element, group)

        consumed_refs = group.getConsumedServiceInstanceRefs()
        assert len(consumed_refs) == 2
        assert consumed_refs[0].getValue() == "/ServiceInstances/ConsumedServiceInstance1"
        assert consumed_refs[0].getDest() == "CONSUMED-SERVICE-INSTANCE"
        assert consumed_refs[1].getValue() == "/ServiceInstances/ConsumedServiceInstance2"

        provided_refs = group.getProvidedServiceInstanceRefs()
        assert len(provided_refs) == 1
        assert provided_refs[0].getValue() == "/ServiceInstances/ProvidedServiceInstance1"
        assert provided_refs[0].getDest() == "PROVIDED-SERVICE-INSTANCE"

    def test_read_empty(self, parser):
        element = _snip(
            """
                <SHORT-NAME>Group1</SHORT-NAME>
            """,
            root_tag="CONSUMED-PROVIDED-SERVICE-INSTANCE-GROUP",
        )
        group = _group()
        parser.readConsumedProvidedServiceInstanceGroup(element, group)

        assert group.getConsumedServiceInstanceRefs() == []
        assert group.getProvidedServiceInstanceRefs() == []

    def test_read_empty_wrapper(self, parser):
        element = _snip(
            """
                <SHORT-NAME>Group1</SHORT-NAME>
                <CONSUMED-SERVICE-INSTANCES/>
                <PROVIDED-SERVICE-INSTANCES/>
            """,
            root_tag="CONSUMED-PROVIDED-SERVICE-INSTANCE-GROUP",
        )
        group = _group()
        parser.readConsumedProvidedServiceInstanceGroup(element, group)

        assert group.getConsumedServiceInstanceRefs() == []
        assert group.getProvidedServiceInstanceRefs() == []

    def test_dispatch_via_ar_package(self, parser):
        parent = _make_parent()
        xml = (
            f"<AR-PACKAGE xmlns='{NS}'>"
            "<SHORT-NAME>TestPkg</SHORT-NAME>"
            "<ELEMENTS>"
            "<CONSUMED-PROVIDED-SERVICE-INSTANCE-GROUP>"
            "<SHORT-NAME>Group1</SHORT-NAME>"
            "<CONSUMED-SERVICE-INSTANCES>"
            "<CONSUMED-SERVICE-INSTANCE-REF-CONDITIONAL>"
            '<CONSUMED-SERVICE-INSTANCE-REF DEST="CONSUMED-SERVICE-INSTANCE">/ServiceInstances/ConsumedServiceInstance1</CONSUMED-SERVICE-INSTANCE-REF>'
            "</CONSUMED-SERVICE-INSTANCE-REF-CONDITIONAL>"
            "</CONSUMED-SERVICE-INSTANCES>"
            "</CONSUMED-PROVIDED-SERVICE-INSTANCE-GROUP>"
            "</ELEMENTS>"
            "</AR-PACKAGE>"
        )
        pkg_element = ET.fromstring(xml)
        parser.readARPackageElements(pkg_element, parent)

        groups = [e for e in parent.getElements() if isinstance(e, ConsumedProvidedServiceInstanceGroup)]
        assert len(groups) == 1
        group = groups[0]
        assert group.getShortName() == "Group1"
        assert [ref.getValue() for ref in group.getConsumedServiceInstanceRefs()] == ["/ServiceInstances/ConsumedServiceInstance1"]
        assert group.getProvidedServiceInstanceRefs() == []
