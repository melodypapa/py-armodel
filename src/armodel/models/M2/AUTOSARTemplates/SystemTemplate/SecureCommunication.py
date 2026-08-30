# This module contains AUTOSAR System Template classes for secure communication
# It defines crypto service mappings and TLS configurations for secure data transmission

from typing import List, Optional
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
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable import ARElement


class CryptoServiceMapping(Identifiable, ABC):
    """
    Abstract base class for crypto service mappings, defining
    common properties for different types of cryptographic
    service mappings in the AUTOSAR system.
    """

    # CryptoServiceMapping method parity checklist:
    # [ ] __init__                     [x] impl  [ ] docstring  [ ] test

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

    # SecOcCryptoServiceMapping method parity checklist:
    # [ ] __init__                     [x] impl  [ ] docstring  [ ] test
    # [ ] getAuthenticationRef         [x] impl  [ ] docstring  [ ] test
    # [ ] setAuthenticationRef         [x] impl  [ ] docstring  [ ] test
    # [ ] getCryptoServiceKeyRef       [x] impl  [ ] docstring  [ ] test
    # [ ] setCryptoServiceKeyRef       [x] impl  [ ] docstring  [ ] test
    # [ ] getCryptoServiceQueueRef     [x] impl  [ ] docstring  [ ] test
    # [ ] setCryptoServiceQueueRef     [x] impl  [ ] docstring  [ ] test

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

    # TlsCryptoServiceMapping method parity checklist:
    # [ ] __init__                     [x] impl  [ ] docstring  [ ] test
    # [ ] getKeyExchangeRef            [x] impl  [ ] docstring  [ ] test
    # [ ] setKeyExchangeRef            [x] impl  [ ] docstring  [ ] test
    # [ ] getTlsCipherSuites           [x] impl  [ ] docstring  [ ] test
    # [ ] addTlsCipherSuite            [x] impl  [ ] docstring  [ ] test
    # [ ] getUseClientAuthenticationRequest [x] impl  [ ] docstring  [ ] test
    # [ ] setUseClientAuthenticationRequest [x] impl  [ ] docstring  [ ] test
    # [ ] getUseSecurityExtensionRecordSizeLimit [x] impl  [ ] docstring  [ ] test
    # [ ] setUseSecurityExtensionRecordSizeLimit [x] impl  [ ] docstring  [ ] test

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

    def addBypassEtherType(self, value: Optional[PositiveInteger]) -> "MacSecGlobalKayProps":
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

    def addBypassVlan(self, value: Optional[PositiveInteger]) -> "MacSecGlobalKayProps":
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

    def setCipherSuite(self, value: Optional[String]) -> "MacSecCipherSuiteConfig":
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

    def setCipherSuitePriority(self, value: Optional[PositiveInteger]) -> "MacSecCipherSuiteConfig":
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

    def setCapability(self, value: Optional[MacSecCapabilityEnum]) -> "MacSecCryptoAlgoConfig":
        """
        This attribute defines the MACsec capability.
        A None value is a no-op and does not overwrite an existing capability.
        """
        if value is not None:
            self.capability = value
        return self

    def createCipherSuiteConfig(self) -> "MacSecCipherSuiteConfig":
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

    def setConfidentialityOffset(self, value: Optional[MacSecConfidentialityOffsetEnum]) -> "MacSecCryptoAlgoConfig":
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

    def setReplayProtection(self, value: Optional[Boolean]) -> "MacSecCryptoAlgoConfig":
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

    def setReplayProtectionWindow(self, value: Optional[PositiveInteger]) -> "MacSecCryptoAlgoConfig":
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
    # [x] getGlobalKayProps              [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] setGlobalKayProps              [x] impl  [x] docstring  [x] test  [x] reader  [—] writer
    # [x] getKeyServerPriority          [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] setKeyServerPriority          [x] impl  [x] docstring  [x] test  [x] reader  [—] writer
    # [x] addMkaParticipant              [x] impl  [x] docstring  [x] test  [x] reader  [—] writer
    # [x] getMkaParticipant              [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] getRole                        [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] setRole                        [x] impl  [x] docstring  [x] test  [x] reader  [—] writer
    # [x] getSourceMacAddress            [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] setSourceMacAddress            [x] impl  [x] docstring  [x] test  [x] reader  [—] writer

    def __init__(self):
        super().__init__()

        # This attribute defines the destination MAC Address that is used to calculate the ICV (Integrity Check Value).
        self.destinationMacAddress: Optional[MacAddressString] = None

        # Reference to properties that are shared between MAC Security Key Agreement Entities.
        self.globalKayProps: Optional[RefType] = None

        # This attribute defines the key-server priority.
        self.keyServerPriority: Optional[PositiveInteger] = None

        # Reference to MKA participant settings supported on the CouplingPort.
        self.mkaParticipant: List[RefType] = []

        # Role of the MAC Security Key Agreement Entity
        self.role: Optional[MacSecRoleEnum] = None

        # This attribute defines the source MAC Address that is used to calculate the ICV (Integrity Check Value).
        self.sourceMacAddress: Optional[MacAddressString] = None

    def getDestinationMacAddress(self) -> Optional[MacAddressString]:
        """This attribute defines the destination MAC Address that is used to calculate the ICV (Integrity Check Value)."""
        return self.destinationMacAddress

    def setDestinationMacAddress(self, value: Optional[MacAddressString]) -> "MacSecLocalKayProps":
        """
        This attribute defines the destination MAC Address that is used to calculate the ICV (Integrity Check Value).
        A None value is a no-op and does not overwrite an existing destinationMacAddress.
        """
        if value is not None:
            self.destinationMacAddress = value
        return self

    def getGlobalKayProps(self) -> Optional[RefType]:
        """Reference to properties that are shared between MAC Security Key Agreement Entities."""
        return self.globalKayProps

    def setGlobalKayProps(self, value: Optional[RefType]) -> "MacSecLocalKayProps":
        """
        Reference to properties that are shared between MAC Security Key Agreement Entities.
        A None value is a no-op and does not overwrite an existing globalKayProps.
        """
        if value is not None:
            self.globalKayProps = value
        return self

    def getKeyServerPriority(self) -> Optional[PositiveInteger]:
        """This attribute defines the key-server priority."""
        return self.keyServerPriority

    def setKeyServerPriority(self, value: Optional[PositiveInteger]) -> "MacSecLocalKayProps":
        """
        This attribute defines the key-server priority.
        A None value is a no-op and does not overwrite an existing keyServerPriority.
        """
        if value is not None:
            self.keyServerPriority = value
        return self

    def addMkaParticipant(self, ref: Optional[RefType]) -> "MacSecLocalKayProps":
        """
        Reference to MKA participant settings supported on the CouplingPort.
        A None value is a no-op and does not append to mkaParticipant.
        """
        if ref is not None:
            self.mkaParticipant.append(ref)
        return self

    def getMkaParticipant(self) -> List[RefType]:
        """Reference to MKA participant settings supported on the CouplingPort."""
        return self.mkaParticipant

    def getRole(self) -> Optional[MacSecRoleEnum]:
        """Role of the MAC Security Key Agreement Entity"""
        return self.role

    def setRole(self, value: Optional[MacSecRoleEnum]) -> "MacSecLocalKayProps":
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

    def setSourceMacAddress(self, value: Optional[MacAddressString]) -> "MacSecLocalKayProps":
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
    # [x] getCkn                        [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] setCkn                        [x] impl  [x] docstring  [x] test  [x] reader  [—] writer
    # [x] getCryptoAlgoConfig           [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] setCryptoAlgoConfig           [x] impl  [x] docstring  [x] test  [x] reader  [—] writer
    # [x] getSak                        [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] setSak                        [x] impl  [x] docstring  [x] test  [x] reader  [—] writer

    def __init__(self, parent, short_name):
        super().__init__(parent, short_name)

        # Reference to the key where the ckn (Connectivity Association key) is stored.
        self.ckn: Optional[RefType] = None

        # Cryptography that is used by the MKA Participant.
        self.cryptoAlgoConfig: Optional[MacSecCryptoAlgoConfig] = None

        # Reference to the key where SAK shall be stored.
        self.sak: Optional[RefType] = None

    def getCkn(self) -> Optional[RefType]:
        """Reference to the key where the ckn (Connectivity Association key) is stored."""
        return self.ckn

    def setCkn(self, value: Optional[RefType]) -> "MacSecKayParticipant":
        """
        Reference to the key where the ckn (Connectivity Association key) is stored.
        A None value is a no-op and does not overwrite an existing ckn.
        """
        if value is not None:
            self.ckn = value
        return self

    def getCryptoAlgoConfig(self) -> Optional[MacSecCryptoAlgoConfig]:
        """Cryptography that is used by the MKA Participant."""
        return self.cryptoAlgoConfig

    def setCryptoAlgoConfig(self, value: Optional[MacSecCryptoAlgoConfig]) -> "MacSecKayParticipant":
        """
        Cryptography that is used by the MKA Participant.
        A None value is a no-op and does not overwrite an existing cryptoAlgoConfig.
        """
        if value is not None:
            self.cryptoAlgoConfig = value
        return self

    def getSak(self) -> Optional[RefType]:
        """Reference to the key where SAK shall be stored."""
        return self.sak

    def setSak(self, value: Optional[RefType]) -> "MacSecKayParticipant":
        """
        Reference to the key where SAK shall be stored.
        A None value is a no-op and does not overwrite an existing sak.
        """
        if value is not None:
            self.sak = value
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

    def setAutoStart(self, value: Optional[Boolean]) -> "MacSecProps":
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

    def setMacSecKayConfig(self, value: Optional[MacSecLocalKayProps]) -> "MacSecProps":
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

    def setOnFailPermissiveMode(self, value: Optional[MacSecFailPermissiveModeEnum]) -> "MacSecProps":
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

    def setOnFailPermissiveModeTimeout(self, value: Optional[TimeValue]) -> "MacSecProps":
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

    def setSakRekeyTimeSpan(self, value: Optional[TimeValue]) -> "MacSecProps":
        """
        Time in seconds to trigger the rekey of an in use SAK (Static Secure Association key). If set to 0, the rekey will not be triggered after a time span.
        A None value is a no-op and does not overwrite an existing sakRekeyTimeSpan.
        """
        if value is not None:
            self.sakRekeyTimeSpan = value
        return self
