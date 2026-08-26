"""
This module contains tests for the ConfidenceInterval class in the
AUTOSAR CommonStructure.Timing.TimingConstraint.EventTriggeringConstraint module.
"""

from armodel.models.M2.AUTOSARTemplates.CommonStructure.Timing.TimingConstraint.EventTriggeringConstraint import (
    ConfidenceInterval,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.MultidimensionalTime import (
    MultidimensionalTime,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    CseCodeType,
    Float,
    Integer,
)


class TestConfidenceInterval:
    """
    Test class for ConfidenceInterval functionality.
    """

    def _mdt(self, cse_code: str, factor: str) -> MultidimensionalTime:
        mdt = MultidimensionalTime()
        mdt.setCseCode(CseCodeType().setValue(cse_code))
        mdt.setCseCodeFactor(Integer().setValue(factor))
        return mdt

    def test_initialization(self):
        obj = ConfidenceInterval()
        assert isinstance(obj, ConfidenceInterval)
        assert obj.getLowerBound() is None
        assert obj.getPropability() is None
        assert obj.getUpperBound() is None

    def test_get_set_lower_bound(self):
        obj = ConfidenceInterval()

        lower_bound = self._mdt("0", "50")
        assert obj.setLowerBound(lower_bound) is obj
        assert obj.getLowerBound() is lower_bound
        assert obj.getLowerBound().getCseCodeFactor().getValue() == 50

    def test_get_set_propability(self):
        obj = ConfidenceInterval()

        propability = Float().setValue("0.95")
        assert obj.setPropability(propability) is obj
        assert obj.getPropability() is propability
        assert obj.getPropability().getValue() == 0.95

    def test_get_set_upper_bound(self):
        obj = ConfidenceInterval()

        upper_bound = self._mdt("0", "100")
        assert obj.setUpperBound(upper_bound) is obj
        assert obj.getUpperBound() is upper_bound
        assert obj.getUpperBound().getCseCode().getValue() == "0"

    def test_set_none_no_op(self):
        obj = ConfidenceInterval()
        lower_bound = self._mdt("0", "50")
        propability = Float().setValue("0.95")
        upper_bound = self._mdt("0", "100")

        obj.setLowerBound(lower_bound)
        obj.setPropability(propability)
        obj.setUpperBound(upper_bound)
        obj.setLowerBound(None)
        obj.setPropability(None)
        obj.setUpperBound(None)
        assert obj.getLowerBound() is lower_bound
        assert obj.getPropability() is propability
        assert obj.getUpperBound() is upper_bound
