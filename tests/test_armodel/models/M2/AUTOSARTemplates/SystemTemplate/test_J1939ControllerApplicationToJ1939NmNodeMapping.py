import inspect
import typing

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import RefType
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.SWmapping import J1939ControllerApplicationToJ1939NmNodeMapping


class TestJ1939ControllerApplicationToJ1939NmNodeMapping:
    """Test cases for J1939ControllerApplicationToJ1939NmNodeMapping (Table 5.12, p.207)."""

    MEMBERS = [
        "j1939ControllerApplicationRef",
        "j1939NmNodeRef",
    ]

    def test_inheritance(self):
        assert issubclass(J1939ControllerApplicationToJ1939NmNodeMapping, ARObject)

    def test_class_docstring_note(self):
        expected = "This meta-class represents the ability to map a J1939ControllerApplication to a J1939NmNode. Note that this is similar but not identical to the mapping of SwComponentPrototypes to EcuInstances; for J1939 the semantics of an EcuInstance itself is basically replaced by a J1939NmNode."
        assert inspect.cleandoc(J1939ControllerApplicationToJ1939NmNodeMapping.__doc__) == expected

    def test_init_has_no_docstring(self):
        assert J1939ControllerApplicationToJ1939NmNodeMapping.__init__.__doc__ is None

    def test_initialization_defaults(self):
        mapping = J1939ControllerApplicationToJ1939NmNodeMapping()
        assert mapping.getJ1939ControllerApplicationRef() is None
        assert mapping.getJ1939NmNodeRef() is None

    def test_member_order(self):
        mapping = J1939ControllerApplicationToJ1939NmNodeMapping()
        members = [k for k in vars(mapping) if k in set(self.MEMBERS)]
        assert members == self.MEMBERS

    def test_get_set_j1939_controller_application_ref(self):
        mapping = J1939ControllerApplicationToJ1939NmNodeMapping()
        value = RefType()
        value.setValue("/J1939ControllerApplications/J1939ControllerApplication")
        value.setDest("J-1939-CONTROLLER-APPLICATION")
        result = mapping.setJ1939ControllerApplicationRef(value)
        assert result is mapping
        assert mapping.getJ1939ControllerApplicationRef() is value
        mapping.setJ1939ControllerApplicationRef(None)
        assert mapping.getJ1939ControllerApplicationRef() is value

    def test_get_set_j1939_nm_node_ref(self):
        mapping = J1939ControllerApplicationToJ1939NmNodeMapping()
        value = RefType()
        value.setValue("J1939NmNodes/J1939NmNode")
        value.setDest("J-1939-NM-NODE")
        result = mapping.setJ1939NmNodeRef(value)
        assert result is mapping
        assert mapping.getJ1939NmNodeRef() is value
        mapping.setJ1939NmNodeRef(None)
        assert mapping.getJ1939NmNodeRef() is value

    def test_type_hints(self):
        hints = typing.get_type_hints(J1939ControllerApplicationToJ1939NmNodeMapping.getJ1939ControllerApplicationRef)
        assert hints.get("return") == typing.Optional[RefType]
        hints = typing.get_type_hints(J1939ControllerApplicationToJ1939NmNodeMapping.setJ1939ControllerApplicationRef)
        assert hints.get("value") == typing.Optional[RefType]
        assert hints.get("return") is J1939ControllerApplicationToJ1939NmNodeMapping
        hints = typing.get_type_hints(J1939ControllerApplicationToJ1939NmNodeMapping.getJ1939NmNodeRef)
        assert hints.get("return") == typing.Optional[RefType]
        hints = typing.get_type_hints(J1939ControllerApplicationToJ1939NmNodeMapping.setJ1939NmNodeRef)
        assert hints.get("value") == typing.Optional[RefType]
        assert hints.get("return") is J1939ControllerApplicationToJ1939NmNodeMapping
