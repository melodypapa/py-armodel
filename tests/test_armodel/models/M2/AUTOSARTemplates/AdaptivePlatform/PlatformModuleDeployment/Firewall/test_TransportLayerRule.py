import inspect
import typing
from typing import Optional

from armodel.models.M2.AUTOSARTemplates.AdaptivePlatform.PlatformModuleDeployment.Firewall import TransportLayerRule
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import Boolean, PositiveInteger

CHECKSUM_VERIFICATION_NOTE = "Defines whether checksum verification is performed or not."
MAX_DESTINATION_PORT_NUMBER_NOTE = "Filter to match packets with the maximum destination UDP/TCP port  number."
MAX_SOURCE_PORT_NUMBER_NOTE = "Filter to match packets with the maximum source UDP/TCP port  number."
MIN_DESTINATION_PORT_NUMBER_NOTE = "Filter to match packets with the minimum destination UDP/TCP port  number."
MIN_SOURCE_PORT_NUMBER_NOTE = "Filter to match packets with the minimum source UDP/TCP port  number."


def _pos_int(value):
    p = PositiveInteger()
    p.setValue(value)
    return p


def _boolean(value):
    b = Boolean()
    b.setValue(value)
    return b


class TestTransportLayerRule:
    def test_instantiation_and_base(self):
        obj = TransportLayerRule()
        assert isinstance(obj, ARObject)

    def test_init_has_no_docstring(self):
        assert TransportLayerRule.__init__.__doc__ is None

    def test_class_docstring_is_spec_note_verbatim(self):
        assert TransportLayerRule.__doc__.strip() == "Configuration of filter rules on Transport Layer level. Tags: atp.Status=candidate"

    def test_defaults_in_spec_displayed_order(self):
        obj = TransportLayerRule()
        assert obj.getChecksumVerification() is None
        assert obj.getMaxDestinationPortNumber() is None
        assert obj.getMaxSourcePortNumber() is None
        assert obj.getMinDestinationPortNumber() is None
        assert obj.getMinSourcePortNumber() is None

    def test_docstrings_are_spec_note_verbatim(self):
        assert inspect.cleandoc(TransportLayerRule.getChecksumVerification.__doc__) == CHECKSUM_VERIFICATION_NOTE
        assert inspect.cleandoc(TransportLayerRule.setChecksumVerification.__doc__) == CHECKSUM_VERIFICATION_NOTE + "\nA None value is a no-op and does not overwrite an existing checksumVerification."
        assert inspect.cleandoc(TransportLayerRule.getMaxDestinationPortNumber.__doc__) == MAX_DESTINATION_PORT_NUMBER_NOTE
        assert (
            inspect.cleandoc(TransportLayerRule.setMaxDestinationPortNumber.__doc__)
            == MAX_DESTINATION_PORT_NUMBER_NOTE + "\nA None value is a no-op and does not overwrite an existing maxDestinationPortNumber."
        )
        assert inspect.cleandoc(TransportLayerRule.getMaxSourcePortNumber.__doc__) == MAX_SOURCE_PORT_NUMBER_NOTE
        assert inspect.cleandoc(TransportLayerRule.setMaxSourcePortNumber.__doc__) == MAX_SOURCE_PORT_NUMBER_NOTE + "\nA None value is a no-op and does not overwrite an existing maxSourcePortNumber."
        assert inspect.cleandoc(TransportLayerRule.getMinDestinationPortNumber.__doc__) == MIN_DESTINATION_PORT_NUMBER_NOTE
        assert (
            inspect.cleandoc(TransportLayerRule.setMinDestinationPortNumber.__doc__)
            == MIN_DESTINATION_PORT_NUMBER_NOTE + "\nA None value is a no-op and does not overwrite an existing minDestinationPortNumber."
        )
        assert inspect.cleandoc(TransportLayerRule.getMinSourcePortNumber.__doc__) == MIN_SOURCE_PORT_NUMBER_NOTE
        assert inspect.cleandoc(TransportLayerRule.setMinSourcePortNumber.__doc__) == MIN_SOURCE_PORT_NUMBER_NOTE + "\nA None value is a no-op and does not overwrite an existing minSourcePortNumber."

    def test_get_set_round_trip_and_none_noop(self):
        obj = TransportLayerRule()
        checksum_verification = _boolean(True)
        max_destination_port_number = _pos_int(8080)
        max_source_port_number = _pos_int(9090)
        min_destination_port_number = _pos_int(1000)
        min_source_port_number = _pos_int(2000)

        assert obj.setChecksumVerification(checksum_verification) is obj
        assert obj.setMaxDestinationPortNumber(max_destination_port_number) is obj
        assert obj.setMaxSourcePortNumber(max_source_port_number) is obj
        assert obj.setMinDestinationPortNumber(min_destination_port_number) is obj
        assert obj.setMinSourcePortNumber(min_source_port_number) is obj

        assert obj.getChecksumVerification() is checksum_verification
        assert obj.getMaxDestinationPortNumber() is max_destination_port_number
        assert obj.getMaxSourcePortNumber() is max_source_port_number
        assert obj.getMinDestinationPortNumber() is min_destination_port_number
        assert obj.getMinSourcePortNumber() is min_source_port_number

        obj.setChecksumVerification(None)
        obj.setMaxDestinationPortNumber(None)
        obj.setMaxSourcePortNumber(None)
        obj.setMinDestinationPortNumber(None)
        obj.setMinSourcePortNumber(None)
        assert obj.getChecksumVerification() is checksum_verification
        assert obj.getMaxDestinationPortNumber() is max_destination_port_number
        assert obj.getMaxSourcePortNumber() is max_source_port_number
        assert obj.getMinDestinationPortNumber() is min_destination_port_number
        assert obj.getMinSourcePortNumber() is min_source_port_number

    def test_get_type_hints_pins(self):
        hints = typing.get_type_hints(TransportLayerRule.setChecksumVerification)
        assert hints["return"] is TransportLayerRule
        assert hints["value"] == Optional[Boolean]
        hints = typing.get_type_hints(TransportLayerRule.setMaxDestinationPortNumber)
        assert hints["return"] is TransportLayerRule
        assert hints["value"] == Optional[PositiveInteger]
        hints = typing.get_type_hints(TransportLayerRule.setMaxSourcePortNumber)
        assert hints["return"] is TransportLayerRule
        assert hints["value"] == Optional[PositiveInteger]
        hints = typing.get_type_hints(TransportLayerRule.setMinDestinationPortNumber)
        assert hints["return"] is TransportLayerRule
        assert hints["value"] == Optional[PositiveInteger]
        hints = typing.get_type_hints(TransportLayerRule.setMinSourcePortNumber)
        assert hints["return"] is TransportLayerRule
        assert hints["value"] == Optional[PositiveInteger]
