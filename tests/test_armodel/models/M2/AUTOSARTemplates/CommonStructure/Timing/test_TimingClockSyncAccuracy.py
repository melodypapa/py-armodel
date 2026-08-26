from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.CommonStructure.Timing.TimingClock import TimingClockSyncAccuracy
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.MultidimensionalTime import (
    MultidimensionalTime,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    CseCodeType,
    Integer,
    RefType,
)


class TestTimingClockSyncAccuracy:
    def _parent(self):
        document = AUTOSAR.getInstance()
        document.clear()
        document.setARRelease("R23-11")
        return document.createARPackage("AUTOSAR")

    def _mdt(self, cse_code: str, factor: str) -> MultidimensionalTime:
        mdt = MultidimensionalTime()
        mdt.setCseCode(CseCodeType().setValue(cse_code))
        mdt.setCseCodeFactor(Integer().setValue(factor))
        return mdt

    def test_initialization_defaults(self):
        accuracy = TimingClockSyncAccuracy(self._parent(), "Sync1")
        assert accuracy.getShortName() == "Sync1"
        assert accuracy.getAccuracy() is None
        assert accuracy.getLowerRef() is None
        assert accuracy.getUpperRef() is None

    def test_get_set_accuracy(self):
        accuracy = TimingClockSyncAccuracy(self._parent(), "Sync1")
        value = self._mdt("0", "10")
        assert accuracy.setAccuracy(value) is accuracy
        result = accuracy.getAccuracy()
        assert isinstance(result, MultidimensionalTime)
        assert result.getCseCode().getValue() == "0"
        assert result.getCseCodeFactor().getValue() == 10

    def test_get_set_lower_ref(self):
        accuracy = TimingClockSyncAccuracy(self._parent(), "Sync1")
        ref = RefType().setValue("/AUTOSAR/TargetClock").setDest("TDLET-ZONE-CLOCK")
        assert accuracy.setLowerRef(ref) is accuracy
        assert accuracy.getLowerRef() is ref
        assert accuracy.getLowerRef().getValue() == "/AUTOSAR/TargetClock"
        assert accuracy.getLowerRef().getDest() == "TDLET-ZONE-CLOCK"

    def test_get_set_upper_ref(self):
        accuracy = TimingClockSyncAccuracy(self._parent(), "Sync1")
        ref = RefType().setValue("/AUTOSAR/SourceClock").setDest("TIMING-CLOCK")
        assert accuracy.setUpperRef(ref) is accuracy
        assert accuracy.getUpperRef() is ref
        assert accuracy.getUpperRef().getValue() == "/AUTOSAR/SourceClock"
        assert accuracy.getUpperRef().getDest() == "TIMING-CLOCK"

    def test_set_none_is_no_op(self):
        accuracy = TimingClockSyncAccuracy(self._parent(), "Sync1")
        value = self._mdt("0", "10")
        lower_ref = RefType().setValue("/AUTOSAR/TargetClock").setDest("TDLET-ZONE-CLOCK")
        upper_ref = RefType().setValue("/AUTOSAR/SourceClock").setDest("TIMING-CLOCK")
        accuracy.setAccuracy(value)
        accuracy.setLowerRef(lower_ref)
        accuracy.setUpperRef(upper_ref)
        accuracy.setAccuracy(None)
        accuracy.setLowerRef(None)
        accuracy.setUpperRef(None)
        assert accuracy.getAccuracy() is value
        assert accuracy.getLowerRef() is lower_ref
        assert accuracy.getUpperRef() is upper_ref
