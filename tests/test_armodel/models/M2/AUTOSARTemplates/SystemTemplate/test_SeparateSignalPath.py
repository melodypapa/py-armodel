import inspect
import typing

from armodel.models.M2.AUTOSARTemplates.SystemTemplate.SignalPaths import SeparateSignalPath, SignalPathConstraint, SwcToSwcOperationArguments, SwcToSwcSignal


class TestSeparateSignalPath:
    """Test cases for SeparateSignalPath (Table 5.42, p.257)."""

    MEMBERS = [
        "operations",
        "signals",
    ]

    def test_inheritance(self):
        assert issubclass(SeparateSignalPath, SignalPathConstraint)

    def test_instantiable(self):
        SeparateSignalPath()

    def test_class_docstring_note(self):
        expected = "The SeparateSignalPath describes that two SwcToSwcSignals and/or SwcToSwcOperationArguments shall not take the same way (Signal Path) in the topology (e.g. Redundancy). This means that the signals are not allowed to share even a single physical channel in their path."
        assert inspect.cleandoc(SeparateSignalPath.__doc__) == expected

    def test_init_has_no_docstring(self):
        assert SeparateSignalPath.__init__.__doc__ is None

    def test_initialization_defaults(self):
        path = SeparateSignalPath()
        assert path.getOperations() == []
        assert path.getSignals() == []
        assert path.getIntroduction() is None

    def test_member_order(self):
        path = SeparateSignalPath()
        members = [k for k in vars(path) if k in set(self.MEMBERS)]
        assert members == self.MEMBERS

    def test_add_operation(self):
        path = SeparateSignalPath()
        operation1 = SwcToSwcOperationArguments()
        operation2 = SwcToSwcOperationArguments()
        result = path.addOperation(operation1)
        assert result is path
        path.addOperation(operation2)
        assert path.getOperations() == [operation1, operation2]
        path.addOperation(None)
        assert len(path.getOperations()) == 2

    def test_add_signal(self):
        path = SeparateSignalPath()
        signal1 = SwcToSwcSignal()
        signal2 = SwcToSwcSignal()
        result = path.addSignal(signal1)
        assert result is path
        path.addSignal(signal2)
        assert path.getSignals() == [signal1, signal2]
        path.addSignal(None)
        assert len(path.getSignals()) == 2

    def test_type_hints(self):
        hints = typing.get_type_hints(SeparateSignalPath.getOperations)
        assert hints["return"] == typing.List[SwcToSwcOperationArguments]
        hints = typing.get_type_hints(SeparateSignalPath.addOperation)
        assert hints["value"] == typing.Optional[SwcToSwcOperationArguments]
        assert hints["return"] is SeparateSignalPath
        hints = typing.get_type_hints(SeparateSignalPath.getSignals)
        assert hints["return"] == typing.List[SwcToSwcSignal]
        hints = typing.get_type_hints(SeparateSignalPath.addSignal)
        assert hints["value"] == typing.Optional[SwcToSwcSignal]
        assert hints["return"] is SeparateSignalPath
