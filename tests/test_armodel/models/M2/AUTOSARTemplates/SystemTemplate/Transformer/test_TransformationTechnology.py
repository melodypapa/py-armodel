import typing

from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable import Identifiable
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import Boolean, String
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Transformer import (
    BufferProperties,
    EndToEndTransformationDescription,
    TransformationTechnology,
    TransformerClassEnum,
)

SPEC_NOTE = "A TransformationTechnology is a transformer inside a transformer chain."
BUFFER_NOTE = "Aggregation of the mandatory BufferProperties."
INTERNAL_STATE_NOTE = "This attribute defines whether the Transformer has an internal state or not."
ORIGINAL_DATA_NOTE = "Specifies whether this transformer gets access to the SWC's original data."
PROTOCOL_NOTE = "Specifies the protocol that is implemented by this transformer."
DESCRIPTION_NOTE = "A transformer can be configured with transformer specific parameters which are represented by the Transformer Description."
CLASS_NOTE = "Specifies to which transformer class this transformer belongs."
VERSION_NOTE = "Version of the implemented protocol."


class TestTransformationTechnology:
    def test_initialization(self):
        document = AUTOSAR.getInstance()
        ar_root = document.createARPackage("Pkg")
        tech = TransformationTechnology(ar_root, "Tech")

        assert tech.getShortName() == "Tech"
        assert tech.getBufferProperties() is None
        assert tech.getHasInternalState() is None
        assert tech.getNeedsOriginalData() is None
        assert tech.getProtocol() is None
        assert tech.getTransformationDescription() is None
        assert tech.getTransformerClass() is None
        assert tech.getVersion() is None

    def test_heritage(self):
        document = AUTOSAR.getInstance()
        ar_root = document.createARPackage("Pkg")
        tech = TransformationTechnology(ar_root, "Tech")

        assert type(tech).__bases__ == (Identifiable,)
        assert isinstance(tech, Identifiable)
        assert not hasattr(tech, "getVariationPoint")

    def test_class_docstring_verbatim(self):
        assert TransformationTechnology.__doc__.strip() == SPEC_NOTE

    def test_set_get_buffer_properties(self):
        document = AUTOSAR.getInstance()
        ar_root = document.createARPackage("Pkg")
        tech = TransformationTechnology(ar_root, "Tech")

        props = BufferProperties()
        assert tech == tech.setBufferProperties(None)
        assert tech.getBufferProperties() is None

        assert tech == tech.setBufferProperties(props)
        assert tech.getBufferProperties() is props

        assert tech == tech.setBufferProperties(None)
        assert tech.getBufferProperties() is props

    def test_get_set_scalars(self):
        document = AUTOSAR.getInstance()
        ar_root = document.createARPackage("Pkg")
        tech = TransformationTechnology(ar_root, "Tech")

        has_internal_state = Boolean().setValue(True)
        assert tech == tech.setHasInternalState(has_internal_state)
        assert tech.getHasInternalState() is has_internal_state
        assert tech == tech.setHasInternalState(None)
        assert tech.getHasInternalState() is has_internal_state

        needs_original_data = Boolean().setValue(False)
        assert tech == tech.setNeedsOriginalData(needs_original_data)
        assert tech.getNeedsOriginalData() is needs_original_data

        protocol = String().setValue("EndToEnd")
        assert tech == tech.setProtocol(protocol)
        assert tech.getProtocol() is protocol

        transformer_class = TransformerClassEnum().setValue(TransformerClassEnum.SERIALIZER)
        assert tech == tech.setTransformerClass(transformer_class)
        assert tech.getTransformerClass().getValue() == "serializer"

        version = String().setValue("1.0")
        assert tech == tech.setVersion(version)
        assert tech.getVersion() is version

    def test_set_transformation_description(self):
        document = AUTOSAR.getInstance()
        ar_root = document.createARPackage("Pkg")
        tech = TransformationTechnology(ar_root, "Tech")

        desc = EndToEndTransformationDescription()
        assert tech == tech.setTransformationDescription(None)
        assert tech.getTransformationDescription() is None

        assert tech == tech.setTransformationDescription(desc)
        assert tech.getTransformationDescription() is desc

    def test_docstrings_verbatim(self):
        document = AUTOSAR.getInstance()
        ar_root = document.createARPackage("Pkg")
        tech = TransformationTechnology(ar_root, "Tech")

        assert BUFFER_NOTE in tech.setBufferProperties.__doc__
        assert tech.getBufferProperties.__doc__.strip() == BUFFER_NOTE
        assert tech.getHasInternalState.__doc__.strip() == INTERNAL_STATE_NOTE
        assert INTERNAL_STATE_NOTE in tech.setHasInternalState.__doc__
        assert tech.getNeedsOriginalData.__doc__.strip() == ORIGINAL_DATA_NOTE
        assert tech.getProtocol.__doc__.strip() == PROTOCOL_NOTE
        assert tech.getTransformationDescription.__doc__.strip() == DESCRIPTION_NOTE
        assert tech.getTransformerClass.__doc__.strip() == CLASS_NOTE
        assert tech.getVersion.__doc__.strip() == VERSION_NOTE

    def test_get_type_hints_pins(self):
        hints = typing.get_type_hints(TransformationTechnology.getBufferProperties)
        assert hints.get("return") == typing.Optional[BufferProperties]

        hints = typing.get_type_hints(TransformationTechnology.setBufferProperties)
        assert hints.get("value") == typing.Optional[BufferProperties]
        assert hints.get("return") is TransformationTechnology

        hints = typing.get_type_hints(TransformationTechnology.getTransformationDescription)
        hints_return = hints.get("return")
        assert hints_return is not None and "TransformationDescription" in str(hints_return)

        hints = typing.get_type_hints(TransformationTechnology.getTransformerClass)
        assert hints.get("return") == typing.Optional[TransformerClassEnum]

        hints = typing.get_type_hints(TransformationTechnology.getVersion)
        assert hints.get("return") == typing.Optional[String]
