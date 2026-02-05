# This module contains AUTOSAR System Template classes for secure communication
# It defines crypto service mappings and TLS configurations for secure data transmission

from typing import List
from abc import ABC
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import Boolean, RefType
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable import Identifiable


class CryptoServiceMapping(Identifiable, ABC):
    """
    Abstract base class for crypto service mappings, defining
    common properties for different types of cryptographic
    service mappings in the AUTOSAR system.
    """

    def __init__(self, parent, short_name):
        if type(self) is CryptoServiceMapping:
            raise TypeError("CryptoServiceMapping is an abstract class.")
        super().__init__(parent, short_name)


class SecOcCryptoServiceMapping(CryptoServiceMapping):
    """
    Represents a Secure Onboard Communication (SecOC) crypto service mapping,
    defining authentication, key, and queue references for secure
    communication between ECUs.
    """
    def __init__(self, parent, short_name):
        super().__init__(parent, short_name)

        self.authenticationRef: RefType = None
        self.cryptoServiceKeyRef: RefType = None
        self.cryptoServiceQueueRef: RefType = None

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
    def __init__(self, parent, short_name):
        super().__init__(parent, short_name)

        self.keyExchangeRef: RefType = None
        self.tlsCipherSuites: List = []
        self.useClientAuthenticationRequest: Boolean = None
        self.useSecurityExtensionRecordSizeLimit: Boolean = None

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