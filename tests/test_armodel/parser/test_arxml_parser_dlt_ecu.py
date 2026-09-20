"""Tests for the readDltEcu handler and the ARPackage DltEcu dispatch (R23-11 DltEcu, Table F.49, p.8)."""

import xml.etree.ElementTree as ET

import pytest

from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ARPackage import ARPackage
from armodel.models.M2.AUTOSARTemplates.LogAndTraceExtract import DltApplication, DltEcu
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


class TestReadDltEcu:
    """Tests for readDltEcu handler (R23-11 DltEcu, Table F.49, p.8)."""

    def test_read_dlt_ecu_full(self, parser):
        element = _snip(
            """
                <SHORT-NAME>ecu_one</SHORT-NAME>
                <APPLICATIONS>
                    <DLT-APPLICATION>
                        <SHORT-NAME>app_one</SHORT-NAME>
                        <APPLICATION-ID>APP1</APPLICATION-ID>
                    </DLT-APPLICATION>
                    <DLT-APPLICATION>
                        <SHORT-NAME>app_two</SHORT-NAME>
                        <APPLICATION-ID>APP2</APPLICATION-ID>
                    </DLT-APPLICATION>
                </APPLICATIONS>
                <ECU-ID>ECU1</ECU-ID>
            """,
            root_tag="DLT-ECU",
        )
        ecu = DltEcu(None, "ecu_one")
        parser.readDltEcu(element, ecu)
        assert ecu.getShortName() == "ecu_one"
        applications = ecu.getApplications()
        assert len(applications) == 2
        assert isinstance(applications[0], DltApplication)
        assert applications[0].getShortName() == "app_one"
        assert applications[0].getApplicationId().getValue() == "APP1"
        assert applications[1].getShortName() == "app_two"
        assert applications[1].getApplicationId().getValue() == "APP2"
        assert ecu.getEcuId().getValue() == "ECU1"

    def test_read_dlt_ecu_empty(self, parser):
        element = _snip(
            """
            """,
            root_tag="DLT-ECU",
        )
        ecu = DltEcu(None, "ecu_empty")
        parser.readDltEcu(element, ecu)
        assert ecu.getApplications() == []
        assert ecu.getEcuId() is None


class TestDltEcuDispatch:
    """Tests for the DLT-ECU branch of the readARPackageElements dispatch."""

    def test_dispatch_creates_dlt_ecu_on_package(self, parser):
        parent = ARPackage(parent=AUTOSAR.getInstance(), short_name="TestPkg")
        xml = f"<AR-PACKAGE xmlns='{NS}'>" "<SHORT-NAME>TestPkg</SHORT-NAME>" "<ELEMENTS>" "<DLT-ECU><SHORT-NAME>DE1</SHORT-NAME><ECU-ID>ECU9</ECU-ID></DLT-ECU>" "</ELEMENTS>" "</AR-PACKAGE>"
        pkg_element = ET.fromstring(xml)
        parser.readARPackageElements(pkg_element, parent)
        created = parent.getElement("DE1", DltEcu)
        assert created is not None
        assert isinstance(created, DltEcu)
        assert created.getEcuId().getValue() == "ECU9"
