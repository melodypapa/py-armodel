"""Reader/writer round-trip tests for SwSystemconst (Table 5.120)."""

import os
import tempfile
import xml.etree.ElementTree as ET

import pytest

from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import RefType
from armodel.models.M2.MSR.DataDictionary.DataDefProperties import SwDataDefProps
from armodel.models.M2.MSR.DataDictionary.SystemConstant import SwSystemconst
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


def _ref(value: str, dest: str = "SW-BASE-TYPE") -> RefType:
    ref = RefType()
    ref.setValue(value)
    ref.setDest(dest)
    return ref


def _fill_data_def_props(const: SwSystemconst):
    props = SwDataDefProps()
    props.setBaseTypeRef(_ref("/DataTypes/uint32"))
    const.setSwDataDefProps(props)


def test_write_sw_systemconst(writer):
    document = _make_document()
    system_const = document.createARPackage("Pkg").createSwSystemConst("MaxValue")
    _fill_data_def_props(system_const)

    parent = _parent()
    writer.writeSwSystemconst(parent, system_const)

    tag = parent.find("SW-SYSTEMCONST")
    assert tag is not None
    children = list(tag)
    assert [child.tag for child in children] == ["SHORT-NAME", "SW-DATA-DEF-PROPS"]
    assert children[0].text == "MaxValue"
    props_tag = children[1]
    base_type_ref = props_tag.find("SW-DATA-DEF-PROPS-VARIANTS/SW-DATA-DEF-PROPS-CONDITIONAL/BASE-TYPE-REF")
    assert base_type_ref is not None
    assert base_type_ref.text == "/DataTypes/uint32"
    assert base_type_ref.attrib["DEST"] == "SW-BASE-TYPE"


def test_write_sw_systemconst_empty(writer):
    document = _make_document()
    system_const = document.createARPackage("Pkg").createSwSystemConst("EmptyConst")

    parent = _parent()
    writer.writeSwSystemconst(parent, system_const)

    tag = parent.find("SW-SYSTEMCONST")
    assert tag is not None
    assert tag.find("SW-DATA-DEF-PROPS") is None


def test_sw_systemconst_round_trip(writer):
    document = _make_document()
    system_const = document.createARPackage("Pkg").createSwSystemConst("MaxValue")
    _fill_data_def_props(system_const)

    file_path = tempfile.mktemp(suffix=".arxml")
    try:
        writer.save(file_path, document)

        document_2 = _make_document()
        ARXMLParser().load(file_path, document_2)

        system_consts = document_2.getARPackages()[0].getSwSystemConsts()
        assert len(system_consts) == 1
        reloaded = system_consts[0]
        assert isinstance(reloaded, SwSystemconst)
        assert reloaded.getShortName() == "MaxValue"
        props = reloaded.getSwDataDefProps()
        assert props is not None
        base_type_ref = props.getBaseTypeRef()
        assert base_type_ref.getValue() == "/DataTypes/uint32"
        assert base_type_ref.getDest() == "SW-BASE-TYPE"
    finally:
        if os.path.exists(file_path):
            os.remove(file_path)
