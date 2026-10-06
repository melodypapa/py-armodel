import inspect
import typing

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable import Identifiable
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import PositiveInteger, RefType
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.InstanceRefs import RteEventInCompositionInstanceRef
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.RteEventToOsTaskMapping import RteEventInCompositionToOsTaskProxyMapping


class MockParent(ARObject):
    def __init__(self):
        super().__init__()


class TestRteEventInCompositionToOsTaskProxyMapping:
    """Test cases for RteEventInCompositionToOsTaskProxyMapping (Table 5.18, p.212)."""

    MEMBERS = [
        "offset",
        "osTaskProxyRef",
        "rteEventIRef",
    ]

    def test_inheritance(self):
        assert issubclass(RteEventInCompositionToOsTaskProxyMapping, Identifiable)

    def test_class_docstring_note(self):
        expected = (
            "This meta-class is used to map an RteEvent to an OsTaskProxy in the context of a SwComposition. "
            "Several RteEventInCompositionToOsTaskProxyMappings can be used to define a pairing constraint that describes which RteEvents shall be mapped together into an OsTask. "
            "Optionally the relative position of the RteEvents in the OsTask can be defined in the mapping."
        )
        assert inspect.cleandoc(RteEventInCompositionToOsTaskProxyMapping.__doc__) == expected

    def test_init_has_no_docstring(self):
        assert RteEventInCompositionToOsTaskProxyMapping.__init__.__doc__ is None

    def test_initialization_defaults(self):
        mapping = RteEventInCompositionToOsTaskProxyMapping(MockParent(), "mapping")
        assert mapping.getOffset() is None
        assert mapping.getOsTaskProxyRef() is None
        assert mapping.getRteEventIRef() is None

    def test_member_order(self):
        mapping = RteEventInCompositionToOsTaskProxyMapping(MockParent(), "mapping")
        members = [k for k in vars(mapping) if k in set(self.MEMBERS)]
        assert members == self.MEMBERS

    def test_get_set_offset(self):
        mapping = RteEventInCompositionToOsTaskProxyMapping(MockParent(), "mapping")
        offset = PositiveInteger()
        offset.setValue("4")
        result = mapping.setOffset(offset)
        assert result is mapping
        assert mapping.getOffset() is offset
        mapping.setOffset(None)
        assert mapping.getOffset() is offset

    def test_get_set_os_task_proxy_ref(self):
        mapping = RteEventInCompositionToOsTaskProxyMapping(MockParent(), "mapping")
        ref = RefType()
        ref.setValue("/OsTaskProxies/TaskProxy1")
        ref.setDest("OS-TASK-PROXY")
        result = mapping.setOsTaskProxyRef(ref)
        assert result is mapping
        assert mapping.getOsTaskProxyRef() is ref
        assert mapping.getOsTaskProxyRef().getValue() == "/OsTaskProxies/TaskProxy1"
        mapping.setOsTaskProxyRef(None)
        assert mapping.getOsTaskProxyRef() is ref

    def test_get_set_rte_event_i_ref(self):
        mapping = RteEventInCompositionToOsTaskProxyMapping(MockParent(), "mapping")
        iref = RteEventInCompositionInstanceRef()
        result = mapping.setRteEventIRef(iref)
        assert result is mapping
        assert mapping.getRteEventIRef() is iref
        mapping.setRteEventIRef(None)
        assert mapping.getRteEventIRef() is iref

    def test_type_hints(self):
        hints = typing.get_type_hints(RteEventInCompositionToOsTaskProxyMapping.setOffset)
        assert hints["return"] is RteEventInCompositionToOsTaskProxyMapping
        hints = typing.get_type_hints(RteEventInCompositionToOsTaskProxyMapping.getRteEventIRef)
        assert hints["return"] == typing.Optional[RteEventInCompositionInstanceRef]
