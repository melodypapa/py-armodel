"""
This module contains tests for the GlobalTimeDomain class in the
AUTOSAR GenericStructure.GeneralTemplateClasses.ARPackage module.

Spec: AUTOSAR_CP_TPS_SystemTemplate.pdf, Table 9.1, p.859
"""

import inspect
import typing

import pytest

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import (
    AbstractGlobalTimeDomainProps,
    CanGlobalTimeDomainProps,
    GlobalTimeCorrectionProps,
    NetworkSegmentIdentification,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ARPackage import (
    ARElement,
    GlobalTimeDomain,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable import (
    GlobalTimeCanMaster,
    GlobalTimeCanSlave,
    GlobalTimeEthMaster,
    GlobalTimeEthSlave,
    GlobalTimeFrMaster,
    GlobalTimeFrSlave,
    GlobalTimeGateway,
    GlobalTimeMaster,
    GlobalTimeSlave,
    UserDefinedGlobalTimeMaster,
    UserDefinedGlobalTimeSlave,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    PositiveInteger,
    RefType,
    TimeValue,
)


class TestGlobalTimeDomain:
    """
    Test class for GlobalTimeDomain functionality.

    Spec: AUTOSAR_CP_TPS_SystemTemplate.pdf, Table 9.1, p.859
    """

    CLASS_NOTE = "This represents the ability to define a global time domain. Tags: atp.recommendedPackage=GlobalTimeDomains"
    DEBOUNCE_TIME_NOTE = "Defines the minimum amount of time between two time sync messages are transmitted."
    DOMAIN_ID_NOTE = "This represents the ID of the GlobalTimeDomain used in the network messages sent on behalf of global time management."
    GATEWAY_NOTE = "A GlobalTimeGateway may exist in the context of a GlobalTimeDomain to actively update the global time information as it is routed from one GlobalTimeDomain to another. Stereotypes: atpSplitable; atpVariation Tags: atp.Splitkey=gateway.shortName, gateway.variation Point.shortLabel vh.latestBindingTime=postBuild"
    GLOBAL_TIME_CORRECTION_PROPS_NOTE = "Defintion of attributes for rate and offset correction."
    GLOBAL_TIME_DOMAIN_PROPERTY_NOTE = "Additional properties of the GlobalTimeDomain. Stereotypes: atpSplitable; atpVariation Tags: atp.Splitkey=globalTimeDomainProperty, globalTime DomainProperty.variationPoint.shortLabel vh.latestBindingTime=postBuild"
    GLOBAL_TIME_MASTER_NOTE = "This represents the single master of a GlobalTime Domain. A GlobalTimeDomain may have no GlobalTime Domain.master, e.g. when it gets its time from a GPS receiver. Stereotypes: atpSplitable; atpVariation Tags: atp.Splitkey=globalTimeMaster.shortName, globalTime Master.variationPoint.shortLabel vh.latestBindingTime=postBuild"
    GLOBAL_TIME_SUB_DOMAIN_NOTE = "By this means it is possible to create a hierarchy of sub Domains where one global time domain can declare one or more other global time domains as its subDomains. Stereotypes: atpSplitable; atpVariation Tags: atp.Splitkey=globalTimeSubDomain.globalTimeDomain, globalTimeSubDomain.variationPoint.shortLabel vh.latestBindingTime=postBuild"
    NETWORK_SEGMENT_ID_NOTE = "Defines the numerical identification of a GlobalTime sub domain."
    OFFSET_TIME_DOMAIN_NOTE = (
        "Reference to a synchronized time domain this offset time domain is based on. The reference source is the offset time domain. The reference target is the synchronized time domain."
    )
    PDU_TRIGGERING_NOTE = "This PduTriggering will be taken to transmit the global time information from a GlobalTimeMaster to a the associated GlobalTimeSlaves. Stereotypes: atpSplitable; atpVariation Tags: atp.Splitkey=pduTriggering.pduTriggering, pdu Triggering.variationPoint.shortLabel vh.latestBindingTime=postBuild"
    SLAVE_NOTE = "This represents the collections of slaves of the Global TimeDomain. A GlobalTimeDomain may have no Global TimeDomain.slaves, e.g. when it propagates its time directly to sub domains. Stereotypes: atpSplitable; atpVariation Tags: atp.Splitkey=slave.shortName, slave.variationPoint.short Label vh.latestBindingTime=postBuild"
    SYNC_LOSS_TIMEOUT_NOTE = "This attribute describes the timeout for the situation that the time synchronization gets lost in the scope of the time domain."

    def _create_domain(self) -> GlobalTimeDomain:
        return GlobalTimeDomain(None, "Domain1")

    def test_is_arelement_subclass(self):
        """
        Test that GlobalTimeDomain derives from ARElement per the Table 9.1 Base row.
        """
        assert issubclass(GlobalTimeDomain, ARElement)

    def test_class_docstring_is_spec_note_verbatim(self):
        """
        Test that the class docstring is the spec Note verbatim.
        """
        assert inspect.cleandoc(GlobalTimeDomain.__doc__) == self.CLASS_NOTE

    def test_init_has_no_docstring(self):
        """
        Test that __init__ carries no docstring.
        """
        assert GlobalTimeDomain.__init__.__doc__ is None

    def test_member_order_follows_spec_rows(self):
        """
        Test that the accessors follow the Table 9.1 displayed row order
        (creates/adders first on aggregation rows, getter first on 0..1 rows).
        """
        methods = [name for name, value in GlobalTimeDomain.__dict__.items() if callable(value) and not name.startswith("_")]
        assert methods == [
            "getDebounceTime",
            "setDebounceTime",
            "getDomainId",
            "setDomainId",
            "createGlobalTimeGateway",
            "getGateways",
            "getGlobalTimeCorrectionProps",
            "setGlobalTimeCorrectionProps",
            "getGlobalTimeDomainProperty",
            "setGlobalTimeDomainProperty",
            "createGlobalTimeCanMaster",
            "createGlobalTimeEthMaster",
            "createGlobalTimeFrMaster",
            "createUserDefinedGlobalTimeMaster",
            "getGlobalTimeMaster",
            "addGlobalTimeSubDomainRef",
            "getGlobalTimeSubDomainRefs",
            "getNetworkSegmentId",
            "setNetworkSegmentId",
            "getOffsetTimeDomainRef",
            "setOffsetTimeDomainRef",
            "getPduTriggeringRef",
            "setPduTriggeringRef",
            "createGlobalTimeCanSlave",
            "createGlobalTimeEthSlave",
            "createGlobalTimeFrSlave",
            "createUserDefinedGlobalTimeSlave",
            "getSlaves",
            "getSyncLossTimeout",
            "setSyncLossTimeout",
        ]

    def test_initialization_defaults(self):
        """
        Test that the instance initializes all attributes to their defaults.
        """
        obj = self._create_domain()

        assert obj.getShortName() == "Domain1"
        assert obj.getDebounceTime() is None
        assert obj.getDomainId() is None
        assert obj.getGateways() == []
        assert obj.getGlobalTimeCorrectionProps() is None
        assert obj.getGlobalTimeDomainProperty() is None
        assert obj.getGlobalTimeMaster() is None
        assert obj.getGlobalTimeSubDomainRefs() == []
        assert obj.getNetworkSegmentId() is None
        assert obj.getOffsetTimeDomainRef() is None
        assert obj.getPduTriggeringRef() is None
        assert obj.getSlaves() == []
        assert obj.getSyncLossTimeout() is None

    def test_annotations_are_optional_typed(self):
        """
        Test that the accessors carry the spec types.
        """
        hints = typing.get_type_hints(GlobalTimeDomain.getDebounceTime)
        assert hints.get("return") == typing.Optional[TimeValue]
        hints = typing.get_type_hints(GlobalTimeDomain.setDebounceTime)
        assert hints.get("value") == typing.Optional[TimeValue]
        assert hints.get("return") is GlobalTimeDomain

        hints = typing.get_type_hints(GlobalTimeDomain.getDomainId)
        assert hints.get("return") == typing.Optional[PositiveInteger]

        hints = typing.get_type_hints(GlobalTimeDomain.createGlobalTimeGateway)
        assert hints.get("short_name") is str
        assert hints.get("return") is GlobalTimeGateway
        hints = typing.get_type_hints(GlobalTimeDomain.getGateways)
        assert hints.get("return") == typing.List[GlobalTimeGateway]

        hints = typing.get_type_hints(GlobalTimeDomain.getGlobalTimeCorrectionProps)
        assert hints.get("return") == typing.Optional[GlobalTimeCorrectionProps]

        hints = typing.get_type_hints(GlobalTimeDomain.getGlobalTimeDomainProperty)
        assert hints.get("return") == typing.Optional[AbstractGlobalTimeDomainProps]

        hints = typing.get_type_hints(GlobalTimeDomain.getGlobalTimeMaster)
        assert hints.get("return") == typing.Optional[GlobalTimeMaster]

        hints = typing.get_type_hints(GlobalTimeDomain.addGlobalTimeSubDomainRef)
        assert hints.get("value") == typing.Optional[RefType]
        assert hints.get("return") is GlobalTimeDomain
        hints = typing.get_type_hints(GlobalTimeDomain.getGlobalTimeSubDomainRefs)
        assert hints.get("return") == typing.List[RefType]

        hints = typing.get_type_hints(GlobalTimeDomain.getNetworkSegmentId)
        assert hints.get("return") == typing.Optional[NetworkSegmentIdentification]

        hints = typing.get_type_hints(GlobalTimeDomain.getOffsetTimeDomainRef)
        assert hints.get("return") == typing.Optional[RefType]

        hints = typing.get_type_hints(GlobalTimeDomain.getPduTriggeringRef)
        assert hints.get("return") == typing.Optional[RefType]

        hints = typing.get_type_hints(GlobalTimeDomain.getSlaves)
        assert hints.get("return") == typing.List[GlobalTimeSlave]

        hints = typing.get_type_hints(GlobalTimeDomain.getSyncLossTimeout)
        assert hints.get("return") == typing.Optional[TimeValue]

    def test_method_docstrings_are_spec_notes_verbatim(self):
        """
        Test that the accessor docstrings are the spec Notes verbatim
        (setters/adders carry the None no-op tail).
        """
        assert inspect.cleandoc(GlobalTimeDomain.getDebounceTime.__doc__) == self.DEBOUNCE_TIME_NOTE
        assert inspect.cleandoc(GlobalTimeDomain.setDebounceTime.__doc__) == (self.DEBOUNCE_TIME_NOTE + "\n\nA None value is a no-op and does not overwrite an existing debounceTime.")
        assert inspect.cleandoc(GlobalTimeDomain.getDomainId.__doc__) == self.DOMAIN_ID_NOTE
        assert inspect.cleandoc(GlobalTimeDomain.setDomainId.__doc__) == (self.DOMAIN_ID_NOTE + "\n\nA None value is a no-op and does not overwrite an existing domainId.")
        assert inspect.cleandoc(GlobalTimeDomain.createGlobalTimeGateway.__doc__) == self.GATEWAY_NOTE
        assert inspect.cleandoc(GlobalTimeDomain.getGateways.__doc__) == self.GATEWAY_NOTE
        assert inspect.cleandoc(GlobalTimeDomain.getGlobalTimeCorrectionProps.__doc__) == self.GLOBAL_TIME_CORRECTION_PROPS_NOTE
        assert inspect.cleandoc(GlobalTimeDomain.setGlobalTimeCorrectionProps.__doc__) == (
            self.GLOBAL_TIME_CORRECTION_PROPS_NOTE + "\n\nA None value is a no-op and does not overwrite an existing globalTimeCorrectionProps."
        )
        assert inspect.cleandoc(GlobalTimeDomain.getGlobalTimeDomainProperty.__doc__) == self.GLOBAL_TIME_DOMAIN_PROPERTY_NOTE
        assert inspect.cleandoc(GlobalTimeDomain.setGlobalTimeDomainProperty.__doc__) == (
            self.GLOBAL_TIME_DOMAIN_PROPERTY_NOTE + "\n\nA None value is a no-op and does not overwrite an existing globalTimeDomainProperty."
        )
        assert inspect.cleandoc(GlobalTimeDomain.createGlobalTimeCanMaster.__doc__) == self.GLOBAL_TIME_MASTER_NOTE
        assert inspect.cleandoc(GlobalTimeDomain.createGlobalTimeEthMaster.__doc__) == self.GLOBAL_TIME_MASTER_NOTE
        assert inspect.cleandoc(GlobalTimeDomain.createGlobalTimeFrMaster.__doc__) == self.GLOBAL_TIME_MASTER_NOTE
        assert inspect.cleandoc(GlobalTimeDomain.createUserDefinedGlobalTimeMaster.__doc__) == self.GLOBAL_TIME_MASTER_NOTE
        assert inspect.cleandoc(GlobalTimeDomain.getGlobalTimeMaster.__doc__) == self.GLOBAL_TIME_MASTER_NOTE
        assert inspect.cleandoc(GlobalTimeDomain.addGlobalTimeSubDomainRef.__doc__) == (
            self.GLOBAL_TIME_SUB_DOMAIN_NOTE + "\n\nA None value is a no-op and does not append to globalTimeSubDomainRefs."
        )
        assert inspect.cleandoc(GlobalTimeDomain.getGlobalTimeSubDomainRefs.__doc__) == self.GLOBAL_TIME_SUB_DOMAIN_NOTE
        assert inspect.cleandoc(GlobalTimeDomain.getNetworkSegmentId.__doc__) == self.NETWORK_SEGMENT_ID_NOTE
        assert inspect.cleandoc(GlobalTimeDomain.setNetworkSegmentId.__doc__) == (self.NETWORK_SEGMENT_ID_NOTE + "\n\nA None value is a no-op and does not overwrite an existing networkSegmentId.")
        assert inspect.cleandoc(GlobalTimeDomain.getOffsetTimeDomainRef.__doc__) == self.OFFSET_TIME_DOMAIN_NOTE
        assert inspect.cleandoc(GlobalTimeDomain.setOffsetTimeDomainRef.__doc__) == (
            self.OFFSET_TIME_DOMAIN_NOTE + "\n\nA None value is a no-op and does not overwrite an existing offsetTimeDomainRef."
        )
        assert inspect.cleandoc(GlobalTimeDomain.getPduTriggeringRef.__doc__) == self.PDU_TRIGGERING_NOTE
        assert inspect.cleandoc(GlobalTimeDomain.setPduTriggeringRef.__doc__) == (self.PDU_TRIGGERING_NOTE + "\n\nA None value is a no-op and does not overwrite an existing pduTriggeringRef.")
        assert inspect.cleandoc(GlobalTimeDomain.createGlobalTimeCanSlave.__doc__) == self.SLAVE_NOTE
        assert inspect.cleandoc(GlobalTimeDomain.createGlobalTimeEthSlave.__doc__) == self.SLAVE_NOTE
        assert inspect.cleandoc(GlobalTimeDomain.createGlobalTimeFrSlave.__doc__) == self.SLAVE_NOTE
        assert inspect.cleandoc(GlobalTimeDomain.createUserDefinedGlobalTimeSlave.__doc__) == self.SLAVE_NOTE
        assert inspect.cleandoc(GlobalTimeDomain.getSlaves.__doc__) == self.SLAVE_NOTE
        assert inspect.cleandoc(GlobalTimeDomain.getSyncLossTimeout.__doc__) == self.SYNC_LOSS_TIMEOUT_NOTE
        assert inspect.cleandoc(GlobalTimeDomain.setSyncLossTimeout.__doc__) == (self.SYNC_LOSS_TIMEOUT_NOTE + "\n\nA None value is a no-op and does not overwrite an existing syncLossTimeout.")

    def test_get_set_debounce_time(self):
        """
        Test getDebounceTime and setDebounceTime round-trip and None no-op.
        """
        obj = self._create_domain()

        value = TimeValue()
        value.setValue("0.5")
        result = obj.setDebounceTime(value)
        assert result is obj
        assert obj.getDebounceTime() is value
        assert obj.getDebounceTime().getValue() == pytest.approx(0.5)

        result = obj.setDebounceTime(None)
        assert result is obj
        assert obj.getDebounceTime() is value

    def test_get_set_domain_id(self):
        """
        Test getDomainId and setDomainId round-trip and None no-op.
        """
        obj = self._create_domain()

        value = PositiveInteger().setValue(8)
        result = obj.setDomainId(value)
        assert result is obj
        assert obj.getDomainId() is value
        assert obj.getDomainId().getValue() == 8

        result = obj.setDomainId(None)
        assert result is obj
        assert obj.getDomainId() is value

    def test_create_global_time_gateway(self):
        """
        Test createGlobalTimeGateway registers the child and duplicate-protects by type.
        """
        obj = self._create_domain()
        gateway = obj.createGlobalTimeGateway("Gateway1")
        assert isinstance(gateway, GlobalTimeGateway)
        assert gateway.getParent() is obj
        assert obj.getGateways() == [gateway]

        same = obj.createGlobalTimeGateway("Gateway1")
        assert same is gateway
        assert obj.getGateways() == [gateway]

    def test_get_set_global_time_correction_props(self):
        """
        Test getGlobalTimeCorrectionProps and setGlobalTimeCorrectionProps round-trip and None no-op.
        """
        obj = self._create_domain()

        props = GlobalTimeCorrectionProps()
        result = obj.setGlobalTimeCorrectionProps(props)
        assert result is obj
        assert obj.getGlobalTimeCorrectionProps() is props

        result = obj.setGlobalTimeCorrectionProps(None)
        assert result is obj
        assert obj.getGlobalTimeCorrectionProps() is props

    def test_get_set_global_time_domain_property(self):
        """
        Test getGlobalTimeDomainProperty and setGlobalTimeDomainProperty round-trip
        with a concrete AbstractGlobalTimeDomainProps subclass and None no-op.
        """
        obj = self._create_domain()

        props = CanGlobalTimeDomainProps()
        assert isinstance(props, AbstractGlobalTimeDomainProps)
        result = obj.setGlobalTimeDomainProperty(props)
        assert result is obj
        assert obj.getGlobalTimeDomainProperty() is props

        result = obj.setGlobalTimeDomainProperty(None)
        assert result is obj
        assert obj.getGlobalTimeDomainProperty() is props

    def test_create_global_time_can_master(self):
        """
        Test createGlobalTimeCanMaster registers the child as the single master
        and duplicate-protects by type.
        """
        obj = self._create_domain()
        master = obj.createGlobalTimeCanMaster("Master1")
        assert isinstance(master, GlobalTimeCanMaster)
        assert isinstance(master, GlobalTimeMaster)
        assert master.getParent() is obj
        assert obj.getGlobalTimeMaster() is master

        same = obj.createGlobalTimeCanMaster("Master1")
        assert same is master
        assert obj.getGlobalTimeMaster() is master

    def test_create_master_subtypes_set_master(self):
        """
        Test the remaining master factory subtypes; the single-valued slot
        points at the most recently created master.
        """
        obj = self._create_domain()
        eth = obj.createGlobalTimeEthMaster("EthMaster")
        assert isinstance(eth, GlobalTimeEthMaster)
        assert obj.getGlobalTimeMaster() is eth

        fr = obj.createGlobalTimeFrMaster("FrMaster")
        assert isinstance(fr, GlobalTimeFrMaster)
        assert obj.getGlobalTimeMaster() is fr

        user_defined = obj.createUserDefinedGlobalTimeMaster("UserMaster")
        assert isinstance(user_defined, UserDefinedGlobalTimeMaster)
        assert obj.getGlobalTimeMaster() is user_defined

    def test_add_global_time_sub_domain_ref(self):
        """
        Test addGlobalTimeSubDomainRef appends, returns self and ignores None.
        """
        obj = self._create_domain()

        ref = RefType().setValue("/TimeDomains/Sub1").setDest("GLOBAL-TIME-DOMAIN")
        result = obj.addGlobalTimeSubDomainRef(ref)
        assert result is obj
        assert obj.getGlobalTimeSubDomainRefs() == [ref]

        result = obj.addGlobalTimeSubDomainRef(None)
        assert result is obj
        assert obj.getGlobalTimeSubDomainRefs() == [ref]

        second = RefType().setValue("/TimeDomains/Sub2").setDest("GLOBAL-TIME-DOMAIN")
        obj.addGlobalTimeSubDomainRef(second)
        assert obj.getGlobalTimeSubDomainRefs() == [ref, second]

    def test_get_set_network_segment_id(self):
        """
        Test getNetworkSegmentId and setNetworkSegmentId round-trip and None no-op.
        """
        obj = self._create_domain()

        props = NetworkSegmentIdentification()
        result = obj.setNetworkSegmentId(props)
        assert result is obj
        assert obj.getNetworkSegmentId() is props

        result = obj.setNetworkSegmentId(None)
        assert result is obj
        assert obj.getNetworkSegmentId() is props

    def test_get_set_offset_time_domain_ref(self):
        """
        Test getOffsetTimeDomainRef and setOffsetTimeDomainRef round-trip and None no-op.
        """
        obj = self._create_domain()

        ref = RefType().setValue("/TimeDomains/Base1").setDest("GLOBAL-TIME-DOMAIN")
        result = obj.setOffsetTimeDomainRef(ref)
        assert result is obj
        assert obj.getOffsetTimeDomainRef() is ref
        assert obj.getOffsetTimeDomainRef().getValue() == "/TimeDomains/Base1"

        result = obj.setOffsetTimeDomainRef(None)
        assert result is obj
        assert obj.getOffsetTimeDomainRef() is ref

    def test_get_set_pdu_triggering_ref(self):
        """
        Test getPduTriggeringRef and setPduTriggeringRef round-trip and None no-op.
        """
        obj = self._create_domain()

        ref = RefType().setValue("/Com/PduTriggering1").setDest("PDU-TRIGGERING")
        result = obj.setPduTriggeringRef(ref)
        assert result is obj
        assert obj.getPduTriggeringRef() is ref
        assert obj.getPduTriggeringRef().getDest() == "PDU-TRIGGERING"

        result = obj.setPduTriggeringRef(None)
        assert result is obj
        assert obj.getPduTriggeringRef() is ref

    def test_create_global_time_can_slave(self):
        """
        Test createGlobalTimeCanSlave registers the child and duplicate-protects by type.
        """
        obj = self._create_domain()
        slave = obj.createGlobalTimeCanSlave("Slave1")
        assert isinstance(slave, GlobalTimeCanSlave)
        assert isinstance(slave, GlobalTimeSlave)
        assert slave.getParent() is obj
        assert obj.getSlaves() == [slave]

        same = obj.createGlobalTimeCanSlave("Slave1")
        assert same is slave
        assert obj.getSlaves() == [slave]

    def test_create_slave_subtypes_append(self):
        """
        Test the remaining slave factory subtypes append to the collection in order.
        """
        obj = self._create_domain()
        eth = obj.createGlobalTimeEthSlave("EthSlave")
        assert isinstance(eth, GlobalTimeEthSlave)
        fr = obj.createGlobalTimeFrSlave("FrSlave")
        assert isinstance(fr, GlobalTimeFrSlave)
        user_defined = obj.createUserDefinedGlobalTimeSlave("UserSlave")
        assert isinstance(user_defined, UserDefinedGlobalTimeSlave)
        assert obj.getSlaves() == [eth, fr, user_defined]

    def test_get_set_sync_loss_timeout(self):
        """
        Test getSyncLossTimeout and setSyncLossTimeout round-trip and None no-op.
        """
        obj = self._create_domain()

        value = TimeValue()
        value.setValue("1.0")
        result = obj.setSyncLossTimeout(value)
        assert result is obj
        assert obj.getSyncLossTimeout() is value
        assert obj.getSyncLossTimeout().getValue() == pytest.approx(1.0)

        result = obj.setSyncLossTimeout(None)
        assert result is obj
        assert obj.getSyncLossTimeout() is value
