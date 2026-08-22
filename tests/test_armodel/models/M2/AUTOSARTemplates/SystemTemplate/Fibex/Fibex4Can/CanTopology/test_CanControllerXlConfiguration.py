from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import Boolean, PositiveInteger
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Can.CanTopology import CanControllerXlConfiguration


class TestCanControllerXlConfiguration:
    """Tests for CanControllerXlConfiguration (Table 3.18, R23-11)."""

    def test_initialization(self):
        config = CanControllerXlConfiguration()
        assert isinstance(config, ARObject)
        assert config.getErrorSignalingEnabled() is None
        assert config.getPropSeg() is None
        assert config.getPwmL() is None
        assert config.getPwmO() is None
        assert config.getPwmS() is None
        assert config.getSspOffset() is None
        assert config.getSyncJumpWidth() is None
        assert config.getTimeSeg1() is None
        assert config.getTimeSeg2() is None
        assert config.getTrcvPwmModeEnabled() is None

    def test_get_set_errorSignalingEnabled(self):
        config = CanControllerXlConfiguration()
        value = Boolean().setValue("true")
        result = config.setErrorSignalingEnabled(value)
        assert config.getErrorSignalingEnabled() is value
        assert config.getErrorSignalingEnabled().getValue() is True
        assert result == config
        assert config.setErrorSignalingEnabled(None) == config
        assert config.getErrorSignalingEnabled() is value

    def test_get_set_propSeg(self):
        config = CanControllerXlConfiguration()
        value = PositiveInteger().setValue("4")
        result = config.setPropSeg(value)
        assert config.getPropSeg() is value
        assert config.getPropSeg().getValue() == 4
        assert result == config
        assert config.setPropSeg(None) == config
        assert config.getPropSeg() is value

    def test_get_set_pwmL(self):
        config = CanControllerXlConfiguration()
        value = PositiveInteger().setValue("5")
        result = config.setPwmL(value)
        assert config.getPwmL() is value
        assert config.getPwmL().getValue() == 5
        assert result == config
        assert config.setPwmL(None) == config
        assert config.getPwmL() is value

    def test_get_set_pwmO(self):
        config = CanControllerXlConfiguration()
        value = PositiveInteger().setValue("6")
        result = config.setPwmO(value)
        assert config.getPwmO() is value
        assert config.getPwmO().getValue() == 6
        assert result == config
        assert config.setPwmO(None) == config
        assert config.getPwmO() is value

    def test_get_set_pwmS(self):
        config = CanControllerXlConfiguration()
        value = PositiveInteger().setValue("7")
        result = config.setPwmS(value)
        assert config.getPwmS() is value
        assert config.getPwmS().getValue() == 7
        assert result == config
        assert config.setPwmS(None) == config
        assert config.getPwmS() is value

    def test_get_set_sspOffset(self):
        config = CanControllerXlConfiguration()
        value = PositiveInteger().setValue("8")
        result = config.setSspOffset(value)
        assert config.getSspOffset() is value
        assert config.getSspOffset().getValue() == 8
        assert result == config
        assert config.setSspOffset(None) == config
        assert config.getSspOffset() is value

    def test_get_set_syncJumpWidth(self):
        config = CanControllerXlConfiguration()
        value = PositiveInteger().setValue("1")
        result = config.setSyncJumpWidth(value)
        assert config.getSyncJumpWidth() is value
        assert config.getSyncJumpWidth().getValue() == 1
        assert result == config
        assert config.setSyncJumpWidth(None) == config
        assert config.getSyncJumpWidth() is value

    def test_get_set_timeSeg1(self):
        config = CanControllerXlConfiguration()
        value = PositiveInteger().setValue("13")
        result = config.setTimeSeg1(value)
        assert config.getTimeSeg1() is value
        assert config.getTimeSeg1().getValue() == 13
        assert result == config
        assert config.setTimeSeg1(None) == config
        assert config.getTimeSeg1() is value

    def test_get_set_timeSeg2(self):
        config = CanControllerXlConfiguration()
        value = PositiveInteger().setValue("2")
        result = config.setTimeSeg2(value)
        assert config.getTimeSeg2() is value
        assert config.getTimeSeg2().getValue() == 2
        assert result == config
        assert config.setTimeSeg2(None) == config
        assert config.getTimeSeg2() is value

    def test_get_set_trcvPwmModeEnabled(self):
        config = CanControllerXlConfiguration()
        value = Boolean().setValue("true")
        result = config.setTrcvPwmModeEnabled(value)
        assert config.getTrcvPwmModeEnabled() is value
        assert config.getTrcvPwmModeEnabled().getValue() is True
        assert result == config
        assert config.setTrcvPwmModeEnabled(None) == config
        assert config.getTrcvPwmModeEnabled() is value
