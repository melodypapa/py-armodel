import inspect
import typing
from typing import Optional

from armodel.models.M2.AUTOSARTemplates.AdaptivePlatform.PlatformModuleDeployment.Firewall import SomeipSdRule
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import PositiveInteger

ENTRY_TYPE_NOTE = "Filter for SOME/IP SD messages in which the entryType in the SOME/IP header matches."
EVENT_GROUP_ID_NOTE = "Filter for SOME/IP SD messages in which the eventGroupId in the SOME/IP header matches."
MAX_MAJOR_VERSION_NOTE = "Filter for SOME/IP SD messages in which the MajorVersion in the SOME/IP header is smaller or equal than maxMajorVersion."
MAX_MINOR_VERSION_NOTE = "Filter for SOME/IP SD messages in which the MinorVersion in the SOME/IP header is smaller or equal than maxMinorVersion."
MIN_MAJOR_VERSION_NOTE = "Filter for SOME/IP SD messages in which the MajorVersion in the SOME/IP header is greater or equal than minMajorVersion."
MIN_MINOR_VERSION_NOTE = "Filter for SOME/IP SD messages in which the MinorVersion in the SOME/IP header is greater or equal than minMinorVersion."
SERVICE_INSTANCE_ID_NOTE = "Filter for SOME/IP SD messages in which the serviceInstanceId in the SOME/IP header matches."
SERVICE_INTERFACE_ID_NOTE = "Filter for SOME/IP SD messages in which the serviceInterfaceId in the SOME/IP header matches."


def _pos_int(value):
    p = PositiveInteger()
    p.setValue(value)
    return p


class TestSomeipSdRule:
    def test_defaults_in_spec_displayed_order(self):
        obj = SomeipSdRule()
        assert isinstance(obj, ARObject)
        assert obj.getEntryType() is None
        assert obj.getEventGroupId() is None
        assert obj.getMaxMajorVersion() is None
        assert obj.getMaxMinorVersion() is None
        assert obj.getMinMajorVersion() is None
        assert obj.getMinMinorVersion() is None
        assert obj.getServiceInstanceId() is None
        assert obj.getServiceInterfaceId() is None

    def test_class_docstring_is_spec_note_verbatim(self):
        assert SomeipSdRule.__doc__.strip() == "Configuration of SOME/IP Service Discovery firewall rules Tags: atp.Status=candidate"

    def test_docstrings_are_spec_note_verbatim(self):
        assert inspect.cleandoc(SomeipSdRule.getEntryType.__doc__) == ENTRY_TYPE_NOTE
        assert inspect.cleandoc(SomeipSdRule.setEntryType.__doc__) == ENTRY_TYPE_NOTE + "\nA None value is a no-op and does not overwrite an existing entryType."
        assert inspect.cleandoc(SomeipSdRule.getEventGroupId.__doc__) == EVENT_GROUP_ID_NOTE
        assert inspect.cleandoc(SomeipSdRule.setEventGroupId.__doc__) == EVENT_GROUP_ID_NOTE + "\nA None value is a no-op and does not overwrite an existing eventGroupId."
        assert inspect.cleandoc(SomeipSdRule.getMaxMajorVersion.__doc__) == MAX_MAJOR_VERSION_NOTE
        assert inspect.cleandoc(SomeipSdRule.setMaxMajorVersion.__doc__) == MAX_MAJOR_VERSION_NOTE + "\nA None value is a no-op and does not overwrite an existing maxMajorVersion."
        assert inspect.cleandoc(SomeipSdRule.getMaxMinorVersion.__doc__) == MAX_MINOR_VERSION_NOTE
        assert inspect.cleandoc(SomeipSdRule.setMaxMinorVersion.__doc__) == MAX_MINOR_VERSION_NOTE + "\nA None value is a no-op and does not overwrite an existing maxMinorVersion."
        assert inspect.cleandoc(SomeipSdRule.getMinMajorVersion.__doc__) == MIN_MAJOR_VERSION_NOTE
        assert inspect.cleandoc(SomeipSdRule.setMinMajorVersion.__doc__) == MIN_MAJOR_VERSION_NOTE + "\nA None value is a no-op and does not overwrite an existing minMajorVersion."
        assert inspect.cleandoc(SomeipSdRule.getMinMinorVersion.__doc__) == MIN_MINOR_VERSION_NOTE
        assert inspect.cleandoc(SomeipSdRule.setMinMinorVersion.__doc__) == MIN_MINOR_VERSION_NOTE + "\nA None value is a no-op and does not overwrite an existing minMinorVersion."
        assert inspect.cleandoc(SomeipSdRule.getServiceInstanceId.__doc__) == SERVICE_INSTANCE_ID_NOTE
        assert inspect.cleandoc(SomeipSdRule.setServiceInstanceId.__doc__) == SERVICE_INSTANCE_ID_NOTE + "\nA None value is a no-op and does not overwrite an existing serviceInstanceId."
        assert inspect.cleandoc(SomeipSdRule.getServiceInterfaceId.__doc__) == SERVICE_INTERFACE_ID_NOTE
        assert inspect.cleandoc(SomeipSdRule.setServiceInterfaceId.__doc__) == SERVICE_INTERFACE_ID_NOTE + "\nA None value is a no-op and does not overwrite an existing serviceInterfaceId."

    def test_get_set_round_trip_and_none_noop(self):
        obj = SomeipSdRule()
        entry_type = _pos_int(1)
        event_group_id = _pos_int(2)
        max_major_version = _pos_int(3)
        max_minor_version = _pos_int(4)
        min_major_version = _pos_int(5)
        min_minor_version = _pos_int(6)
        service_instance_id = _pos_int(7)
        service_interface_id = _pos_int(8)

        assert obj.setEntryType(entry_type) is obj
        assert obj.setEventGroupId(event_group_id) is obj
        assert obj.setMaxMajorVersion(max_major_version) is obj
        assert obj.setMaxMinorVersion(max_minor_version) is obj
        assert obj.setMinMajorVersion(min_major_version) is obj
        assert obj.setMinMinorVersion(min_minor_version) is obj
        assert obj.setServiceInstanceId(service_instance_id) is obj
        assert obj.setServiceInterfaceId(service_interface_id) is obj

        assert obj.getEntryType() is entry_type
        assert obj.getEventGroupId() is event_group_id
        assert obj.getMaxMajorVersion() is max_major_version
        assert obj.getMaxMinorVersion() is max_minor_version
        assert obj.getMinMajorVersion() is min_major_version
        assert obj.getMinMinorVersion() is min_minor_version
        assert obj.getServiceInstanceId() is service_instance_id
        assert obj.getServiceInterfaceId() is service_interface_id

        obj.setEntryType(None)
        obj.setEventGroupId(None)
        obj.setMaxMajorVersion(None)
        obj.setMaxMinorVersion(None)
        obj.setMinMajorVersion(None)
        obj.setMinMinorVersion(None)
        obj.setServiceInstanceId(None)
        obj.setServiceInterfaceId(None)
        assert obj.getEntryType() is entry_type
        assert obj.getEventGroupId() is event_group_id
        assert obj.getMaxMajorVersion() is max_major_version
        assert obj.getMaxMinorVersion() is max_minor_version
        assert obj.getMinMajorVersion() is min_major_version
        assert obj.getMinMinorVersion() is min_minor_version
        assert obj.getServiceInstanceId() is service_instance_id
        assert obj.getServiceInterfaceId() is service_interface_id

    def test_get_type_hints_pins(self):
        hints = typing.get_type_hints(SomeipSdRule.setEntryType)
        assert hints["return"] is SomeipSdRule
        assert hints["value"] == Optional[PositiveInteger]
        hints = typing.get_type_hints(SomeipSdRule.setServiceInterfaceId)
        assert hints["return"] is SomeipSdRule
        assert hints["value"] == Optional[PositiveInteger]
