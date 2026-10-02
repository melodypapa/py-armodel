"""
This module contains classes for representing AUTOSAR service needs structures
in the CommonStructure module. Service needs define requirements for various
services such as NV block management, diagnostic services, cryptographic services, etc.
"""

from __future__ import annotations
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.StereotypeMixins import VariationPointCapable

from abc import ABC
from typing import List, Optional, TYPE_CHECKING

if TYPE_CHECKING:
    from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.SwcInternalBehavior.ServiceMapping import RoleBasedDataTypeAssignment
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import ARObject
from armodel.models.M2.AUTOSARTemplates.CommonStructure.Implementation import ImplementationProps
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable import Identifiable
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import Identifier, RefType, AREnum, Boolean
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import DiagRequirementIdString, Integer, PositiveInteger
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import NameToken
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import String, TimeValue


class RoleBasedDataAssignment(ARObject, VariationPointCapable):
    """
    This class specifies an assignment of a role to a particular data object in either • the SwcInternalBehavior of a software component (or in the BswInternalBehavior of a BSW module or BSW cluster) in the context of an AUTOSAR Service or • an NvBlockDescriptor to sort out the assignment of event-based writing strategies to data elements in a PortPrototype. With this assignment, the role of the data can be mapped to a DataPrototype that is used in the context of the definition of a specific ServiceNeeds or NvBlockDescriptor, so that a tool is able to create the correct access or writing strategy.
    """

    # RoleBasedDataAssignment method parity checklist:
    # Spec: AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.pdf, Table 12.4, p.227 (sibling rendering: AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf, Table 7.55, p.607)
    # Spec verified: R23-11
    # Columns: impl / docstring / test / reader / writer / release   ([—] = no XML element)
    # [x] __init__                [x] impl  [x] docstring  [x] test  [—] reader  [—] writer  R23-11
    # [x] getRole                 [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setRole                 [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getUsedDataElement      [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setUsedDataElement      [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getUsedParameterElement [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setUsedParameterElement [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getUsedPimRef           [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setUsedPimRef           [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11

    def __init__(self):
        super().__init__()

        # This is the role of the assigned data in the given context. Possible values need to be specified on M1 level. Additionally the TPS Software Component Template provides a list of applicable roles for various service dependencies and service use cases in chapter 13 "Service Dependencies and Service Use Cases" (e.g., ramBlock in case of the needs for a permanent RAM block).
        self.role: Optional[Identifier] = None

        # The VariableDataPrototype used in this role, e.g. • Permanent RAM Block of an NVRAM Block which shall belong to the same SwcInternalBehavior or BswInternalBehavior. • In the role signalBasedDiagnostics it has to refer to a VariableDataPrototype in a SenderReceiverInterface or a NvDataInterface.
        self.usedDataElement: Optional[AutosarVariableRef] = None

        # The ParameterDataPrototype used in this role, e.g. • ROM Block of an NVRAM Block. It shall belong to the same SwcInternalBehavior or BswInternalbehavior. • In the role signalBasedDiagnostics it has to refer to a ParameterDataPrototype in a ParameterInterface.
        self.usedParameterElement: Optional[AutosarParameterRef] = None

        # The (untyped) PerInstanceMemory used in this role (e.g. as a Permanent RAM Block for an NVRAM Block).
        self.usedPimRef: Optional[RefType] = None

    def getRole(self) -> Optional[Identifier]:
        """
        This is the role of the assigned data in the given context. Possible values need to be specified on M1 level. Additionally the TPS Software Component Template provides a list of applicable roles for various service dependencies and service use cases in chapter 13 "Service Dependencies and Service Use Cases" (e.g., ramBlock in case of the needs for a permanent RAM block).
        """
        return self.role

    def setRole(self, value: Optional[Identifier]) -> RoleBasedDataAssignment:
        """
        This is the role of the assigned data in the given context. Possible values need to be specified on M1 level. Additionally the TPS Software Component Template provides a list of applicable roles for various service dependencies and service use cases in chapter 13 "Service Dependencies and Service Use Cases" (e.g., ramBlock in case of the needs for a permanent RAM block). A None value is a no-op and does not overwrite an existing role.
        """
        if value is not None:
            self.role = value
        return self

    def getUsedDataElement(self) -> Optional[AutosarVariableRef]:
        """
        The VariableDataPrototype used in this role, e.g. • Permanent RAM Block of an NVRAM Block which shall belong to the same SwcInternalBehavior or BswInternalBehavior. • In the role signalBasedDiagnostics it has to refer to a VariableDataPrototype in a SenderReceiverInterface or a NvDataInterface.
        """
        return self.usedDataElement

    def setUsedDataElement(self, value: Optional[AutosarVariableRef]) -> RoleBasedDataAssignment:
        """
        The VariableDataPrototype used in this role, e.g. • Permanent RAM Block of an NVRAM Block which shall belong to the same SwcInternalBehavior or BswInternalBehavior. • In the role signalBasedDiagnostics it has to refer to a VariableDataPrototype in a SenderReceiverInterface or a NvDataInterface. A None value is a no-op and does not overwrite an existing usedDataElement.
        """
        if value is not None:
            self.usedDataElement = value
        return self

    def getUsedParameterElement(self) -> Optional[AutosarParameterRef]:
        """
        The ParameterDataPrototype used in this role, e.g. • ROM Block of an NVRAM Block. It shall belong to the same SwcInternalBehavior or BswInternalbehavior. • In the role signalBasedDiagnostics it has to refer to a ParameterDataPrototype in a ParameterInterface.
        """
        return self.usedParameterElement

    def setUsedParameterElement(self, value: Optional[AutosarParameterRef]) -> RoleBasedDataAssignment:
        """
        The ParameterDataPrototype used in this role, e.g. • ROM Block of an NVRAM Block. It shall belong to the same SwcInternalBehavior or BswInternalbehavior. • In the role signalBasedDiagnostics it has to refer to a ParameterDataPrototype in a ParameterInterface. A None value is a no-op and does not overwrite an existing usedParameterElement.
        """
        if value is not None:
            self.usedParameterElement = value
        return self

    def getUsedPimRef(self) -> Optional[RefType]:
        """
        The (untyped) PerInstanceMemory used in this role (e.g. as a Permanent RAM Block for an NVRAM Block).
        """
        return self.usedPimRef

    def setUsedPimRef(self, value: Optional[RefType]) -> RoleBasedDataAssignment:
        """
        The (untyped) PerInstanceMemory used in this role (e.g. as a Permanent RAM Block for an NVRAM Block). A None value is a no-op and does not overwrite an existing usedPimRef.
        """
        if value is not None:
            self.usedPimRef = value
        return self


class ServiceNeeds(Identifiable, ABC):
    """
    This expresses the abstract needs that a Software Component or Basic Software Module has on the configuration of an AUTOSAR Service to which it will be connected. "Abstract needs" means that the model abstracts from the Configuration Parameters of the underlying Basic Software.
    """

    # ServiceNeeds method parity checklist:
    # Spec: AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.pdf, Table 12.6, p.228 (class Note: sibling copy AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf, Table 7.52, p.603)
    # Spec verified: R23-11
    # Columns: impl / docstring / test / reader / writer / release   ([—] = no XML element)
    # [x] __init__                     [x] impl  [x] docstring  [x] test  [—] reader  [—] writer  R23-11

    def __init__(self, parent: ARObject, short_name: str):
        if type(self) is ServiceNeeds:
            raise TypeError("ServiceNeeds is an abstract class.")

        super().__init__(parent, short_name)


class RamBlockStatusControlEnum(AREnum):
    """
    This enumeration type defines options for how the management of the ramBlock status is controlled.
    """

    # RamBlockStatusControlEnum method parity checklist:
    # Spec: AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf, Table 13.1, p.701
    # Spec verified: R23-11
    # Columns: impl / docstring / test / reader / writer / release   ([—] = no XML element)
    # [x] __init__                     [x] impl  [x] docstring  [x] test  [—] reader  [—] writer  R23-11

    # The ramBlock status is controlled via service interface by usage of the SetRamBlockStatus operation. Tags: atp.EnumerationLiteralIndex=0
    API = "api"

    # The ramBlock status is controlled exclusively by the Nv Ram Manager. Tags: atp.EnumerationLiteralIndex=1
    NV_RAM_MANAGER = "nvRamManager"

    def __init__(self):
        super().__init__(
            (
                RamBlockStatusControlEnum.API,
                RamBlockStatusControlEnum.NV_RAM_MANAGER,
            )
        )


class NvBlockNeedsReliabilityEnum(AREnum):
    """
    Reliability against data loss on the non-volatile medium. These requirements give only a relative indication, for example on the required degree of redundancy for storage. They do, however, not specify by which means (e.g. software or hardware) the reliability is actually achieved.
    """

    # NvBlockNeedsReliabilityEnum method parity checklist:
    # Spec: AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf, Table 11.10, p.681
    # Spec verified: R23-11
    # Columns: impl / docstring / test / reader / writer / release   ([—] = no XML element)
    # [x] __init__                     [x] impl  [x] docstring  [x] test  [—] reader  [—] writer  R23-11

    # Errors shall be corrected Tags: atp.EnumerationLiteralIndex=0
    ERROR_CORRECTION = "errorCorrection"

    # Errors shall be detected Tags: atp.EnumerationLiteralIndex=1
    ERROR_DETECTION = "errorDetection"

    # Data need not to be handled with protection Tags: atp.EnumerationLiteralIndex=2
    NO_PROTECTION = "noProtection"

    def __init__(self):
        super().__init__(
            (
                NvBlockNeedsReliabilityEnum.ERROR_CORRECTION,
                NvBlockNeedsReliabilityEnum.ERROR_DETECTION,
                NvBlockNeedsReliabilityEnum.NO_PROTECTION,
            )
        )


class NvBlockNeedsWritingPriorityEnum(AREnum):
    """
    Specifies the priority of writing this block in case of concurrent requests to write other blocks.
    """

    # NvBlockNeedsWritingPriorityEnum method parity checklist:
    # Spec: AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf, Table 11.9, p.680
    # Spec verified: R23-11
    # Columns: impl / docstring / test / reader / writer / release   ([—] = no XML element)
    # [x] __init__                     [x] impl  [x] docstring  [x] test  [—] reader  [—] writer  R23-11

    # Writing priority is high. Tags: atp.EnumerationLiteralIndex=0
    HIGH = "high"

    # Writing priority is low. Tags: atp.EnumerationLiteralIndex=1
    LOW = "low"

    # Writing priority is medium. Tags: atp.EnumerationLiteralIndex=2
    MEDIUM = "medium"

    def __init__(self):
        super().__init__(
            (
                NvBlockNeedsWritingPriorityEnum.HIGH,
                NvBlockNeedsWritingPriorityEnum.LOW,
                NvBlockNeedsWritingPriorityEnum.MEDIUM,
            )
        )


class NvBlockNeeds(ServiceNeeds):
    """
    Specifies the abstract needs on the configuration of a single NVRAM Block.

    [constr_1308] Existence of NvBlockNeeds.cyclicWritingPeriod: The attribute NvBlockNeeds.cyclicWritingPeriod shall exist if and only if the attribute NvBlockNeeds.storeCyclic exists and its value is set to true.

    [constr_1310] Existence of attributes of meta-class NvBlockNeeds: If in the context of an ApplicationSwComponentType the attribute SwcServiceDependency.serviceNeeds is implemented by an NvBlockNeeds then the following attributes NvBlockNeeds.storeCyclic, NvBlockNeeds.cyclicWritingPeriod, NvBlockNeeds.storeEmergency, NvBlockNeeds.storeImmediate, NvBlockNeeds.storeOnChange shall only exist if in the context of the same SwcServiceDependency a SwcServiceDependency.assignedPort exists that has the attribute role set to the value NvDataPort.
    """

    # NvBlockNeeds method parity checklist:
    # Spec: AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf, Table 11.8, p.680 (twin rendering: AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.pdf, Table 12.7, p.232)
    # Spec verified: R23-11
    # Columns: impl / docstring / test / reader / writer / release   ([—] = no XML element)
    # [x] __init__                        [x] impl  [x] docstring  [x] test  [—] reader  [—] writer  R23-11
    # [x] getCalcRamBlockCrc              [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setCalcRamBlockCrc              [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getCheckStaticBlockId           [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setCheckStaticBlockId           [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getCyclicWritingPeriod          [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setCyclicWritingPeriod          [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getNDataSets                    [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setNDataSets                    [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getNRomBlocks                   [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setNRomBlocks                   [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getRamBlockStatusControl        [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setRamBlockStatusControl        [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getReadonly                     [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setReadonly                     [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getReliability                  [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setReliability                  [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getResistantToChangedSw         [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setResistantToChangedSw         [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getRestoreAtStart               [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setRestoreAtStart               [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getSelectBlockForFirstInitAll   [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setSelectBlockForFirstInitAll   [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getStoreAtShutdown              [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setStoreAtShutdown              [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getStoreCyclic                  [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setStoreCyclic                  [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getStoreEmergency               [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setStoreEmergency               [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getStoreImmediate               [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setStoreImmediate               [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getStoreOnChange                [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setStoreOnChange                [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getUseAutoValidationAtShutDown  [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setUseAutoValidationAtShutDown  [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getUseCRCCompMechanism          [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setUseCRCCompMechanism          [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getWriteOnlyOnce                [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setWriteOnlyOnce                [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getWriteVerification            [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setWriteVerification            [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getWritingFrequency             [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setWritingFrequency             [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getWritingPriority              [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setWritingPriority              [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11

    def __init__(self, parent: ARObject, short_name: str):
        super().__init__(parent, short_name)

        # Defines if CRC (re)calculation for the permanent RAM Block is required.
        self.calcRamBlockCrc: Optional[Boolean] = None

        # Defines if the Static Block Id check shall be enabled.
        self.checkStaticBlockId: Optional[Boolean] = None

        # This represents the period for cyclic writing of NvData to store the associated RAM Block.
        self.cyclicWritingPeriod: Optional[TimeValue] = None

        # Number of data sets to be provided by the NVRAM manager for this block. This is the total number of ROM Blocks and RAM Blocks.
        self.nDataSets: Optional[PositiveInteger] = None

        # Number of ROM Blocks to be provided by the NVRAM manager for this block. Please note that these multiple ROM Blocks are given in a contiguous area.
        self.nRomBlocks: Optional[PositiveInteger] = None

        # This attribute defines how the management of the RAM Block status is controlled.
        self.ramBlockStatusControl: Optional[RamBlockStatusControlEnum] = None

        # true: data of this NVRAM Block are write protected for normal operation (but protection can be disabled) false: no restriction
        self.readonly: Optional[Boolean] = None

        # Reliability against data loss on the non-volatile medium.
        self.reliability: Optional[NvBlockNeedsReliabilityEnum] = None

        # Defines whether an NVRAM Block shall be treated resistant to configuration changes (true) or not (false). For details how to handle initialization in the latter case, please refer to the NVRAM specification.
        self.resistantToChangedSw: Optional[Boolean] = None

        # Defines whether the associated RAM Block shall be implicitly restored during startup by the basic software.
        self.restoreAtStart: Optional[Boolean] = None

        # If this attribute is set to true the NvM shall process this block in the NvM_FirstInitAll() function.
        self.selectBlockForFirstInitAll: Optional[Boolean] = None

        # Defines whether or not the associated RAM Block shall be implicitly stored during shutdown by the basic software.
        self.storeAtShutdown: Optional[Boolean] = None

        # Defines whether or not the associated RAM Block shall be implicitly stored periodically by the basic software.
        self.storeCyclic: Optional[Boolean] = None

        # Defines whether or not the associated RAM Block shall be implicitly stored in case of ECU failure (e.g. loss of power) by the basic software. If the attribute storeEmergency is set to true the associated RAM Block shall be configured to have immediate priority.
        self.storeEmergency: Optional[Boolean] = None

        # Defines whether or not the associated RAM Block shall be implicitly stored immediately during or after execution of the according SW-C RunnableEntity by the basic software.
        self.storeImmediate: Optional[Boolean] = None

        # This attribute defines whether the associated RAM Block shall be stored immediately if the written value is different to the value stored in the associated RAM Block(s) during or after execution of the according SW-C RunnableEntity.
        self.storeOnChange: Optional[Boolean] = None

        # If set to true the RAM Block shall be auto validated during shutdown phase.
        self.useAutoValidationAtShutDown: Optional[Boolean] = None

        # If set to true the CRC of the RAM Block shall be compared during a write job with the CRC which was calculated during the last successful read or write job in order to skip unnecessary NVRAM writings.
        self.useCRCCompMechanism: Optional[Boolean] = None

        # Defines write protection after first write: true: This block is prevented from being changed/erased or being replaced with the default ROM data after first initialization by the software-component. false: No such restriction.
        self.writeOnlyOnce: Optional[Boolean] = None

        # Defines if Write Verification shall be enabled for this NVRAM Block.
        self.writeVerification: Optional[Boolean] = None

        # Provides the amount of updates to this block from the application point of view. It has to be provided in "number of write access per year".
        self.writingFrequency: Optional[PositiveInteger] = None

        # Requires the priority of writing this block in case of concurrent requests to write other blocks.
        self.writingPriority: Optional[NvBlockNeedsWritingPriorityEnum] = None

    def getCalcRamBlockCrc(self) -> Optional[Boolean]:
        """
        Defines if CRC (re)calculation for the permanent RAM Block is required.
        """
        return self.calcRamBlockCrc

    def setCalcRamBlockCrc(self, value: Optional[Boolean]) -> NvBlockNeeds:
        """
        Defines if CRC (re)calculation for the permanent RAM Block is required. A None value is a no-op and does not overwrite an existing calcRamBlockCrc.
        """
        if value is not None:
            self.calcRamBlockCrc = value
        return self

    def getCheckStaticBlockId(self) -> Optional[Boolean]:
        """
        Defines if the Static Block Id check shall be enabled.
        """
        return self.checkStaticBlockId

    def setCheckStaticBlockId(self, value: Optional[Boolean]) -> NvBlockNeeds:
        """
        Defines if the Static Block Id check shall be enabled. A None value is a no-op and does not overwrite an existing checkStaticBlockId.
        """
        if value is not None:
            self.checkStaticBlockId = value
        return self

    def getCyclicWritingPeriod(self) -> Optional[TimeValue]:
        """
        This represents the period for cyclic writing of NvData to store the associated RAM Block.
        """
        return self.cyclicWritingPeriod

    def setCyclicWritingPeriod(self, value: Optional[TimeValue]) -> NvBlockNeeds:
        """
        This represents the period for cyclic writing of NvData to store the associated RAM Block. A None value is a no-op and does not overwrite an existing cyclicWritingPeriod.
        """
        if value is not None:
            self.cyclicWritingPeriod = value
        return self

    def getNDataSets(self) -> Optional[PositiveInteger]:
        """
        Number of data sets to be provided by the NVRAM manager for this block. This is the total number of ROM Blocks and RAM Blocks.
        """
        return self.nDataSets

    def setNDataSets(self, value: Optional[PositiveInteger]) -> NvBlockNeeds:
        """
        Number of data sets to be provided by the NVRAM manager for this block. This is the total number of ROM Blocks and RAM Blocks. A None value is a no-op and does not overwrite an existing nDataSets.
        """
        if value is not None:
            self.nDataSets = value
        return self

    def getNRomBlocks(self) -> Optional[PositiveInteger]:
        """
        Number of ROM Blocks to be provided by the NVRAM manager for this block. Please note that these multiple ROM Blocks are given in a contiguous area.
        """
        return self.nRomBlocks

    def setNRomBlocks(self, value: Optional[PositiveInteger]) -> NvBlockNeeds:
        """
        Number of ROM Blocks to be provided by the NVRAM manager for this block. Please note that these multiple ROM Blocks are given in a contiguous area. A None value is a no-op and does not overwrite an existing nRomBlocks.
        """
        if value is not None:
            self.nRomBlocks = value
        return self

    def getRamBlockStatusControl(self) -> Optional[RamBlockStatusControlEnum]:
        """
        This attribute defines how the management of the RAM Block status is controlled.
        """
        return self.ramBlockStatusControl

    def setRamBlockStatusControl(self, value: Optional[RamBlockStatusControlEnum]) -> NvBlockNeeds:
        """
        This attribute defines how the management of the RAM Block status is controlled. A None value is a no-op and does not overwrite an existing ramBlockStatusControl.
        """
        if value is not None:
            self.ramBlockStatusControl = value
        return self

    def getReadonly(self) -> Optional[Boolean]:
        """
        true: data of this NVRAM Block are write protected for normal operation (but protection can be disabled) false: no restriction
        """
        return self.readonly

    def setReadonly(self, value: Optional[Boolean]) -> NvBlockNeeds:
        """
        true: data of this NVRAM Block are write protected for normal operation (but protection can be disabled) false: no restriction A None value is a no-op and does not overwrite an existing readonly.
        """
        if value is not None:
            self.readonly = value
        return self

    def getReliability(self) -> Optional[NvBlockNeedsReliabilityEnum]:
        """
        Reliability against data loss on the non-volatile medium.
        """
        return self.reliability

    def setReliability(self, value: Optional[NvBlockNeedsReliabilityEnum]) -> NvBlockNeeds:
        """
        Reliability against data loss on the non-volatile medium. A None value is a no-op and does not overwrite an existing reliability.
        """
        if value is not None:
            self.reliability = value
        return self

    def getResistantToChangedSw(self) -> Optional[Boolean]:
        """
        Defines whether an NVRAM Block shall be treated resistant to configuration changes (true) or not (false). For details how to handle initialization in the latter case, please refer to the NVRAM specification.
        """
        return self.resistantToChangedSw

    def setResistantToChangedSw(self, value: Optional[Boolean]) -> NvBlockNeeds:
        """
        Defines whether an NVRAM Block shall be treated resistant to configuration changes (true) or not (false). For details how to handle initialization in the latter case, please refer to the NVRAM specification. A None value is a no-op and does not overwrite an existing resistantToChangedSw.
        """
        if value is not None:
            self.resistantToChangedSw = value
        return self

    def getRestoreAtStart(self) -> Optional[Boolean]:
        """
        Defines whether the associated RAM Block shall be implicitly restored during startup by the basic software.
        """
        return self.restoreAtStart

    def setRestoreAtStart(self, value: Optional[Boolean]) -> NvBlockNeeds:
        """
        Defines whether the associated RAM Block shall be implicitly restored during startup by the basic software. A None value is a no-op and does not overwrite an existing restoreAtStart.
        """
        if value is not None:
            self.restoreAtStart = value
        return self

    def getSelectBlockForFirstInitAll(self) -> Optional[Boolean]:
        """
        If this attribute is set to true the NvM shall process this block in the NvM_FirstInitAll() function.
        """
        return self.selectBlockForFirstInitAll

    def setSelectBlockForFirstInitAll(self, value: Optional[Boolean]) -> NvBlockNeeds:
        """
        If this attribute is set to true the NvM shall process this block in the NvM_FirstInitAll() function. A None value is a no-op and does not overwrite an existing selectBlockForFirstInitAll.
        """
        if value is not None:
            self.selectBlockForFirstInitAll = value
        return self

    def getStoreAtShutdown(self) -> Optional[Boolean]:
        """
        Defines whether or not the associated RAM Block shall be implicitly stored during shutdown by the basic software.
        """
        return self.storeAtShutdown

    def setStoreAtShutdown(self, value: Optional[Boolean]) -> NvBlockNeeds:
        """
        Defines whether or not the associated RAM Block shall be implicitly stored during shutdown by the basic software. A None value is a no-op and does not overwrite an existing storeAtShutdown.
        """
        if value is not None:
            self.storeAtShutdown = value
        return self

    def getStoreCyclic(self) -> Optional[Boolean]:
        """
        Defines whether or not the associated RAM Block shall be implicitly stored periodically by the basic software.
        """
        return self.storeCyclic

    def setStoreCyclic(self, value: Optional[Boolean]) -> NvBlockNeeds:
        """
        Defines whether or not the associated RAM Block shall be implicitly stored periodically by the basic software. A None value is a no-op and does not overwrite an existing storeCyclic.
        """
        if value is not None:
            self.storeCyclic = value
        return self

    def getStoreEmergency(self) -> Optional[Boolean]:
        """
        Defines whether or not the associated RAM Block shall be implicitly stored in case of ECU failure (e.g. loss of power) by the basic software. If the attribute storeEmergency is set to true the associated RAM Block shall be configured to have immediate priority.
        """
        return self.storeEmergency

    def setStoreEmergency(self, value: Optional[Boolean]) -> NvBlockNeeds:
        """
        Defines whether or not the associated RAM Block shall be implicitly stored in case of ECU failure (e.g. loss of power) by the basic software. If the attribute storeEmergency is set to true the associated RAM Block shall be configured to have immediate priority. A None value is a no-op and does not overwrite an existing storeEmergency.
        """
        if value is not None:
            self.storeEmergency = value
        return self

    def getStoreImmediate(self) -> Optional[Boolean]:
        """
        Defines whether or not the associated RAM Block shall be implicitly stored immediately during or after execution of the according SW-C RunnableEntity by the basic software.
        """
        return self.storeImmediate

    def setStoreImmediate(self, value: Optional[Boolean]) -> NvBlockNeeds:
        """
        Defines whether or not the associated RAM Block shall be implicitly stored immediately during or after execution of the according SW-C RunnableEntity by the basic software. A None value is a no-op and does not overwrite an existing storeImmediate.
        """
        if value is not None:
            self.storeImmediate = value
        return self

    def getStoreOnChange(self) -> Optional[Boolean]:
        """
        This attribute defines whether the associated RAM Block shall be stored immediately if the written value is different to the value stored in the associated RAM Block(s) during or after execution of the according SW-C RunnableEntity.
        """
        return self.storeOnChange

    def setStoreOnChange(self, value: Optional[Boolean]) -> NvBlockNeeds:
        """
        This attribute defines whether the associated RAM Block shall be stored immediately if the written value is different to the value stored in the associated RAM Block(s) during or after execution of the according SW-C RunnableEntity. A None value is a no-op and does not overwrite an existing storeOnChange.
        """
        if value is not None:
            self.storeOnChange = value
        return self

    def getUseAutoValidationAtShutDown(self) -> Optional[Boolean]:
        """
        If set to true the RAM Block shall be auto validated during shutdown phase.
        """
        return self.useAutoValidationAtShutDown

    def setUseAutoValidationAtShutDown(self, value: Optional[Boolean]) -> NvBlockNeeds:
        """
        If set to true the RAM Block shall be auto validated during shutdown phase. A None value is a no-op and does not overwrite an existing useAutoValidationAtShutDown.
        """
        if value is not None:
            self.useAutoValidationAtShutDown = value
        return self

    def getUseCRCCompMechanism(self) -> Optional[Boolean]:
        """
        If set to true the CRC of the RAM Block shall be compared during a write job with the CRC which was calculated during the last successful read or write job in order to skip unnecessary NVRAM writings.
        """
        return self.useCRCCompMechanism

    def setUseCRCCompMechanism(self, value: Optional[Boolean]) -> NvBlockNeeds:
        """
        If set to true the CRC of the RAM Block shall be compared during a write job with the CRC which was calculated during the last successful read or write job in order to skip unnecessary NVRAM writings. A None value is a no-op and does not overwrite an existing useCRCCompMechanism.
        """
        if value is not None:
            self.useCRCCompMechanism = value
        return self

    def getWriteOnlyOnce(self) -> Optional[Boolean]:
        """
        Defines write protection after first write: true: This block is prevented from being changed/erased or being replaced with the default ROM data after first initialization by the software-component. false: No such restriction.
        """
        return self.writeOnlyOnce

    def setWriteOnlyOnce(self, value: Optional[Boolean]) -> NvBlockNeeds:
        """
        Defines write protection after first write: true: This block is prevented from being changed/erased or being replaced with the default ROM data after first initialization by the software-component. false: No such restriction. A None value is a no-op and does not overwrite an existing writeOnlyOnce.
        """
        if value is not None:
            self.writeOnlyOnce = value
        return self

    def getWriteVerification(self) -> Optional[Boolean]:
        """
        Defines if Write Verification shall be enabled for this NVRAM Block.
        """
        return self.writeVerification

    def setWriteVerification(self, value: Optional[Boolean]) -> NvBlockNeeds:
        """
        Defines if Write Verification shall be enabled for this NVRAM Block. A None value is a no-op and does not overwrite an existing writeVerification.
        """
        if value is not None:
            self.writeVerification = value
        return self

    def getWritingFrequency(self) -> Optional[PositiveInteger]:
        """
        Provides the amount of updates to this block from the application point of view. It has to be provided in "number of write access per year".
        """
        return self.writingFrequency

    def setWritingFrequency(self, value: Optional[PositiveInteger]) -> NvBlockNeeds:
        """
        Provides the amount of updates to this block from the application point of view. It has to be provided in "number of write access per year". A None value is a no-op and does not overwrite an existing writingFrequency.
        """
        if value is not None:
            self.writingFrequency = value
        return self

    def getWritingPriority(self) -> Optional[NvBlockNeedsWritingPriorityEnum]:
        """
        Requires the priority of writing this block in case of concurrent requests to write other blocks.
        """
        return self.writingPriority

    def setWritingPriority(self, value: Optional[NvBlockNeedsWritingPriorityEnum]) -> NvBlockNeeds:
        """
        Requires the priority of writing this block in case of concurrent requests to write other blocks. A None value is a no-op and does not overwrite an existing writingPriority.
        """
        if value is not None:
            self.writingPriority = value
        return self


class ServiceDiagnosticRelevanceEnum(AREnum):
    """
    This enumeration provides values to describe the diagnostic relevance of a SwcServiceDependency (specifically if the aggregated ServiceNeeds itself does not indicate a relevance for diagnostics).
    """

    # ServiceDiagnosticRelevanceEnum method parity checklist:
    # Spec: AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf, Table 7.58, p.609
    # (no methods)

    # This value indicates that a relevance for diagnostics does not exist. Tags: atp.EnumerationLiteralIndex=0
    IS_NOT_RELEVANT = "isNotRelevant"

    # This value indicates a relevance for diagnostics. Tags: atp.EnumerationLiteralIndex=1
    IS_RELEVANT = "isRelevant"

    def __init__(self):
        super().__init__(
            (
                ServiceDiagnosticRelevanceEnum.IS_NOT_RELEVANT,
                ServiceDiagnosticRelevanceEnum.IS_RELEVANT,
            )
        )


class ServiceDependency(ARObject, ABC):
    """
    Collects all dependencies of a software module or component on an AUTOSAR
    Service related to a specific item (e.g. an NVRAM Block, a diagnostic event
    etc.). It defines the quality of service (Service Needs) of this item as
    well as (optionally) references to additional elements. This information is
    required for tools in order to generate the related basic software
    configuration and ServiceSwComponentTypes.
    """

    # ServiceDependency method parity checklist:
    # Spec: AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.pdf, Table 12.1, p.225
    # Spec verified: R23-11
    # Columns: impl / docstring / test / reader / writer   ([—] = no XML element)
    # [x] __init__                     [x] impl  [x] docstring  [x] test  [—] reader  [—] writer
    # [x] setAssignedDataType          [x] impl  [x] docstring  [x] test  [x] reader  [—] writer
    # [x] getAssignedDataType         [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] getDiagnosticRelevance       [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] setDiagnosticRelevance       [x] impl  [x] docstring  [x] test  [x] reader  [—] writer
    # [x] getSymbolicNameProps         [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] setSymbolicNameProps         [x] impl  [x] docstring  [x] test  [x] reader  [—] writer

    def __init__(self):
        if type(self) is ServiceDependency:
            raise TypeError("ServiceDependency is an abstract class.")
        super().__init__()

        # This is the role of the assignment data type in the given context. Stereotypes: atpSplitable; atpVariation Tags: atp.Splitkey=assignedDataType, assignedDataType.variationPoint.shortLabel vh.latestBindingTime=preCompileTime
        self.assignedDataType: Optional[RoleBasedDataTypeAssignment] = None

        # If this attribute indicates a relevance for diagnostics then the integrator has a much easier time identifying the candidates for the configuration of the diagnostic stack. Example: identification of mode conditions (e.g. communication between application and BswM) relevant for the Dcm.
        self.diagnosticRelevance: Optional[ServiceDiagnosticRelevanceEnum] = None

        # This attribute can be taken to contribute to the creation of symbolic name values.
        self.symbolicNameProps: Optional[SymbolicNameProps] = None

    def getAssignedDataType(self) -> Optional[RoleBasedDataTypeAssignment]:
        """
        This is the role of the assignment data type in the given context. Stereotypes: atpSplitable; atpVariation Tags: atp.Splitkey=assignedDataType, assignedDataType.variationPoint.shortLabel vh.latestBindingTime=preCompileTime

        Returns:
            The RoleBasedDataTypeAssignment instance
        """
        return self.assignedDataType

    def setAssignedDataType(self, value: Optional[RoleBasedDataTypeAssignment]) -> ServiceDependency:
        """
        This is the role of the assignment data type in the given context. Stereotypes: atpSplitable; atpVariation Tags: atp.Splitkey=assignedDataType, assignedDataType.variationPoint.shortLabel vh.latestBindingTime=preCompileTime
        Only sets the value if it is not None.

        Args:
            value: The role-based data type assignment to set

        Returns:
            self for method chaining
        """
        if value is not None:
            self.assignedDataType = value
        return self

    def getDiagnosticRelevance(self) -> Optional[ServiceDiagnosticRelevanceEnum]:
        """
        If this attribute indicates a relevance for diagnostics then the integrator has a much easier time identifying the candidates for the configuration of the diagnostic stack. Example: identification of mode conditions (e.g. communication between application and BswM) relevant for the Dcm.
        """
        return self.diagnosticRelevance

    def setDiagnosticRelevance(self, value: Optional[ServiceDiagnosticRelevanceEnum]) -> ServiceDependency:
        """
        If this attribute indicates a relevance for diagnostics then the integrator has a much easier time identifying the candidates for the configuration of the diagnostic stack. Example: identification of mode conditions (e.g. communication between application and BswM) relevant for the Dcm.
        Only sets the value if it is not None.

        Args:
            value: The diagnostic relevance to set

        Returns:
            self for method chaining
        """
        if value is not None:
            self.diagnosticRelevance = value
        return self

    def getSymbolicNameProps(self) -> Optional[SymbolicNameProps]:
        """
        This attribute can be taken to contribute to the creation of symbolic name values.
        """
        return self.symbolicNameProps

    def setSymbolicNameProps(self, value: Optional[SymbolicNameProps]) -> ServiceDependency:
        """
        This attribute can be taken to contribute to the creation of symbolic name values.
        Only sets the value if it is not None.

        Args:
            value: The symbolic name properties to set

        Returns:
            self for method chaining
        """
        if value is not None:
            self.symbolicNameProps = value
        return self


class DiagnosticAudienceEnum(AREnum):
    """
    The possible values of the intended audience for a diagnostic object.
    """

    # DiagnosticAudienceEnum method parity checklist:
    # Spec: AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf, Table 13.17, p.754
    # Spec verified: R23-11
    # Columns: impl / docstring / test / reader / writer / release   ([—] = no XML element)
    # (no methods) — enum value form serialized on DiagnosticCapabilityElement.audience (Steps 5/6 N/A: standalone AREnum)
    # [x] __init__                     [x] impl  [x] docstring  [x] test  [—] reader  [—] writer  R23-11

    # The object is for free aftermarket service organizations. Tags: atp.EnumerationLiteralIndex=1
    AFTER_MARKET = "aftermarket"

    # The object is relevant for the OEM after-sales organization. Tags: atp.EnumerationLiteralIndex=2
    AFTER_SALES = "afterSales"

    # The object is relevant for engineering only. Tags: atp.EnumerationLiteralIndex=3
    DEVELOPMENT = "development"

    # The object is relevant for manufacturing. Tags: atp.EnumerationLiteralIndex=4
    MANUFACTURING = "manufacturing"

    # The object is relevant for the ECU-supplier aftermarket organization. Tags: atp.EnumerationLiteralIndex=5
    SUPPLIER = "supplier"

    def __init__(self):
        super().__init__(
            (
                DiagnosticAudienceEnum.AFTER_MARKET,
                DiagnosticAudienceEnum.AFTER_SALES,
                DiagnosticAudienceEnum.DEVELOPMENT,
                DiagnosticAudienceEnum.MANUFACTURING,
                DiagnosticAudienceEnum.SUPPLIER,
            )
        )


class DiagnosticServiceRequestCallbackTypeEnum(AREnum):
    """
    This represents the ability to define whether a Service Request Notification was used in the role of a manufacturer or a supplier.
    """

    # DiagnosticServiceRequestCallbackTypeEnum method parity checklist:
    # Spec: AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf, Table 13.35, p.780
    # Spec verified: R23-11
    # Columns: impl / docstring / test / reader / writer / release   ([—] = no XML element)
    # (no methods) — enum value form serialized on DiagnosticCommunicationManagerNeeds.serviceRequestCallbackType (Steps 5/6 N/A: standalone AREnum)
    # [x] __init__                     [x] impl  [x] docstring  [x] test  [—] reader  [—] writer  R23-11

    # This represents the case that the usage of PortInterface ServiceRequestNotification has the characteristics of being used by a manufacturer. Tags: atp.EnumerationLiteralIndex=0
    REQUEST_CALLBACK_TYPE_MANUFACTURER = "requestCallbackTypeManufacturer"

    # This represents the case that the usage of PortInterface ServiceRequestNotification has the characteristics of being used by a supplier. Tags: atp.EnumerationLiteralIndex=1
    REQUEST_CALLBACK_TYPE_SUPPLIER = "requestCallbackTypeSupplier"

    def __init__(self):
        super().__init__(
            (
                DiagnosticServiceRequestCallbackTypeEnum.REQUEST_CALLBACK_TYPE_MANUFACTURER,
                DiagnosticServiceRequestCallbackTypeEnum.REQUEST_CALLBACK_TYPE_SUPPLIER,
            )
        )


class DiagnosticCapabilityElement(ServiceNeeds, ABC):
    """
    This class identifies the capability to provide generic information about diagnostic capabilities
    """

    # DiagnosticCapabilityElement method parity checklist:
    # Spec: AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf, Table 13.15, p.753
    # Columns: impl / docstring / test / reader / writer / release   ([—] = no XML element)
    # [x] __init__                 [x] impl  [x] docstring  [x] test  [—] reader  [—] writer  R23-11
    # [x] getAudiences             [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] addAudience              [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getDiagRequirement       [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setDiagRequirement       [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getSecurityAccessLevel   [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setSecurityAccessLevel   [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11

    def __init__(self, parent: ARObject, short_name: str):
        if type(self) is DiagnosticCapabilityElement:
            raise TypeError("DiagnosticCapabilityElement is an abstract class.")

        super().__init__(parent, short_name)

        # This specifies the intended audience for the diagnostic object. Note that this is not only for the documentation but also subsequent audience specific implementation.
        self.audiences: List[DiagnosticAudienceEnum] = []

        # This denotes the requirement identifier to which the object can be linked to. Note that with the implementation of a generic tracing concept in AUTOSAR this attribute might become obsolete.
        self.diagRequirement: Optional[DiagRequirementIdString] = None

        # This attribute denotes the level of security which is touched by the diagnostic object. The higher the level the more relevance for the security exists. This level shall be mapped to the security level in the ECU.
        self.securityAccessLevel: Optional[PositiveInteger] = None

    def getAudiences(self) -> List[DiagnosticAudienceEnum]:
        """
        This specifies the intended audience for the diagnostic object. Note that this is not only for the documentation but also subsequent audience specific implementation.
        """
        return self.audiences

    def addAudience(self, value: Optional[DiagnosticAudienceEnum]) -> DiagnosticCapabilityElement:
        """
        This specifies the intended audience for the diagnostic object. Note that this is not only for the documentation but also subsequent audience specific implementation.
        A None value is a no-op and does not modify the existing audiences.
        """
        if value is not None:
            self.audiences.append(value)
        return self

    def getDiagRequirement(self) -> Optional[DiagRequirementIdString]:
        """
        This denotes the requirement identifier to which the object can be linked to. Note that with the implementation of a generic tracing concept in AUTOSAR this attribute might become obsolete.
        """
        return self.diagRequirement

    def setDiagRequirement(self, value: Optional[DiagRequirementIdString]) -> DiagnosticCapabilityElement:
        """
        This denotes the requirement identifier to which the object can be linked to. Note that with the implementation of a generic tracing concept in AUTOSAR this attribute might become obsolete.
        A None value is a no-op and does not overwrite an existing diagRequirement.
        """
        if value is not None:
            self.diagRequirement = value
        return self

    def getSecurityAccessLevel(self) -> Optional[PositiveInteger]:
        """
        This attribute denotes the level of security which is touched by the diagnostic object. The higher the level the more relevance for the security exists. This level shall be mapped to the security level in the ECU.
        """
        return self.securityAccessLevel

    def setSecurityAccessLevel(self, value: Optional[PositiveInteger]) -> DiagnosticCapabilityElement:
        """
        This attribute denotes the level of security which is touched by the diagnostic object. The higher the level the more relevance for the security exists. This level shall be mapped to the security level in the ECU.
        A None value is a no-op and does not overwrite an existing securityAccessLevel.
        """
        if value is not None:
            self.securityAccessLevel = value
        return self


class DiagnosticRoutineTypeEnum(AREnum):
    """
    This enumerator specifies the different types of diagnostic routines.
    """

    # DiagnosticRoutineTypeEnum method parity checklist:
    # Spec: AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.pdf, Table 12.25, p.247
    # Spec verified: R23-11
    # Columns: impl / docstring / test / reader / writer / release   ([—] = no XML element)
    # (no methods) — enum value form serialized on DiagnosticRoutineNeeds.diagRoutineType (Steps 5/6 N/A: standalone AREnum)
    # [x] __init__                     [x] impl  [x] docstring  [x] test  [—] reader  [—] writer  R23-11

    # This indicates that the diagnostic server is not blocked while the diagnostic routine is running. Tags: atp.EnumerationLiteralIndex=0
    ASYNCHRONOUS = "asynchronous"

    # This indicates that the diagnostic routine blocks the diagnostic server in the ECU while the routine is running. Tags: atp.EnumerationLiteralIndex=1
    SYNCHRONOUS = "synchronous"

    def __init__(self):
        super().__init__(
            (
                DiagnosticRoutineTypeEnum.ASYNCHRONOUS,
                DiagnosticRoutineTypeEnum.SYNCHRONOUS,
            )
        )


class DiagnosticCommunicationManagerNeeds(DiagnosticCapabilityElement):
    """
    Specifies the general needs on the configuration of the Diagnostic Communication Manager (Dcm) which are not related to a particular item (e.g. a PID or DiagnosticRoutineNeeds). The main use case is the mapping of service ports to the Dcm which are not related to a particular item.
    """

    # DiagnosticCommunicationManagerNeeds method parity checklist:
    # Spec: AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf, Table 13.34, p.777
    # Columns: impl / docstring / test / reader / writer / release   ([—] = no XML element)
    # [x] __init__                        [x] impl  [x] docstring  [x] test  [—] reader  [—] writer  R23-11
    # [x] getServiceRequestCallbackType   [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setServiceRequestCallbackType   [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11

    def __init__(self, parent: ARObject, short_name: str):
        super().__init__(parent, short_name)

        # This represents the ability to define whether the usage of PortInterface ServiceRequestNotification has the characteristics of being initiated by a manufacturer or by a supplier.
        self.serviceRequestCallbackType: Optional[DiagnosticServiceRequestCallbackTypeEnum] = None

    def getServiceRequestCallbackType(self) -> Optional[DiagnosticServiceRequestCallbackTypeEnum]:
        """
        This represents the ability to define whether the usage of PortInterface ServiceRequestNotification has the characteristics of being initiated by a manufacturer or by a supplier.
        """
        return self.serviceRequestCallbackType

    def setServiceRequestCallbackType(self, value: Optional[DiagnosticServiceRequestCallbackTypeEnum]) -> DiagnosticCommunicationManagerNeeds:
        """
        This represents the ability to define whether the usage of PortInterface ServiceRequestNotification has the characteristics of being initiated by a manufacturer or by a supplier.
        A None value is a no-op and does not overwrite an existing serviceRequestCallbackType.
        """
        if value is not None:
            self.serviceRequestCallbackType = value
        return self


class DiagnosticRoutineNeeds(DiagnosticCapabilityElement):
    """
    Specifies the general needs on the configuration of the Diagnostic Communication Manager (Dcm) which are not related to a particular item (e.g. a PID). The main use case is the mapping of service ports to the Dcm which are not related to a particular item.
    """

    # DiagnosticRoutineNeeds method parity checklist:
    # Spec: AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf, Table 13.36, p.778 (R23-11)
    # Spec: R4.3.1/AUTOSAR_TPS_SoftwareComponentTemplate.pdf (R4.3.1)
    # Columns: impl / docstring / test / reader / writer / release   ([—] = no XML element)
    # [x] __init__                 [x] impl  [x] docstring  [x] test  [—] reader  [—] writer  R23-11
    # [x] getDiagRoutineType       [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setDiagRoutineType       [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getRidNumber             [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R4.3.1
    # [x] setRidNumber             [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R4.3.1

    def __init__(self, parent: ARObject, short_name: str):
        super().__init__(parent, short_name)

        # This denotes the type of diagnostic routine which is implemented by the referenced server port.
        self.diagRoutineType: Optional[DiagnosticRoutineTypeEnum] = None

        # This represents a routine identifier for the diagnostic routine. This allows to predefine the RID number if the a function developer has received a particular requirement from the OEM or from a standardization body.
        self.ridNumber: Optional[PositiveInteger] = None

    def getDiagRoutineType(self) -> Optional[DiagnosticRoutineTypeEnum]:
        """
        This denotes the type of diagnostic routine which is implemented by the referenced server port.
        """
        return self.diagRoutineType

    def setDiagRoutineType(self, value: Optional[DiagnosticRoutineTypeEnum]) -> DiagnosticRoutineNeeds:
        """
        This denotes the type of diagnostic routine which is implemented by the referenced server port.
        A None value is a no-op and does not overwrite an existing diagRoutineType.
        """
        if value is not None:
            self.diagRoutineType = value
        return self

    def getRidNumber(self) -> Optional[PositiveInteger]:
        """
        This represents a routine identifier for the diagnostic routine. This allows to predefine the RID number if the a function developer has received a particular requirement from the OEM or from a standardization body.
        """
        return self.ridNumber

    def setRidNumber(self, value: Optional[PositiveInteger]) -> DiagnosticRoutineNeeds:
        """
        This represents a routine identifier for the diagnostic routine. This allows to predefine the RID number if the a function developer has received a particular requirement from the OEM or from a standardization body.
        A None value is a no-op and does not overwrite an existing ridNumber.
        """
        if value is not None:
            self.ridNumber = value
        return self


class DiagnosticValueAccessEnum(AREnum):
    """
    Defines the access of the configured diagnostic current values which will be used by the Dem or Dcm module.
    """

    # DiagnosticValueAccessEnum method parity checklist:
    # Spec: AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.pdf, Table 12.22, p.246
    # (no methods)

    # The access to the data element is limited to read-only. This is typically used to read-out diagnostic information (e.g. current values). Tags: atp.EnumerationLiteralIndex=0
    READ_ONLY = "readOnly"

    # The value of the diagnostic data element is classified as configurable (read and write access is possible). Tags: atp.EnumerationLiteralIndex=1
    READ_WRITE = "readWrite"

    # The access to the data element is limited to write-only. This supports the use case where the Dcm just writes data to the application software without the intention to read it back, Tags: atp.EnumerationLiteralIndex=2
    WRITE_ONLY = "writeOnly"

    def __init__(self):
        super().__init__(
            (
                DiagnosticValueAccessEnum.READ_ONLY,
                DiagnosticValueAccessEnum.READ_WRITE,
                DiagnosticValueAccessEnum.WRITE_ONLY,
            )
        )


class DiagnosticProcessingStyleEnum(AREnum):
    """
    This meta-class represents the ability to define the processing style of diagnostic requests.
    """

    # DiagnosticProcessingStyleEnum method parity checklist:
    # Spec: AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.pdf, Table 12.23, p.247
    # Spec verified: R23-11
    # Columns: impl / docstring / test / reader / writer / release   ([—] = no XML element)
    # (no methods) — enum value form serialized on DiagnosticValueNeeds.processingStyle (Steps 5/6 N/A: standalone AREnum)
    # [x] __init__                     [x] impl  [x] docstring  [x] test  [—] reader  [—] writer  R23-11

    # The software-component processes the request in background but still the Dcm has to issue the call again to eventually obtain the result of the request. Tags: atp.EnumerationLiteralIndex=0
    PROCESSING_STYLE_ASYNCHRONOUS = "processingStyleAsynchronous"

    # The software-component processes the request in background but still the Dcm has to issue the call again to eventually obtain the result of the request or handle error code. Tags: atp.EnumerationLiteralIndex=1
    PROCESSING_STYLE_ASYNCHRONOUS_WITH_ERROR = "processingStyleAsynchronousWithError"

    # The software-component is supposed to react synchronously on the request. Tags: atp.EnumerationLiteralIndex=2
    PROCESSING_STYLE_SYNCHRONOUS = "processingStyleSynchronous"

    def __init__(self):
        super().__init__(
            (
                DiagnosticProcessingStyleEnum.PROCESSING_STYLE_ASYNCHRONOUS,
                DiagnosticProcessingStyleEnum.PROCESSING_STYLE_ASYNCHRONOUS_WITH_ERROR,
                DiagnosticProcessingStyleEnum.PROCESSING_STYLE_SYNCHRONOUS,
            )
        )


class DiagnosticValueNeeds(DiagnosticCapabilityElement):
    """
    Specifies the general needs on the configuration of the Diagnostic Communication Manager (DCM) which are not related to a particular item (e.g. a PID). The main use case is the mapping of service ports to the DCM which are not related to a particular item. In the case of using a sender receiver communicated value, the related value shall be taken via assigned Data in the role "signalBasedDiagnostics". In case of using a client/server communicated value, the related value shall be communicated via the port referenced by assignedPort. The details of this communication (e.g. appropriate naming conventions) are specified in the related software specifications (SWS).
    """

    # DiagnosticValueNeeds method parity checklist:
    # Spec: AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf, Table 13.39, p.780 (R23-11)
    # Spec: R4.3.1/AUTOSAR_TPS_SoftwareComponentTemplate.pdf (R4.3.1)
    # Columns: impl / docstring / test / reader / writer / release   ([—] = no XML element)
    # [x] __init__                     [x] impl  [x] docstring  [x] test  [—] reader  [—] writer  R23-11
    # [x] getDataLength                [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setDataLength                [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getDiagnosticValueAccess     [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setDiagnosticValueAccess     [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getDidNumber                 [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R4.3.1
    # [x] setDidNumber                 [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R4.3.1
    # [x] getFixedLength               [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setFixedLength               [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getProcessingStyle           [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setProcessingStyle           [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11

    def __init__(self, parent: ARObject, short_name: str):
        super().__init__(parent, short_name)

        # This attribute is applicable only if the DiagnosticValueNeeds is aggregated within a BswModuleDependency. This attribute represents the length of data (in bytes) provided for this particular PID signal.
        self.dataLength: Optional[PositiveInteger] = None

        # This attribute is applicable only if the DiagnosticValueNeeds is aggregated within a BswModuleDependency. This attribute controls whether the data can be read and written or whether it is to be handled read-only.
        self.diagnosticValueAccess: Optional[DiagnosticValueAccessEnum] = None

        # This represents a Data identifier for the diagnostic value. This allows to predefine the DID number if the responsible function developer has received a particular requirement from the OEM or from a standardization body.
        self.didNumber: Optional[PositiveInteger] = None

        # This attribute is applicable only if the DiagnosticValueNeeds is aggregated within a BswModuleDependency. This attribute controls whether the data length of the data is fixed.
        self.fixedLength: Optional[Boolean] = None

        # This attribute controls whether interaction requires the software-component to react synchronously on a request or whether it processes the request in background but still the DCM has to issue the call again to eventually obtain the result of the request.
        self.processingStyle: Optional[DiagnosticProcessingStyleEnum] = None

    def getDataLength(self) -> Optional[PositiveInteger]:
        """
        This attribute is applicable only if the DiagnosticValueNeeds is aggregated within a BswModuleDependency. This attribute represents the length of data (in bytes) provided for this particular PID signal.
        """
        return self.dataLength

    def setDataLength(self, value: Optional[PositiveInteger]) -> DiagnosticValueNeeds:
        """
        This attribute is applicable only if the DiagnosticValueNeeds is aggregated within a BswModuleDependency. This attribute represents the length of data (in bytes) provided for this particular PID signal.
        A None value is a no-op and does not overwrite an existing dataLength.
        """
        if value is not None:
            self.dataLength = value
        return self

    def getDiagnosticValueAccess(self) -> Optional[DiagnosticValueAccessEnum]:
        """
        This attribute is applicable only if the DiagnosticValueNeeds is aggregated within a BswModuleDependency. This attribute controls whether the data can be read and written or whether it is to be handled read-only.
        """
        return self.diagnosticValueAccess

    def setDiagnosticValueAccess(self, value: Optional[DiagnosticValueAccessEnum]) -> DiagnosticValueNeeds:
        """
        This attribute is applicable only if the DiagnosticValueNeeds is aggregated within a BswModuleDependency. This attribute controls whether the data can be read and written or whether it is to be handled read-only.
        A None value is a no-op and does not overwrite an existing diagnosticValueAccess.
        """
        if value is not None:
            self.diagnosticValueAccess = value
        return self

    def getDidNumber(self) -> Optional[PositiveInteger]:
        """
        This represents a Data identifier for the diagnostic value. This allows to predefine the DID number if the responsible function developer has received a particular requirement from the OEM or from a standardization body.
        """
        return self.didNumber

    def setDidNumber(self, value: Optional[PositiveInteger]) -> DiagnosticValueNeeds:
        """
        This represents a Data identifier for the diagnostic value. This allows to predefine the DID number if the responsible function developer has received a particular requirement from the OEM or from a standardization body.
        A None value is a no-op and does not overwrite an existing didNumber.
        """
        if value is not None:
            self.didNumber = value
        return self

    def getFixedLength(self) -> Optional[Boolean]:
        """
        This attribute is applicable only if the DiagnosticValueNeeds is aggregated within a BswModuleDependency. This attribute controls whether the data length of the data is fixed.
        """
        return self.fixedLength

    def setFixedLength(self, value: Optional[Boolean]) -> DiagnosticValueNeeds:
        """
        This attribute is applicable only if the DiagnosticValueNeeds is aggregated within a BswModuleDependency. This attribute controls whether the data length of the data is fixed.
        A None value is a no-op and does not overwrite an existing fixedLength.
        """
        if value is not None:
            self.fixedLength = value
        return self

    def getProcessingStyle(self) -> Optional[DiagnosticProcessingStyleEnum]:
        """
        This attribute controls whether interaction requires the software-component to react synchronously on a request or whether it processes the request in background but still the DCM has to issue the call again to eventually obtain the result of the request.
        """
        return self.processingStyle

    def setProcessingStyle(self, value: Optional[DiagnosticProcessingStyleEnum]) -> DiagnosticValueNeeds:
        """
        This attribute controls whether interaction requires the software-component to react synchronously on a request or whether it processes the request in background but still the DCM has to issue the call again to eventually obtain the result of the request.
        A None value is a no-op and does not overwrite an existing processingStyle.
        """
        if value is not None:
            self.processingStyle = value
        return self


class DiagEventDebounceAlgorithm(Identifiable, ABC):
    """
    This class represents the ability to specify the pre-debounce algorithm which is selected and/or required by the particular monitor. This class inherits from Identifiable in order to allow further documentation of the expected or implemented debouncing and to use the category for the identification of the expected / implemented debouncing.
    """

    # DiagEventDebounceAlgorithm method parity checklist:
    # Spec: AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.pdf, Table 12.32, p.259
    # Spec verified: R23-11
    # Columns: impl / docstring / test / reader / writer / release   ([—] = no XML element)
    # [x] __init__                     [x] impl  [x] docstring  [x] test  [—] reader  [—] writer  R23-11

    def __init__(self, parent: ARObject, short_name: str):
        if type(self) is DiagEventDebounceAlgorithm:
            raise TypeError("DiagEventDebounceAlgorithm is an abstract class.")

        super().__init__(parent, short_name)


class DiagEventDebounceCounterBased(DiagEventDebounceAlgorithm):
    """
    This meta-class represents the ability to indicate that the counter-based debounce algorithm shall be used by the DEM for this diagnostic monitor. This is related to set the ECUC choice container DemDebounceAlgorithmClass to DemDebounceCounterBased.
    """

    # DiagEventDebounceCounterBased method parity checklist:
    # Spec: AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.pdf, Table 12.33, p.260
    # Columns: impl / docstring / test / reader / writer / release   ([—] = no XML element)
    # [x] __init__                                [x] impl  [x] docstring  [x] test  [—] reader  [—] writer  R23-11
    # [x] getCounterBasedFdcThresholdStorageValue [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setCounterBasedFdcThresholdStorageValue [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getCounterDecrementStepSize             [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setCounterDecrementStepSize             [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getCounterFailedThreshold               [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setCounterFailedThreshold               [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getCounterIncrementStepSize             [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setCounterIncrementStepSize             [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getCounterJumpDown                      [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setCounterJumpDown                      [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getCounterJumpDownValue                 [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setCounterJumpDownValue                 [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getCounterJumpUp                        [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setCounterJumpUp                        [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getCounterJumpUpValue                   [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setCounterJumpUpValue                   [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getCounterPassedThreshold               [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setCounterPassedThreshold               [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11

    def __init__(self, parent: ARObject, short_name: str):
        super().__init__(parent, short_name)

        # Threshold to allocate an event memory entry and to capture the Freeze Frame.
        self.counterBasedFdcThresholdStorageValue: Optional[Integer] = None

        # This value shall be taken to decrement the internal debounce counter. Stereotypes: atpVariation Tags: vh.latestBindingTime=preCompileTime
        self.counterDecrementStepSize: Optional[Integer] = None

        # This value defines the event-specific limit that indicates the "failed" counter status. Stereotypes: atpVariation Tags: vh.latestBindingTime=preCompileTime
        self.counterFailedThreshold: Optional[Integer] = None

        # This value shall be taken to increment the internal debounce counter. Stereotypes: atpVariation Tags: vh.latestBindingTime=preCompileTime
        self.counterIncrementStepSize: Optional[Integer] = None

        # This value activates or deactivates the counter jump-down behavior. Stereotypes: atpVariation Tags: vh.latestBindingTime=preCompileTime
        self.counterJumpDown: Optional[Boolean] = None

        # This value represents the initial value of the internal debounce counter if the counting direction changes from incrementing to decrementing. Stereotypes: atpVariation Tags: vh.latestBindingTime=preCompileTime
        self.counterJumpDownValue: Optional[Integer] = None

        # This value activates or deactivates the counter jump-up behavior. Stereotypes: atpVariation Tags: vh.latestBindingTime=preCompileTime
        self.counterJumpUp: Optional[Boolean] = None

        # This value represents the initial value of the internal debounce counter if the counting direction changes from decrementing to incrementing. Stereotypes: atpVariation Tags: vh.latestBindingTime=preCompileTime
        self.counterJumpUpValue: Optional[Integer] = None

        # This value defines the event-specific limit that indicates the "passed" counter status. Stereotypes: atpVariation Tags: vh.latestBindingTime=preCompileTime
        self.counterPassedThreshold: Optional[Integer] = None

    def getCounterBasedFdcThresholdStorageValue(self) -> Optional[Integer]:
        """
        Threshold to allocate an event memory entry and to capture the Freeze Frame.
        """
        return self.counterBasedFdcThresholdStorageValue

    def setCounterBasedFdcThresholdStorageValue(self, value: Optional[Integer]) -> DiagEventDebounceCounterBased:
        """
        Threshold to allocate an event memory entry and to capture the Freeze Frame.
        A None value is a no-op and does not overwrite an existing counterBasedFdcThresholdStorageValue.
        """
        if value is not None:
            self.counterBasedFdcThresholdStorageValue = value
        return self

    def getCounterDecrementStepSize(self) -> Optional[Integer]:
        """
        This value shall be taken to decrement the internal debounce counter.
        """
        return self.counterDecrementStepSize

    def setCounterDecrementStepSize(self, value: Optional[Integer]) -> DiagEventDebounceCounterBased:
        """
        This value shall be taken to decrement the internal debounce counter.
        A None value is a no-op and does not overwrite an existing counterDecrementStepSize.
        """
        if value is not None:
            self.counterDecrementStepSize = value
        return self

    def getCounterFailedThreshold(self) -> Optional[Integer]:
        """
        This value defines the event-specific limit that indicates the "failed" counter status.
        """
        return self.counterFailedThreshold

    def setCounterFailedThreshold(self, value: Optional[Integer]) -> DiagEventDebounceCounterBased:
        """
        This value defines the event-specific limit that indicates the "failed" counter status.
        A None value is a no-op and does not overwrite an existing counterFailedThreshold.
        """
        if value is not None:
            self.counterFailedThreshold = value
        return self

    def getCounterIncrementStepSize(self) -> Optional[Integer]:
        """
        This value shall be taken to increment the internal debounce counter.
        """
        return self.counterIncrementStepSize

    def setCounterIncrementStepSize(self, value: Optional[Integer]) -> DiagEventDebounceCounterBased:
        """
        This value shall be taken to increment the internal debounce counter.
        A None value is a no-op and does not overwrite an existing counterIncrementStepSize.
        """
        if value is not None:
            self.counterIncrementStepSize = value
        return self

    def getCounterJumpDown(self) -> Optional[Boolean]:
        """
        This value activates or deactivates the counter jump-down behavior.
        """
        return self.counterJumpDown

    def setCounterJumpDown(self, value: Optional[Boolean]) -> DiagEventDebounceCounterBased:
        """
        This value activates or deactivates the counter jump-down behavior.
        A None value is a no-op and does not overwrite an existing counterJumpDown.
        """
        if value is not None:
            self.counterJumpDown = value
        return self

    def getCounterJumpDownValue(self) -> Optional[Integer]:
        """
        This value represents the initial value of the internal debounce counter if the counting direction changes from incrementing to decrementing.
        """
        return self.counterJumpDownValue

    def setCounterJumpDownValue(self, value: Optional[Integer]) -> DiagEventDebounceCounterBased:
        """
        This value represents the initial value of the internal debounce counter if the counting direction changes from incrementing to decrementing.
        A None value is a no-op and does not overwrite an existing counterJumpDownValue.
        """
        if value is not None:
            self.counterJumpDownValue = value
        return self

    def getCounterJumpUp(self) -> Optional[Boolean]:
        """
        This value activates or deactivates the counter jump-up behavior.
        """
        return self.counterJumpUp

    def setCounterJumpUp(self, value: Optional[Boolean]) -> DiagEventDebounceCounterBased:
        """
        This value activates or deactivates the counter jump-up behavior.
        A None value is a no-op and does not overwrite an existing counterJumpUp.
        """
        if value is not None:
            self.counterJumpUp = value
        return self

    def getCounterJumpUpValue(self) -> Optional[Integer]:
        """
        This value represents the initial value of the internal debounce counter if the counting direction changes from decrementing to incrementing.
        """
        return self.counterJumpUpValue

    def setCounterJumpUpValue(self, value: Optional[Integer]) -> DiagEventDebounceCounterBased:
        """
        This value represents the initial value of the internal debounce counter if the counting direction changes from decrementing to incrementing.
        A None value is a no-op and does not overwrite an existing counterJumpUpValue.
        """
        if value is not None:
            self.counterJumpUpValue = value
        return self

    def getCounterPassedThreshold(self) -> Optional[Integer]:
        """
        This value defines the event-specific limit that indicates the "passed" counter status.
        """
        return self.counterPassedThreshold

    def setCounterPassedThreshold(self, value: Optional[Integer]) -> DiagEventDebounceCounterBased:
        """
        This value defines the event-specific limit that indicates the "passed" counter status.
        A None value is a no-op and does not overwrite an existing counterPassedThreshold.
        """
        if value is not None:
            self.counterPassedThreshold = value
        return self


class DiagEventDebounceMonitorInternal(DiagEventDebounceAlgorithm):
    """
    This meta-class represents the ability to indicate that no Dem pre-debounce algorithm shall be used for this diagnostic monitor. The SWC might implement an internal debouncing algorithm and report qualified (debounced) results to the Dem/DM.
    """

    # DiagEventDebounceMonitorInternal method parity checklist:
    # Spec: AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.pdf, Table 12.35, p.260
    # Spec verified: R23-11
    # Columns: impl / docstring / test / reader / writer / release   ([—] = no XML element)
    # [x] __init__                     [x] impl  [x] docstring  [x] test  [—] reader  [—] writer  R23-11

    def __init__(self, parent: ARObject, short_name: str):
        super().__init__(parent, short_name)


class DiagEventDebounceTimeBased(DiagEventDebounceAlgorithm):
    """
    This meta-class represents the ability to indicate that the time-based pre-debounce algorithm shall be used by the Dem for this diagnostic monitor. This is related to set the EcuC choice container DemDebounceAlgorithmClass to DemDebounceTimeBase.
    """

    # DiagEventDebounceTimeBased method parity checklist:
    # Spec: AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.pdf, Table 12.34, p.260
    # Columns: impl / docstring / test / reader / writer / release   ([—] = no XML element)
    # [x] __init__                             [x] impl  [x] docstring  [x] test  [—] reader  [—] writer  R23-11
    # [x] getTimeBasedFdcThresholdStorageValue [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setTimeBasedFdcThresholdStorageValue [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getTimeFailedThreshold               [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setTimeFailedThreshold               [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getTimePassedThreshold               [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setTimePassedThreshold               [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11

    def __init__(self, parent: ARObject, short_name: str):
        super().__init__(parent, short_name)

        # Threshold to allocate an event memory entry and to capture the Freeze Frame. Stereotypes: atpVariation Tags: vh.latestBindingTime=preCompileTime
        self.timeBasedFdcThresholdStorageValue: Optional[TimeValue] = None

        # This value represents the event-specific delay indicating the "failed" status. Stereotypes: atpVariation Tags: vh.latestBindingTime=preCompileTime
        self.timeFailedThreshold: Optional[TimeValue] = None

        # This value represents the event-specific delay indicating the "passed" status. Stereotypes: atpVariation Tags: vh.latestBindingTime=preCompileTime
        self.timePassedThreshold: Optional[TimeValue] = None

    def getTimeBasedFdcThresholdStorageValue(self) -> Optional[TimeValue]:
        """
        Threshold to allocate an event memory entry and to capture the Freeze Frame.
        """
        return self.timeBasedFdcThresholdStorageValue

    def setTimeBasedFdcThresholdStorageValue(self, value: Optional[TimeValue]) -> DiagEventDebounceTimeBased:
        """
        Threshold to allocate an event memory entry and to capture the Freeze Frame.
        A None value is a no-op and does not overwrite an existing timeBasedFdcThresholdStorageValue.
        """
        if value is not None:
            self.timeBasedFdcThresholdStorageValue = value
        return self

    def getTimeFailedThreshold(self) -> Optional[TimeValue]:
        """
        This value represents the event-specific delay indicating the "failed" status.
        """
        return self.timeFailedThreshold

    def setTimeFailedThreshold(self, value: Optional[TimeValue]) -> DiagEventDebounceTimeBased:
        """
        This value represents the event-specific delay indicating the "failed" status.
        A None value is a no-op and does not overwrite an existing timeFailedThreshold.
        """
        if value is not None:
            self.timeFailedThreshold = value
        return self

    def getTimePassedThreshold(self) -> Optional[TimeValue]:
        """
        This value represents the event-specific delay indicating the "passed" status.
        """
        return self.timePassedThreshold

    def setTimePassedThreshold(self, value: Optional[TimeValue]) -> DiagEventDebounceTimeBased:
        """
        This value represents the event-specific delay indicating the "passed" status.
        A None value is a no-op and does not overwrite an existing timePassedThreshold.
        """
        if value is not None:
            self.timePassedThreshold = value
        return self


class DtcKindEnum(AREnum):
    """
    This enumeration defines the possible kinds of diagnostic monitors regarding the OBD relevance.
    """

    # DtcKindEnum method parity checklist:
    # Spec: R4.3.1/AUTOSAR_TPS_SoftwareComponentTemplate.pdf, Table 13.16, p.760 (R4.3.1)
    # (no methods)

    # This indicates that the monitor reports a OBD-relevant malfunction. Tags: atp.EnumerationValue=0
    EMISSION_RELATED_DTC = "emissionRelatedDtc"

    # This indicates that the monitor reports a non-OBD-relevant malfunction. Tags: atp.EnumerationValue=1
    NON_EMMISSION_RELATED_DTC = "nonEmmissionRelatedDtc"

    def __init__(self):
        super().__init__(
            (
                DtcKindEnum.EMISSION_RELATED_DTC,
                DtcKindEnum.NON_EMMISSION_RELATED_DTC,
            )
        )


class DiagnosticEventInfoNeeds(DiagnosticCapabilityElement):
    """
    This meta-class represents the needs of a software-component interested to get information regarding specific DTCs.
    """

    # DiagnosticEventInfoNeeds method parity checklist:
    # Spec: AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf, Table 13.23, p.761 (R23-11)
    # Spec: R4.3.1/AUTOSAR_TPS_SoftwareComponentTemplate.pdf (R4.3.1)
    # Columns: impl / docstring / test / reader / writer / release   ([—] = no XML element)
    # [x] __init__           [x] impl  [x] docstring  [x] test  [—] reader  [—] writer  R23-11
    # [x] getDtcKind         [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R4.3.1
    # [x] setDtcKind         [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R4.3.1
    # [x] getObdDtcNumber    [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setObdDtcNumber    [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getUdsDtcNumber    [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setUdsDtcNumber    [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11

    def __init__(self, parent: ARObject, short_name: str):
        super().__init__(parent, short_name)

        # This attribute indicates the kind of the diagnostic event according to the SWS Diagnostic Event Manger for which the DiagnosticInfo is requested. This attribute applies for the UDS diagnostics use case.
        self.dtcKind: Optional[DtcKindEnum] = None

        # This represents a reasonable Diagnostic Trouble Code. This allows to predefine the Diagnostic Trouble Code, e.g. if the function developer has received a particular requirement from the OEM or from a standardization body. This attribute applies for the OBD diagnostics use case.
        self.obdDtcNumber: Optional[PositiveInteger] = None

        # This represents a reasonable Diagnostic Trouble Code. This allows to predefine the Diagnostic Trouble Code, e.g. if the function developer has received a particular requirement from the OEM or from a standardization body. This attribute applies for the UDS diagnostics use case.
        self.udsDtcNumber: Optional[PositiveInteger] = None

    def getDtcKind(self) -> Optional[DtcKindEnum]:
        """
        This attribute indicates the kind of the diagnostic event according to the SWS Diagnostic Event Manger for which the DiagnosticInfo is requested. This attribute applies for the UDS diagnostics use case.
        """
        return self.dtcKind

    def setDtcKind(self, value: Optional[DtcKindEnum]) -> DiagnosticEventInfoNeeds:
        """
        This attribute indicates the kind of the diagnostic event according to the SWS Diagnostic Event Manger for which the DiagnosticInfo is requested. This attribute applies for the UDS diagnostics use case.
        A None value is a no-op and does not overwrite an existing dtcKind.
        """
        if value is not None:
            self.dtcKind = value
        return self

    def getObdDtcNumber(self) -> Optional[PositiveInteger]:
        """
        This represents a reasonable Diagnostic Trouble Code. This allows to predefine the Diagnostic Trouble Code, e.g. if the function developer has received a particular requirement from the OEM or from a standardization body. This attribute applies for the OBD diagnostics use case.
        """
        return self.obdDtcNumber

    def setObdDtcNumber(self, value: Optional[PositiveInteger]) -> DiagnosticEventInfoNeeds:
        """
        This represents a reasonable Diagnostic Trouble Code. This allows to predefine the Diagnostic Trouble Code, e.g. if the function developer has received a particular requirement from the OEM or from a standardization body. This attribute applies for the OBD diagnostics use case.
        A None value is a no-op and does not overwrite an existing obdDtcNumber.
        """
        if value is not None:
            self.obdDtcNumber = value
        return self

    def getUdsDtcNumber(self) -> Optional[PositiveInteger]:
        """
        This represents a reasonable Diagnostic Trouble Code. This allows to predefine the Diagnostic Trouble Code, e.g. if the function developer has received a particular requirement from the OEM or from a standardization body. This attribute applies for the UDS diagnostics use case.
        """
        return self.udsDtcNumber

    def setUdsDtcNumber(self, value: Optional[PositiveInteger]) -> DiagnosticEventInfoNeeds:
        """
        This represents a reasonable Diagnostic Trouble Code. This allows to predefine the Diagnostic Trouble Code, e.g. if the function developer has received a particular requirement from the OEM or from a standardization body. This attribute applies for the UDS diagnostics use case.
        A None value is a no-op and does not overwrite an existing udsDtcNumber.
        """
        if value is not None:
            self.udsDtcNumber = value
        return self


class DiagnosticClearDtcNotificationEnum(AREnum):
    """
    This enumeration supports the specification of the time when the ClearDtcNotification callback is supposed to be executed.
    """

    # DiagnosticClearDtcNotificationEnum method parity checklist:
    # Spec: AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf, Table 13.33, p.776
    # Spec verified: R23-11
    # Columns: impl / docstring / test / reader / writer / release   ([—] = no XML element)
    # (no methods) — enum value form serialized on DtcStatusChangeNotificationNeeds.notificationTime (Steps 5/6 N/A: standalone AREnum)
    # [x] __init__                     [x] impl  [x] docstring  [x] test  [—] reader  [—] writer  R23-11

    # The ClearDtcCallback shall be executed when the DTC operation finishes. Tags: atp.EnumerationLiteralIndex=1
    FINISH = "finish"

    # The ClearDtcCallback shall be executed when the DTC operation starts. Tags: atp.EnumerationLiteralIndex=0
    START = "start"

    def __init__(self):
        super().__init__(
            (
                DiagnosticClearDtcNotificationEnum.FINISH,
                DiagnosticClearDtcNotificationEnum.START,
            )
        )


class DtcFormatTypeEnum(AREnum):
    """
    This enumeration specifies the DTC format.
    """

    # DtcFormatTypeEnum method parity checklist:
    # Spec: R4.3.1/AUTOSAR_TPS_SoftwareComponentTemplate.pdf, Table 13.30, p.770 (R4.3.1)
    # (no methods)

    # Defines the J1939 DTC format. Tags: atp.EnumerationValue=0
    J1939 = "j1939"

    # Defines the OBD DTC format. Tags: atp.EnumerationValue=1
    OBD = "obd"

    def __init__(self):
        super().__init__(
            (
                DtcFormatTypeEnum.J1939,
                DtcFormatTypeEnum.OBD,
            )
        )


class DtcStatusChangeNotificationNeeds(DiagnosticCapabilityElement):
    """
    This meta-class represents the needs of a software-component interested to get information regarding any DTC status change.
    """

    # DtcStatusChangeNotificationNeeds method parity checklist:
    # Spec: AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf, Table 13.32, p.776 (R23-11)
    # Spec: R4.3.1/AUTOSAR_TPS_SoftwareComponentTemplate.pdf (R4.3.1)
    # Columns: impl / docstring / test / reader / writer / release   ([—] = no XML element)
    # [x] __init__              [x] impl  [x] docstring  [x] test  [—] reader  [—] writer  R23-11
    # [x] getDtcFormatType      [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R4.3.1
    # [x] setDtcFormatType      [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R4.3.1
    # [x] getNotificationTime   [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setNotificationTime   [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11

    def __init__(self, parent: ARObject, short_name: str):
        super().__init__(parent, short_name)

        # This attribute specifies the DTC format.
        self.dtcFormatType: Optional[DtcFormatTypeEnum] = None

        # This attribute determines the time when the notification about the DTC operation shall be executed. This attribute is only relevant for the configuration of the ClearDtcNotification.
        self.notificationTime: Optional[DiagnosticClearDtcNotificationEnum] = None

    def getDtcFormatType(self) -> Optional[DtcFormatTypeEnum]:
        """
        This attribute specifies the DTC format.
        """
        return self.dtcFormatType

    def setDtcFormatType(self, value: Optional[DtcFormatTypeEnum]) -> DtcStatusChangeNotificationNeeds:
        """
        This attribute specifies the DTC format.
        A None value is a no-op and does not overwrite an existing dtcFormatType.
        """
        if value is not None:
            self.dtcFormatType = value
        return self

    def getNotificationTime(self) -> Optional[DiagnosticClearDtcNotificationEnum]:
        """
        This attribute determines the time when the notification about the DTC operation shall be executed. This attribute is only relevant for the configuration of the ClearDtcNotification.
        """
        return self.notificationTime

    def setNotificationTime(self, value: Optional[DiagnosticClearDtcNotificationEnum]) -> DtcStatusChangeNotificationNeeds:
        """
        This attribute determines the time when the notification about the DTC operation shall be executed. This attribute is only relevant for the configuration of the ClearDtcNotification.
        A None value is a no-op and does not overwrite an existing notificationTime.
        """
        if value is not None:
            self.notificationTime = value
        return self


class DiagnosticEventNeeds(DiagnosticCapabilityElement):
    """
    Specifies the abstract needs on the configuration of the Diagnostic Event Manager for one diagnostic event. Its shortName can be regarded as a symbol identifying the diagnostic event from the viewpoint of the component or module which owns this element. In case the diagnostic event specifies a production error, the shortName shall be the name of the production error.
    """

    # DiagnosticEventNeeds method parity checklist:
    # Spec: AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.pdf, Table 12.31, p.258
    # Spec verified: R23-11
    # Columns: impl / docstring / test / reader / writer / release   ([—] = no XML element)
    # [x] __init__    [x] impl  [x] docstring  [x] test  [—] reader  [—] writer  R23-11
    # [x] getDeferringFidRefs         [x] impl  [x] docstring  [x] test  [x] reader  [x] writer  R23-11
    # [x] addDeferringFidRef          [x] impl  [x] docstring  [x] test  [x] reader  [x] writer  R23-11
    # [x] getDiagEventDebounceAlgorithm[x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] createDiagEventDebounceCounterBased[x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] createDiagEventDebounceMonitorInternal[x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] createDiagEventDebounceTimeBased[x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getInhibitingFidRef         [x] impl  [x] docstring  [x] test  [x] reader  [x] writer  R23-11
    # [x] setInhibitingFidRef         [x] impl  [x] docstring  [x] test  [x] reader  [x] writer  R23-11
    # [x] getInhibitingSecondaryFidRefs[x] impl  [x] docstring  [x] test  [x] reader  [x] writer  R23-11
    # [x] addInhibitingSecondaryFidRef[x] impl  [x] docstring  [x] test  [x] reader  [x] writer  R23-11
    # [x] getPrestoredFreezeframeStoredInNvm[x] impl  [x] docstring  [x] test  [x] reader  [x] writer  R23-11
    # [x] setPrestoredFreezeframeStoredInNvm[x] impl  [x] docstring  [x] test  [x] reader  [x] writer  R23-11
    # [x] getUsesMonitorData          [x] impl  [x] docstring  [x] test  [x] reader  [x] writer  R23-11
    # [x] setUsesMonitorData          [x] impl  [x] docstring  [x] test  [x] reader  [x] writer  R23-11

    def __init__(self, parent: ARObject, short_name: str):
        super().__init__(parent, short_name)

        # This reference contains the link to a function identifier within the FiM which is used by the monitor before delivering a result.
        self.deferringFidRefs: List[RefType] = []

        # Specifies the abstract need on the Debounce Algorithm applied by the Diagnostic Event Manager.
        self.diagEventDebounceAlgorithm: Optional[DiagEventDebounceAlgorithm] = None

        # This represents the primary Function Inhibition Identifier used for inhibition of the diagnostic monitor. The FID might either inhibit the monitoring of a symptom or the reporting of detected faults.
        self.inhibitingFidRef: Optional[RefType] = None

        # This represents the secondary Function Inhibition Identifier used for inhibition of the diagnostic monitor. Any of the FID inhibitions leads to an inhibition of the monitoring of a symptom or the reporting of detected faults.
        self.inhibitingSecondaryFidRefs: List[RefType] = []

        # If the Event uses a prestored freeze-frame (using the operations PrestoreFreezeFrame and ClearPrestored FreezeFrame of the service interface DiagnosticMonitor) this attribute indicates if the Event requires the data to be stored in non-volatile memory. TRUE = Dem shall store the prestored data in non-volatile memory, FALSE = Data can be lost at shutdown (not stored in Nvm).
        self.prestoredFreezeframeStoredInNvm: Optional[Boolean] = None

        # This attribute defines whether additional monitor data shall be added to the reporting of events.
        self.usesMonitorData: Optional[Boolean] = None

    def getDeferringFidRefs(self) -> List[RefType]:
        """
        This reference contains the link to a function identifier within the FiM which is used by the monitor before delivering a result.
        """
        return self.deferringFidRefs

    def addDeferringFidRef(self, value: Optional[RefType]) -> DiagnosticEventNeeds:
        """
        This reference contains the link to a function identifier within the FiM which is used by the monitor before delivering a result.
        A None value is a no-op and does not append to deferringFidRefs.
        """
        if value is not None:
            self.deferringFidRefs.append(value)
        return self

    def getDiagEventDebounceAlgorithm(self) -> Optional[DiagEventDebounceAlgorithm]:
        """
        Specifies the abstract need on the Debounce Algorithm applied by the Diagnostic Event Manager.
        """
        return self.diagEventDebounceAlgorithm

    def createDiagEventDebounceCounterBased(self, short_name: str) -> DiagEventDebounceCounterBased:
        """
        Creates and adds a counter-based debounce algorithm for this diagnostic event.

        Args:
            short_name: The short name for the new counter-based debounce algorithm

        Returns:
            The created DiagEventDebounceCounterBased instance
        """
        if not self.IsElementExists(short_name, DiagEventDebounceCounterBased):
            algorithm = DiagEventDebounceCounterBased(self, short_name)
            self.addElement(algorithm)
            self.diagEventDebounceAlgorithm = algorithm
        return self.getElement(short_name, DiagEventDebounceCounterBased)

    def createDiagEventDebounceMonitorInternal(self, short_name: str) -> DiagEventDebounceMonitorInternal:
        """
        Creates and adds an internal monitor-based debounce algorithm for this diagnostic event.

        Args:
            short_name: The short name for the new internal monitor debounce algorithm

        Returns:
            The created DiagEventDebounceMonitorInternal instance
        """
        if not self.IsElementExists(short_name, DiagEventDebounceMonitorInternal):
            algorithm = DiagEventDebounceMonitorInternal(self, short_name)
            self.addElement(algorithm)
            self.diagEventDebounceAlgorithm = algorithm
        return self.getElement(short_name, DiagEventDebounceMonitorInternal)

    def createDiagEventDebounceTimeBased(self, short_name: str) -> DiagEventDebounceTimeBased:
        """
        Creates and adds a time-based debounce algorithm for this diagnostic event.

        Args:
            short_name: The short name for the new time-based debounce algorithm

        Returns:
            The created DiagEventDebounceTimeBased instance
        """
        if not self.IsElementExists(short_name, DiagEventDebounceTimeBased):
            algorithm = DiagEventDebounceTimeBased(self, short_name)
            self.addElement(algorithm)
            self.diagEventDebounceAlgorithm = algorithm
        return self.getElement(short_name, DiagEventDebounceTimeBased)

    def getInhibitingFidRef(self) -> Optional[RefType]:
        """
        This represents the primary Function Inhibition Identifier used for inhibition of the diagnostic monitor. The FID might either inhibit the monitoring of a symptom or the reporting of detected faults.
        """
        return self.inhibitingFidRef

    def setInhibitingFidRef(self, value: Optional[RefType]) -> DiagnosticEventNeeds:
        """
        This represents the primary Function Inhibition Identifier used for inhibition of the diagnostic monitor. The FID might either inhibit the monitoring of a symptom or the reporting of detected faults.
        A None value is a no-op and does not overwrite an existing inhibitingFidRef.
        """
        if value is not None:
            self.inhibitingFidRef = value
        return self

    def getInhibitingSecondaryFidRefs(self) -> List[RefType]:
        """
        This represents the secondary Function Inhibition Identifier used for inhibition of the diagnostic monitor. Any of the FID inhibitions leads to an inhibition of the monitoring of a symptom or the reporting of detected faults.
        """
        return self.inhibitingSecondaryFidRefs

    def addInhibitingSecondaryFidRef(self, value: Optional[RefType]) -> DiagnosticEventNeeds:
        """
        This represents the secondary Function Inhibition Identifier used for inhibition of the diagnostic monitor. Any of the FID inhibitions leads to an inhibition of the monitoring of a symptom or the reporting of detected faults.
        A None value is a no-op and does not append to inhibitingSecondaryFidRefs.
        """
        if value is not None:
            self.inhibitingSecondaryFidRefs.append(value)
        return self

    def getPrestoredFreezeframeStoredInNvm(self) -> Optional[Boolean]:
        """
        If the Event uses a prestored freeze-frame (using the operations PrestoreFreezeFrame and ClearPrestored FreezeFrame of the service interface DiagnosticMonitor) this attribute indicates if the Event requires the data to be stored in non-volatile memory. TRUE = Dem shall store the prestored data in non-volatile memory, FALSE = Data can be lost at shutdown (not stored in Nvm).
        """
        return self.prestoredFreezeframeStoredInNvm

    def setPrestoredFreezeframeStoredInNvm(self, value: Optional[Boolean]) -> DiagnosticEventNeeds:
        """
        If the Event uses a prestored freeze-frame (using the operations PrestoreFreezeFrame and ClearPrestored FreezeFrame of the service interface DiagnosticMonitor) this attribute indicates if the Event requires the data to be stored in non-volatile memory. TRUE = Dem shall store the prestored data in non-volatile memory, FALSE = Data can be lost at shutdown (not stored in Nvm).
        A None value is a no-op and does not overwrite an existing prestoredFreezeframeStoredInNvm.
        """
        if value is not None:
            self.prestoredFreezeframeStoredInNvm = value
        return self

    def getUsesMonitorData(self) -> Optional[Boolean]:
        """
        This attribute defines whether additional monitor data shall be added to the reporting of events.
        """
        return self.usesMonitorData

    def setUsesMonitorData(self, value: Optional[Boolean]) -> DiagnosticEventNeeds:
        """
        This attribute defines whether additional monitor data shall be added to the reporting of events.
        A None value is a no-op and does not overwrite an existing usesMonitorData.
        """
        if value is not None:
            self.usesMonitorData = value
        return self


class CryptoServiceNeeds(ServiceNeeds):
    """
    Specifies the needs on the configuration of the CryptoServiceManager for one ConfigID (see Specification AUTOSAR_SWS_CSM.doc). An instance of this class is used to find out which ports of a software-component belong to this ConfigID.
    """

    # CryptoServiceNeeds method parity checklist:
    # Spec: AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf, Table 13.9, p.733
    # Columns: impl / docstring / test / reader / writer / release   ([—] = no XML element)
    # [x] __init__                 [x] impl  [x] docstring  [x] test  [—] reader  [—] writer  R23-11
    # [x] getAlgorithmFamily       [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setAlgorithmFamily       [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getAlgorithmMode         [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setAlgorithmMode         [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getCryptoKeyDescription  [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setCryptoKeyDescription  [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getMaximumKeyLength      [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setMaximumKeyLength      [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11

    def __init__(self, parent: ARObject, short_name: str):
        super().__init__(parent, short_name)

        # This attribute represents a description of the family (e.g. AES) of crypto algorithm implemented by the crypto service use case.
        self.algorithmFamily: Optional[String] = None

        # This meta-class has the ability to represent a crypto service use case.
        self.algorithmMode: Optional[String] = None

        # This attribute allows for a verbal description of the applicable cryptographic key. The goal is to pass a hint for the integrator about how to treat the corresponding service use case.
        self.cryptoKeyDescription: Optional[String] = None

        # The maximum length of a cryptographic key, that is used by the software-component or module for this configuration. Unit: bit.
        self.maximumKeyLength: Optional[PositiveInteger] = None

    def getAlgorithmFamily(self) -> Optional[String]:
        """
        This attribute represents a description of the family (e.g. AES) of crypto algorithm implemented by the crypto service use case.
        """
        return self.algorithmFamily

    def setAlgorithmFamily(self, value: Optional[String]) -> CryptoServiceNeeds:
        """
        This attribute represents a description of the family (e.g. AES) of crypto algorithm implemented by the crypto service use case.
        A None value is a no-op and does not overwrite an existing algorithmFamily.
        """
        if value is not None:
            self.algorithmFamily = value
        return self

    def getAlgorithmMode(self) -> Optional[String]:
        """
        This meta-class has the ability to represent a crypto service use case.
        """
        return self.algorithmMode

    def setAlgorithmMode(self, value: Optional[String]) -> CryptoServiceNeeds:
        """
        This meta-class has the ability to represent a crypto service use case.
        A None value is a no-op and does not overwrite an existing algorithmMode.
        """
        if value is not None:
            self.algorithmMode = value
        return self

    def getCryptoKeyDescription(self) -> Optional[String]:
        """
        This attribute allows for a verbal description of the applicable cryptographic key. The goal is to pass a hint for the integrator about how to treat the corresponding service use case.
        """
        return self.cryptoKeyDescription

    def setCryptoKeyDescription(self, value: Optional[String]) -> CryptoServiceNeeds:
        """
        This attribute allows for a verbal description of the applicable cryptographic key. The goal is to pass a hint for the integrator about how to treat the corresponding service use case.
        A None value is a no-op and does not overwrite an existing cryptoKeyDescription.
        """
        if value is not None:
            self.cryptoKeyDescription = value
        return self

    def getMaximumKeyLength(self) -> Optional[PositiveInteger]:
        """
        The maximum length of a cryptographic key, that is used by the software-component or module for this configuration. Unit: bit.
        """
        return self.maximumKeyLength

    def setMaximumKeyLength(self, value: Optional[PositiveInteger]) -> CryptoServiceNeeds:
        """
        The maximum length of a cryptographic key, that is used by the software-component or module for this configuration. Unit: bit.
        A None value is a no-op and does not overwrite an existing maximumKeyLength.
        """
        if value is not None:
            self.maximumKeyLength = value
        return self


class EcuStateMgrUserNeeds(ServiceNeeds):
    """
    Specifies the abstract needs on the configuration of the ECU State Manager for one "user". This class currently contains no attributes. Its name can be regarded as a symbol identifying the user from the viewpoint of the component or module which owns this class.
    """

    # EcuStateMgrUserNeeds method parity checklist:
    # Spec: AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.pdf, Table 12.14, p.235
    # Spec verified: R23-11
    # Columns: impl / docstring / test / reader / writer / release   ([—] = no XML element)
    # [x] __init__                     [x] impl  [x] docstring  [x] test  [—] reader  [—] writer  R23-11

    def __init__(self, parent: ARObject, short_name: str):
        super().__init__(parent, short_name)


class DltUserNeeds(ServiceNeeds):
    """
    This meta-class specifies the needs on the configuration of the Diagnostic Log and Trace module for one SessionId. This class currently contains no attributes. An instance of this class is used to find out which PortPrototypes of an AtomicSwComponentType belong to this SessionId in order to group the request and response PortPrototypes of the same SessionId. The actual SessionId value is stored in the PortDefinedArgumentValue of the respective PortPrototype specification.
    """

    # DltUserNeeds method parity checklist:
    # Spec: AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.pdf, Table 12.16, p.236
    # Spec verified: R23-11
    # Columns: impl / docstring / test / reader / writer / release   ([—] = no XML element)
    # [x] __init__                     [x] impl  [x] docstring  [x] test  [—] reader  [—] writer  R23-11

    def __init__(self, parent: ARObject, short_name: str):
        super().__init__(parent, short_name)


class BswMgrNeeds(ServiceNeeds):
    """
    Specifies the abstract needs on the configuration of the Basic Software Manager for one "user".
    """

    # BswMgrNeeds method parity checklist:
    # Spec: AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf, Table 13.8, p.716
    # Spec verified: R23-11
    # Columns: impl / docstring / test / reader / writer / release   ([—] = no XML element)
    # [x] __init__                     [x] impl  [x] docstring  [x] test  [—] reader  [—] writer  R23-11

    def __init__(self, parent: ARObject, short_name: str):
        super().__init__(parent, short_name)


class ComMgrUserNeeds(ServiceNeeds):
    """
    Specifies the abstract needs on the configuration of the Communication Manager for one "user".
    """

    # ComMgrUserNeeds method parity checklist:
    # Spec: AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.pdf, Table 12.13, p.235
    # Spec verified: R23-11
    # Columns: impl / docstring / test / reader / writer / release   ([—] = no XML element)
    # [x] __init__    [x] impl  [x] docstring  [x] test  [—] reader  [—] writer  R23-11
    # [x] getMaxCommMode              [x] impl  [x] docstring  [x] test  [x] reader  [x] writer  R23-11
    # [x] setMaxCommMode              [x] impl  [x] docstring  [x] test  [x] reader  [x] writer  R23-11

    def __init__(self, parent: ARObject, short_name: str):
        super().__init__(parent, short_name)

        # Maximum communication mode requested by this ComM user.
        self.maxCommMode: Optional[MaxCommModeEnum] = None

    def getMaxCommMode(self) -> Optional[MaxCommModeEnum]:
        """
        Maximum communication mode requested by this ComM user.
        """
        return self.maxCommMode

    def setMaxCommMode(self, value: Optional[MaxCommModeEnum]) -> ComMgrUserNeeds:
        """
        Maximum communication mode requested by this ComM user.
        A None value is a no-op and does not overwrite an existing maxCommMode.
        """
        if value is not None:
            self.maxCommMode = value
        return self


class CryptoKeyManagementNeeds(ServiceNeeds):
    """
    This meta-class can be used to indicate a service use case for key management.
    """

    # CryptoKeyManagementNeeds method parity checklist:
    # Spec: AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf, Table 13.11, p.745
    # Spec verified: R23-11
    # Columns: impl / docstring / test / reader / writer / release   ([—] = no XML element)
    # [x] __init__                     [x] impl  [x] docstring  [x] test  [—] reader  [—] writer  R23-11

    def __init__(self, parent: ARObject, short_name: str):
        super().__init__(parent, short_name)


class CryptoServiceJobNeeds(ServiceNeeds):
    """
    This meta-class shall be taken to indicate that the service use case modeled with this kind of Service Needs assumes the usage of the crypto job API.
    """

    # CryptoServiceJobNeeds method parity checklist:
    # Spec: AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf, Table 13.10, p.733
    # Spec verified: R23-11
    # Columns: impl / docstring / test / reader / writer / release   ([—] = no XML element)
    # [x] __init__                     [x] impl  [x] docstring  [x] test  [—] reader  [—] writer  R23-11

    def __init__(self, parent: ARObject, short_name: str):
        super().__init__(parent, short_name)


class TracedFailure(Identifiable, VariationPointCapable, ABC):
    """
    Specifies the ability to report a specific failure to the error tracer. The short name specifies the literal applicable for the Default Error Tracer.
    """

    # TracedFailure method parity checklist:
    # Spec: AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.pdf, Table 12.37, p.263
    # Spec verified: R23-11
    # [x] __init__                     [x] impl  [x] docstring  [x] test
    # [x] getId                        [x] impl  [x] docstring  [x] test
    # [x] setId                        [x] impl  [x] docstring  [x] test

    def __init__(self, parent: ARObject, short_name: str):
        """
        Initializes the TracedFailure with a parent and short name.
        Raises TypeError if this abstract class is instantiated directly.

        Args:
            parent: The parent ARObject that contains this traced failure
            short_name: The unique short name of this traced failure
        """
        if type(self) is TracedFailure:
            raise TypeError("TracedFailure is an abstract class.")

        super().__init__(parent, short_name)

        # ID of detected failure used in reporting API as error or fault id.
        self.id: Optional[PositiveInteger] = None

    def getId(self) -> Optional[PositiveInteger]:
        """
        Gets the ID of detected failure used in reporting API as error or fault id.

        Returns:
            PositiveInteger instance, or None if not set
        """
        return self.id

    def setId(self, value: Optional[PositiveInteger]) -> TracedFailure:
        """
        Sets the ID of detected failure used in reporting API as error or fault id.
        A None value is a no-op and does not overwrite an existing id.

        Args:
            value: The PositiveInteger instance to set

        Returns:
            self for method chaining
        """
        if value is not None:
            self.id = value
        return self


class DevelopmentError(TracedFailure):
    """
    The reported failure is classified as development error.
    """

    # DevelopmentError method parity checklist:
    # Spec: AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.pdf, Table 12.38, p.263
    # Spec verified: R23-11
    # Columns: impl / docstring / test / reader / writer / release   ([—] = no XML element)
    # [x] __init__    [x] impl  [x] docstring  [x] test  [—] reader  [—] writer  R23-11

    def __init__(self, parent: ARObject, short_name: str):
        super().__init__(parent, short_name)


class DiagnosticComponentNeeds(DiagnosticCapabilityElement):
    """
    This meta-class represents the ability to specify the service needs for the configuration of component events.
    """

    # DiagnosticComponentNeeds method parity checklist:
    # Spec: AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf, Table 13.64, p.816
    # Spec verified: R23-11
    # Columns: impl / docstring / test / reader / writer / release   ([—] = no XML element)
    # [x] __init__                     [x] impl  [x] docstring  [x] test  [—] reader  [—] writer  R23-11

    def __init__(self, parent: ARObject, short_name: str):
        super().__init__(parent, short_name)


class DiagnosticControlNeeds(DiagnosticCapabilityElement):
    """
    This meta-class indicates a service use-case for reporting the controlled status by diagnostic services.
    """

    # DiagnosticControlNeeds method parity checklist:
    # Spec: AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf, Table 13.63, p.812
    # Spec verified: R23-11
    # Columns: impl / docstring / test / reader / writer / release   ([—] = no XML element)
    # [x] __init__                     [x] impl  [x] docstring  [x] test  [—] reader  [—] writer  R23-11

    def __init__(self, parent: ARObject, short_name: str):
        super().__init__(parent, short_name)


class DiagnosticDenominatorConditionEnum(AREnum):
    """
    This enumeration contains valid denominator types.
    """

    # DiagnosticDenominatorConditionEnum method parity checklist:
    # Spec: AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf, Table 13.52, p.803
    # Spec verified: R23-11
    # Columns: impl / docstring / test / reader / writer / release   ([—] = no XML element)
    # [x] __init__    [x] impl  [x] docstring  [x] test  [—] reader  [—] writer  R23-11
    # (no methods) — serialized as an attribute value on the consuming class

    # Condition based on definition of 500miles conditions as defined for OBD2. Tags: atp.EnumerationLiteralIndex=2 xml.name=-500-MILES
    _500MILES = "-500-MILES"
    # Condition based on definition of "cold start" as defined for EU5+ Tags: atp.EnumerationLiteralIndex=0
    COLDSTART = "coldstart"
    # Conditions based on the "Cold start emission reduction strategy" denominator Tags: atp.EnumerationLiteralIndex=5
    CSERS = "csers"
    # Condition based on definition of "EVAP" conditions as defined for OBD2. Tags: atp.EnumerationLiteralIndex=1
    EVAP = "evap"
    # Conditions based on the "EVAP purge flow" denominator. Tags: atp.EnumerationLiteralIndex=6
    EVAPPURGEFLOW = "evappurgeflow"
    # condition based on definition of individual requirements. Tags: atp.EnumerationLiteralIndex=3
    INDIVIDUAL = "individual"
    # Condition based on definition of OBD requirements. Tags: atp.EnumerationLiteralIndex=4
    OBD = "obd"

    def __init__(self):
        super().__init__(
            [
                DiagnosticDenominatorConditionEnum._500MILES,
                DiagnosticDenominatorConditionEnum.COLDSTART,
                DiagnosticDenominatorConditionEnum.CSERS,
                DiagnosticDenominatorConditionEnum.EVAP,
                DiagnosticDenominatorConditionEnum.EVAPPURGEFLOW,
                DiagnosticDenominatorConditionEnum.INDIVIDUAL,
                DiagnosticDenominatorConditionEnum.OBD,
            ]
        )


class DiagnosticEnableConditionNeeds(DiagnosticCapabilityElement):
    """
    This meta-class represents the needs of a software-component to provide the capability to set an enable condition.
    """

    # DiagnosticEnableConditionNeeds method parity checklist:
    # Spec: AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf, Table 13.26, p.762
    # Spec verified: R23-11
    # Columns: impl / docstring / test / reader / writer / release   ([—] = no XML element)
    # [x] __init__    [x] impl  [x] docstring  [x] test  [—] reader  [—] writer  R23-11
    # [x] getInitialStatus            [x] impl  [x] docstring  [x] test  [x] reader  [x] writer  R23-11
    # [x] setInitialStatus            [x] impl  [x] docstring  [x] test  [x] reader  [x] writer  R23-11

    def __init__(self, parent: ARObject, short_name: str):
        super().__init__(parent, short_name)

        # Defines the initial status for enable or disable of acceptance of event reports of a diagnostic event.
        self.initialStatus: Optional[EventAcceptanceStatusEnum] = None

    def getInitialStatus(self) -> Optional[EventAcceptanceStatusEnum]:
        """
        Defines the initial status for enable or disable of acceptance of event reports of a diagnostic event.
        """
        return self.initialStatus

    def setInitialStatus(self, value: Optional[EventAcceptanceStatusEnum]) -> DiagnosticEnableConditionNeeds:
        """
        Defines the initial status for enable or disable of acceptance of event reports of a diagnostic event.
        A None value is a no-op and does not overwrite an existing initialStatus.
        """
        if value is not None:
            self.initialStatus = value
        return self


class DiagnosticEventManagerNeeds(DiagnosticCapabilityElement):
    """
    Specifies the general needs on the configuration of the Diagnostic Event Manager (Dem) which are not related to a particular item.
    """

    # DiagnosticEventManagerNeeds method parity checklist:
    # Spec: AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf, Table 13.14, p.753
    # Spec verified: R23-11
    # Columns: impl / docstring / test / reader / writer / release   ([—] = no XML element)
    # [x] __init__                     [x] impl  [x] docstring  [x] test  [—] reader  [—] writer  R23-11

    def __init__(self, parent: ARObject, short_name: str):
        super().__init__(parent, short_name)


class DiagnosticIoControlNeeds(DiagnosticCapabilityElement):
    """
    Specifies the general needs on the configuration of the Diagnostic Communication Manager (DCM) which are not related to a particular item (e.g. a PID). The main use case is the mapping of service ports to the Dcm which are not related to a particular item.
    """

    # DiagnosticIoControlNeeds method parity checklist:
    # Spec: AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.pdf, Table 12.26, p.248
    # Spec verified: R23-11
    # Columns: impl / docstring / test / reader / writer / release   ([—] = no XML element)
    # [x] __init__    [x] impl  [x] docstring  [x] test  [—] reader  [—] writer  R23-11
    # [x] getCurrentValueRef          [x] impl  [x] docstring  [x] test  [x] reader  [x] writer  R23-11
    # [x] setCurrentValueRef          [x] impl  [x] docstring  [x] test  [x] reader  [x] writer  R23-11
    # [x] getFreezeCurrentStateSupported[x] impl  [x] docstring  [x] test  [x] reader  [x] writer  R23-11
    # [x] setFreezeCurrentStateSupported[x] impl  [x] docstring  [x] test  [x] reader  [x] writer  R23-11
    # [x] getResetToDefaultSupported  [x] impl  [x] docstring  [x] test  [x] reader  [x] writer  R23-11
    # [x] setResetToDefaultSupported  [x] impl  [x] docstring  [x] test  [x] reader  [x] writer  R23-11
    # [x] getShortTermAdjustmentSupported[x] impl  [x] docstring  [x] test  [x] reader  [x] writer  R23-11
    # [x] setShortTermAdjustmentSupported[x] impl  [x] docstring  [x] test  [x] reader  [x] writer  R23-11

    def __init__(self, parent: ARObject, short_name: str):
        super().__init__(parent, short_name)

        # Reference to the DiagnosticValueNeeds indicating the access to the current value via signalBasedDiagnostics.
        self.currentValueRef: Optional[RefType] = None

        # This attribute determines, if the referenced port supports temporary freezing of I/O value. The temporary freeze is not supported if the enclosing DiagnosticIoControlNeeds is aggregated by a Swc ServiceDependency, see [constr_1364].
        self.freezeCurrentStateSupported: Optional[Boolean] = None

        # This represents a flag for the existence of the ResetTo Default operation in the service interface.
        self.resetToDefaultSupported: Optional[Boolean] = None

        # This attribute determines, if the referenced port supports temporarily setting of I/O value to a specific value provided by the diagnostic tester. The short term adjustment is not supported if the enclosing DiagnosticIoControlNeeds is aggregated by a SwcServiceDependency, see [constr_1364].
        self.shortTermAdjustmentSupported: Optional[Boolean] = None

    def getCurrentValueRef(self) -> Optional[RefType]:
        """
        Reference to the DiagnosticValueNeeds indicating the access to the current value via signalBasedDiagnostics.
        """
        return self.currentValueRef

    def setCurrentValueRef(self, value: Optional[RefType]) -> DiagnosticIoControlNeeds:
        """
        Reference to the DiagnosticValueNeeds indicating the access to the current value via signalBasedDiagnostics.
        A None value is a no-op and does not overwrite an existing currentValueRef.
        """
        if value is not None:
            self.currentValueRef = value
        return self

    def getFreezeCurrentStateSupported(self) -> Optional[Boolean]:
        """
        This attribute determines, if the referenced port supports temporary freezing of I/O value. The temporary freeze is not supported if the enclosing DiagnosticIoControlNeeds is aggregated by a Swc ServiceDependency, see [constr_1364].
        """
        return self.freezeCurrentStateSupported

    def setFreezeCurrentStateSupported(self, value: Optional[Boolean]) -> DiagnosticIoControlNeeds:
        """
        This attribute determines, if the referenced port supports temporary freezing of I/O value. The temporary freeze is not supported if the enclosing DiagnosticIoControlNeeds is aggregated by a Swc ServiceDependency, see [constr_1364].
        A None value is a no-op and does not overwrite an existing freezeCurrentStateSupported.
        """
        if value is not None:
            self.freezeCurrentStateSupported = value
        return self

    def getResetToDefaultSupported(self) -> Optional[Boolean]:
        """
        This represents a flag for the existence of the ResetTo Default operation in the service interface.
        """
        return self.resetToDefaultSupported

    def setResetToDefaultSupported(self, value: Optional[Boolean]) -> DiagnosticIoControlNeeds:
        """
        This represents a flag for the existence of the ResetTo Default operation in the service interface.
        A None value is a no-op and does not overwrite an existing resetToDefaultSupported.
        """
        if value is not None:
            self.resetToDefaultSupported = value
        return self

    def getShortTermAdjustmentSupported(self) -> Optional[Boolean]:
        """
        This attribute determines, if the referenced port supports temporarily setting of I/O value to a specific value provided by the diagnostic tester. The short term adjustment is not supported if the enclosing DiagnosticIoControlNeeds is aggregated by a SwcServiceDependency, see [constr_1364].
        """
        return self.shortTermAdjustmentSupported

    def setShortTermAdjustmentSupported(self, value: Optional[Boolean]) -> DiagnosticIoControlNeeds:
        """
        This attribute determines, if the referenced port supports temporarily setting of I/O value to a specific value provided by the diagnostic tester. The short term adjustment is not supported if the enclosing DiagnosticIoControlNeeds is aggregated by a SwcServiceDependency, see [constr_1364].
        A None value is a no-op and does not overwrite an existing shortTermAdjustmentSupported.
        """
        if value is not None:
            self.shortTermAdjustmentSupported = value
        return self


class DiagnosticMonitorUpdateKindEnum(AREnum):
    """
    This enumeration indicates the acceptance criteria for a diagnostic monitor.
    """

    # DiagnosticMonitorUpdateKindEnum method parity checklist:
    # Spec: AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf, Table 13.50, p.798
    # Spec verified: R23-11
    # Columns: impl / docstring / test / reader / writer / release   ([—] = no XML element)
    # [x] __init__    [x] impl  [x] docstring  [x] test  [—] reader  [—] writer  R23-11
    # (no methods) — serialized as an attribute value on the consuming class

    # The value 'always' configures Dem to accept the call to SetDTR() regardless of the state of the diagnostics. Tags: atp.EnumerationLiteralIndex=0
    ALWAYS = "always"

    # The value 'steady' configures Dem to accept it only when debouncing is at the limit. Tags: atp.EnumerationLiteralIndex=1
    STEADY = "steady"

    def __init__(self):
        """
        Initializes the DiagnosticMonitorUpdateKindEnum with all possible values.
        """
        super().__init__(
            [
                DiagnosticMonitorUpdateKindEnum.ALWAYS,
                DiagnosticMonitorUpdateKindEnum.STEADY,
            ]
        )


class DiagnosticOperationCycleNeeds(DiagnosticCapabilityElement):
    """
    This meta-class represents the needs of a software-component to provide information regarding the operation cycle management to the Dem module.
    """

    # DiagnosticOperationCycleNeeds method parity checklist:
    # Spec: AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf, Table 13.24, p.761
    # Spec verified: R23-11
    # Columns: impl / docstring / test / reader / writer / release   ([—] = no XML element)
    # [x] __init__    [x] impl  [x] docstring  [x] test  [—] reader  [—] writer  R23-11
    # [x] getOperationCycle           [x] impl  [x] docstring  [x] test  [x] reader  [x] writer  R23-11
    # [x] setOperationCycle           [x] impl  [x] docstring  [x] test  [x] reader  [x] writer  R23-11

    def __init__(self, parent: ARObject, short_name: str):
        super().__init__(parent, short_name)

        # Operation cycles types for the Dem to be supported by cycle-state APIs.
        self.operationCycle: Optional[OperationCycleTypeEnum] = None

    def getOperationCycle(self) -> Optional[OperationCycleTypeEnum]:
        """
        Operation cycles types for the Dem to be supported by cycle-state APIs.
        """
        return self.operationCycle

    def setOperationCycle(self, value: Optional[OperationCycleTypeEnum]) -> DiagnosticOperationCycleNeeds:
        """
        Operation cycles types for the Dem to be supported by cycle-state APIs.
        A None value is a no-op and does not overwrite an existing operationCycle.
        """
        if value is not None:
            self.operationCycle = value
        return self


class DiagnosticRequestFileTransferNeeds(DiagnosticCapabilityElement):
    """
    This meta-class indicates the existence of a service use case that involves UDS service 0x38, Request File Transfer.
    """

    # DiagnosticRequestFileTransferNeeds method parity checklist:
    # Spec: AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf, Table 13.43, p.795
    # Spec verified: R23-11
    # Columns: impl / docstring / test / reader / writer / release   ([—] = no XML element)
    # [x] __init__                     [x] impl  [x] docstring  [x] test  [—] reader  [—] writer  R23-11

    def __init__(self, parent: ARObject, short_name: str):
        super().__init__(parent, short_name)


class DiagnosticStorageConditionNeeds(DiagnosticCapabilityElement):
    """
    This meta-class represents the needs of a software-component to provide the capability to set a storage condition.
    """

    # DiagnosticStorageConditionNeeds method parity checklist:
    # Spec: AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf, Table 13.28, p.762
    # Spec verified: R23-11
    # Columns: impl / docstring / test / reader / writer / release   ([—] = no XML element)
    # [x] __init__    [x] impl  [x] docstring  [x] test  [—] reader  [—] writer  R23-11
    # [x] getInitialStatus            [x] impl  [x] docstring  [x] test  [x] reader  [x] writer  R23-11
    # [x] setInitialStatus            [x] impl  [x] docstring  [x] test  [x] reader  [x] writer  R23-11

    def __init__(self, parent: ARObject, short_name: str):
        super().__init__(parent, short_name)

        # Defines the initial status for enable or disable of storage of a diagnostic event.
        self.initialStatus: Optional[StorageConditionStatusEnum] = None

    def getInitialStatus(self) -> Optional[StorageConditionStatusEnum]:
        """
        Defines the initial status for enable or disable of storage of a diagnostic event.
        """
        return self.initialStatus

    def setInitialStatus(self, value: Optional[StorageConditionStatusEnum]) -> DiagnosticStorageConditionNeeds:
        """
        Defines the initial status for enable or disable of storage of a diagnostic event.
        A None value is a no-op and does not overwrite an existing initialStatus.
        """
        if value is not None:
            self.initialStatus = value
        return self


class DiagnosticUploadDownloadNeeds(DiagnosticCapabilityElement):
    """
    This meta-class represents the ability to specify needs regarding upload and download by means of diagnostic services.
    """

    # DiagnosticUploadDownloadNeeds method parity checklist:
    # Spec: AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.pdf, Table 12.29, p.252
    # Spec verified: R23-11
    # Columns: impl / docstring / test / reader / writer / release   ([—] = no XML element)
    # [x] __init__                     [x] impl  [x] docstring  [x] test  [—] reader  [—] writer  R23-11

    def __init__(self, parent: ARObject, short_name: str):
        super().__init__(parent, short_name)


class DiagnosticsCommunicationSecurityNeeds(DiagnosticCapabilityElement):
    """
    This meta-class represents the needs of a software-component to verify the access to security level via diagnostic services.
    """

    # DiagnosticsCommunicationSecurityNeeds method parity checklist:
    # Spec: AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.pdf, Table 12.27, p.248
    # Spec verified: R23-11
    # Columns: impl / docstring / test / reader / writer / release   ([—] = no XML element)
    # [x] __init__                     [x] impl  [x] docstring  [x] test  [—] reader  [—] writer  R23-11

    def __init__(self, parent: ARObject, short_name: str):
        super().__init__(parent, short_name)


class DoIpServiceNeeds(ServiceNeeds, ABC):
    """
    This represents an abstract base class for ServiceNeeds related to DoIP.
    """

    # DoIpServiceNeeds method parity checklist:
    # Spec: AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf, Table 13.54, p.805
    # Spec verified: R23-11
    # [x] __init__                     [x] impl  [x] docstring  [x] test

    def __init__(self, parent: ARObject, short_name: str):
        if type(self) is DoIpServiceNeeds:
            raise TypeError("DoIpServiceNeeds is an abstract class.")

        super().__init__(parent, short_name)


class DoIpActivationLineNeeds(DoIpServiceNeeds):
    """
    A DoIP entity needs to be informed when an external tester is attached or activated. The DoIpActivation ServiceNeeds specifies the trigger for such an event. Examples would be a Pdu via a regular communication bus, a PWM signal, or an I/O. For details please refer to the ISO 13400.
    """

    # DoIpActivationLineNeeds method parity checklist:
    # Spec: AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf, Table 13.60, p.807
    # Spec verified: R23-11
    # Columns: impl / docstring / test / reader / writer / release   ([—] = no XML element)
    # [x] __init__                     [x] impl  [x] docstring  [x] test  [—] reader  [—] writer  R23-11

    def __init__(self, parent: ARObject, short_name: str):
        super().__init__(parent, short_name)


class DoIpGidNeeds(DoIpServiceNeeds):
    """
    The DoIpGidNeeds indicates that the software-component owning this ServiceNeeds is providing the GID number either after a GID Synchronisation or by other means like e.g. flashed EEPROM parameter. This need can be used independent from DoIpGidSynchronizationNeeds and is necessary if the GID can not be provided out of the DoIP configuration options.
    """

    # DoIpGidNeeds method parity checklist:
    # Spec: AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf, Table 13.55, p.805
    # Spec verified: R23-11
    # Columns: impl / docstring / test / reader / writer / release   ([—] = no XML element)
    # [x] __init__                     [x] impl  [x] docstring  [x] test  [—] reader  [—] writer  R23-11

    def __init__(self, parent: ARObject, short_name: str):
        super().__init__(parent, short_name)


class DoIpGidSynchronizationNeeds(DoIpServiceNeeds):
    """
    The DoIpGidSynchronizationNeeds indicates that the software-component owning this ServiceNeeds is triggered by the DoIP entity to start a synchronization of the GID (Group Identification) on the DoIP service 0x0001, 0x0002, 0x0003 or before announcement via service 0x0004 according to ISO 13400-2:2012 if necessary. Note that this need is only relevant for DoIP synchronization masters.
    """

    # DoIpGidSynchronizationNeeds method parity checklist:
    # Spec: AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf, Table 13.56, p.806
    # Spec verified: R23-11
    # Columns: impl / docstring / test / reader / writer / release   ([—] = no XML element)
    # [x] __init__                     [x] impl  [x] docstring  [x] test  [—] reader  [—] writer  R23-11

    def __init__(self, parent: ARObject, short_name: str):
        super().__init__(parent, short_name)


class DoIpPowerModeStatusNeeds(DoIpServiceNeeds):
    """
    The DoIpPowerModeStatusNeeds indicates that the software-component owning this ServiceNeeds is providing the PowerModeStatus for the DoIP service 0x4003 according to ISO 13400-2:2012.
    """

    # DoIpPowerModeStatusNeeds method parity checklist:
    # Spec: AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf, Table 13.57, p.806
    # Spec verified: R23-11
    # Columns: impl / docstring / test / reader / writer / release   ([—] = no XML element)
    # [x] __init__                     [x] impl  [x] docstring  [x] test  [—] reader  [—] writer  R23-11

    def __init__(self, parent: ARObject, short_name: str):
        super().__init__(parent, short_name)


class DoIpRoutingActivationAuthenticationNeeds(DoIpServiceNeeds):
    """
    DoIPRoutingActivationAuthenticationNeeds indicates that the software-component owning this Service Needs will have an authentication required for a DoIP routing activation service (0x0005) according to ISO 13400-2:2012.
    """

    # DoIpRoutingActivationAuthenticationNeeds method parity checklist:
    # Spec: AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf, Table 13.58, p.806
    # Spec verified: R23-11
    # [x] __init__                  [x] impl  [x] docstring  [x] test  [—] reader  [—] writer
    # [x] getDataLengthRequest      [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] setDataLengthRequest      [x] impl  [x] docstring  [x] test  [x] reader  [—] writer
    # [x] getDataLengthResponse     [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] setDataLengthResponse     [x] impl  [x] docstring  [x] test  [x] reader  [—] writer
    # [x] getRoutingActivationType  [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] setRoutingActivationType  [x] impl  [x] docstring  [x] test  [x] reader  [—] writer

    def __init__(self, parent: ARObject, short_name: str):
        super().__init__(parent, short_name)

        # Describes the length in byte of the additional information for RA authentication that is needed by the software entity. If the software entity is a software-component the attribute does not need to exist as the information is available via the length of the uint8 Array type. Otherwise (i.e the software entity is a Complex Driver) this attribute needs to be filled out if additional information is needed.
        self.dataLengthRequest: Optional[PositiveInteger] = None

        # Describes the length in byte of the additional information for RA authentication that is provided by the software entity. If the software entity is a software-component the attribute does not need to exist as the information is available via the length of the uint8 Array type. Otherwise (i.e the software entity is a Complex Driver) this attribute needs to be filled in if additional information is provided.
        self.dataLengthResponse: Optional[PositiveInteger] = None

        # Describes the ISO 13400-2:2012 "routing activation request activation type" which is received via DoIP service 0x0005. 0x00 is DEFAULT, 0x01 is WWH-OBD. If neither of the specified values (0x00 or 0x01) is needed the token shall contain RA_ + hex value representation of the integer value shall be used (i.e: RA_0xE1).
        self.routingActivationType: Optional[NameToken] = None

    def getDataLengthRequest(self) -> Optional[PositiveInteger]:
        """
        Describes the length in byte of the additional information for RA authentication that is needed by the software entity. If the software entity is a software-component the attribute does not need to exist as the information is available via the length of the uint8 Array type. Otherwise (i.e the software entity is a Complex Driver) this attribute needs to be filled out if additional information is needed.

        Returns:
            PositiveInteger instance, or None if not set
        """
        return self.dataLengthRequest

    def setDataLengthRequest(self, value: Optional[PositiveInteger]) -> DoIpRoutingActivationAuthenticationNeeds:
        """
        Describes the length in byte of the additional information for RA authentication that is needed by the software entity. If the software entity is a software-component the attribute does not need to exist as the information is available via the length of the uint8 Array type. Otherwise (i.e the software entity is a Complex Driver) this attribute needs to be filled out if additional information is needed.
        A None value is a no-op and does not overwrite an existing dataLengthRequest.

        Args:
            value: The PositiveInteger instance to set

        Returns:
            self for method chaining
        """
        if value is not None:
            self.dataLengthRequest = value
        return self

    def getDataLengthResponse(self) -> Optional[PositiveInteger]:
        """
        Describes the length in byte of the additional information for RA authentication that is provided by the software entity. If the software entity is a software-component the attribute does not need to exist as the information is available via the length of the uint8 Array type. Otherwise (i.e the software entity is a Complex Driver) this attribute needs to be filled in if additional information is provided.

        Returns:
            PositiveInteger instance, or None if not set
        """
        return self.dataLengthResponse

    def setDataLengthResponse(self, value: Optional[PositiveInteger]) -> DoIpRoutingActivationAuthenticationNeeds:
        """
        Describes the length in byte of the additional information for RA authentication that is provided by the software entity. If the software entity is a software-component the attribute does not need to exist as the information is available via the length of the uint8 Array type. Otherwise (i.e the software entity is a Complex Driver) this attribute needs to be filled in if additional information is provided.
        A None value is a no-op and does not overwrite an existing dataLengthResponse.

        Args:
            value: The PositiveInteger instance to set

        Returns:
            self for method chaining
        """
        if value is not None:
            self.dataLengthResponse = value
        return self

    def getRoutingActivationType(self) -> Optional[NameToken]:
        """
        Describes the ISO 13400-2:2012 "routing activation request activation type" which is received via DoIP service 0x0005. 0x00 is DEFAULT, 0x01 is WWH-OBD. If neither of the specified values (0x00 or 0x01) is needed the token shall contain ``RA_`` + hex value representation of the integer value shall be used (i.e: ``RA_0xE1``).

        Returns:
            NameToken instance, or None if not set
        """
        return self.routingActivationType

    def setRoutingActivationType(self, value: Optional[NameToken]) -> DoIpRoutingActivationAuthenticationNeeds:
        """
        Describes the ISO 13400-2:2012 "routing activation request activation type" which is received via DoIP service 0x0005. 0x00 is DEFAULT, 0x01 is WWH-OBD. If neither of the specified values (0x00 or 0x01) is needed the token shall contain ``RA_`` + hex value representation of the integer value shall be used (i.e: ``RA_0xE1``).
        A None value is a no-op and does not overwrite an existing routingActivationType.

        Args:
            value: The NameToken instance to set

        Returns:
            self for method chaining
        """
        if value is not None:
            self.routingActivationType = value
        return self


class DoIpRoutingActivationConfirmationNeeds(DoIpServiceNeeds):
    """
    DoIpRoutingActivationConfirmationNeeds indicates that the software-component that owns this Service Needs will have a confirmation required for a DoIP routing activation service (0x0005) according to ISO 13400-2:2012.
    """

    # DoIpRoutingActivationConfirmationNeeds method parity checklist:
    # Spec: AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf, Table 13.59, p.807
    # Spec verified: R23-11
    # [x] __init__                  [x] impl  [x] docstring  [x] test  [—] reader  [—] writer
    # [x] getDataLengthRequest      [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] setDataLengthRequest      [x] impl  [x] docstring  [x] test  [x] reader  [—] writer
    # [x] getDataLengthResponse     [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] setDataLengthResponse     [x] impl  [x] docstring  [x] test  [x] reader  [—] writer
    # [x] getRoutingActivationType  [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] setRoutingActivationType  [x] impl  [x] docstring  [x] test  [x] reader  [—] writer

    def __init__(self, parent: ARObject, short_name: str):
        super().__init__(parent, short_name)

        # Describes the length in byte of the additional information for RA confirmation that is needed by the software entity. If the software entity is a software-component the attribute does not need to exist as the information is available via the length of the uint8 Array type. Otherwise (i.e the software entity is a Complex Driver) this attribute needs to be filled out if additional information is needed.
        self.dataLengthRequest: Optional[PositiveInteger] = None

        # Describes the length in byte of the additional information for RA confirmation that is provided by the software entity. If the software entity is a software-component the attribute does not need to exist as the information is available via the length of the uint8 Array type. Otherwise (i.e the software entity is a Complex Driver) this attribute needs to be filled out if additional information is provided.
        self.dataLengthResponse: Optional[PositiveInteger] = None

        # Describes the ISO 13400-2:2012 "routing activation request activation type" which is received via DoIP service 0x0005. 0x00 is DEFAULT, 0x01 is WWH-OBD. If neither of the specified values (0x00 or 0x01) is needed the token shall contain RA_ + hex value representation of the integer value shall be used (i.e: RA_0xE1).
        self.routingActivationType: Optional[NameToken] = None

    def getDataLengthRequest(self) -> Optional[PositiveInteger]:
        """
        Describes the length in byte of the additional information for RA confirmation that is needed by the software entity. If the software entity is a software-component the attribute does not need to exist as the information is available via the length of the uint8 Array type. Otherwise (i.e the software entity is a Complex Driver) this attribute needs to be filled out if additional information is needed.

        Returns:
            PositiveInteger instance, or None if not set
        """
        return self.dataLengthRequest

    def setDataLengthRequest(self, value: Optional[PositiveInteger]) -> DoIpRoutingActivationConfirmationNeeds:
        """
        Describes the length in byte of the additional information for RA confirmation that is needed by the software entity. If the software entity is a software-component the attribute does not need to exist as the information is available via the length of the uint8 Array type. Otherwise (i.e the software entity is a Complex Driver) this attribute needs to be filled out if additional information is needed.
        A None value is a no-op and does not overwrite an existing dataLengthRequest.

        Args:
            value: The PositiveInteger instance to set

        Returns:
            self for method chaining
        """
        if value is not None:
            self.dataLengthRequest = value
        return self

    def getDataLengthResponse(self) -> Optional[PositiveInteger]:
        """
        Describes the length in byte of the additional information for RA confirmation that is provided by the software entity. If the software entity is a software-component the attribute does not need to exist as the information is available via the length of the uint8 Array type. Otherwise (i.e the software entity is a Complex Driver) this attribute needs to be filled out if additional information is provided.

        Returns:
            PositiveInteger instance, or None if not set
        """
        return self.dataLengthResponse

    def setDataLengthResponse(self, value: Optional[PositiveInteger]) -> DoIpRoutingActivationConfirmationNeeds:
        """
        Describes the length in byte of the additional information for RA confirmation that is provided by the software entity. If the software entity is a software-component the attribute does not need to exist as the information is available via the length of the uint8 Array type. Otherwise (i.e the software entity is a Complex Driver) this attribute needs to be filled out if additional information is provided.
        A None value is a no-op and does not overwrite an existing dataLengthResponse.

        Args:
            value: The PositiveInteger instance to set

        Returns:
            self for method chaining
        """
        if value is not None:
            self.dataLengthResponse = value
        return self

    def getRoutingActivationType(self) -> Optional[NameToken]:
        """
        Describes the ISO 13400-2:2012 "routing activation request activation type" which is received via DoIP service 0x0005. 0x00 is DEFAULT, 0x01 is WWH-OBD. If neither of the specified values (0x00 or 0x01) is needed the token shall contain ``RA_`` + hex value representation of the integer value shall be used (i.e: ``RA_0xE1``).

        Returns:
            NameToken instance, or None if not set
        """
        return self.routingActivationType

    def setRoutingActivationType(self, value: Optional[NameToken]) -> DoIpRoutingActivationConfirmationNeeds:
        """
        Describes the ISO 13400-2:2012 "routing activation request activation type" which is received via DoIP service 0x0005. 0x00 is DEFAULT, 0x01 is WWH-OBD. If neither of the specified values (0x00 or 0x01) is needed the token shall contain ``RA_`` + hex value representation of the integer value shall be used (i.e: ``RA_0xE1``).
        A None value is a no-op and does not overwrite an existing routingActivationType.

        Args:
            value: The NameToken instance to set

        Returns:
            self for method chaining
        """
        if value is not None:
            self.routingActivationType = value
        return self


class ErrorTracerNeeds(ServiceNeeds):
    """
    Specifies the need to report failures to the error tracer.
    """

    # ErrorTracerNeeds method parity checklist:
    # Spec: AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.pdf, Table 12.36, p.263
    # Spec verified: R23-11
    # Columns: impl / docstring / test / reader / writer / release   ([—] = no XML element)
    # [x] __init__    [x] impl  [x] docstring  [x] test  [—] reader  [—] writer  R23-11
    # [x] getTracedFailures           [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] createDevelopmentError      [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] createRuntimeError          [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11

    def __init__(self, parent: ARObject, short_name: str):
        super().__init__(parent, short_name)

        # list of traced failures Stereotypes: atpSplitable; atpVariation Tags: atp.Splitkey=tracedFailure.shortName, traced Failure.variationPoint.shortLabel vh.latestBindingTime=preCompileTime
        self.tracedFailures: List[TracedFailure] = []

    def getTracedFailures(self) -> List[TracedFailure]:
        """
        list of traced failures Stereotypes: atpSplitable; atpVariation Tags: atp.Splitkey=tracedFailure.shortName, traced Failure.variationPoint.shortLabel vh.latestBindingTime=preCompileTime
        """
        return self.tracedFailures

    def createDevelopmentError(self, short_name: str) -> DevelopmentError:
        """
        Creates and adds a DevelopmentError traced failure for the error tracer.

        Args:
            short_name: The short name for the new development error

        Returns:
            The created DevelopmentError instance
        """
        if not self.IsElementExists(short_name, DevelopmentError):
            failure = DevelopmentError(self, short_name)
            self.addElement(failure)
            self.tracedFailures.append(failure)
        return self.getElement(short_name, DevelopmentError)

    def createRuntimeError(self, short_name: str) -> RuntimeError:
        """
        Creates and adds a RuntimeError traced failure for the error tracer.

        Args:
            short_name: The short name for the new runtime error

        Returns:
            The created RuntimeError instance
        """
        if not self.IsElementExists(short_name, RuntimeError):
            failure = RuntimeError(self, short_name)
            self.addElement(failure)
            self.tracedFailures.append(failure)
        return self.getElement(short_name, RuntimeError)

    def createTransientFault(self, short_name: str) -> TransientFault:
        """
        Creates and adds a TransientFault traced failure for the error tracer.

        Args:
            short_name: The short name for the new transient fault

        Returns:
            The created TransientFault instance
        """
        if not self.IsElementExists(short_name, TransientFault):
            failure = TransientFault(self, short_name)
            self.addElement(failure)
            self.tracedFailures.append(failure)
        return self.getElement(short_name, TransientFault)


class EventAcceptanceStatusEnum(AREnum):
    """
    This enumerator specifies the initial status for enable or disable of acceptance of event reports of a diagnostic event.
    """

    # EventAcceptanceStatusEnum method parity checklist:
    # Spec: AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf, Table 13.27, p.762
    # Spec verified: R23-11
    # Columns: impl / docstring / test / reader / writer / release   ([—] = no XML element)
    # [x] __init__    [x] impl  [x] docstring  [x] test  [—] reader  [—] writer  R23-11
    # (no methods) — serialized as an attribute value on the consuming class

    # Acceptance of a diagnostic event is disabled. Tags: atp.EnumerationLiteralIndex=0
    EVENT_ACCEPTANCE_DISABLED = "eventAcceptanceDisabled"
    # Acceptance of a diagnostic event is enabled. Tags: atp.EnumerationLiteralIndex=1
    EVENT_ACCEPTANCE_ENABLED = "eventAcceptanceEnabled"

    def __init__(self):
        super().__init__(
            (
                EventAcceptanceStatusEnum.EVENT_ACCEPTANCE_DISABLED,
                EventAcceptanceStatusEnum.EVENT_ACCEPTANCE_ENABLED,
            )
        )


class FunctionInhibitionAvailabilityNeeds(ServiceNeeds):
    """
    Specifies the abstract needs on the configuration of the Function Inhibition Manager to provide the control function for one Function Identifier (FID).
    """

    # FunctionInhibitionAvailabilityNeeds method parity checklist:
    # Spec: AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf, Table 13.13, p.751
    # Spec verified: R23-11
    # Columns: impl / docstring / test / reader / writer / release   ([—] = no XML element)
    # [x] __init__    [x] impl  [x] docstring  [x] test  [—] reader  [—] writer  R23-11
    # [x] getControlledFidRef         [x] impl  [x] docstring  [x] test  [x] reader  [x] writer  R23-11
    # [x] setControlledFidRef         [x] impl  [x] docstring  [x] test  [x] reader  [x] writer  R23-11

    def __init__(self, parent: ARObject, short_name: str):
        super().__init__(parent, short_name)

        # This reference represents the controlled FID
        self.controlledFidRef: Optional[RefType] = None

    def getControlledFidRef(self) -> Optional[RefType]:
        """
        This reference represents the controlled FID
        """
        return self.controlledFidRef

    def setControlledFidRef(self, value: Optional[RefType]) -> FunctionInhibitionAvailabilityNeeds:
        """
        This reference represents the controlled FID
        A None value is a no-op and does not overwrite an existing controlledFidRef.
        """
        if value is not None:
            self.controlledFidRef = value
        return self


class FunctionInhibitionNeeds(ServiceNeeds):
    """
    Specifies the abstract needs on the configuration of the Function Inhibition Manager for one Function Identifier (FID). This class currently contains no attributes. Its name can be regarded as a symbol identifying the FID from the viewpoint of the component or module which owns this class.
    """

    # FunctionInhibitionNeeds method parity checklist:
    # Spec: AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.pdf, Table 12.19, p.237
    # Spec verified: R23-11
    # Columns: impl / docstring / test / reader / writer / release   ([—] = no XML element)
    # [x] __init__                     [x] impl  [x] docstring  [x] test  [—] reader  [—] writer  R23-11

    def __init__(self, parent: ARObject, short_name: str):
        super().__init__(parent, short_name)


class FurtherActionByteNeeds(DoIpServiceNeeds):
    """
    The FurtherActionByteNeeds indicates that the software-component is able to provide the "further action byte" to the DoIp Service Component.
    """

    # FurtherActionByteNeeds method parity checklist:
    # Spec: AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf, Table 13.62, p.812
    # Spec verified: R23-11
    # Columns: impl / docstring / test / reader / writer / release   ([—] = no XML element)
    # [x] __init__                     [x] impl  [x] docstring  [x] test  [—] reader  [—] writer  R23-11

    def __init__(self, parent: ARObject, short_name: str):
        super().__init__(parent, short_name)


class GlobalSupervisionNeeds(ServiceNeeds):
    """
    Specifies the abstract needs on the configuration of the Watchdog Manager to get access on the Global Supervision control and status interface.
    """

    # GlobalSupervisionNeeds method parity checklist:
    # Spec: AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf, Table 13.4, p.709
    # Spec verified: R23-11
    # Columns: impl / docstring / test / reader / writer / release   ([—] = no XML element)
    # [x] __init__                     [x] impl  [x] docstring  [x] test  [—] reader  [—] writer  R23-11

    def __init__(self, parent: ARObject, short_name: str):
        super().__init__(parent, short_name)


class HardwareTestNeeds(ServiceNeeds):
    """
    This meta-class represents the ability to indicate that a software-component is interested in the results of the hardware test and will establish a PortPrototype to query the hardware test manager.
    """

    # HardwareTestNeeds method parity checklist:
    # Spec: AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.pdf, Table 12.40, p.264
    # Spec verified: R23-11
    # Columns: impl / docstring / test / reader / writer / release   ([—] = no XML element)
    # [x] __init__                     [x] impl  [x] docstring  [x] test  [—] reader  [—] writer  R23-11

    def __init__(self, parent: ARObject, short_name: str):
        super().__init__(parent, short_name)


class IdsMgrCustomTimestampNeeds(ServiceNeeds):
    """
    This meta-class is used to indicate that the enclosing SwcServiceDependency represents a service use case for the retrieval of a custom timestamp by the Intrusion Detection System Manager. Tags: atp.Status=draft
    """

    # IdsMgrCustomTimestampNeeds method parity checklist:
    # Spec: AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf, Table 13.82, p.842
    # Spec verified: R23-11
    # Columns: impl / docstring / test / reader / writer / release   ([—] = no XML element)
    # [x] __init__                     [x] impl  [x] docstring  [x] test  [—] reader  [—] writer  R23-11

    def __init__(self, parent: ARObject, short_name: str):
        super().__init__(parent, short_name)


class IdsMgrNeeds(ServiceNeeds):
    """
    This meta-class is used to indicate that the enclosing SwcServiceDependency represents a service use case for the Intrusion Detection System Manager. Tags: atp.Status=draft
    """

    # IdsMgrNeeds method parity checklist:
    # Spec: AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf, Table 13.81, p.842
    # Spec verified: R23-11
    # [x] __init__                [x] impl  [x] docstring  [x] test  [—] reader  [—] writer
    # [x] getUseSmartSensorApi    [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] setUseSmartSensorApi    [x] impl  [x] docstring  [x] test  [x] reader  [—] writer

    def __init__(self, parent: ARObject, short_name: str):
        super().__init__(parent, short_name)

        # This attribute controls whether the reporting of the security event shall be done by means of the smart sensor API.
        self.useSmartSensorApi: Optional[Boolean] = None

    def getUseSmartSensorApi(self) -> Optional[Boolean]:
        """
        This attribute controls whether the reporting of the security event shall be done by means of the smart sensor API.

        Returns:
            Boolean instance, or None if not set
        """
        return self.useSmartSensorApi

    def setUseSmartSensorApi(self, value: Optional[Boolean]) -> IdsMgrNeeds:
        """
        This attribute controls whether the reporting of the security event shall be done by means of the smart sensor API.
        A None value is a no-op and does not overwrite an existing useSmartSensorApi.

        Args:
            value: The Boolean instance to set

        Returns:
            self for method chaining
        """
        if value is not None:
            self.useSmartSensorApi = value
        return self


class DiagnosticIndicatorTypeEnum(AREnum):
    """
    Type of an indicator.
    """

    # DiagnosticIndicatorTypeEnum method parity checklist:
    # Spec: AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf, Table 13.31, p.766
    # Spec verified: R23-11
    # Columns: impl / docstring / test / reader / writer / release   ([—] = no XML element)
    # [x] __init__    [x] impl  [x] docstring  [x] test  [—] reader  [—] writer  R23-11
    # (no methods) — serialized as an attribute value on the consuming class

    # Amber Warning Lamp Tags: atp.EnumerationLiteralIndex=0
    AMBER_WARNING = "amberWarning"

    # Malfunction Indicator Lamp Tags: atp.EnumerationLiteralIndex=1
    MALFUNCTION = "malfunction"

    # Protect Lamp Tags: atp.EnumerationLiteralIndex=2
    PROTECT_LAMP = "protectLamp"

    # Red Stop Lamp Tags: atp.EnumerationLiteralIndex=3
    RED_STOP_LAMP = "redStopLamp"

    # Warning Tags: atp.EnumerationLiteralIndex=4
    WARNING = "warning"

    def __init__(self):
        """
        Initializes the DiagnosticIndicatorTypeEnum with all possible values.
        """
        super().__init__(
            (
                DiagnosticIndicatorTypeEnum.AMBER_WARNING,
                DiagnosticIndicatorTypeEnum.MALFUNCTION,
                DiagnosticIndicatorTypeEnum.PROTECT_LAMP,
                DiagnosticIndicatorTypeEnum.RED_STOP_LAMP,
                DiagnosticIndicatorTypeEnum.WARNING,
            )
        )


class IndicatorStatusNeeds(ServiceNeeds):
    """
    This meta-class shall be taken to signal a service use case that affects the indicator status.
    """

    # IndicatorStatusNeeds method parity checklist:
    # Spec: AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf, Table 13.30, p.766
    # Spec verified: R23-11
    # Columns: impl / docstring / test / reader / writer / release   ([—] = no XML element)
    # [x] __init__    [x] impl  [x] docstring  [x] test  [—] reader  [—] writer  R23-11
    # [x] getType                     [x] impl  [x] docstring  [x] test  [x] reader  [x] writer  R23-11
    # [x] setType                     [x] impl  [x] docstring  [x] test  [x] reader  [x] writer  R23-11

    def __init__(self, parent: ARObject, short_name: str):
        super().__init__(parent, short_name)

        # Defines the type of the indicator.
        self.type: Optional[DiagnosticIndicatorTypeEnum] = None

    def getType(self) -> Optional[DiagnosticIndicatorTypeEnum]:
        """
        Defines the type of the indicator.
        """
        return self.type

    def setType(self, value: Optional[DiagnosticIndicatorTypeEnum]) -> IndicatorStatusNeeds:
        """
        Defines the type of the indicator.
        A None value is a no-op and does not overwrite an existing type.
        """
        if value is not None:
            self.type = value
        return self


class J1939DcmDm19Support(ServiceNeeds):
    """
    The software-component provides information about calibration verification numbers for inclusion in DM19
    """

    # J1939DcmDm19Support method parity checklist:
    # Spec: AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf, Table 13.72, p.831
    # Spec verified: R23-11
    # Columns: impl / docstring / test / reader / writer / release   ([—] = no XML element)
    # [x] __init__                     [x] impl  [x] docstring  [x] test  [—] reader  [—] writer  R23-11

    def __init__(self, parent: ARObject, short_name: str):
        super().__init__(parent, short_name)


class J1939RmIncomingRequestServiceNeeds(ServiceNeeds):
    """
    "This meta-class shall be used to specify needs with respect to the configuration of the J1939Rm, in particular for the case where an ApplicationSwComponentType needs to accept a request from another J1939 node.
    """

    # J1939RmIncomingRequestServiceNeeds method parity checklist:
    # Spec: AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf, Table 13.71, p.829
    # Spec verified: R23-11
    # Columns: impl / docstring / test / reader / writer / release   ([—] = no XML element)
    # [x] __init__                     [x] impl  [x] docstring  [x] test  [—] reader  [—] writer  R23-11

    def __init__(self, parent: ARObject, short_name: str):
        super().__init__(parent, short_name)


class J1939RmOutgoingRequestServiceNeeds(ServiceNeeds):
    """
    This meta-class shall be used to specify needs with respect to the configuration of the J1939Rm, in particular for the case where an ApplicationSwComponentType needs to send a request to another J1939 node.
    """

    # J1939RmOutgoingRequestServiceNeeds method parity checklist:
    # Spec: AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf, Table 13.70, p.829
    # Spec verified: R23-11
    # Columns: impl / docstring / test / reader / writer / release   ([—] = no XML element)
    # [x] __init__                     [x] impl  [x] docstring  [x] test  [—] reader  [—] writer  R23-11

    def __init__(self, parent: ARObject, short_name: str):
        super().__init__(parent, short_name)


class MaxCommModeEnum(AREnum):
    """
    Maximum bus communication mode required by a user of the Communication Manager Service.
    """

    # MaxCommModeEnum method parity checklist:
    # Spec: AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf, Table 13.6, p.711
    # Spec verified: R23-11
    # Columns: impl / docstring / test / reader / writer / release   ([—] = no XML element)
    # [x] __init__    [x] impl  [x] docstring  [x] test  [—] reader  [—] writer  R23-11
    # (no methods) — serialized as an attribute value on the consuming class

    # Full communication is requested. Tags: atp.EnumerationLiteralIndex=0
    FULL = "full"

    # No communication is requested. Tags: atp.EnumerationLiteralIndex=1
    NONE = "none"

    # Silent communication is requested: Only listening but not "talking". Tags: atp.EnumerationLiteralIndex=2
    SILENT = "silent"

    def __init__(self):
        """
        Initializes the MaxCommModeEnum with all possible values.
        """
        super().__init__(
            (
                MaxCommModeEnum.FULL,
                MaxCommModeEnum.NONE,
                MaxCommModeEnum.SILENT,
            )
        )


class ObdControlServiceNeeds(DiagnosticCapabilityElement):
    """
    Specifies the abstract needs of a component or module on the configuration of OBD Service 08 (request control of on-board system) in relation to a particular test-Identifier (TID) supported by this component or module.
    """

    # ObdControlServiceNeeds method parity checklist:
    # Spec: AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf, Table 13.45, p.796
    # Spec verified: R23-11
    # Columns: impl / docstring / test / reader / writer / release   ([—] = no XML element)
    # [x] __init__    [x] impl  [x] docstring  [x] test  [—] reader  [—] writer  R23-11

    def __init__(self, parent: ARObject, short_name: str):
        super().__init__(parent, short_name)


class ObdInfoServiceNeeds(DiagnosticCapabilityElement):
    """
    Specifies the abstract needs of a component or module on the configuration of OBD Services in relation to a given InfoType (OBD Service 09) which is supported by this component or module.
    """

    # ObdInfoServiceNeeds method parity checklist:
    # Spec: AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf, Table 13.48, p.797
    # Spec verified: R23-11
    # Columns: impl / docstring / test / reader / writer / release   ([—] = no XML element)
    # [x] __init__    [x] impl  [x] docstring  [x] test  [—] reader  [—] writer  R23-11

    def __init__(self, parent: ARObject, short_name: str):
        super().__init__(parent, short_name)


class ObdMonitorServiceNeeds(DiagnosticCapabilityElement):
    """
    Specifies the abstract needs of a component or module on the configuration of OBD Services in relation to a particular on-board monitoring test supported by this component or module. (OBD Service 06).
    """

    # ObdMonitorServiceNeeds method parity checklist:
    # Spec: AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf, Table 13.49, p.798
    # Spec verified: R23-11
    # Columns: impl / docstring / test / reader / writer / release   ([—] = no XML element)
    # [x] __init__    [x] impl  [x] docstring  [x] test  [—] reader  [—] writer  R23-11
    # [x] getApplicationDataTypeRef   [x] impl  [x] docstring  [x] test  [x] reader  [x] writer  R23-11
    # [x] setApplicationDataTypeRef   [x] impl  [x] docstring  [x] test  [x] reader  [x] writer  R23-11
    # [x] getEventNeedsRef            [x] impl  [x] docstring  [x] test  [x] reader  [x] writer  R23-11
    # [x] setEventNeedsRef            [x] impl  [x] docstring  [x] test  [x] reader  [x] writer  R23-11
    # [x] getUnitAndScalingId         [x] impl  [x] docstring  [x] test  [x] reader  [x] writer  R23-11
    # [x] setUnitAndScalingId         [x] impl  [x] docstring  [x] test  [x] reader  [x] writer  R23-11
    # [x] getUpdateKind               [x] impl  [x] docstring  [x] test  [x] reader  [x] writer  R23-11
    # [x] setUpdateKind               [x] impl  [x] docstring  [x] test  [x] reader  [x] writer  R23-11

    def __init__(self, parent: ARObject, short_name: str):
        super().__init__(parent, short_name)

        # reference to an ApplicationDataType that describes the scaling of the data reported by the software-component to the Dem.
        self.applicationDataTypeRef: Optional[RefType] = None

        # This reference identifies the corresponding diagnostic event.
        self.eventNeedsRef: Optional[RefType] = None

        # Unit and scaling ID according to ISO 15031-5.
        self.unitAndScalingId: Optional[PositiveInteger] = None

        # This attribute indicates the settings for the acceptance of updates to the Dem.
        self.updateKind: Optional[DiagnosticMonitorUpdateKindEnum] = None

    def getApplicationDataTypeRef(self) -> Optional[RefType]:
        """
        reference to an ApplicationDataType that describes the scaling of the data reported by the software-component to the Dem.
        """
        return self.applicationDataTypeRef

    def setApplicationDataTypeRef(self, value: Optional[RefType]) -> ObdMonitorServiceNeeds:
        """
        reference to an ApplicationDataType that describes the scaling of the data reported by the software-component to the Dem.
        A None value is a no-op and does not overwrite an existing applicationDataTypeRef.
        """
        if value is not None:
            self.applicationDataTypeRef = value
        return self

    def getEventNeedsRef(self) -> Optional[RefType]:
        """
        This reference identifies the corresponding diagnostic event.
        """
        return self.eventNeedsRef

    def setEventNeedsRef(self, value: Optional[RefType]) -> ObdMonitorServiceNeeds:
        """
        This reference identifies the corresponding diagnostic event.
        A None value is a no-op and does not overwrite an existing eventNeedsRef.
        """
        if value is not None:
            self.eventNeedsRef = value
        return self

    def getUnitAndScalingId(self) -> Optional[PositiveInteger]:
        """
        Unit and scaling ID according to ISO 15031-5.
        """
        return self.unitAndScalingId

    def setUnitAndScalingId(self, value: Optional[PositiveInteger]) -> ObdMonitorServiceNeeds:
        """
        Unit and scaling ID according to ISO 15031-5.
        A None value is a no-op and does not overwrite an existing unitAndScalingId.
        """
        if value is not None:
            self.unitAndScalingId = value
        return self

    def getUpdateKind(self) -> Optional[DiagnosticMonitorUpdateKindEnum]:
        """
        This attribute indicates the settings for the acceptance of updates to the Dem.
        """
        return self.updateKind

    def setUpdateKind(self, value: Optional[DiagnosticMonitorUpdateKindEnum]) -> ObdMonitorServiceNeeds:
        """
        This attribute indicates the settings for the acceptance of updates to the Dem.
        A None value is a no-op and does not overwrite an existing updateKind.
        """
        if value is not None:
            self.updateKind = value
        return self


class ObdPidServiceNeeds(DiagnosticCapabilityElement):
    """
    Specifies the abstract needs of a component or module on the configuration of OBD Services in relation to a particular PID (parameter identifier) which is supported by this component or module. In case of using a client/server communicated value, the related value shall be communicated via the port referenced by assignedPort. The details of this communication (e.g. appropriate naming conventions) are specified in the related software specifications (SWS).
    """

    # ObdPidServiceNeeds method parity checklist:
    # Spec: AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf, Table 13.47, p.797
    # Spec verified: R23-11
    # Columns: impl / docstring / test / reader / writer / release   ([—] = no XML element)
    # [x] __init__    [x] impl  [x] docstring  [x] test  [—] reader  [—] writer  R23-11

    def __init__(self, parent: ARObject, short_name: str):
        super().__init__(parent, short_name)


class ObdRatioConnectionKindEnum(AREnum):
    """
    Defines the way how the IUMPR service connection between the Dem and the client component or module is handled (for details see the DEM Specification).
    """

    # ObdRatioConnectionKindEnum method parity checklist:
    # Spec: AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf, Table 13.46, p.796
    # Spec verified: R23-11
    # Columns: impl / docstring / test / reader / writer / release   ([—] = no XML element)
    # [x] __init__    [x] impl  [x] docstring  [x] test  [—] reader  [—] writer  R23-11
    # (no methods) — serialized as an attribute value on the consuming class

    # The IUMPR service (of the DEM) uses an explicit API to connect to the component or module. Tags: atp.EnumerationLiteralIndex=0
    API_USE = "apiUse"
    # The IUMPR service (of the Dem) uses no API but "observes" the associated diagnostic event. Tags: atp.EnumerationLiteralIndex=1
    OBSERVER = "observer"

    def __init__(self):
        super().__init__(
            [
                ObdRatioConnectionKindEnum.API_USE,
                ObdRatioConnectionKindEnum.OBSERVER,
            ]
        )


class ObdRatioDenominatorNeeds(ServiceNeeds):
    """
    This meta-class shall be used to indicate that a software-component wants to access the in-use-monitoring performance ration denominator.
    """

    # ObdRatioDenominatorNeeds method parity checklist:
    # Spec: AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf, Table 13.51, p.803
    # Spec verified: R23-11
    # [x] __init__                        [x] impl  [x] docstring  [x] test  [—] reader  [—] writer
    # [x] getDenominatorCondition         [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] setDenominatorCondition         [x] impl  [x] docstring  [x] test  [x] reader  [—] writer

    def __init__(self, parent: ARObject, short_name: str):
        super().__init__(parent, short_name)

        # This attribute indicates the applicable denominator condition.
        self.denominatorCondition: Optional[DiagnosticDenominatorConditionEnum] = None

    def getDenominatorCondition(self) -> Optional[DiagnosticDenominatorConditionEnum]:
        """
        This attribute indicates the applicable denominator condition.

        Returns:
            DiagnosticDenominatorConditionEnum instance, or None if not set
        """
        return self.denominatorCondition

    def setDenominatorCondition(self, value: Optional[DiagnosticDenominatorConditionEnum]) -> ObdRatioDenominatorNeeds:
        """
        This attribute indicates the applicable denominator condition.
        A None value is a no-op and does not overwrite an existing denominatorCondition.

        Args:
            value: The DiagnosticDenominatorConditionEnum instance to set

        Returns:
            self for method chaining
        """
        if value is not None:
            self.denominatorCondition = value
        return self


class ObdRatioServiceNeeds(DiagnosticCapabilityElement):
    """
    Specifies the abstract needs of a component or module on the configuration of OBD Services in relation to a particular "ratio monitoring" which is supported by this component or module.
    """

    # ObdRatioServiceNeeds method parity checklist:
    # Spec: AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf, Table 13.44, p.795
    # Spec verified: R23-11
    # [x] __init__                          [x] impl  [x] docstring  [x] test  [—] reader  [—] writer
    # [x] getConnectionType                 [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] setConnectionType                 [x] impl  [x] docstring  [x] test  [x] reader  [—] writer
    # [x] getRateBasedMonitoredEventRef     [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] setRateBasedMonitoredEventRef     [x] impl  [x] docstring  [x] test  [x] reader  [—] writer
    # [x] getUsedFidRef                     [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] setUsedFidRef                     [x] impl  [x] docstring  [x] test  [x] reader  [—] writer

    def __init__(self, parent: ARObject, short_name: str):
        super().__init__(parent, short_name)

        # Defines how the DEM is connected to the component or module to perform the IUMPR (In use monitor performance ratio) service.
        self.connectionType: Optional[ObdRatioConnectionKindEnum] = None

        # The rate based monitored Diagnostic Event.
        self.rateBasedMonitoredEventRef: Optional[RefType] = None

        # This represents the primary Function Inhibition Identifier used for the rate based monitor. This is an optional attribute.
        self.usedFidRef: Optional[RefType] = None

    def getConnectionType(self) -> Optional[ObdRatioConnectionKindEnum]:
        """
        Defines how the DEM is connected to the component or module to perform the IUMPR (In use monitor performance ratio) service.

        Returns:
            ObdRatioConnectionKindEnum instance, or None if not set
        """
        return self.connectionType

    def setConnectionType(self, value: Optional[ObdRatioConnectionKindEnum]) -> ObdRatioServiceNeeds:
        """
        Defines how the DEM is connected to the component or module to perform the IUMPR (In use monitor performance ratio) service.
        A None value is a no-op and does not overwrite an existing connectionType.

        Args:
            value: The ObdRatioConnectionKindEnum instance to set

        Returns:
            self for method chaining
        """
        if value is not None:
            self.connectionType = value
        return self

    def getRateBasedMonitoredEventRef(self) -> Optional[RefType]:
        """
        The rate based monitored Diagnostic Event.

        Returns:
            RefType instance, or None if not set
        """
        return self.rateBasedMonitoredEventRef

    def setRateBasedMonitoredEventRef(self, value: Optional[RefType]) -> ObdRatioServiceNeeds:
        """
        The rate based monitored Diagnostic Event.
        A None value is a no-op and does not overwrite an existing rateBasedMonitoredEventRef.

        Args:
            value: The RefType instance to set

        Returns:
            self for method chaining
        """
        if value is not None:
            self.rateBasedMonitoredEventRef = value
        return self

    def getUsedFidRef(self) -> Optional[RefType]:
        """
        This represents the primary Function Inhibition Identifier used for the rate based monitor. This is an optional attribute.

        Returns:
            RefType instance, or None if not set
        """
        return self.usedFidRef

    def setUsedFidRef(self, value: Optional[RefType]) -> ObdRatioServiceNeeds:
        """
        This represents the primary Function Inhibition Identifier used for the rate based monitor. This is an optional attribute.
        A None value is a no-op and does not overwrite an existing usedFidRef.

        Args:
            value: The RefType instance to set

        Returns:
            self for method chaining
        """
        if value is not None:
            self.usedFidRef = value
        return self


class OperationCycleTypeEnum(AREnum):
    """
    The possible values of the operation cycles types for the Dem.
    """

    # OperationCycleTypeEnum method parity checklist:
    # Spec: AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf, Table 13.25, p.761
    # Spec verified: R23-11
    # Columns: impl / docstring / test / reader / writer / release   ([—] = no XML element)
    # [x] __init__    [x] impl  [x] docstring  [x] test  [—] reader  [—] writer  R23-11
    # (no methods) — serialized as an attribute value on the consuming class

    # Ignition ON / OFF cycle. Tags: atp.EnumerationLiteralIndex=0
    IGNITION = "ignition"
    # OBD Driving cycle. Tags: atp.EnumerationLiteralIndex=1
    OBD_DCY = "obdDcy"
    # Further operation cycle. Tags: atp.EnumerationLiteralIndex=2
    OTHER = "other"
    # Power ON / OFF cycle. Tags: atp.EnumerationLiteralIndex=3
    POWER = "power"
    # Time based operation cycle. Tags: atp.EnumerationLiteralIndex=4
    TIME = "time"
    # OBD Warm up cycle. Tags: atp.EnumerationLiteralIndex=5
    WARMUP = "warmup"

    def __init__(self):
        super().__init__(
            (
                OperationCycleTypeEnum.IGNITION,
                OperationCycleTypeEnum.OBD_DCY,
                OperationCycleTypeEnum.OTHER,
                OperationCycleTypeEnum.POWER,
                OperationCycleTypeEnum.TIME,
                OperationCycleTypeEnum.WARMUP,
            )
        )


class RuntimeError(TracedFailure):
    """
    The reported failure is classified as runtime error.
    """

    # RuntimeError method parity checklist:
    # Spec: AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.pdf, Table 12.39, p.263
    # Spec verified: R23-11
    # Columns: impl / docstring / test / reader / writer / release   ([—] = no XML element)
    # [x] __init__    [x] impl  [x] docstring  [x] test  [—] reader  [—] writer  R23-11

    def __init__(self, parent: ARObject, short_name: str):
        super().__init__(parent, short_name)


class SecureOnBoardCommunicationNeeds(ServiceNeeds):
    """
    Specifies the need for the existence of the SecOc module on the respective ECU. This class currently contains no attributes. An instance of this class is used to find out which ports of a software-component deal with the administration of secure communication in order to group the request and response ports.
    """

    # SecureOnBoardCommunicationNeeds method parity checklist:
    # Spec: AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf, Table 13.68, p.824
    # Spec verified: R23-11
    # [x] __init__                              [x] impl  [x] docstring  [x] test  [—] reader  [—] writer
    # [x] getVerificationStatusIndicationMode   [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] setVerificationStatusIndicationMode   [x] impl  [x] docstring  [x] test  [x] reader  [—] writer

    def __init__(self, parent: ARObject, short_name: str):
        super().__init__(parent, short_name)

        # This attribute provides the ability to control the mode in which the application software is notified about the result of authentication attempts.
        self.verificationStatusIndicationMode: Optional[VerificationStatusIndicationModeEnum] = None

    def getVerificationStatusIndicationMode(self) -> Optional[VerificationStatusIndicationModeEnum]:
        """
        This attribute provides the ability to control the mode in which the application software is notified about the result of authentication attempts.

        Returns:
            VerificationStatusIndicationModeEnum instance, or None if not set
        """
        return self.verificationStatusIndicationMode

    def setVerificationStatusIndicationMode(self, value: Optional[VerificationStatusIndicationModeEnum]) -> SecureOnBoardCommunicationNeeds:
        """
        This attribute provides the ability to control the mode in which the application software is notified about the result of authentication attempts.
        A None value is a no-op and does not overwrite an existing verificationStatusIndicationMode.

        Args:
            value: The VerificationStatusIndicationModeEnum instance to set

        Returns:
            self for method chaining
        """
        if value is not None:
            self.verificationStatusIndicationMode = value
        return self


class ServiceProviderEnum(AREnum):
    """
    This represents a list of possible service providers
    """

    # ServiceProviderEnum method parity checklist:
    # Spec: AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf, Table 3.20, p.90
    # Spec verified: R23-11
    # Columns: impl / docstring / test / reader / writer / release   ([—] = no XML element)
    # [x] __init__    [x] impl  [x] docstring  [x] test  [—] reader  [—] writer  R23-11
    # (no methods) — serialized as an attribute value on the consuming class

    # This value means that the specific nature is either unknown or it is not important for the given purpose. This is also the default value for any attribute of type ServiceProviderEnum Tags: atp.EnumerationLiteralIndex=0
    ANY_STANDARDIZED = "anyStandardized"

    # The service relates to the Basic Software Mode Manager (BswM) Tags: atp.EnumerationLiteralIndex=1
    BASIC_SOFTWARE_MODE_MANAGER = "basicSoftwareModeManager"

    # The service relates to the COM Manager (ComM). Tags: atp.EnumerationLiteralIndex=2
    COM_MANAGER = "comManager"

    # The service relates to the Key Manager (KeyM). Tags: atp.EnumerationLiteralIndex=23
    CRYPTO_KEY_MANAGEMENT = "cryptoKeyManagement"

    # The service relates to the Crypto Service Manager (CsM). Tags: atp.EnumerationLiteralIndex=3
    CRYPTO_SERVICE_MANAGER = "cryptoServiceManager"

    # The service relates to the Default Error Tracer (DET) Tags: atp.EnumerationLiteralIndex=4
    DEFAULT_ERROR_TRACER = "defaultErrorTracer"

    # The service relates to the Diagnostic Communication Manager (DCM). Tags: atp.EnumerationLiteralIndex=6
    DIAGNOSTIC_COMMUNICATION_MANAGER = "diagnosticCommunicationManager"

    # The service relates to the Diagnostic Event Manager (DEM). Tags: atp.EnumerationLiteralIndex=7
    DIAGNOSTIC_EVENT_MANAGER = "diagnosticEventManager"

    # The service relates to the Diagnostic Log and Trace (DLT). Tags: atp.EnumerationLiteralIndex=8
    DIAGNOSTIC_LOG_AND_TRACE = "diagnosticLogAndTrace"

    # The service relates to the ECU Manager (EcuM). Tags: atp.EnumerationLiteralIndex=9
    ECU_MANAGER = "ecuManager"

    # This service relates to the error tracer. Tags: atp.EnumerationLiteralIndex=18
    ERROR_TRACER = "errorTracer"

    # The service relates to the Function Inhibition Manager (FIM). Tags: atp.EnumerationLiteralIndex=10
    FUNCTION_INHIBITION_MANAGER = "functionInhibitionManager"

    # This service relates to the hardware test manager. Tags: atp.EnumerationLiteralIndex=19
    HARDWARE_TEST_MANAGER = "hardwareTestManager"

    # The service relates to the intrusion detection security management (IdsM). Tags: atp.EnumerationLiteralIndex=24
    INTRUSION_DETECTION_SECURITY_MANAGEMENT = "intrusionDetectionSecurityManagement"

    # This service relates to the J1939 Dcm. Tags: atp.EnumerationLiteralIndex=22
    J1939_DCM = "j1939Dcm"

    # The service relates to the J1939Rm. Tags: atp.EnumerationLiteralIndex=11
    J1939_REQUEST_MANAGER = "j1939RequestManager"

    # The service relates to the Non-Volatile RAM Manager (NvM). Tags: atp.EnumerationLiteralIndex=12
    NON_VOLATILE_RAM_MANAGER = "nonVolatileRamManager"

    # The service relates to the Operating System (OS). Tags: atp.EnumerationLiteralIndex=13
    OPERATING_SYSTEM = "operatingSystem"

    # The service relates to the SecOc module. Tags: atp.EnumerationLiteralIndex=14
    SECURE_ON_BOARD_COMMUNICATION = "secureOnBoardCommunication"

    # The service relates to the Sync Time Base Manager (StbM). Tags: atp.EnumerationLiteralIndex=15
    SYNC_BASE_TIME_MANAGER = "syncBaseTimeManager"

    # This service relates to the Vehicle to X facilities. Tags: atp.EnumerationLiteralIndex=20
    V2X_FACILITIES = "v2xFacilities"

    # This service relates to the Vehicle to X management. Tags: atp.EnumerationLiteralIndex=21
    V2X_MANAGEMENT = "v2xManagement"

    # This value denotes a vendor-specific service. Tags: atp.EnumerationLiteralIndex=16
    VENDOR_SPECIFIC = "vendorSpecific"

    # The service relates to the Watchdog Manager (WdgM). Tags: atp.EnumerationLiteralIndex=17
    WATCH_DOG_MANAGER = "watchDogManager"

    def __init__(self):
        """
        Initializes a ServiceProviderEnum instance with the spec-defined literals.
        """
        super().__init__(
            (
                ServiceProviderEnum.ANY_STANDARDIZED,
                ServiceProviderEnum.BASIC_SOFTWARE_MODE_MANAGER,
                ServiceProviderEnum.COM_MANAGER,
                ServiceProviderEnum.CRYPTO_KEY_MANAGEMENT,
                ServiceProviderEnum.CRYPTO_SERVICE_MANAGER,
                ServiceProviderEnum.DEFAULT_ERROR_TRACER,
                ServiceProviderEnum.DIAGNOSTIC_COMMUNICATION_MANAGER,
                ServiceProviderEnum.DIAGNOSTIC_EVENT_MANAGER,
                ServiceProviderEnum.DIAGNOSTIC_LOG_AND_TRACE,
                ServiceProviderEnum.ECU_MANAGER,
                ServiceProviderEnum.ERROR_TRACER,
                ServiceProviderEnum.FUNCTION_INHIBITION_MANAGER,
                ServiceProviderEnum.HARDWARE_TEST_MANAGER,
                ServiceProviderEnum.INTRUSION_DETECTION_SECURITY_MANAGEMENT,
                ServiceProviderEnum.J1939_DCM,
                ServiceProviderEnum.J1939_REQUEST_MANAGER,
                ServiceProviderEnum.NON_VOLATILE_RAM_MANAGER,
                ServiceProviderEnum.OPERATING_SYSTEM,
                ServiceProviderEnum.SECURE_ON_BOARD_COMMUNICATION,
                ServiceProviderEnum.SYNC_BASE_TIME_MANAGER,
                ServiceProviderEnum.V2X_FACILITIES,
                ServiceProviderEnum.V2X_MANAGEMENT,
                ServiceProviderEnum.VENDOR_SPECIFIC,
            )
        )


class StorageConditionStatusEnum(AREnum):
    """
    This enumeration specifies the initial status for enable or disable of storage of a diagnostic event.
    """

    # StorageConditionStatusEnum method parity checklist:
    # Spec: AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf, Table 13.29, p.762
    # Spec verified: R23-11
    # Columns: impl / docstring / test / reader / writer / release   ([—] = no XML element)
    # [x] __init__    [x] impl  [x] docstring  [x] test  [—] reader  [—] writer  R23-11
    # (no methods) — serialized as an attribute value on the consuming class

    # Storage of a diagnostic event is disabled. Tags: atp.EnumerationLiteralIndex=0
    EVENT_STORAGE_DISABLE = "eventStorageDisabled"
    # Storage of a diagnostic event is enabled. Tags: atp.EnumerationLiteralIndex=1
    EVENT_STORAGE_ENABLE = "eventStorageEnabled"

    def __init__(self):
        super().__init__(
            (
                StorageConditionStatusEnum.EVENT_STORAGE_DISABLE,
                StorageConditionStatusEnum.EVENT_STORAGE_ENABLE,
            )
        )


class SupervisedEntityCheckpointNeeds(ServiceNeeds):
    """
    Specifies the abstract needs on the configuration of the Watchdog Manager to support a Checkpoint for a Supervised Entity.
    """

    # SupervisedEntityCheckpointNeeds method parity checklist:
    # Spec: AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.pdf, Table 12.30, p.254
    # Spec verified: R23-11
    # Columns: impl / docstring / test / reader / writer / release   ([—] = no XML element)
    # [x] __init__                     [x] impl  [x] docstring  [x] test  [—] reader  [—] writer  R23-11

    def __init__(self, parent: ARObject, short_name: str):
        super().__init__(parent, short_name)


class SupervisedEntityNeeds(ServiceNeeds):
    """
    Specifies the abstract needs on the configuration of the Watchdog Manager for one specific Supervised Entity.
    """

    # SupervisedEntityNeeds method parity checklist:
    # Spec: AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.pdf, Table 12.12, p.234
    # Spec verified: R23-11
    # Columns: impl / docstring / test / reader / writer / release   ([—] = no XML element)
    # [x] __init__    [x] impl  [x] docstring  [x] test  [—] reader  [—] writer  R23-11
    # [x] getActivateAtStart          [x] impl  [x] docstring  [x] test  [x] reader  [x] writer  R23-11
    # [x] setActivateAtStart          [x] impl  [x] docstring  [x] test  [x] reader  [x] writer  R23-11
    # [x] getCheckpointsRefs          [x] impl  [x] docstring  [x] test  [x] reader  [x] writer  R23-11
    # [x] addCheckpointsRef           [x] impl  [x] docstring  [x] test  [x] reader  [x] writer  R23-11
    # [x] getEnableDeactivation       [x] impl  [x] docstring  [x] test  [x] reader  [x] writer  R23-11
    # [x] setEnableDeactivation       [x] impl  [x] docstring  [x] test  [x] reader  [x] writer  R23-11
    # [x] getExpectedAliveCycle       [x] impl  [x] docstring  [x] test  [x] reader  [x] writer  R23-11
    # [x] setExpectedAliveCycle       [x] impl  [x] docstring  [x] test  [x] reader  [x] writer  R23-11
    # [x] getMaxAliveCycle            [x] impl  [x] docstring  [x] test  [x] reader  [x] writer  R23-11
    # [x] setMaxAliveCycle            [x] impl  [x] docstring  [x] test  [x] reader  [x] writer  R23-11
    # [x] getMinAliveCycle            [x] impl  [x] docstring  [x] test  [x] reader  [x] writer  R23-11
    # [x] setMinAliveCycle            [x] impl  [x] docstring  [x] test  [x] reader  [x] writer  R23-11
    # [x] getToleratedFailedCycles    [x] impl  [x] docstring  [x] test  [x] reader  [x] writer  R23-11
    # [x] setToleratedFailedCycles    [x] impl  [x] docstring  [x] test  [x] reader  [x] writer  R23-11

    def __init__(self, parent: ARObject, short_name: str):
        super().__init__(parent, short_name)

        # true/false: supervision activation status of Supervised Entity shall be enabled/disabled at start.
        self.activateAtStart: Optional[Boolean] = None

        # This reference indicates the checkpoints belonging to the Supervised Entity. Stereotypes: atpSplitable; atpVariation Tags: atp.Splitkey=checkpoints.supervisedEntityCheckpoint Needs, checkpoints.variationPoint.shortLabel vh.latestBindingTime=preCompileTime
        self.checkpointsRefs: List[RefType] = []

        # true: software-component shall be allowed to deactivate supervision of this SupervisedEntity false: software-component shall be not allowed to deactivate supervision of this SupervisedEntity
        self.enableDeactivation: Optional[Boolean] = None

        # Expected cycle time of alive trigger of this Supervised Entity (in seconds).
        self.expectedAliveCycle: Optional[TimeValue] = None

        # Maximum cycle time of alive trigger of this Supervised Entity (in seconds).
        self.maxAliveCycle: Optional[TimeValue] = None

        # Minimum cycle time of alive trigger of this Supervised Entity (in seconds).
        self.minAliveCycle: Optional[TimeValue] = None

        # Number of consecutive failed alive cycles for this SupervisedEntity which shall be tolerated until the supervision status of the SupervisedEntity is set to WDGM_ALIVE_EXPIRED (see SWS WdgM for more details). Note that this value has to be recalculated with respect to the WdgM's own cycle time for ECU configuration.
        self.toleratedFailedCycles: Optional[PositiveInteger] = None

    def getActivateAtStart(self) -> Optional[Boolean]:
        """
        true/false: supervision activation status of Supervised Entity shall be enabled/disabled at start.
        """
        return self.activateAtStart

    def setActivateAtStart(self, value: Optional[Boolean]) -> SupervisedEntityNeeds:
        """
        true/false: supervision activation status of Supervised Entity shall be enabled/disabled at start.
        A None value is a no-op and does not overwrite an existing activateAtStart.
        """
        if value is not None:
            self.activateAtStart = value
        return self

    def addCheckpointsRef(self, value: Optional[RefType]) -> SupervisedEntityNeeds:
        """
        This reference indicates the checkpoints belonging to the Supervised Entity. Stereotypes: atpSplitable; atpVariation Tags: atp.Splitkey=checkpoints.supervisedEntityCheckpoint Needs, checkpoints.variationPoint.shortLabel vh.latestBindingTime=preCompileTime
        A None value is a no-op and does not append to checkpointsRefs.
        """
        if value is not None:
            self.checkpointsRefs.append(value)
        return self

    def getCheckpointsRefs(self) -> List[RefType]:
        """
        This reference indicates the checkpoints belonging to the Supervised Entity. Stereotypes: atpSplitable; atpVariation Tags: atp.Splitkey=checkpoints.supervisedEntityCheckpoint Needs, checkpoints.variationPoint.shortLabel vh.latestBindingTime=preCompileTime
        """
        return self.checkpointsRefs

    def getEnableDeactivation(self) -> Optional[Boolean]:
        """
        true: software-component shall be allowed to deactivate supervision of this SupervisedEntity false: software-component shall be not allowed to deactivate supervision of this SupervisedEntity
        """
        return self.enableDeactivation

    def setEnableDeactivation(self, value: Optional[Boolean]) -> SupervisedEntityNeeds:
        """
        true: software-component shall be allowed to deactivate supervision of this SupervisedEntity false: software-component shall be not allowed to deactivate supervision of this SupervisedEntity
        A None value is a no-op and does not overwrite an existing enableDeactivation.
        """
        if value is not None:
            self.enableDeactivation = value
        return self

    def getExpectedAliveCycle(self) -> Optional[TimeValue]:
        """
        Expected cycle time of alive trigger of this Supervised Entity (in seconds).
        """
        return self.expectedAliveCycle

    def setExpectedAliveCycle(self, value: Optional[TimeValue]) -> SupervisedEntityNeeds:
        """
        Expected cycle time of alive trigger of this Supervised Entity (in seconds).
        A None value is a no-op and does not overwrite an existing expectedAliveCycle.
        """
        if value is not None:
            self.expectedAliveCycle = value
        return self

    def getMaxAliveCycle(self) -> Optional[TimeValue]:
        """
        Maximum cycle time of alive trigger of this Supervised Entity (in seconds).
        """
        return self.maxAliveCycle

    def setMaxAliveCycle(self, value: Optional[TimeValue]) -> SupervisedEntityNeeds:
        """
        Maximum cycle time of alive trigger of this Supervised Entity (in seconds).
        A None value is a no-op and does not overwrite an existing maxAliveCycle.
        """
        if value is not None:
            self.maxAliveCycle = value
        return self

    def getMinAliveCycle(self) -> Optional[TimeValue]:
        """
        Minimum cycle time of alive trigger of this Supervised Entity (in seconds).
        """
        return self.minAliveCycle

    def setMinAliveCycle(self, value: Optional[TimeValue]) -> SupervisedEntityNeeds:
        """
        Minimum cycle time of alive trigger of this Supervised Entity (in seconds).
        A None value is a no-op and does not overwrite an existing minAliveCycle.
        """
        if value is not None:
            self.minAliveCycle = value
        return self

    def getToleratedFailedCycles(self) -> Optional[PositiveInteger]:
        """
        Number of consecutive failed alive cycles for this SupervisedEntity which shall be tolerated until the supervision status of the SupervisedEntity is set to WDGM_ALIVE_EXPIRED (see SWS WdgM for more details). Note that this value has to be recalculated with respect to the WdgM's own cycle time for ECU configuration.
        """
        return self.toleratedFailedCycles

    def setToleratedFailedCycles(self, value: Optional[PositiveInteger]) -> SupervisedEntityNeeds:
        """
        Number of consecutive failed alive cycles for this SupervisedEntity which shall be tolerated until the supervision status of the SupervisedEntity is set to WDGM_ALIVE_EXPIRED (see SWS WdgM for more details). Note that this value has to be recalculated with respect to the WdgM's own cycle time for ECU configuration.
        A None value is a no-op and does not overwrite an existing toleratedFailedCycles.
        """
        if value is not None:
            self.toleratedFailedCycles = value
        return self


class SymbolicNameProps(ImplementationProps):
    """
    This meta-class can be taken to contribute to the creation of symbolic name values.
    """

    # SymbolicNameProps method parity checklist:
    # Spec: AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf, Table 7.59, p.610
    # Spec verified: R23-11
    # Columns: impl / docstring / test / reader / writer / release   ([—] = no XML element)
    # [x] __init__    [x] impl  [x] docstring  [x] test  [—] reader  [—] writer  R23-11

    def __init__(self, parent: ARObject, short_name: str):
        super().__init__(parent, short_name)


class SyncTimeBaseMgrUserNeeds(ServiceNeeds):
    """
    Specifies the needs on the configuration of the Synchronized Time-base Manager for one time-base. This class currently contains no attributes. An instance of this class is used to find out which ports of a software-component belong to this time-base in order to group the request and response ports of the same time-base. The actual time-base value is stored in the PortDefinedArgumentValue of the respective port specification.
    """

    # SyncTimeBaseMgrUserNeeds method parity checklist:
    # Spec: AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.pdf, Table 12.17, p.236
    # Spec verified: R23-11
    # Columns: impl / docstring / test / reader / writer / release   ([—] = no XML element)
    # [x] __init__                     [x] impl  [x] docstring  [x] test  [—] reader  [—] writer  R23-11

    def __init__(self, parent: ARObject, short_name: str):
        super().__init__(parent, short_name)


class PossibleErrorReaction(Identifiable):
    """
    Describes a possible error reaction code for the transient fault handler.
    """

    # PossibleErrorReaction method parity checklist:
    # [ ] __init__                     [ ] impl  [ ] docstring  [ ] test
    # [ ] getReactionCode              [ ] impl  [ ] docstring  [ ] test
    # [ ] setReactionCode              [ ] impl  [ ] docstring  [ ] test

    def __init__(self, parent: ARObject, short_name: str):
        """
        Initializes the PossibleErrorReaction with a parent and short name.

        Args:
            parent: The parent ARObject that contains this possible error reaction
            short_name: The unique short name of this possible error reaction
        """
        super().__init__(parent, short_name)

        # Fault reaction code which can be returned by transient fault handler.
        self.reactionCode: Optional[PositiveInteger] = None

    def getReactionCode(self) -> Optional[PositiveInteger]:
        """
        Gets the fault reaction code which can be returned by transient fault handler.

        Returns:
            PositiveInteger instance, or None if not set
        """
        return self.reactionCode

    def setReactionCode(self, value: Optional[PositiveInteger]) -> PossibleErrorReaction:
        """
        Sets the fault reaction code which can be returned by transient fault handler.
        A None value is a no-op and does not overwrite an existing reactionCode.

        Args:
            value: The PositiveInteger instance to set

        Returns:
            self for method chaining
        """
        if value is not None:
            self.reactionCode = value
        return self


class TransientFault(TracedFailure):
    """
    The reported failure is classified as runtime error.
    """

    # TransientFault method parity checklist:
    # Spec: AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf, Table E.50, p.1009
    # Spec verified: R23-11
    # Columns: impl / docstring / test / reader / writer / release   ([—] = no XML element)
    # [x] __init__    [x] impl  [x] docstring  [x] test  [—] reader  [—] writer  R23-11
    # [x] getPossibleErrorReactions   [x] impl  [x] docstring  [x] test  [x] reader  [x] writer  R23-11
    # [x] createPossibleErrorReaction [x] impl  [x] docstring  [x] test  [x] reader  [x] writer  R23-11

    def __init__(self, parent: ARObject, short_name: str):
        super().__init__(parent, short_name)

        # Describes a possible error reactions for the transient fault handler.
        self.possibleErrorReactions: List[PossibleErrorReaction] = []

    def createPossibleErrorReaction(self, short_name: str) -> PossibleErrorReaction:
        """
        Describes a possible error reactions for the transient fault handler.
        """
        if not self.IsElementExists(short_name, PossibleErrorReaction):
            reaction = PossibleErrorReaction(self, short_name)
            self.addElement(reaction)
            self.possibleErrorReactions.append(reaction)
        return self.getElement(short_name, PossibleErrorReaction)

    def getPossibleErrorReactions(self) -> List[PossibleErrorReaction]:
        """
        Describes a possible error reactions for the transient fault handler.
        """
        return self.possibleErrorReactions


class V2xDataManagerNeeds(ServiceNeeds):
    """
    This meta-class represents the ability to define service needs for V2x Data Manager.
    """

    # V2xDataManagerNeeds method parity checklist:
    # Spec: AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf, Table 13.79, p.840
    # Spec verified: R23-11
    # Columns: impl / docstring / test / reader / writer / release   ([—] = no XML element)
    # [x] __init__                     [x] impl  [x] docstring  [x] test  [—] reader  [—] writer  R23-11

    def __init__(self, parent: ARObject, short_name: str):
        super().__init__(parent, short_name)


class V2xFacUserNeeds(ServiceNeeds):
    """
    This meta-class represents the ability to define service needs for V2x facilities.
    """

    # V2xFacUserNeeds method parity checklist:
    # Spec: AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf, Table 13.77, p.834
    # Spec verified: R23-11
    # Columns: impl / docstring / test / reader / writer / release   ([—] = no XML element)
    # [x] __init__                     [x] impl  [x] docstring  [x] test  [—] reader  [—] writer  R23-11

    def __init__(self, parent: ARObject, short_name: str):
        super().__init__(parent, short_name)


class V2xMUserNeeds(ServiceNeeds):
    """
    This meta-class represents the ability to express service needs for the V2x management.
    """

    # V2xMUserNeeds method parity checklist:
    # Spec: AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf, Table 13.78, p.836
    # Spec verified: R23-11
    # Columns: impl / docstring / test / reader / writer / release   ([—] = no XML element)
    # [x] __init__                     [x] impl  [x] docstring  [x] test  [—] reader  [—] writer  R23-11

    def __init__(self, parent: ARObject, short_name: str):
        super().__init__(parent, short_name)


class VendorSpecificServiceNeeds(ServiceNeeds):
    """
    This represents the ability to define vendor-specific service needs.
    """

    # VendorSpecificServiceNeeds method parity checklist:
    # Spec: AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf, Table 7.53, p.604
    # Spec verified: R23-11
    # Columns: impl / docstring / test / reader / writer / release   ([—] = no XML element)
    # [x] __init__                     [x] impl  [x] docstring  [x] test  [—] reader  [—] writer  R23-11

    def __init__(self, parent: ARObject, short_name: str):
        super().__init__(parent, short_name)


class VerificationStatusIndicationModeEnum(AREnum):
    """
    This enumeration provides options for setting the mode of a verification status indication.
    """

    # VerificationStatusIndicationModeEnum method parity checklist:
    # Spec: AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf, Table 13.69, p.824
    # Spec verified: R23-11
    # Columns: impl / docstring / test / reader / writer / release   ([—] = no XML element)
    # [x] __init__    [x] impl  [x] docstring  [x] test  [—] reader  [—] writer  R23-11
    # (no methods) — serialized as an attribute value on the consuming class

    # Verification attempts that came out "false" or "true" shall be forwarded to the application software. Tags: atp.EnumerationLiteralIndex=1
    FAILURE_AND_SUCCESS = "failureAndSuccess"
    # Only verification attempts that came out "false" shall be forwarded to the application software. Tags: atp.EnumerationLiteralIndex=0
    FAILURE_ONLY = "failureOnly"

    def __init__(self):
        super().__init__(
            [
                VerificationStatusIndicationModeEnum.FAILURE_AND_SUCCESS,
                VerificationStatusIndicationModeEnum.FAILURE_ONLY,
            ]
        )


class WarningIndicatorRequestedBitNeeds(ServiceNeeds):
    """
    This meta-class represents the ability to explicitly request the existence of the WarningIndicatorRequestedBit.
    """

    # WarningIndicatorRequestedBitNeeds method parity checklist:
    # Spec: AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf, Table 13.61, p.811
    # Spec verified: R23-11
    # Columns: impl / docstring / test / reader / writer / release   ([—] = no XML element)
    # [x] __init__                     [x] impl  [x] docstring  [x] test  [—] reader  [—] writer  R23-11

    def __init__(self, parent: ARObject, short_name: str):
        super().__init__(parent, short_name)


# Runtime cycle-breaker: SWComponentTemplate.SwcInternalBehavior.__init__ -> ServiceMapping imports this module,
# so the DataElements import must run after every class above is defined (Rule 0005).
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.SwcInternalBehavior.DataElements import AutosarParameterRef, AutosarVariableRef  # noqa: E402
