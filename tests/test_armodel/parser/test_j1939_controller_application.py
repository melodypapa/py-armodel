"""Parser tests for J1939ControllerApplication (Table 5.13, p.207).

ARElement aggregated by ARPackage.element: the XSD group J-1939-CONTROLLER-APPLICATION
(AUTOSAR_00052.xsd l.75176) sequences FUNCTION-ID, SW-COMPONENT-PROTOTYPE-IREF after the
base groups, so the reader owns the IDENTIFIABLE base level (SHORT-NAME/UUID/CATEGORY)
via readIdentifiable exactly once, then reads the two own fields in XSD order.
"""

import os
import tempfile
import xml.etree.ElementTree as ET

import pytest

from armodel.models import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR as AutosarDocument
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.SWmapping import J1939ControllerApplication
from armodel.parser.arxml_parser import ARXMLParser

NS = "http://autosar.org/schema/r4.0"


@pytest.fixture(autouse=True)
def reset_autosar():
    AUTOSAR.getInstance().new()
    AUTOSAR.getInstance().setARRelease("R23-11")
    yield
    AUTOSAR.getInstance().new()


FULL_AUTOSAR = f"""<?xml version="1.0" encoding="utf-8"?>
<AUTOSAR xmlns="{NS}" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:schemaLocation="{NS} AUTOSAR_00052.xsd">
    <AR-PACKAGES>
        <AR-PACKAGE>
            <SHORT-NAME>J1939ControllerApplications</SHORT-NAME>
            <ELEMENTS>
                <J-1939-CONTROLLER-APPLICATION UUID="7a1f2b3c-4d5e-4f60-8a9b-0c1d2e3f4a5b">
                    <SHORT-NAME>Ca1</SHORT-NAME>
                    <CATEGORY>J1939_CONTROLLER_APPLICATION</CATEGORY>
                    <FUNCTION-ID>42</FUNCTION-ID>
                    <SW-COMPONENT-PROTOTYPE-IREF>
                        <CONTEXT-COMPOSITION-REF DEST="ROOT-SW-COMPOSITION-PROTOTYPE">/Root/Composition</CONTEXT-COMPOSITION-REF>
                        <TARGET-COMPONENT-REF DEST="SW-COMPONENT-PROTOTYPE">/Root/Composition/Swc1</TARGET-COMPONENT-REF>
                    </SW-COMPONENT-PROTOTYPE-IREF>
                </J-1939-CONTROLLER-APPLICATION>
            </ELEMENTS>
        </AR-PACKAGE>
    </AR-PACKAGES>
</AUTOSAR>"""


EMPTY_AUTOSAR = f"""<?xml version="1.0" encoding="utf-8"?>
<AUTOSAR xmlns="{NS}" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:schemaLocation="{NS} AUTOSAR_00052.xsd">
    <AR-PACKAGES>
        <AR-PACKAGE>
            <SHORT-NAME>J1939ControllerApplications</SHORT-NAME>
            <ELEMENTS/>
        </AR-PACKAGE>
    </AR-PACKAGES>
</AUTOSAR>"""


def _load(content: str):
    file_path = tempfile.mktemp(suffix=".arxml")
    try:
        with open(file_path, "w", encoding="utf-8") as f:
            f.write(content)
        document = AutosarDocument.getInstance()
        document.clear()
        ARXMLParser(options={"warning": True}).load(file_path, document)
        return document
    finally:
        os.remove(file_path)


def _ca_applications(pkg):
    return [e for e in pkg.getReferrableElements() if isinstance(e, J1939ControllerApplication)]


class TestReadJ1939ControllerApplication:
    def test_read_field_values(self):
        parser = ARXMLParser(options={"warning": True})
        element = ET.fromstring(
            f"<J-1939-CONTROLLER-APPLICATION xmlns='{NS}' UUID='7a1f2b3c-4d5e-4f60-8a9b-0c1d2e3f4a5b'>"
            "<SHORT-NAME>Ca1</SHORT-NAME>"
            "<FUNCTION-ID>42</FUNCTION-ID>"
            "<SW-COMPONENT-PROTOTYPE-IREF>"
            "<CONTEXT-COMPOSITION-REF DEST='ROOT-SW-COMPOSITION-PROTOTYPE'>/Root/Composition</CONTEXT-COMPOSITION-REF>"
            "<TARGET-COMPONENT-REF DEST='SW-COMPONENT-PROTOTYPE'>/Root/Composition/Swc1</TARGET-COMPONENT-REF>"
            "</SW-COMPONENT-PROTOTYPE-IREF>"
            "</J-1939-CONTROLLER-APPLICATION>"
        )
        controller_application = J1939ControllerApplication(AutosarDocument.getInstance(), "Ca1")
        parser.readJ1939ControllerApplication(element, controller_application)

        assert controller_application.getShortName() == "Ca1"
        assert controller_application.getUuid().getValue() == "7a1f2b3c-4d5e-4f60-8a9b-0c1d2e3f4a5b"
        assert controller_application.getFunctionId().getValue() == 42

        iref = controller_application.getSwComponentPrototypeIRef()
        assert iref is not None
        assert iref.getContextCompositionRef().getValue() == "/Root/Composition"
        assert iref.getContextCompositionRef().getDest() == "ROOT-SW-COMPOSITION-PROTOTYPE"
        assert iref.getTargetComponentRef().getValue() == "/Root/Composition/Swc1"
        assert iref.getTargetComponentRef().getDest() == "SW-COMPONENT-PROTOTYPE"

    def test_load_via_ar_package(self):
        """The ARPackage ELEMENTS dispatch reads a J-1939-CONTROLLER-APPLICATION."""
        document = _load(FULL_AUTOSAR)

        pkg = document.getARPackages()[0]
        applications = _ca_applications(pkg)
        assert len(applications) == 1
        controller_application = applications[0]
        assert controller_application.getShortName() == "Ca1"
        assert controller_application.getCategory().getValue() == "J1939_CONTROLLER_APPLICATION"
        assert controller_application.getFunctionId().getValue() == 42
        assert controller_application.getSwComponentPrototypeIRef().getTargetComponentRef().getValue() == "/Root/Composition/Swc1"

    def test_read_empty_elements(self):
        """A package with an empty ELEMENTS wrapper creates no J1939ControllerApplication."""
        document = _load(EMPTY_AUTOSAR)

        pkg = document.getARPackages()[0]
        assert _ca_applications(pkg) == []

    def test_read_missing_optional_fields(self):
        """An element with no own-field children leaves functionId and the iref None."""
        parser = ARXMLParser(options={"warning": True})
        element = ET.fromstring(f"<J-1939-CONTROLLER-APPLICATION xmlns='{NS}'><SHORT-NAME>Ca2</SHORT-NAME></J-1939-CONTROLLER-APPLICATION>")
        controller_application = J1939ControllerApplication(AutosarDocument.getInstance(), "Initial")
        parser.readJ1939ControllerApplication(element, controller_application)

        assert controller_application.getFunctionId() is None
        assert controller_application.getSwComponentPrototypeIRef() is None
