"""Unit tests for CanXlProps (AdaptivePlatform CAN-XL-PROPS, AUTOSAR_00052.xsd).

CanXlProps is a standalone ARElement consumed by
EthernetCommunicationConnector.canXlPropsRefs / apApplicationEndpoint. It carries
the machine specific CAN XL attributes: canBaudrate, canConfig, canFdBaudrate,
canFdConfig, canXlBaudrate, canXlConfig and canXlConfigReqs.
"""

import pytest

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import PositiveInteger
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Can.CanTopology import (
    CanControllerConfiguration,
    CanControllerFdConfiguration,
    CanControllerXlConfiguration,
    CanControllerXlConfigurationRequirements,
    CanXlProps,
)


@pytest.fixture
def props():
    return CanXlProps(None, "CanXlProps_1")


class TestCanXlProps:
    def test_initialization(self, props):
        assert props.getCanBaudrate() is None
        assert props.getCanConfig() is None
        assert props.getCanFdBaudrate() is None
        assert props.getCanFdConfig() is None
        assert props.getCanXlBaudrate() is None
        assert props.getCanXlConfig() is None
        assert props.getCanXlConfigReqs() is None

    def _baudrate(self, value):
        v = PositiveInteger()
        v.setValue(str(value))
        return v

    def test_get_set_can_baudrate(self, props):
        v = self._baudrate(500000)
        assert props.setCanBaudrate(v) is props
        assert props.getCanBaudrate() is v
        assert props.setCanBaudrate(None) is props
        assert props.getCanBaudrate() is v

    def test_get_set_can_config(self, props):
        config = CanControllerConfiguration()
        assert props.setCanConfig(config) is props
        assert props.getCanConfig() is config
        assert props.setCanConfig(None) is props
        assert props.getCanConfig() is config

    def test_get_set_can_fd_baudrate(self, props):
        v = self._baudrate(2000000)
        assert props.setCanFdBaudrate(v) is props
        assert props.getCanFdBaudrate() is v
        assert props.setCanFdBaudrate(None) is props
        assert props.getCanFdBaudrate() is v

    def test_get_set_can_fd_config(self, props):
        config = CanControllerFdConfiguration()
        assert props.setCanFdConfig(config) is props
        assert props.getCanFdConfig() is config
        assert props.setCanFdConfig(None) is props
        assert props.getCanFdConfig() is config

    def test_get_set_can_xl_baudrate(self, props):
        v = self._baudrate(10000000)
        assert props.setCanXlBaudrate(v) is props
        assert props.getCanXlBaudrate() is v
        assert props.setCanXlBaudrate(None) is props
        assert props.getCanXlBaudrate() is v

    def test_get_set_can_xl_config(self, props):
        config = CanControllerXlConfiguration()
        assert props.setCanXlConfig(config) is props
        assert props.getCanXlConfig() is config
        assert props.setCanXlConfig(None) is props
        assert props.getCanXlConfig() is config

    def test_get_set_can_xl_config_reqs(self, props):
        reqs = CanControllerXlConfigurationRequirements()
        assert props.setCanXlConfigReqs(reqs) is props
        assert props.getCanXlConfigReqs() is reqs
        assert props.setCanXlConfigReqs(None) is props
        assert props.getCanXlConfigReqs() is reqs
