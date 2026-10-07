"""Reader tests for SwComponentDocumentation (Swc TPS Table 12.1, p.698).

readSwComponentDocumentationElement populates the model via the createXxx
factories in XSD group order (AUTOSAR_00052.xsd line 114911): the seven
predefined CHAPTER slots, the free CHAPTER list, then VARIATION-POINT — with
the inherited AR:AR-OBJECT S/T attributes read through readARObject (Rule 0025:
base helper called exactly once).
"""

from tests.test_armodel.parser._helpers import _snip


class TestSwComponentDocumentationReader:
    def test_read_own_group_field_values(self, parser):
        element = _snip(
            """
            <SW-FEATURE-DEF>
                <SHORT-NAME>FeatureDef</SHORT-NAME>
            </SW-FEATURE-DEF>
            <SW-FEATURE-DESC>
                <SHORT-NAME>FeatureDesc</SHORT-NAME>
            </SW-FEATURE-DESC>
            <SW-TEST-DESC>
                <SHORT-NAME>TestDesc</SHORT-NAME>
            </SW-TEST-DESC>
            <SW-CALIBRATION-NOTES>
                <SHORT-NAME>CalibrationNotes</SHORT-NAME>
            </SW-CALIBRATION-NOTES>
            <SW-MAINTENANCE-NOTES>
                <SHORT-NAME>MaintenanceNotes</SHORT-NAME>
            </SW-MAINTENANCE-NOTES>
            <SW-DIAGNOSTICS-NOTES>
                <SHORT-NAME>DiagnosticsNotes</SHORT-NAME>
            </SW-DIAGNOSTICS-NOTES>
            <SW-CARB-DOC>
                <SHORT-NAME>CarbDoc</SHORT-NAME>
            </SW-CARB-DOC>
            <CHAPTER>
                <SHORT-NAME>FreeChapter1</SHORT-NAME>
            </CHAPTER>
            <CHAPTER>
                <SHORT-NAME>FreeChapter2</SHORT-NAME>
            </CHAPTER>
            <VARIATION-POINT>
                <SHORT-LABEL>vpLabel</SHORT-LABEL>
            </VARIATION-POINT>
            """,
            root_tag="SW-COMPONENT-DOCUMENTATION",
            attrs=' S="chk-1" T="2009-07-23T13:38:00Z"',
        )
        documentation = parser.readSwComponentDocumentationElement(element)

        assert documentation.getChecksum() is not None
        assert documentation.getChecksum().getValue() == "chk-1"
        assert documentation.getTimestamp() is not None
        assert documentation.getTimestamp().getValue() == "2009-07-23T13:38:00Z"

        assert documentation.getSwFeatureDef().getShortName() == "FeatureDef"
        assert documentation.getSwFeatureDesc().getShortName() == "FeatureDesc"
        assert documentation.getSwTestDesc().getShortName() == "TestDesc"
        assert documentation.getSwCalibrationNotes().getShortName() == "CalibrationNotes"
        assert documentation.getSwMaintenanceNotes().getShortName() == "MaintenanceNotes"
        assert documentation.getSwDiagnosticsNotes().getShortName() == "DiagnosticsNotes"
        assert documentation.getSwCarbDoc().getShortName() == "CarbDoc"

        chapters = documentation.getChapters()
        assert len(chapters) == 2
        assert chapters[0].getShortName() == "FreeChapter1"
        assert chapters[1].getShortName() == "FreeChapter2"

        variation_point = documentation.getVariationPoint()
        assert variation_point is not None
        assert variation_point.getShortLabel().getValue() == "vpLabel"

    def test_read_empty_documentation(self, parser):
        element = _snip("", root_tag="SW-COMPONENT-DOCUMENTATION")
        documentation = parser.readSwComponentDocumentationElement(element)

        assert documentation.getChapters() == []
        assert documentation.getSwFeatureDef() is None
        assert documentation.getSwCarbDoc() is None
        assert documentation.getVariationPoint() is None
