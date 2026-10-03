from abc import ABC
from typing import List, Optional

from armodel.models.M2.AUTOSARTemplates.DiagnosticExtract.CommonDiagnostics import DiagnosticCommonElement
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import (
    ARObject,
    DiagnosticComControlSpecificChannel,
    DiagnosticComControlSubNodeChannel,
    DiagnosticPeriodicRate,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Boolean,
    DiagnosticDynamicallyDefineDataIdentifierSubfunctionEnum,
    DiagnosticHandleDDDIConfigurationEnum,
    DiagnosticResponseToEcuResetEnum,
    PositiveInteger,
    RefType,
    TimeValue,
)


class DiagnosticServiceInstance(DiagnosticCommonElement, ABC):
    """This represents a concrete instance of a diagnostic service."""

    # DiagnosticServiceInstance method parity checklist:
    # Spec: AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf, Table 4.26, p.70
    # Spec verified: R23-11
    # Columns: impl / docstring / test / reader / writer / release   ([—] = no XML element)
    # [x] __init__                [x] impl  [x] docstring  [x] test  [—] reader  [—] writer  R23-11
    # [x] setAccessPermissionRef  [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getAccessPermissionRef  [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setServiceClassRef      [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getServiceClassRef      [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11

    def __init__(self, parent: ARObject, short_name: str):
        if type(self) is DiagnosticServiceInstance:
            raise TypeError("DiagnosticServiceInstance is an abstract class.")
        super().__init__(parent, short_name)

        # This represents the collection of DiagnosticAccessPermissions that allow for the execution of the referencing DiagnosticServiceInstance..
        self.accessPermissionRef: Optional[RefType] = None

        # This represents the corresponding "class", i.e. this meta-class provides properties that are shared among all instances of applicable sub-classes of DiagnosticServiceInstance. The subclasses that affected by this pattern implement references to the applicable "class"-role that substantiate this abstract reference. Stereotypes: atpAbstract
        self.serviceClassRef: Optional[RefType] = None

    def getAccessPermissionRef(self) -> Optional[RefType]:
        """
        This represents the collection of DiagnosticAccessPermissions that allow for the execution of the referencing DiagnosticServiceInstance..
        """
        return self.accessPermissionRef

    def setAccessPermissionRef(self, value: Optional[RefType]):
        """
        This represents the collection of DiagnosticAccessPermissions that allow for the execution of the referencing DiagnosticServiceInstance..

        A None value is a no-op and does not overwrite an existing accessPermissionRef.
        """
        if value is not None:
            self.accessPermissionRef = value
        return self

    def getServiceClassRef(self) -> Optional[RefType]:
        """
        This represents the corresponding "class", i.e. this meta-class provides properties that are shared among all instances of applicable sub-classes of DiagnosticServiceInstance. The subclasses that affected by this pattern implement references to the applicable "class"-role that substantiate this abstract reference. Stereotypes: atpAbstract
        """
        return self.serviceClassRef

    def setServiceClassRef(self, value: Optional[RefType]):
        """
        This represents the corresponding "class", i.e. this meta-class provides properties that are shared among all instances of applicable sub-classes of DiagnosticServiceInstance. The subclasses that affected by this pattern implement references to the applicable "class"-role that substantiate this abstract reference. Stereotypes: atpAbstract

        A None value is a no-op and does not overwrite an existing serviceClassRef.
        """
        if value is not None:
            self.serviceClassRef = value
        return self


class DiagnosticServiceClass(DiagnosticCommonElement, ABC):
    """This meta-class provides the ability to define common properties that are shared among all instances of sub-classes of DiagnosticServiceInstance."""

    # DiagnosticServiceClass method parity checklist:
    # Spec: AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf, Table 4.25, p.69
    # Spec verified: R23-11
    # Columns: impl / docstring / test / reader / writer / release   ([—] = no XML element)
    # [x] __init__  [x] impl  [x] docstring  [x] test  [—] reader  [—] writer  R23-11

    def __init__(self, parent: ARObject, short_name: str):
        if type(self) is DiagnosticServiceClass:
            raise TypeError("DiagnosticServiceClass is an abstract class.")

        super().__init__(parent, short_name)


class DiagnosticAuthenticationClass(DiagnosticServiceClass):
    """This meta-class contains configuration shared by all instances of the Authentication diagnostic service."""

    # DiagnosticAuthenticationClass method parity checklist:
    # Spec: AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf, Table 4.52, p.99
    # Columns: impl / docstring / test / reader / writer / release   ([—] = no XML element)
    # [x] __init__  [x] impl  [x] docstring  [x] test  [—] reader  [—] writer  R23-11

    def __init__(self, parent: ARObject, short_name: str):
        super().__init__(parent, short_name)


class DiagnosticClearDiagnosticInformationClass(DiagnosticServiceClass):
    """This meta-class contains attributes shared by all instances of the "Clear Diagnostic Information" diagnostic service."""

    # DiagnosticClearDiagnosticInformationClass method parity checklist:
    # Spec: AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf, Table 4.109, p.137
    # Columns: impl / docstring / test / reader / writer / release   ([—] = no XML element)
    # [x] __init__  [x] impl  [x] docstring  [x] test  [—] reader  [—] writer  R23-11

    def __init__(self, parent: ARObject, short_name: str):
        super().__init__(parent, short_name)


class DiagnosticClearResetEmissionRelatedInfoClass(DiagnosticServiceClass):
    """This meta-class represents the ability to define common properties for all instances of the "Clear Reset Emission Related Data" OBD diagnostic service."""

    # DiagnosticClearResetEmissionRelatedInfoClass method parity checklist:
    # Spec: AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf, Table 4.138, p.155
    # Columns: impl / docstring / test / reader / writer / release   ([—] = no XML element)
    # [x] __init__  [x] impl  [x] docstring  [x] test  [—] reader  [—] writer  R23-11

    def __init__(self, parent: ARObject, short_name: str):
        super().__init__(parent, short_name)


class DiagnosticComControlClass(DiagnosticServiceClass):
    """This meta-class contains attributes shared by all instances of the "Communication Control" diagnostic service."""

    # DiagnosticComControlClass method parity checklist:
    # Spec: AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf, Table 4.66, p.109
    # Columns: impl / docstring / test / reader / writer / release   ([—] = no XML element)
    # [x] __init__                    [x] impl  [x] docstring  [x] test  [—] reader  [—] writer  R23-11
    # [x] addAllChannel               [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getAllChannels              [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] addAllPhysicalChannel       [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getAllPhysicalChannels      [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] addSpecificChannel          [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getSpecificChannels         [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] addSubNodeChannel           [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getSubNodeChannels          [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11

    def __init__(self, parent: ARObject, short_name: str):
        super().__init__(parent, short_name)

        # This reference represents the semantics that all available channels shall be affected. It is still necessary to refer to individual CommunicatuionClusters because there could be private CommunicationClusters in the System Extract that are not subject to the service "communication control". By referring to the applicable CommunicationClusters it can be made sure that only the affected CommunicationClusters are accessed.
        self.allChannels: List[RefType] = []

        # This reference represents the semantics that all available channels shall be affected. It is still necessary to refer to individual EthernetPhysicalChannels because there could be private VLANs (and thus private EthernetPhysicalChannels) in the System Extract that are not subject to the service "communication control". By referring to the applicable EthernetPhysicalChannels it can be made sure that only the affected EthernetPhysicalChannels are accessed.
        self.allPhysicalChannels: List[RefType] = []

        # This represents the ability to add additional attributes to the case that only specific channels are supposed to be considered,
        self.specificChannel: List[DiagnosticComControlSpecificChannel] = []

        # This attribute represents the ability to add further attributes to the definition of a specific sub-node channel that is subject to the diagnostic service "communication control".
        self.subNodeChannel: List[DiagnosticComControlSubNodeChannel] = []

    def addAllChannel(self, value: Optional[RefType]) -> "DiagnosticComControlClass":
        """
        This reference represents the semantics that all available channels shall be affected. It is still necessary to refer to individual CommunicatuionClusters because there could be private CommunicationClusters in the System Extract that are not subject to the service "communication control". By referring to the applicable CommunicationClusters it can be made sure that only the affected CommunicationClusters are accessed.

        A None value is a no-op and does not append an allChannel.
        """
        if value is not None:
            self.allChannels.append(value)
        return self

    def getAllChannels(self) -> List[RefType]:
        """
        This reference represents the semantics that all available channels shall be affected. It is still necessary to refer to individual CommunicatuionClusters because there could be private CommunicationClusters in the System Extract that are not subject to the service "communication control". By referring to the applicable CommunicationClusters it can be made sure that only the affected CommunicationClusters are accessed.
        """
        return self.allChannels

    def addAllPhysicalChannel(self, value: Optional[RefType]) -> "DiagnosticComControlClass":
        """
        This reference represents the semantics that all available channels shall be affected. It is still necessary to refer to individual EthernetPhysicalChannels because there could be private VLANs (and thus private EthernetPhysicalChannels) in the System Extract that are not subject to the service "communication control". By referring to the applicable EthernetPhysicalChannels it can be made sure that only the affected EthernetPhysicalChannels are accessed.

        A None value is a no-op and does not append an allPhysicalChannel.
        """
        if value is not None:
            self.allPhysicalChannels.append(value)
        return self

    def getAllPhysicalChannels(self) -> List[RefType]:
        """
        This reference represents the semantics that all available channels shall be affected. It is still necessary to refer to individual EthernetPhysicalChannels because there could be private VLANs (and thus private EthernetPhysicalChannels) in the System Extract that are not subject to the service "communication control". By referring to the applicable EthernetPhysicalChannels it can be made sure that only the affected EthernetPhysicalChannels are accessed.
        """
        return self.allPhysicalChannels

    def addSpecificChannel(self, value: Optional[DiagnosticComControlSpecificChannel]) -> "DiagnosticComControlClass":
        """
        This represents the ability to add additional attributes to the case that only specific channels are supposed to be considered,

        A None value is a no-op and does not append a specificChannel.
        """
        if value is not None:
            self.specificChannel.append(value)
        return self

    def getSpecificChannels(self) -> List[DiagnosticComControlSpecificChannel]:
        """
        This represents the ability to add additional attributes to the case that only specific channels are supposed to be considered,
        """
        return self.specificChannel

    def addSubNodeChannel(self, value: Optional[DiagnosticComControlSubNodeChannel]) -> "DiagnosticComControlClass":
        """
        This attribute represents the ability to add further attributes to the definition of a specific sub-node channel that is subject to the diagnostic service "communication control".

        A None value is a no-op and does not append a subNodeChannel.
        """
        if value is not None:
            self.subNodeChannel.append(value)
        return self

    def getSubNodeChannels(self) -> List[DiagnosticComControlSubNodeChannel]:
        """
        This attribute represents the ability to add further attributes to the definition of a specific sub-node channel that is subject to the diagnostic service "communication control".
        """
        return self.subNodeChannel


class DiagnosticControlDTCSettingClass(DiagnosticServiceClass):
    """This meta-class contains attributes shared by all instances of the "Control DTC Setting" diagnostic service."""

    # DiagnosticControlDTCSettingClass method parity checklist:
    # Spec: AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf, Table 4.69, p.111
    # Columns: impl / docstring / test / reader / writer / release   ([—] = no XML element)
    # [x] __init__                        [x] impl  [x] docstring  [x] test  [—] reader  [—] writer  R23-11
    # [x] getControlOptionRecordPresent   [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setControlOptionRecordPresent   [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11

    def __init__(self, parent: ARObject, short_name: str):
        super().__init__(parent, short_name)

        # This represents the decision whether the DTCSettingControlOptionRecord (see ISO 14229-1) is in general supported in the request message.
        self.controlOptionRecordPresent: Optional[Boolean] = None

    def getControlOptionRecordPresent(self) -> Optional[Boolean]:
        """
        This represents the decision whether the DTCSettingControlOptionRecord (see ISO 14229-1) is in general supported in the request message.
        """
        return self.controlOptionRecordPresent

    def setControlOptionRecordPresent(self, value: Optional[Boolean]) -> "DiagnosticControlDTCSettingClass":
        """
        This represents the decision whether the DTCSettingControlOptionRecord (see ISO 14229-1) is in general supported in the request message.

        A None value is a no-op and does not overwrite an existing controlOptionRecordPresent.
        """
        if value is not None:
            self.controlOptionRecordPresent = value
        return self


class DiagnosticCustomServiceClass(DiagnosticServiceClass):
    """
    This represents the ability to define a custom diagnostic service class and assign an ID to it. Further configuration is not foreseen from the point of view of the diagnostic extract and consequently needs to be done on the level of ECUC.

    [constr_1330] Custom service identifier shall not overlap with standardized service identifiers: The value of the attribute customServiceId shall not be set to any of the values reserved for standardized service identifiers as defined by the ISO 14229-1, see [17]. This rule shall be imposed at the time when the DEXT is complete.
    """

    # DiagnosticCustomServiceClass method parity checklist:
    # Spec: AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf, Table 4.28, p.71
    # Columns: impl / docstring / test / reader / writer / release   ([—] = no XML element)
    # [x] __init__            [x] impl  [x] docstring  [x] test  [—] reader  [—] writer  R23-11
    # [x] getCustomServiceId  [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setCustomServiceId  [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11

    def __init__(self, parent: ARObject, short_name: str):
        super().__init__(parent, short_name)

        # This attribute may only be used for the definition of custom services. The values shall not overlap with existing standardized service IDs.
        self.customServiceId: Optional[PositiveInteger] = None

    def getCustomServiceId(self) -> Optional[PositiveInteger]:
        """
        This attribute may only be used for the definition of custom services. The values shall not overlap with existing standardized service IDs.
        """
        return self.customServiceId

    def setCustomServiceId(self, value: Optional[PositiveInteger]):
        """
        This attribute may only be used for the definition of custom services. The values shall not overlap with existing standardized service IDs.

        A None value is a no-op and does not overwrite an existing customServiceId.
        """
        if value is not None:
            self.customServiceId = value
        return self


class DiagnosticDataTransferClass(DiagnosticServiceClass):
    """This meta-class contains attributes shared by all instances of the "Data Transfer" diagnostic service."""

    # DiagnosticDataTransferClass method parity checklist:
    # Spec: AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf, Table 4.120, p.143
    # Columns: impl / docstring / test / reader / writer / release   ([—] = no XML element)
    # [x] __init__  [x] impl  [x] docstring  [x] test  [—] reader  [—] writer  R23-11

    def __init__(self, parent: ARObject, short_name: str):
        super().__init__(parent, short_name)


class DiagnosticDynamicallyDefineDataIdentifierClass(DiagnosticServiceClass):
    """This meta-class contains attributes shared by all instances of the "Dynamically Define Data Identifier" diagnostic service."""

    # DiagnosticDynamicallyDefineDataIdentifierClass method parity checklist:
    # Spec: AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf, Table 4.94, p.128
    # Columns: impl / docstring / test / reader / writer / release   ([—] = no XML element)
    # [x] __init__                    [x] impl  [x] docstring  [x] test  [—] reader  [—] writer  R23-11
    # [x] getCheckPerSourceId         [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setCheckPerSourceId         [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getConfigurationHandling    [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setConfigurationHandling    [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] addSubfunction              [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getSubfunctions             [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11

    def __init__(self, parent: ARObject, short_name: str):
        super().__init__(parent, short_name)

        # If set to TRUE, the Dcm module shall check the session, security and mode dependencies per source DIDs with a ReadDataByIdentifier (0x22) with DID in the range 0xF200 to 0xF3FF. If set to FALSE. the Dcm module shall not check the session, security and mode dependencies per source DIDs with a ReadDataByIdentifier (0x22) with DID in the range 0xF200 to 0xF3FF.
        self.checkPerSourceId: Optional[Boolean] = None

        # This configuration switch defines whether DDDID definition is handled as non-volatile information or not.
        self.configurationHandling: Optional[DiagnosticHandleDDDIConfigurationEnum] = None

        # This attribute contains a list of applicable subfunctions for all DiagnosticDynamicallyDefineDataIdentifier that reference the DiagnosticDynamicallyDefineDataIdentifier Class.
        self.subfunction: List[DiagnosticDynamicallyDefineDataIdentifierSubfunctionEnum] = []

    def getCheckPerSourceId(self) -> Optional[Boolean]:
        """
        If set to TRUE, the Dcm module shall check the session, security and mode dependencies per source DIDs with a ReadDataByIdentifier (0x22) with DID in the range 0xF200 to 0xF3FF. If set to FALSE. the Dcm module shall not check the session, security and mode dependencies per source DIDs with a ReadDataByIdentifier (0x22) with DID in the range 0xF200 to 0xF3FF.
        """
        return self.checkPerSourceId

    def setCheckPerSourceId(self, value: Optional[Boolean]) -> "DiagnosticDynamicallyDefineDataIdentifierClass":
        """
        If set to TRUE, the Dcm module shall check the session, security and mode dependencies per source DIDs with a ReadDataByIdentifier (0x22) with DID in the range 0xF200 to 0xF3FF. If set to FALSE. the Dcm module shall not check the session, security and mode dependencies per source DIDs with a ReadDataByIdentifier (0x22) with DID in the range 0xF200 to 0xF3FF.

        A None value is a no-op and does not overwrite an existing checkPerSourceId.
        """
        if value is not None:
            self.checkPerSourceId = value
        return self

    def getConfigurationHandling(self) -> Optional[DiagnosticHandleDDDIConfigurationEnum]:
        """
        This configuration switch defines whether DDDID definition is handled as non-volatile information or not.
        """
        return self.configurationHandling

    def setConfigurationHandling(self, value: Optional[DiagnosticHandleDDDIConfigurationEnum]) -> "DiagnosticDynamicallyDefineDataIdentifierClass":
        """
        This configuration switch defines whether DDDID definition is handled as non-volatile information or not.

        A None value is a no-op and does not overwrite an existing configurationHandling.
        """
        if value is not None:
            self.configurationHandling = value
        return self

    def addSubfunction(self, value: Optional[DiagnosticDynamicallyDefineDataIdentifierSubfunctionEnum]) -> "DiagnosticDynamicallyDefineDataIdentifierClass":
        """
        This attribute contains a list of applicable subfunctions for all DiagnosticDynamicallyDefineDataIdentifier that reference the DiagnosticDynamicallyDefineDataIdentifier Class.

        A None value is a no-op and does not append a subfunction.
        """
        if value is not None:
            self.subfunction.append(value)
        return self

    def getSubfunctions(self) -> List[DiagnosticDynamicallyDefineDataIdentifierSubfunctionEnum]:
        """
        This attribute contains a list of applicable subfunctions for all DiagnosticDynamicallyDefineDataIdentifier that reference the DiagnosticDynamicallyDefineDataIdentifier Class.
        """
        return self.subfunction


class DiagnosticEcuResetClass(DiagnosticServiceClass):
    """This meta-class contains attributes shared by all instances of the "Ecu Reset" diagnostic service."""

    # DiagnosticEcuResetClass method parity checklist:
    # Spec: AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf, Table 4.61, p.102
    # Columns: impl / docstring / test / reader / writer / release   ([—] = no XML element)
    # [x] __init__             [x] impl  [x] docstring  [x] test  [—] reader  [—] writer  R23-11
    # [x] getRespondToReset    [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setRespondToReset    [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11

    def __init__(self, parent: ARObject, short_name: str):
        super().__init__(parent, short_name)

        # This attribute defines whether the response to the EcuReset service shall be transmitted before or after the actual reset.
        self.respondToReset: Optional[DiagnosticResponseToEcuResetEnum] = None

    def getRespondToReset(self) -> Optional[DiagnosticResponseToEcuResetEnum]:
        """
        This attribute defines whether the response to the EcuReset service shall be transmitted before or after the actual reset.
        """
        return self.respondToReset

    def setRespondToReset(self, value: Optional[DiagnosticResponseToEcuResetEnum]):
        """
        This attribute defines whether the response to the EcuReset service shall be transmitted before or after the actual reset.

        A None value is a no-op and does not overwrite an existing respondToReset.
        """
        if value is not None:
            self.respondToReset = value
        return self


class DiagnosticIoControlClass(DiagnosticServiceClass):
    """This meta-class contains attributes shared by all instances of the "IO Control" diagnostic service."""

    # DiagnosticIoControlClass method parity checklist:
    # Spec: AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf, Table 4.81, p.118
    # Columns: impl / docstring / test / reader / writer / release   ([—] = no XML element)
    # [x] __init__  [x] impl  [x] docstring  [x] test  [—] reader  [—] writer  R23-11

    def __init__(self, parent: ARObject, short_name: str):
        super().__init__(parent, short_name)


class DiagnosticReadDTCInformationClass(DiagnosticServiceClass):
    """This meta-class contains attributes shared by all instances of the "ReadDTCInformation" diagnostic service."""

    # DiagnosticReadDTCInformationClass method parity checklist:
    # Spec: AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf, Table 4.107, p.136
    # Columns: impl / docstring / test / reader / writer / release   ([—] = no XML element)
    # [x] __init__  [x] impl  [x] docstring  [x] test  [—] reader  [—] writer  R23-11

    def __init__(self, parent: ARObject, short_name: str):
        super().__init__(parent, short_name)


class DiagnosticReadDataByIdentifierClass(DiagnosticServiceClass):
    """This meta-class contains attributes shared by all instances of the "Read Data by Identifier" diagnostic service."""

    # DiagnosticReadDataByIdentifierClass method parity checklist:
    # Spec: AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf, Table 4.74, p.114
    # Columns: impl / docstring / test / reader / writer / release   ([—] = no XML element)
    # [x] __init__           [x] impl  [x] docstring  [x] test  [—] reader  [—] writer  R23-11
    # [x] getMaxDidToRead    [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setMaxDidToRead    [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11

    def __init__(self, parent: ARObject, short_name: str):
        super().__init__(parent, short_name)

        # This attribute represents the maximum number of allowed DIDs in a single instance of DiagnosticReadDataByIdentifier.
        self.maxDidToRead: Optional[PositiveInteger] = None

    def getMaxDidToRead(self) -> Optional[PositiveInteger]:
        """
        This attribute represents the maximum number of allowed DIDs in a single instance of DiagnosticReadDataByIdentifier.
        """
        return self.maxDidToRead

    def setMaxDidToRead(self, value: Optional[PositiveInteger]) -> "DiagnosticReadDataByIdentifierClass":
        """
        This attribute represents the maximum number of allowed DIDs in a single instance of DiagnosticReadDataByIdentifier.

        A None value is a no-op and does not overwrite an existing maxDidToRead.
        """
        if value is not None:
            self.maxDidToRead = value
        return self


class DiagnosticReadDataByPeriodicIDClass(DiagnosticServiceClass):
    """This meta-class contains attributes shared by all instances of the "Read Data by periodic Identifier" diagnostic service."""

    # DiagnosticReadDataByPeriodicIDClass method parity checklist:
    # Spec: AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf, Table 4.98, p.130
    # Columns: impl / docstring / test / reader / writer / release   ([—] = no XML element)
    # [x] __init__                       [x] impl  [x] docstring  [x] test  [—] reader  [—] writer  R23-11
    # [x] getMaxPeriodicDidToRead        [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setMaxPeriodicDidToRead        [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] addPeriodicRate                [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getPeriodicRates               [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] getSchedulerMaxNumber          [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setSchedulerMaxNumber          [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11

    def __init__(self, parent: ARObject, short_name: str):
        super().__init__(parent, short_name)

        # This represents the maximum number of data identifiers that can be included in one request.
        self.maxPeriodicDidToRead: Optional[PositiveInteger] = None

        # This represents the description of a collection of periodic rates in which the service can be executed.
        self.periodicRate: List[DiagnosticPeriodicRate] = []

        # This represents the maximum number of periodic data identifiers that can be scheduled in parallel.
        self.schedulerMaxNumber: Optional[PositiveInteger] = None

    def getMaxPeriodicDidToRead(self) -> Optional[PositiveInteger]:
        """
        This represents the maximum number of data identifiers that can be included in one request.
        """
        return self.maxPeriodicDidToRead

    def setMaxPeriodicDidToRead(self, value: Optional[PositiveInteger]) -> "DiagnosticReadDataByPeriodicIDClass":
        """
        This represents the maximum number of data identifiers that can be included in one request.

        A None value is a no-op and does not overwrite an existing maxPeriodicDidToRead.
        """
        if value is not None:
            self.maxPeriodicDidToRead = value
        return self

    def addPeriodicRate(self, value: Optional[DiagnosticPeriodicRate]) -> "DiagnosticReadDataByPeriodicIDClass":
        """
        This represents the description of a collection of periodic rates in which the service can be executed.

        A None value is a no-op and does not append a periodicRate.
        """
        if value is not None:
            self.periodicRate.append(value)
        return self

    def getPeriodicRates(self) -> List[DiagnosticPeriodicRate]:
        """
        This represents the description of a collection of periodic rates in which the service can be executed.
        """
        return self.periodicRate

    def getSchedulerMaxNumber(self) -> Optional[PositiveInteger]:
        """
        This represents the maximum number of periodic data identifiers that can be scheduled in parallel.
        """
        return self.schedulerMaxNumber

    def setSchedulerMaxNumber(self, value: Optional[PositiveInteger]) -> "DiagnosticReadDataByPeriodicIDClass":
        """
        This represents the maximum number of periodic data identifiers that can be scheduled in parallel.

        A None value is a no-op and does not overwrite an existing schedulerMaxNumber.
        """
        if value is not None:
            self.schedulerMaxNumber = value
        return self


class DiagnosticReadMemoryByAddressClass(DiagnosticServiceClass):
    """This meta-class contains attributes shared by all instances of the "Read Memory by Address" diagnostic service."""

    # DiagnosticReadMemoryByAddressClass method parity checklist:
    # Spec: AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf, Table 4.116, p.142
    # Columns: impl / docstring / test / reader / writer / release   ([—] = no XML element)
    # [x] __init__  [x] impl  [x] docstring  [x] test  [—] reader  [—] writer  R23-11

    def __init__(self, parent: ARObject, short_name: str):
        super().__init__(parent, short_name)


class DiagnosticReadScalingDataByIdentifierClass(DiagnosticServiceClass):
    """This meta-class contains attributes shared by all instances of the "Read Scaling Data by Identifier" diagnostic service."""

    # DiagnosticReadScalingDataByIdentifierClass method parity checklist:
    # Spec: AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf, Table 4.79, p.116
    # Columns: impl / docstring / test / reader / writer / release   ([—] = no XML element)
    # [x] __init__           [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11

    def __init__(self, parent: ARObject, short_name: str):
        super().__init__(parent, short_name)


class DiagnosticRequestControlOfOnBoardDeviceClass(DiagnosticServiceClass):
    pass


class DiagnosticRequestCurrentPowertrainDataClass(DiagnosticServiceClass):
    """This meta-class represents the ability to define common properties for all instances of the "Request current Powertrain Data" OBD diagnostic service."""

    # DiagnosticRequestCurrentPowertrainDataClass method parity checklist:
    # Spec: AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf, Table 4.131, p.151
    # Columns: impl / docstring / test / reader / writer / release   ([—] = no XML element)
    # [x] __init__  [x] impl  [x] docstring  [x] test  [—] reader  [—] writer  R23-11

    def __init__(self, parent: ARObject, short_name: str):
        super().__init__(parent, short_name)


class DiagnosticRequestDownloadClass(DiagnosticServiceClass):
    """This meta-class contains attributes shared by all instances of the "Request Download" diagnostic service."""

    # DiagnosticRequestDownloadClass method parity checklist:
    # Spec: AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf, Table 4.122, p.145
    # Columns: impl / docstring / test / reader / writer / release   ([—] = no XML element)
    # [x] __init__  [x] impl  [x] docstring  [x] test  [—] reader  [—] writer  R23-11

    def __init__(self, parent: ARObject, short_name: str):
        super().__init__(parent, short_name)


class DiagnosticRequestEmissionRelatedDTCClass(DiagnosticServiceClass):
    """This meta-class represents the ability to define common properties for all instances of the "Request Emission Related DTC" OBD diagnostic service."""

    # DiagnosticRequestEmissionRelatedDTCClass method parity checklist:
    # Spec: AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf, Table 4.136, p.154
    # Columns: impl / docstring / test / reader / writer / release   ([—] = no XML element)
    # [x] __init__  [x] impl  [x] docstring  [x] test  [—] reader  [—] writer  R23-11

    def __init__(self, parent: ARObject, short_name: str):
        super().__init__(parent, short_name)


class DiagnosticRequestEmissionRelatedDTCPermanentStatusClass(DiagnosticServiceClass):
    pass


class DiagnosticRequestFileTransferClass(DiagnosticServiceClass):
    """This meta-class contains attributes shared by all instances of the "Request File transfer" diagnostic service."""

    # DiagnosticRequestFileTransferClass method parity checklist:
    # Spec: AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf, Table 4.126, p.147
    # Columns: impl / docstring / test / reader / writer / release   ([—] = no XML element)
    # [x] __init__  [x] impl  [x] docstring  [x] test  [—] reader  [—] writer  R23-11

    def __init__(self, parent: ARObject, short_name: str):
        super().__init__(parent, short_name)


class DiagnosticRequestOnBoardMonitoringTestResultsClass(DiagnosticServiceClass):
    """This meta-class represents the ability to define common properties for all instances of the "Request On-Board Monitoring Test Results" OBD diagnostic service."""

    # DiagnosticRequestOnBoardMonitoringTestResultsClass method parity checklist:
    # Spec: AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf, Table 4.140, p.157
    # Columns: impl / docstring / test / reader / writer / release   ([—] = no XML element)
    # [x] __init__  [x] impl  [x] docstring  [x] test  [—] reader  [—] writer  R23-11

    def __init__(self, parent: ARObject, short_name: str):
        super().__init__(parent, short_name)


class DiagnosticRequestPowertrainFreezeFrameDataClass(DiagnosticServiceClass):
    """This meta-class represents the ability to define common properties for all instances of the "Request Powertrain Freeze Frame Data" OBD diagnostic service."""

    # DiagnosticRequestPowertrainFreezeFrameDataClass method parity checklist:
    # Spec: AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf, Table 4.133, p.152
    # Columns: impl / docstring / test / reader / writer / release   ([—] = no XML element)
    # [x] __init__  [x] impl  [x] docstring  [x] test  [—] reader  [—] writer  R23-11

    def __init__(self, parent: ARObject, short_name: str):
        super().__init__(parent, short_name)


class DiagnosticRequestUploadClass(DiagnosticServiceClass):
    """This meta-class contains attributes shared by all instances of the "Request Upload" diagnostic service."""

    # DiagnosticRequestUploadClass method parity checklist:
    # Spec: AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf, Table 4.124, p.146
    # Columns: impl / docstring / test / reader / writer / release   ([—] = no XML element)
    # [x] __init__  [x] impl  [x] docstring  [x] test  [—] reader  [—] writer  R23-11

    def __init__(self, parent: ARObject, short_name: str):
        super().__init__(parent, short_name)


class DiagnosticRequestVehicleInfoClass(DiagnosticServiceClass):
    pass


class DiagnosticResponseOnEventClass(DiagnosticServiceClass):
    """This represents the ability to define common properties for all instances of the "Response on Event" diagnostic service."""

    # DiagnosticResponseOnEventClass method parity checklist:
    # Spec: AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf, Table 4.102, p.133
    # Columns: impl / docstring / test / reader / writer / release   ([—] = no XML element)
    # [x] __init__                                        [x] impl  [x] docstring  [x] test  [—] reader  [—] writer  R23-11
    # [x] getMaxNumChangeOfDataIdentfierEvents            [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setMaxNumChangeOfDataIdentfierEvents            [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getMaxNumComparisionOfValueEvents               [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setMaxNumComparisionOfValueEvents               [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getMaxNumberOfStoredDTCStatusChangedEvents      [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setMaxNumberOfStoredDTCStatusChangedEvents      [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getMaxSupportedDIDLength                        [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setMaxSupportedDIDLength                        [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getResponseOnEventSchedulerRate                 [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setResponseOnEventSchedulerRate                 [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getStoreEventEnabled                            [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setStoreEventEnabled                            [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11

    def __init__(self, parent: ARObject, short_name: str):
        super().__init__(parent, short_name)

        # The maximum number of DTCs that can be stored as DTCs with change status within one ResponseOnEventSchedulerRate interval.
        self.maxNumberOfStoredDTCStatusChangedEvents: Optional[PositiveInteger] = None

        # The maximum number of events that can be simultaneously configured with sub function onChangeOfDataIdentifier.
        self.maxNumChangeOfDataIdentfierEvents: Optional[PositiveInteger] = None

        # The maximum number of events that can be simultaneously configured with sub function onComparisonOfValues.
        self.maxNumComparisionOfValueEvents: Optional[PositiveInteger] = None

        # The maximum number of measurable data bytes allowed for each DID that is used for comparison or data change.
        self.maxSupportedDIDLength: Optional[PositiveInteger] = None

        # The call rate of the periodic scheduler to compare the values of the DataIdentifier (DID) or to detect DTC status changes.
        self.responseOnEventSchedulerRate: Optional[TimeValue] = None

        # Specifies if the storeEvent functionality of the Response OnEvent diagnostic service shall be supported or not. If set to true, the storeEvent functionality is available. If set to false the storeEvent functionality is not available.
        self.storeEventEnabled: Optional[Boolean] = None

    def getMaxNumChangeOfDataIdentfierEvents(self) -> Optional[PositiveInteger]:
        """
        The maximum number of events that can be simultaneously configured with sub function onChangeOfDataIdentifier.
        """
        return self.maxNumChangeOfDataIdentfierEvents

    def setMaxNumChangeOfDataIdentfierEvents(self, value: Optional[PositiveInteger]) -> "DiagnosticResponseOnEventClass":
        """
        The maximum number of events that can be simultaneously configured with sub function onChangeOfDataIdentifier.

        A None value is a no-op and does not overwrite an existing maxNumChangeOfDataIdentfierEvents.
        """
        if value is not None:
            self.maxNumChangeOfDataIdentfierEvents = value
        return self

    def getMaxNumComparisionOfValueEvents(self) -> Optional[PositiveInteger]:
        """
        The maximum number of events that can be simultaneously configured with sub function onComparisonOfValues.
        """
        return self.maxNumComparisionOfValueEvents

    def setMaxNumComparisionOfValueEvents(self, value: Optional[PositiveInteger]) -> "DiagnosticResponseOnEventClass":
        """
        The maximum number of events that can be simultaneously configured with sub function onComparisonOfValues.

        A None value is a no-op and does not overwrite an existing maxNumComparisionOfValueEvents.
        """
        if value is not None:
            self.maxNumComparisionOfValueEvents = value
        return self

    def getMaxNumberOfStoredDTCStatusChangedEvents(self) -> Optional[PositiveInteger]:
        """
        The maximum number of DTCs that can be stored as DTCs with change status within one ResponseOnEventSchedulerRate interval.
        """
        return self.maxNumberOfStoredDTCStatusChangedEvents

    def setMaxNumberOfStoredDTCStatusChangedEvents(self, value: Optional[PositiveInteger]) -> "DiagnosticResponseOnEventClass":
        """
        The maximum number of DTCs that can be stored as DTCs with change status within one ResponseOnEventSchedulerRate interval.

        A None value is a no-op and does not overwrite an existing maxNumberOfStoredDTCStatusChangedEvents.
        """
        if value is not None:
            self.maxNumberOfStoredDTCStatusChangedEvents = value
        return self

    def getMaxSupportedDIDLength(self) -> Optional[PositiveInteger]:
        """
        The maximum number of measurable data bytes allowed for each DID that is used for comparison or data change.
        """
        return self.maxSupportedDIDLength

    def setMaxSupportedDIDLength(self, value: Optional[PositiveInteger]) -> "DiagnosticResponseOnEventClass":
        """
        The maximum number of measurable data bytes allowed for each DID that is used for comparison or data change.

        A None value is a no-op and does not overwrite an existing maxSupportedDIDLength.
        """
        if value is not None:
            self.maxSupportedDIDLength = value
        return self

    def getResponseOnEventSchedulerRate(self) -> Optional[TimeValue]:
        """
        The call rate of the periodic scheduler to compare the values of the DataIdentifier (DID) or to detect DTC status changes.
        """
        return self.responseOnEventSchedulerRate

    def setResponseOnEventSchedulerRate(self, value: Optional[TimeValue]) -> "DiagnosticResponseOnEventClass":
        """
        The call rate of the periodic scheduler to compare the values of the DataIdentifier (DID) or to detect DTC status changes.

        A None value is a no-op and does not overwrite an existing responseOnEventSchedulerRate.
        """
        if value is not None:
            self.responseOnEventSchedulerRate = value
        return self

    def getStoreEventEnabled(self) -> Optional[Boolean]:
        """
        Specifies if the storeEvent functionality of the Response OnEvent diagnostic service shall be supported or not. If set to true, the storeEvent functionality is available. If set to false the storeEvent functionality is not available.
        """
        return self.storeEventEnabled

    def setStoreEventEnabled(self, value: Optional[Boolean]) -> "DiagnosticResponseOnEventClass":
        """
        Specifies if the storeEvent functionality of the Response OnEvent diagnostic service shall be supported or not. If set to true, the storeEvent functionality is available. If set to false the storeEvent functionality is not available.

        A None value is a no-op and does not overwrite an existing storeEventEnabled.
        """
        if value is not None:
            self.storeEventEnabled = value
        return self


class DiagnosticRoutineControlClass(DiagnosticServiceClass):
    """This meta-class contains attributes shared by all instances of the "Routine Control" diagnostic service."""

    # DiagnosticRoutineControlClass method parity checklist:
    # Spec: AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf, Table 4.90, p.126
    # Columns: impl / docstring / test / reader / writer / release   ([—] = no XML element)
    # [x] __init__  [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11

    def __init__(self, parent: ARObject, short_name: str):
        super().__init__(parent, short_name)


class DiagnosticSecurityAccessClass(DiagnosticServiceClass):
    """This meta-class contains attributes shared by all instances of the "Security Access" diagnostic service."""

    # DiagnosticSecurityAccessClass method parity checklist:
    # Spec: AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf, Table 4.50, p.96
    # Columns: impl / docstring / test / reader / writer / release   ([—] = no XML element)
    # [x] __init__  [x] impl  [x] docstring  [x] test  [—] reader  [—] writer  R23-11

    def __init__(self, parent: ARObject, short_name: str):
        super().__init__(parent, short_name)


class DiagnosticSessionControlClass(DiagnosticServiceClass):
    """
    This meta-class contains attributes shared by all instances of the "Session Control" diagnostic service.

    [constr_10440] Restriction for the minimum value of attribute DiagnosticSessionControlClass.s3ServerTimeout: The value of attribute DiagnosticSessionControlClass.s3ServerTimeout shall be greater than or equal to 5.0 at the time when the DEXT is complete.
    """

    # DiagnosticSessionControlClass method parity checklist:
    # Spec: AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf, Table 4.48, p.93
    # Columns: impl / docstring / test / reader / writer / release   ([—] = no XML element)
    # [x] __init__            [x] impl  [x] docstring  [x] test  [—] reader  [—] writer  R23-11
    # [x] getS3ServerTimeout  [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setS3ServerTimeout  [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11

    def __init__(self, parent: ARObject, short_name: str):
        super().__init__(parent, short_name)

        # Time for the server to keep a diagnostic session other than the default session active while not receiving any diagnostic request message.
        self.s3ServerTimeout: Optional[TimeValue] = None

    def getS3ServerTimeout(self) -> Optional[TimeValue]:
        """
        Time for the server to keep a diagnostic session other than the default session active while not receiving any diagnostic request message.
        """
        return self.s3ServerTimeout

    def setS3ServerTimeout(self, value: Optional[TimeValue]):
        """
        Time for the server to keep a diagnostic session other than the default session active while not receiving any diagnostic request message.

        A None value is a no-op and does not overwrite an existing s3ServerTimeout.
        """
        if value is not None:
            self.s3ServerTimeout = value
        return self


class DiagnosticTransferExitClass(DiagnosticServiceClass):
    """This meta-class contains attributes shared by all instances of the "Transfer Exit" diagnostic service."""

    # DiagnosticTransferExitClass method parity checklist:
    # Spec: AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf, Table 4.118, p.143
    # Columns: impl / docstring / test / reader / writer / release   ([—] = no XML element)
    # [x] __init__  [x] impl  [x] docstring  [x] test  [—] reader  [—] writer  R23-11

    def __init__(self, parent: ARObject, short_name: str):
        super().__init__(parent, short_name)


class DiagnosticWriteDataByIdentifierClass(DiagnosticServiceClass):
    """This meta-class contains attributes shared by all instances of the "Write Data by Identifier" diagnostic service."""

    # DiagnosticWriteDataByIdentifierClass method parity checklist:
    # Spec: AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf, Table 4.72, p.113
    # Columns: impl / docstring / test / reader / writer / release   ([—] = no XML element)
    # [x] __init__           [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11

    def __init__(self, parent: ARObject, short_name: str):
        super().__init__(parent, short_name)


class DiagnosticWriteMemoryByAddressClass(DiagnosticServiceClass):
    """This meta-class contains attributes shared by all instances of the "Write Memory by Address" diagnostic service."""

    # DiagnosticWriteMemoryByAddressClass method parity checklist:
    # Spec: AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf, Table 4.114, p.141
    # Columns: impl / docstring / test / reader / writer / release   ([—] = no XML element)
    # [x] __init__  [x] impl  [x] docstring  [x] test  [—] reader  [—] writer  R23-11

    def __init__(self, parent: ARObject, short_name: str):
        super().__init__(parent, short_name)
