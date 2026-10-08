from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import ByteOrderEnum, PositiveInteger
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Transformer import SOMEIPTransformationDescription, TransformationDescription


class TestSOMEIPTransformationDescription:
    """
    Model tests for SOMEIPTransformationDescription (Table 7.10, p.777).

    Concrete subclass of TransformationDescription (Base = ARObject, Describable,
    TransformationDescription) with three own attributes.
    """

    def test_docstring_is_spec_note_verbatim(self):
        # Table 7.10, p.777 — class Note verbatim from the markdown + existence constraints
        note = "The SOMEIPTransformationDescription is used to specify SOME/IP transformer specific attributes."
        assert SOMEIPTransformationDescription.__doc__.split("\n\n")[0].strip() == note
        assert "[constr_9282] Existence of SOMEIPTransformationDescription . alignment" in SOMEIPTransformationDescription.__doc__
        assert "[constr_9283] Existence of SOMEIPTransformationDescription . byteOrder" in SOMEIPTransformationDescription.__doc__
        assert "[constr_9284] Existence of SOMEIPTransformationDescription . interfaceVersion" in SOMEIPTransformationDescription.__doc__

    def test_init_has_no_docstring(self):
        assert SOMEIPTransformationDescription.__init__.__doc__ is None

    def test_heritage(self):
        assert issubclass(SOMEIPTransformationDescription, TransformationDescription)

        desc = SOMEIPTransformationDescription()
        assert isinstance(desc, TransformationDescription)

    def test_initialization(self):
        desc = SOMEIPTransformationDescription()

        assert desc.getAlignment() is None
        assert desc.getByteOrder() is None
        assert desc.getInterfaceVersion() is None

    def test_get_set_alignment(self):
        desc = SOMEIPTransformationDescription()
        value = PositiveInteger().setValue("8")

        assert desc == desc.setAlignment(None)
        assert desc.getAlignment() is None

        assert desc == desc.setAlignment(value)
        assert desc.getAlignment() == value
        assert desc.getAlignment().getValue() == 8

        assert desc == desc.setAlignment(None)  # None no-op
        assert desc.getAlignment() == value

    def test_get_set_byte_order(self):
        desc = SOMEIPTransformationDescription()
        value = ByteOrderEnum().setValue(ByteOrderEnum.MOST_SIGNIFICANT_BYTE_FIRST)

        assert desc == desc.setByteOrder(None)
        assert desc.getByteOrder() is None

        assert desc == desc.setByteOrder(value)
        assert isinstance(desc.getByteOrder(), ByteOrderEnum)
        assert desc.getByteOrder().getValue() == "MOST-SIGNIFICANT-BYTE-FIRST"

        assert desc == desc.setByteOrder(None)  # None no-op
        assert desc.getByteOrder() == value

    def test_get_set_interface_version(self):
        desc = SOMEIPTransformationDescription()
        value = PositiveInteger().setValue("4")

        assert desc == desc.setInterfaceVersion(None)
        assert desc.getInterfaceVersion() is None

        assert desc == desc.setInterfaceVersion(value)
        assert desc.getInterfaceVersion() == value
        assert desc.getInterfaceVersion().getValue() == 4

        assert desc == desc.setInterfaceVersion(None)  # None no-op
        assert desc.getInterfaceVersion() == value
