"""Reader tests for SwCalprmAxis (Swc TPS Table 5.47, p.352).

getSwCalprmAxis populates the model via the five mutators. Element order per the
XSD group SW-CALPRM-AXIS (AUTOSAR_00052.xsd): SW-AXIS-INDEX (sequenceOffset 20),
CATEGORY (30), SW-AXIS-GROUPED|SW-AXIS-INDIVIDUAL (40), SW-CALIBRATION-ACCESS (90),
DISPLAY-FORMAT (100). CATEGORY and SW-CALIBRATION-ACCESS carry the UPPERCASE XSD
wire tokens (CALPRM-AXIS-CATEGORY-ENUM--SIMPLE / SW-CALIBRATION-ACCESS-ENUM--SIMPLE),
mapped to the model members via CALPRM_AXIS_CATEGORY_XML_MAP and
SW_CALIBRATION_ACCESS_XML_MAP.
"""

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import DisplayFormatString, MonotonyEnum
from armodel.models.M2.MSR.DataDictionary.Axis import SwAxisGrouped, SwAxisIndividual
from armodel.models.M2.MSR.DataDictionary.CalibrationParameter import CalprmAxisCategoryEnum
from armodel.models.M2.MSR.DataDictionary.DataDefProperties import SwCalibrationAccessEnum
from armodel.models.M2.MSR.DataDictionary.RecordLayout import AxisIndexType
from tests.test_armodel.parser._helpers import _snip


class TestSwCalprmAxisReader:
    def test_read_full_field_values(self, parser):
        element = _snip(
            """
            <SW-AXIS-INDEX>1</SW-AXIS-INDEX>
            <CATEGORY>STD_AXIS</CATEGORY>
            <SW-AXIS-GROUPED>
                <SHARED-AXIS-TYPE-REF DEST="SW-AXIS-TYPE">/axis/types/shared</SHARED-AXIS-TYPE-REF>
            </SW-AXIS-GROUPED>
            <SW-CALIBRATION-ACCESS>READ-ONLY</SW-CALIBRATION-ACCESS>
            <DISPLAY-FORMAT>%.3f</DISPLAY-FORMAT>
            """,
            root_tag="SW-CALPRM-AXIS",
        )
        axis = parser.getSwCalprmAxis(element)
        assert axis is not None
        assert isinstance(axis.getSwAxisIndex(), AxisIndexType)
        assert axis.getSwAxisIndex().getValue() == "1"
        assert isinstance(axis.getCategory(), CalprmAxisCategoryEnum)
        assert axis.getCategory().getValue() == "stdAxis"
        assert isinstance(axis.getSwCalprmAxisTypeProps(), SwAxisGrouped)
        assert axis.getSwCalprmAxisTypeProps().getSharedAxisTypeRef().getValue() == "/axis/types/shared"
        assert isinstance(axis.getSwCalibrationAccess(), SwCalibrationAccessEnum)
        assert axis.getSwCalibrationAccess().getValue() == "readOnly"
        assert isinstance(axis.getDisplayFormat(), DisplayFormatString)
        assert axis.getDisplayFormat().getValue() == "%.3f"

    def test_read_category_token_maps_to_member_value(self, parser):
        """The UPPERCASE XSD wire token maps to the camelCase CalprmAxisCategoryEnum member value."""
        element = _snip(
            """
            <SW-AXIS-INDEX>1</SW-AXIS-INDEX>
            <CATEGORY>COM_AXIS</CATEGORY>
            """,
            root_tag="SW-CALPRM-AXIS",
        )
        axis = parser.getSwCalprmAxis(element)
        assert isinstance(axis.getCategory(), CalprmAxisCategoryEnum)
        assert axis.getCategory().getValue() == "comAxis"

    def test_read_individual_choice_variant(self, parser):
        element = _snip(
            """
            <SW-AXIS-INDEX>2</SW-AXIS-INDEX>
            <SW-AXIS-INDIVIDUAL>
                <SW-MAX-AXIS-POINTS>10</SW-MAX-AXIS-POINTS>
            </SW-AXIS-INDIVIDUAL>
            """,
            root_tag="SW-CALPRM-AXIS",
        )
        axis = parser.getSwCalprmAxis(element)
        props = axis.getSwCalprmAxisTypeProps()
        assert isinstance(props, SwAxisIndividual)
        assert props.getSwMaxAxisPoints().getValue() == 10
        assert axis.getCategory() is None
        assert axis.getSwCalibrationAccess() is None
        assert axis.getDisplayFormat() is None

    def test_read_empty_element_yields_unset_fields(self, parser):
        element = _snip(
            "<SW-CALPRM-AXIS/>",
            root_tag="SW-CALPRM-AXIS",
        )
        axis = parser.getSwCalprmAxis(element)
        assert axis is not None
        assert axis.getSwAxisIndex() is None
        assert axis.getCategory() is None
        assert axis.getSwCalprmAxisTypeProps() is None
        assert axis.getSwCalibrationAccess() is None
        assert axis.getDisplayFormat() is None


class TestSwCalprmAxisTypePropsReader:
    """Reader tests for the abstract SwCalprmAxisTypeProps element group (SWCT Table 5.49, p.353).

    The XSD element group SW-CALPRM-AXIS-TYPE-PROPS (AUTOSAR_00052.xsd L114844) carries
    MAX-GRADIENT (AR:FLOAT) then MONOTONY (AR:MONOTONY-ENUM--SIMPLE, UPPERCASE wire
    tokens); both concrete choice branches (SW-AXIS-GROUPED L114493 / SW-AXIS-INDIVIDUAL
    L114607) inline the group ahead of their own elements. The abstract class owns the
    reusable readSwCalprmAxisTypeProps helper called by both branches (Rule 0001.7);
    MONOTONY materializes a typed MonotonyEnum via MONOTONY_XML_MAP.
    """

    def test_read_helper_populates_base_attrs(self, parser):
        """readSwCalprmAxisTypeProps populates maxGradient (Float) and monotony (MonotonyEnum) from the XSD wire forms."""
        element = _snip(
            "<MAX-GRADIENT>0.75</MAX-GRADIENT><MONOTONY>MONOTONOUS</MONOTONY>",
            root_tag="SW-AXIS-GROUPED",
        )
        props = SwAxisGrouped()
        parser.readSwCalprmAxisTypeProps(element, props)
        assert props.getMaxGradient() is not None
        assert props.getMaxGradient().getValue() == 0.75
        assert isinstance(props.getMonotony(), MonotonyEnum)
        assert props.getMonotony().getValue() == "monotonous"

    def test_read_base_attrs_via_grouped_choice(self, parser):
        """The SW-AXIS-GROUPED choice branch reads the base group attrs (polymorphic dispatch)."""
        element = _snip(
            "<SW-AXIS-GROUPED><MAX-GRADIENT>1.5</MAX-GRADIENT><MONOTONY>STRICTLY-INCREASING</MONOTONY>"
            "<SHARED-AXIS-TYPE-REF DEST='SW-AXIS-TYPE'>/axis/types/shared</SHARED-AXIS-TYPE-REF></SW-AXIS-GROUPED>",
            root_tag="SW-CALPRM-AXIS",
        )
        axis = parser.getSwCalprmAxis(element)
        props = axis.getSwCalprmAxisTypeProps()
        assert isinstance(props, SwAxisGrouped)
        assert props.getMaxGradient().getValue() == 1.5
        assert isinstance(props.getMonotony(), MonotonyEnum)
        assert props.getMonotony().getValue() == "strictlyIncreasing"
        assert props.getSharedAxisTypeRef().getValue() == "/axis/types/shared"

    def test_read_base_attrs_via_individual_choice(self, parser):
        """The SW-AXIS-INDIVIDUAL choice branch reads the base group attrs (polymorphic dispatch)."""
        element = _snip(
            "<SW-AXIS-INDIVIDUAL><MAX-GRADIENT>2.5</MAX-GRADIENT><MONOTONY>DECREASING</MONOTONY>" "<SW-MAX-AXIS-POINTS>10</SW-MAX-AXIS-POINTS></SW-AXIS-INDIVIDUAL>",
            root_tag="SW-CALPRM-AXIS",
        )
        axis = parser.getSwCalprmAxis(element)
        props = axis.getSwCalprmAxisTypeProps()
        assert isinstance(props, SwAxisIndividual)
        assert props.getMaxGradient().getValue() == 2.5
        assert isinstance(props.getMonotony(), MonotonyEnum)
        assert props.getMonotony().getValue() == "decreasing"

    def test_read_empty_type_props_yields_unset_base_attrs(self, parser):
        element = _snip(
            "<SW-AXIS-GROUPED/>",
            root_tag="SW-CALPRM-AXIS",
        )
        axis = parser.getSwCalprmAxis(element)
        props = axis.getSwCalprmAxisTypeProps()
        assert isinstance(props, SwAxisGrouped)
        assert props.getMaxGradient() is None
        assert props.getMonotony() is None


class TestSwAxisGenericReader:
    """Reader tests for SwAxisGeneric (Swc TPS Table 5.51, p.355).

    getSwAxisGeneric populates the model via setSwAxisTypeRef / addSwGenericAxisParam.
    Element order per the XSD group SW-AXIS-GENERIC (AUTOSAR_00052.xsd L114396):
    SW-AXIS-TYPE-REF (sequenceOffset 20), then the SW-GENERIC-AXIS-PARAMS wrapper (40)
    whose SW-GENERIC-AXIS-PARAM items carry SW-GENERIC-AXIS-PARAM-TYPE-REF + VF children.
    """

    def test_read_sw_axis_generic_full_field_values(self, parser):
        element = _snip(
            "<SW-AXIS-TYPE-REF DEST='SW-AXIS-TYPE'>/axis/types/fixed</SW-AXIS-TYPE-REF>"
            "<SW-GENERIC-AXIS-PARAMS>"
            "<SW-GENERIC-AXIS-PARAM>"
            "<SW-GENERIC-AXIS-PARAM-TYPE-REF DEST='SW-GENERIC-AXIS-PARAM-TYPE'>/axis/types/fixed/shift</SW-GENERIC-AXIS-PARAM-TYPE-REF>"
            "<VF>1.5</VF>"
            "</SW-GENERIC-AXIS-PARAM>"
            "<SW-GENERIC-AXIS-PARAM>"
            "<SW-GENERIC-AXIS-PARAM-TYPE-REF DEST='SW-GENERIC-AXIS-PARAM-TYPE'>/axis/types/fixed/offset</SW-GENERIC-AXIS-PARAM-TYPE-REF>"
            "<VF>2.5</VF>"
            "<VF>3.5</VF>"
            "</SW-GENERIC-AXIS-PARAM>"
            "</SW-GENERIC-AXIS-PARAMS>",
            root_tag="SW-AXIS-GENERIC",
        )
        generic = parser.getSwAxisGeneric(element)
        assert generic is not None
        assert generic.getSwAxisTypeRef() is not None
        assert generic.getSwAxisTypeRef().getValue() == "/axis/types/fixed"
        params = generic.getSwGenericAxisParams()
        assert len(params) == 2
        assert params[0].getSwGenericAxisParamTypeRef().getValue() == "/axis/types/fixed/shift"
        assert params[0].getVfs()[0].getValue() == 1.5
        assert params[1].getSwGenericAxisParamTypeRef().getValue() == "/axis/types/fixed/offset"
        assert [vf.getValue() for vf in params[1].getVfs()] == [2.5, 3.5]

    def test_read_sw_axis_generic_empty_params_wrapper_yields_empty_list(self, parser):
        """An empty SW-GENERIC-AXIS-PARAMS wrapper parses to an empty list, not None."""
        element = _snip(
            "<SW-AXIS-TYPE-REF DEST='SW-AXIS-TYPE'>/axis/types/fixed</SW-AXIS-TYPE-REF>" "<SW-GENERIC-AXIS-PARAMS/>",
            root_tag="SW-AXIS-GENERIC",
        )
        generic = parser.getSwAxisGeneric(element)
        assert generic.getSwAxisTypeRef().getValue() == "/axis/types/fixed"
        assert generic.getSwGenericAxisParams() == []

    def test_read_sw_axis_generic_minimal_defaults(self, parser):
        element = _snip("", root_tag="SW-AXIS-GENERIC")
        generic = parser.getSwAxisGeneric(element)
        assert generic is not None
        assert generic.getSwAxisTypeRef() is None
        assert generic.getSwGenericAxisParams() == []
