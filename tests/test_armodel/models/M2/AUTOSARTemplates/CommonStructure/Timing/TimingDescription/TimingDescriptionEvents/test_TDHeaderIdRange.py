from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Integer,
)
from armodel.models.M2.AUTOSARTemplates.CommonStructure.Timing.TimingDescription.TimingDescriptionEvents.TDEventCom import (
    TDHeaderIdRange,
)


class TestTDHeaderIdRange:
    def test_base_is_ar_object(self):
        assert issubclass(TDHeaderIdRange, ARObject)

    def test_defaults(self):
        rng = TDHeaderIdRange()
        assert rng.getMinHeaderId() is None
        assert rng.getMaxHeaderId() is None

    def test_set_get_min_header_id(self):
        rng = TDHeaderIdRange()
        value = Integer().setValue("5")
        assert rng.setMinHeaderId(value) is rng
        assert rng.getMinHeaderId() is value
        assert rng.getMinHeaderId().getValue() == 5

    def test_set_get_max_header_id(self):
        rng = TDHeaderIdRange()
        value = Integer().setValue("10")
        assert rng.setMaxHeaderId(value) is rng
        assert rng.getMaxHeaderId() is value
        assert rng.getMaxHeaderId().getValue() == 10

    def test_set_none_noop(self):
        rng = TDHeaderIdRange()
        value = Integer().setValue("5")
        rng.setMinHeaderId(value)
        rng.setMinHeaderId(None)
        assert rng.getMinHeaderId() is value
