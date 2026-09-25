"""Reader/writer round-trip tests for UnitGroup (Table 5.81)."""

import os
import tempfile
import xml.etree.ElementTree as ET

import pytest

from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import RefType
from armodel.models.M2.MSR.AsamHdo.Units import UnitGroup
from armodel.parser.arxml_parser import ARXMLParser
from armodel.writer.arxml_writer import ARXMLWriter


@pytest.fixture(autouse=True)
def reset_autosar():
    AUTOSAR.getInstance().new()
    yield
    AUTOSAR.getInstance().new()


@pytest.fixture
def writer():
    return ARXMLWriter()


def _parent():
    return ET.Element("ELEMENTS")


def _make_document() -> AUTOSAR:
    document = AUTOSAR.getInstance()
    document.clear()
    document.setARRelease("R23-11")
    return document


def _ref(value: str, dest: str = "UNIT") -> RefType:
    ref = RefType()
    ref.setValue(value)
    ref.setDest(dest)
    return ref


def _fill_unit_refs(unit_group: UnitGroup):
    unit_group.addUnitRef(_ref("/Units/KmPerHour"))
    unit_group.addUnitRef(_ref("/Units/MilesPerHour"))


def test_write_unit_group(writer):
    document = _make_document()
    unit_group = document.createARPackage("Pkg").createUnitGroup("vehicle_speed")
    _fill_unit_refs(unit_group)

    parent = _parent()
    writer.writeUnitGroup(parent, unit_group)

    tag = parent.find("UNIT-GROUP")
    assert tag is not None
    children = list(tag)
    assert [child.tag for child in children] == ["SHORT-NAME", "UNIT-REFS"]
    assert children[0].text == "vehicle_speed"
    refs_tag = children[1]
    unit_refs = list(refs_tag)
    assert [child.tag for child in unit_refs] == ["UNIT-REF", "UNIT-REF"]
    assert [child.text for child in unit_refs] == ["/Units/KmPerHour", "/Units/MilesPerHour"]
    assert [child.attrib["DEST"] for child in unit_refs] == ["UNIT", "UNIT"]


def test_write_unit_group_empty(writer):
    document = _make_document()
    unit_group = document.createARPackage("Pkg").createUnitGroup("EmptyGroup")

    parent = _parent()
    writer.writeUnitGroup(parent, unit_group)

    tag = parent.find("UNIT-GROUP")
    assert tag is not None
    assert tag.find("UNIT-REFS") is None


def test_unit_group_round_trip(writer):
    document = _make_document()
    unit_group = document.createARPackage("Pkg").createUnitGroup("vehicle_speed")
    _fill_unit_refs(unit_group)

    file_path = tempfile.mktemp(suffix=".arxml")
    try:
        writer.save(file_path, document)

        document_2 = _make_document()
        ARXMLParser().load(file_path, document_2)

        unit_groups = document_2.getARPackages()[0].getUnitGroups()
        assert len(unit_groups) == 1
        reloaded = unit_groups[0]
        assert isinstance(reloaded, UnitGroup)
        assert reloaded.getShortName() == "vehicle_speed"
        refs = reloaded.getUnitRefs()
        assert [ref.getValue() for ref in refs] == ["/Units/KmPerHour", "/Units/MilesPerHour"]
        assert [ref.getDest() for ref in refs] == ["UNIT", "UNIT"]
    finally:
        if os.path.exists(file_path):
            os.remove(file_path)
