from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import Boolean, Float, Integer, PositiveInteger, TimeValue
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Can.CanTopology import CanControllerXlConfigurationRequirements


class TestCanControllerXlConfigurationRequirements:
    """Tests for CanControllerXlConfigurationRequirements (Table 3.19, R23-11)."""

    def test_initialization(self):
        req = CanControllerXlConfigurationRequirements()
        assert isinstance(req, ARObject)
        assert req.getErrorSignalingEnabled() is None
        assert req.getMaxNumberOfTimeQuantaPerBit() is None
        assert req.getMaxPwmL() is None
        assert req.getMaxPwmO() is None
        assert req.getMaxPwmS() is None
        assert req.getMaxSamplePoint() is None
        assert req.getMaxSyncJumpWidth() is None
        assert req.getMaxTrcvDelayCompensationOffset() is None
        assert req.getMinNumberOfTimeQuantaPerBit() is None
        assert req.getMinPwmL() is None
        assert req.getMinPwmO() is None
        assert req.getMinPwmS() is None
        assert req.getMinSamplePoint() is None
        assert req.getMinSyncJumpWidth() is None
        assert req.getMinTrcvDelayCompensationOffset() is None
        assert req.getTrcvPwmModeEnabled() is None

    def test_get_set_all(self):
        req = CanControllerXlConfigurationRequirements()
        values = {
            "errorSignalingEnabled": Boolean().setValue("true"),
            "maxNumberOfTimeQuantaPerBit": Integer().setValue("32"),
            "maxPwmL": PositiveInteger().setValue("5"),
            "maxPwmO": PositiveInteger().setValue("6"),
            "maxPwmS": PositiveInteger().setValue("7"),
            "maxSamplePoint": Float().setValue("0.8"),
            "maxSyncJumpWidth": Float().setValue("0.2"),
            "maxTrcvDelayCompensationOffset": TimeValue().setValue("0.001"),
            "minNumberOfTimeQuantaPerBit": Integer().setValue("16"),
            "minPwmL": PositiveInteger().setValue("3"),
            "minPwmO": PositiveInteger().setValue("4"),
            "minPwmS": PositiveInteger().setValue("5"),
            "minSamplePoint": Float().setValue("0.7"),
            "minSyncJumpWidth": Float().setValue("0.1"),
            "minTrcvDelayCompensationOffset": TimeValue().setValue("0.0005"),
            "trcvPwmModeEnabled": Boolean().setValue("true"),
        }
        setters = {
            "errorSignalingEnabled": req.setErrorSignalingEnabled,
            "maxNumberOfTimeQuantaPerBit": req.setMaxNumberOfTimeQuantaPerBit,
            "maxPwmL": req.setMaxPwmL,
            "maxPwmO": req.setMaxPwmO,
            "maxPwmS": req.setMaxPwmS,
            "maxSamplePoint": req.setMaxSamplePoint,
            "maxSyncJumpWidth": req.setMaxSyncJumpWidth,
            "maxTrcvDelayCompensationOffset": req.setMaxTrcvDelayCompensationOffset,
            "minNumberOfTimeQuantaPerBit": req.setMinNumberOfTimeQuantaPerBit,
            "minPwmL": req.setMinPwmL,
            "minPwmO": req.setMinPwmO,
            "minPwmS": req.setMinPwmS,
            "minSamplePoint": req.setMinSamplePoint,
            "minSyncJumpWidth": req.setMinSyncJumpWidth,
            "minTrcvDelayCompensationOffset": req.setMinTrcvDelayCompensationOffset,
            "trcvPwmModeEnabled": req.setTrcvPwmModeEnabled,
        }
        getters = {
            "errorSignalingEnabled": req.getErrorSignalingEnabled,
            "maxNumberOfTimeQuantaPerBit": req.getMaxNumberOfTimeQuantaPerBit,
            "maxPwmL": req.getMaxPwmL,
            "maxPwmO": req.getMaxPwmO,
            "maxPwmS": req.getMaxPwmS,
            "maxSamplePoint": req.getMaxSamplePoint,
            "maxSyncJumpWidth": req.getMaxSyncJumpWidth,
            "maxTrcvDelayCompensationOffset": req.getMaxTrcvDelayCompensationOffset,
            "minNumberOfTimeQuantaPerBit": req.getMinNumberOfTimeQuantaPerBit,
            "minPwmL": req.getMinPwmL,
            "minPwmO": req.getMinPwmO,
            "minPwmS": req.getMinPwmS,
            "minSamplePoint": req.getMinSamplePoint,
            "minSyncJumpWidth": req.getMinSyncJumpWidth,
            "minTrcvDelayCompensationOffset": req.getMinTrcvDelayCompensationOffset,
            "trcvPwmModeEnabled": req.getTrcvPwmModeEnabled,
        }
        for name, value in values.items():
            result = setters[name](value)
            assert result == req
            assert getters[name]() is value

        for name in values:
            assert setters[name](None) == req
            assert getters[name]() is values[name]

        assert req.getErrorSignalingEnabled().getValue() is True
        assert req.getMaxNumberOfTimeQuantaPerBit().getValue() == 32
        assert req.getMaxPwmL().getValue() == 5
        assert req.getMaxPwmO().getValue() == 6
        assert req.getMaxPwmS().getValue() == 7
        assert req.getMaxSamplePoint().getValue() == 0.8
        assert req.getMaxSyncJumpWidth().getValue() == 0.2
        assert req.getMaxTrcvDelayCompensationOffset().getValue() == 0.001
        assert req.getMinNumberOfTimeQuantaPerBit().getValue() == 16
        assert req.getMinPwmL().getValue() == 3
        assert req.getMinPwmO().getValue() == 4
        assert req.getMinPwmS().getValue() == 5
        assert req.getMinSamplePoint().getValue() == 0.7
        assert req.getMinSyncJumpWidth().getValue() == 0.1
        assert req.getMinTrcvDelayCompensationOffset().getValue() == 0.0005
        assert req.getTrcvPwmModeEnabled().getValue() is True
