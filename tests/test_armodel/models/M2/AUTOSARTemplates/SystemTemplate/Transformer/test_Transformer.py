import pytest

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ARPackage import ARElement
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable import Describable, Identifiable
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
    SOMEIPMessageTypeEnum,
    SomeipTransformationISignalProps,
    TlvDataIdDefinition,
    TlvDataIdDefinitionSet,
    TransformationDescription,
    TransformationISignalProps,
    TransformationTechnology,
    TransformerClassEnum,
    UserDefinedTransformationISignalProps,
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
        assert issubclass(DataTransformationSet, ARElement)

        # Verbatim spec Note (AUTOSAR_CP_TPS_SystemTemplate Table 7.1)
        assert DataTransformationSet.__doc__ == (
            "This element is the system wide container of DataTransformations which represent transformer chains. " "Tags: atp.recommendedPackage=DataTransformationSets"
        )
        assert DataTransformationSet.__init__.__doc__ is None

        # Test default values
        assert data_set.getDataTransformations() == []
        assert data_set.getTransformationTechnologies() == []

        # Test create methods (duplicate short name returns the existing element)
        trans = data_set.createDataTransformation("test_transformation")
        assert isinstance(trans, DataTransformation)
        assert data_set.createDataTransformation("test_transformation") is trans
        assert len(data_set.getDataTransformations()) == 1

        tech = data_set.createTransformationTechnology("test_technology")
        assert isinstance(tech, TransformationTechnology)
        assert data_set.createTransformationTechnology("test_technology") is tech
        assert len(data_set.getTransformationTechnologies()) == 1

    def test_end_to_end_profile_behavior_enum(self):
        """
        Test EndToEndProfileBehaviorEnum class functionality.
        """
        enum = EndToEndProfileBehaviorEnum()

        # Test that it's properly initialized and instantiable
        assert isinstance(enum, EndToEndProfileBehaviorEnum)

        # Member names and values match the spec Enumeration literals (Table 7.26); values are the xml.name forms
        assert EndToEndProfileBehaviorEnum.PRE_R4_2 == "PRE-R-4-2"
        assert EndToEndProfileBehaviorEnum.R4_2 == "R-4-2"

        # Validated set of allowed values
        assert list(enum.getEnumValues()) == ["PRE-R-4-2", "R-4-2"]

        # setValue / getValue round-trip
        assert enum.setValue(EndToEndProfileBehaviorEnum.R4_2).getValue() == "R-4-2"
        assert enum.setValue(EndToEndProfileBehaviorEnum.PRE_R4_2).getValue() == "PRE-R-4-2"

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

        # Test instantiation with a value (XSD wire values)
        enum.setValue(CSTransformerErrorReactionEnum.AUTONOMOUS)
        assert enum.getValue() == "AUTONOMOUS"

        enum.setValue(CSTransformerErrorReactionEnum.APPLICATION_ONLY)
        assert enum.getValue() == "APPLICATION-ONLY"

    def test_transformation_isignal_props_abstract(self):
        """
        Test TransformationISignalProps abstract class functionality.
        """
        from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable import Describable
        from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import RefType
        from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Transformer import DataPrototypeTransformationProps

        with pytest.raises(TypeError):
            TransformationISignalProps()

        class ConcreteTransformationISignalProps(TransformationISignalProps):
            def __init__(self):
                super().__init__()

        props = ConcreteTransformationISignalProps()

        # Verbatim spec Note (AUTOSAR_CP_TPS_SystemTemplate Table 7.8)
        assert TransformationISignalProps.__doc__ == (
            "TransformationISignalProps holds all the attributes for the different TransformationTechnologies that are ISignal specific. " "Tags: vh.latestBindingTime=postBuild"
        )
        assert TransformationISignalProps.__init__.__doc__ is None
        assert issubclass(ConcreteTransformationISignalProps, Describable)
        assert issubclass(ConcreteTransformationISignalProps, TransformationISignalProps)

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

        assert props == props.addDataPrototypeTransformationProps(None)
        assert props.getDataPrototypeTransformationProps() == []  # Should remain empty list

        assert props == props.setTransformerRef(None)
        assert props.getTransformerRef() is None

        # Test setter/getter methods with method chaining - with actual values
        props.setCsErrorReaction(CSTransformerErrorReactionEnum.APPLICATION_ONLY)
        assert props.getCsErrorReaction() == CSTransformerErrorReactionEnum.APPLICATION_ONLY
        assert props == props.setCsErrorReaction(CSTransformerErrorReactionEnum.APPLICATION_ONLY)

        dp_props = DataPrototypeTransformationProps()
        assert props == props.addDataPrototypeTransformationProps(dp_props)
        assert props.getDataPrototypeTransformationProps() == [dp_props]
        assert props == props.setDataPrototypeTransformationProps([dp_props])
        assert props.getDataPrototypeTransformationProps() == [dp_props]

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


class Test_SOMEIPMessageTypeEnum:
    def test_docstring_is_spec_note_verbatim(self):
        # Table 7.13, p.779 — class Note verbatim from the markdown
        note = "Depending on the style of the communication different message types shall be set in the header of a SOME/IP message."
        assert SOMEIPMessageTypeEnum.__doc__.strip() == note

    def test_init_has_no_docstring(self):
        assert SOMEIPMessageTypeEnum.__init__.__doc__ is None

    def test_literal_values_and_indexes(self):
        # spec literals per Table 7.13 (notification idx1, request idx2, requestNoReturn idx3, response idx4, displayed order); xml values per XSD SIMPLE type
        assert SOMEIPMessageTypeEnum.NOTIFICATION == "NOTIFICATION"
        assert SOMEIPMessageTypeEnum.REQUEST == "REQUEST"
        assert SOMEIPMessageTypeEnum.REQUEST_NO_RETURN == "REQUEST-NO-RETURN"
        assert SOMEIPMessageTypeEnum.RESPONSE == "RESPONSE"
        e = SOMEIPMessageTypeEnum()
        assert e.getEnumValues() == ["NOTIFICATION", "REQUEST", "REQUEST-NO-RETURN", "RESPONSE"]
        assert e.validateEnumValue("NOTIFICATION") is True
        assert e.validateEnumValue("REQUEST") is True
        assert e.validateEnumValue("REQUEST-NO-RETURN") is True
        assert e.validateEnumValue("RESPONSE") is True
        assert e.validateEnumValue("ERROR") is False

    def test_instantiation(self):
        e = SOMEIPMessageTypeEnum()
        e.setValue(SOMEIPMessageTypeEnum.NOTIFICATION)
        assert e.getValue() == "NOTIFICATION"
        assert e.getText() == "NOTIFICATION"
        e.setValue(SOMEIPMessageTypeEnum.REQUEST)
        assert e.getValue() == "REQUEST"
        assert e.getText() == "REQUEST"
        e.setValue(SOMEIPMessageTypeEnum.REQUEST_NO_RETURN)
        assert e.getValue() == "REQUEST-NO-RETURN"
        assert e.getText() == "REQUEST-NO-RETURN"
        e.setValue(SOMEIPMessageTypeEnum.RESPONSE)
        assert e.getValue() == "RESPONSE"
        assert e.getText() == "RESPONSE"


class Test_TlvDataIdDefinition:
    def _make_positive(self, value):
        from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import PositiveInteger

        return PositiveInteger().setValue(value)

    def _make_ref(self, value, dest):
        from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import RefType

        ref = RefType()
        ref.setDest(dest)
        ref.setValue(value)
        return ref

    def test_docstring_is_spec_note_verbatim(self):
        # Table 7.31, p.831 — class Note verbatim from the markdown
        note = "This meta-class represents the ability to define the tlvDataId."
        assert TlvDataIdDefinition.__doc__.strip() == note

    def test_init_has_no_docstring(self):
        assert TlvDataIdDefinition.__init__.__doc__ is None

    def test_heritage_is_arobject_not_identifiable(self):
        assert issubclass(TlvDataIdDefinition, ARObject)
        assert not issubclass(TlvDataIdDefinition, Identifiable)
        assert not issubclass(TlvDataIdDefinition, ARElement)

    def test_initialization(self):
        tlv = TlvDataIdDefinition()

        assert tlv.getId() is None
        assert tlv.getTlvArgumentRef() is None
        assert tlv.getTlvImplementationDataTypeElementRef() is None
        assert tlv.getTlvRecordElementRef() is None

    def test_get_set_id(self):
        tlv = TlvDataIdDefinition()
        value = self._make_positive(7)

        assert tlv == tlv.setId(None)
        assert tlv.getId() is None

        assert tlv == tlv.setId(value)
        assert tlv.getId() == value
        assert tlv.getId().getValue() == 7

        assert tlv == tlv.setId(None)
        assert tlv.getId() == value

    def test_get_set_tlv_argument_ref(self):
        tlv = TlvDataIdDefinition()
        ref = self._make_ref("/PortInterface/op/arg", "ARGUMENT-DATA-PROTOTYPE")

        assert tlv == tlv.setTlvArgumentRef(None)
        assert tlv.getTlvArgumentRef() is None

        assert tlv == tlv.setTlvArgumentRef(ref)
        assert tlv.getTlvArgumentRef() == ref
        assert tlv.getTlvArgumentRef().getValue() == "/PortInterface/op/arg"
        assert tlv.getTlvArgumentRef().getDest() == "ARGUMENT-DATA-PROTOTYPE"

        assert tlv == tlv.setTlvArgumentRef(None)
        assert tlv.getTlvArgumentRef() == ref

    def test_get_set_tlv_implementation_data_type_element_ref(self):
        tlv = TlvDataIdDefinition()
        ref = self._make_ref("/DataType/element", "IMPLEMENTATION-DATA-TYPE-ELEMENT")

        assert tlv == tlv.setTlvImplementationDataTypeElementRef(None)
        assert tlv.getTlvImplementationDataTypeElementRef() is None

        assert tlv == tlv.setTlvImplementationDataTypeElementRef(ref)
        assert tlv.getTlvImplementationDataTypeElementRef() == ref
        assert tlv.getTlvImplementationDataTypeElementRef().getValue() == "/DataType/element"
        assert tlv.getTlvImplementationDataTypeElementRef().getDest() == "IMPLEMENTATION-DATA-TYPE-ELEMENT"

        assert tlv == tlv.setTlvImplementationDataTypeElementRef(None)
        assert tlv.getTlvImplementationDataTypeElementRef() == ref

    def test_get_set_tlv_record_element_ref(self):
        tlv = TlvDataIdDefinition()
        ref = self._make_ref("/DataType/record", "APPLICATION-RECORD-ELEMENT")

        assert tlv == tlv.setTlvRecordElementRef(None)
        assert tlv.getTlvRecordElementRef() is None

        assert tlv == tlv.setTlvRecordElementRef(ref)
        assert tlv.getTlvRecordElementRef() == ref
        assert tlv.getTlvRecordElementRef().getValue() == "/DataType/record"
        assert tlv.getTlvRecordElementRef().getDest() == "APPLICATION-RECORD-ELEMENT"

        assert tlv == tlv.setTlvRecordElementRef(None)
        assert tlv.getTlvRecordElementRef() == ref


class Test_TlvDataIdDefinitionSet:
    def _make_set(self):
        return TlvDataIdDefinitionSet(MockParent(), "TlvDataIdDefinitionSet")

    def _make_definition(self, id_value, ref_value, dest):
        from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import PositiveInteger, RefType

        tlv = TlvDataIdDefinition()
        tlv.setId(PositiveInteger().setValue(id_value))
        ref = RefType()
        ref.setDest(dest)
        ref.setValue(ref_value)
        tlv.setTlvArgumentRef(ref)
        return tlv

    def test_docstring_is_spec_note_verbatim(self):
        # Table 7.30, p.830 — class Note verbatim from the markdown (incl. Tags tail)
        note = "This meta-class acts as a container of TlvDataIdDefinitions to be used in a given context Tags: atp.recommendedPackage=TlvDataDefinitionSets"
        assert TlvDataIdDefinitionSet.__doc__.strip() == note

    def test_init_has_no_docstring(self):
        assert TlvDataIdDefinitionSet.__init__.__doc__ is None

    def test_heritage_is_aelement(self):
        assert issubclass(TlvDataIdDefinitionSet, ARElement)
        assert issubclass(TlvDataIdDefinitionSet, Identifiable)

        tlv_set = self._make_set()
        assert isinstance(tlv_set, ARElement)
        assert isinstance(tlv_set, Identifiable)

    def test_initialization_defaults(self):
        tlv_set = self._make_set()

        assert tlv_set.getShortName() == "TlvDataIdDefinitionSet"
        assert tlv_set.getTlvDataIdDefinitions() == []

    def test_add_tlv_data_id_definition_appends(self):
        tlv_set = self._make_set()
        first = self._make_definition(1, "/PortInterface/op/arg", "ARGUMENT-DATA-PROTOTYPE")
        second = self._make_definition(2, "/DataType/record", "APPLICATION-RECORD-ELEMENT")

        assert tlv_set == tlv_set.addTlvDataIdDefinition(first)
        assert tlv_set == tlv_set.addTlvDataIdDefinition(second)

        definitions = tlv_set.getTlvDataIdDefinitions()
        assert len(definitions) == 2
        assert definitions[0] is first
        assert definitions[1] is second
        assert definitions[0].getId().getValue() == 1
        assert definitions[1].getId().getValue() == 2
        assert definitions[0].getTlvArgumentRef().getValue() == "/PortInterface/op/arg"
        assert definitions[1].getTlvArgumentRef().getValue() == "/DataType/record"

    def test_add_tlv_data_id_definition_none_is_no_op(self):
        tlv_set = self._make_set()
        first = self._make_definition(1, "/PortInterface/op/arg", "ARGUMENT-DATA-PROTOTYPE")
        tlv_set.addTlvDataIdDefinition(first)

        assert tlv_set == tlv_set.addTlvDataIdDefinition(None)

        definitions = tlv_set.getTlvDataIdDefinitions()
        assert len(definitions) == 1
        assert definitions[0] is first


class Test_SomeipTransformationISignalProps:
    # Table 7.11, p.778 — attribute Notes verbatim from the markdown (cell wraps resolved per XSD mmt.qualifiedName / XSD documentation)
    NOTE_IMPLEMENTS_LEGACY_STRING_SERIALIZATION = (
        "This attribute indicates that Strings in the SOME/IP message shall NOT be serialized according to the SOME/IP specification for Strings. "
        "If this attribute is set to true, BOM and null-termination shall NOT be added in the serialization for Strings in the payload. "
        "If this attribute is set to false (or not set) BOM and null-termination shall be added in the serialization for Strings in the payload according to the SOME/IP specification for Strings. "
        'NOTE! This attribute is not future safe, and will be removed in an upcoming AUTOSAR release!" Tags: atp.Status=obsolete'
    )
    NOTE_INTERFACE_VERSION = "The interface version the SOME/IP transformer shall use."
    NOTE_IS_DYNAMIC_LENGTH_FIELD_SIZE = "This attribute shall be used to determine the wire type in the context of using the TLV encoding."
    NOTE_MESSAGE_TYPE = "The Message Type which shall be placed into the SOME/IP header."
    NOTE_SIZE_OF_ARRAY_LENGTH_FIELDS = "The size of all length fields (in Bytes) of fixed-size arrays or dynamic size arrays in the SOME/IP message. This attribute is valid for all available occurrences of fixed-size arrays or dynamic size arrays in the SOME/IP message."
    NOTE_SIZE_OF_STRING_LENGTH_FIELDS = (
        "The size of all length fields (in Bytes) of dynamic length strings in the SOME/IP message. This attribute is valid for all available occurrences of strings in the SOME/IP message."
    )
    NOTE_SIZE_OF_STRUCT_LENGTH_FIELDS = "The size of all length fields (in Bytes) of structs in the SOME/IP message. This attribute is valid for all available occurrences of structures in the SOME/IP message. For a more fine granular modeling on the level of DataPrototypes the DataPrototypeTransformationProps shall be used."
    NOTE_SIZE_OF_UNION_LENGTH_FIELDS = "The size of all length fields (in Bytes) of unions in the SOME/IP message. This attribute is valid for all available occurrences of Unions in the SOME/IP message. For a more fine granular modeling on the level of DataPrototypes the DataPrototypeTransformationProps shall be used."
    NOTE_TLV_DATA_ID_DEFINITION = "This reference identifies the TlvDataIdDefinitions relevant for the enclosing SOMEIPTransformationISignalProps"

    def _make_positive(self, value):
        from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import PositiveInteger

        return PositiveInteger().setValue(value)

    def _make_ref(self, value, dest):
        from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import RefType

        ref = RefType()
        ref.setDest(dest)
        ref.setValue(value)
        return ref

    def test_docstring_is_spec_note_verbatim(self):
        # Table 7.11, p.778 — class Note verbatim from the markdown
        note = "The class SOMEIPTransformationISignalProps specifies ISignal specific configuration properties for SOME/IP transformer attributes."
        assert SomeipTransformationISignalProps.__doc__.strip() == note

    def test_init_has_no_docstring(self):
        assert SomeipTransformationISignalProps.__init__.__doc__ is None

    def test_heritage(self):
        assert issubclass(SomeipTransformationISignalProps, TransformationISignalProps)
        assert issubclass(SomeipTransformationISignalProps, Describable)
        assert not issubclass(SomeipTransformationISignalProps, ARElement)

        props = SomeipTransformationISignalProps()
        assert isinstance(props, TransformationISignalProps)
        assert isinstance(props, Describable)

    def test_initialization(self):
        props = SomeipTransformationISignalProps()

        assert props.getImplementsLegacyStringSerialization() is None
        assert props.getInterfaceVersion() is None
        assert props.getIsDynamicLengthFieldSize() is None
        assert props.getMessageType() is None
        assert props.getSizeOfArrayLengthFields() is None
        assert props.getSizeOfStringLengthFields() is None
        assert props.getSizeOfStructLengthFields() is None
        assert props.getSizeOfUnionLengthFields() is None
        assert props.getTlvDataIdDefinitionRefs() == []

    def test_get_set_implements_legacy_string_serialization(self):
        props = SomeipTransformationISignalProps()
        value = Boolean().setValue(True)

        assert props == props.setImplementsLegacyStringSerialization(None)
        assert props.getImplementsLegacyStringSerialization() is None

        assert props == props.setImplementsLegacyStringSerialization(value)
        assert props.getImplementsLegacyStringSerialization() == value
        assert props.getImplementsLegacyStringSerialization().getValue() is True

        assert props == props.setImplementsLegacyStringSerialization(None)
        assert props.getImplementsLegacyStringSerialization() == value

    def test_get_set_interface_version(self):
        props = SomeipTransformationISignalProps()
        value = self._make_positive(4)

        assert props == props.setInterfaceVersion(None)
        assert props.getInterfaceVersion() is None

        assert props == props.setInterfaceVersion(value)
        assert props.getInterfaceVersion() == value
        assert props.getInterfaceVersion().getValue() == 4

        assert props == props.setInterfaceVersion(None)
        assert props.getInterfaceVersion() == value

    def test_get_set_is_dynamic_length_field_size(self):
        props = SomeipTransformationISignalProps()
        value = Boolean().setValue(False)

        assert props == props.setIsDynamicLengthFieldSize(None)
        assert props.getIsDynamicLengthFieldSize() is None

        assert props == props.setIsDynamicLengthFieldSize(value)
        assert props.getIsDynamicLengthFieldSize() == value
        assert props.getIsDynamicLengthFieldSize().getValue() is False

        assert props == props.setIsDynamicLengthFieldSize(None)
        assert props.getIsDynamicLengthFieldSize() == value

    def test_get_set_message_type(self):
        props = SomeipTransformationISignalProps()
        value = SOMEIPMessageTypeEnum().setValue(SOMEIPMessageTypeEnum.REQUEST_NO_RETURN)

        assert props == props.setMessageType(None)
        assert props.getMessageType() is None

        assert props == props.setMessageType(value)
        assert isinstance(props.getMessageType(), SOMEIPMessageTypeEnum)
        assert props.getMessageType().getValue() == "REQUEST-NO-RETURN"

        assert props == props.setMessageType(None)
        assert props.getMessageType().getValue() == "REQUEST-NO-RETURN"

    def test_get_set_size_of_array_length_fields(self):
        props = SomeipTransformationISignalProps()
        value = self._make_positive(8)

        assert props == props.setSizeOfArrayLengthFields(None)
        assert props.getSizeOfArrayLengthFields() is None

        assert props == props.setSizeOfArrayLengthFields(value)
        assert props.getSizeOfArrayLengthFields().getValue() == 8

        assert props == props.setSizeOfArrayLengthFields(None)
        assert props.getSizeOfArrayLengthFields().getValue() == 8

    def test_get_set_size_of_string_length_fields(self):
        props = SomeipTransformationISignalProps()
        value = self._make_positive(12)

        assert props == props.setSizeOfStringLengthFields(None)
        assert props.getSizeOfStringLengthFields() is None

        assert props == props.setSizeOfStringLengthFields(value)
        assert props.getSizeOfStringLengthFields().getValue() == 12

        assert props == props.setSizeOfStringLengthFields(None)
        assert props.getSizeOfStringLengthFields().getValue() == 12

    def test_get_set_size_of_struct_length_fields(self):
        props = SomeipTransformationISignalProps()
        value = self._make_positive(16)

        assert props == props.setSizeOfStructLengthFields(None)
        assert props.getSizeOfStructLengthFields() is None

        assert props == props.setSizeOfStructLengthFields(value)
        assert props.getSizeOfStructLengthFields().getValue() == 16

        assert props == props.setSizeOfStructLengthFields(None)
        assert props.getSizeOfStructLengthFields().getValue() == 16

    def test_get_set_size_of_union_length_fields(self):
        props = SomeipTransformationISignalProps()
        value = self._make_positive(4)

        assert props == props.setSizeOfUnionLengthFields(None)
        assert props.getSizeOfUnionLengthFields() is None

        assert props == props.setSizeOfUnionLengthFields(value)
        assert props.getSizeOfUnionLengthFields().getValue() == 4

        assert props == props.setSizeOfUnionLengthFields(None)
        assert props.getSizeOfUnionLengthFields().getValue() == 4

    def test_add_tlv_data_id_definition_ref_appends(self):
        props = SomeipTransformationISignalProps()
        first = self._make_ref("/TlvSets/Set1", "TLV-DATA-ID-DEFINITION-SET")
        second = self._make_ref("/TlvSets/Set2", "TLV-DATA-ID-DEFINITION-SET")

        assert props == props.addTlvDataIdDefinitionRef(None)
        assert props.getTlvDataIdDefinitionRefs() == []

        assert props == props.addTlvDataIdDefinitionRef(first)
        assert props == props.addTlvDataIdDefinitionRef(second)

        refs = props.getTlvDataIdDefinitionRefs()
        assert len(refs) == 2
        assert refs[0] is first
        assert refs[1] is second
        assert refs[0].getValue() == "/TlvSets/Set1"
        assert refs[0].getDest() == "TLV-DATA-ID-DEFINITION-SET"

        assert props == props.addTlvDataIdDefinitionRef(None)
        assert len(props.getTlvDataIdDefinitionRefs()) == 2


class Test_UserDefinedTransformationISignalProps:
    # Table 7.28, p.828 — class Note verbatim from the markdown; zero attribute rows
    # (J1939NmEcu zero-attr precedent: shape = base + nothing)

    def test_concrete_instantiation_and_heritage(self):
        props = UserDefinedTransformationISignalProps()
        assert isinstance(props, TransformationISignalProps)
        assert isinstance(props, Describable)
        assert issubclass(UserDefinedTransformationISignalProps, TransformationISignalProps)
        assert issubclass(UserDefinedTransformationISignalProps, Describable)
        assert not issubclass(UserDefinedTransformationISignalProps, ARElement)

    def test_class_docstring_is_spec_note_verbatim(self):
        # Table 7.28, p.828 — class Note verbatim from the markdown
        note = "The UserDefinedTransformationISignalProps is used to specify ISignal specific configuration properties for custom transformers."
        assert UserDefinedTransformationISignalProps.__doc__.strip() == note

    def test_init_has_no_docstring(self):
        assert UserDefinedTransformationISignalProps.__init__.__doc__ is None

    def test_zero_own_attributes(self):
        # Zero attribute rows (Table 7.28) — no new public accessors beyond the base class
        props = UserDefinedTransformationISignalProps()
        base_accessors = {name for name in dir(TransformationISignalProps) if not name.startswith("_") and callable(getattr(TransformationISignalProps, name, None))}
        own_accessors = {name for name in dir(props) if not name.startswith("_") and callable(getattr(props, name, None))} - base_accessors
        assert own_accessors == set()
