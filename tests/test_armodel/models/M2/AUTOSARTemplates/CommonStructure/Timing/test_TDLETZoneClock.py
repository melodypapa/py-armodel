from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.CommonStructure.Timing.TimingClock import TDLETZoneClock, TimingClock
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.MultidimensionalTime import (
    MultidimensionalTime,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    CseCodeType,
    Integer,
)


class TestTDLETZoneClock:
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

    def test_base_is_timing_clock(self):
        assert issubclass(TDLETZoneClock, TimingClock)

    def test_initialization_defaults(self):
        clock = TDLETZoneClock(self._parent(), "Zone1")
        assert clock.getShortName() == "Zone1"
        assert clock.getAccuracyExt() is None
        assert clock.getAccuracyInt() is None

    def test_get_set_accuracy_ext(self):
        clock = TDLETZoneClock(self._parent(), "Zone1")
        accuracy = self._mdt("0", "30")
        assert clock.setAccuracyExt(accuracy) is clock
        ext = clock.getAccuracyExt()
        assert isinstance(ext, MultidimensionalTime)
        assert ext.getCseCode().getValue() == "0"
        assert ext.getCseCodeFactor().getValue() == 30

    def test_get_set_accuracy_int(self):
        clock = TDLETZoneClock(self._parent(), "Zone1")
        accuracy = self._mdt("0", "50")
        assert clock.setAccuracyInt(accuracy) is clock
        internal = clock.getAccuracyInt()
        assert isinstance(internal, MultidimensionalTime)
        assert internal.getCseCode().getValue() == "0"
        assert internal.getCseCodeFactor().getValue() == 50

    def test_set_accuracy_none_is_no_op(self):
        clock = TDLETZoneClock(self._parent(), "Zone1")
        ext_accuracy = self._mdt("0", "30")
        int_accuracy = self._mdt("0", "50")
        clock.setAccuracyExt(ext_accuracy)
        clock.setAccuracyInt(int_accuracy)
        clock.setAccuracyExt(None)
        clock.setAccuracyInt(None)
        assert clock.getAccuracyExt() is ext_accuracy
        assert clock.getAccuracyInt() is int_accuracy
