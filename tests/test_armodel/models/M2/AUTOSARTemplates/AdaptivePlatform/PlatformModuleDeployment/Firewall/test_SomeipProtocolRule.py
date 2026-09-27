import inspect
import typing
from typing import Optional

from armodel.models.M2.AUTOSARTemplates.AdaptivePlatform.PlatformModuleDeployment.Firewall import SomeipProtocolRule
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import Boolean, PositiveInteger

CLIENT_ID_NOTE = "Filter for SOME/IP messages in which the clientId in the SOME/IP header matches."
LENGTH_VERIFICATION_NOTE = "Defines whether length verification is performed or not."
MAJOR_VERSION_NOTE = "Filter for SOME/IP messages in which the majorVersion  in the SOME/IP header matches."
MESSAGE_TYPE_NOTE = "Filter for SOME/IP messages in which the messageType in the SOME/IP header matches."
METHOD_ID_NOTE = "Filter for SOME/IP messages in which the methodId in the SOME/IP header matches."
PROTOCOL_VERSION_NOTE = "Filter for SOME/IP messages in which the protocolVersion  in the SOME/IP header matches."
RETURN_CODE_NOTE = "Filter for SOME/IP messages in which the returnCode  in the SOME/IP header matches."
SERVICE_INTERFACE_ID_NOTE = "Filter for SOME/IP messages in which the serviceInterfaceId in the SOME/IP header matches."


def _pos_int(value):
    p = PositiveInteger()
    p.setValue(value)
    return p


def _boolean(value):
    b = Boolean()
    b.setValue(value)
    return b


class TestSomeipProtocolRule:
    def test_defaults_in_spec_displayed_order(self):
        obj = SomeipProtocolRule()
        assert isinstance(obj, ARObject)
        assert obj.getClientId() is None
        assert obj.getLengthVerification() is None
        assert obj.getMajorVersion() is None
        assert obj.getMessageType() is None
        assert obj.getMethodId() is None
        assert obj.getProtocolVersion() is None
        assert obj.getReturnCode() is None
        assert obj.getServiceInterfaceId() is None

    def test_class_docstring_is_spec_note_verbatim(self):
        assert SomeipProtocolRule.__doc__.strip() == "Configuration of SOME/IP firewall rules Tags: atp.Status=candidate"

    def test_docstrings_are_spec_note_verbatim(self):
        assert inspect.cleandoc(SomeipProtocolRule.getClientId.__doc__) == CLIENT_ID_NOTE
        assert inspect.cleandoc(SomeipProtocolRule.setClientId.__doc__) == CLIENT_ID_NOTE + "\nA None value is a no-op and does not overwrite an existing clientId."
        assert inspect.cleandoc(SomeipProtocolRule.getLengthVerification.__doc__) == LENGTH_VERIFICATION_NOTE
        assert inspect.cleandoc(SomeipProtocolRule.setLengthVerification.__doc__) == LENGTH_VERIFICATION_NOTE + "\nA None value is a no-op and does not overwrite an existing lengthVerification."
        assert inspect.cleandoc(SomeipProtocolRule.getMajorVersion.__doc__) == MAJOR_VERSION_NOTE
        assert inspect.cleandoc(SomeipProtocolRule.setMajorVersion.__doc__) == MAJOR_VERSION_NOTE + "\nA None value is a no-op and does not overwrite an existing majorVersion."
        assert inspect.cleandoc(SomeipProtocolRule.getMessageType.__doc__) == MESSAGE_TYPE_NOTE
        assert inspect.cleandoc(SomeipProtocolRule.setMessageType.__doc__) == MESSAGE_TYPE_NOTE + "\nA None value is a no-op and does not overwrite an existing messageType."
        assert inspect.cleandoc(SomeipProtocolRule.getMethodId.__doc__) == METHOD_ID_NOTE
        assert inspect.cleandoc(SomeipProtocolRule.setMethodId.__doc__) == METHOD_ID_NOTE + "\nA None value is a no-op and does not overwrite an existing methodId."
        assert inspect.cleandoc(SomeipProtocolRule.getProtocolVersion.__doc__) == PROTOCOL_VERSION_NOTE
        assert inspect.cleandoc(SomeipProtocolRule.setProtocolVersion.__doc__) == PROTOCOL_VERSION_NOTE + "\nA None value is a no-op and does not overwrite an existing protocolVersion."
        assert inspect.cleandoc(SomeipProtocolRule.getReturnCode.__doc__) == RETURN_CODE_NOTE
        assert inspect.cleandoc(SomeipProtocolRule.setReturnCode.__doc__) == RETURN_CODE_NOTE + "\nA None value is a no-op and does not overwrite an existing returnCode."
        assert inspect.cleandoc(SomeipProtocolRule.getServiceInterfaceId.__doc__) == SERVICE_INTERFACE_ID_NOTE
        assert inspect.cleandoc(SomeipProtocolRule.setServiceInterfaceId.__doc__) == SERVICE_INTERFACE_ID_NOTE + "\nA None value is a no-op and does not overwrite an existing serviceInterfaceId."

    def test_get_set_round_trip_and_none_noop(self):
        obj = SomeipProtocolRule()
        client_id = _pos_int(1)
        length_verification = _boolean(True)
        major_version = _pos_int(2)
        message_type = _pos_int(3)
        method_id = _pos_int(4)
        protocol_version = _pos_int(5)
        return_code = _pos_int(6)
        service_interface_id = _pos_int(7)

        assert obj.setClientId(client_id) is obj
        assert obj.setLengthVerification(length_verification) is obj
        assert obj.setMajorVersion(major_version) is obj
        assert obj.setMessageType(message_type) is obj
        assert obj.setMethodId(method_id) is obj
        assert obj.setProtocolVersion(protocol_version) is obj
        assert obj.setReturnCode(return_code) is obj
        assert obj.setServiceInterfaceId(service_interface_id) is obj

        assert obj.getClientId() is client_id
        assert obj.getLengthVerification() is length_verification
        assert obj.getMajorVersion() is major_version
        assert obj.getMessageType() is message_type
        assert obj.getMethodId() is method_id
        assert obj.getProtocolVersion() is protocol_version
        assert obj.getReturnCode() is return_code
        assert obj.getServiceInterfaceId() is service_interface_id

        obj.setClientId(None)
        obj.setLengthVerification(None)
        obj.setMajorVersion(None)
        obj.setMessageType(None)
        obj.setMethodId(None)
        obj.setProtocolVersion(None)
        obj.setReturnCode(None)
        obj.setServiceInterfaceId(None)
        assert obj.getClientId() is client_id
        assert obj.getLengthVerification() is length_verification
        assert obj.getMajorVersion() is major_version
        assert obj.getMessageType() is message_type
        assert obj.getMethodId() is method_id
        assert obj.getProtocolVersion() is protocol_version
        assert obj.getReturnCode() is return_code
        assert obj.getServiceInterfaceId() is service_interface_id

    def test_get_type_hints_pins(self):
        hints = typing.get_type_hints(SomeipProtocolRule.setClientId)
        assert hints["return"] is SomeipProtocolRule
        assert hints["value"] == Optional[PositiveInteger]
        hints = typing.get_type_hints(SomeipProtocolRule.setLengthVerification)
        assert hints["return"] is SomeipProtocolRule
        assert hints["value"] == Optional[Boolean]
