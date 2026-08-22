import pytest

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable import ARElement, Describable, Identifiable
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import Boolean
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Transformer import (
    BufferProperties,
    CSTransformerErrorReactionEnum,
    DataIdModeEnum,
    DataTransformation,
    DataTransformationKindEnum,
    DataTransformationSet,
    E2EProfileCompatibilityProps,
    EndToEndProfileBehaviorEnum,
    EndToEndTransformationComSpecProps,
    EndToEndTransformationDescription,
    EndToEndTransformationISignalProps,
    TransformationDescription,
    TransformationISignalProps,
    TransformationTechnology,
    TransformerClassEnum,
)


class MockParent(ARObject):
    def __init__(self):
        super().__init__()


class TestTransformer:
    """
    Test class for Transformer module functionality.
    This class contains test methods for validating the behavior of
    data transformation classes, including their initialization,
    inheritance relationships, and property accessors.
    """

    def test_buffer_properties_initialization(self):
        props = BufferProperties()

        assert isinstance(props, ARObject)
        assert props.getHeaderLength() is None
        assert props.getInPlace() is None

    def test_get_set_buffer_properties_header_length(self):
        from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import Integer

        props = BufferProperties()
        value = Integer().setValue(8)

        assert props == props.setHeaderLength(None)
        assert props.getHeaderLength() is None

        assert props == props.setHeaderLength(value)
        assert props.getHeaderLength() == value
        assert props.getHeaderLength().getValue() == 8

    def test_get_set_buffer_properties_in_place(self):
        from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import Boolean

        props = BufferProperties()
        value = Boolean().setValue(True)

        assert props == props.setInPlace(None)
        assert props.getInPlace() is None

        assert props == props.setInPlace(value)
        assert props.getInPlace() == value
        assert value.getValue() is True

    def test_no_fabricated_buffer_computation(self):
        props = BufferProperties()

        assert not hasattr(props, "bufferComputation")

    def test_data_transformation(self):
        """
        Test DataTransformation class functionality with method chaining and None handling.
        """
        from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import RefType

        parent = MockParent()
        transformation = DataTransformation(parent, "test_transformation")

        assert isinstance(transformation, Identifiable)

        # Test default values
        assert transformation.getDataTransformationKind() is None
        assert transformation.getExecuteDespiteDataUnavailability() is None
        assert transformation.getTransformerChainRefs() == []

        # Test setter/getter methods with method chaining - with None values
        assert transformation == transformation.setDataTransformationKind(None)
        assert transformation.getDataTransformationKind() is None

        assert transformation == transformation.setExecuteDespiteDataUnavailability(None)
        assert transformation.getExecuteDespiteDataUnavailability() is None

        # Test setter/getter methods with method chaining - with actual values
        mock_kind = DataTransformationKindEnum.ASYMMETRIC_FROM_BYTE_ARRAY
        transformation.setDataTransformationKind(mock_kind)
        assert transformation.getDataTransformationKind() == mock_kind
        assert transformation == transformation.setDataTransformationKind(mock_kind)
        assert transformation == transformation.setDataTransformationKind(None)  # None is a no-op
        assert transformation.getDataTransformationKind() == mock_kind

        transformation.setExecuteDespiteDataUnavailability(True)
        assert transformation.getExecuteDespiteDataUnavailability() is True
        assert transformation == transformation.setExecuteDespiteDataUnavailability(True)
        assert transformation == transformation.setExecuteDespiteDataUnavailability(None)  # None is a no-op
        assert transformation.getExecuteDespiteDataUnavailability() is True

        # Test addTransformerChainRef with method chaining and None no-op
        ref1 = RefType()
        ref1.setValue("/chain1")
        transformation.addTransformerChainRef(ref1)
        assert ref1 in transformation.getTransformerChainRefs()
        assert len(transformation.getTransformerChainRefs()) == 1

        assert transformation == transformation.addTransformerChainRef(None)  # None is a no-op
        assert len(transformation.getTransformerChainRefs()) == 1

        ref2 = RefType()
        ref2.setValue("/chain2")
        assert transformation == transformation.addTransformerChainRef(ref2)  # Test method chaining
        assert len(transformation.getTransformerChainRefs()) == 2

    def test_data_transformation_kind_enum(self):
        """
        Test DataTransformationKindEnum enum functionality.
        """
        enum = DataTransformationKindEnum()

        # Test that it's properly initialized
        assert enum is not None
        assert DataTransformationKindEnum.ASYMMETRIC_FROM_BYTE_ARRAY in enum.getEnumValues()
        assert DataTransformationKindEnum.ASYMMETRIC_TO_BYTE_ARRAY in enum.getEnumValues()
        assert DataTransformationKindEnum.SYMMETRIC in enum.getEnumValues()

        # Test instantiation with a value
        enum.setValue(DataTransformationKindEnum.SYMMETRIC)
        assert enum.getValue() == "symmetric"

    def test_data_transformation_set(self):
        """
        Test DataTransformationSet class functionality.
        """
        parent = MockParent()
        data_set = DataTransformationSet(parent, "test_data_set")

        assert isinstance(data_set, ARElement)

        # Test default values
        assert data_set.getDataTransformations() == []
        assert data_set.getTransformationTechnologies() == []

        # Test create methods
        trans = data_set.createDataTransformation("test_transformation")
        assert isinstance(trans, DataTransformation)
        assert len(data_set.getDataTransformations()) == 1

        tech = data_set.createTransformationTechnology("test_technology")
        assert isinstance(tech, TransformationTechnology)
        assert len(data_set.getTransformationTechnologies()) == 1

    def test_end_to_end_profile_behavior_enum(self):
        """
        Test EndToEndProfileBehaviorEnum class functionality.
        """
        enum = EndToEndProfileBehaviorEnum()

        # Test that it's properly initialized and instantiable
        assert isinstance(enum, EndToEndProfileBehaviorEnum)

        # Member names and values match the spec Enumeration literals (Table 7.26)
        assert EndToEndProfileBehaviorEnum.PRE_R4_2 == "PRE_R4_2"
        assert EndToEndProfileBehaviorEnum.R4_2 == "R4_2"

        # Validated set of allowed values
        assert list(enum.getEnumValues()) == ["PRE_R4_2", "R4_2"]

        # setValue / getValue round-trip
        assert enum.setValue(EndToEndProfileBehaviorEnum.R4_2).getValue() == "R4_2"
        assert enum.setValue(EndToEndProfileBehaviorEnum.PRE_R4_2).getValue() == "PRE_R4_2"

    def test_e2e_profile_compatibility_props(self):
        """
        Test E2EProfileCompatibilityProps class functionality with method chaining and None handling.
        """
        parent = MockParent()
        props = E2EProfileCompatibilityProps(parent, "test_e2e_profile_compatibility_props")

        assert isinstance(props, ARElement)

        # Test default values
        assert props.getTransitToInvalidExtended() is None

        # Test set/get round-trip and method chaining
        flag = Boolean()
        flag.setValue("true")
        assert props.setTransitToInvalidExtended(flag) is props
        assert props.getTransitToInvalidExtended() is flag

        # Test None no-op
        assert props.setTransitToInvalidExtended(None) is props
        assert props.getTransitToInvalidExtended() is flag

    def test_end_to_end_transformation_description(self):
        """
        Test EndToEndTransformationDescription class functionality with method chaining and None handling.
        """
        description = EndToEndTransformationDescription()

        assert isinstance(description, Describable)

        # Test default values
        assert description.getClearFromValidToInvalid() is None
        assert description.getCounterOffset() is None
        assert description.getCrcOffset() is None
        assert description.getDataIdMode() is None
        assert description.getDataIdNibbleOffset() is None
        assert description.getE2eProfileCompatibilityPropsRef() is None
        assert description.getMaxDeltaCounter() is None
        assert description.getMaxErrorStateInit() is None
        assert description.getMaxErrorStateInvalid() is None
        assert description.getMaxErrorStateValid() is None
        assert description.getMaxNoNewOrRepeatedData() is None
        assert description.getMinOkStateInit() is None
        assert description.getMinOkStateInvalid() is None
        assert description.getMinOkStateValid() is None
        assert description.getOffset() is None
        assert description.getProfileBehavior() is None
        assert description.getProfileName() is None
        assert description.getSyncCounterInit() is None
        assert description.getUpperHeaderBitsToShift() is None
        assert description.getWindowSizeInit() is None
        assert description.getWindowSizeInvalid() is None
        assert description.getWindowSizeValid() is None

        # Test setter/getter methods with method chaining - with None values
        assert description == description.setClearFromValidToInvalid(None)
        assert description.getClearFromValidToInvalid() is None

        assert description == description.setCounterOffset(None)
        assert description.getCounterOffset() is None

        assert description == description.setCrcOffset(None)
        assert description.getCrcOffset() is None

        assert description == description.setDataIdMode(None)
        assert description.getDataIdMode() is None

        assert description == description.setDataIdNibbleOffset(None)
        assert description.getDataIdNibbleOffset() is None

        assert description == description.setE2eProfileCompatibilityPropsRef(None)
        assert description.getE2eProfileCompatibilityPropsRef() is None

        assert description == description.setMaxDeltaCounter(None)
        assert description.getMaxDeltaCounter() is None

        assert description == description.setMaxErrorStateInit(None)
        assert description.getMaxErrorStateInit() is None

        assert description == description.setMaxErrorStateInvalid(None)
        assert description.getMaxErrorStateInvalid() is None

        assert description == description.setMaxErrorStateValid(None)
        assert description.getMaxErrorStateValid() is None

        assert description == description.setMaxNoNewOrRepeatedData(None)
        assert description.getMaxNoNewOrRepeatedData() is None

        assert description == description.setMinOkStateInit(None)
        assert description.getMinOkStateInit() is None

        assert description == description.setMinOkStateInvalid(None)
        assert description.getMinOkStateInvalid() is None

        assert description == description.setMinOkStateValid(None)
        assert description.getMinOkStateValid() is None

        assert description == description.setOffset(None)
        assert description.getOffset() is None

        assert description == description.setProfileBehavior(None)
        assert description.getProfileBehavior() is None

        assert description == description.setProfileName(None)
        assert description.getProfileName() is None

        assert description == description.setSyncCounterInit(None)
        assert description.getSyncCounterInit() is None

        assert description == description.setUpperHeaderBitsToShift(None)
        assert description.getUpperHeaderBitsToShift() is None

        assert description == description.setWindowSizeInit(None)
        assert description.getWindowSizeInit() is None

        assert description == description.setWindowSizeInvalid(None)
        assert description.getWindowSizeInvalid() is None

        assert description == description.setWindowSizeValid(None)
        assert description.getWindowSizeValid() is None

        # Test setter/getter methods with method chaining - with actual values
        description.setCounterOffset(5)
        assert description.getCounterOffset() == 5
        assert description == description.setCounterOffset(5)

        description.setClearFromValidToInvalid(True)
        assert description.getClearFromValidToInvalid() is True
        assert description == description.setClearFromValidToInvalid(True)

        description.setCrcOffset(10)
        assert description.getCrcOffset() == 10
        assert description == description.setCrcOffset(10)

        description.setDataIdMode(DataIdModeEnum.ALL_16_BIT)
        assert description.getDataIdMode() == DataIdModeEnum.ALL_16_BIT
        assert description == description.setDataIdMode(DataIdModeEnum.ALL_16_BIT)

        description.setDataIdNibbleOffset(2)
        assert description.getDataIdNibbleOffset() == 2
        assert description == description.setDataIdNibbleOffset(2)

        description.setE2eProfileCompatibilityPropsRef("ref")
        assert description.getE2eProfileCompatibilityPropsRef() == "ref"
        assert description == description.setE2eProfileCompatibilityPropsRef("ref")

        description.setMaxDeltaCounter(100)
        assert description.getMaxDeltaCounter() == 100
        assert description == description.setMaxDeltaCounter(100)

        description.setMaxErrorStateInit(50)
        assert description.getMaxErrorStateInit() == 50
        assert description == description.setMaxErrorStateInit(50)

        description.setMaxErrorStateInvalid(40)
        assert description.getMaxErrorStateInvalid() == 40
        assert description == description.setMaxErrorStateInvalid(40)

        description.setMaxErrorStateValid(60)
        assert description.getMaxErrorStateValid() == 60
        assert description == description.setMaxErrorStateValid(60)

        description.setMaxNoNewOrRepeatedData(30)
        assert description.getMaxNoNewOrRepeatedData() == 30
        assert description == description.setMaxNoNewOrRepeatedData(30)

        description.setMinOkStateInit(5)
        assert description.getMinOkStateInit() == 5
        assert description == description.setMinOkStateInit(5)

        description.setMinOkStateInvalid(4)
        assert description.getMinOkStateInvalid() == 4
        assert description == description.setMinOkStateInvalid(4)

        description.setMinOkStateValid(6)
        assert description.getMinOkStateValid() == 6
        assert description == description.setMinOkStateValid(6)

        description.setOffset(20)
        assert description.getOffset() == 20
        assert description == description.setOffset(20)

        description.setProfileBehavior(EndToEndProfileBehaviorEnum.R4_2)
        assert description.getProfileBehavior() == EndToEndProfileBehaviorEnum.R4_2
        assert description == description.setProfileBehavior(EndToEndProfileBehaviorEnum.R4_2)

        description.setProfileName("profile")
        assert description.getProfileName() == "profile"
        assert description == description.setProfileName("profile")

        description.setSyncCounterInit(1)
        assert description.getSyncCounterInit() == 1
        assert description == description.setSyncCounterInit(1)

        description.setUpperHeaderBitsToShift(3)
        assert description.getUpperHeaderBitsToShift() == 3
        assert description == description.setUpperHeaderBitsToShift(3)

        description.setWindowSizeInit(10)
        assert description.getWindowSizeInit() == 10
        assert description == description.setWindowSizeInit(10)

        description.setWindowSizeInvalid(8)
        assert description.getWindowSizeInvalid() == 8
        assert description == description.setWindowSizeInvalid(8)

        description.setWindowSizeValid(12)
        assert description.getWindowSizeValid() == 12
        assert description == description.setWindowSizeValid(12)

    def test_transformation_description_abstract(self):
        """
        Test TransformationDescription abstract class functionality.
        """
        with pytest.raises(TypeError):
            TransformationDescription()

    def test_transformation_description_base_properties(self):
        from armodel.models.M2.MSR.Documentation.TextModel.MultilanguageData import MultiLanguageOverviewParagraph

        class ConcreteTransformationDescription(TransformationDescription):
            def __init__(self):
                super().__init__()

        desc = ConcreteTransformationDescription()

        assert desc.getCategory() is None
        assert desc.getDesc() is None
        assert desc.getIntroduction() is None

        assert desc == desc.setCategory(None)
        assert desc.getCategory() is None

        assert desc == desc.setDesc(None)
        assert desc.getDesc() is None

        assert desc == desc.setIntroduction(None)
        assert desc.getIntroduction() is None

        desc.setCategory("category")
        assert desc.getCategory() == "category"
        assert desc == desc.setCategory("category")

        value = MultiLanguageOverviewParagraph()
        desc.setDesc(value)
        assert desc.getDesc() == value
        assert desc == desc.setDesc(value)

    def test_transformation_technology(self):
        """
        Test TransformationTechnology class functionality with method chaining and None handling.
        """
        parent = MockParent()
        technology = TransformationTechnology(parent, "test_technology")

        assert isinstance(technology, Identifiable)

        # Test default values
        assert technology.getBufferProperties() is None
        assert technology.getHasInternalState() is None
        assert technology.getNeedsOriginalData() is None
        assert technology.getProtocol() is None
        assert technology.getTransformationDescription() is None
        assert technology.getTransformerClass() is None
        assert technology.getVersion() is None

        # Test setter/getter methods with method chaining - with None values
        assert technology == technology.setBufferProperties(None)
        assert technology.getBufferProperties() is None

        assert technology == technology.setHasInternalState(None)
        assert technology.getHasInternalState() is None

        assert technology == technology.setNeedsOriginalData(None)
        assert technology.getNeedsOriginalData() is None

        assert technology == technology.setProtocol(None)
        assert technology.getProtocol() is None

        assert technology == technology.setTransformationDescription(None)
        assert technology.getTransformationDescription() is None

        assert technology == technology.setTransformerClass(None)
        assert technology.getTransformerClass() is None

        assert technology == technology.setVersion(None)
        assert technology.getVersion() is None

        # Test setter/getter methods with method chaining - with actual values
        mock_buffer = BufferProperties()
        technology.setBufferProperties(mock_buffer)
        assert technology.getBufferProperties() == mock_buffer
        assert technology == technology.setBufferProperties(mock_buffer)

        technology.setHasInternalState(True)
        assert technology.getHasInternalState() is True
        assert technology == technology.setHasInternalState(True)

        technology.setProtocol("e2e")
        assert technology.getProtocol() == "e2e"
        assert technology == technology.setProtocol("e2e")

        technology.setNeedsOriginalData(False)
        assert technology.getNeedsOriginalData() is False
        assert technology == technology.setNeedsOriginalData(False)

        mock_desc = EndToEndTransformationDescription()
        technology.setTransformationDescription(mock_desc)
        assert technology.getTransformationDescription() == mock_desc
        assert technology == technology.setTransformationDescription(mock_desc)

        transformer_class = TransformerClassEnum().setValue(TransformerClassEnum.SECURITY)
        technology.setTransformerClass(transformer_class)
        assert technology.getTransformerClass() == transformer_class
        assert technology.getTransformerClass().getValue() == "security"
        assert technology == technology.setTransformerClass(transformer_class)

        technology.setVersion("1.0")
        assert technology.getVersion() == "1.0"
        assert technology == technology.setVersion("1.0")

    def test_transformer_class_enum(self):
        """
        Test TransformerClassEnum class functionality.
        """
        enum = TransformerClassEnum()

        assert enum is not None
        assert TransformerClassEnum.CUSTOM == "custom"
        assert TransformerClassEnum.SAFETY == "safety"
        assert TransformerClassEnum.SECURITY == "security"
        assert TransformerClassEnum.SERIALIZER == "serializer"

        assert enum == enum.setValue(TransformerClassEnum.CUSTOM)
        assert enum.getValue() == "custom"
        assert enum == enum.setValue(TransformerClassEnum.SAFETY)
        assert enum.getValue() == "safety"
        assert enum == enum.setValue(TransformerClassEnum.SECURITY)
        assert enum.getValue() == "security"
        assert enum == enum.setValue(TransformerClassEnum.SERIALIZER)
        assert enum.getValue() == "serializer"

    def test_cs_transformer_error_reaction_enum(self):
        """
        Test CSTransformerErrorReactionEnum enum functionality.
        """
        enum = CSTransformerErrorReactionEnum()

        # Test that it's properly initialized
        assert enum is not None
        assert CSTransformerErrorReactionEnum.APPLICATION_ONLY in enum.getEnumValues()
        assert CSTransformerErrorReactionEnum.AUTONOMOUS in enum.getEnumValues()

        # Test instantiation with a value
        enum.setValue(CSTransformerErrorReactionEnum.AUTONOMOUS)
        assert enum.getValue() == "autonomous"

    def test_transformation_isignal_props_abstract(self):
        """
        Test TransformationISignalProps abstract class functionality.
        """
        from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import RefType

        class ConcreteTransformationISignalProps(TransformationISignalProps):
            def __init__(self):
                super().__init__()

        props = ConcreteTransformationISignalProps()

        # Test default values
        assert props.getCsErrorReaction() is None
        assert props.getDataPrototypeTransformationProps() == []
        assert props.getTransformerRef() is None

        # No fabricated ident field
        assert not hasattr(props, "ident")

        # Test setter/getter methods with method chaining - with None values
        assert props == props.setCsErrorReaction(None)
        assert props.getCsErrorReaction() is None

        assert props == props.setDataPrototypeTransformationProps(None)
        assert props.getDataPrototypeTransformationProps() == []  # Should remain empty list

        assert props == props.setTransformerRef(None)
        assert props.getTransformerRef() is None

        # Test setter/getter methods with method chaining - with actual values
        props.setCsErrorReaction(CSTransformerErrorReactionEnum.APPLICATION_ONLY)
        assert props.getCsErrorReaction() == CSTransformerErrorReactionEnum.APPLICATION_ONLY
        assert props == props.setCsErrorReaction(CSTransformerErrorReactionEnum.APPLICATION_ONLY)

        props.setDataPrototypeTransformationProps(["prop1", "prop2"])
        assert "prop1" in props.getDataPrototypeTransformationProps()
        assert props == props.setDataPrototypeTransformationProps(["prop1", "prop2"])

        transformer_ref = RefType()
        transformer_ref.setValue("/Pkg/Transformer")
        props.setTransformerRef(transformer_ref)
        assert props.getTransformerRef() == transformer_ref
        assert props == props.setTransformerRef(transformer_ref)

    def test_end_to_end_transformation_isignal_props(self):
        """
        Test EndToEndTransformationISignalProps class functionality with method chaining and None handling.
        """
        props = EndToEndTransformationISignalProps()

        # Test default values
        assert props.getDataIds() == []
        assert props.getDataLength() is None
        assert props.getMaxDataLength() is None
        assert props.getMinDataLength() is None
        assert props.getSourceId() is None

        # Test addDataId with method chaining
        props.addDataId(1)
        assert 1 in props.getDataIds()
        assert props == props.addDataId(2)
        assert len(props.getDataIds()) == 2

        # Test setter/getter methods with method chaining - with None values
        assert props == props.setDataLength(None)
        assert props.getDataLength() is None

        assert props == props.setMaxDataLength(None)
        assert props.getMaxDataLength() is None

        assert props == props.setMinDataLength(None)
        assert props.getMinDataLength() is None

        assert props == props.setSourceId(None)
        assert props.getSourceId() is None

        # Test setter/getter methods with method chaining - with actual values
        props.setDataLength(8)
        assert props.getDataLength() == 8
        assert props == props.setDataLength(8)

        props.setMaxDataLength(16)
        assert props.getMaxDataLength() == 16
        assert props == props.setMaxDataLength(16)

        props.setMinDataLength(4)
        assert props.getMinDataLength() == 4
        assert props == props.setMinDataLength(4)

        props.setSourceId(100)
        assert props.getSourceId() == 100
        assert props == props.setSourceId(100)


class TestEndToEndTransformationComSpecProps:
    """
    Test EndToEndTransformationComSpecProps against SWCT Table 4.92 (p.201).
    """

    def _make_positive(self, value):
        from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import PositiveInteger

        return PositiveInteger().setValue(value)

    def test_initialization(self):
        props = EndToEndTransformationComSpecProps()
        assert props.getClearFromValidToInvalid() is None
        assert props.getDisableEndToEndCheck() is None
        assert props.getDisableEndToEndStateMachine() is None
        assert props.getE2eProfileCompatibilityPropsRef() is None
        assert props.getMaxDeltaCounter() is None
        assert props.getMaxErrorStateInit() is None
        assert props.getMaxErrorStateInvalid() is None
        assert props.getMaxErrorStateValid() is None
        assert props.getMaxNoNewOrRepeatedData() is None
        assert props.getMinOkStateInit() is None
        assert props.getMinOkStateInvalid() is None
        assert props.getMinOkStateValid() is None
        assert props.getSyncCounterInit() is None
        assert props.getWindowSizeInit() is None
        assert props.getWindowSizeInvalid() is None
        assert props.getWindowSizeValid() is None

    def test_get_set_clear_from_valid_to_invalid(self):
        props = EndToEndTransformationComSpecProps()
        assert props.setClearFromValidToInvalid(None) is props
        assert props.getClearFromValidToInvalid() is None
        props.setClearFromValidToInvalid(True)
        assert props.getClearFromValidToInvalid() is True

    def test_get_set_disable_end_to_end_check(self):
        props = EndToEndTransformationComSpecProps()
        assert props.setDisableEndToEndCheck(None) is props
        assert props.getDisableEndToEndCheck() is None
        props.setDisableEndToEndCheck(True)
        assert props.getDisableEndToEndCheck() is True

    def test_get_set_disable_end_to_end_state_machine(self):
        props = EndToEndTransformationComSpecProps()
        assert props.setDisableEndToEndStateMachine(None) is props
        assert props.getDisableEndToEndStateMachine() is None
        props.setDisableEndToEndStateMachine(True)
        assert props.getDisableEndToEndStateMachine() is True

    def test_get_set_e2e_profile_compatibility_props_ref(self):
        from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import RefType

        props = EndToEndTransformationComSpecProps()
        assert props.setE2eProfileCompatibilityPropsRef(None) is props
        assert props.getE2eProfileCompatibilityPropsRef() is None
        ref = RefType()
        ref.setDest("E2EProfileCompatibilityProps")
        ref.setValue("/Pkg/Props")
        props.setE2eProfileCompatibilityPropsRef(ref)
        assert props.getE2eProfileCompatibilityPropsRef() == ref

    def test_get_set_max_delta_counter(self):
        props = EndToEndTransformationComSpecProps()
        assert props.setMaxDeltaCounter(None) is props
        assert props.getMaxDeltaCounter() is None
        value = self._make_positive(3)
        props.setMaxDeltaCounter(value)
        assert props.getMaxDeltaCounter() == value

    def test_get_set_max_error_state_init(self):
        props = EndToEndTransformationComSpecProps()
        assert props.setMaxErrorStateInit(None) is props
        assert props.getMaxErrorStateInit() is None
        value = self._make_positive(2)
        props.setMaxErrorStateInit(value)
        assert props.getMaxErrorStateInit() == value

    def test_get_set_max_error_state_invalid(self):
        props = EndToEndTransformationComSpecProps()
        assert props.setMaxErrorStateInvalid(None) is props
        assert props.getMaxErrorStateInvalid() is None
        value = self._make_positive(2)
        props.setMaxErrorStateInvalid(value)
        assert props.getMaxErrorStateInvalid() == value

    def test_get_set_max_error_state_valid(self):
        props = EndToEndTransformationComSpecProps()
        assert props.setMaxErrorStateValid(None) is props
        assert props.getMaxErrorStateValid() is None
        value = self._make_positive(2)
        props.setMaxErrorStateValid(value)
        assert props.getMaxErrorStateValid() == value

    def test_get_set_max_no_new_or_repeated_data(self):
        props = EndToEndTransformationComSpecProps()
        assert props.setMaxNoNewOrRepeatedData(None) is props
        assert props.getMaxNoNewOrRepeatedData() is None
        value = self._make_positive(2)
        props.setMaxNoNewOrRepeatedData(value)
        assert props.getMaxNoNewOrRepeatedData() == value

    def test_get_set_min_ok_state_init(self):
        props = EndToEndTransformationComSpecProps()
        assert props.setMinOkStateInit(None) is props
        assert props.getMinOkStateInit() is None
        value = self._make_positive(1)
        props.setMinOkStateInit(value)
        assert props.getMinOkStateInit() == value

    def test_get_set_min_ok_state_invalid(self):
        props = EndToEndTransformationComSpecProps()
        assert props.setMinOkStateInvalid(None) is props
        assert props.getMinOkStateInvalid() is None
        value = self._make_positive(1)
        props.setMinOkStateInvalid(value)
        assert props.getMinOkStateInvalid() == value

    def test_get_set_min_ok_state_valid(self):
        props = EndToEndTransformationComSpecProps()
        assert props.setMinOkStateValid(None) is props
        assert props.getMinOkStateValid() is None
        value = self._make_positive(1)
        props.setMinOkStateValid(value)
        assert props.getMinOkStateValid() == value

    def test_get_set_sync_counter_init(self):
        props = EndToEndTransformationComSpecProps()
        assert props.setSyncCounterInit(None) is props
        assert props.getSyncCounterInit() is None
        value = self._make_positive(0)
        props.setSyncCounterInit(value)
        assert props.getSyncCounterInit() == value

    def test_get_set_window_size_init(self):
        props = EndToEndTransformationComSpecProps()
        assert props.setWindowSizeInit(None) is props
        assert props.getWindowSizeInit() is None
        value = self._make_positive(5)
        props.setWindowSizeInit(value)
        assert props.getWindowSizeInit() == value

    def test_get_set_window_size_invalid(self):
        props = EndToEndTransformationComSpecProps()
        assert props.setWindowSizeInvalid(None) is props
        assert props.getWindowSizeInvalid() is None
        value = self._make_positive(5)
        props.setWindowSizeInvalid(value)
        assert props.getWindowSizeInvalid() == value

    def test_get_set_window_size_valid(self):
        props = EndToEndTransformationComSpecProps()
        assert props.setWindowSizeValid(None) is props
        assert props.getWindowSizeValid() is None
        value = self._make_positive(5)
        props.setWindowSizeValid(value)
        assert props.getWindowSizeValid() == value

    def test_inherits_from_transformation_com_spec_props(self):
        from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.Communication import TransformationComSpecProps

        assert issubclass(EndToEndTransformationComSpecProps, TransformationComSpecProps)
