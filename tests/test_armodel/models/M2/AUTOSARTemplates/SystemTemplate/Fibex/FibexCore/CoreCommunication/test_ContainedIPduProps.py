import inspect
import sys
import typing

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    PositiveInteger,
    RefType,
    TimeValue,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Ethernet.ServiceInstances import (
    PduCollectionTriggerEnum,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore.CoreCommunication import (
    ContainedIPduCollectionSemanticsEnum,
    ContainedIPduProps,
)


def _get_type_hints(obj):
    """typing.get_type_hints leaves PEP 563 self-references as ForwardRef on Python 3.8; resolve against the defining module."""
    hints = typing.get_type_hints(obj)
    module_vars = vars(sys.modules[obj.__module__])
    for name, hint in hints.items():
        if isinstance(hint, typing.ForwardRef):
            hints[name] = module_vars.get(hint.__forward_arg__, hint)
    return hints


CLASS_NOTE = (
    "Defines the aspects of an IPdu which can be collected inside a ContainerIPdu.\n"
    "\n"
    "[constr_9202] Existence of ContainedIPduProps.collectionSemantics: For each ContainedIPduProps, "
    "the attribute collectionSemantics shall exist at the time when the System Description is complete.\n"
    "[constr_5268] Existence of ContainedIPduProps.containedPduTriggering reference: If a ContainedIPduProps "
    "is aggregated at the ContainerIPdu in the role ContainerIPdu.containedIPduTriggeringProps then the "
    "reference ContainedIPduProps.containedPduTriggering shall exist.\n"
    "[constr_5269] Exclusion of ContainedIPduProps.containedPduTriggering reference: If a ContainedIPduProps "
    "is aggregated at the IPdu in the role IPdu.containedIPduProps then the reference "
    "ContainedIPduProps.containedPduTriggering shall NOT exist."
)

COLLECTION_SEMANTICS_NOTE = "Defines whether this ContainedIPdu shall be collected using a last-is-best or queued semantics."

CONTAINED_PDU_TRIGGERING_NOTE = "Reference to Pdu for which the ContainedIPduProps are valid."

HEADER_ID_LONG_HEADER_NOTE = "Defines the header id this IPdu shall have in case this IPdu is put inside a ContainerIPdu with headerType = longHeader."

HEADER_ID_SHORT_HEADER_NOTE = "Defines the header id this IPdu shall have in case this IPdu is put inside a ContainerIPdu with headerType = shortHeader."

OFFSET_NOTE = "Byte offset that describes the location of the ContainedPdu in the ContainerPdu if no header is used."

PRIORITY_NOTE = "Defines a priority of a ContainedTxPdu. 255 represents the lowest priority and 0 represent the highest priority."

TIMEOUT_NOTE = "Defines a IPdu specific sender timeout which can reduce the ContainerIPdu timer when this containedIPdu is put inside the ContainerIPdu. This attribute is ignored on receiver side."

TRIGGER_NOTE = "Defines whether this IPdu does trigger the sending of the ContainerIPdu. This attribute is ignored on receiver side."

UPDATE_INDICATION_BIT_POSITION_NOTE = (
    "The updateIndicationBit specifies the bit location of ContainedIPdu Update-Bit in the Container PDU. It indicates to the receivers that the ContainedIPdu in the ContainerIPdu was updated."
)


class TestContainedIPduProps:
    """Test cases for ContainedIPduProps (Table 6.39, p.356)."""

    MEMBERS = [
        "collectionSemantics",
        "containedPduTriggeringRef",
        "headerIdLongHeader",
        "headerIdShortHeader",
        "offset",
        "priority",
        "timeout",
        "trigger",
        "updateIndicationBitPosition",
    ]

    def test_inheritance(self):
        assert issubclass(ContainedIPduProps, ARObject)

    def test_class_docstring_note(self):
        assert inspect.cleandoc(ContainedIPduProps.__doc__) == CLASS_NOTE

    def test_init_docless(self):
        assert ContainedIPduProps.__init__.__doc__ is None

    def test_initialization_defaults(self):
        props = ContainedIPduProps()
        assert props.getCollectionSemantics() is None
        assert props.getContainedPduTriggeringRef() is None
        assert props.getHeaderIdLongHeader() is None
        assert props.getHeaderIdShortHeader() is None
        assert props.getOffset() is None
        assert props.getPriority() is None
        assert props.getTimeout() is None
        assert props.getTrigger() is None
        assert props.getUpdateIndicationBitPosition() is None

    def test_member_order(self):
        props = ContainedIPduProps()
        members = [k for k in vars(props) if k in set(self.MEMBERS)]
        assert members == self.MEMBERS

    def test_get_set_collection_semantics(self):
        props = ContainedIPduProps()
        value = ContainedIPduCollectionSemanticsEnum()
        value.setValue(ContainedIPduCollectionSemanticsEnum.QUEUED)
        assert props == props.setCollectionSemantics(value)
        assert props.getCollectionSemantics() == value

        assert props == props.setCollectionSemantics(None)
        assert props.getCollectionSemantics() == value

        getter_hints = _get_type_hints(ContainedIPduProps.getCollectionSemantics)
        assert getter_hints.get("return") == typing.Optional[ContainedIPduCollectionSemanticsEnum]

        setter_hints = _get_type_hints(ContainedIPduProps.setCollectionSemantics)
        assert setter_hints.get("value") == typing.Optional[ContainedIPduCollectionSemanticsEnum]
        assert setter_hints.get("return") is ContainedIPduProps

    def test_get_set_contained_pdu_triggering_ref(self):
        props = ContainedIPduProps()
        ref = RefType()
        ref.setDest("PDU-TRIGGERING")
        ref.setValue("/PduTriggering1")
        assert props == props.setContainedPduTriggeringRef(ref)
        assert props.getContainedPduTriggeringRef() == ref

        assert props == props.setContainedPduTriggeringRef(None)
        assert props.getContainedPduTriggeringRef() == ref

        getter_hints = _get_type_hints(ContainedIPduProps.getContainedPduTriggeringRef)
        assert getter_hints.get("return") == typing.Optional[RefType]

        setter_hints = _get_type_hints(ContainedIPduProps.setContainedPduTriggeringRef)
        assert setter_hints.get("value") == typing.Optional[RefType]
        assert setter_hints.get("return") is ContainedIPduProps

    def test_get_set_header_id_long_header(self):
        props = ContainedIPduProps()
        value = PositiveInteger()
        value.setValue("100")
        assert props == props.setHeaderIdLongHeader(value)
        assert props.getHeaderIdLongHeader().getValue() == 100

        assert props == props.setHeaderIdLongHeader(None)
        assert props.getHeaderIdLongHeader() == value

        getter_hints = _get_type_hints(ContainedIPduProps.getHeaderIdLongHeader)
        assert getter_hints.get("return") == typing.Optional[PositiveInteger]

        setter_hints = _get_type_hints(ContainedIPduProps.setHeaderIdLongHeader)
        assert setter_hints.get("value") == typing.Optional[PositiveInteger]
        assert setter_hints.get("return") is ContainedIPduProps

    def test_get_set_header_id_short_header(self):
        props = ContainedIPduProps()
        value = PositiveInteger()
        value.setValue("50")
        assert props == props.setHeaderIdShortHeader(value)
        assert props.getHeaderIdShortHeader().getValue() == 50

        assert props == props.setHeaderIdShortHeader(None)
        assert props.getHeaderIdShortHeader() == value

        getter_hints = _get_type_hints(ContainedIPduProps.getHeaderIdShortHeader)
        assert getter_hints.get("return") == typing.Optional[PositiveInteger]

        setter_hints = _get_type_hints(ContainedIPduProps.setHeaderIdShortHeader)
        assert setter_hints.get("value") == typing.Optional[PositiveInteger]
        assert setter_hints.get("return") is ContainedIPduProps

    def test_get_set_offset(self):
        props = ContainedIPduProps()
        value = PositiveInteger()
        value.setValue("4")
        assert props == props.setOffset(value)
        assert props.getOffset().getValue() == 4

        assert props == props.setOffset(None)
        assert props.getOffset() == value

        getter_hints = _get_type_hints(ContainedIPduProps.getOffset)
        assert getter_hints.get("return") == typing.Optional[PositiveInteger]

        setter_hints = _get_type_hints(ContainedIPduProps.setOffset)
        assert setter_hints.get("value") == typing.Optional[PositiveInteger]
        assert setter_hints.get("return") is ContainedIPduProps

    def test_get_set_priority(self):
        props = ContainedIPduProps()
        value = PositiveInteger()
        value.setValue("6")
        assert props == props.setPriority(value)
        assert props.getPriority().getValue() == 6

        assert props == props.setPriority(None)
        assert props.getPriority() == value

        getter_hints = _get_type_hints(ContainedIPduProps.getPriority)
        assert getter_hints.get("return") == typing.Optional[PositiveInteger]

        setter_hints = _get_type_hints(ContainedIPduProps.setPriority)
        assert setter_hints.get("value") == typing.Optional[PositiveInteger]
        assert setter_hints.get("return") is ContainedIPduProps

    def test_get_set_timeout(self):
        props = ContainedIPduProps()
        value = TimeValue()
        value.setValue("0.01")
        assert props == props.setTimeout(value)
        assert props.getTimeout().getValue() == 0.01

        assert props == props.setTimeout(None)
        assert props.getTimeout() == value

        getter_hints = _get_type_hints(ContainedIPduProps.getTimeout)
        assert getter_hints.get("return") == typing.Optional[TimeValue]

        setter_hints = _get_type_hints(ContainedIPduProps.setTimeout)
        assert setter_hints.get("value") == typing.Optional[TimeValue]
        assert setter_hints.get("return") is ContainedIPduProps

    def test_get_set_trigger(self):
        props = ContainedIPduProps()
        value = PduCollectionTriggerEnum()
        value.setValue(PduCollectionTriggerEnum.ALWAYS)
        assert props == props.setTrigger(value)
        assert props.getTrigger() == value

        assert props == props.setTrigger(None)
        assert props.getTrigger() == value

        getter_hints = _get_type_hints(ContainedIPduProps.getTrigger)
        assert getter_hints.get("return") == typing.Optional[PduCollectionTriggerEnum]

        setter_hints = _get_type_hints(ContainedIPduProps.setTrigger)
        assert setter_hints.get("value") == typing.Optional[PduCollectionTriggerEnum]
        assert setter_hints.get("return") is ContainedIPduProps

    def test_get_set_update_indication_bit_position(self):
        props = ContainedIPduProps()
        value = PositiveInteger()
        value.setValue("7")
        assert props == props.setUpdateIndicationBitPosition(value)
        assert props.getUpdateIndicationBitPosition().getValue() == 7

        assert props == props.setUpdateIndicationBitPosition(None)
        assert props.getUpdateIndicationBitPosition() == value

        getter_hints = _get_type_hints(ContainedIPduProps.getUpdateIndicationBitPosition)
        assert getter_hints.get("return") == typing.Optional[PositiveInteger]

        setter_hints = _get_type_hints(ContainedIPduProps.setUpdateIndicationBitPosition)
        assert setter_hints.get("value") == typing.Optional[PositiveInteger]
        assert setter_hints.get("return") is ContainedIPduProps

    def test_docstrings_are_spec_notes(self):
        """Test that the getter/setter docstrings carry the attribute Notes verbatim (Table 6.39)."""
        assert ContainedIPduProps.getCollectionSemantics.__doc__.strip() == COLLECTION_SEMANTICS_NOTE
        assert (
            inspect.cleandoc(ContainedIPduProps.setCollectionSemantics.__doc__).strip()
            == COLLECTION_SEMANTICS_NOTE + "\nA None value is a no-op and does not overwrite an existing collectionSemantics."
        )
        assert ContainedIPduProps.getContainedPduTriggeringRef.__doc__.strip() == CONTAINED_PDU_TRIGGERING_NOTE
        assert (
            inspect.cleandoc(ContainedIPduProps.setContainedPduTriggeringRef.__doc__).strip()
            == CONTAINED_PDU_TRIGGERING_NOTE + "\nA None value is a no-op and does not overwrite an existing containedPduTriggeringRef."
        )
        assert ContainedIPduProps.getHeaderIdLongHeader.__doc__.strip() == HEADER_ID_LONG_HEADER_NOTE
        assert (
            inspect.cleandoc(ContainedIPduProps.setHeaderIdLongHeader.__doc__).strip()
            == HEADER_ID_LONG_HEADER_NOTE + "\nA None value is a no-op and does not overwrite an existing headerIdLongHeader."
        )
        assert ContainedIPduProps.getHeaderIdShortHeader.__doc__.strip() == HEADER_ID_SHORT_HEADER_NOTE
        assert (
            inspect.cleandoc(ContainedIPduProps.setHeaderIdShortHeader.__doc__).strip()
            == HEADER_ID_SHORT_HEADER_NOTE + "\nA None value is a no-op and does not overwrite an existing headerIdShortHeader."
        )
        assert ContainedIPduProps.getOffset.__doc__.strip() == OFFSET_NOTE
        assert inspect.cleandoc(ContainedIPduProps.setOffset.__doc__).strip() == OFFSET_NOTE + "\nA None value is a no-op and does not overwrite an existing offset."
        assert ContainedIPduProps.getPriority.__doc__.strip() == PRIORITY_NOTE
        assert inspect.cleandoc(ContainedIPduProps.setPriority.__doc__).strip() == PRIORITY_NOTE + "\nA None value is a no-op and does not overwrite an existing priority."
        assert ContainedIPduProps.getTimeout.__doc__.strip() == TIMEOUT_NOTE
        assert inspect.cleandoc(ContainedIPduProps.setTimeout.__doc__).strip() == TIMEOUT_NOTE + "\nA None value is a no-op and does not overwrite an existing timeout."
        assert ContainedIPduProps.getTrigger.__doc__.strip() == TRIGGER_NOTE
        assert inspect.cleandoc(ContainedIPduProps.setTrigger.__doc__).strip() == TRIGGER_NOTE + "\nA None value is a no-op and does not overwrite an existing trigger."
        assert ContainedIPduProps.getUpdateIndicationBitPosition.__doc__.strip() == UPDATE_INDICATION_BIT_POSITION_NOTE
        assert (
            inspect.cleandoc(ContainedIPduProps.setUpdateIndicationBitPosition.__doc__).strip()
            == UPDATE_INDICATION_BIT_POSITION_NOTE + "\nA None value is a no-op and does not overwrite an existing updateIndicationBitPosition."
        )
