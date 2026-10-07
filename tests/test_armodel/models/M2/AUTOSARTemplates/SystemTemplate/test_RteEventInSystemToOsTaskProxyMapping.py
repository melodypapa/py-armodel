import inspect
import typing

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable import Identifiable
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import Integer, RefType
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.InstanceRefs import RteEventInSystemInstanceRef
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.RteEventToOsTaskMapping import RteEventInSystemToOsTaskProxyMapping


class MockParent(ARObject):
    def __init__(self):
        super().__init__()


class TestRteEventInSystemToOsTaskProxyMapping:
    """Test cases for RteEventInSystemToOsTaskProxyMapping (Table 5.20, p.214)."""

    MEMBERS = [
        "offset",
        "osTaskProxyRef",
        "rteEventIRef",
    ]

    def test_inheritance(self):
        assert issubclass(RteEventInSystemToOsTaskProxyMapping, Identifiable)

    def test_class_docstring_note(self):
        expected = (
            "This meta-class is used to map an RteEvent to an OsTaskProxy in the context of the System. "
            "Several Rte EventToOsTaskProxyMappings can be used to define a pairing constraint that describes which Rte Events shall be mapped together into an OsTask. "
            "Optionally the position of the RteEvents in the OsTask can be defined."
        )
        assert inspect.cleandoc(RteEventInSystemToOsTaskProxyMapping.__doc__) == expected

    def test_init_has_no_docstring(self):
        assert RteEventInSystemToOsTaskProxyMapping.__init__.__doc__ is None

    def test_initialization_defaults(self):
        mapping = RteEventInSystemToOsTaskProxyMapping(MockParent(), "mapping")
        assert mapping.getOffset() is None
        assert mapping.getOsTaskProxyRef() is None
        assert mapping.getRteEventIRef() is None

    def test_member_order(self):
        mapping = RteEventInSystemToOsTaskProxyMapping(MockParent(), "mapping")
        members = [k for k in vars(mapping) if k in set(self.MEMBERS)]
        assert members == self.MEMBERS

    def test_get_set_offset(self):
        mapping = RteEventInSystemToOsTaskProxyMapping(MockParent(), "mapping")
        offset = Integer()
        offset.setValue("2")
        result = mapping.setOffset(offset)
        assert result is mapping
        assert mapping.getOffset() is offset
        mapping.setOffset(None)
        assert mapping.getOffset() is offset

    def test_get_set_os_task_proxy_ref(self):
        mapping = RteEventInSystemToOsTaskProxyMapping(MockParent(), "mapping")
        ref = RefType()
        ref.setValue("/OsTaskProxies/TaskProxy2")
        ref.setDest("OS-TASK-PROXY")
        result = mapping.setOsTaskProxyRef(ref)
        assert result is mapping
        assert mapping.getOsTaskProxyRef() is ref
        assert mapping.getOsTaskProxyRef().getValue() == "/OsTaskProxies/TaskProxy2"
        mapping.setOsTaskProxyRef(None)
        assert mapping.getOsTaskProxyRef() is ref

    def test_get_set_rte_event_i_ref(self):
        mapping = RteEventInSystemToOsTaskProxyMapping(MockParent(), "mapping")
        iref = RteEventInSystemInstanceRef()
        result = mapping.setRteEventIRef(iref)
        assert result is mapping
        assert mapping.getRteEventIRef() is iref
        mapping.setRteEventIRef(None)
        assert mapping.getRteEventIRef() is iref

    def test_type_hints(self):
        hints = typing.get_type_hints(RteEventInSystemToOsTaskProxyMapping.setOffset)
        assert hints["return"] is RteEventInSystemToOsTaskProxyMapping
        hints = typing.get_type_hints(RteEventInSystemToOsTaskProxyMapping.getRteEventIRef)
        assert hints["return"] == typing.Optional[RteEventInSystemInstanceRef]
