import inspect
import typing

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import RefType
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.SignalPaths import ForbiddenSignalPath, SignalPathConstraint, SwcToSwcOperationArguments, SwcToSwcSignal


class TestForbiddenSignalPath:
    """Test cases for ForbiddenSignalPath (Table 5.40, p.255)."""

    MEMBERS = [
        "operations",
        "physicalChannelRefs",
        "signals",
    ]

    def test_inheritance(self):
        assert issubclass(ForbiddenSignalPath, SignalPathConstraint)

    def test_instantiable(self):
        ForbiddenSignalPath()

    def test_class_docstring_note(self):
        expected = "The ForbiddenSignalPath describes the physical channels which an element shall not take in the topology. Such a signal path can be a constraint for the communication matrix, because such a path has an effect on the frame generation and the frame path."
        assert inspect.cleandoc(ForbiddenSignalPath.__doc__) == expected

    def test_init_has_no_docstring(self):
        assert ForbiddenSignalPath.__init__.__doc__ is None

    def test_initialization_defaults(self):
        path = ForbiddenSignalPath()
        assert path.getOperations() == []
        assert path.getPhysicalChannelRefs() == []
        assert path.getSignals() == []
        assert path.getIntroduction() is None

    def test_member_order(self):
        path = ForbiddenSignalPath()
        members = [k for k in vars(path) if k in set(self.MEMBERS)]
        assert members == self.MEMBERS

    def test_add_operation(self):
        path = ForbiddenSignalPath()
        operation1 = SwcToSwcOperationArguments()
        operation2 = SwcToSwcOperationArguments()
        result = path.addOperation(operation1)
        assert result is path
        path.addOperation(operation2)
        assert path.getOperations() == [operation1, operation2]
        path.addOperation(None)
        assert len(path.getOperations()) == 2

    def test_add_physical_channel_ref(self):
        path = ForbiddenSignalPath()
        ref1 = RefType()
        ref1.setValue("/Topology/Can1")
        ref2 = RefType()
        ref2.setValue("/Topology/Can2")
        result = path.addPhysicalChannelRef(ref1)
        assert result is path
        path.addPhysicalChannelRef(ref2)
        assert path.getPhysicalChannelRefs() == [ref1, ref2]
        path.addPhysicalChannelRef(None)
        assert len(path.getPhysicalChannelRefs()) == 2

    def test_add_signal(self):
        path = ForbiddenSignalPath()
        signal1 = SwcToSwcSignal()
        signal2 = SwcToSwcSignal()
        result = path.addSignal(signal1)
        assert result is path
        path.addSignal(signal2)
        assert path.getSignals() == [signal1, signal2]
        path.addSignal(None)
        assert len(path.getSignals()) == 2

    def test_type_hints(self):
        hints = typing.get_type_hints(ForbiddenSignalPath.getOperations)
        assert hints["return"] == typing.List[SwcToSwcOperationArguments]
        hints = typing.get_type_hints(ForbiddenSignalPath.addOperation)
        assert hints["value"] == typing.Optional[SwcToSwcOperationArguments]
        assert hints["return"] is ForbiddenSignalPath
        hints = typing.get_type_hints(ForbiddenSignalPath.getPhysicalChannelRefs)
        assert hints["return"] == typing.List[RefType]
        hints = typing.get_type_hints(ForbiddenSignalPath.addPhysicalChannelRef)
        assert hints["value"] == typing.Optional[RefType]
        assert hints["return"] is ForbiddenSignalPath
        hints = typing.get_type_hints(ForbiddenSignalPath.getSignals)
        assert hints["return"] == typing.List[SwcToSwcSignal]
        hints = typing.get_type_hints(ForbiddenSignalPath.addSignal)
        assert hints["value"] == typing.Optional[SwcToSwcSignal]
        assert hints["return"] is ForbiddenSignalPath
