# This module contains AUTOSAR System Template classes for secure communication
# It defines crypto service mappings and TLS configurations for secure data transmission

from __future__ import annotations

from typing import List, Optional
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.StereotypeMixins import VariationPointCapable
from abc import ABC
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    AREnum,
    Boolean,
    MacAddressString,
    PositiveInteger,
    RefType,
    String,
    TimeValue,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable import Identifiable
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ARPackage import ARElement


class CryptoServiceMapping(Identifiable, VariationPointCapable, ABC):
    """
    This meta-class represents an abstract base class for specializations of crypto service mappings.
    """

    # CryptoServiceMapping method parity checklist:
    # Spec: AUTOSAR_CP_TPS_SystemTemplate.pdf, Table 6.48, p.375
    # Spec verified: R23-11
    # Columns: impl / docstring / test / reader / writer / release   ([—] = no XML element)
    # [x] __init__    [x] impl  [x] docstring  [x] test  [—] reader  [—] writer  R23-11

    def __init__(self, parent, short_name):
        if type(self) is CryptoServiceMapping:
            raise TypeError("CryptoServiceMapping is an abstract class.")
        super().__init__(parent, short_name)


class SecOcCryptoServiceMapping(CryptoServiceMapping):
    """
    This meta-class has the ability to represent a crypto service mapping for the Pdu-based communication via SecOC.
    """

    # SecOcCryptoServiceMapping method parity checklist:
    # Spec: AUTOSAR_CP_TPS_SystemTemplate.pdf, Table 6.49, p.375
    # Columns: impl / docstring / test / reader / writer / release   ([—] = no XML element)
    # [x] __init__                  [x] impl  [x] docstring  [x] test  [—] reader  [—] writer  R23-11
    # [x] getAuthenticationRef      [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setAuthenticationRef      [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getCryptoServiceKeyRef    [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setCryptoServiceKeyRef    [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getCryptoServiceQueueRef  [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setCryptoServiceQueueRef  [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11

    def __init__(self, parent, short_name):
        super().__init__(parent, short_name)

        # This reference identifies the applicable crypto primitive for the authentication.
        self.authenticationRef: Optional[RefType] = None

        # This reference identifies the applicable crypto key.
        self.cryptoServiceKeyRef: Optional[RefType] = None

        # This reference identifies the CryptoServiceQueue the processing of this SecOcCryptoServiceMapping shall be performed in.
        self.cryptoServiceQueueRef: Optional[RefType] = None

    def getAuthenticationRef(self) -> Optional[RefType]:
        """This reference identifies the applicable crypto primitive for the authentication."""
        return self.authenticationRef

    def setAuthenticationRef(self, value: Optional[RefType]) -> SecOcCryptoServiceMapping:
        """
        This reference identifies the applicable crypto primitive for the authentication.
        A None value is a no-op and does not overwrite an existing authenticationRef.
        """
        if value is not None:
            self.authenticationRef = value
        return self

    def getCryptoServiceKeyRef(self) -> Optional[RefType]:
        """This reference identifies the applicable crypto key."""
        return self.cryptoServiceKeyRef

    def setCryptoServiceKeyRef(self, value: Optional[RefType]) -> SecOcCryptoServiceMapping:
        """
        This reference identifies the applicable crypto key.
        A None value is a no-op and does not overwrite an existing cryptoServiceKeyRef.
        """
        if value is not None:
            self.cryptoServiceKeyRef = value
        return self

    def getCryptoServiceQueueRef(self) -> Optional[RefType]:
        """This reference identifies the CryptoServiceQueue the processing of this SecOcCryptoServiceMapping shall be performed in."""
        return self.cryptoServiceQueueRef

    def setCryptoServiceQueueRef(self, value: Optional[RefType]) -> SecOcCryptoServiceMapping:
        """
        This reference identifies the CryptoServiceQueue the processing of this SecOcCryptoServiceMapping shall be performed in.
        A None value is a no-op and does not overwrite an existing cryptoServiceQueueRef.
        """
        if value is not None:
            self.cryptoServiceQueueRef = value
        return self


class TlsCryptoServiceMapping(CryptoServiceMapping):
    """
    This meta-class has the ability to represent a crypto service mapping for the socket-based configuration of Transport Layer Security (TLS).
    """

    # TlsCryptoServiceMapping method parity checklist:
    # Spec: AUTOSAR_CP_TPS_SystemTemplate.pdf, Table 6.211, p.560
    # Spec verified: R23-11
    # Columns: impl / docstring / test / reader / writer / release   ([—] = no XML element)
    # [x] __init__    [x] impl  [x] docstring  [x] test  [—] reader  [—] writer  R23-11
    # [x] addKeyExchangeRef    [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getKeyExchangeRefs    [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] addTlsCipherSuite    [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getTlsCipherSuites    [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] getUseClientAuthenticationRequest    [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setUseClientAuthenticationRequest    [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getUseSecurityExtensionRecordSizeLimit    [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setUseSecurityExtensionRecordSizeLimit    [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11

    def __init__(self, parent, short_name):
        super().__init__(parent, short_name)

        # This reference identifies the shared(i.e. applicable for each of the aggregated cipher suites) crypto service primitive for the execution of key exchange during the handshake phase.
        self.keyExchangeRefs: List[RefType] = []

        # This aggregation represents the collection of supported cipher suites.
        self.tlsCipherSuites: List[TlsCryptoCipherSuite] = []

        # Defines if client authentication shall be applied for this TLS connection.
        self.useClientAuthenticationRequest: Optional[Boolean] = None

        # Defines if the security extension for max_fragment_length shall be supported as defined in IETF RFC 8449, chapter 4.1.
        self.useSecurityExtensionRecordSizeLimit: Optional[Boolean] = None

    def addKeyExchangeRef(self, ref: Optional[RefType]) -> TlsCryptoServiceMapping:
        """
        This reference identifies the shared(i.e. applicable for each of the aggregated cipher suites) crypto service primitive for the execution of key exchange during the handshake phase.
        A None value is a no-op and does not extend the keyExchangeRefs list.
        """
        if ref is not None:
            self.keyExchangeRefs.append(ref)
        return self

    def getKeyExchangeRefs(self) -> List[RefType]:
        """This reference identifies the shared(i.e. applicable for each of the aggregated cipher suites) crypto service primitive for the execution of key exchange during the handshake phase."""
        return self.keyExchangeRefs

    def addTlsCipherSuite(self, value: Optional[TlsCryptoCipherSuite]) -> TlsCryptoServiceMapping:
        """
        This aggregation represents the collection of supported cipher suites.
        A None value is a no-op and does not extend the tlsCipherSuites list.
        """
        if value is not None:
            self.tlsCipherSuites.append(value)
        return self

    def getTlsCipherSuites(self) -> List[TlsCryptoCipherSuite]:
        """This aggregation represents the collection of supported cipher suites."""
        return self.tlsCipherSuites

    def getUseClientAuthenticationRequest(self) -> Optional[Boolean]:
        """Defines if client authentication shall be applied for this TLS connection."""
        return self.useClientAuthenticationRequest

    def setUseClientAuthenticationRequest(self, value: Optional[Boolean]) -> TlsCryptoServiceMapping:
        """
        Defines if client authentication shall be applied for this TLS connection.
        A None value is a no-op and does not overwrite an existing useClientAuthenticationRequest.
        """
        if value is not None:
            self.useClientAuthenticationRequest = value
        return self

    def getUseSecurityExtensionRecordSizeLimit(self) -> Optional[Boolean]:
        """Defines if the security extension for max_fragment_length shall be supported as defined in IETF RFC 8449, chapter 4.1."""
        return self.useSecurityExtensionRecordSizeLimit

    def setUseSecurityExtensionRecordSizeLimit(self, value: Optional[Boolean]) -> TlsCryptoServiceMapping:
        """
        Defines if the security extension for max_fragment_length shall be supported as defined in IETF RFC 8449, chapter 4.1.
        A None value is a no-op and does not overwrite an existing useSecurityExtensionRecordSizeLimit.
        """
        if value is not None:
            self.useSecurityExtensionRecordSizeLimit = value
        return self


class TlsCryptoCipherSuite(Identifiable):
    """
    This meta-class represents a cipher suite for describing cryptographic operations in the context of establishing a connection of ApplicationEndpoints that is protected by TLS.
    """

    # TlsCryptoCipherSuite method parity checklist:
    # Spec: AUTOSAR_CP_TPS_SystemTemplate.pdf, Table 6.212, p.562
    # Spec verified: R23-11
    # Columns: impl / docstring / test / reader / writer / release   ([—] = no XML element)
    # [x] __init__                                [x] impl  [x] docstring  [x] test  [—] reader  [—] writer  R23-11
    # [x] getAuthenticationRef                    [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setAuthenticationRef                    [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getCertificateRef                       [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setCertificateRef                       [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getCipherSuiteId                        [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setCipherSuiteId                        [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getCipherSuiteShortLabel                [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setCipherSuiteShortLabel                [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] addEllipticCurveRef                     [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getEllipticCurveRefs                    [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] getEncryptionRef                        [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setEncryptionRef                        [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] addKeyExchangeRef                       [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getKeyExchangeRefs                      [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] addKeyExchangeAuthenticationRef         [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getKeyExchangeAuthenticationRefs        [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] getPriority                             [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setPriority                             [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getProps                                [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setProps                                [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getPskIdentity                          [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setPskIdentity                          [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getRemoteCertificateRef                 [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setRemoteCertificateRef                 [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] addSignatureSchemeRef                   [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getSignatureSchemeRefs                  [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] getVersion                              [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setVersion                              [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11

    def __init__(self, parent, short_name):
        super().__init__(parent, short_name)

        # This reference identifies the crypto service primitive for the generation and verification of MACs.
        self.authenticationRef: Optional[RefType] = None

        # This reference identifies the applicable local certificate.
        self.certificateRef: Optional[RefType] = None

        # Identification of the CipherSuite according to the IANA assignments list.
        self.cipherSuiteId: Optional[PositiveInteger] = None

        # Name of the CipherSuite according to the IANA assignments list.
        self.cipherSuiteShortLabel: Optional[String] = None

        # This references point to the properties of elliptic curves.
        self.ellipticCurveRefs: List[RefType] = []

        # This reference identifies the crypto service primitive for the execution of encryption.
        self.encryptionRef: Optional[RefType] = None

        # This reference identifies the individual (i.e. per cipher suite) crypto service primitive for the execution of key exchange during the handshake phase.
        self.keyExchangeRefs: List[RefType] = []

        # This reference identifies the crypto service primitives for the generation and verification of signatures during the key exchange algorithm.
        self.keyExchangeAuthenticationRefs: List[RefType] = []

        # This attribute identifies the priority of the cipher suite. Range: 1..65535. Lower values represent higher priorities.
        self.priority: Optional[PositiveInteger] = None

        # The aggregated TlsCryptoCipherSuiteProps provide details for the TLS Cipher Suite.
        self.props: Optional[TlsCryptoCipherSuiteProps] = None

        # Pre-shared key identity shared during the handshake among the communication parties, to establish a TLS connection if the handshake is based on the existence of a pre-shared key.
        self.pskIdentity: Optional[TlsPskIdentity] = None

        # This reference identifies the applicable remote certificate.
        self.remoteCertificateRef: Optional[RefType] = None

        # This reference points to the properties of a TLS Signature Scheme.
        self.signatureSchemeRefs: List[RefType] = []

        # This attribute supports the definition of the applicable version of TLS.
        self.version: Optional[TlsVersionEnum] = None

    def getAuthenticationRef(self) -> Optional[RefType]:
        """This reference identifies the crypto service primitive for the generation and verification of MACs."""
        return self.authenticationRef

    def setAuthenticationRef(self, value: Optional[RefType]) -> TlsCryptoCipherSuite:
        """
        This reference identifies the crypto service primitive for the generation and verification of MACs.
        A None value is a no-op and does not overwrite an existing authenticationRef.
        """
        if value is not None:
            self.authenticationRef = value
        return self

    def getCertificateRef(self) -> Optional[RefType]:
        """This reference identifies the applicable local certificate."""
        return self.certificateRef

    def setCertificateRef(self, value: Optional[RefType]) -> TlsCryptoCipherSuite:
        """
        This reference identifies the applicable local certificate.
        A None value is a no-op and does not overwrite an existing certificateRef.
        """
        if value is not None:
            self.certificateRef = value
        return self

    def getCipherSuiteId(self) -> Optional[PositiveInteger]:
        """Identification of the CipherSuite according to the IANA assignments list."""
        return self.cipherSuiteId

    def setCipherSuiteId(self, value: Optional[PositiveInteger]) -> TlsCryptoCipherSuite:
        """
        Identification of the CipherSuite according to the IANA assignments list.
        A None value is a no-op and does not overwrite an existing cipherSuiteId.
        """
        if value is not None:
            self.cipherSuiteId = value
        return self

    def getCipherSuiteShortLabel(self) -> Optional[String]:
        """Name of the CipherSuite according to the IANA assignments list."""
        return self.cipherSuiteShortLabel

    def setCipherSuiteShortLabel(self, value: Optional[String]) -> TlsCryptoCipherSuite:
        """
        Name of the CipherSuite according to the IANA assignments list.
        A None value is a no-op and does not overwrite an existing cipherSuiteShortLabel.
        """
        if value is not None:
            self.cipherSuiteShortLabel = value
        return self

    def addEllipticCurveRef(self, ref: Optional[RefType]) -> TlsCryptoCipherSuite:
        """
        This references point to the properties of elliptic curves.
        A None value is a no-op and does not extend the ellipticCurveRefs list.
        """
        if ref is not None:
            self.ellipticCurveRefs.append(ref)
        return self

    def getEllipticCurveRefs(self) -> List[RefType]:
        """This references point to the properties of elliptic curves."""
        return self.ellipticCurveRefs

    def getEncryptionRef(self) -> Optional[RefType]:
        """This reference identifies the crypto service primitive for the execution of encryption."""
        return self.encryptionRef

    def setEncryptionRef(self, value: Optional[RefType]) -> TlsCryptoCipherSuite:
        """
        This reference identifies the crypto service primitive for the execution of encryption.
        A None value is a no-op and does not overwrite an existing encryptionRef.
        """
        if value is not None:
            self.encryptionRef = value
        return self

    def addKeyExchangeRef(self, ref: Optional[RefType]) -> TlsCryptoCipherSuite:
        """
        This reference identifies the individual (i.e. per cipher suite) crypto service primitive for the execution of key exchange during the handshake phase.
        A None value is a no-op and does not extend the keyExchangeRefs list.
        """
        if ref is not None:
            self.keyExchangeRefs.append(ref)
        return self

    def getKeyExchangeRefs(self) -> List[RefType]:
        """This reference identifies the individual (i.e. per cipher suite) crypto service primitive for the execution of key exchange during the handshake phase."""
        return self.keyExchangeRefs

    def addKeyExchangeAuthenticationRef(self, ref: Optional[RefType]) -> TlsCryptoCipherSuite:
        """
        This reference identifies the crypto service primitives for the generation and verification of signatures during the key exchange algorithm.
        A None value is a no-op and does not extend the keyExchangeAuthenticationRefs list.
        """
        if ref is not None:
            self.keyExchangeAuthenticationRefs.append(ref)
        return self

    def getKeyExchangeAuthenticationRefs(self) -> List[RefType]:
        """This reference identifies the crypto service primitives for the generation and verification of signatures during the key exchange algorithm."""
        return self.keyExchangeAuthenticationRefs

    def getPriority(self) -> Optional[PositiveInteger]:
        """This attribute identifies the priority of the cipher suite. Range: 1..65535. Lower values represent higher priorities."""
        return self.priority

    def setPriority(self, value: Optional[PositiveInteger]) -> TlsCryptoCipherSuite:
        """
        This attribute identifies the priority of the cipher suite. Range: 1..65535. Lower values represent higher priorities.
        A None value is a no-op and does not overwrite an existing priority.
        """
        if value is not None:
            self.priority = value
        return self

    def getProps(self) -> Optional[TlsCryptoCipherSuiteProps]:
        """The aggregated TlsCryptoCipherSuiteProps provide details for the TLS Cipher Suite."""
        return self.props

    def setProps(self, value: Optional[TlsCryptoCipherSuiteProps]) -> TlsCryptoCipherSuite:
        """
        The aggregated TlsCryptoCipherSuiteProps provide details for the TLS Cipher Suite.
        A None value is a no-op and does not overwrite an existing props.
        """
        if value is not None:
            self.props = value
        return self

    def getPskIdentity(self) -> Optional[TlsPskIdentity]:
        """Pre-shared key identity shared during the handshake among the communication parties, to establish a TLS connection if the handshake is based on the existence of a pre-shared key."""
        return self.pskIdentity

    def setPskIdentity(self, value: Optional[TlsPskIdentity]) -> TlsCryptoCipherSuite:
        """
        Pre-shared key identity shared during the handshake among the communication parties, to establish a TLS connection if the handshake is based on the existence of a pre-shared key.
        A None value is a no-op and does not overwrite an existing pskIdentity.
        """
        if value is not None:
            self.pskIdentity = value
        return self

    def getRemoteCertificateRef(self) -> Optional[RefType]:
        """This reference identifies the applicable remote certificate."""
        return self.remoteCertificateRef

    def setRemoteCertificateRef(self, value: Optional[RefType]) -> TlsCryptoCipherSuite:
        """
        This reference identifies the applicable remote certificate.
        A None value is a no-op and does not overwrite an existing remoteCertificateRef.
        """
        if value is not None:
            self.remoteCertificateRef = value
        return self

    def addSignatureSchemeRef(self, ref: Optional[RefType]) -> TlsCryptoCipherSuite:
        """
        This reference points to the properties of a TLS Signature Scheme.
        A None value is a no-op and does not extend the signatureSchemeRefs list.
        """
        if ref is not None:
            self.signatureSchemeRefs.append(ref)
        return self

    def getSignatureSchemeRefs(self) -> List[RefType]:
        """This reference points to the properties of a TLS Signature Scheme."""
        return self.signatureSchemeRefs

    def getVersion(self) -> Optional[TlsVersionEnum]:
        """This attribute supports the definition of the applicable version of TLS."""
        return self.version

    def setVersion(self, value: Optional[TlsVersionEnum]) -> TlsCryptoCipherSuite:
        """
        This attribute supports the definition of the applicable version of TLS.
        A None value is a no-op and does not overwrite an existing version.
        """
        if value is not None:
            self.version = value
        return self


class TlsVersionEnum(AREnum):
    """
    This meta-class has the ability to identify a specific version of the transport-layer security (TLS) protocol.
    """

    # TlsVersionEnum method parity checklist:
    # Spec: AUTOSAR_CP_TPS_SystemTemplate.pdf, Table 6.213, p.563
    # Spec verified: R23-11
    # Columns: impl / docstring / test / reader / writer   ([—] = no XML element)
    # (no methods) — enum value form serialized on TlsCryptoCipherSuite.version

    # TLS version 1.2 Tags: atp.EnumerationLiteralIndex=0 xml.name=TLS-12
    TLS_12 = "TLS-12"

    # TLS version 1.3 Tags: atp.EnumerationLiteralIndex=2 xml.name=TLS-13
    TLS_13 = "TLS-13"

    def __init__(self):
        super().__init__(
            [
                TlsVersionEnum.TLS_12,
                TlsVersionEnum.TLS_13,
            ]
        )


class TlsPskIdentity(ARObject):
    """
    This element is used to describe the pre-shared key shared during the handshake among the communication parties, to establish a TLS connection if the handshake is based on the existence of a pre-shared key.
    """

    # TlsPskIdentity method parity checklist:
    # Spec: AUTOSAR_CP_TPS_SystemTemplate.pdf, Table 6.214, p.563
    # Spec verified: R23-11
    # Columns: impl / docstring / test / reader / writer   ([—] = no XML element)
    # [x] __init__            [x] impl  [—] docstring  [x] test  [—] reader  [—] writer  R23-11
    # [x] setPreSharedKeyRef  [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getPreSharedKeyRef  [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setPskIdentity      [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getPskIdentity      [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setPskIdentityHint  [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getPskIdentityHint  [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11

    def __init__(self):
        super().__init__()

        # This reference identifies the applicable cryptographic key.
        self.preSharedKeyRef: Optional[RefType] = None

        # This attribute provides the key identification.
        self.pskIdentity: Optional[String] = None

        # This attribute provides the identity hint for a pre-shared key.
        self.pskIdentityHint: Optional[String] = None

    def setPreSharedKeyRef(self, value: Optional[RefType]) -> TlsPskIdentity:
        """
        This reference identifies the applicable cryptographic key.
        A None value is a no-op and does not overwrite an existing preSharedKeyRef.
        """
        if value is not None:
            self.preSharedKeyRef = value
        return self

    def getPreSharedKeyRef(self) -> Optional[RefType]:
        """This reference identifies the applicable cryptographic key."""
        return self.preSharedKeyRef

    def setPskIdentity(self, value: Optional[String]) -> TlsPskIdentity:
        """
        This attribute provides the key identification.
        A None value is a no-op and does not overwrite an existing pskIdentity.
        """
        if value is not None:
            self.pskIdentity = value
        return self

    def getPskIdentity(self) -> Optional[String]:
        """This attribute provides the key identification."""
        return self.pskIdentity

    def setPskIdentityHint(self, value: Optional[String]) -> TlsPskIdentity:
        """
        This attribute provides the identity hint for a pre-shared key.
        A None value is a no-op and does not overwrite an existing pskIdentityHint.
        """
        if value is not None:
            self.pskIdentityHint = value
        return self

    def getPskIdentityHint(self) -> Optional[String]:
        """This attribute provides the identity hint for a pre-shared key."""
        return self.pskIdentityHint


class TlsCryptoCipherSuiteProps(Identifiable):
    """
    This meta-class provides attributes to specify details of TLS Cipher Suites.
    """

    # TlsCryptoCipherSuiteProps method parity checklist:
    # Spec: AUTOSAR_CP_TPS_SystemTemplate.pdf, Table 6.215, p.563
    # Spec verified: R23-11
    # Columns: impl / docstring / test / reader / writer / release   ([—] = no XML element)
    # [x] __init__                                            [x] impl  [x] docstring  [x] test  [—] reader  [—] writer  R23-11
    # [x] getTcpIpTlsUseSecurityExtensionForceEncryptThenMac  [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setTcpIpTlsUseSecurityExtensionForceEncryptThenMac  [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11

    def __init__(self, parent, short_name):
        super().__init__(parent, short_name)

        # Defines if the security extension according to IETF RFC 7366 shall be supported. This is useful for cipher suites using CBC mode.
        self.tcpIpTlsUseSecurityExtensionForceEncryptThenMac: Optional[Boolean] = None

    def getTcpIpTlsUseSecurityExtensionForceEncryptThenMac(self) -> Optional[Boolean]:
        """Defines if the security extension according to IETF RFC 7366 shall be supported. This is useful for cipher suites using CBC mode."""
        return self.tcpIpTlsUseSecurityExtensionForceEncryptThenMac

    def setTcpIpTlsUseSecurityExtensionForceEncryptThenMac(self, value: Optional[Boolean]) -> TlsCryptoCipherSuiteProps:
        """
        Defines if the security extension according to IETF RFC 7366 shall be supported. This is useful for cipher suites using CBC mode.
        A None value is a no-op and does not overwrite an existing tcpIpTlsUseSecurityExtensionForceEncryptThenMac.
        """
        if value is not None:
            self.tcpIpTlsUseSecurityExtensionForceEncryptThenMac = value
        return self


class CryptoServicePrimitive(ARElement):
    """
    This meta-class has the ability to represent a crypto primitive. Tags: atp.recommendedPackage=CryptoPrimitives
    """

    # CryptoServicePrimitive method parity checklist:
    # Spec: AUTOSAR_CP_TPS_SystemTemplate.pdf, Table 6.50, p.376
    # Spec verified: R23-11
    # Columns: impl / docstring / test / reader / writer / release   ([—] = no XML element)
    # [x] __init__                     [x] impl  [x] docstring  [x] test  [—] reader  [—] writer  R23-11
    # [x] getAlgorithmFamily           [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setAlgorithmFamily           [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getAlgorithmMode             [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setAlgorithmMode             [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getAlgorithmSecondaryFamily  [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setAlgorithmSecondaryFamily  [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11

    def __init__(self, parent, short_name):
        super().__init__(parent, short_name)

        # This attribute represents a description of the family (e.g. AES) of crypto algorithm implemented by the crypto primitive.
        self.algorithmFamily: Optional[String] = None

        # This attribute represents a description of the mode of the crypto algorithm implemented by the crypto primitive.
        self.algorithmMode: Optional[String] = None

        # This attribute represents a further description of the secondary family of crypto algorithm implemented by the crypto primitive. The secondary family is needed for the specification of the hash algorithm for a signature check, e.g. using RSA.
        self.algorithmSecondaryFamily: Optional[String] = None

    def getAlgorithmFamily(self) -> Optional[String]:
        """This attribute represents a description of the family (e.g. AES) of crypto algorithm implemented by the crypto primitive."""
        return self.algorithmFamily

    def setAlgorithmFamily(self, value: Optional[String]) -> CryptoServicePrimitive:
        """
        This attribute represents a description of the family (e.g. AES) of crypto algorithm implemented by the crypto primitive.
        A None value is a no-op and does not overwrite an existing algorithmFamily.
        """
        if value is not None:
            self.algorithmFamily = value
        return self

    def getAlgorithmMode(self) -> Optional[String]:
        """This attribute represents a description of the mode of the crypto algorithm implemented by the crypto primitive."""
        return self.algorithmMode

    def setAlgorithmMode(self, value: Optional[String]) -> CryptoServicePrimitive:
        """
        This attribute represents a description of the mode of the crypto algorithm implemented by the crypto primitive.
        A None value is a no-op and does not overwrite an existing algorithmMode.
        """
        if value is not None:
            self.algorithmMode = value
        return self

    def getAlgorithmSecondaryFamily(self) -> Optional[String]:
        """This attribute represents a further description of the secondary family of crypto algorithm implemented by the crypto primitive. The secondary family is needed for the specification of the hash algorithm for a signature check, e.g. using RSA."""
        return self.algorithmSecondaryFamily

    def setAlgorithmSecondaryFamily(self, value: Optional[String]) -> CryptoServicePrimitive:
        """
        This attribute represents a further description of the secondary family of crypto algorithm implemented by the crypto primitive. The secondary family is needed for the specification of the hash algorithm for a signature check, e.g. using RSA.
        A None value is a no-op and does not overwrite an existing algorithmSecondaryFamily.
        """
        if value is not None:
            self.algorithmSecondaryFamily = value
        return self


class CryptoEllipticCurveProps(ARElement):
    """
    This meta-class provides attributes to specify the properties of elliptic curves. Tags: atp.recommendedPackage=CryptoEllipticCurveProps
    """

    # CryptoEllipticCurveProps method parity checklist:
    # Spec: AUTOSAR_CP_TPS_SystemTemplate.pdf, Table 6.216, p.564
    # Spec verified: R23-11
    # Columns: impl / docstring / test / reader / writer / release   ([—] = no XML element)
    # [x] __init__           [x] impl  [x] docstring  [x] test  [—] reader  [—] writer  R23-11
    # [x] getNamedCurveId    [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setNamedCurveId    [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11

    def __init__(self, parent, short_name):
        super().__init__(parent, short_name)

        # Defines the value of one specific NamedCurve Id.
        self.namedCurveId: Optional[PositiveInteger] = None

    def getNamedCurveId(self) -> Optional[PositiveInteger]:
        """Defines the value of one specific NamedCurve Id."""
        return self.namedCurveId

    def setNamedCurveId(self, value: Optional[PositiveInteger]) -> CryptoEllipticCurveProps:
        """
        Defines the value of one specific NamedCurve Id.
        A None value is a no-op and does not overwrite an existing namedCurveId.
        """
        if value is not None:
            self.namedCurveId = value
        return self


class CryptoSignatureScheme(ARElement):
    """
    This meta-class provides attributes to specify the TLS Signature Scheme. Tags: atp.recommendedPackage=CryptoSignatureSchemas
    """

    # CryptoSignatureScheme method parity checklist:
    # Spec: AUTOSAR_CP_TPS_SystemTemplate.pdf, Table 6.217, p.564
    # Spec verified: R23-11
    # Columns: impl / docstring / test / reader / writer / release   ([—] = no XML element)
    # [x] __init__                  [x] impl  [x] docstring  [x] test  [—] reader  [—] writer  R23-11
    # [x] getSignatureSchemeId      [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setSignatureSchemeId      [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11

    def __init__(self, parent, short_name):
        super().__init__(parent, short_name)

        # Defines the value of one specific TLS Signature Scheme.
        self.signatureSchemeId: Optional[PositiveInteger] = None

    def getSignatureSchemeId(self) -> Optional[PositiveInteger]:
        """Defines the value of one specific TLS Signature Scheme."""
        return self.signatureSchemeId

    def setSignatureSchemeId(self, value: Optional[PositiveInteger]) -> CryptoSignatureScheme:
        """
        Defines the value of one specific TLS Signature Scheme.
        A None value is a no-op and does not overwrite an existing signatureSchemeId.
        """
        if value is not None:
            self.signatureSchemeId = value
        return self


class CryptoServiceCertificate(ARElement):
    """
    This meta-class represents the ability to model a cryptographic certificate. Tags: atp.recommendedPackage=CryptoServiceCertificates
    """

    # CryptoServiceCertificate method parity checklist:
    # Spec: AUTOSAR_CP_TPS_SystemTemplate.pdf, Table 6.218, p.565
    # Spec verified: R23-11
    # Columns: impl / docstring / test / reader / writer / release   ([—] = no XML element)
    # [x] __init__                              [x] impl  [x] docstring  [x] test  [—] reader  [—] writer  R23-11
    # [x] getAlgorithmFamily                    [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setAlgorithmFamily                    [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getFormat                             [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setFormat                             [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getMaximumLength                      [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setMaximumLength                      [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getNextHigherCertificateRef           [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setNextHigherCertificateRef           [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getServerNameIdentification           [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setServerNameIdentification           [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11

    def __init__(self, parent, short_name):
        super().__init__(parent, short_name)

        # This attribute represents a description of the family of crypto algorithm used to generate public key and signature of the cryptographic certificate.
        self.algorithmFamily: Optional[CryptoCertificateAlgorithmFamilyEnum] = None

        # This attribute can be used to provide information about the format used to create the certificate
        self.format: Optional[CryptoCertificateFormatEnum] = None

        # This attribute represents the ability to define the maximum length of the certificate in bytes.
        self.maximumLength: Optional[PositiveInteger] = None

        # The reference identifies the next higher certificate in the certificate chain.
        self.nextHigherCertificateRef: Optional[RefType] = None

        # Server Name Indication (SNI) is needed if the IP address hosts multiple servers (on the same port), each of them using a different certificate. If the client sends the SNI to the Server in the client hello, the server looks the SNI up in its certificate list and uses the certificate identified by the SNI.
        self.serverNameIdentification: Optional[String] = None

    def getAlgorithmFamily(self) -> Optional[CryptoCertificateAlgorithmFamilyEnum]:
        """This attribute represents a description of the family of crypto algorithm used to generate public key and signature of the cryptographic certificate."""
        return self.algorithmFamily

    def setAlgorithmFamily(self, value: Optional[CryptoCertificateAlgorithmFamilyEnum]) -> CryptoServiceCertificate:
        """
        This attribute represents a description of the family of crypto algorithm used to generate public key and signature of the cryptographic certificate.
        A None value is a no-op and does not overwrite an existing algorithmFamily.
        """
        if value is not None:
            self.algorithmFamily = value
        return self

    def getFormat(self) -> Optional[CryptoCertificateFormatEnum]:
        """This attribute can be used to provide information about the format used to create the certificate"""
        return self.format

    def setFormat(self, value: Optional[CryptoCertificateFormatEnum]) -> CryptoServiceCertificate:
        """
        This attribute can be used to provide information about the format used to create the certificate
        A None value is a no-op and does not overwrite an existing format.
        """
        if value is not None:
            self.format = value
        return self

    def getMaximumLength(self) -> Optional[PositiveInteger]:
        """This attribute represents the ability to define the maximum length of the certificate in bytes."""
        return self.maximumLength

    def setMaximumLength(self, value: Optional[PositiveInteger]) -> CryptoServiceCertificate:
        """
        This attribute represents the ability to define the maximum length of the certificate in bytes.
        A None value is a no-op and does not overwrite an existing maximumLength.
        """
        if value is not None:
            self.maximumLength = value
        return self

    def getNextHigherCertificateRef(self) -> Optional[RefType]:
        """The reference identifies the next higher certificate in the certificate chain."""
        return self.nextHigherCertificateRef

    def setNextHigherCertificateRef(self, value: Optional[RefType]) -> CryptoServiceCertificate:
        """
        The reference identifies the next higher certificate in the certificate chain.
        A None value is a no-op and does not overwrite an existing nextHigherCertificateRef.
        """
        if value is not None:
            self.nextHigherCertificateRef = value
        return self

    def getServerNameIdentification(self) -> Optional[String]:
        """Server Name Indication (SNI) is needed if the IP address hosts multiple servers (on the same port), each of them using a different certificate. If the client sends the SNI to the Server in the client hello, the server looks the SNI up in its certificate list and uses the certificate identified by the SNI."""
        return self.serverNameIdentification

    def setServerNameIdentification(self, value: Optional[String]) -> CryptoServiceCertificate:
        """
        Server Name Indication (SNI) is needed if the IP address hosts multiple servers (on the same port), each of them using a different certificate. If the client sends the SNI to the Server in the client hello, the server looks the SNI up in its certificate list and uses the certificate identified by the SNI.
        A None value is a no-op and does not overwrite an existing serverNameIdentification.
        """
        if value is not None:
            self.serverNameIdentification = value
        return self


class CryptoCertificateAlgorithmFamilyEnum(AREnum):
    """
    This meta-class defies possible cryptographic algorithm families used to create public keys and signatures within the certificate.
    """

    # CryptoCertificateAlgorithmFamilyEnum method parity checklist:
    # Spec: AUTOSAR_CP_TPS_SystemTemplate.pdf, Table 6.219, p.565
    # Spec verified: R23-11
    # Columns: impl / docstring / test / reader / writer   ([—] = no XML element)
    # (no methods) — enum value form serialized on CryptoServiceCertificate.algorithmFamily

    # The cryptographic operations in the certificate are executed using elliptic curves (ecc) Tags: atp.EnumerationLiteralIndex=2 xml.name=ECC
    ECC = "ECC"

    # The cryptographic operations in the certificate are executed using the RSA approach. Tags: atp.EnumerationLiteralIndex=1 xml.name=RSA
    RSA = "RSA"

    def __init__(self):
        super().__init__(
            [
                CryptoCertificateAlgorithmFamilyEnum.ECC,
                CryptoCertificateAlgorithmFamilyEnum.RSA,
            ]
        )


class CryptoCertificateFormatEnum(AREnum):
    """
    This meta-class defines possible formats of cryptographic certificates.
    """

    # CryptoCertificateFormatEnum method parity checklist:
    # Spec: AUTOSAR_CP_TPS_SystemTemplate.pdf, Table 6.220, p.565
    # Spec verified: R23-11
    # Columns: impl / docstring / test / reader / writer   ([—] = no XML element)
    # (no methods) — enum value form serialized on CryptoServiceCertificate.format

    # The certificate has been created in Card Verifiable Certificate (CVC) format Tags: atp.EnumerationLiteralIndex=2 xml.name=CVC
    CVC = "CVC"

    # The certificate is created in X.509 format. Tags: atp.EnumerationLiteralIndex=1 xml.name=X-509
    X_509 = "X-509"

    def __init__(self):
        super().__init__(
            [
                CryptoCertificateFormatEnum.CVC,
                CryptoCertificateFormatEnum.X_509,
            ]
        )


class MacSecConfidentialityOffsetEnum(AREnum):
    """
    This enum defines the MACsec capability options.
    """

    # MacSecConfidentialityOffsetEnum method parity checklist:
    # Spec: AUTOSAR_CP_TPS_SystemTemplate.pdf, Table 3.125, p.177
    # Spec verified: R23-11
    # Columns: impl / docstring / test / reader / writer   ([—] = no XML element)
    # (no methods) — enum value form serialized on MacSecCryptoAlgoConfig.confidentialityOffset

    # confidentiality offset of 0. Tags: atp.EnumerationLiteralIndex=0 xml.name=CONFIDENTIALITY-OFFSET-0
    CONFIDENTIALITY_OFFSET_0 = "CONFIDENTIALITY-OFFSET-0"

    # confidentiality offset of 30. Tags: atp.EnumerationLiteralIndex=1 xml.name=CONFIDENTIALITY-OFFSET-30
    CONFIDENTIALITY_OFFSET_30 = "CONFIDENTIALITY-OFFSET-30"

    # confidentiality offset of 50. Tags: atp.EnumerationLiteralIndex=2 xml.name=CONFIDENTIALITY-OFFSET-50
    CONFIDENTIALITY_OFFSET_50 = "CONFIDENTIALITY-OFFSET-50"

    def __init__(self):
        super().__init__(
            [
                MacSecConfidentialityOffsetEnum.CONFIDENTIALITY_OFFSET_0,
                MacSecConfidentialityOffsetEnum.CONFIDENTIALITY_OFFSET_30,
                MacSecConfidentialityOffsetEnum.CONFIDENTIALITY_OFFSET_50,
            ]
        )


class MacSecCapabilityEnum(AREnum):
    """
    This enum defines the MACsec capability options.
    """

    # MacSecCapabilityEnum method parity checklist:
    # Spec: AUTOSAR_CP_TPS_SystemTemplate.pdf, Table 3.126, p.177
    # Spec verified: R23-11
    # Columns: impl / docstring / test / reader / writer   ([—] = no XML element)
    # (no methods) — enum value form serialized on MacSecCryptoAlgoConfig.capability

    # Option that ensures integrity without confidentiality Tags: atp.EnumerationLiteralIndex=0
    INTERGRITY_WITHOUT_CONFIDENTIALITY = "intergrityWithoutConfidentiality"

    # Option that ensures confidentiality and integrity Tags: atp.EnumerationLiteralIndex=1
    INTERGRITY_AND_CONFIDENTIALITY = "intergrityAndConfidentiality"

    def __init__(self):
        super().__init__(
            [
                MacSecCapabilityEnum.INTERGRITY_WITHOUT_CONFIDENTIALITY,
                MacSecCapabilityEnum.INTERGRITY_AND_CONFIDENTIALITY,
            ]
        )


class MacSecRoleEnum(AREnum):
    """
    This enum defines the MACsec Role options.
    """

    # MacSecRoleEnum method parity checklist:
    # Spec: AUTOSAR_CP_TPS_SystemTemplate.pdf, Table 3.127, p.177
    # Spec verified: R23-11
    # Columns: impl / docstring / test / reader / writer   ([—] = no XML element)
    # (no methods) — enum value form serialized on MacSecLocalKayProps.role

    # Port acts in the peer role Tags: atp.EnumerationLiteralIndex=0
    PEER = "peer"

    # Port acts in the KeyServer role Tags: atp.EnumerationLiteralIndex=1
    KEY_SERVER = "keyServer"

    def __init__(self):
        super().__init__(
            [
                MacSecRoleEnum.PEER,
                MacSecRoleEnum.KEY_SERVER,
            ]
        )


class MacSecFailPermissiveModeEnum(AREnum):
    """
    Behavior options of the Port Access Entity in case MACsec does not succeed.
    """

    # MacSecFailPermissiveModeEnum method parity checklist:
    # Spec: AUTOSAR_CP_TPS_SystemTemplate.pdf, Table 3.128, p.178
    # Spec verified: R23-11
    # Columns: impl / docstring / test / reader / writer   ([—] = no XML element)
    # (no methods) — enum value form serialized on MacSecProps.onFailPermissiveMode

    # The controlled port will never be set to enabled if the participants cannot establish and successfully use a MACsec Secure Channel. Tags: atp.EnumerationLiteralIndex=0
    NEVER = "never"

    # The controlled port will be set to enabled and MACsec will not be used in the port if the timeout value (onFailPermissiveModeTimeout) is reached and the following conditions apply: - A participant belonging to the same CA was recognized and authenticated. - A secure channel could be established. - Both participants can transmit and receive MACsec protected traffic through the SC. Tags: atp.EnumerationLiteralIndex=1
    TIMEOUT = "timeout"

    def __init__(self):
        super().__init__(
            [
                MacSecFailPermissiveModeEnum.NEVER,
                MacSecFailPermissiveModeEnum.TIMEOUT,
            ]
        )


class IPsecIpProtocolEnum(AREnum):
    """
    Definition of supported TcpIp protocols that are supported in Security Policy Database (SPD) entries in IPSec configurations.
    """

    # IPsecIpProtocolEnum method parity checklist:
    # Spec: AUTOSAR_CP_TPS_SystemTemplate.pdf, Table 6.224, p.574
    # Columns: impl / docstring / test / reader / writer / release   ([—] = no XML element)
    # (no methods) — serialized as value form on IPSecRule/IPSecConfigProps members
    # [x] __init__     [x] impl  [x] docstring  [x] test  [—] reader  [—] writer  R23-11

    # ANY protocol Tags: atp.EnumerationLiteralIndex=3
    ANY = "any"

    # Internet Control Message Protocol (ICMP) Tags: atp.EnumerationLiteralIndex=2
    ICMP = "icmp"

    # TCP Protocol Tags: atp.EnumerationLiteralIndex=1
    TCP = "tcp"

    # UDP Protocol Tags: atp.EnumerationLiteralIndex=0
    UDP = "udp"

    def __init__(self):
        super().__init__(
            [
                IPsecIpProtocolEnum.ANY,
                IPsecIpProtocolEnum.ICMP,
                IPsecIpProtocolEnum.TCP,
                IPsecIpProtocolEnum.UDP,
            ]
        )


class IPsecPolicyEnum(AREnum):
    """
    Defines the filter actions that are supported by IPsec.
    """

    # IPsecPolicyEnum method parity checklist:
    # Spec: AUTOSAR_CP_TPS_SystemTemplate.pdf, Table 6.225, p.574
    # Columns: impl / docstring / test / reader / writer / release   ([—] = no XML element)
    # (no methods) — serialized as value form on IPSecRule/IPSecConfigProps members
    # [x] __init__     [x] impl  [x] docstring  [x] test  [—] reader  [—] writer  R23-11

    # Signifying that packets should be discarded Tags: atp.EnumerationLiteralIndex=3
    DROP = "drop"

    # Signifying that packets should be protected. Tags: atp.EnumerationLiteralIndex=1
    IPSEC = "ipsec"

    # Signifying that no IPsec processing should be done at all. Tags: atp.EnumerationLiteralIndex=2
    PASSTHROUGH = "passthrough"

    # Signifying that packets should be discarded and a diagnostic ICMP returned. Tags: atp.EnumerationLiteralIndex=4
    REJECT = "reject"

    def __init__(self):
        super().__init__(
            [
                IPsecPolicyEnum.DROP,
                IPsecPolicyEnum.IPSEC,
                IPsecPolicyEnum.PASSTHROUGH,
                IPsecPolicyEnum.REJECT,
            ]
        )


class IPsecModeEnum(AREnum):
    """
    This enumeration describes the supported IPSec modes.
    """

    # IPsecModeEnum method parity checklist:
    # Spec: AUTOSAR_CP_TPS_SystemTemplate.pdf, Table 6.226, p.575
    # Columns: impl / docstring / test / reader / writer / release   ([—] = no XML element)
    # (no methods) — serialized as value form on IPSecRule/IPSecConfigProps members
    # [x] __init__     [x] impl  [x] docstring  [x] test  [—] reader  [—] writer  R23-11

    # Signifying that the IPSec transport mode is used. With the transport mode the original IP header is retained and only the IP payload and ESP trailer is encrypted. Tags: atp.EnumerationLiteralIndex=1
    TRANSPORT = "transport"

    # Signifying that the IPSec tunnel mode is used. With tunnel mode, the entire original IP packet is protected by IPSec. This means IPSec wraps the original packet, encrypts it, adds a new IP header and sends it to the other side. Tags: atp.EnumerationLiteralIndex=0
    TUNNEL = "tunnel"

    def __init__(self):
        super().__init__(
            [
                IPsecModeEnum.TRANSPORT,
                IPsecModeEnum.TUNNEL,
            ]
        )


class IPsecHeaderTypeEnum(AREnum):
    """
    IPsec Header Type options
    """

    # IPsecHeaderTypeEnum method parity checklist:
    # Spec: AUTOSAR_CP_TPS_SystemTemplate.pdf, Table 6.227, p.576
    # Columns: impl / docstring / test / reader / writer / release   ([—] = no XML element)
    # (no methods) — serialized as value form on IPSecRule/IPSecConfigProps members
    # [x] __init__     [x] impl  [x] docstring  [x] test  [—] reader  [—] writer  R23-11

    # Authentication Header (AH) Tags: atp.EnumerationLiteralIndex=0
    AH = "ah"

    # Encapsulating Security Payloads (ESP) Tags: atp.EnumerationLiteralIndex=1
    ESP = "esp"

    # No header Tags: atp.EnumerationLiteralIndex=2
    NONE = "none"

    def __init__(self):
        super().__init__(
            [
                IPsecHeaderTypeEnum.AH,
                IPsecHeaderTypeEnum.ESP,
                IPsecHeaderTypeEnum.NONE,
            ]
        )


class IPsecDpdActionEnum(AREnum):
    """
    Potential Dead Peer Detection (Dpd) Actions
    """

    # IPsecDpdActionEnum method parity checklist:
    # Spec: AUTOSAR_CP_TPS_SystemTemplate.pdf, Table 6.228, p.577
    # Columns: impl / docstring / test / reader / writer / release   ([—] = no XML element)
    # (no methods) — serialized as value form on IPSecRule/IPSecConfigProps members
    # [x] __init__     [x] impl  [x] docstring  [x] test  [—] reader  [—] writer  R23-11

    # Deletes the SA. Tags: atp.EnumerationLiteralIndex=0
    CLEAR = "clear"

    # Immediately tries to establish the connection. Tags: atp.EnumerationLiteralIndex=2
    RESTART = "restart"

    # tries to establish the connection after traffic is sent to the peer. Tags: atp.EnumerationLiteralIndex=1
    TRAP = "trap"

    def __init__(self):
        super().__init__(
            [
                IPsecDpdActionEnum.CLEAR,
                IPsecDpdActionEnum.RESTART,
                IPsecDpdActionEnum.TRAP,
            ]
        )


class IPSecRule(Identifiable):
    """
    This element defines an IPsec rule that describes communication traffic that is monitored, protected and filtered.

    [TPS_SYST_02266] Definition of IPSecRules: The IPSecConfig meta-class may contain one or several IPSecRules. Each IPSecRule defines the network connection that is monitored by IPsec by defining the local endpoint and the remote endpoint. Each endpoint is defined by the IP Address and the Tcp/Udp Port. The communication direction for which the IPSecRule is valid is defined by the direction attribute.

    [constr_5163] Existence of IPSecRule.headerType: For each IPSecRule, the attribute headerType shall exist at the time when the System Description is complete.

    [constr_5164] Existence of IPSecRule.ipProtocol: For each IPSecRule, the attribute ipProtocol shall exist at the time when the System Description is complete.

    [constr_5165] Existence of IPSecRule.policy: For each IPSecRule, the attribute policy shall exist at the time when the System Description is complete.
    """

    # IPSecRule method parity checklist:
    # Spec: AUTOSAR_CP_TPS_SystemTemplate.pdf, Table 6.222, p.572 (R23-11)
    # Table 6.222's body is split by an image/glyph interruption after localPortRangeEnd; the
    # continuation block (localPortRangeStart..remotePortRangeStart) was verified row-by-row
    # against the XSD group IP-SEC-RULE (AUTOSAR_00052.xsd L73884) — all 16 attributes carry
    # R23-11 markdown text; no R4.3.1 / XSD-doc fallback rows were needed.
    # ikeAuthenticationMethod (XSD atp.Status="removed"; absent from the PDF table) is not modeled.
    # Columns: impl / docstring / test / reader / writer / release   ([—] = no XML element)
    # [x] __init__                     [x] impl  [x] docstring  [x] test  [—] reader  [—] writer  R23-11
    # [x] getDirection                 [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setDirection                 [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getHeaderType                [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setHeaderType                [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getIpProtocol                [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setIpProtocol                [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] addLocalCertificateRef       [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getLocalCertificateRefs      [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] getLocalId                   [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setLocalId                   [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getLocalPortRangeEnd         [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setLocalPortRangeEnd         [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getLocalPortRangeStart       [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setLocalPortRangeStart       [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getMode                      [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setMode                      [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getPolicy                    [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setPolicy                    [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getPreSharedKeyRef           [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setPreSharedKeyRef           [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getPriority                  [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setPriority                  [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] addRemoteCertificateRef      [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getRemoteCertificateRefs     [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] getRemoteId                  [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setRemoteId                  [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] addRemoteIpAddressRef        [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getRemoteIpAddressRefs       [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] getRemotePortRangeEnd        [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setRemotePortRangeEnd        [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getRemotePortRangeStart      [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setRemotePortRangeStart      [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11

    def __init__(self, parent, short_name):
        super().__init__(parent, short_name)

        # This attribute defines the direction in which the traffic is monitored. If this attribute is not set a bidirectional traffic monitoring is assumed.
        self.direction: Optional[CommunicationDirectionType] = None

        # Header type specifying the IPsec security mechanism.
        self.headerType: Optional[IPsecHeaderTypeEnum] = None

        # This attribute defines the relevant IP protocol used in the Security Policy Database (SPD) entry.
        self.ipProtocol: Optional[IPsecIpProtocolEnum] = None

        # This reference identifies the applicable certificate used for a local authentication.
        self.localCertificateRefs: List[RefType] = []

        # This attribute defines how the local participant should be identified for authentication.
        self.localId: Optional[String] = None

        # This attribute restricts the traffic monitoring and defines an end value for the local port range. If this attribute is not set then this rule shall be effective for all local ports. Please note that port ranges are currently not supported in the AUTOSAR AP's operating system backend. If AP systems are involved, each IPsec rule may only contain a single port.
        self.localPortRangeEnd: Optional[PositiveInteger] = None

        # This attribute restricts the traffic monitoring and defines a start value for the local port range. If this attribute is not set then this rule shall be effective for all local ports. Please note that port ranges are currently not supported in the AUTOSAR AP's operating system backend. If AP systems are involved, each IPsec rule may only contain a single port.
        self.localPortRangeStart: Optional[PositiveInteger] = None

        # This attribute defines the type of the connection.
        self.mode: Optional[IPsecModeEnum] = None

        # An IPsec policy defines the rules that determine which type of IP traffic needs to be secured using IPsec and how that traffic is secured.
        self.policy: Optional[IPsecPolicyEnum] = None

        # This reference identifies the applicable cryptograhic key used for authentication.
        self.preSharedKeyRef: Optional[RefType] = None

        # This attribute defines the priority of the IPSecRule (SPD entry). The processing of entries is based on priority, starting with the highest priority "0".
        self.priority: Optional[PositiveInteger] = None

        # This reference identifies the applicable certificate used for a remote authentication.
        self.remoteCertificateRefs: List[RefType] = []

        # This attribute defines how the remote participant should be identified for authentication.
        self.remoteId: Optional[String] = None

        # Definition of the remote NetworkEndpoint. With this reference the connection between the local Network Endpoint and the remote NetworkEndpoint is described on which the traffic is monitored.
        self.remoteIpAddressRefs: List[RefType] = []

        # This attribute restricts the traffic monitoring and defines an end value for the remote port range. If this attribute is not set then this rule shall be effective for all local ports. Please note that port ranges are currently not supported in the AUTOSAR AP's operating system backend. If AP systems are involved, each IPsec rule may only contain a single port.
        self.remotePortRangeEnd: Optional[PositiveInteger] = None

        # This attribute restricts the traffic monitoring and defines a start value for the remote port range. If this attribute is not set then this rule shall be effective for all local ports. Please note that port ranges are currently not supported in the AUTOSAR AP's operating system backend. If AP systems are involved, each IPsec rule may only contain a single port.
        self.remotePortRangeStart: Optional[PositiveInteger] = None

    def getDirection(self) -> Optional[CommunicationDirectionType]:
        """This attribute defines the direction in which the traffic is monitored. If this attribute is not set a bidirectional traffic monitoring is assumed."""
        return self.direction

    def setDirection(self, value: Optional[CommunicationDirectionType]) -> IPSecRule:
        """
        This attribute defines the direction in which the traffic is monitored. If this attribute is not set a bidirectional traffic monitoring is assumed.
        A None value is a no-op and does not overwrite an existing direction.
        """
        if value is not None:
            self.direction = value
        return self

    def getHeaderType(self) -> Optional[IPsecHeaderTypeEnum]:
        """Header type specifying the IPsec security mechanism."""
        return self.headerType

    def setHeaderType(self, value: Optional[IPsecHeaderTypeEnum]) -> IPSecRule:
        """
        Header type specifying the IPsec security mechanism.
        A None value is a no-op and does not overwrite an existing headerType.
        """
        if value is not None:
            self.headerType = value
        return self

    def getIpProtocol(self) -> Optional[IPsecIpProtocolEnum]:
        """This attribute defines the relevant IP protocol used in the Security Policy Database (SPD) entry."""
        return self.ipProtocol

    def setIpProtocol(self, value: Optional[IPsecIpProtocolEnum]) -> IPSecRule:
        """
        This attribute defines the relevant IP protocol used in the Security Policy Database (SPD) entry.
        A None value is a no-op and does not overwrite an existing ipProtocol.
        """
        if value is not None:
            self.ipProtocol = value
        return self

    def addLocalCertificateRef(self, ref: Optional[RefType]) -> IPSecRule:
        """
        This reference identifies the applicable certificate used for a local authentication.
        A None value is a no-op and does not extend the localCertificateRefs list.
        """
        if ref is not None:
            self.localCertificateRefs.append(ref)
        return self

    def getLocalCertificateRefs(self) -> List[RefType]:
        """This reference identifies the applicable certificate used for a local authentication."""
        return self.localCertificateRefs

    def getLocalId(self) -> Optional[String]:
        """This attribute defines how the local participant should be identified for authentication."""
        return self.localId

    def setLocalId(self, value: Optional[String]) -> IPSecRule:
        """
        This attribute defines how the local participant should be identified for authentication.
        A None value is a no-op and does not overwrite an existing localId.
        """
        if value is not None:
            self.localId = value
        return self

    def getLocalPortRangeEnd(self) -> Optional[PositiveInteger]:
        """This attribute restricts the traffic monitoring and defines an end value for the local port range. If this attribute is not set then this rule shall be effective for all local ports. Please note that port ranges are currently not supported in the AUTOSAR AP's operating system backend. If AP systems are involved, each IPsec rule may only contain a single port."""
        return self.localPortRangeEnd

    def setLocalPortRangeEnd(self, value: Optional[PositiveInteger]) -> IPSecRule:
        """
        This attribute restricts the traffic monitoring and defines an end value for the local port range. If this attribute is not set then this rule shall be effective for all local ports. Please note that port ranges are currently not supported in the AUTOSAR AP's operating system backend. If AP systems are involved, each IPsec rule may only contain a single port.
        A None value is a no-op and does not overwrite an existing localPortRangeEnd.
        """
        if value is not None:
            self.localPortRangeEnd = value
        return self

    def getLocalPortRangeStart(self) -> Optional[PositiveInteger]:
        """This attribute restricts the traffic monitoring and defines a start value for the local port range. If this attribute is not set then this rule shall be effective for all local ports. Please note that port ranges are currently not supported in the AUTOSAR AP's operating system backend. If AP systems are involved, each IPsec rule may only contain a single port."""
        return self.localPortRangeStart

    def setLocalPortRangeStart(self, value: Optional[PositiveInteger]) -> IPSecRule:
        """
        This attribute restricts the traffic monitoring and defines a start value for the local port range. If this attribute is not set then this rule shall be effective for all local ports. Please note that port ranges are currently not supported in the AUTOSAR AP's operating system backend. If AP systems are involved, each IPsec rule may only contain a single port.
        A None value is a no-op and does not overwrite an existing localPortRangeStart.
        """
        if value is not None:
            self.localPortRangeStart = value
        return self

    def getMode(self) -> Optional[IPsecModeEnum]:
        """This attribute defines the type of the connection."""
        return self.mode

    def setMode(self, value: Optional[IPsecModeEnum]) -> IPSecRule:
        """
        This attribute defines the type of the connection.
        A None value is a no-op and does not overwrite an existing mode.
        """
        if value is not None:
            self.mode = value
        return self

    def getPolicy(self) -> Optional[IPsecPolicyEnum]:
        """An IPsec policy defines the rules that determine which type of IP traffic needs to be secured using IPsec and how that traffic is secured."""
        return self.policy

    def setPolicy(self, value: Optional[IPsecPolicyEnum]) -> IPSecRule:
        """
        An IPsec policy defines the rules that determine which type of IP traffic needs to be secured using IPsec and how that traffic is secured.
        A None value is a no-op and does not overwrite an existing policy.
        """
        if value is not None:
            self.policy = value
        return self

    def getPreSharedKeyRef(self) -> Optional[RefType]:
        """This reference identifies the applicable cryptograhic key used for authentication."""
        return self.preSharedKeyRef

    def setPreSharedKeyRef(self, value: Optional[RefType]) -> IPSecRule:
        """
        This reference identifies the applicable cryptograhic key used for authentication.
        A None value is a no-op and does not overwrite an existing preSharedKeyRef.
        """
        if value is not None:
            self.preSharedKeyRef = value
        return self

    def getPriority(self) -> Optional[PositiveInteger]:
        """This attribute defines the priority of the IPSecRule (SPD entry). The processing of entries is based on priority, starting with the highest priority "0"."""
        return self.priority

    def setPriority(self, value: Optional[PositiveInteger]) -> IPSecRule:
        """
        This attribute defines the priority of the IPSecRule (SPD entry). The processing of entries is based on priority, starting with the highest priority "0".
        A None value is a no-op and does not overwrite an existing priority.
        """
        if value is not None:
            self.priority = value
        return self

    def addRemoteCertificateRef(self, ref: Optional[RefType]) -> IPSecRule:
        """
        This reference identifies the applicable certificate used for a remote authentication.
        A None value is a no-op and does not extend the remoteCertificateRefs list.
        """
        if ref is not None:
            self.remoteCertificateRefs.append(ref)
        return self

    def getRemoteCertificateRefs(self) -> List[RefType]:
        """This reference identifies the applicable certificate used for a remote authentication."""
        return self.remoteCertificateRefs

    def getRemoteId(self) -> Optional[String]:
        """This attribute defines how the remote participant should be identified for authentication."""
        return self.remoteId

    def setRemoteId(self, value: Optional[String]) -> IPSecRule:
        """
        This attribute defines how the remote participant should be identified for authentication.
        A None value is a no-op and does not overwrite an existing remoteId.
        """
        if value is not None:
            self.remoteId = value
        return self

    def addRemoteIpAddressRef(self, ref: Optional[RefType]) -> IPSecRule:
        """
        Definition of the remote NetworkEndpoint. With this reference the connection between the local Network Endpoint and the remote NetworkEndpoint is described on which the traffic is monitored.
        A None value is a no-op and does not extend the remoteIpAddressRefs list.
        """
        if ref is not None:
            self.remoteIpAddressRefs.append(ref)
        return self

    def getRemoteIpAddressRefs(self) -> List[RefType]:
        """Definition of the remote NetworkEndpoint. With this reference the connection between the local Network Endpoint and the remote NetworkEndpoint is described on which the traffic is monitored."""
        return self.remoteIpAddressRefs

    def getRemotePortRangeEnd(self) -> Optional[PositiveInteger]:
        """This attribute restricts the traffic monitoring and defines an end value for the remote port range. If this attribute is not set then this rule shall be effective for all local ports. Please note that port ranges are currently not supported in the AUTOSAR AP's operating system backend. If AP systems are involved, each IPsec rule may only contain a single port."""
        return self.remotePortRangeEnd

    def setRemotePortRangeEnd(self, value: Optional[PositiveInteger]) -> IPSecRule:
        """
        This attribute restricts the traffic monitoring and defines an end value for the remote port range. If this attribute is not set then this rule shall be effective for all local ports. Please note that port ranges are currently not supported in the AUTOSAR AP's operating system backend. If AP systems are involved, each IPsec rule may only contain a single port.
        A None value is a no-op and does not overwrite an existing remotePortRangeEnd.
        """
        if value is not None:
            self.remotePortRangeEnd = value
        return self

    def getRemotePortRangeStart(self) -> Optional[PositiveInteger]:
        """This attribute restricts the traffic monitoring and defines a start value for the remote port range. If this attribute is not set then this rule shall be effective for all local ports. Please note that port ranges are currently not supported in the AUTOSAR AP's operating system backend. If AP systems are involved, each IPsec rule may only contain a single port."""
        return self.remotePortRangeStart

    def setRemotePortRangeStart(self, value: Optional[PositiveInteger]) -> IPSecRule:
        """
        This attribute restricts the traffic monitoring and defines a start value for the remote port range. If this attribute is not set then this rule shall be effective for all local ports. Please note that port ranges are currently not supported in the AUTOSAR AP's operating system backend. If AP systems are involved, each IPsec rule may only contain a single port.
        A None value is a no-op and does not overwrite an existing remotePortRangeStart.
        """
        if value is not None:
            self.remotePortRangeStart = value
        return self


class MacSecGlobalKayProps(ARElement):
    """
    Configuration of the MAC Security Key Agreement Entity properties that are shared by different KaY configurations.
    """

    # MacSecGlobalKayProps method parity checklist:
    # Spec: AUTOSAR_CP_TPS_SystemTemplate.pdf, Table 3.120, p.174
    # Spec verified: R23-11
    # Columns: impl / docstring / test / reader / writer   ([—] = no XML element)
    # [x] __init__                   [x] impl  [x] docstring  [x] test  [—] reader  [—] writer
    # [x] addBypassEtherType         [x] impl  [x] docstring  [x] test  [x] reader  [—] writer
    # [x] getBypassEtherTypes        [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] addBypassVlan              [x] impl  [x] docstring  [x] test  [x] reader  [—] writer
    # [x] getBypassVlans             [x] impl  [x] docstring  [x] test  [—] reader  [x] writer

    def __init__(self, parent, short_name):
        super().__init__(parent, short_name)

        # This attribute is used to define EtherTypes that are bypassed by MACsec. The providedEtherType will not be MACsec protected.
        self.bypassEtherTypes: List[PositiveInteger] = []

        # This attribute is used to define VLAN-IDs that are bypassed by MACsec. The provided VLAN-IDs will not be MACsec protected. (VLAN-ID 0 is interpreted as no-VLAN -> Bypass untagged traffic)
        self.bypassVlans: List[PositiveInteger] = []

    def addBypassEtherType(self, value: Optional[PositiveInteger]) -> MacSecGlobalKayProps:
        """
        This attribute is used to define EtherTypes that are bypassed by MACsec. The providedEtherType will not be MACsec protected.
        A None value is a no-op and does not append to bypassEtherTypes.
        """
        if value is not None:
            self.bypassEtherTypes.append(value)
        return self

    def getBypassEtherTypes(self) -> List[PositiveInteger]:
        """This attribute is used to define EtherTypes that are bypassed by MACsec. The providedEtherType will not be MACsec protected."""
        return self.bypassEtherTypes

    def addBypassVlan(self, value: Optional[PositiveInteger]) -> MacSecGlobalKayProps:
        """
        This attribute is used to define VLAN-IDs that are bypassed by MACsec. The provided VLAN-IDs will not be MACsec protected. (VLAN-ID 0 is interpreted as no-VLAN -> Bypass untagged traffic)
        A None value is a no-op and does not append to bypassVlans.
        """
        if value is not None:
            self.bypassVlans.append(value)
        return self

    def getBypassVlans(self) -> List[PositiveInteger]:
        """This attribute is used to define VLAN-IDs that are bypassed by MACsec. The provided VLAN-IDs will not be MACsec protected. (VLAN-ID 0 is interpreted as no-VLAN -> Bypass untagged traffic)"""
        return self.bypassVlans


class MacSecCipherSuiteConfig(ARObject):
    """
    This meta-class defines the cipher suite configuration to use with MACsec. cipherSuitePriority is present in case the MKA instance acts as a Key Server to select the cipher suite to use for MACsec.
    """

    # MacSecCipherSuiteConfig method parity checklist:
    # Spec: AUTOSAR_CP_TPS_SystemTemplate.pdf, Table 3.124, p.176
    # Spec verified: R23-11
    # Columns: impl / docstring / test / reader / writer   ([—] = no XML element)
    # [x] __init__                [x] impl  [x] docstring  [x] test  [—] reader  [—] writer
    # [x] getCipherSuite          [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] setCipherSuite          [x] impl  [x] docstring  [x] test  [x] reader  [—] writer
    # [x] getCipherSuitePriority  [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] setCipherSuitePriority  [x] impl  [x] docstring  [x] test  [x] reader  [—] writer

    def __init__(self):
        super().__init__()

        # Cipher Suite to use for MACsec.
        self.cipherSuite: Optional[String] = None

        # In case the MKA instance acts as a Key Server, the priority is used to select the Cipher Suite to use with MACsec from the supported Ciphers.
        self.cipherSuitePriority: Optional[PositiveInteger] = None

    def getCipherSuite(self) -> Optional[String]:
        """Cipher Suite to use for MACsec."""
        return self.cipherSuite

    def setCipherSuite(self, value: Optional[String]) -> MacSecCipherSuiteConfig:
        """
        Cipher Suite to use for MACsec.
        A None value is a no-op and does not overwrite an existing cipherSuite.
        """
        if value is not None:
            self.cipherSuite = value
        return self

    def getCipherSuitePriority(self) -> Optional[PositiveInteger]:
        """In case the MKA instance acts as a Key Server, the priority is used to select the Cipher Suite to use with MACsec from the supported Ciphers."""
        return self.cipherSuitePriority

    def setCipherSuitePriority(self, value: Optional[PositiveInteger]) -> MacSecCipherSuiteConfig:
        """
        In case the MKA instance acts as a Key Server, the priority is used to select the Cipher Suite to use with MACsec from the supported Ciphers.
        A None value is a no-op and does not overwrite an existing cipherSuitePriority.
        """
        if value is not None:
            self.cipherSuitePriority = value
        return self


class MacSecCryptoAlgoConfig(ARObject):
    """
    This meta-class defines the cryptography configuration for MACsec.
    """

    # MacSecCryptoAlgoConfig method parity checklist:
    # Spec: AUTOSAR_CP_TPS_SystemTemplate.pdf, Table 3.123, p.175
    # Spec verified: R23-11
    # Columns: impl / docstring / test / reader / writer   ([—] = no XML element)
    # [x] __init__                      [x] impl  [x] docstring  [x] test  [—] reader  [—] writer
    # [x] getCapability                 [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] setCapability                 [x] impl  [x] docstring  [x] test  [x] reader  [—] writer
    # [x] createCipherSuiteConfig       [x] impl  [x] docstring  [x] test  [x] reader  [—] writer
    # [x] getCipherSuiteConfigs         [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] getConfidentialityOffset      [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] setConfidentialityOffset      [x] impl  [x] docstring  [x] test  [x] reader  [—] writer
    # [x] getReplayProtection           [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] setReplayProtection           [x] impl  [x] docstring  [x] test  [x] reader  [—] writer
    # [x] getReplayProtectionWindow     [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] setReplayProtectionWindow     [x] impl  [x] docstring  [x] test  [x] reader  [—] writer

    def __init__(self):
        super().__init__()

        # This attribute defines the MACsec capability.
        self.capability: Optional[MacSecCapabilityEnum] = None

        # Cipher suite configuration to use with MACsec.
        self.cipherSuiteConfigs: List[MacSecCipherSuiteConfig] = []

        # The MACsec confidentiality offset specifies the number of bytes starting from the frame header. MACsec encrypts only the bytes after the offset in a frame.
        self.confidentialityOffset: Optional[MacSecConfidentialityOffsetEnum] = None

        # This attribute is used to configure the MACsec replay protection.
        self.replayProtection: Optional[Boolean] = None

        # In case replay protection is active, this attribute defines the replay protection window.
        self.replayProtectionWindow: Optional[PositiveInteger] = None

    def getCapability(self) -> Optional[MacSecCapabilityEnum]:
        """This attribute defines the MACsec capability."""
        return self.capability

    def setCapability(self, value: Optional[MacSecCapabilityEnum]) -> MacSecCryptoAlgoConfig:
        """
        This attribute defines the MACsec capability.
        A None value is a no-op and does not overwrite an existing capability.
        """
        if value is not None:
            self.capability = value
        return self

    def createCipherSuiteConfig(self) -> MacSecCipherSuiteConfig:
        """Cipher suite configuration to use with MACsec."""
        config = MacSecCipherSuiteConfig()
        self.cipherSuiteConfigs.append(config)
        return config

    def getCipherSuiteConfigs(self) -> List[MacSecCipherSuiteConfig]:
        """Cipher suite configuration to use with MACsec."""
        return self.cipherSuiteConfigs

    def getConfidentialityOffset(self) -> Optional[MacSecConfidentialityOffsetEnum]:
        """The MACsec confidentiality offset specifies the number of bytes starting from the frame header. MACsec encrypts only the bytes after the offset in a frame."""
        return self.confidentialityOffset

    def setConfidentialityOffset(self, value: Optional[MacSecConfidentialityOffsetEnum]) -> MacSecCryptoAlgoConfig:
        """
        The MACsec confidentiality offset specifies the number of bytes starting from the frame header. MACsec encrypts only the bytes after the offset in a frame.
        A None value is a no-op and does not overwrite an existing confidentialityOffset.
        """
        if value is not None:
            self.confidentialityOffset = value
        return self

    def getReplayProtection(self) -> Optional[Boolean]:
        """This attribute is used to configure the MACsec replay protection."""
        return self.replayProtection

    def setReplayProtection(self, value: Optional[Boolean]) -> MacSecCryptoAlgoConfig:
        """
        This attribute is used to configure the MACsec replay protection.
        A None value is a no-op and does not overwrite an existing replayProtection.
        """
        if value is not None:
            self.replayProtection = value
        return self

    def getReplayProtectionWindow(self) -> Optional[PositiveInteger]:
        """In case replay protection is active, this attribute defines the replay protection window."""
        return self.replayProtectionWindow

    def setReplayProtectionWindow(self, value: Optional[PositiveInteger]) -> MacSecCryptoAlgoConfig:
        """
        In case replay protection is active, this attribute defines the replay protection window.
        A None value is a no-op and does not overwrite an existing replayProtectionWindow.
        """
        if value is not None:
            self.replayProtectionWindow = value
        return self


class MacSecLocalKayProps(ARObject):
    """
    Configuration of the MAC Security Key Agreement Entity (KaY).
    """

    # MacSecLocalKayProps method parity checklist:
    # Spec: AUTOSAR_CP_TPS_SystemTemplate.pdf, Table 3.119, p.174
    # Spec verified: R23-11
    # Columns: impl / docstring / test / reader / writer   ([—] = no XML element)
    # [x] __init__                       [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] getDestinationMacAddress       [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] setDestinationMacAddress       [x] impl  [x] docstring  [x] test  [x] reader  [—] writer
    # [x] getGlobalKayPropsRef          [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] setGlobalKayPropsRef          [x] impl  [x] docstring  [x] test  [x] reader  [—] writer
    # [x] getKeyServerPriority          [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] setKeyServerPriority          [x] impl  [x] docstring  [x] test  [x] reader  [—] writer
    # [x] addMkaParticipantRef          [x] impl  [x] docstring  [x] test  [x] reader  [—] writer
    # [x] getMkaParticipantRefs         [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] getRole                        [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] setRole                        [x] impl  [x] docstring  [x] test  [x] reader  [—] writer
    # [x] getSourceMacAddress            [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] setSourceMacAddress            [x] impl  [x] docstring  [x] test  [x] reader  [—] writer

    def __init__(self):
        super().__init__()

        # This attribute defines the destination MAC Address that is used to calculate the ICV (Integrity Check Value).
        self.destinationMacAddress: Optional[MacAddressString] = None

        # Reference to properties that are shared between MAC Security Key Agreement Entities.
        self.globalKayPropsRef: Optional[RefType] = None

        # This attribute defines the key-server priority.
        self.keyServerPriority: Optional[PositiveInteger] = None

        # Reference to MKA participant settings supported on the CouplingPort.
        self.mkaParticipantRefs: List[RefType] = []

        # Role of the MAC Security Key Agreement Entity
        self.role: Optional[MacSecRoleEnum] = None

        # This attribute defines the source MAC Address that is used to calculate the ICV (Integrity Check Value).
        self.sourceMacAddress: Optional[MacAddressString] = None

    def getDestinationMacAddress(self) -> Optional[MacAddressString]:
        """This attribute defines the destination MAC Address that is used to calculate the ICV (Integrity Check Value)."""
        return self.destinationMacAddress

    def setDestinationMacAddress(self, value: Optional[MacAddressString]) -> MacSecLocalKayProps:
        """
        This attribute defines the destination MAC Address that is used to calculate the ICV (Integrity Check Value).
        A None value is a no-op and does not overwrite an existing destinationMacAddress.
        """
        if value is not None:
            self.destinationMacAddress = value
        return self

    def getGlobalKayPropsRef(self) -> Optional[RefType]:
        """Reference to properties that are shared between MAC Security Key Agreement Entities."""
        return self.globalKayPropsRef

    def setGlobalKayPropsRef(self, value: Optional[RefType]) -> MacSecLocalKayProps:
        """
        Reference to properties that are shared between MAC Security Key Agreement Entities.
        A None value is a no-op and does not overwrite an existing globalKayPropsRef.
        """
        if value is not None:
            self.globalKayPropsRef = value
        return self

    def getKeyServerPriority(self) -> Optional[PositiveInteger]:
        """This attribute defines the key-server priority."""
        return self.keyServerPriority

    def setKeyServerPriority(self, value: Optional[PositiveInteger]) -> MacSecLocalKayProps:
        """
        This attribute defines the key-server priority.
        A None value is a no-op and does not overwrite an existing keyServerPriority.
        """
        if value is not None:
            self.keyServerPriority = value
        return self

    def addMkaParticipantRef(self, ref: Optional[RefType]) -> MacSecLocalKayProps:
        """
        Reference to MKA participant settings supported on the CouplingPort.
        A None value is a no-op and does not append to mkaParticipantRefs.
        """
        if ref is not None:
            self.mkaParticipantRefs.append(ref)
        return self

    def getMkaParticipantRefs(self) -> List[RefType]:
        """Reference to MKA participant settings supported on the CouplingPort."""
        return self.mkaParticipantRefs

    def getRole(self) -> Optional[MacSecRoleEnum]:
        """Role of the MAC Security Key Agreement Entity"""
        return self.role

    def setRole(self, value: Optional[MacSecRoleEnum]) -> MacSecLocalKayProps:
        """
        Role of the MAC Security Key Agreement Entity
        A None value is a no-op and does not overwrite an existing role.
        """
        if value is not None:
            self.role = value
        return self

    def getSourceMacAddress(self) -> Optional[MacAddressString]:
        """This attribute defines the source MAC Address that is used to calculate the ICV (Integrity Check Value)."""
        return self.sourceMacAddress

    def setSourceMacAddress(self, value: Optional[MacAddressString]) -> MacSecLocalKayProps:
        """
        This attribute defines the source MAC Address that is used to calculate the ICV (Integrity Check Value).
        A None value is a no-op and does not overwrite an existing sourceMacAddress.
        """
        if value is not None:
            self.sourceMacAddress = value
        return self


class MacSecKayParticipant(Identifiable):
    """
    This meta-class configures a MKA participant.
    """

    # MacSecKayParticipant method parity checklist:
    # Spec: AUTOSAR_CP_TPS_SystemTemplate.pdf, Table 3.122, p.175
    # Spec verified: R23-11
    # Columns: impl / docstring / test / reader / writer   ([—] = no XML element)
    # [x] __init__                      [x] impl  [x] docstring  [x] test  [—] reader  [—] writer
    # [x] getCknRef                     [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] setCknRef                     [x] impl  [x] docstring  [x] test  [x] reader  [—] writer
    # [x] getCryptoAlgoConfig           [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] setCryptoAlgoConfig           [x] impl  [x] docstring  [x] test  [x] reader  [—] writer
    # [x] getSakRef                     [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] setSakRef                     [x] impl  [x] docstring  [x] test  [x] reader  [—] writer

    def __init__(self, parent, short_name):
        super().__init__(parent, short_name)

        # Reference to the key where the ckn (Connectivity Association key) is stored.
        self.cknRef: Optional[RefType] = None

        # Cryptography that is used by the MKA Participant.
        self.cryptoAlgoConfig: Optional[MacSecCryptoAlgoConfig] = None

        # Reference to the key where SAK shall be stored.
        self.sakRef: Optional[RefType] = None

    def getCknRef(self) -> Optional[RefType]:
        """Reference to the key where the ckn (Connectivity Association key) is stored."""
        return self.cknRef

    def setCknRef(self, value: Optional[RefType]) -> MacSecKayParticipant:
        """
        Reference to the key where the ckn (Connectivity Association key) is stored.
        A None value is a no-op and does not overwrite an existing cknRef.
        """
        if value is not None:
            self.cknRef = value
        return self

    def getCryptoAlgoConfig(self) -> Optional[MacSecCryptoAlgoConfig]:
        """Cryptography that is used by the MKA Participant."""
        return self.cryptoAlgoConfig

    def setCryptoAlgoConfig(self, value: Optional[MacSecCryptoAlgoConfig]) -> MacSecKayParticipant:
        """
        Cryptography that is used by the MKA Participant.
        A None value is a no-op and does not overwrite an existing cryptoAlgoConfig.
        """
        if value is not None:
            self.cryptoAlgoConfig = value
        return self

    def getSakRef(self) -> Optional[RefType]:
        """Reference to the key where SAK shall be stored."""
        return self.sakRef

    def setSakRef(self, value: Optional[RefType]) -> MacSecKayParticipant:
        """
        Reference to the key where SAK shall be stored.
        A None value is a no-op and does not overwrite an existing sakRef.
        """
        if value is not None:
            self.sakRef = value
        return self


class MacSecProps(ARObject):
    """
    This meta-class allows to configure MACsec (Media access control security) and the MKA (MACsec Key Agreement) for the CouplingPort (PHY).
    """

    # MacSecProps method parity checklist:
    # Spec: AUTOSAR_CP_TPS_SystemTemplate.pdf, Table 3.118, p.173
    # Spec verified: R23-11
    # Columns: impl / docstring / test / reader / writer   ([—] = no XML element)
    # [x] __init__                          [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] getAutoStart                     [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] setAutoStart                     [x] impl  [x] docstring  [x] test  [x] reader  [—] writer
    # [x] getMacSecKayConfig               [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] setMacSecKayConfig               [x] impl  [x] docstring  [x] test  [x] reader  [—] writer
    # [x] getOnFailPermissiveMode          [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] setOnFailPermissiveMode          [x] impl  [x] docstring  [x] test  [x] reader  [—] writer
    # [x] getOnFailPermissiveModeTimeout   [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] setOnFailPermissiveModeTimeout   [x] impl  [x] docstring  [x] test  [x] reader  [—] writer
    # [x] getSakRekeyTimeSpan              [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] setSakRekeyTimeSpan              [x] impl  [x] docstring  [x] test  [x] reader  [—] writer

    def __init__(self):
        super().__init__()

        # This attribute defines how the Port Access Entity (PAE) is started: • true := Autostart • false := Manual Start
        self.autoStart: Optional[Boolean] = None

        # Properties to configure the MKA instance (KaY) for a controlled CouplingPort (PaE).
        self.macSecKayConfig: Optional[MacSecLocalKayProps] = None

        # This attribute sets the behavior of the Port Access Entity in case MACsec does not succeed.
        self.onFailPermissiveMode: Optional[MacSecFailPermissiveModeEnum] = None

        # Timeout in seconds to enable the controlled port in case onFailPermissiveMode is set to Timeout.
        self.onFailPermissiveModeTimeout: Optional[TimeValue] = None

        # Time in seconds to trigger the rekey of an in use SAK (Static Secure Association key). If set to 0, the rekey will not be triggered after a time span.
        self.sakRekeyTimeSpan: Optional[TimeValue] = None

    def getAutoStart(self) -> Optional[Boolean]:
        """This attribute defines how the Port Access Entity (PAE) is started: • true := Autostart • false := Manual Start"""
        return self.autoStart

    def setAutoStart(self, value: Optional[Boolean]) -> MacSecProps:
        """
        This attribute defines how the Port Access Entity (PAE) is started: • true := Autostart • false := Manual Start
        A None value is a no-op and does not overwrite an existing autoStart.
        """
        if value is not None:
            self.autoStart = value
        return self

    def getMacSecKayConfig(self) -> Optional[MacSecLocalKayProps]:
        """Properties to configure the MKA instance (KaY) for a controlled CouplingPort (PaE)."""
        return self.macSecKayConfig

    def setMacSecKayConfig(self, value: Optional[MacSecLocalKayProps]) -> MacSecProps:
        """
        Properties to configure the MKA instance (KaY) for a controlled CouplingPort (PaE).
        A None value is a no-op and does not overwrite an existing macSecKayConfig.
        """
        if value is not None:
            self.macSecKayConfig = value
        return self

    def getOnFailPermissiveMode(self) -> Optional[MacSecFailPermissiveModeEnum]:
        """This attribute sets the behavior of the Port Access Entity in case MACsec does not succeed."""
        return self.onFailPermissiveMode

    def setOnFailPermissiveMode(self, value: Optional[MacSecFailPermissiveModeEnum]) -> MacSecProps:
        """
        This attribute sets the behavior of the Port Access Entity in case MACsec does not succeed.
        A None value is a no-op and does not overwrite an existing onFailPermissiveMode.
        """
        if value is not None:
            self.onFailPermissiveMode = value
        return self

    def getOnFailPermissiveModeTimeout(self) -> Optional[TimeValue]:
        """Timeout in seconds to enable the controlled port in case onFailPermissiveMode is set to Timeout."""
        return self.onFailPermissiveModeTimeout

    def setOnFailPermissiveModeTimeout(self, value: Optional[TimeValue]) -> MacSecProps:
        """
        Timeout in seconds to enable the controlled port in case onFailPermissiveMode is set to Timeout.
        A None value is a no-op and does not overwrite an existing onFailPermissiveModeTimeout.
        """
        if value is not None:
            self.onFailPermissiveModeTimeout = value
        return self

    def getSakRekeyTimeSpan(self) -> Optional[TimeValue]:
        """Time in seconds to trigger the rekey of an in use SAK (Static Secure Association key). If set to 0, the rekey will not be triggered after a time span."""
        return self.sakRekeyTimeSpan

    def setSakRekeyTimeSpan(self, value: Optional[TimeValue]) -> MacSecProps:
        """
        Time in seconds to trigger the rekey of an in use SAK (Static Secure Association key). If set to 0, the rekey will not be triggered after a time span.
        A None value is a no-op and does not overwrite an existing sakRekeyTimeSpan.
        """
        if value is not None:
            self.sakRekeyTimeSpan = value
        return self


# Cycle-breaker: CommunicationDirectionType (FibexCore.CoreCommunication) transitively
# imports MacSecProps from this module via Fibex4Ethernet.EthernetTopology; a top-of-module
# import runs while this module is partially initialized (Rule 0005 bottom-import).
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore.CoreCommunication import CommunicationDirectionType  # noqa: E402
