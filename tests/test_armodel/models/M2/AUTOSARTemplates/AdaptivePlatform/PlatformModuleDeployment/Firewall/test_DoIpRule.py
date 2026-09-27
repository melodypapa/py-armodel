import inspect
import typing
from typing import Optional

from armodel.models.M2.AUTOSARTemplates.AdaptivePlatform.PlatformModuleDeployment.Firewall import DoIpRule
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import PositiveInteger

DESTINATION_MAX_ADDRESS_NOTE = "Filter to match DoIP messages in which the destinationAddress is smaller or equal than destinationMaxAddress."
DESTINATION_MIN_ADDRESS_NOTE = "Filter to match DoIP messages in which the destinationAddress is greater or equal than destinationMinAddress."
INVERSE_PROTOCOL_VERSION_NOTE = "Filter to match DoIP messages  in which the inverseprotocolVersion in the DoIP header matches."
PAYLOAD_LENGTH_NOTE = "Filter to match DoIP messages  in which the payloadLength in the DoIP header matches."
PAYLOAD_TYPE_NOTE = "Filter to match DoIP messages  in which the payloadType in the DoIP header matches."
PROTOCOL_VERSION_NOTE = "Filter to match DoIP messages  in which the protocolVersion in the DoIP header matches."
SOURCE_MAX_ADDRESS_NOTE = "Filter to match DoIP messages in which the sourceAddress is smaller or equal than sourceMaxAddress."
SOURCE_MIN_ADDRESS_NOTE = "Filter to match DoIP messages in which the sourceAddress is greater or equal than sourceMinAddress.."
UDS_SERVICE_NOTE = "Filter to match DoIP messages that contain the udsService."


def _pos_int(value):
    p = PositiveInteger()
    p.setValue(value)
    return p


class TestDoIpRule:
    def test_defaults_in_spec_displayed_order(self):
        obj = DoIpRule()
        assert isinstance(obj, ARObject)
        assert obj.getDestinationMaxAddress() is None
        assert obj.getDestinationMinAddress() is None
        assert obj.getInverseProtocolVersion() is None
        assert obj.getPayloadLength() is None
        assert obj.getPayloadType() is None
        assert obj.getProtocolVersion() is None
        assert obj.getSourceMaxAddress() is None
        assert obj.getSourceMinAddress() is None
        assert obj.getUdsService() is None

    def test_class_docstring_is_spec_note_verbatim(self):
        assert DoIpRule.__doc__.strip() == "Configuration of a generic firewall rule Tags: atp.Status=candidate"

    def test_docstrings_are_spec_note_verbatim(self):
        assert inspect.cleandoc(DoIpRule.getDestinationMaxAddress.__doc__) == DESTINATION_MAX_ADDRESS_NOTE
        assert inspect.cleandoc(DoIpRule.setDestinationMaxAddress.__doc__) == DESTINATION_MAX_ADDRESS_NOTE + "\nA None value is a no-op and does not overwrite an existing destinationMaxAddress."
        assert inspect.cleandoc(DoIpRule.getDestinationMinAddress.__doc__) == DESTINATION_MIN_ADDRESS_NOTE
        assert inspect.cleandoc(DoIpRule.setDestinationMinAddress.__doc__) == DESTINATION_MIN_ADDRESS_NOTE + "\nA None value is a no-op and does not overwrite an existing destinationMinAddress."
        assert inspect.cleandoc(DoIpRule.getInverseProtocolVersion.__doc__) == INVERSE_PROTOCOL_VERSION_NOTE
        assert inspect.cleandoc(DoIpRule.setInverseProtocolVersion.__doc__) == INVERSE_PROTOCOL_VERSION_NOTE + "\nA None value is a no-op and does not overwrite an existing inverseProtocolVersion."
        assert inspect.cleandoc(DoIpRule.getPayloadLength.__doc__) == PAYLOAD_LENGTH_NOTE
        assert inspect.cleandoc(DoIpRule.setPayloadLength.__doc__) == PAYLOAD_LENGTH_NOTE + "\nA None value is a no-op and does not overwrite an existing payloadLength."
        assert inspect.cleandoc(DoIpRule.getPayloadType.__doc__) == PAYLOAD_TYPE_NOTE
        assert inspect.cleandoc(DoIpRule.setPayloadType.__doc__) == PAYLOAD_TYPE_NOTE + "\nA None value is a no-op and does not overwrite an existing payloadType."
        assert inspect.cleandoc(DoIpRule.getProtocolVersion.__doc__) == PROTOCOL_VERSION_NOTE
        assert inspect.cleandoc(DoIpRule.setProtocolVersion.__doc__) == PROTOCOL_VERSION_NOTE + "\nA None value is a no-op and does not overwrite an existing protocolVersion."
        assert inspect.cleandoc(DoIpRule.getSourceMaxAddress.__doc__) == SOURCE_MAX_ADDRESS_NOTE
        assert inspect.cleandoc(DoIpRule.setSourceMaxAddress.__doc__) == SOURCE_MAX_ADDRESS_NOTE + "\nA None value is a no-op and does not overwrite an existing sourceMaxAddress."
        assert inspect.cleandoc(DoIpRule.getSourceMinAddress.__doc__) == SOURCE_MIN_ADDRESS_NOTE
        assert inspect.cleandoc(DoIpRule.setSourceMinAddress.__doc__) == SOURCE_MIN_ADDRESS_NOTE + "\nA None value is a no-op and does not overwrite an existing sourceMinAddress."
        assert inspect.cleandoc(DoIpRule.getUdsService.__doc__) == UDS_SERVICE_NOTE
        assert inspect.cleandoc(DoIpRule.setUdsService.__doc__) == UDS_SERVICE_NOTE + "\nA None value is a no-op and does not overwrite an existing udsService."

    def test_get_set_round_trip_and_none_noop(self):
        obj = DoIpRule()
        destination_max_address = _pos_int(1)
        destination_min_address = _pos_int(2)
        inverse_protocol_version = _pos_int(3)
        payload_length = _pos_int(4)
        payload_type = _pos_int(5)
        protocol_version = _pos_int(6)
        source_max_address = _pos_int(7)
        source_min_address = _pos_int(8)
        uds_service = _pos_int(9)

        assert obj.setDestinationMaxAddress(destination_max_address) is obj
        assert obj.setDestinationMinAddress(destination_min_address) is obj
        assert obj.setInverseProtocolVersion(inverse_protocol_version) is obj
        assert obj.setPayloadLength(payload_length) is obj
        assert obj.setPayloadType(payload_type) is obj
        assert obj.setProtocolVersion(protocol_version) is obj
        assert obj.setSourceMaxAddress(source_max_address) is obj
        assert obj.setSourceMinAddress(source_min_address) is obj
        assert obj.setUdsService(uds_service) is obj

        assert obj.getDestinationMaxAddress() is destination_max_address
        assert obj.getDestinationMinAddress() is destination_min_address
        assert obj.getInverseProtocolVersion() is inverse_protocol_version
        assert obj.getPayloadLength() is payload_length
        assert obj.getPayloadType() is payload_type
        assert obj.getProtocolVersion() is protocol_version
        assert obj.getSourceMaxAddress() is source_max_address
        assert obj.getSourceMinAddress() is source_min_address
        assert obj.getUdsService() is uds_service

        obj.setDestinationMaxAddress(None)
        obj.setDestinationMinAddress(None)
        obj.setInverseProtocolVersion(None)
        obj.setPayloadLength(None)
        obj.setPayloadType(None)
        obj.setProtocolVersion(None)
        obj.setSourceMaxAddress(None)
        obj.setSourceMinAddress(None)
        obj.setUdsService(None)
        assert obj.getDestinationMaxAddress() is destination_max_address
        assert obj.getDestinationMinAddress() is destination_min_address
        assert obj.getInverseProtocolVersion() is inverse_protocol_version
        assert obj.getPayloadLength() is payload_length
        assert obj.getPayloadType() is payload_type
        assert obj.getProtocolVersion() is protocol_version
        assert obj.getSourceMaxAddress() is source_max_address
        assert obj.getSourceMinAddress() is source_min_address
        assert obj.getUdsService() is uds_service

    def test_get_type_hints_pins(self):
        hints = typing.get_type_hints(DoIpRule.setDestinationMaxAddress)
        assert hints["return"] is DoIpRule
        assert hints["value"] == Optional[PositiveInteger]
        hints = typing.get_type_hints(DoIpRule.setUdsService)
        assert hints["return"] is DoIpRule
        assert hints["value"] == Optional[PositiveInteger]
