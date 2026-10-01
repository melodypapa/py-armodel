from abc import ABC
from typing import List, Optional

from armodel.models.M2.AUTOSARTemplates.DiagnosticExtract.CommonDiagnostics import DiagnosticCommonElement
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import ARObject, DiagnosticComControlSpecificChannel, DiagnosticComControlSubNodeChannel
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import Boolean, DiagnosticResponseToEcuResetEnum, PositiveInteger, RefType, TimeValue


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
    pass


class DiagnosticClearResetEmissionRelatedInfoClass(DiagnosticServiceClass):
    pass


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
    pass


class DiagnosticDynamicallyDefineDataIdentifierClass(DiagnosticServiceClass):
    pass


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
    pass


class DiagnosticReadDTCInformationClass(DiagnosticServiceClass):
    pass


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
    pass


class DiagnosticReadMemoryByAddressClass(DiagnosticServiceClass):
    pass


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
    pass


class DiagnosticRequestEmissionRelatedDTCClass(DiagnosticServiceClass):
    pass


class DiagnosticRequestEmissionRelatedDTCPermanentStatusClass(DiagnosticServiceClass):
    pass


class DiagnosticRequestFileTransferClass(DiagnosticServiceClass):
    pass


class DiagnosticRequestPowertrainFreezeFrameDataClass(DiagnosticServiceClass):
    pass


class DiagnosticRequestUploadClass(DiagnosticServiceClass):
    pass


class DiagnosticRequestVehicleInfoClass(DiagnosticServiceClass):
    pass


class DiagnosticResponseOnEventClass(DiagnosticServiceClass):
    pass


class DiagnosticRoutineControlClass(DiagnosticServiceClass):
    pass


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
    pass


class DiagnosticWriteDataByIdentifierClass(DiagnosticServiceClass):
    """This meta-class contains attributes shared by all instances of the "Write Data by Identifier" diagnostic service."""

    # DiagnosticWriteDataByIdentifierClass method parity checklist:
    # Spec: AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf, Table 4.72, p.113
    # Columns: impl / docstring / test / reader / writer / release   ([—] = no XML element)
    # [x] __init__           [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11

    def __init__(self, parent: ARObject, short_name: str):
        super().__init__(parent, short_name)


class DiagnosticWriteMemoryByAddressClass(DiagnosticServiceClass):
    pass
