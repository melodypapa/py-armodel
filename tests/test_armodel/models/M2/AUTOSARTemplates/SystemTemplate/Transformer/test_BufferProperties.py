from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import Boolean, Integer
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Transformer import BufferProperties


class TestBufferProperties:
    """
    Model tests for BufferProperties (Table 4.88).
    """

    def test_initialization(self):
        props = BufferProperties()

        assert isinstance(props, ARObject)
        assert props.getHeaderLength() is None
        assert props.getInPlace() is None

    def test_get_set_header_length(self):
        props = BufferProperties()
        header_length = Integer().setValue("16")

        assert props == props.setHeaderLength(None)
        assert props.getHeaderLength() is None

        assert props == props.setHeaderLength(header_length)
        assert props.getHeaderLength() == header_length
        assert props.getHeaderLength().getValue() == 16

        assert props == props.setHeaderLength(None)  # None no-op
        assert props.getHeaderLength() == header_length
        assert props.getHeaderLength().getValue() == 16

    def test_get_set_in_place(self):
        props = BufferProperties()
        in_place = Boolean().setValue(True)

        assert props == props.setInPlace(None)
        assert props.getInPlace() is None

        assert props == props.setInPlace(in_place)
        assert props.getInPlace() == in_place
        assert props.getInPlace().getValue() is True

        assert props == props.setInPlace(None)  # None no-op
        assert props.getInPlace() == in_place
        assert props.getInPlace().getValue() is True
