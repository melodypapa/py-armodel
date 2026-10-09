import inspect
import sys
import typing

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable import Identifiable
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import Boolean, PositiveInteger
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore.CoreCommunication import SecureCommunicationFreshnessProps


def _get_type_hints(obj):
    """typing.get_type_hints leaves PEP 563 self-references as ForwardRef on Python 3.8; resolve against the defining module."""
    hints = typing.get_type_hints(obj)
    module_vars = vars(sys.modules[obj.__module__])
    for name, hint in hints.items():
        if isinstance(hint, typing.ForwardRef):
            hints[name] = module_vars.get(hint.__forward_arg__, hint)
    return hints


CLASS_NOTE = "Freshness properties used to configure SecuredIPdus."

FRESHNESS_COUNTER_SYNC_ATTEMPTS_NOTE = (
    "This attribute defines the number of Freshness Counter re-synchronization attempts when a verification failed for a Secured I-PDU. "
    "If the value is zero, there will be no additional verification attempt to synchronize with a potentially better fitting Freshness Counter value. "
    "This attribute is only applicable if useFreshnessTimestamp is FALSE."
)

FRESHNESS_TIMESTAMP_TIME_PERIOD_FACTOR_NOTE = (
    "This attribute defines a factor that specifies the time period for the Freshness Timestamp. "
    "It holds a multiplication factor that specifies the concrete meaning of a Freshness Timestamp increment by one on basis of microseconds."
)

FRESHNESS_VALUE_LENGTH_NOTE = (
    "This attribute defines the complete length in bits of the Freshness Value. As long as the key doesn't change the counter shall not overflow. "
    "The length of the counter shall be determined based on the expected life time of the corresponding key and frequency of usage of the counter."
)

FRESHNESS_VALUE_TX_LENGTH_NOTE = (
    "This attribute defines the length in bits of the Freshness Value to be included in the payload of the Secured I-PDU. "
    "This length is specific to the least significant bits of the complete Freshness Counter. If the attribute is 0 no Freshness Value is included in the Secured I-PDU."
)

USE_FRESHNESS_TIMESTAMP_NOTE = (
    "This attribute specifies whether the Freshness Value is generated through individual Freshness Counters or by a Timestamps. " "The value is set to TRUE when Timestamps are used."
)


class TestSecureCommunicationFreshnessProps:
    """Test cases for SecureCommunicationFreshnessProps (Table 6.46, p.371)."""

    MEMBERS = [
        "freshnessCounterSyncAttempts",
        "freshnessTimestampTimePeriodFactor",
        "freshnessValueLength",
        "freshnessValueTxLength",
        "useFreshnessTimestamp",
    ]

    def _create(self, short_name: str = "props") -> SecureCommunicationFreshnessProps:
        return SecureCommunicationFreshnessProps(None, short_name)

    def test_inheritance(self):
        assert issubclass(SecureCommunicationFreshnessProps, ARObject)
        assert issubclass(SecureCommunicationFreshnessProps, Identifiable)

    def test_class_docstring_note(self):
        assert inspect.cleandoc(SecureCommunicationFreshnessProps.__doc__) == inspect.cleandoc(CLASS_NOTE)

    def test_init_docless(self):
        assert SecureCommunicationFreshnessProps.__init__.__doc__ is None

    def test_initialization_defaults(self):
        props = self._create()
        assert props.getFreshnessCounterSyncAttempts() is None
        assert props.getFreshnessTimestampTimePeriodFactor() is None
        assert props.getFreshnessValueLength() is None
        assert props.getFreshnessValueTxLength() is None
        assert props.getUseFreshnessTimestamp() is None

    def test_member_order(self):
        props = self._create()
        members = [k for k in vars(props) if k in set(self.MEMBERS)]
        assert members == self.MEMBERS

    def test_get_set_freshness_counter_sync_attempts(self):
        props = self._create()
        value = PositiveInteger()
        value.setValue("3")
        assert props == props.setFreshnessCounterSyncAttempts(value)
        assert props.getFreshnessCounterSyncAttempts().getValue() == 3

        assert props == props.setFreshnessCounterSyncAttempts(None)
        assert props.getFreshnessCounterSyncAttempts() == value

        getter_hints = _get_type_hints(SecureCommunicationFreshnessProps.getFreshnessCounterSyncAttempts)
        assert getter_hints.get("return") == typing.Optional[PositiveInteger]

        setter_hints = _get_type_hints(SecureCommunicationFreshnessProps.setFreshnessCounterSyncAttempts)
        assert setter_hints.get("value") == typing.Optional[PositiveInteger]
        assert setter_hints.get("return") is SecureCommunicationFreshnessProps

    def test_get_set_freshness_timestamp_time_period_factor(self):
        props = self._create()
        value = PositiveInteger()
        value.setValue("10")
        assert props == props.setFreshnessTimestampTimePeriodFactor(value)
        assert props.getFreshnessTimestampTimePeriodFactor().getValue() == 10

        assert props == props.setFreshnessTimestampTimePeriodFactor(None)
        assert props.getFreshnessTimestampTimePeriodFactor() == value

        getter_hints = _get_type_hints(SecureCommunicationFreshnessProps.getFreshnessTimestampTimePeriodFactor)
        assert getter_hints.get("return") == typing.Optional[PositiveInteger]

        setter_hints = _get_type_hints(SecureCommunicationFreshnessProps.setFreshnessTimestampTimePeriodFactor)
        assert setter_hints.get("value") == typing.Optional[PositiveInteger]
        assert setter_hints.get("return") is SecureCommunicationFreshnessProps

    def test_get_set_freshness_value_length(self):
        props = self._create()
        value = PositiveInteger()
        value.setValue("64")
        assert props == props.setFreshnessValueLength(value)
        assert props.getFreshnessValueLength().getValue() == 64

        assert props == props.setFreshnessValueLength(None)
        assert props.getFreshnessValueLength() == value

        getter_hints = _get_type_hints(SecureCommunicationFreshnessProps.getFreshnessValueLength)
        assert getter_hints.get("return") == typing.Optional[PositiveInteger]

        setter_hints = _get_type_hints(SecureCommunicationFreshnessProps.setFreshnessValueLength)
        assert setter_hints.get("value") == typing.Optional[PositiveInteger]
        assert setter_hints.get("return") is SecureCommunicationFreshnessProps

    def test_get_set_freshness_value_tx_length(self):
        props = self._create()
        value = PositiveInteger()
        value.setValue("8")
        assert props == props.setFreshnessValueTxLength(value)
        assert props.getFreshnessValueTxLength().getValue() == 8

        assert props == props.setFreshnessValueTxLength(None)
        assert props.getFreshnessValueTxLength() == value

        getter_hints = _get_type_hints(SecureCommunicationFreshnessProps.getFreshnessValueTxLength)
        assert getter_hints.get("return") == typing.Optional[PositiveInteger]

        setter_hints = _get_type_hints(SecureCommunicationFreshnessProps.setFreshnessValueTxLength)
        assert setter_hints.get("value") == typing.Optional[PositiveInteger]
        assert setter_hints.get("return") is SecureCommunicationFreshnessProps

    def test_get_set_use_freshness_timestamp(self):
        props = self._create()
        value = Boolean()
        value.setValue("true")
        assert props == props.setUseFreshnessTimestamp(value)
        assert props.getUseFreshnessTimestamp() is value

        assert props == props.setUseFreshnessTimestamp(None)
        assert props.getUseFreshnessTimestamp() == value

        getter_hints = _get_type_hints(SecureCommunicationFreshnessProps.getUseFreshnessTimestamp)
        assert getter_hints.get("return") == typing.Optional[Boolean]

        setter_hints = _get_type_hints(SecureCommunicationFreshnessProps.setUseFreshnessTimestamp)
        assert setter_hints.get("value") == typing.Optional[Boolean]
        assert setter_hints.get("return") is SecureCommunicationFreshnessProps

    def test_docstrings_are_spec_notes(self):
        """Test that the getter/setter docstrings carry the attribute Notes verbatim (Table 6.46)."""
        assert SecureCommunicationFreshnessProps.getFreshnessCounterSyncAttempts.__doc__.strip() == FRESHNESS_COUNTER_SYNC_ATTEMPTS_NOTE
        assert (
            inspect.cleandoc(SecureCommunicationFreshnessProps.setFreshnessCounterSyncAttempts.__doc__).strip()
            == FRESHNESS_COUNTER_SYNC_ATTEMPTS_NOTE + "\nA None value is a no-op and does not overwrite an existing freshnessCounterSyncAttempts."
        )
        assert SecureCommunicationFreshnessProps.getFreshnessTimestampTimePeriodFactor.__doc__.strip() == FRESHNESS_TIMESTAMP_TIME_PERIOD_FACTOR_NOTE
        assert (
            inspect.cleandoc(SecureCommunicationFreshnessProps.setFreshnessTimestampTimePeriodFactor.__doc__).strip()
            == FRESHNESS_TIMESTAMP_TIME_PERIOD_FACTOR_NOTE + "\nA None value is a no-op and does not overwrite an existing freshnessTimestampTimePeriodFactor."
        )
        assert SecureCommunicationFreshnessProps.getFreshnessValueLength.__doc__.strip() == FRESHNESS_VALUE_LENGTH_NOTE
        assert (
            inspect.cleandoc(SecureCommunicationFreshnessProps.setFreshnessValueLength.__doc__).strip()
            == FRESHNESS_VALUE_LENGTH_NOTE + "\nA None value is a no-op and does not overwrite an existing freshnessValueLength."
        )
        assert SecureCommunicationFreshnessProps.getFreshnessValueTxLength.__doc__.strip() == FRESHNESS_VALUE_TX_LENGTH_NOTE
        assert (
            inspect.cleandoc(SecureCommunicationFreshnessProps.setFreshnessValueTxLength.__doc__).strip()
            == FRESHNESS_VALUE_TX_LENGTH_NOTE + "\nA None value is a no-op and does not overwrite an existing freshnessValueTxLength."
        )
        assert SecureCommunicationFreshnessProps.getUseFreshnessTimestamp.__doc__.strip() == USE_FRESHNESS_TIMESTAMP_NOTE
        assert (
            inspect.cleandoc(SecureCommunicationFreshnessProps.setUseFreshnessTimestamp.__doc__).strip()
            == USE_FRESHNESS_TIMESTAMP_NOTE + "\nA None value is a no-op and does not overwrite an existing useFreshnessTimestamp."
        )
