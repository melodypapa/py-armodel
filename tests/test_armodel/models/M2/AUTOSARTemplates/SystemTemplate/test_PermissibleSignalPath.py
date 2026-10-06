import inspect
import typing

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import RefType
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.SignalPaths import PermissibleSignalPath, SignalPathConstraint, SwcToSwcOperationArguments, SwcToSwcSignal


class TestPermissibleSignalPath:
    """Test cases for PermissibleSignalPath (Table 5.41, p.256)."""

    MEMBERS = [
        "operations",
        "physicalChannelRefs",
        "signals",
    ]

    def test_inheritance(self):
        assert issubclass(PermissibleSignalPath, SignalPathConstraint)

    def test_instantiable(self):
        PermissibleSignalPath()

    def test_class_docstring_note(self):
        expected = "The PermissibleSignalPath describes the way a data element shall take in the topology. The path is described by ordered references to PhysicalChannels. If more than one PermissibleSignalPath is defined for the same signal/operation attributes, any of them can be chosen. Such a signal path can be a constraint for the communication matrix . This path describes that one data element should take path A (e.g. 1. CAN channel, 2. LIN channel) and not path B (1. CAN channel, FlexRay channel A). This has an effect on the frame generation and the frame path."
        assert inspect.cleandoc(PermissibleSignalPath.__doc__) == expected

    def test_init_has_no_docstring(self):
        assert PermissibleSignalPath.__init__.__doc__ is None

    def test_initialization_defaults(self):
        path = PermissibleSignalPath()
        assert path.getOperations() == []
        assert path.getPhysicalChannelRefs() == []
        assert path.getSignals() == []
        assert path.getIntroduction() is None

    def test_member_order(self):
        path = PermissibleSignalPath()
        members = [k for k in vars(path) if k in set(self.MEMBERS)]
        assert members == self.MEMBERS

    def test_add_operation(self):
        path = PermissibleSignalPath()
        operation1 = SwcToSwcOperationArguments()
        operation2 = SwcToSwcOperationArguments()
        result = path.addOperation(operation1)
        assert result is path
        path.addOperation(operation2)
        assert path.getOperations() == [operation1, operation2]
        path.addOperation(None)
        assert len(path.getOperations()) == 2

    def test_add_physical_channel_ref(self):
        path = PermissibleSignalPath()
        ref1 = RefType()
        ref1.setValue("/Topology/Can1")
        ref2 = RefType()
        ref2.setValue("/Topology/Lin1")
        result = path.addPhysicalChannelRef(ref1)
        assert result is path
        path.addPhysicalChannelRef(ref2)
        assert path.getPhysicalChannelRefs() == [ref1, ref2]
        path.addPhysicalChannelRef(None)
        assert len(path.getPhysicalChannelRefs()) == 2

    def test_add_signal(self):
        path = PermissibleSignalPath()
        signal1 = SwcToSwcSignal()
        signal2 = SwcToSwcSignal()
        result = path.addSignal(signal1)
        assert result is path
        path.addSignal(signal2)
        assert path.getSignals() == [signal1, signal2]
        path.addSignal(None)
        assert len(path.getSignals()) == 2

    def test_type_hints(self):
        hints = typing.get_type_hints(PermissibleSignalPath.getOperations)
        assert hints["return"] == typing.List[SwcToSwcOperationArguments]
        hints = typing.get_type_hints(PermissibleSignalPath.addOperation)
        assert hints["value"] == typing.Optional[SwcToSwcOperationArguments]
        assert hints["return"] is PermissibleSignalPath
        hints = typing.get_type_hints(PermissibleSignalPath.getPhysicalChannelRefs)
        assert hints["return"] == typing.List[RefType]
        hints = typing.get_type_hints(PermissibleSignalPath.addPhysicalChannelRef)
        assert hints["value"] == typing.Optional[RefType]
        assert hints["return"] is PermissibleSignalPath
        hints = typing.get_type_hints(PermissibleSignalPath.getSignals)
        assert hints["return"] == typing.List[SwcToSwcSignal]
        hints = typing.get_type_hints(PermissibleSignalPath.addSignal)
        assert hints["value"] == typing.Optional[SwcToSwcSignal]
        assert hints["return"] is PermissibleSignalPath
