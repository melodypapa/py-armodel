import inspect

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import PositiveInteger, RefType, TimeValue
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore.CoreCommunication import (
    ContainedIPduProps,
    ContainerIPdu,
    ContainerIPduHeaderTypeEnum,
    ContainerIPduTriggerEnum,
    RxAcceptContainedIPduEnum,
)

CLASS_NOTE = "Allows to collect several IPdus in one ContainerIPdu based on the headerType. Tags: atp.recommendedPackage=Pdus"


class TestContainerIPdu:
    """Test cases for ContainerIPdu (Table 6.35, p.354)."""

    def test_initialization_defaults(self):
        ipdu = ContainerIPdu(None, "container")
        assert ipdu.getContainedIPduTriggeringProps() == []
        assert ipdu.getContainedPduTriggeringRefs() == []
        assert ipdu.getContainerTimeout() is None
        assert ipdu.getContainerTrigger() is None
        assert ipdu.getHeaderType() is None
        assert ipdu.getMinimumRxContainerQueueSize() is None
        assert ipdu.getMinimumTxContainerQueueSize() is None
        assert ipdu.getRxAcceptContainedIPdu() is None
        assert ipdu.getThresholdSize() is None
        assert ipdu.getUnusedBitPattern() is None

    def test_add_contained_ipdu_triggering_props(self):
        ipdu = ContainerIPdu(None, "container")
        props = ContainedIPduProps()
        assert ipdu.addContainedIPduTriggeringProps(props) is ipdu
        assert ipdu.getContainedIPduTriggeringProps() == [props]
        assert ipdu.addContainedIPduTriggeringProps(None) is ipdu
        assert ipdu.getContainedIPduTriggeringProps() == [props]

    def test_add_contained_pdu_triggering_refs(self):
        ipdu = ContainerIPdu(None, "container")
        ref = RefType()
        ref.setValue("/Cluster/PduTriggering")
        assert ipdu.addContainedPduTriggeringRef(ref) is ipdu
        assert ipdu.getContainedPduTriggeringRefs() == [ref]
        assert ipdu.addContainedPduTriggeringRef(None) is ipdu
        assert ipdu.getContainedPduTriggeringRefs() == [ref]

    def test_get_set_round_trip_and_none_noop(self):
        ipdu = ContainerIPdu(None, "container")

        timeout = TimeValue()
        timeout.setValue("0.01")
        assert ipdu.setContainerTimeout(timeout) is ipdu
        assert ipdu.getContainerTimeout() is timeout
        ipdu.setContainerTimeout(None)
        assert ipdu.getContainerTimeout() is timeout

        trigger = ContainerIPduTriggerEnum()
        trigger.setValue(ContainerIPduTriggerEnum.FIRST_CONTAINED_TRIGGER)
        assert ipdu.setContainerTrigger(trigger) is ipdu
        assert ipdu.getContainerTrigger() is trigger
        ipdu.setContainerTrigger(None)
        assert ipdu.getContainerTrigger() is trigger

        header_type = ContainerIPduHeaderTypeEnum()
        header_type.setValue(ContainerIPduHeaderTypeEnum.SHORT_HEADER)
        assert ipdu.setHeaderType(header_type) is ipdu
        assert ipdu.getHeaderType() is header_type

        rx_size = PositiveInteger()
        rx_size.setValue("4")
        assert ipdu.setMinimumRxContainerQueueSize(rx_size) is ipdu
        assert ipdu.getMinimumRxContainerQueueSize() is rx_size

        tx_size = PositiveInteger()
        tx_size.setValue("8")
        assert ipdu.setMinimumTxContainerQueueSize(tx_size) is ipdu
        assert ipdu.getMinimumTxContainerQueueSize() is tx_size

        rx_accept = RxAcceptContainedIPduEnum()
        rx_accept.setValue(RxAcceptContainedIPduEnum.ACCEPT_CONFIGURED)
        assert ipdu.setRxAcceptContainedIPdu(rx_accept) is ipdu
        assert ipdu.getRxAcceptContainedIPdu() is rx_accept

        threshold = PositiveInteger()
        threshold.setValue("100")
        assert ipdu.setThresholdSize(threshold) is ipdu
        assert ipdu.getThresholdSize() is threshold

        pattern = PositiveInteger()
        pattern.setValue("255")
        assert ipdu.setUnusedBitPattern(pattern) is ipdu
        assert ipdu.getUnusedBitPattern() is pattern

    def test_class_docstring_note(self):
        assert inspect.cleandoc(ContainerIPdu.__doc__) == CLASS_NOTE
