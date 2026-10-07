import inspect
import typing

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable import Identifiable
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.InstanceRefs import RteEventInSystemInstanceRef
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.RteEventToOsTaskMapping import RteEventInSystemSeparation


class MockParent(ARObject):
    def __init__(self):
        super().__init__()


class TestRteEventInSystemSeparation:
    """Test cases for RteEventInSystemSeparation (Table 5.21, p.214)."""

    MEMBERS = [
        "rteEventIRefs",
    ]

    def test_inheritance(self):
        assert issubclass(RteEventInSystemSeparation, Identifiable)

    def test_class_docstring_note(self):
        expected = "This meta-class is used to define a separation constraint in the context of the System. " "The referenced RteEvents are not allowed to be mapped into the same OsTask."
        assert inspect.cleandoc(RteEventInSystemSeparation.__doc__) == expected

    def test_init_has_no_docstring(self):
        assert RteEventInSystemSeparation.__init__.__doc__ is None

    def test_initialization_defaults(self):
        separation = RteEventInSystemSeparation(MockParent(), "sep")
        assert separation.getRteEventIRefs() == []

    def test_member_order(self):
        separation = RteEventInSystemSeparation(MockParent(), "sep")
        members = [k for k in vars(separation) if k in set(self.MEMBERS)]
        assert members == self.MEMBERS

    def test_add_rte_event_i_ref(self):
        separation = RteEventInSystemSeparation(MockParent(), "sep")
        iref1 = RteEventInSystemInstanceRef()
        iref2 = RteEventInSystemInstanceRef()
        result = separation.addRteEventIRef(iref1)
        assert result is separation
        separation.addRteEventIRef(iref2)
        assert separation.getRteEventIRefs() == [iref1, iref2]
        separation.addRteEventIRef(None)
        assert len(separation.getRteEventIRefs()) == 2

    def test_type_hints(self):
        hints = typing.get_type_hints(RteEventInSystemSeparation.getRteEventIRefs)
        assert hints["return"] == typing.List[RteEventInSystemInstanceRef]
        hints = typing.get_type_hints(RteEventInSystemSeparation.addRteEventIRef)
        assert hints["return"] is RteEventInSystemSeparation
