import pytest
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Transformer import (
    DataTransformationKindEnum,
    DataTransformation,
    BufferProperties,
    TransformationDescription,
    DataIdModeEnum,
    EndToEndProfileBehaviorEnum,
    EndToEndTransformationDescription,
    TransformerClassEnum,
    TransformationTechnology,
    DataTransformationSet,
    TransformationISignalProps,
    EndToEndTransformationISignalProps
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable import Identifiable, ARElement, Describable


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

    def test_buffer_properties(self):
        """
        Test BufferProperties class functionality with method chaining and None handling.
        """
        buffer_props = BufferProperties()

        assert isinstance(buffer_props, ARObject)
        
        # Test default values
        assert buffer_props.getBufferComputation() is None
        assert buffer_props.getHeaderLength() is None
        assert buffer_props.getInPlace() is None

        # Test setter/getter methods with method chaining - with None values
        assert buffer_props == buffer_props.setBufferComputation(None)
        assert buffer_props.getBufferComputation() is None

        assert buffer_props == buffer_props.setHeaderLength(None)
        assert buffer_props.getHeaderLength() is None

        assert buffer_props == buffer_props.setInPlace(None)
        assert buffer_props.getInPlace() is None

        # Test setter/getter methods with method chaining - with actual values
        buffer_props.setHeaderLength(10)
        assert buffer_props.getHeaderLength() == 10
        assert buffer_props == buffer_props.setHeaderLength(10)
        
        buffer_props.setInPlace(True)
        assert buffer_props.getInPlace() is True
        assert buffer_props == buffer_props.setInPlace(True)

    def test_data_id_mode_enum(self):
        """
        Test DataIdModeEnum class functionality.
        """
        enum = DataIdModeEnum()

        # Test that it's properly initialized
        assert enum is not None
        assert hasattr(enum, 'ALL_16_BIT')
        assert hasattr(enum, 'ALTERNATING_8_BIT')
        assert hasattr(enum, 'LOWER_12_BIT')
        assert hasattr(enum, 'LOWER_8_BIT')

    def test_data_transformation(self):
        """
        Test DataTransformation class functionality with method chaining and None handling.
        """
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
        mock_kind = DataTransformationKindEnum()
        transformation.setDataTransformationKind(mock_kind)
        assert transformation.getDataTransformationKind() == mock_kind
        assert transformation == transformation.setDataTransformationKind(mock_kind)
        
        transformation.setExecuteDespiteDataUnavailability(True)
        assert transformation.getExecuteDespiteDataUnavailability() is True
        assert transformation == transformation.setExecuteDespiteDataUnavailability(True)
        
        # Test addTransformerChainRef with method chaining
        transformation.addTransformerChainRef("chain_ref")
        assert transformation.getTransformerChainRefs() == ["chain_ref"]
        assert transformation == transformation.addTransformerChainRef("chain_ref2")
        assert len(transformation.getTransformerChainRefs()) == 2

    def test_data_transformation_kind_enum(self):
        """
        Test DataTransformationKindEnum class functionality.
        """
        enum = DataTransformationKindEnum()

        # Test that it's properly initialized
        assert enum is not None

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

        # Test that it's properly initialized
        assert enum is not None
        assert hasattr(enum, 'PRE_R4_2')
        assert hasattr(enum, 'R4_2')

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
        with pytest.raises(NotImplementedError):
            TransformationDescription()

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

        technology.setTransformerClass(TransformerClassEnum.SECURITY)
        assert technology.getTransformerClass() == TransformerClassEnum.SECURITY
        assert technology == technology.setTransformerClass(TransformerClassEnum.SECURITY)

        technology.setVersion("1.0")
        assert technology.getVersion() == "1.0"
        assert technology == technology.setVersion("1.0")

    def test_transformer_class_enum(self):
        """
        Test TransformerClassEnum class functionality.
        """
        enum = TransformerClassEnum()

        # Test that it's properly initialized
        assert enum is not None
        assert hasattr(enum, 'CUSTOM')
        assert hasattr(enum, 'SAFETY')
        assert hasattr(enum, 'SECURITY')
        assert hasattr(enum, 'SERIALIZER')

    def test_transformation_isignal_props_abstract(self):
        """
        Test TransformationISignalProps abstract class functionality.
        """
        class ConcreteTransformationISignalProps(TransformationISignalProps):
            def __init__(self):
                super().__init__()

        props = ConcreteTransformationISignalProps()

        # Test default values
        assert props.getCsErrorReaction() is None
        assert props.getDataPrototypeTransformationProps() == []
        assert props.getIdent() is None
        assert props.getTransformerRef() is None

        # Test setter/getter methods with method chaining - with None values
        assert props == props.setCsErrorReaction(None)
        assert props.getCsErrorReaction() is None

        assert props == props.setDataPrototypeTransformationProps(None)
        assert props.getDataPrototypeTransformationProps() == []  # Should remain empty list

        assert props == props.setIdent(None)
        assert props.getIdent() is None

        assert props == props.setTransformerRef(None)
        assert props.getTransformerRef() is None

        # Test setter/getter methods with method chaining - with actual values
        props.setCsErrorReaction("error_reaction")
        assert props.getCsErrorReaction() == "error_reaction"
        assert props == props.setCsErrorReaction("error_reaction")

        props.setDataPrototypeTransformationProps(["prop1", "prop2"])
        assert "prop1" in props.getDataPrototypeTransformationProps()
        assert props == props.setDataPrototypeTransformationProps(["prop1", "prop2"])

        props.setIdent("ident_value")
        assert props.getIdent() == "ident_value"
        assert props == props.setIdent("ident_value")

        props.setTransformerRef("transformer_ref")
        assert props.getTransformerRef() == "transformer_ref"
        assert props == props.setTransformerRef("transformer_ref")

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