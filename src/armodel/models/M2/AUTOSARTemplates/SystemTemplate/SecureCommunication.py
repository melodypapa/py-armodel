# This module contains AUTOSAR System Template classes for secure communication
# It defines crypto service mappings and TLS configurations for secure data transmission

from typing import List
from ....M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import Boolean, RefType
from ....M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable import Identifiable


class CryptoServiceMapping(Identifiable):
    def __init__(self, parent, short_name):
        super().__init__(parent, short_name)


class SecOcCryptoServiceMapping(CryptoServiceMapping):
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