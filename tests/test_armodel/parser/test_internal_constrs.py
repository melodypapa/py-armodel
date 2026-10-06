"""Reader tests for InternalConstrs (Swc TPS Table 5.85, p.407).

readInternalConstrs populates the model via the mutators. Element order per the XSD
group INTERNAL-CONSTRS (AUTOSAR_00052.xsd): LOWER-LIMIT (sequenceOffset 20),
UPPER-LIMIT (30), SCALE-CONSTRS (40), MAX-GRADIENT (50), MAX-DIFF (60), MONOTONY (70).
MONOTONY carries the UPPERCASE XSD wire token (AR:MONOTONY-ENUM--SIMPLE), decoded to
the camelCase MonotonyEnum member via MONOTONY_XML_MAP; LIMIT children carry the
INTERVAL-TYPE attribute token decoded by getChildLimitElement. InternalConstrs has no
unit row (that is the PhysConstrs differentiator).
"""

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import IntervalTypeEnum, Limit, MonotonyEnum, Numerical
from armodel.models.M2.MSR.AsamHdo.Constraints.GlobalConstraints import DataConstrRule, InternalConstrs
from tests.test_armodel.parser._helpers import _snip


class TestInternalConstrsReader:
    def test_read_full_field_values(self, parser):
        element = _snip(
            """
            <INTERNAL-CONSTRS>
                <LOWER-LIMIT INTERVAL-TYPE="CLOSED">-32768</LOWER-LIMIT>
                <UPPER-LIMIT INTERVAL-TYPE="OPEN">32767</UPPER-LIMIT>
                <SCALE-CONSTRS>
                    <SCALE-CONSTR>
                        <SHORT-LABEL>s1</SHORT-LABEL>
                        <LOWER-LIMIT>5.0</LOWER-LIMIT>
                        <UPPER-LIMIT>50.0</UPPER-LIMIT>
                    </SCALE-CONSTR>
                </SCALE-CONSTRS>
                <MAX-GRADIENT>1.5</MAX-GRADIENT>
                <MAX-DIFF>0.5</MAX-DIFF>
                <MONOTONY>STRICTLY-INCREASING</MONOTONY>
            </INTERNAL-CONSTRS>
            """,
        )
        rule = DataConstrRule()
        parser.readInternalConstrs(element, rule)

        constrs = rule.getInternalConstrs()
        assert constrs is not None
        assert isinstance(constrs, InternalConstrs)
        lower = constrs.getLowerLimit()
        assert isinstance(lower, Limit)
        assert lower.getValue() == "-32768"
        assert isinstance(lower.getIntervalType(), IntervalTypeEnum)
        assert lower.getIntervalType().getValue() == IntervalTypeEnum.CLOSED
        upper = constrs.getUpperLimit()
        assert isinstance(upper, Limit)
        assert upper.getValue() == "32767"
        assert upper.getIntervalType().getValue() == IntervalTypeEnum.OPEN
        assert isinstance(constrs.getMaxGradient(), Numerical)
        assert constrs.getMaxGradient().getValue() == 1.5
        assert isinstance(constrs.getMaxDiff(), Numerical)
        assert constrs.getMaxDiff().getValue() == 0.5
        assert isinstance(constrs.getMonotony(), MonotonyEnum)
        assert constrs.getMonotony().getValue() == MonotonyEnum.STRICTLY_INCREASING
        scales = constrs.getScaleConstrs()
        assert len(scales) == 1
        assert scales[0].getShortLabel().getValue() == "s1"
        assert scales[0].getLowerLimit().getValue() == "5.0"
        assert scales[0].getUpperLimit().getValue() == "50.0"

    def test_read_partial_rest_is_none(self, parser):
        element = _snip(
            """
            <INTERNAL-CONSTRS>
                <MAX-GRADIENT>1.5</MAX-GRADIENT>
            </INTERNAL-CONSTRS>
            """,
        )
        rule = DataConstrRule()
        parser.readInternalConstrs(element, rule)

        constrs = rule.getInternalConstrs()
        assert constrs is not None
        assert constrs.getMaxGradient().getValue() == 1.5
        assert constrs.getLowerLimit() is None
        assert constrs.getUpperLimit() is None
        assert constrs.getMaxDiff() is None
        assert constrs.getMonotony() is None
        assert constrs.getScaleConstrs() == []

    def test_read_absent_element_sets_none(self, parser):
        element = _snip("<CONSTR-LEVEL>3</CONSTR-LEVEL>")
        rule = DataConstrRule()
        parser.readInternalConstrs(element, rule)
        assert rule.getInternalConstrs() is None
