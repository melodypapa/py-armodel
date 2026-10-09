import inspect

from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.Communication import HandleOutOfRangeEnum
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore.CoreCommunication import ISignalProps

CLASS_NOTE = "Additional ISignal properties that may be stored in different files."
HANDLE_OUT_OF_RANGE_NOTE = "This attribute defines the outOfRangeHandling for received and sent signals."


class TestISignalProps:
    """Test cases for ISignalProps class (Table 6.10, p.323)."""

    def test_initialization_defaults(self):
        props = ISignalProps()
        assert props.getHandleOutOfRange() is None

    def test_get_set_handle_out_of_range(self):
        props = ISignalProps()

        value = HandleOutOfRangeEnum()
        value.setValue(HandleOutOfRangeEnum.EXTERNAL_REPLACEMENT)
        assert props.setHandleOutOfRange(value) is props
        assert props.getHandleOutOfRange() is value
        assert props.getHandleOutOfRange().getValue() == HandleOutOfRangeEnum.EXTERNAL_REPLACEMENT
        props.setHandleOutOfRange(None)
        assert props.getHandleOutOfRange() is value

    def test_class_docstring_note(self):
        assert inspect.cleandoc(ISignalProps.__doc__) == CLASS_NOTE

    def test_accessor_docstrings_verbatim(self):
        props = ISignalProps()
        assert inspect.cleandoc(props.getHandleOutOfRange.__doc__) == HANDLE_OUT_OF_RANGE_NOTE
        assert inspect.cleandoc(props.setHandleOutOfRange.__doc__).split("\n")[0] == HANDLE_OUT_OF_RANGE_NOTE

    def test_init_has_no_docstring(self):
        assert ISignalProps.__init__.__doc__ is None
