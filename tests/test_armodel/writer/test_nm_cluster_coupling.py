"""Writer round-trip tests for NmClusterCoupling (Table 6.305, p.676).

NmClusterCoupling is abstract with zero attribute rows (XSD group
NM-CLUSTER-COUPLING carries only VARIATION-POINT), so coverage runs through
its concrete subclasses via the NM-CLUSTER-COUPLINGS wrapper dispatch.
"""

import xml.etree.ElementTree as ET

import pytest

from armodel.models import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import Boolean, RefType
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.NetworkManagement import (
    CanNmClusterCoupling,
    NmConfig,
    UdpNmClusterCoupling,
)
from armodel.writer.arxml_writer import ARXMLWriter

NS = "http://autosar.org/schema/r4.0"


@pytest.fixture(autouse=True)
def reset_autosar():
    AUTOSAR.getInstance().new()
    yield
    AUTOSAR.getInstance().new()


class MockParent(ARObject):
    def __init__(self):
        super().__init__()


def _ref(dest, value):
    ref = RefType()
    ref.setDest(dest)
    ref.setValue(value)
    return ref


def _bool(value):
    boolean = Boolean()
    boolean.setValue(value)
    return boolean


def _new_config():
    config = NmConfig(MockParent(), "NmConfig")

    can_coupling = CanNmClusterCoupling()
    can_coupling.addCoupledClusterRef(_ref("CAN-CLUSTER", "/Clusters/Can1"))
    can_coupling.setNmBusloadReductionEnabled(_bool(True))
    can_coupling.setNmImmediateRestartEnabled(_bool(False))
    config.addNmClusterCouplings(can_coupling)

    udp_coupling = UdpNmClusterCoupling()
    udp_coupling.addCoupledClusterRef(_ref("ETHERNET-CLUSTER", "/Clusters/Eth1"))
    udp_coupling.setNmImmediateRestartEnabled(_bool(True))
    config.addNmClusterCouplings(udp_coupling)
    return config


class TestWriteNmClusterCoupling:
    def test_can_nm_cluster_coupling_element_order(self):
        parent = ET.Element("PARENT")
        ARXMLWriter().writeNmConfigNmClusterCouplings(parent, _new_config())
        wrapper = parent.find("NM-CLUSTER-COUPLINGS")
        assert wrapper is not None
        can_coupling = wrapper.find("CAN-NM-CLUSTER-COUPLING")
        assert can_coupling is not None
        ref = can_coupling.find("COUPLED-CLUSTER-REFS/COUPLED-CLUSTER-REF")
        assert ref.text == "/Clusters/Can1"
        assert ref.attrib["DEST"] == "CAN-CLUSTER"
        assert can_coupling.find("NM-BUSLOAD-REDUCTION-ENABLED").text == "true"
        assert can_coupling.find("NM-IMMEDIATE-RESTART-ENABLED").text == "false"
        assert [child.tag for child in can_coupling] == ["COUPLED-CLUSTER-REFS", "NM-BUSLOAD-REDUCTION-ENABLED", "NM-IMMEDIATE-RESTART-ENABLED"]

    def test_udp_nm_cluster_coupling_element_order(self):
        parent = ET.Element("PARENT")
        ARXMLWriter().writeNmConfigNmClusterCouplings(parent, _new_config())
        wrapper = parent.find("NM-CLUSTER-COUPLINGS")
        udp_coupling = wrapper.find("UDP-NM-CLUSTER-COUPLING")
        assert udp_coupling is not None
        ref = udp_coupling.find("COUPLED-CLUSTER-REFS/COUPLED-CLUSTER-REF")
        assert ref.text == "/Clusters/Eth1"
        assert ref.attrib["DEST"] == "ETHERNET-CLUSTER"
        assert [child.tag for child in udp_coupling] == ["COUPLED-CLUSTER-REFS", "NM-IMMEDIATE-RESTART-ENABLED"]

    def test_write_empty_couplings_omits_wrapper(self):
        parent = ET.Element("PARENT")
        config = NmConfig(MockParent(), "NmConfig")
        ARXMLWriter().writeNmConfigNmClusterCouplings(parent, config)
        assert parent.find("NM-CLUSTER-COUPLINGS") is None
