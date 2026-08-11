from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.Communication import HandleOutOfRangeEnum
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore.CoreCommunication import ISignalProps


class Test_ISignalProps:
    """Test cases for ISignalProps class."""

    def test_initialization(self):
        """Test ISignalProps initialization with default values."""
        props = ISignalProps()
        assert props.getHandleOutOfRange() is None

    def test_get_set_handle_out_of_range(self):
        """Test getHandleOutOfRange/setHandleOutOfRange."""
        props = ISignalProps()

        assert props == props.setHandleOutOfRange(None)
        assert props.getHandleOutOfRange() is None

        value = HandleOutOfRangeEnum()
        value.setValue(HandleOutOfRangeEnum.DEFAULT)
        assert props == props.setHandleOutOfRange(value)
        assert props.getHandleOutOfRange() == value
        assert props == props.setHandleOutOfRange(None)
        assert props.getHandleOutOfRange() == value
