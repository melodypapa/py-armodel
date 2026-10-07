import inspect
import typing

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import ARObject
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.InstanceRefs import OperationInSystemInstanceRef
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.SignalPaths import SwcToSwcOperationArguments, SwcToSwcOperationArgumentsDirectionEnum


class MockParent(ARObject):
    def __init__(self):
        super().__init__()


class TestSwcToSwcOperationArguments:
    """Test cases for SwcToSwcOperationArguments (Table 5.38, p.254)."""

    MEMBERS = [
        "direction",
        "operationIRefs",
    ]

    def test_inheritance(self):
        assert issubclass(SwcToSwcOperationArguments, ARObject)

    def test_class_docstring_note(self):
        expected = (
            "The SwcToSwcOperationArguments describes the information (client server operation arguments, plus the operation identification, if required) "
            "that are exchanged between two SW Components from exactly one client to one server, or from one server back to one client. "
            "The direction attribute defines which direction is described. If direction == IN, all arguments sent from the client to the server are described by the SwcToSwcOperationArguments, "
            "in direction == OUT, it's the arguments sent back from server to client."
        )
        assert inspect.cleandoc(SwcToSwcOperationArguments.__doc__) == expected

    def test_init_has_no_docstring(self):
        assert SwcToSwcOperationArguments.__init__.__doc__ is None

    def test_initialization_defaults(self):
        arguments = SwcToSwcOperationArguments()
        assert arguments.getDirection() is None
        assert arguments.getOperationIRefs() == []

    def test_member_order(self):
        arguments = SwcToSwcOperationArguments()
        members = [k for k in vars(arguments) if k in set(self.MEMBERS)]
        assert members == self.MEMBERS

    def test_get_set_direction(self):
        arguments = SwcToSwcOperationArguments()
        direction = SwcToSwcOperationArgumentsDirectionEnum()
        direction.setValue(SwcToSwcOperationArgumentsDirectionEnum.IN)
        result = arguments.setDirection(direction)
        assert result is arguments
        assert arguments.getDirection() is direction
        arguments.setDirection(None)
        assert arguments.getDirection() is direction

    def test_add_operation_i_ref(self):
        arguments = SwcToSwcOperationArguments()
        iref1 = OperationInSystemInstanceRef()
        iref2 = OperationInSystemInstanceRef()
        result = arguments.addOperationIRef(iref1)
        assert result is arguments
        arguments.addOperationIRef(iref2)
        assert arguments.getOperationIRefs() == [iref1, iref2]
        arguments.addOperationIRef(None)
        assert len(arguments.getOperationIRefs()) == 2

    def test_type_hints(self):
        hints = typing.get_type_hints(SwcToSwcOperationArguments.getDirection)
        assert hints["return"] == typing.Optional[SwcToSwcOperationArgumentsDirectionEnum]
        hints = typing.get_type_hints(SwcToSwcOperationArguments.setDirection)
        assert hints["value"] == typing.Optional[SwcToSwcOperationArgumentsDirectionEnum]
        assert hints["return"] is SwcToSwcOperationArguments
        hints = typing.get_type_hints(SwcToSwcOperationArguments.getOperationIRefs)
        assert hints["return"] == typing.List[OperationInSystemInstanceRef]
        hints = typing.get_type_hints(SwcToSwcOperationArguments.addOperationIRef)
        assert hints["value"] == typing.Optional[OperationInSystemInstanceRef]
        assert hints["return"] is SwcToSwcOperationArguments
