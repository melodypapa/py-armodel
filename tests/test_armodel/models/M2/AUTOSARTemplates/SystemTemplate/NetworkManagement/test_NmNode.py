import pytest

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import Boolean, Integer, PositiveInteger, RefType
from armodel.models.M2.AUTOSARTemplates.GenericStructure.VariantHandling import VariationPoint
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.NetworkManagement import (
    CanNmNode,
    NmCoordinatorRoleEnum,
    NmNode,
)


class MockParent(ARObject):
    def __init__(self):
        super().__init__()


def _bool(value):
    boolean = Boolean()
    boolean.setValue(value)
    return boolean


def _integer(value):
    integer = Integer()
    integer.setValue(value)
    return integer


def _positive_integer(value):
    positive_integer = PositiveInteger()
    positive_integer.setValue(value)
    return positive_integer


def _ref(dest, value):
    ref = RefType()
    ref.setDest(dest)
    ref.setValue(value)
    return ref


def _new_node():
    return CanNmNode(MockParent(), "CanNmNode")


class TestNmNode:
    def test_abstract(self):
        """
        NmNode is abstract and cannot be instantiated directly.
        """
        with pytest.raises(TypeError):
            NmNode(MockParent(), "NmNode")

    def test_initialization(self):
        """
        All Table 6.303 fields default to None (0..1) or [] (0..*).
        """
        node = _new_node()
        assert node.getControllerRef() is None
        assert node.getNmCoordCluster() is None
        assert node.getNmCoordinatorRole() is None
        assert node.getNmIfEcuRef() is None
        assert node.getNmNodeId() is None
        assert node.getNmPassiveModeEnabled() is None
        assert node.getRxNmPduRefs() == []
        assert node.getTxNmPduRefs() == []

    def test_get_set_controller_ref(self):
        node = _new_node()
        value = _ref("COMMUNICATION-CONTROLLER", "/Topology/Can1/Controller")
        assert node.setControllerRef(value) is node
        assert node.getControllerRef() is value
        node.setControllerRef(None)
        assert node.getControllerRef() is value

    def test_get_set_nm_coord_cluster(self):
        node = _new_node()
        value = _positive_integer("2")
        assert node.setNmCoordCluster(value) is node
        assert node.getNmCoordCluster() is value
        assert node.getNmCoordCluster().getValue() == 2
        node.setNmCoordCluster(None)
        assert node.getNmCoordCluster() is value

    def test_get_set_nm_coordinator_role(self):
        node = _new_node()
        value = NmCoordinatorRoleEnum()
        value.setValue(NmCoordinatorRoleEnum.ACTIVE)
        assert node.setNmCoordinatorRole(value) is node
        assert node.getNmCoordinatorRole() is value
        assert node.getNmCoordinatorRole().getValue() == NmCoordinatorRoleEnum.ACTIVE
        node.setNmCoordinatorRole(None)
        assert node.getNmCoordinatorRole() is value

    def test_get_set_nm_if_ecu_ref(self):
        node = _new_node()
        value = _ref("NM-ECU", "/Ecus/Can1/NmEcu")
        assert node.setNmIfEcuRef(value) is node
        assert node.getNmIfEcuRef() is value
        node.setNmIfEcuRef(None)
        assert node.getNmIfEcuRef() is value

    def test_get_set_nm_node_id(self):
        node = _new_node()
        value = _integer(16)
        assert node.setNmNodeId(value) is node
        assert node.getNmNodeId() is value
        node.setNmNodeId(None)
        assert node.getNmNodeId() is value

    def test_get_set_nm_passive_mode_enabled(self):
        node = _new_node()
        value = _bool(True)
        assert node.setNmPassiveModeEnabled(value) is node
        assert node.getNmPassiveModeEnabled() is value
        node.setNmPassiveModeEnabled(None)
        assert node.getNmPassiveModeEnabled() is value

    def test_add_get_rx_nm_pdu_refs(self):
        node = _new_node()
        ref = _ref("NM-PDU", "/Pdus/NmPdu1")
        assert node.addRxNmPduRef(ref) is node
        assert node.getRxNmPduRefs() == [ref]
        node.addRxNmPduRef(None)
        assert node.getRxNmPduRefs() == [ref]

    def test_add_get_tx_nm_pdu_refs(self):
        node = _new_node()
        ref = _ref("NM-PDU", "/Pdus/NmPdu2")
        assert node.addTxNmPduRef(ref) is node
        assert node.getTxNmPduRefs() == [ref]
        node.addTxNmPduRef(None)
        assert node.getTxNmPduRefs() == [ref]

    def test_variation_point_capability(self):
        """
        NmNode is VP-capable (XSD VARIATION-POINT applicable for NmCluster.nmNode).
        """
        node = _new_node()
        assert node.getVariationPoint() is None
        vp = VariationPoint()
        node.setVariationPoint(vp)
        assert node.getVariationPoint() is vp
