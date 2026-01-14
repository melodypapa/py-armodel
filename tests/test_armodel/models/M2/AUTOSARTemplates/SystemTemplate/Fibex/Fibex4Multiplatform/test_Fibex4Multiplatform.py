import pytest
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Multiplatform import (
    FrameMapping,
    ISignalMapping,
    DefaultValueElement,
    PduMappingDefaultValue,
    TargetIPduRef,
    IPduMapping,
    Gateway
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import ARObject


class MockParent(ARObject):
    def __init__(self):
        super().__init__()


class TestFibex4Multiplatform:
    """
    Test class for Fibex4Multiplatform module functionality.
    This class contains test methods for validating the behavior of
    multiplatform communication mapping classes, including their initialization,
    inheritance relationships, and property accessors.
    """

    def test_frame_mapping(self):
        """
        Test FrameMapping class functionality with method chaining and None handling.
        """
        frame_mapping = FrameMapping()

        # Test constructor
        assert frame_mapping is not None

        # Test default values
        assert frame_mapping.getIntroduction() is None
        assert frame_mapping.getSourceFrameRef() is None
        assert frame_mapping.getTargetFrameRef() is None

        # Test setter/getter methods with method chaining - with actual values
        frame_mapping.setSourceFrameRef("source_frame_ref")
        assert frame_mapping.getSourceFrameRef() == "source_frame_ref"
        assert frame_mapping == frame_mapping.setSourceFrameRef("source_frame_ref")

        frame_mapping.setTargetFrameRef("target_frame_ref")
        assert frame_mapping.getTargetFrameRef() == "target_frame_ref"
        assert frame_mapping == frame_mapping.setTargetFrameRef("target_frame_ref")

        # Test setIntroduction to cover lines 21-22
        frame_mapping.setIntroduction("test_introduction")
        assert frame_mapping.getIntroduction() == "test_introduction"
        assert frame_mapping == frame_mapping.setIntroduction("test_introduction")

    def test_isignal_mapping(self):
        """
        Test ISignalMapping class functionality with method chaining and None handling.
        """
        signal_mapping = ISignalMapping()

        # Test constructor
        assert signal_mapping is not None

        # Test default values
        assert signal_mapping.getIntroduction() is None
        assert signal_mapping.getSourceSignalRef() is None
        assert signal_mapping.getTargetSignalRef() is None

        # Test setter/getter methods with method chaining - with actual values
        signal_mapping.setSourceSignalRef("source_signal_ref")
        assert signal_mapping.getSourceSignalRef() == "source_signal_ref"
        assert signal_mapping == signal_mapping.setSourceSignalRef("source_signal_ref")

        signal_mapping.setTargetSignalRef("target_signal_ref")
        assert signal_mapping.getTargetSignalRef() == "target_signal_ref"
        assert signal_mapping == signal_mapping.setTargetSignalRef("target_signal_ref")

        # Test setIntroduction to cover lines 50-51
        signal_mapping.setIntroduction("test_introduction")
        assert signal_mapping.getIntroduction() == "test_introduction"
        assert signal_mapping == signal_mapping.setIntroduction("test_introduction")

    def test_default_value_element(self):
        """
        Test DefaultValueElement class functionality with method chaining and None handling.
        """
        default_val_elem = DefaultValueElement()

        # Test constructor
        assert default_val_elem is not None

        # Test default values
        assert default_val_elem.getElementByteValue() is None
        assert default_val_elem.getElementPosition() is None

        # Test setter/getter methods with method chaining - with None values (tests the if value is not None logic)
        assert default_val_elem == default_val_elem.setElementByteValue(None)
        assert default_val_elem.getElementByteValue() is None

        assert default_val_elem == default_val_elem.setElementPosition(None)
        assert default_val_elem.getElementPosition() is None

        # Test setter/getter methods with method chaining - with actual values
        default_val_elem.setElementByteValue(255)
        assert default_val_elem.getElementByteValue() == 255
        assert default_val_elem == default_val_elem.setElementByteValue(255)
        
        default_val_elem.setElementPosition(1)
        assert default_val_elem.getElementPosition() == 1
        assert default_val_elem == default_val_elem.setElementPosition(1)

    def test_default_value_element_none_handling(self):
        """
        Test DefaultValueElement None value handling specifically to achieve 100% coverage.
        """
        default_val_elem = DefaultValueElement()

        # Test that setting None keeps the original value (which is None) - tests the if value is not None logic
        assert default_val_elem.getElementByteValue() is None
        result = default_val_elem.setElementByteValue(None)
        assert result == default_val_elem
        # Since value is None, elementByteValue should remain None
        assert default_val_elem.getElementByteValue() is None

        assert default_val_elem.getElementPosition() is None
        result = default_val_elem.setElementPosition(None)
        assert result == default_val_elem
        # Since value is None, elementPosition should remain None
        assert default_val_elem.getElementPosition() is None

        # Test setting actual value then trying to set to None (should not change the value)
        default_val_elem.setElementByteValue(42)
        assert default_val_elem.getElementByteValue() == 42
        result = default_val_elem.setElementByteValue(None)
        assert result == default_val_elem
        # Since value is None, elementByteValue should remain 42 (not set)
        assert default_val_elem.getElementByteValue() == 42

    def test_pdu_mapping_default_value(self):
        """
        Test PduMappingDefaultValue class functionality with method chaining and None handling.
        """
        pdu_default = PduMappingDefaultValue()

        # Test constructor
        assert pdu_default is not None

        # Test default values
        assert pdu_default.getDefaultValueElements() == []

        # Test setter/getter methods with method chaining - with actual values
        elem = DefaultValueElement()
        pdu_default.addDefaultValueElements([elem])
        assert elem in pdu_default.getDefaultValueElements()
        assert pdu_default == pdu_default.addDefaultValueElements([elem])

    def test_pdu_mapping_default_value_none_handling(self):
        """
        Test PduMappingDefaultValue addDefaultValueElements None value handling specifically to achieve 100% coverage.
        """
        pdu_default = PduMappingDefaultValue()

        # Test that setting None keeps the original value (which is []) - tests the if value is not None logic
        original_list = pdu_default.getDefaultValueElements()
        assert original_list == []
        result = pdu_default.addDefaultValueElements(None)
        assert result == pdu_default
        # Since value is None, defaultValueElements should remain as the original empty list
        assert pdu_default.getDefaultValueElements() == []
        
        # Test with non-empty list, then try to set to None
        elem = DefaultValueElement()
        pdu_default.addDefaultValueElements([elem])
        assert elem in pdu_default.getDefaultValueElements()
        result = pdu_default.addDefaultValueElements(None)
        assert result == pdu_default
        # Since value is None, defaultValueElements should remain as it was
        assert elem in pdu_default.getDefaultValueElements()

    def test_target_ipdu_ref(self):
        """
        Test TargetIPduRef class functionality with method chaining and None handling.
        """
        target_ipdu = TargetIPduRef()

        # Test constructor
        assert target_ipdu is not None

        # Test default values
        assert target_ipdu.getDefaultValue() is None
        assert target_ipdu.getTargetIPdu() is None

        # Test setter/getter methods with method chaining - with None values
        assert target_ipdu == target_ipdu.setDefaultValue(None)
        assert target_ipdu.getDefaultValue() is None

        assert target_ipdu == target_ipdu.setTargetIPdu(None)
        assert target_ipdu.getTargetIPdu() is None

        # Test setter/getter methods with method chaining - with actual values
        default_val = PduMappingDefaultValue()
        target_ipdu.setDefaultValue(default_val)
        assert target_ipdu.getDefaultValue() == default_val
        assert target_ipdu == target_ipdu.setDefaultValue(default_val)
        
        target_ipdu.setTargetIPdu("target_ipdu_ref")
        assert target_ipdu.getTargetIPdu() == "target_ipdu_ref"
        assert target_ipdu == target_ipdu.setTargetIPdu("target_ipdu_ref")

    def test_target_ipdu_ref_none_handling(self):
        """
        Test TargetIPduRef setDefaultValue None value handling specifically to achieve 100% coverage.
        """
        target_ipdu = TargetIPduRef()

        # Test that setting None keeps the original value (which is None) - tests the if value is not None logic
        assert target_ipdu.getDefaultValue() is None
        result = target_ipdu.setDefaultValue(None)
        assert result == target_ipdu
        # Since value is None, defaultValue should remain None
        assert target_ipdu.getDefaultValue() is None

        # Test setting actual value then trying to set to None (should not change the value)
        default_val = PduMappingDefaultValue()
        target_ipdu.setDefaultValue(default_val)
        assert target_ipdu.getDefaultValue() == default_val
        result = target_ipdu.setDefaultValue(None)
        assert result == target_ipdu
        # Since value is None, defaultValue should remain as default_val (not set)
        assert target_ipdu.getDefaultValue() == default_val

    def test_ipdu_mapping(self):
        """
        Test IPduMapping class functionality with method chaining and None handling.
        """
        ipdu_mapping = IPduMapping()

        # Test constructor
        assert ipdu_mapping is not None

        # Test default values
        assert ipdu_mapping.getIntroduction() is None
        assert ipdu_mapping.getPdurTpChunkSize() is None
        assert ipdu_mapping.getSourceIpduRef() is None
        assert ipdu_mapping.getTargetIPdu() is None

        # Test setter/getter methods with method chaining - with None values
        assert ipdu_mapping == ipdu_mapping.setIntroduction(None)
        assert ipdu_mapping.getIntroduction() is None

        assert ipdu_mapping == ipdu_mapping.setPdurTpChunkSize(None)
        assert ipdu_mapping.getPdurTpChunkSize() is None

        assert ipdu_mapping == ipdu_mapping.setSourceIpduRef(None)
        assert ipdu_mapping.getSourceIpduRef() is None

        assert ipdu_mapping == ipdu_mapping.setTargetIPdu(None)
        assert ipdu_mapping.getTargetIPdu() is None

        # Test setter/getter methods with method chaining - with actual values
        ipdu_mapping.setPdurTpChunkSize(64)
        assert ipdu_mapping.getPdurTpChunkSize() == 64
        assert ipdu_mapping == ipdu_mapping.setPdurTpChunkSize(64)
        
        ipdu_mapping.setSourceIpduRef("source_ipdu_ref")
        assert ipdu_mapping.getSourceIpduRef() == "source_ipdu_ref"
        assert ipdu_mapping == ipdu_mapping.setSourceIpduRef("source_ipdu_ref")

        target_ipdu = TargetIPduRef()
        ipdu_mapping.setTargetIPdu(target_ipdu)
        assert ipdu_mapping.getTargetIPdu() == target_ipdu
        assert ipdu_mapping == ipdu_mapping.setTargetIPdu(target_ipdu)

    def test_ipdu_mapping_target_ipdu_none_handling(self):
        """
        Test IPduMapping setTargetIPdu None value handling specifically to achieve 100% coverage.
        """
        ipdu_mapping = IPduMapping()

        # Test that setting None keeps the original value (which is None) - tests the if value is not None logic
        assert ipdu_mapping.getTargetIPdu() is None
        result = ipdu_mapping.setTargetIPdu(None)
        assert result == ipdu_mapping
        # Since value is None, targetIPdu should remain None
        assert ipdu_mapping.getTargetIPdu() is None

        # Test setting actual value then trying to set to None (should not change the value)
        target_ipdu = TargetIPduRef()
        ipdu_mapping.setTargetIPdu(target_ipdu)
        assert ipdu_mapping.getTargetIPdu() == target_ipdu
        result = ipdu_mapping.setTargetIPdu(None)
        assert result == ipdu_mapping
        # Since value is None, targetIPdu should remain as target_ipdu (not set)
        assert ipdu_mapping.getTargetIPdu() == target_ipdu

    def test_ipdu_mapping_introduction_none_handling(self):
        """
        Test IPduMapping setIntroduction None value handling to achieve 100% coverage.
        """
        ipdu_mapping = IPduMapping()

        # Test that setting None keeps the original value (which is None) - tests the if value is not None logic
        assert ipdu_mapping.getIntroduction() is None
        result = ipdu_mapping.setIntroduction(None)
        assert result == ipdu_mapping
        # Since value is None, introduction should remain None
        assert ipdu_mapping.getIntroduction() is None

        # Test setting actual value then trying to set to None (should not change the value)
        ipdu_mapping.setIntroduction("some introduction")
        assert ipdu_mapping.getIntroduction() == "some introduction"
        result = ipdu_mapping.setIntroduction(None)
        assert result == ipdu_mapping
        # Since value is None, introduction should remain as before (not set)
        assert ipdu_mapping.getIntroduction() == "some introduction"

    def test_ipdu_mapping_pdur_tp_chunk_size_none_handling(self):
        """
        Test IPduMapping setPdurTpChunkSize None value handling to achieve 100% coverage.
        """
        ipdu_mapping = IPduMapping()

        # Test that setting None keeps the original value (which is None) - tests the if value is not None logic
        assert ipdu_mapping.getPdurTpChunkSize() is None
        result = ipdu_mapping.setPdurTpChunkSize(None)
        assert result == ipdu_mapping
        # Since value is None, pdurTpChunkSize should remain None
        assert ipdu_mapping.getPdurTpChunkSize() is None

        # Test setting actual value then trying to set to None (should not change the value)
        ipdu_mapping.setPdurTpChunkSize(64)
        assert ipdu_mapping.getPdurTpChunkSize() == 64
        result = ipdu_mapping.setPdurTpChunkSize(None)
        assert result == ipdu_mapping
        # Since value is None, pdurTpChunkSize should remain as before (not set)
        assert ipdu_mapping.getPdurTpChunkSize() == 64

    def test_ipdu_mapping_source_ipdu_ref_none_handling(self):
        """
        Test IPduMapping setSourceIpduRef None value handling to achieve 100% coverage.
        """
        ipdu_mapping = IPduMapping()

        # Test that setting None keeps the original value (which is None) - tests the if value is not None logic
        assert ipdu_mapping.getSourceIpduRef() is None
        result = ipdu_mapping.setSourceIpduRef(None)
        assert result == ipdu_mapping
        # Since value is None, sourceIpduRef should remain None
        assert ipdu_mapping.getSourceIpduRef() is None

        # Test setting actual value then trying to set to None (should not change the value)
        ipdu_mapping.setSourceIpduRef("some_ref")
        assert ipdu_mapping.getSourceIpduRef() == "some_ref"
        result = ipdu_mapping.setSourceIpduRef(None)
        assert result == ipdu_mapping
        # Since value is None, sourceIpduRef should remain as before (not set)
        assert ipdu_mapping.getSourceIpduRef() == "some_ref"

    def test_gateway(self):
        """
        Test Gateway class functionality with method chaining and None handling.
        """
        parent = MockParent()
        gateway = Gateway(parent, "test_gateway")

        # Test constructor
        assert gateway is not None

        # Test default values
        assert gateway.getEcuRef() is None
        assert gateway.getFrameMappings() == []
        assert gateway.getIPduMappings() == []
        assert gateway.getSignalMappings() == []

        # Test setter/getter methods with method chaining
        gateway.setEcuRef("ecu_ref")
        assert gateway.getEcuRef() == "ecu_ref"
        assert gateway == gateway.setEcuRef("ecu_ref")

        # Test add methods
        frame_mapping = FrameMapping()
        gateway.addFrameMapping(frame_mapping)
        assert frame_mapping in gateway.getFrameMappings()
        assert gateway == gateway.addFrameMapping(frame_mapping)

        ipdu_mapping = IPduMapping()
        gateway.addIPduMapping(ipdu_mapping)
        assert ipdu_mapping in gateway.getIPduMappings()
        assert gateway == gateway.addIPduMapping(ipdu_mapping)

        signal_mapping = ISignalMapping()
        gateway.addSignalMapping(signal_mapping)
        assert signal_mapping in gateway.getSignalMappings()
        assert gateway == gateway.addSignalMapping(signal_mapping)