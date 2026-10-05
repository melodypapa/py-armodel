"""Tests for reading and writing SwCalprmAxis elements (Swc TPS Table 5.47, p.352).

The XSD group SW-CALPRM-AXIS (AUTOSAR_00052.xsd) fixes the child element order:
SW-AXIS-INDEX (sequenceOffset 20), CATEGORY (30), SW-AXIS-GROUPED|SW-AXIS-INDIVIDUAL
(40), SW-CALIBRATION-ACCESS (90), DISPLAY-FORMAT (100). CATEGORY and
SW-CALIBRATION-ACCESS are written as the UPPERCASE XSD wire tokens via
CALPRM_AXIS_CATEGORY_XML_MAP and SW_CALIBRATION_ACCESS_XML_MAP.
"""

import os
import tempfile
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import DisplayFormatString, RefType
from armodel.models.M2.MSR.DataDictionary.Axis import SwAxisGrouped
from armodel.models.M2.MSR.DataDictionary.CalibrationParameter import CalprmAxisCategoryEnum, SwCalprmAxis, SwCalprmAxisSet
from armodel.models.M2.MSR.DataDictionary.DataDefProperties import SwCalibrationAccessEnum, SwDataDefProps
from armodel.models.M2.MSR.DataDictionary.RecordLayout import AxisIndexType
from armodel.parser.arxml_parser import ARXMLParser
from armodel.writer.arxml_writer import ARXMLWriter


def _build_shared_axis_type_ref() -> RefType:
    ref = RefType()
    ref.setValue("/axis/types/shared")
    ref.setDest("SW-AXIS-TYPE")
    return ref


def _build_axis() -> SwCalprmAxis:
    axis = SwCalprmAxis()
    axis.setSwAxisIndex(AxisIndexType().setValue("1"))
    axis.setCategory(CalprmAxisCategoryEnum().setValue(CalprmAxisCategoryEnum.STD_AXIS))
    props = SwAxisGrouped()
    props.setSharedAxisTypeRef(_build_shared_axis_type_ref())
    axis.setSwCalprmAxisTypeProps(props)
    axis.setSwCalibrationAccess(SwCalibrationAccessEnum().setValue(SwCalibrationAccessEnum.READ_ONLY))
    axis.setDisplayFormat(DisplayFormatString().setValue("%.3f"))
    return axis


class TestWriteSwCalprmAxis:
    def test_write_element_order_matches_xsd_group(self):
        parent_element = ET.Element("PARENT")
        ARXMLWriter().setSwCalprmAxis(parent_element, _build_axis())

        axis_element = parent_element.find("SW-CALPRM-AXIS")
        assert axis_element is not None
        tags = [element.tag for element in axis_element]
        assert tags == ["SW-AXIS-INDEX", "CATEGORY", "SW-AXIS-GROUPED", "SW-CALIBRATION-ACCESS", "DISPLAY-FORMAT"]
        assert axis_element.find("SW-AXIS-INDEX").text == "1"
        assert axis_element.find("CATEGORY").text == "STD_AXIS"
        shared_ref_element = axis_element.find("SW-AXIS-GROUPED/SHARED-AXIS-TYPE-REF")
        assert shared_ref_element.text == "/axis/types/shared"
        assert shared_ref_element.attrib["DEST"] == "SW-AXIS-TYPE"
        assert axis_element.find("SW-CALIBRATION-ACCESS").text == "READ-ONLY"
        assert axis_element.find("DISPLAY-FORMAT").text == "%.3f"

    def test_write_partial_axis_omits_unset_elements(self):
        axis = SwCalprmAxis()
        axis.setCategory(CalprmAxisCategoryEnum().setValue(CalprmAxisCategoryEnum.FIX_AXIS))
        parent_element = ET.Element("PARENT")
        ARXMLWriter().setSwCalprmAxis(parent_element, axis)

        axis_element = parent_element.find("SW-CALPRM-AXIS")
        assert axis_element is not None
        assert [element.tag for element in axis_element] == ["CATEGORY"]
        assert axis_element.find("CATEGORY").text == "FIX_AXIS"

    def test_write_empty_set_omits_wrapper(self):
        parent_element = ET.Element("SW-DATA-DEF-PROPS-CONDITIONAL")
        ARXMLWriter().setSwCalprmAxisSet(parent_element, "SW-CALPRM-AXIS-SET", SwCalprmAxisSet())
        assert parent_element.find("SW-CALPRM-AXIS-SET") is None

        parent_element = ET.Element("SW-DATA-DEF-PROPS-CONDITIONAL")
        ARXMLWriter().setSwCalprmAxisSet(parent_element, "SW-CALPRM-AXIS-SET", None)
        assert parent_element.find("SW-CALPRM-AXIS-SET") is None


class TestSwCalprmAxisRoundTrip:
    def test_round_trip_populated(self):
        AUTOSAR.getInstance().setARRelease("R23-11")
        document = AUTOSAR.getInstance()
        document.clear()
        pkg = document.createARPackage("AUTOSAR")
        data_type = pkg.createApplicationPrimitiveDataType("AxisParam")
        axis_set = SwCalprmAxisSet()
        axis_set.addSwCalprmAxis(_build_axis())
        sw_data_def_props = SwDataDefProps()
        sw_data_def_props.setSwCalprmAxisSet(axis_set)
        data_type.setSwDataDefProps(sw_data_def_props)

        file_path = tempfile.mktemp(suffix=".arxml")
        try:
            ARXMLWriter().save(file_path, document)

            xml = open(file_path, encoding="utf-8").read()
            assert "SW-CALPRM-AXIS-SET" in xml

            document_2 = AUTOSAR.getInstance()
            document_2.clear()
            ARXMLParser().load(file_path, document_2)

            data_type_2 = document_2.getARPackages()[0].getApplicationPrimitiveDataTypes()[0]
            axises = data_type_2.getSwDataDefProps().getSwCalprmAxisSet().getSwCalprmAxises()
            assert len(axises) == 1
            axis = axises[0]
            assert axis.getSwAxisIndex().getValue() == "1"
            assert isinstance(axis.getCategory(), CalprmAxisCategoryEnum)
            assert axis.getCategory().getValue() == "stdAxis"
            assert isinstance(axis.getSwCalprmAxisTypeProps(), SwAxisGrouped)
            assert axis.getSwCalprmAxisTypeProps().getSharedAxisTypeRef().getValue() == "/axis/types/shared"
            assert axis.getSwCalibrationAccess().getValue() == "readOnly"
            assert axis.getDisplayFormat().getValue() == "%.3f"
        finally:
            if os.path.exists(file_path):
                os.remove(file_path)

    def test_round_trip_empty_set(self):
        AUTOSAR.getInstance().setARRelease("R23-11")
        document = AUTOSAR.getInstance()
        document.clear()
        pkg = document.createARPackage("AUTOSAR")
        data_type = pkg.createApplicationPrimitiveDataType("NoAxisParam")
        sw_data_def_props = SwDataDefProps()
        sw_data_def_props.setSwCalprmAxisSet(SwCalprmAxisSet())
        data_type.setSwDataDefProps(sw_data_def_props)

        file_path = tempfile.mktemp(suffix=".arxml")
        try:
            ARXMLWriter().save(file_path, document)

            xml = open(file_path, encoding="utf-8").read()
            assert "SW-CALPRM-AXIS-SET" not in xml

            document_2 = AUTOSAR.getInstance()
            document_2.clear()
            ARXMLParser().load(file_path, document_2)

            data_type_2 = document_2.getARPackages()[0].getApplicationPrimitiveDataTypes()[0]
            assert data_type_2.getSwDataDefProps().getSwCalprmAxisSet().getSwCalprmAxises() == []
        finally:
            if os.path.exists(file_path):
                os.remove(file_path)
