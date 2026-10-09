import inspect
import sys
import typing

from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable import Identifiable
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import RefType
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.StereotypeMixins import VariationPointCapable
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore.CoreCommunication import PduTriggering, TriggerIPduSendCondition


def _get_type_hints(obj):
    """typing.get_type_hints leaves PEP 563 self-references as ForwardRef on Python 3.8; resolve against the defining module."""
    hints = typing.get_type_hints(obj)
    module_vars = vars(sys.modules[obj.__module__])
    for name, hint in hints.items():
        if isinstance(hint, typing.ForwardRef):
            hints[name] = module_vars.get(hint.__forward_arg__, hint)
    return hints


CLASS_NOTE = (
    "The PduTriggering describes on which channel the IPdu is transmitted. The Pdu routing by the PduR is only allowed "
    "for subclasses of IPdu. Depending on its relation to entities such channels and clusters it can be unambiguously "
    "deduced whether a fan-out is handled by the Pdu router or the Bus Interface. If the fan-out is specified between "
    "different clusters it shall be handled by the Pdu Router. If the fan-out is specified between different channels "
    "of the same cluster it shall be handled by the Bus Interface.\n"
    "\n"
    "[constr_9198] Existence of PduTriggering.iPdu: For each PduTriggering, the reference to Pdu in the role iPdu shall "
    "exist at the time when the System Description is complete."
)

IPDU_NOTE = (
    "Reference to the Pdu for which the PduTriggering is defined. One I-Pdu can be triggered on different channels "
    "(PduR fan-out). The Pdu routing by the PduR is only allowed for subclasses of IPdu. Nevertheless is the reference "
    "to the Pdu element necessary since the PduTriggering element is also used to specify the sending and receiving "
    "connections to Ecu Ports."
)

IPDU_PORT_NOTE = (
    "References to the IPduPort on every ECU of the system which sends and/or receives the I-PDU. References for both "
    "the sender and the receiver side shall be included when the system is completely defined."
)

ISIGNAL_TRIGGERING_NOTE = (
    "This reference provides the relationship to the ISignal Triggerings that are implemented by the PduTriggering. "
    "The reference is optional since no ISignalTriggering can be defined for DCM and Multiplexed Pdus. Stereotypes: "
    "atpSplitable; atpVariation Tags: atp.Splitkey=iSignalTriggering.iSignalTriggering, "
    "iSignal Triggering.variationPoint.shortLabel vh.latestBindingTime=postBuild"
)

SEC_OC_CRYPTO_MAPPING_NOTE = (
    "This reference identifies the crypto profile applicable to the usage (send, receive) of the also referenced "
    "Secured IPdu. Obviously, this reference is only applicable if the Pdutriggering also references a SecuredIPdu in "
    "the role i Pdu."
)

TRIGGER_IPDU_SEND_CONDITION_NOTE = (
    "Defines the trigger for the Com_TriggerIPDUSend API call. Only if all defined TriggerIPduSendConditions evaluate " "to true (AND associated) the Com_Trigger IPDUSend API shall be called."
)


class TestPduTriggering:
    """Test cases for PduTriggering (Table 6.31, p.349)."""

    MEMBERS = [
        "iPduRef",
        "iPduPortRefs",
        "iSignalTriggeringRefs",
        "secOcCryptoMappingRef",
        "triggerIPduSendConditions",
    ]

    def _create(self, short_name: str) -> PduTriggering:
        pkg = AUTOSAR.getInstance().createARPackage("PduTriggeringPkg")
        return PduTriggering(pkg, short_name)

    def _ref(self, value: str, dest: str) -> RefType:
        ref = RefType()
        ref.setDest(dest)
        ref.setValue(value)
        return ref

    def test_inheritance(self):
        assert issubclass(PduTriggering, Identifiable)
        assert issubclass(PduTriggering, VariationPointCapable)
        assert issubclass(PduTriggering, ARObject)

    def test_class_docstring_note(self):
        assert inspect.cleandoc(PduTriggering.__doc__) == CLASS_NOTE

    def test_init_docless(self):
        assert PduTriggering.__init__.__doc__ is None

    def test_initialization_defaults(self):
        triggering = self._create("Pt")
        assert triggering.getIPduRef() is None
        assert triggering.getIPduPortRefs() == []
        assert triggering.getISignalTriggeringRefs() == []
        assert triggering.getSecOcCryptoMappingRef() is None
        assert triggering.getTriggerIPduSendConditions() == []

    def test_member_order(self):
        triggering = self._create("Pt")
        members = [k for k in vars(triggering) if k in set(self.MEMBERS)]
        assert members == self.MEMBERS

    def test_get_set_ipdu_ref(self):
        triggering = self._create("Pt")
        ref = self._ref("/Pdu1", "PDU")
        assert triggering == triggering.setIPduRef(ref)
        assert triggering.getIPduRef() == ref

        assert triggering == triggering.setIPduRef(None)
        assert triggering.getIPduRef() == ref

        getter_hints = _get_type_hints(PduTriggering.getIPduRef)
        assert getter_hints.get("return") == typing.Optional[RefType]

        setter_hints = _get_type_hints(PduTriggering.setIPduRef)
        assert setter_hints.get("value") == typing.Optional[RefType]
        assert setter_hints.get("return") is PduTriggering

    def test_add_ipdu_port_ref(self):
        triggering = self._create("Pt")
        ref1 = self._ref("/IPduPort1", "I-PDU-PORT")
        ref2 = self._ref("/IPduPort2", "I-PDU-PORT")

        assert triggering == triggering.addIPduPortRef(ref1)
        assert triggering == triggering.addIPduPortRef(ref2)
        assert triggering.getIPduPortRefs() == [ref1, ref2]

        assert triggering == triggering.addIPduPortRef(None)
        assert triggering.getIPduPortRefs() == [ref1, ref2]

        getter_hints = _get_type_hints(PduTriggering.getIPduPortRefs)
        assert getter_hints.get("return") == typing.List[RefType]

        adder_hints = _get_type_hints(PduTriggering.addIPduPortRef)
        assert adder_hints.get("value") == typing.Optional[RefType]
        assert adder_hints.get("return") is PduTriggering

    def test_add_isignal_triggering_ref(self):
        triggering = self._create("Pt")
        ref1 = self._ref("/ISignalTriggering1", "I-SIGNAL-TRIGGERING")
        ref2 = self._ref("/ISignalTriggering2", "I-SIGNAL-TRIGGERING")

        assert triggering == triggering.addISignalTriggeringRef(ref1)
        assert triggering == triggering.addISignalTriggeringRef(ref2)
        assert triggering.getISignalTriggeringRefs() == [ref1, ref2]

        assert triggering == triggering.addISignalTriggeringRef(None)
        assert triggering.getISignalTriggeringRefs() == [ref1, ref2]

        getter_hints = _get_type_hints(PduTriggering.getISignalTriggeringRefs)
        assert getter_hints.get("return") == typing.List[RefType]

        adder_hints = _get_type_hints(PduTriggering.addISignalTriggeringRef)
        assert adder_hints.get("value") == typing.Optional[RefType]
        assert adder_hints.get("return") is PduTriggering

    def test_get_set_sec_oc_crypto_mapping_ref(self):
        triggering = self._create("Pt")
        ref = self._ref("/SecOcCryptoServiceMapping1", "SEC-OC-CRYPTO-SERVICE-MAPPING")
        assert triggering == triggering.setSecOcCryptoMappingRef(ref)
        assert triggering.getSecOcCryptoMappingRef() == ref

        assert triggering == triggering.setSecOcCryptoMappingRef(None)
        assert triggering.getSecOcCryptoMappingRef() == ref

        getter_hints = _get_type_hints(PduTriggering.getSecOcCryptoMappingRef)
        assert getter_hints.get("return") == typing.Optional[RefType]

        setter_hints = _get_type_hints(PduTriggering.setSecOcCryptoMappingRef)
        assert setter_hints.get("value") == typing.Optional[RefType]
        assert setter_hints.get("return") is PduTriggering

    def test_add_trigger_ipdu_send_condition(self):
        triggering = self._create("Pt")
        condition1 = TriggerIPduSendCondition()
        condition2 = TriggerIPduSendCondition()

        assert triggering == triggering.addTriggerIPduSendCondition(condition1)
        assert triggering == triggering.addTriggerIPduSendCondition(condition2)
        assert triggering.getTriggerIPduSendConditions() == [condition1, condition2]

        assert triggering == triggering.addTriggerIPduSendCondition(None)
        assert triggering.getTriggerIPduSendConditions() == [condition1, condition2]

        getter_hints = _get_type_hints(PduTriggering.getTriggerIPduSendConditions)
        assert getter_hints.get("return") == typing.List[TriggerIPduSendCondition]

        adder_hints = _get_type_hints(PduTriggering.addTriggerIPduSendCondition)
        assert adder_hints.get("value") == typing.Optional[TriggerIPduSendCondition]
        assert adder_hints.get("return") is PduTriggering

    def test_docstrings_are_spec_notes(self):
        """Test that the getter/adder docstrings carry the attribute Notes verbatim (Table 6.31)."""
        assert PduTriggering.getIPduRef.__doc__.strip() == IPDU_NOTE
        assert inspect.cleandoc(PduTriggering.setIPduRef.__doc__).strip() == IPDU_NOTE + "\nA None value is a no-op and does not overwrite an existing iPduRef."
        assert PduTriggering.getIPduPortRefs.__doc__.strip() == IPDU_PORT_NOTE
        assert PduTriggering.addIPduPortRef.__doc__.strip() == IPDU_PORT_NOTE
        assert PduTriggering.getISignalTriggeringRefs.__doc__.strip() == ISIGNAL_TRIGGERING_NOTE
        assert PduTriggering.addISignalTriggeringRef.__doc__.strip() == ISIGNAL_TRIGGERING_NOTE
        assert PduTriggering.getSecOcCryptoMappingRef.__doc__.strip() == SEC_OC_CRYPTO_MAPPING_NOTE
        assert (
            inspect.cleandoc(PduTriggering.setSecOcCryptoMappingRef.__doc__).strip()
            == SEC_OC_CRYPTO_MAPPING_NOTE + "\nA None value is a no-op and does not overwrite an existing secOcCryptoMappingRef."
        )
        assert PduTriggering.getTriggerIPduSendConditions.__doc__.strip() == TRIGGER_IPDU_SEND_CONDITION_NOTE
        assert PduTriggering.addTriggerIPduSendCondition.__doc__.strip() == TRIGGER_IPDU_SEND_CONDITION_NOTE
