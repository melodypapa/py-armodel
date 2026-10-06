import typing

from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable import Identifiable
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import Boolean, RefType
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Transformer import DataTransformation, DataTransformationKindEnum

SPEC_NOTE = "A DataTransformation represents a transformer chain. It is an ordered list of transformers."
KIND_NOTE = "This attribute controls the kind of DataTransformation to be applied."
EXECUTE_NOTE = "Specifies whether the transformer chain is executed even if no input data are available."
CHAIN_NOTE = "This attribute represents the definition of a chain of transformers that are supposed to be executed according to the order of being referenced from DataTransformation."


class TestDataTransformation:
    def test_initialization(self):
        document = AUTOSAR.getInstance()
        ar_root = document.createARPackage("Pkg")
        transformation = DataTransformation(ar_root, "Chain")

        assert transformation.getShortName() == "Chain"
        assert transformation.getDataTransformationKind() is None
        assert transformation.getExecuteDespiteDataUnavailability() is None
        assert transformation.getTransformerChainRefs() == []

    def test_heritage(self):
        document = AUTOSAR.getInstance()
        ar_root = document.createARPackage("Pkg")
        transformation = DataTransformation(ar_root, "Chain")

        assert type(transformation).__bases__ == (Identifiable,)
        assert isinstance(transformation, Identifiable)
        assert not hasattr(transformation, "getVariationPoint")

    def test_class_docstring_verbatim(self):
        assert SPEC_NOTE in DataTransformation.__doc__
        assert "[constr_1888]" in DataTransformation.__doc__

    def test_get_set_data_transformation_kind(self):
        document = AUTOSAR.getInstance()
        ar_root = document.createARPackage("Pkg")
        transformation = DataTransformation(ar_root, "Chain")

        value = DataTransformationKindEnum().setValue(DataTransformationKindEnum.SYMMETRIC)
        assert transformation == transformation.setDataTransformationKind(None)
        assert transformation.getDataTransformationKind() is None

        assert transformation == transformation.setDataTransformationKind(value)
        assert transformation.getDataTransformationKind() is value
        assert transformation.getDataTransformationKind().getValue() == DataTransformationKindEnum.SYMMETRIC

        assert transformation == transformation.setDataTransformationKind(None)
        assert transformation.getDataTransformationKind() is value

    def test_get_set_execute_despite_data_unavailability(self):
        document = AUTOSAR.getInstance()
        ar_root = document.createARPackage("Pkg")
        transformation = DataTransformation(ar_root, "Chain")

        value = Boolean().setValue(True)
        assert transformation == transformation.setExecuteDespiteDataUnavailability(None)
        assert transformation.getExecuteDespiteDataUnavailability() is None

        assert transformation == transformation.setExecuteDespiteDataUnavailability(value)
        assert transformation.getExecuteDespiteDataUnavailability() is value
        assert transformation.getExecuteDespiteDataUnavailability().getValue() is True

        assert transformation == transformation.setExecuteDespiteDataUnavailability(None)
        assert transformation.getExecuteDespiteDataUnavailability() is value

    def test_add_transformer_chain_ref(self):
        document = AUTOSAR.getInstance()
        ar_root = document.createARPackage("Pkg")
        transformation = DataTransformation(ar_root, "Chain")

        ref = RefType().setValue("/Pkg/Serializer")
        assert transformation == transformation.addTransformerChainRef(None)
        assert transformation.getTransformerChainRefs() == []

        assert transformation == transformation.addTransformerChainRef(ref)
        assert transformation.getTransformerChainRefs() == [ref]
        assert transformation.getTransformerChainRefs()[0].getValue() == "/Pkg/Serializer"

    def test_docstrings_verbatim(self):
        document = AUTOSAR.getInstance()
        ar_root = document.createARPackage("Pkg")
        transformation = DataTransformation(ar_root, "Chain")

        assert transformation.getDataTransformationKind.__doc__.strip() == KIND_NOTE
        assert KIND_NOTE in transformation.setDataTransformationKind.__doc__
        assert transformation.getExecuteDespiteDataUnavailability.__doc__.strip() == EXECUTE_NOTE
        assert EXECUTE_NOTE in transformation.setExecuteDespiteDataUnavailability.__doc__
        assert transformation.getTransformerChainRefs.__doc__.strip() == CHAIN_NOTE
        assert CHAIN_NOTE in transformation.addTransformerChainRef.__doc__

    def test_get_type_hints_pins(self):
        hints = typing.get_type_hints(DataTransformation.getDataTransformationKind)
        assert hints.get("return") == typing.Optional[DataTransformationKindEnum]

        hints = typing.get_type_hints(DataTransformation.setDataTransformationKind)
        assert hints.get("value") == typing.Optional[DataTransformationKindEnum]
        assert hints.get("return") is DataTransformation

        hints = typing.get_type_hints(DataTransformation.getExecuteDespiteDataUnavailability)
        assert hints.get("return") == typing.Optional[Boolean]

        hints = typing.get_type_hints(DataTransformation.getTransformerChainRefs)
        assert hints.get("return") == typing.List[RefType]

        hints = typing.get_type_hints(DataTransformation.addTransformerChainRef)
        assert hints.get("value") == typing.Optional[RefType]
        assert hints.get("return") is DataTransformation
