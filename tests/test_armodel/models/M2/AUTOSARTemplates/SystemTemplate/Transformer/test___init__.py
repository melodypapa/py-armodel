"""
Test suite for Transformer classes in AUTOSAR System Template.

This module contains comprehensive unit tests for data transformation classes
including transformation technologies, end-to-end protection, and transformation properties.
Each test validates the functionality, inheritance, and setter/getter methods
of the respective classes.
"""

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
    """
    Mock parent class for testing purposes.
    
    This class extends ARObject to provide a concrete implementation
    that can be used as a parent for testing classes that require
    an ARObject instance during initialization.
    """
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
        Test BufferProperties class functionality.
        """
        buffer_props = BufferProperties()

        assert isinstance(buffer_props, ARObject)
        
        # Test default values
        assert buffer_props.getBufferComputation() is None
        assert buffer_props.getHeaderLength() is None
        assert buffer_props.getInPlace() is None
        
        # Test setter/getter methods
        # Since we can't easily import CompuScale, just test with None or a simple object
        buffer_props.setHeaderLength(10)
        assert buffer_props.getHeaderLength() == 10
        
        buffer_props.setInPlace(True)
        assert buffer_props.getInPlace() is True

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
        Test DataTransformation class functionality.
        """
        parent = MockParent()
        transformation = DataTransformation(parent, "test_transformation")

        assert isinstance(transformation, Identifiable)
        
        # Test default values
        assert transformation.getDataTransformationKind() is None
        assert transformation.getExecuteDespiteDataUnavailability() is None
        assert transformation.getTransformerChainRefs() == []
        
        # Test setter/getter methods
        mock_kind = DataTransformationKindEnum()
        transformation.setDataTransformationKind(mock_kind)
        assert transformation.getDataTransformationKind() == mock_kind
        
        transformation.setExecuteDespiteDataUnavailability(True)
        assert transformation.getExecuteDespiteDataUnavailability() is True
        
        transformation.addTransformerChainRef("chain_ref")
        assert transformation.getTransformerChainRefs() == ["chain_ref"]

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
        Test EndToEndTransformationDescription class functionality.
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
        
        # Test setter/getter methods
        description.setCounterOffset(5)
        assert description.getCounterOffset() == 5
        
        description.setClearFromValidToInvalid(True)
        assert description.getClearFromValidToInvalid() is True

    def test_transformation_description_abstract(self):
        """
        Test TransformationDescription abstract class functionality.
        """
        with pytest.raises(NotImplementedError):
            TransformationDescription()

    def test_transformation_technology(self):
        """
        Test TransformationTechnology class functionality.
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
        
        # Test setter/getter methods
        mock_buffer = BufferProperties()
        technology.setBufferProperties(mock_buffer)
        assert technology.getBufferProperties() == mock_buffer
        
        technology.setHasInternalState(True)
        assert technology.getHasInternalState() is True
        
        technology.setProtocol("e2e")
        assert technology.getProtocol() == "e2e"

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