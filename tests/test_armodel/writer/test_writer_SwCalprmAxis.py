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
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import DisplayFormatString, Float, MonotonyEnum, Numerical, RefType
from armodel.models.M2.MSR.DataDictionary.Axis import SwAxisGeneric, SwAxisGrouped, SwGenericAxisParam
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
    gradient = Float()
    gradient.setValue(2.5)
    props.setMaxGradient(gradient)
    props.setMonotony(MonotonyEnum().setValue(MonotonyEnum.STRICTLY_INCREASING))
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
            assert axis.getSwCalprmAxisTypeProps().getMaxGradient().getValue() == 2.5
            assert isinstance(axis.getSwCalprmAxisTypeProps().getMonotony(), MonotonyEnum)
            assert axis.getSwCalprmAxisTypeProps().getMonotony().getValue() == "strictlyIncreasing"
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


class TestWriteSwCalprmAxisTypeProps:
    """Writer tests for the abstract SwCalprmAxisTypeProps element group (SWCT Table 5.49, p.353).

    MAX-GRADIENT then MONOTONY lead both concrete choice branches (XSD element group
    SW-CALPRM-AXIS-TYPE-PROPS, AUTOSAR_00052.xsd L114844; SW-AXIS-GROUPED complexType
    L114493 inlines it ahead of the SW-AXIS-GROUPED group). MONOTONY is written as the
    UPPERCASE XSD wire token (MONOTONY-ENUM--SIMPLE) via MONOTONY_XML_MAP; the abstract
    class owns the reusable writeSwCalprmAxisTypeProps helper called by both branches
    (Rule 0001.7).
    """

    def test_write_helper_emits_base_attrs(self):
        """writeSwCalprmAxisTypeProps emits MAX-GRADIENT then MONOTONY in XSD group order."""
        props = SwAxisGrouped()
        gradient = Float()
        gradient.setValue(2.5)
        props.setMaxGradient(gradient)
        props.setMonotony(MonotonyEnum().setValue(MonotonyEnum.STRICTLY_INCREASING))
        parent = ET.Element("SW-AXIS-GROUPED")
        ARXMLWriter().writeSwCalprmAxisTypeProps(parent, props)

        assert [child.tag for child in parent] == ["MAX-GRADIENT", "MONOTONY"]
        assert parent.find("MAX-GRADIENT").text == "2.5"
        assert parent.find("MONOTONY").text == "STRICTLY-INCREASING"

    def test_write_helper_omits_unset_attrs(self):
        props = SwAxisGrouped()
        parent = ET.Element("SW-AXIS-GROUPED")
        ARXMLWriter().writeSwCalprmAxisTypeProps(parent, props)
        assert len(list(parent)) == 0

    def test_write_base_attrs_lead_grouped_choice_branch(self):
        """MAX-GRADIENT/MONOTONY lead SW-AXIS-GROUPED ahead of the subtype's own elements."""
        axis = SwCalprmAxis()
        props = SwAxisGrouped()
        gradient = Float()
        gradient.setValue(0.75)
        props.setMaxGradient(gradient)
        props.setMonotony(MonotonyEnum().setValue(MonotonyEnum.MONOTONOUS))
        props.setSharedAxisTypeRef(_build_shared_axis_type_ref())
        props.setSwAxisIndex(AxisIndexType().setValue("2"))
        axis.setSwCalprmAxisTypeProps(props)

        parent = ET.Element("PARENT")
        ARXMLWriter().setSwCalprmAxis(parent, axis)

        grouped = parent.find("SW-CALPRM-AXIS/SW-AXIS-GROUPED")
        assert grouped is not None
        assert [child.tag for child in grouped] == ["MAX-GRADIENT", "MONOTONY", "SHARED-AXIS-TYPE-REF", "SW-AXIS-INDEX"]
        assert grouped.find("MAX-GRADIENT").text == "0.75"
        assert grouped.find("MONOTONY").text == "MONOTONOUS"


class TestWriteSwAxisGeneric:
    """Tests for writing SwAxisGeneric (Swc TPS Table 5.51, p.355).

    setSwAxisGeneric emits SW-AXIS-GENERIC with SW-AXIS-TYPE-REF (XSD sequenceOffset 20)
    ahead of the SW-GENERIC-AXIS-PARAMS wrapper (40); the wrapper is emitted only when
    the parameter list is non-empty, and the round-trip re-parses to equal field values.
    """

    def _build_generic_axis(self) -> SwAxisGeneric:
        generic = SwAxisGeneric()
        axis_type_ref = RefType()
        axis_type_ref.setDest("SW-AXIS-TYPE")
        axis_type_ref.setValue("/axis/types/fixed")
        generic.setSwAxisTypeRef(axis_type_ref)
        param = SwGenericAxisParam()
        param_type_ref = RefType()
        param_type_ref.setDest("SW-GENERIC-AXIS-PARAM-TYPE")
        param_type_ref.setValue("/axis/types/fixed/shift")
        param.setSwGenericAxisParamTypeRef(param_type_ref)
        vf = Numerical()
        vf.setValue("1.5")
        param.addVf(vf)
        generic.addSwGenericAxisParam(param)
        return generic

    def test_write_sw_axis_generic_with_params_roundtrip(self):
        generic = self._build_generic_axis()

        parent = ET.Element("PARENT")
        ARXMLWriter().setSwAxisGeneric(parent, generic)

        generic_el = parent.find("SW-AXIS-GENERIC")
        assert generic_el is not None
        assert [child.tag for child in generic_el] == ["SW-AXIS-TYPE-REF", "SW-GENERIC-AXIS-PARAMS"]
        assert generic_el.find("SW-AXIS-TYPE-REF").text == "/axis/types/fixed"
        params_wrapper = generic_el.find("SW-GENERIC-AXIS-PARAMS")
        assert params_wrapper is not None
        param_el = params_wrapper.find("SW-GENERIC-AXIS-PARAM")
        assert param_el is not None
        assert param_el.find("SW-GENERIC-AXIS-PARAM-TYPE-REF").text == "/axis/types/fixed/shift"
        assert param_el.find("VF").text == "1.5"

        wrapped = ET.fromstring("<WRAP xmlns='http://autosar.org/schema/r4.0'>%s</WRAP>" % ET.tostring(generic_el, encoding="unicode"))
        reparsed = ARXMLParser().getSwAxisGeneric(wrapped[0])
        assert reparsed is not None
        assert reparsed.getSwAxisTypeRef().getValue() == "/axis/types/fixed"
        reparsed_params = reparsed.getSwGenericAxisParams()
        assert len(reparsed_params) == 1
        assert reparsed_params[0].getSwGenericAxisParamTypeRef().getValue() == "/axis/types/fixed/shift"
        assert reparsed_params[0].getVfs()[0].getValue() == 1.5

    def test_write_sw_axis_generic_empty_params_omits_wrapper(self):
        """No parameters means no SW-GENERIC-AXIS-PARAMS wrapper in the output XML."""
        generic = SwAxisGeneric()
        axis_type_ref = RefType()
        axis_type_ref.setDest("SW-AXIS-TYPE")
        axis_type_ref.setValue("/axis/types/fixed")
        generic.setSwAxisTypeRef(axis_type_ref)

        parent = ET.Element("PARENT")
        ARXMLWriter().setSwAxisGeneric(parent, generic)

        generic_el = parent.find("SW-AXIS-GENERIC")
        assert generic_el is not None
        assert [child.tag for child in generic_el] == ["SW-AXIS-TYPE-REF"]
        assert generic_el.find("SW-GENERIC-AXIS-PARAMS") is None

        wrapped = ET.fromstring("<WRAP xmlns='http://autosar.org/schema/r4.0'>%s</WRAP>" % ET.tostring(generic_el, encoding="unicode"))
        reparsed = ARXMLParser().getSwAxisGeneric(wrapped[0])
        assert reparsed.getSwAxisTypeRef().getValue() == "/axis/types/fixed"
        assert reparsed.getSwGenericAxisParams() == []
