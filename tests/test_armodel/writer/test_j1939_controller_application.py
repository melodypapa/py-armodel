"""Writer round-trip tests for J1939ControllerApplication (Table 5.13, p.207).

writeJ1939ControllerApplication calls writeIdentifiable on the J-1939-CONTROLLER-APPLICATION
element exactly once, then emits the own fields in XSD group J-1939-CONTROLLER-APPLICATION
sequence (AUTOSAR_00052.xsd l.75176): FUNCTION-ID, SW-COMPONENT-PROTOTYPE-IREF; and the
writeARPackageElement dispatch emits the element into the package ELEMENTS.

Round-trip counterpart: tests/test_armodel/parser/test_j1939_controller_application.py
"""

import os
import tempfile
import xml.etree.ElementTree as ET

import pytest

from armodel.models import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import PositiveInteger, RefType
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.InstanceRefs import ComponentInSystemInstanceRef
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.SWmapping import J1939ControllerApplication
from armodel.parser.arxml_parser import ARXMLParser
from armodel.writer.arxml_writer import ARXMLWriter

NS = "http://autosar.org/schema/r4.0"


@pytest.fixture(autouse=True)
def reset_autosar():
    AUTOSAR.getInstance().new()
    AUTOSAR.getInstance().setARRelease("R23-11")
    yield
    AUTOSAR.getInstance().new()


def _ref(value: str, dest: str) -> RefType:
    ref = RefType()
    ref.setValue(value)
    ref.setDest(dest)
    return ref


def _full_application() -> J1939ControllerApplication:
    pkg = AUTOSAR.getInstance().createARPackage("J1939ControllerApplications")
    controller_application = pkg.createJ1939ControllerApplication("Ca1")
    controller_application.setFunctionId(PositiveInteger().setValue("42"))
    iref = ComponentInSystemInstanceRef()
    iref.setContextCompositionRef(_ref("/Root/Composition", "ROOT-SW-COMPOSITION-PROTOTYPE"))
    iref.setTargetComponentRef(_ref("/Root/Composition/Swc1", "SW-COMPONENT-PROTOTYPE"))
    controller_application.setSwComponentPrototypeIRef(iref)
    return controller_application


def _write_application(controller_application):
    parent = ET.Element("PARENT")
    ARXMLWriter().writeJ1939ControllerApplication(parent, controller_application)
    return parent


class TestWriteJ1939ControllerApplication:
    def test_entry_point_emits_fields_in_xsd_order(self):
        parent = _write_application(_full_application())

        ca_element = parent.find("J-1939-CONTROLLER-APPLICATION")
        assert ca_element is not None
        assert [child.tag for child in ca_element] == ["SHORT-NAME", "FUNCTION-ID", "SW-COMPONENT-PROTOTYPE-IREF"]
        assert ca_element.find("SHORT-NAME").text == "Ca1"
        assert ca_element.find("FUNCTION-ID").text == "42"

        iref_element = ca_element.find("SW-COMPONENT-PROTOTYPE-IREF")
        assert [child.tag for child in iref_element] == ["CONTEXT-COMPOSITION-REF", "TARGET-COMPONENT-REF"]
        assert iref_element.find("CONTEXT-COMPOSITION-REF").text == "/Root/Composition"
        assert iref_element.find("CONTEXT-COMPOSITION-REF").attrib["DEST"] == "ROOT-SW-COMPOSITION-PROTOTYPE"
        assert iref_element.find("TARGET-COMPONENT-REF").text == "/Root/Composition/Swc1"
        assert iref_element.find("TARGET-COMPONENT-REF").attrib["DEST"] == "SW-COMPONENT-PROTOTYPE"

    def test_bare_application_emits_short_name_only(self):
        pkg = AUTOSAR.getInstance().createARPackage("J1939ControllerApplications")
        controller_application = pkg.createJ1939ControllerApplication("Ca2")

        parent = _write_application(controller_application)
        ca_element = parent.find("J-1939-CONTROLLER-APPLICATION")

        assert [child.tag for child in ca_element] == ["SHORT-NAME"]
        assert ca_element.find("SHORT-NAME").text == "Ca2"


class TestJ1939ControllerApplicationRoundTrip:
    def test_round_trip_through_ar_package_save_load(self):
        """The full ARPackage ELEMENTS path: writeARPackageElement emits the J-1939-CONTROLLER-APPLICATION and the parser dispatch reads it back."""
        source = _full_application()
        file_path = tempfile.mktemp(suffix=".arxml")
        try:
            ARXMLWriter().save(file_path, AUTOSAR.getInstance())

            document = AUTOSAR.getInstance()
            document.clear()
            ARXMLParser(options={"warning": True}).load(file_path, document)

            pkg = document.getARPackages()[0]
            applications = [e for e in pkg.getReferrableElements() if isinstance(e, J1939ControllerApplication)]
            assert len(applications) == 1
            round_tripped = applications[0]
            assert round_tripped.getShortName() == source.getShortName()
            assert round_tripped.getFunctionId().getValue() == 42
            round_tripped_iref = round_tripped.getSwComponentPrototypeIRef()
            assert round_tripped_iref is not None
            assert round_tripped_iref.getContextCompositionRef().getValue() == "/Root/Composition"
            assert round_tripped_iref.getContextCompositionRef().getDest() == "ROOT-SW-COMPOSITION-PROTOTYPE"
            assert round_tripped_iref.getTargetComponentRef().getValue() == "/Root/Composition/Swc1"
            assert round_tripped_iref.getTargetComponentRef().getDest() == "SW-COMPONENT-PROTOTYPE"
        finally:
            os.remove(file_path)

    def test_empty_package_has_no_wrapper(self):
        """A package with no J1939ControllerApplication emits no J-1939-CONTROLLER-APPLICATION element."""
        AUTOSAR.getInstance().createARPackage("EmptyPkg")
        file_path = tempfile.mktemp(suffix=".arxml")
        try:
            ARXMLWriter().save(file_path, AUTOSAR.getInstance())

            tree = ET.parse(file_path)
            assert tree.getroot().find(".//J-1939-CONTROLLER-APPLICATION") is None
        finally:
            os.remove(file_path)
