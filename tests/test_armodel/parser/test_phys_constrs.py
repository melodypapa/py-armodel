"""Reader tests for PhysConstrs (Swc TPS Table 5.84, p.406).

readPhysConstrs populates the model via the mutators. Element order per the XSD group
PHYS-CONSTRS (AUTOSAR_00052.xsd): LOWER-LIMIT (sequenceOffset 20), UPPER-LIMIT (30),
SCALE-CONSTRS (40), MAX-GRADIENT (50), MAX-DIFF (60), MONOTONY (70), UNIT-REF (80).
MONOTONY carries the UPPERCASE XSD wire token (AR:MONOTONY-ENUM--SIMPLE), decoded to
the camelCase MonotonyEnum member via MONOTONY_XML_MAP; LIMIT children carry the
INTERVAL-TYPE attribute token decoded by getChildLimitElement.
"""

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import IntervalTypeEnum, Limit, MonotonyEnum, Numerical, RefType
from armodel.models.M2.MSR.AsamHdo.Constraints.GlobalConstraints import DataConstrRule, PhysConstrs
from tests.test_armodel.parser._helpers import _snip


class TestPhysConstrsReader:
    def test_read_full_field_values(self, parser):
        element = _snip(
            """
            <PHYS-CONSTRS>
                <LOWER-LIMIT INTERVAL-TYPE="CLOSED">0</LOWER-LIMIT>
                <UPPER-LIMIT INTERVAL-TYPE="OPEN">65535</UPPER-LIMIT>
                <SCALE-CONSTRS>
                    <SCALE-CONSTR>
                        <SHORT-LABEL>s1</SHORT-LABEL>
                        <LOWER-LIMIT>5.0</LOWER-LIMIT>
                        <UPPER-LIMIT>50.0</UPPER-LIMIT>
                    </SCALE-CONSTR>
                </SCALE-CONSTRS>
                <MAX-GRADIENT>1.5</MAX-GRADIENT>
                <MAX-DIFF>0.5</MAX-DIFF>
                <MONOTONY>INCREASING</MONOTONY>
                <UNIT-REF DEST="UNIT">/units/c</UNIT-REF>
            </PHYS-CONSTRS>
            """,
        )
        rule = DataConstrRule()
        parser.readPhysConstrs(element, rule)

        constrs = rule.getPhysConstrs()
        assert constrs is not None
        assert isinstance(constrs, PhysConstrs)
        lower = constrs.getLowerLimit()
        assert isinstance(lower, Limit)
        assert lower.getValue() == "0"
        assert isinstance(lower.getIntervalType(), IntervalTypeEnum)
        assert lower.getIntervalType().getValue() == "closed"
        upper = constrs.getUpperLimit()
        assert isinstance(upper, Limit)
        assert upper.getValue() == "65535"
        assert upper.getIntervalType().getValue() == "open"
        assert isinstance(constrs.getMaxGradient(), Numerical)
        assert constrs.getMaxGradient().getValue() == 1.5
        assert isinstance(constrs.getMaxDiff(), Numerical)
        assert constrs.getMaxDiff().getValue() == 0.5
        assert isinstance(constrs.getMonotony(), MonotonyEnum)
        assert constrs.getMonotony().getValue() == "increasing"
        scales = constrs.getScaleConstrs()
        assert len(scales) == 1
        assert scales[0].getShortLabel().getValue() == "s1"
        assert scales[0].getLowerLimit().getValue() == "5.0"
        assert scales[0].getUpperLimit().getValue() == "50.0"
        assert isinstance(constrs.getUnitRef(), RefType)
        assert constrs.getUnitRef().getValue() == "/units/c"
        assert constrs.getUnitRef().getDest() == "UNIT"

    def test_read_partial_rest_is_none(self, parser):
        element = _snip(
            """
            <PHYS-CONSTRS>
                <MAX-DIFF>0.5</MAX-DIFF>
            </PHYS-CONSTRS>
            """,
        )
        rule = DataConstrRule()
        parser.readPhysConstrs(element, rule)

        constrs = rule.getPhysConstrs()
        assert constrs is not None
        assert constrs.getMaxDiff().getValue() == 0.5
        assert constrs.getLowerLimit() is None
        assert constrs.getUpperLimit() is None
        assert constrs.getMaxGradient() is None
        assert constrs.getMonotony() is None
        assert constrs.getScaleConstrs() == []
        assert constrs.getUnitRef() is None

    def test_read_absent_element_sets_none(self, parser):
        element = _snip("<CONSTR-LEVEL>3</CONSTR-LEVEL>")
        rule = DataConstrRule()
        parser.readPhysConstrs(element, rule)
        assert rule.getPhysConstrs() is None
