# This module contains AUTOSAR System Template classes for secure communication
# It defines crypto service mappings and TLS configurations for secure data transmission

from abc import ABC
from typing import List, Union

from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable import (
    Identifiable,
)
from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Boolean,
    RefType,
)


class CryptoServiceMapping(Identifiable, ABC):
    """
    Abstract base class for crypto service mappings, defining
    common properties for different types of cryptographic
    service mappings in the AUTOSAR system.
    """

    def __init__(self, parent, short_name) -> None:
        if type(self) is CryptoServiceMapping:
            raise TypeError("CryptoServiceMapping is an abstract class.")
        super().__init__(parent, short_name)


class SecOcCryptoServiceMapping(CryptoServiceMapping):
    """
    Represents a Secure Onboard Communication (SecOC) crypto service mapping,
    defining authentication, key, and queue references for secure
    communication between ECUs.
    """
    def __init__(self, parent, short_name) -> None:
        super().__init__(parent, short_name)

        self.authenticationRef: Union[Union[RefType, None] , None] = None
        self.cryptoServiceKeyRef: Union[Union[RefType, None] , None] = None
        self.cryptoServiceQueueRef: Union[Union[RefType, None] , None] = None

    def getAuthenticationRef(self):
        return self.authenticationRef

    def setAuthenticationRef(self, value):
        if value is not None:
            self.authenticationRef = value
        return self

    def getCryptoServiceKeyRef(self):
        return self.cryptoServiceKeyRef

    def setCryptoServiceKeyRef(self, value):
        if value is not None:
            self.cryptoServiceKeyRef = value
        return self

    def getCryptoServiceQueueRef(self):
        return self.cryptoServiceQueueRef

    def setCryptoServiceQueueRef(self, value):
        if value is not None:
            self.cryptoServiceQueueRef = value
        return self


class TlsCryptoServiceMapping(CryptoServiceMapping):
    """
    Represents a TLS (Transport Layer Security) crypto service mapping,
    defining key exchange references, cipher suites, and authentication
    settings for TLS-secured communication.
    """
    def __init__(self, parent, short_name) -> None:
        super().__init__(parent, short_name)

        self.keyExchangeRef: Union[Union[RefType, None] , None] = None
        self.tlsCipherSuites: List = []
        self.useClientAuthenticationRequest: Union[Union[Boolean, None] , None] = None
        self.useSecurityExtensionRecordSizeLimit: Union[Union[Boolean, None] , None] = None

    def getKeyExchangeRef(self):
        return self.keyExchangeRef

    def setKeyExchangeRef(self, value):
        if value is not None:
            self.keyExchangeRef = value
        return self

    def getTlsCipherSuites(self):
        return self.tlsCipherSuites

    def addTlsCipherSuite(self, value):
        if value is not None:
            self.tlsCipherSuites.append(value)
        return self

    def getUseClientAuthenticationRequest(self):
        return self.useClientAuthenticationRequest

    def setUseClientAuthenticationRequest(self, value):
        if value is not None:
            self.useClientAuthenticationRequest = value
        return self

    def getUseSecurityExtensionRecordSizeLimit(self):
        return self.useSecurityExtensionRecordSizeLimit

    def setUseSecurityExtensionRecordSizeLimit(self, value):
        if value is not None:
            self.useSecurityExtensionRecordSizeLimit = value
        return self
