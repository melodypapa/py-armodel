"""Reader tests for SwCalprmAxis (Swc TPS Table 5.47, p.352).

getSwCalprmAxis populates the model via the five mutators. Element order per the
XSD group SW-CALPRM-AXIS (AUTOSAR_00052.xsd): SW-AXIS-INDEX (sequenceOffset 20),
CATEGORY (30), SW-AXIS-GROUPED|SW-AXIS-INDIVIDUAL (40), SW-CALIBRATION-ACCESS (90),
DISPLAY-FORMAT (100). SW-CALIBRATION-ACCESS carries the UPPERCASE XSD wire token,
mapped to the SwCalibrationAccessEnum member via SW_CALIBRATION_ACCESS_XML_MAP.
"""

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import DisplayFormatString
from armodel.models.M2.MSR.DataDictionary.Axis import SwAxisGrouped, SwAxisIndividual
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
        assert axis.getCategory().getValue() == "STD_AXIS"
        assert isinstance(axis.getSwCalprmAxisTypeProps(), SwAxisGrouped)
        assert axis.getSwCalprmAxisTypeProps().getSharedAxisTypeRef().getValue() == "/axis/types/shared"
        assert isinstance(axis.getSwCalibrationAccess(), SwCalibrationAccessEnum)
        assert axis.getSwCalibrationAccess().getValue() == "readOnly"
        assert isinstance(axis.getDisplayFormat(), DisplayFormatString)
        assert axis.getDisplayFormat().getValue() == "%.3f"

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
