
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.SecureCommunication import (
    CryptoServiceMapping,
    SecOcCryptoServiceMapping,
    TlsCryptoServiceMapping
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable import Identifiable
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import ARObject


class MockParent(ARObject):
    def __init__(self):
        super().__init__()


class Test_SecureCommunication:
    """Test cases for SecureCommunication-related classes."""
    
    def test_CryptoServiceMapping(self):
        """Test CryptoServiceMapping class functionality."""
        parent = MockParent()
        mapping = CryptoServiceMapping(parent, "test_crypto_mapping")

        assert isinstance(mapping, Identifiable)

    def test_SecOcCryptoServiceMapping(self):
        """Test SecOcCryptoServiceMapping class functionality."""
        parent = MockParent()
        mapping = SecOcCryptoServiceMapping(parent, "test_secoc_mapping")

        assert isinstance(mapping, CryptoServiceMapping)
        
        # Test default values
        assert mapping.getAuthenticationRef() is None
        assert mapping.getCryptoServiceKeyRef() is None
        assert mapping.getCryptoServiceQueueRef() is None
        
        # Test setter/getter methods
        mock_auth_ref = "mock_auth_ref"
        mapping.setAuthenticationRef(mock_auth_ref)
        assert mapping.getAuthenticationRef() == mock_auth_ref
        
        mock_key_ref = "mock_key_ref"
        mapping.setCryptoServiceKeyRef(mock_key_ref)
        assert mapping.getCryptoServiceKeyRef() == mock_key_ref
        
        mock_queue_ref = "mock_queue_ref"
        mapping.setCryptoServiceQueueRef(mock_queue_ref)
        assert mapping.getCryptoServiceQueueRef() == mock_queue_ref

    def test_TlsCryptoServiceMapping(self):
        """Test TlsCryptoServiceMapping class functionality."""
        parent = MockParent()
        mapping = TlsCryptoServiceMapping(parent, "test_tls_mapping")

        assert isinstance(mapping, CryptoServiceMapping)
        
        # Test default values
        assert mapping.getKeyExchangeRef() is None
        assert mapping.getTlsCipherSuites() == []
        assert mapping.getUseClientAuthenticationRequest() is None
        assert mapping.getUseSecurityExtensionRecordSizeLimit() is None
        
        # Test setter/getter methods
        mock_key_ref = "mock_key_ref"
        mapping.setKeyExchangeRef(mock_key_ref)
        assert mapping.getKeyExchangeRef() == mock_key_ref
        
        mock_cipher_suite = "AES_128_GCM"
        mapping.addTlsCipherSuite(mock_cipher_suite)
        assert mapping.getTlsCipherSuites() == [mock_cipher_suite]
        
        mapping.setUseClientAuthenticationRequest(True)
        assert mapping.getUseClientAuthenticationRequest() is True
        
        mapping.setUseSecurityExtensionRecordSizeLimit(False)
        assert mapping.getUseSecurityExtensionRecordSizeLimit() is False