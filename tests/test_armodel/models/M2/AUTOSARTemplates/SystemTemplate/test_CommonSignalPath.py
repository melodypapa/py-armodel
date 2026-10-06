import inspect
import typing

from armodel.models.M2.AUTOSARTemplates.SystemTemplate.SignalPaths import CommonSignalPath, SignalPathConstraint, SwcToSwcOperationArguments, SwcToSwcSignal


class TestCommonSignalPath:
    """Test cases for CommonSignalPath (Table 5.36, p.253)."""

    MEMBERS = [
        "operations",
        "signals",
    ]

    def test_inheritance(self):
        assert issubclass(CommonSignalPath, SignalPathConstraint)

    def test_instantiable(self):
        CommonSignalPath()

    def test_class_docstring_note(self):
        expected = "The CommonSignalPath describes that two or more SwcToSwcSignals and/or SwcToSwcOperationArguments shall take the same way (Signal Path) in the topology."
        assert inspect.cleandoc(CommonSignalPath.__doc__) == expected

    def test_init_has_no_docstring(self):
        assert CommonSignalPath.__init__.__doc__ is None

    def test_initialization_defaults(self):
        path = CommonSignalPath()
        assert path.getOperations() == []
        assert path.getSignals() == []
        assert path.getIntroduction() is None

    def test_member_order(self):
        path = CommonSignalPath()
        members = [k for k in vars(path) if k in set(self.MEMBERS)]
        assert members == self.MEMBERS

    def test_add_operation(self):
        path = CommonSignalPath()
        operation1 = SwcToSwcOperationArguments()
        operation2 = SwcToSwcOperationArguments()
        result = path.addOperation(operation1)
        assert result is path
        path.addOperation(operation2)
        assert path.getOperations() == [operation1, operation2]
        path.addOperation(None)
        assert len(path.getOperations()) == 2

    def test_add_signal(self):
        path = CommonSignalPath()
        signal1 = SwcToSwcSignal()
        signal2 = SwcToSwcSignal()
        result = path.addSignal(signal1)
        assert result is path
        path.addSignal(signal2)
        assert path.getSignals() == [signal1, signal2]
        path.addSignal(None)
        assert len(path.getSignals()) == 2

    def test_type_hints(self):
        hints = typing.get_type_hints(CommonSignalPath.getOperations)
        assert hints["return"] == typing.List[SwcToSwcOperationArguments]
        hints = typing.get_type_hints(CommonSignalPath.addOperation)
        assert hints["value"] == typing.Optional[SwcToSwcOperationArguments]
        assert hints["return"] is CommonSignalPath
        hints = typing.get_type_hints(CommonSignalPath.getSignals)
        assert hints["return"] == typing.List[SwcToSwcSignal]
        hints = typing.get_type_hints(CommonSignalPath.addSignal)
        assert hints["value"] == typing.Optional[SwcToSwcSignal]
        assert hints["return"] is CommonSignalPath
