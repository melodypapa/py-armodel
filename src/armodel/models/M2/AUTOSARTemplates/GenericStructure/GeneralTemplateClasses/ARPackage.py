"""
This module contains the ARPackage class and related classes for AUTOSAR models
in the GenericStructure module. ARPackage represents a hierarchical container for
organizing AUTOSAR elements according to the AUTOSAR standard. It serves as the
primary organizational unit for grouping related AUTOSAR model elements such as
components, interfaces, data types, and other packages.
"""

from __future__ import annotations
from typing import List, Optional, cast
from typing import TYPE_CHECKING

from abc import ABC

if TYPE_CHECKING:
    # ApplicationDeferredDataType is bound at runtime by the PEP 562 __getattr__ below
    # (AbstractPlatform closes an import cycle), so it is imported here for typing only.
    from armodel.models.M2.AUTOSARTemplates.AbstractPlatform import ApplicationDeferredDataType, ApplicationInterface
    from armodel.models.M2.AUTOSARTemplates.CommonStructure.FlatMap import AliasNameSet
    from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ElementCollection import (
        Collection,
    )
    from armodel.models.M2.MSR.AsamHdo.BaseTypes import SwBaseType
    from armodel.models.M2.MSR.DataDictionary.Axis import SwAxisType

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import (
    ARObject,
    CalibrationParameterValue,
    DiagnosticCommonProps,
    DiagnosticConnectedIndicator,
    DiagnosticControlEnableMaskBit,
    DiagnosticEventWindow,
    DiagnosticIumprGroupIdentifier,
    DiagnosticMemoryDestination,
    DiagnosticParameter,
    DiagnosticSupportInfoByte,
    DiagnosticTestIdentifier,
    PhysicalDimensionMapping,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable import (
    DiagnosticAuthTransmitCertificateEvaluation,
    DiagnosticRequestRoutineResults,
    DiagnosticStartRoutine,
    DiagnosticStopRoutine,
    Identifiable,
    Referrable,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ElementCollection import CollectableElement
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.StereotypeMixins import VariationPointCapable


class PackageableElement(CollectableElement, VariationPointCapable, ABC):
    """
    This meta-class specifies the ability to be a member of an AUTOSAR package.
    """

    # PackageableElement method parity checklist:
    # Spec: AUTOSAR_FO_TPS_GenericStructureTemplate.pdf, Table 4.2, p.54
    # Spec verified: R23-11
    # Columns: impl / docstring / test / reader / writer / release   ([—] = no XML element)
    # [x] __init__                     [x] impl  [x] docstring  [x] test  [—] reader  [—] writer  R23-11

    def __init__(self, parent: ARObject, short_name: str):
        if type(self) is PackageableElement:
            raise TypeError("PackageableElement is an abstract class.")
        super().__init__(parent, short_name)


class ARElement(PackageableElement, ABC):
    """
    An element that can be defined stand-alone, i.e. without being part of another element (except for packages of course).
    """

    # ARElement method parity checklist:
    # Spec: AUTOSAR_FO_TPS_GenericStructureTemplate.pdf, Table 4.3, p.55
    # Spec verified: R23-11
    # Columns: impl / docstring / test / reader / writer / release   ([—] = no XML element)
    # [x] __init__   [x] impl  [x] docstring  [x] test  [—] reader  [—] writer  R23-11

    def __init__(self, parent: ARObject, short_name: str):
        if type(self) is ARElement:
            raise TypeError("ARElement is an abstract class.")
        super().__init__(parent, short_name)


# Initialize the CommonStructure package before any import that transitively touches
# AbstractStructure: AbstractStructure's own import of AbstractBlueprintStructure requires
# the CommonStructure package to be present in sys.modules (Task 15 bootstrap-cycle fix).
import armodel.models.M2.AUTOSARTemplates.CommonStructure  # noqa: F401,E402

# Names NOT eagerly imported at the end of this module (import-time 2-rings) are
# re-exported lazily via PEP 562; `from ARPackage import X` and wildcard imports
# keep working because __getattr__ only fires for names missing from module globals.
from importlib import import_module as _import_module  # noqa: E402

_LAZY_IMPORTS = {
    "ApplicationDeferredDataType": "armodel.models.M2.AUTOSARTemplates.AbstractPlatform",
    "SwBaseType": "armodel.models.M2.MSR.AsamHdo.BaseTypes",
    "SwAxisType": "armodel.models.M2.MSR.DataDictionary.Axis",
}


def __getattr__(name):
    module_path = _LAZY_IMPORTS.get(name)
    if module_path is None:
        raise AttributeError("module %r has no attribute %r" % (__name__, name))
    value = getattr(_import_module(module_path), name)
    globals()[name] = value
    return value


__all__ = [
    "ViewMapSet",
    "SwAxisType",
    "SecurityEventDefinition",
    "SecurityEventContextMappingFunctionalCluster",
    "SecurityEventContextMappingBswModule",
    "SecurityEventContextMappingApplication",
    "SdgDef",
    "PostBuildVariantCriterionValueSet",
    "PhysicalDimensionMappingSet",
    "LifeCycleStateDefinitionGroup",
    "IdsDesign",
    "FMFeatureSelectionSet",
    "FMFeatureModel",
    "FMFeatureMap",
    "FMFeature",
    "EvaluatedVariantSet",
    "DiagnosticWriteDataByIdentifier",
    "DiagnosticWriteMemoryByAddress",
    "DiagnosticVerifyCertificateUnidirectional",
    "DiagnosticVerifyCertificateBidirectional",
    "DiagnosticTroubleCodeUdsToTroubleCodeObdMapping",
    "DiagnosticTroubleCodeGroup",
    "DiagnosticTroubleCodeJ1939",
    "DiagnosticTroubleCode",
    "DiagnosticTransferExit",
    "DiagnosticTestRoutineIdentifier",
    "DiagnosticTestResult",
    "DiagnosticStorageConditionPortMapping",
    "DiagnosticStorageConditionGroup",
    "DiagnosticStorageCondition",
    "DiagnosticSessionControl",
    "DiagnosticServiceDataMapping",
    "DiagnosticServiceMappingDiagTarget",
    "DiagnosticServiceSwMapping",
    "DiagnosticParameterElementAccess",
    "DiagnosticSecurityEventReportingModeMapping",
    "DiagnosticSecurityAccess",
    "DiagnosticRoutineControl",
    "DiagnosticRoutine",
    "DiagnosticResponseOnEvent",
    "DiagnosticRequestVehicleInfo",
    "DiagnosticRequestUpload",
    "DiagnosticRequestPowertrainFreezeFrameData",
    "DiagnosticRequestOnBoardMonitoringTestResults",
    "DiagnosticRequestFileTransfer",
    "DiagnosticRequestEmissionRelatedDTCPermanentStatus",
    "DiagnosticRequestDownload",
    "DiagnosticRequestEmissionRelatedDTC",
    "DiagnosticClearResetEmissionRelatedInfo",
    "DiagnosticRequestControlOfOnBoardDevice",
    "DiagnosticRequestCurrentPowertrainData",
    "DiagnosticRequestPowertrainFreezeFrameData",
    "DiagnosticPowertrainFreezeFrame",
    "DiagnosticReadScalingDataByIdentifier",
    "DiagnosticReadDataByPeriodicID",
    "DiagnosticReadDataByIdentifier",
    "DiagnosticReadDTCInformation",
    "DiagnosticReadMemoryByAddress",
    "DiagnosticProtocol",
    "DiagnosticProofOfOwnership",
    "DiagnosticPowertrainFreezeFrame",
    "DiagnosticParameterIdentifier",
    "DiagnosticOperationCyclePortMapping",
    "DiagnosticOperationCycle",
    "DiagnosticMemoryIdentifier",
    "DiagnosticMemoryDestinationPrimary",
    "DiagnosticMemoryAddressableRangeAccess",
    "DiagnosticMeasurementIdentifier",
    "DiagnosticMasterToSlaveEventMapping",
    "DiagnosticJ1939SwMapping",
    "DiagnosticJ1939SpnMapping",
    "DiagnosticJ1939Spn",
    "DiagnosticJ1939Node",
    "DiagnosticJ1939FreezeFrame",
    "DiagnosticJ1939ExpandedFreezeFrame",
    "DiagnosticIumprToFunctionIdentifierMapping",
    "DiagnosticIumprGroup",
    "DiagnosticIumprDenominatorGroup",
    "DiagnosticIumpr",
    "DiagnosticInhibitSourceEventMapping",
    "DiagnosticInfoType",
    "DiagnosticIndicator",
    "DiagnosticIOControl",
    "DiagnosticFunctionIdentifier",
    "DiagnosticFreezeFrame",
    "DiagnosticFimEventGroup",
    "DiagnosticJ1939Spn",
    "DiagnosticFimAliasEventMapping",
    "DiagnosticFimAliasEventGroupMapping",
    "DiagnosticFimAliasEventGroup",
    "DiagnosticFimAliasEvent",
    "DiagnosticExtendedDataRecord",
    "DiagnosticEventToTroubleCodeUdsMapping",
    "DiagnosticEventToTroubleCodeJ1939Mapping",
    "DiagnosticEventToStorageConditionGroupMapping",
    "DiagnosticEventToSecurityEventMapping",
    "DiagnosticEventToOperationCycleMapping",
    "DiagnosticEventToEnableConditionGroupMapping",
    "DiagnosticEventToDebounceAlgorithmMapping",
    "DiagnosticEnableConditionPortMapping",
    "DiagnosticEventPortMapping",
    "DiagnosticSwMapping",
    "DiagnosticEvent",
    "DiagnosticEnableConditionGroup",
    "DiagnosticEnableCondition",
    "DiagnosticEcuReset",
    "DiagnosticEcuInstanceProps",
    "DiagnosticDynamicallyDefineDataIdentifier",
    "DiagnosticDynamicDataIdentifier",
    "DiagnosticDemProvidedDataMapping",
    "DiagnosticDeAuthentication",
    "DiagnosticDataTransfer",
    "DiagnosticMemoryByAddress",
    "DiagnosticDataIdentifierSet",
    "DiagnosticDataIdentifier",
    "DiagnosticDataByIdentifier",
    "DiagnosticCustomServiceInstance",
    "DiagnosticConditionGroup",
    "DiagnosticControlDTCSetting",
    "DiagnosticContributionSet",
    "DiagnosticCondition",
    "DiagnosticComControl",
    "DiagnosticClearDiagnosticInformation",
    "DiagnosticAuthenticationConfiguration",
    "DiagnosticAuthTransmitCertificateMapping",
    "DiagnosticAuthTransmitCertificate",
    "DiagnosticAuthentication",
    "DiagnosticAuthRole",
    "DiagnosticAging",
    "DiagnosticAbstractDataIdentifier",
    "DiagnosticAbstractAliasEvent",
    "DataExchangePoint",
    "CpSwClusterToDiagRoutineSubfunctionMapping",
    "CpSwClusterToDiagEventMapping",
    "CpSwClusterResourceToDiagFunctionIdMapping",
    "CpSwClusterResourceToDiagDataElemMapping",
    "DiagnosticMapping",
    "DiagnosticFimEventGroup",
    "CalibrationParameterValueSet",
    "AclRole",
    "AclPermission",
    "AclOperation",
    "AclObjectSet",
    "AdminData",
    "Annotation",
    "ApplicationArrayDataType",
    "ApplicationDataType",
    "ApplicationDeferredDataType",
    "ApplicationPrimitiveDataType",
    "ApplicationRecordDataType",
    "ApplicationSwComponentType",
    "AtomicSwComponentType",
    "BswImplementation",
    "BswModuleDescription",
    "BswModuleEntry",
    "BlueprintMappingSet",
    "CanCluster",
    "CanFrame",
    "CanTpConfig",
    "CanXlProps",
    "ClientServerInterface",
    "ComplexDeviceDriverSwComponentType",
    "CompositionSwComponentType",
    "CompuMethod",
    "ConsistencyNeeds",
    "ConstantSpecification",
    "ConstantSpecificationMappingSet",
    "CouplingElement",
    "CryptoEllipticCurveProps",
    "CryptoServiceCertificate",
    "CryptoServicePrimitive",
    "CryptoSignatureScheme",
    "DataConstr",
    "DataPrototypeGroup",
    "DataTransformationSet",
    "DataTypeMappingSet",
    "DcmIPdu",
    "DiagnosticAccessPermission",
    "DiagnosticConnection",
    "DiagnosticEnvironmentalCondition",
    "DiagnosticSecurityLevel",
    "DiagnosticServiceTable",
    "DiagnosticSession",
    "DoIpTpConfig",
    "Documentation",
    "DocumentationBlock",
    "E2EProfileCompatibilityProps",
    "EcuAbstractionSwComponentType",
    "EcuInstance",
    "EcucDefinitionCollection",
    "EcucDestinationUriDefSet",
    "EcucModuleConfigurationValues",
    "EcucModuleDef",
    "EcucValueCollection",
    "EndToEndProtectionSet",
    "EthernetCluster",
    "EthernetWakeupSleepOnDatalineConfigSet",
    "FirewallRule",
    "StateDependentFirewall",
    "FlatMap",
    "BuildActionManifest",
    "FlexrayCluster",
    "FlexrayFrame",
    "Gateway",
    "GeneralPurposeIPdu",
    "GeneralPurposePdu",
    "GenericEthernetFrame",
    "HwCategory",
    "HwElement",
    "HwType",
    "ISignal",
    "ISignalGroup",
    "ISignalIPdu",
    "ISignalIPduGroup",
    "Implementation",
    "ImplementationDataType",
    "J1939DcmIPdu",
    "KeywordSet",
    "LifeCycleInfoSet",
    "LinCluster",
    "PdurIPduGroup",
    "LinTpConfig",
    "LinUnconditionalFrame",
    "McFunction",
    "McGroup",
    "ModeDeclarationGroup",
    "ModeDeclarationMappingSet",
    "ModeSwitchInterface",
    "MultiLanguageOverviewParagraph",
    "MultilanguageLongName",
    "MultiplexedIPdu",
    "NPdu",
    "NmConfig",
    "NmPdu",
    "NvBlockSwComponentType",
    "NvDataInterface",
    "ParameterInterface",
    "PhysicalDimension",
    "PortInterfaceMappingSet",
    "PortPrototypeBlueprint",
    "PostBuildVariantCriterion",
    "PredefinedVariant",
    "RunnableEntityGroup",
    "SecureCommunicationPropsSet",
    "SecuredIPdu",
    "SenderReceiverInterface",
    "SensorActuatorSwComponentType",
    "ServiceInstanceCollectionSet",
    "ServiceProxySwComponentType",
    "ServiceSwComponentType",
    "SignalServiceTranslationPropsSet",
    "SoAdRoutingGroup",
    "SomeipSdClientEventGroupTimingConfig",
    "SomeipSdClientServiceInstanceConfig",
    "SomeipSdServerEventGroupTimingConfig",
    "SomeipSdServerServiceInstanceConfig",
    "SocketConnectionIpduIdentifierSet",
    "SwAddrMethod",
    "SwBaseType",
    "SwComponentType",
    "SwRecordLayout",
    "SwSystemconst",
    "SwSystemconstantValueSet",
    "SwcBswMapping",
    "SwcImplementation",
    "SwcTiming",
    "System",
    "SystemSignal",
    "SystemSignalGroup",
    "TcpOptionFilterSet",
    "TlvDataIdDefinitionSet",
    "TtcanCluster",
    "TriggerInterface",
    "Unit",
    "UserDefinedIPdu",
    "UserDefinedPdu",
    "ARElement",
    "ARPackage",
    "PackageableElement",
    "ReferenceBase",
    "BswCompositionTiming",
    "BswModuleTiming",
    "CpSoftwareClusterBinaryManifestDescriptor",
    "CpSoftwareClusterMappingSet",
    "CpSoftwareClusterResourcePool",
    "CryptoServiceKey",
    "CryptoServiceQueue",
    "DdsCpConfig",
    "EcuTiming",
    "EthIpProps",
    "GeneralPurposeConnection",
    "GlobalTimeDomain",
    "IEEE1722TpAafConnection",
    "IEEE1722TpAcfConnection",
    "IEEE1722TpAvConnection",
    "IEEE1722TpConnection",
    "IEEE1722TpCrfConnection",
    "IEEE1722TpIidcConnection",
    "IEEE1722TpRvfConnection",
    "IPSecConfigProps",
    "IPv6ExtHeaderFilterSet",
    "LogAndTraceMessageCollectionSet",
    "MacSecGlobalKayProps",
    "MacSecParticipantSet",
    "ServiceInstanceCollectionSet",
    "SocketConnectionIpduIdentifierSet",
    "TransformationPropsSet",
    "VfbTiming",
]


from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import CategoryString  # noqa: E402,F401


from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (  # noqa: E402
    Boolean,
    DiagnosticClearEventAllowedBehaviorEnum,
    DiagnosticEventClearAllowedEnum,
    DiagnosticEventKindEnum,
    DiagnosticIumprKindEnum,
    DiagnosticObdSupportEnum,
    DiagnosticOperationCycleTypeEnum,
    DiagnosticRecordTriggerEnum,
    DiagnosticResponseOnEventActionEnum,
    DiagnosticTestResultUpdateEnum,
    DiagnosticTroubleCodeJ1939DtcKindEnum,
    DiagnosticTypeOfDtcSupportedEnum,
    Identifier,
    NameToken,
    PositiveInteger,
    RefType,
    ReferrableSubtypesEnum,
    String,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import TimeValue  # noqa: E402


class ReferenceBase(ARObject):
    """
    This meta-class establishes a basis for relative references. Reference bases are identified by the short Label which shall be unique in the current package.
    """

    # ReferenceBase method parity checklist:
    # Spec: R23-11/AUTOSAR_FO_TPS_GenericStructureTemplate.pdf, Table 4.14, p.72 (R23-11)
    # Spec: R4.3.1/AUTOSAR_TPS_GenericStructureTemplate.pdf, Table 4.5, pp.54-55 (R4.3.1)
    # Spec verified: R23-11
    # Columns: impl / docstring / test / reader / writer / release   ([—] = no XML element)
    # [x] __init__               [x] impl  [x] docstring  [x] test  [—] reader  [—] writer  R23-11
    # [x] getGlobalElements      [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] addGlobalElement       [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getGlobalInPackageRefs [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] addGlobalInPackageRef  [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getIsDefault           [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setIsDefault           [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getPackageRef          [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setPackageRef          [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getShortLabel          [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setShortLabel          [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getIsGlobal           [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R4.3.1
    # [x] setIsGlobal           [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R4.3.1
    # [x] getBaseIsThisPackage  [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R4.3.1
    # [x] setBaseIsThisPackage  [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R4.3.1

    def __init__(self):
        super().__init__()

        # This attribute represents a meta-class for which the global referencing is supported via this reference base.
        self.globalElements: List[ReferrableSubtypesEnum] = []

        # This represents the ability to express that global elements live in various packages which do not have a common ancestor package. Packages mentioned by Reference Base.globalInPackage are used in addition to the one in ReferenceBase.package.
        self.globalInPackageRefs: List[RefType] = []

        # This attribute denotes if the current ReferenceBase is the default. Note that there can only be one default reference base within a package.
        self.isDefault: Optional[Boolean] = None

        # This association specifies the basis of all relative references with the base equals shortLabel.
        self.packageRef: Optional[RefType] = None

        # This is the name of the reference base. By this name, particular references can denote the applicable base.
        self.shortLabel: Optional[Identifier] = None

        # This indicates that the target of the applicable reference can be resolved via the non-qualified shortName. This requires that the shortName of the target is unique within the package referenced in the reference base. The default is false. Note that the reference base also maintains a list of elements which may be referenced using a "global Reference".
        self.isGlobal: Optional[Boolean] = None

        # This indicates that this base is established by the current package. In this case the association "package" can be derived as the qualified shortName of the enclosing package. If the value of baseIsThisPackage is set to true then one of the following must be true: • target of the association "package" must be the enclosing package. • association "package" is omitted.
        self.baseIsThisPackage: Optional[Boolean] = None

    def getGlobalElements(self) -> List[ReferrableSubtypesEnum]:
        """
        This attribute represents a meta-class for which the global referencing is supported via this reference base.
        """
        return self.globalElements

    def addGlobalElement(self, value: ReferrableSubtypesEnum) -> ReferenceBase:
        """
        This attribute represents a meta-class for which the global referencing is supported via this reference base.
        """
        self.globalElements.append(value)
        return self

    def getGlobalInPackageRefs(self) -> List[RefType]:
        """
        This represents the ability to express that global elements live in various packages which do not have a common ancestor package. Packages mentioned by Reference Base.globalInPackage are used in addition to the one in ReferenceBase.package.
        """
        return self.globalInPackageRefs

    def addGlobalInPackageRef(self, value: RefType) -> ReferenceBase:
        """
        This represents the ability to express that global elements live in various packages which do not have a common ancestor package. Packages mentioned by Reference Base.globalInPackage are used in addition to the one in ReferenceBase.package.
        """
        self.globalInPackageRefs.append(value)
        return self

    def getIsDefault(self) -> Optional[Boolean]:
        """
        This attribute denotes if the current ReferenceBase is the default. Note that there can only be one default reference base within a package.
        """
        return self.isDefault

    def setIsDefault(self, value: Optional[Boolean]) -> ReferenceBase:
        """
        This attribute denotes if the current ReferenceBase is the default. Note that there can only be one default reference base within a package. A None value is a no-op and does not overwrite an existing isDefault.
        """
        if value is not None:
            self.isDefault = value
        return self

    def getPackageRef(self) -> Optional[RefType]:
        """
        This association specifies the basis of all relative references with the base equals shortLabel.
        """
        return self.packageRef

    def setPackageRef(self, value: Optional[RefType]) -> ReferenceBase:
        """
        This association specifies the basis of all relative references with the base equals shortLabel. A None value is a no-op and does not overwrite an existing packageRef.
        """
        if value is not None:
            self.packageRef = value
        return self

    def getShortLabel(self) -> Optional[Identifier]:
        """
        This is the name of the reference base. By this name, particular references can denote the applicable base.
        """
        return self.shortLabel

    def setShortLabel(self, value: Optional[Identifier]) -> ReferenceBase:
        """
        This is the name of the reference base. By this name, particular references can denote the applicable base. A None value is a no-op and does not overwrite an existing shortLabel.
        """
        if value is not None:
            self.shortLabel = value
        return self

    def getIsGlobal(self) -> Optional[Boolean]:
        """
        This indicates that the target of the applicable reference can be resolved via the non-qualified shortName. This requires that the shortName of the target is unique within the package referenced in the reference base. The default is false. Note that the reference base also maintains a list of elements which may be referenced using a "global Reference".
        """
        return self.isGlobal

    def setIsGlobal(self, value: Optional[Boolean]) -> ReferenceBase:
        """
        This indicates that the target of the applicable reference can be resolved via the non-qualified shortName. This requires that the shortName of the target is unique within the package referenced in the reference base. The default is false. Note that the reference base also maintains a list of elements which may be referenced using a "global Reference". A None value is a no-op and does not overwrite an existing isGlobal.
        """
        if value is not None:
            self.isGlobal = value
        return self

    def getBaseIsThisPackage(self) -> Optional[Boolean]:
        """
        This indicates that this base is established by the current package. In this case the association "package" can be derived as the qualified shortName of the enclosing package. If the value of baseIsThisPackage is set to true then one of the following must be true: • target of the association "package" must be the enclosing package. • association "package" is omitted.
        """
        return self.baseIsThisPackage

    def setBaseIsThisPackage(self, value: Optional[Boolean]) -> ReferenceBase:
        """
        This indicates that this base is established by the current package. In this case the association "package" can be derived as the qualified shortName of the enclosing package. If the value of baseIsThisPackage is set to true then one of the following must be true: • target of the association "package" must be the enclosing package. • association "package" is omitted. A None value is a no-op and does not overwrite an existing baseIsThisPackage.
        """
        if value is not None:
            self.baseIsThisPackage = value
        return self


class ARPackage(CollectableElement, VariationPointCapable):
    """
    AUTOSAR package, allowing to create top level packages to structure the contained ARElements. ARPackages are open sets. This means that in a file based description system multiple files can be used to partially describe the contents of a package. This is an extended version of MSR's SW-SYSTEM.
    """

    # ARPackage method parity checklist:
    # Spec: AUTOSAR_FO_TPS_GenericStructureTemplate.pdf, Table 4.1, p.54
    # Spec verified: R23-11
    # Columns: impl / docstring / test / reader / writer / release   ([—] = no XML element)
    # [x] __init__          [x] impl  [x] docstring  [x] test  [—] reader  [—] writer  R23-11
    # [x] getARPackages     [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] createARPackage   [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getReferrableElement        [x] impl  [x] docstring  [x] test  [—] reader  [—] writer  R23-11
    # [x] getReferenceBases [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] addReferenceBase  [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    #
    # Base chain (Rule 0001.2): parallel chains {AtpBlueprint, AtpBlueprintable,
    # CollectableElement} -> single role-matching branch CollectableElement;
    # AtpBlueprint/AtpBlueprintable are not added via Python multiple inheritance
    # (their own syncs are queued in Group1).
    # Referrable/Identifiable members (parent, short_name, longName, annotations,
    # adminData, category, introduction, desc, uuid, variationPoint) are inherited
    # from the CollectableElement -> Identifiable -> ... -> ARObject chain; they
    # belong to the Identifiable/Referrable checklists, not to ARPackage.
    # ARPackage.__init__ adds only arPackages + referenceBases and calls super().__init__.
    # Convenience factory accessors (createXxx/getXxxs) are pre-existing API for the
    # element aggregation; each concrete element class carries its own spec table
    # and checklist.

    def __init__(self, parent: ARObject, short_name: str):
        # Referrable/Identifiable members (parent, short_name, longName, annotations,
        # adminData, category, introduction, desc, uuid, variationPoint) and the
        # element-collection registry are inherited from CollectableElement -> Identifiable.
        super().__init__(parent, short_name)

        # This represents a sub package within an ARPackage, thus allowing for an unlimited package hierarchy.
        self.arPackages: List[ARPackage] = []
        # This denotes the reference bases for the package. This is the basis for all relative references within the package. The base needs to be selected according to the base attribute within the references.
        self.referenceBases: List[ReferenceBase] = []

    def getARPackages(self) -> List[ARPackage]:
        """
        This represents a sub package within an ARPackage, thus allowing for an unlimited package hierarchy.

        Returns:
            List of ARPackage instances sorted by short name
        """
        return list(sorted(self.arPackages, key=lambda a: a.short_name))
        # return list(filter(lambda e: isinstance(e, ARPackage), self.referrableElements))

    def createARPackage(self, short_name: str) -> ARPackage:
        """
        This represents a sub package within an ARPackage, thus allowing for an unlimited package hierarchy. Creates a new sub-package with the given short name, or returns an existing package if one with the same name already exists.

        Args:
            short_name: The short name for the new sub-package

        Returns:
            The newly created or existing ARPackage instance
        """
        for ar_package in self.arPackages:
            if ar_package.short_name == short_name:
                return ar_package
        ar_package = ARPackage(self, short_name)
        self.arPackages.append(ar_package)
        return ar_package

    def getReferrableElement(self, short_name: str, type=None) -> Referrable:
        """
        Elements that are part of this package. Retrieves an element by its short name, optionally filtered by type. This method searches for both sub-packages and other elements in this package.

        Args:
            short_name: The short name of the element to retrieve
            type: Optional type filter for the element to retrieve

        Returns:
            The element with the specified name and type, or None if not found
        """
        if type is ARPackage or type is None:
            for ar_package in self.arPackages:
                if ar_package.short_name == short_name:
                    return ar_package
        return cast(Referrable, Identifiable.getReferrableElement(self, short_name, type))

    def createDiagnosticClearDiagnosticInformation(self, short_name: str) -> DiagnosticClearDiagnosticInformation:
        """
        Creates a new DiagnosticClearDiagnosticInformation with the given short
        name, or returns an existing one if it already exists in this package.

        DiagnosticClearDiagnosticInformation represents an instance of the
        "Clear Diagnostic Information" diagnostic service.

        Args:
            short_name: The short name for the new DiagnosticClearDiagnosticInformation

        Returns:
            The newly created or existing DiagnosticClearDiagnosticInformation instance
        """
        if not self.IsReferrableElementExists(short_name, DiagnosticClearDiagnosticInformation):
            clear_diagnostic_information = DiagnosticClearDiagnosticInformation(self, short_name)
            self.addReferrableElement(clear_diagnostic_information)
        return cast(DiagnosticClearDiagnosticInformation, self.getReferrableElement(short_name, DiagnosticClearDiagnosticInformation))

    def createDiagnosticClearDiagnosticInformationClass(self, short_name: str) -> DiagnosticClearDiagnosticInformationClass:
        """
        Creates a new DiagnosticClearDiagnosticInformationClass with the given
        short name, or returns an existing one if it already exists in this package.

        DiagnosticClearDiagnosticInformationClass contains attributes shared by all
        instances of the "Clear Diagnostic Information" diagnostic service.

        Args:
            short_name: The short name for the new DiagnosticClearDiagnosticInformationClass

        Returns:
            The newly created or existing DiagnosticClearDiagnosticInformationClass instance
        """
        if not self.IsReferrableElementExists(short_name, DiagnosticClearDiagnosticInformationClass):
            clear_diagnostic_information_class = DiagnosticClearDiagnosticInformationClass(self, short_name)
            self.addReferrableElement(clear_diagnostic_information_class)
        return cast(DiagnosticClearDiagnosticInformationClass, self.getReferrableElement(short_name, DiagnosticClearDiagnosticInformationClass))

    def createDiagnosticClearResetEmissionRelatedInfo(self, short_name: str) -> DiagnosticClearResetEmissionRelatedInfo:
        """
        Creates a new DiagnosticClearResetEmissionRelatedInfo with the given short name, or
        returns an existing one if it already exists in this package.

        DiagnosticClearResetEmissionRelatedInfo represents an instance of the OBD mode 0x04 service.

        Args:
            short_name: The short name for the new DiagnosticClearResetEmissionRelatedInfo

        Returns:
            The newly created or existing DiagnosticClearResetEmissionRelatedInfo instance
        """
        if not self.IsReferrableElementExists(short_name, DiagnosticClearResetEmissionRelatedInfo):
            clear_reset_emission_related_info = DiagnosticClearResetEmissionRelatedInfo(self, short_name)
            self.addReferrableElement(clear_reset_emission_related_info)
        return cast(DiagnosticClearResetEmissionRelatedInfo, self.getReferrableElement(short_name, DiagnosticClearResetEmissionRelatedInfo))

    def createDiagnosticClearResetEmissionRelatedInfoClass(self, short_name: str) -> DiagnosticClearResetEmissionRelatedInfoClass:
        """
        Creates a new DiagnosticClearResetEmissionRelatedInfoClass with the given short name,
        or returns an existing one if it already exists in this package.

        DiagnosticClearResetEmissionRelatedInfoClass contains attributes shared by all
        instances of the "Clear Reset Emission Related Data" OBD diagnostic service.

        Args:
            short_name: The short name for the new DiagnosticClearResetEmissionRelatedInfoClass

        Returns:
            The newly created or existing DiagnosticClearResetEmissionRelatedInfoClass instance
        """
        if not self.IsReferrableElementExists(short_name, DiagnosticClearResetEmissionRelatedInfoClass):
            clear_reset_emission_related_info_class = DiagnosticClearResetEmissionRelatedInfoClass(self, short_name)
            self.addReferrableElement(clear_reset_emission_related_info_class)
        return cast(DiagnosticClearResetEmissionRelatedInfoClass, self.getReferrableElement(short_name, DiagnosticClearResetEmissionRelatedInfoClass))

    def createDiagnosticRequestControlOfOnBoardDevice(self, short_name: str) -> DiagnosticRequestControlOfOnBoardDevice:
        """
        Creates a new DiagnosticRequestControlOfOnBoardDevice with the given short name, or
        returns an existing one if it already exists in this package.

        DiagnosticRequestControlOfOnBoardDevice represents an instance of the OBD mode 0x08 service.

        Args:
            short_name: The short name for the new DiagnosticRequestControlOfOnBoardDevice

        Returns:
            The newly created or existing DiagnosticRequestControlOfOnBoardDevice instance
        """
        if not self.IsReferrableElementExists(short_name, DiagnosticRequestControlOfOnBoardDevice):
            request_control_of_on_board_device = DiagnosticRequestControlOfOnBoardDevice(self, short_name)
            self.addReferrableElement(request_control_of_on_board_device)
        return cast(DiagnosticRequestControlOfOnBoardDevice, self.getReferrableElement(short_name, DiagnosticRequestControlOfOnBoardDevice))

    def createDiagnosticRequestControlOfOnBoardDeviceClass(self, short_name: str) -> DiagnosticRequestControlOfOnBoardDeviceClass:
        """
        Creates a new DiagnosticRequestControlOfOnBoardDeviceClass with the given short name,
        or returns an existing one if it already exists in this package.

        DiagnosticRequestControlOfOnBoardDeviceClass contains attributes shared by all
        instances of the "Request Control Of On-Board Device" OBD diagnostic service.

        Args:
            short_name: The short name for the new DiagnosticRequestControlOfOnBoardDeviceClass

        Returns:
            The newly created or existing DiagnosticRequestControlOfOnBoardDeviceClass instance
        """
        if not self.IsReferrableElementExists(short_name, DiagnosticRequestControlOfOnBoardDeviceClass):
            request_control_of_on_board_device_class = DiagnosticRequestControlOfOnBoardDeviceClass(self, short_name)
            self.addReferrableElement(request_control_of_on_board_device_class)
        return cast(DiagnosticRequestControlOfOnBoardDeviceClass, self.getReferrableElement(short_name, DiagnosticRequestControlOfOnBoardDeviceClass))

    def createDiagnosticTestResult(self, short_name: str) -> DiagnosticTestResult:
        """
        Creates a new DiagnosticTestResult with the given short name, or
        returns an existing one if it already exists in this package.

        DiagnosticTestResult represents the ability to define diagnostic test results.

        Args:
            short_name: The short name for the new DiagnosticTestResult

        Returns:
            The newly created or existing DiagnosticTestResult instance
        """
        if not self.IsReferrableElementExists(short_name, DiagnosticTestResult):
            test_result = DiagnosticTestResult(self, short_name)
            self.addReferrableElement(test_result)
        return cast(DiagnosticTestResult, self.getReferrableElement(short_name, DiagnosticTestResult))

    def createDiagnosticTestRoutineIdentifier(self, short_name: str) -> DiagnosticTestRoutineIdentifier:
        """
        Creates a new DiagnosticTestRoutineIdentifier with the given short name, or
        returns an existing one if it already exists in this package.

        DiagnosticTestRoutineIdentifier represents the test id of the DiagnosticTestIdentifier.

        Args:
            short_name: The short name for the new DiagnosticTestRoutineIdentifier

        Returns:
            The newly created or existing DiagnosticTestRoutineIdentifier instance
        """
        if not self.IsReferrableElementExists(short_name, DiagnosticTestRoutineIdentifier):
            test_routine_identifier = DiagnosticTestRoutineIdentifier(self, short_name)
            self.addReferrableElement(test_routine_identifier)
        return cast(DiagnosticTestRoutineIdentifier, self.getReferrableElement(short_name, DiagnosticTestRoutineIdentifier))

    def createDiagnosticInfoType(self, short_name: str) -> DiagnosticInfoType:
        """
        Creates a new DiagnosticInfoType with the given short name, or
        returns an existing one if it already exists in this package.

        DiagnosticInfoType represents the ability to model an OBD info type.

        Args:
            short_name: The short name for the new DiagnosticInfoType

        Returns:
            The newly created or existing DiagnosticInfoType instance
        """
        if not self.IsReferrableElementExists(short_name, DiagnosticInfoType):
            info_type = DiagnosticInfoType(self, short_name)
            self.addReferrableElement(info_type)
        return cast(DiagnosticInfoType, self.getReferrableElement(short_name, DiagnosticInfoType))

    def createDiagnosticComControlClass(self, short_name: str) -> DiagnosticComControlClass:
        """
        Creates a new DiagnosticComControlClass with the given short name,
        or returns an existing one if it already exists in this package.

        DiagnosticComControlClass contains attributes shared by all
        instances of the "Communication Control" diagnostic service.

        Args:
            short_name: The short name for the new DiagnosticComControlClass

        Returns:
            The newly created or existing DiagnosticComControlClass instance
        """
        if not self.IsReferrableElementExists(short_name, DiagnosticComControlClass):
            com_control_class = DiagnosticComControlClass(self, short_name)
            self.addReferrableElement(com_control_class)
        return cast(DiagnosticComControlClass, self.getReferrableElement(short_name, DiagnosticComControlClass))

    def createDiagnosticControlDTCSetting(self, short_name: str) -> DiagnosticControlDTCSetting:
        """
        Creates a new DiagnosticControlDTCSetting with the given short name,
        or returns an existing one if it already exists in this package.

        DiagnosticControlDTCSetting represents an instance of the "Control DTC Setting" diagnostic service.

        Args:
            short_name: The short name for the new DiagnosticControlDTCSetting

        Returns:
            The newly created or existing DiagnosticControlDTCSetting instance
        """
        if not self.IsReferrableElementExists(short_name, DiagnosticControlDTCSetting):
            control_dtc_setting = DiagnosticControlDTCSetting(self, short_name)
            self.addReferrableElement(control_dtc_setting)
        return cast(DiagnosticControlDTCSetting, self.getReferrableElement(short_name, DiagnosticControlDTCSetting))

    def createDiagnosticControlDTCSettingClass(self, short_name: str) -> DiagnosticControlDTCSettingClass:
        """
        Creates a new DiagnosticControlDTCSettingClass with the given short name,
        or returns an existing one if it already exists in this package.

        DiagnosticControlDTCSettingClass contains attributes shared by all
        instances of the "Control DTC Setting" diagnostic service.

        Args:
            short_name: The short name for the new DiagnosticControlDTCSettingClass

        Returns:
            The newly created or existing DiagnosticControlDTCSettingClass instance
        """
        if not self.IsReferrableElementExists(short_name, DiagnosticControlDTCSettingClass):
            control_dtc_setting_class = DiagnosticControlDTCSettingClass(self, short_name)
            self.addReferrableElement(control_dtc_setting_class)
        return cast(DiagnosticControlDTCSettingClass, self.getReferrableElement(short_name, DiagnosticControlDTCSettingClass))

    def createDiagnosticDynamicallyDefineDataIdentifier(self, short_name: str) -> DiagnosticDynamicallyDefineDataIdentifier:
        """
        Creates a new DiagnosticDynamicallyDefineDataIdentifier with the given
        short name, or returns an existing one if it already exists in this package.

        DiagnosticDynamicallyDefineDataIdentifier represents an instance of the
        "Dynamically Define Data Identifier" diagnostic service.

        Args:
            short_name: The short name for the new DiagnosticDynamicallyDefineDataIdentifier

        Returns:
            The newly created or existing DiagnosticDynamicallyDefineDataIdentifier instance
        """
        if not self.IsReferrableElementExists(short_name, DiagnosticDynamicallyDefineDataIdentifier):
            dddi = DiagnosticDynamicallyDefineDataIdentifier(self, short_name)
            self.addReferrableElement(dddi)
        return cast(DiagnosticDynamicallyDefineDataIdentifier, self.getReferrableElement(short_name, DiagnosticDynamicallyDefineDataIdentifier))

    def createDiagnosticDynamicallyDefineDataIdentifierClass(self, short_name: str) -> DiagnosticDynamicallyDefineDataIdentifierClass:
        """
        Creates a new DiagnosticDynamicallyDefineDataIdentifierClass with the given
        short name, or returns an existing one if it already exists in this package.

        DiagnosticDynamicallyDefineDataIdentifierClass contains attributes shared by all
        instances of the "Dynamically Define Data Identifier" diagnostic service.

        Args:
            short_name: The short name for the new DiagnosticDynamicallyDefineDataIdentifierClass

        Returns:
            The newly created or existing DiagnosticDynamicallyDefineDataIdentifierClass instance
        """
        if not self.IsReferrableElementExists(short_name, DiagnosticDynamicallyDefineDataIdentifierClass):
            dddi_class = DiagnosticDynamicallyDefineDataIdentifierClass(self, short_name)
            self.addReferrableElement(dddi_class)
        return cast(DiagnosticDynamicallyDefineDataIdentifierClass, self.getReferrableElement(short_name, DiagnosticDynamicallyDefineDataIdentifierClass))

    def createDiagnosticIOControl(self, short_name: str) -> DiagnosticIOControl:
        """
        Creates a new DiagnosticIOControl with the given short name,
        or returns an existing one if it already exists in this package.

        DiagnosticIOControl represents an instance of the "I/O Control"
        diagnostic service.

        Args:
            short_name: The short name for the new DiagnosticIOControl

        Returns:
            The newly created or existing DiagnosticIOControl instance
        """
        if not self.IsReferrableElementExists(short_name, DiagnosticIOControl):
            io_control = DiagnosticIOControl(self, short_name)
            self.addReferrableElement(io_control)
        return cast(DiagnosticIOControl, self.getReferrableElement(short_name, DiagnosticIOControl))

    def createDiagnosticIndicator(self, short_name: str) -> DiagnosticIndicator:
        """
        Creates a new DiagnosticIndicator with the given short name,
        or returns an existing one if it already exists in this package.

        DiagnosticIndicator: Definition of an indicator.

        Args:
            short_name: The short name for the new DiagnosticIndicator

        Returns:
            The newly created or existing DiagnosticIndicator instance
        """
        if not self.IsReferrableElementExists(short_name, DiagnosticIndicator):
            element = DiagnosticIndicator(self, short_name)
            self.addReferrableElement(element)
        return cast(DiagnosticIndicator, self.getReferrableElement(short_name, DiagnosticIndicator))

    def createDiagnosticIoControlClass(self, short_name: str) -> DiagnosticIoControlClass:
        """
        Creates a new DiagnosticIoControlClass with the given short name,
        or returns an existing one if it already exists in this package.

        DiagnosticIoControlClass contains attributes shared by all
        instances of the "IO Control" diagnostic service.

        Args:
            short_name: The short name for the new DiagnosticIoControlClass

        Returns:
            The newly created or existing DiagnosticIoControlClass instance
        """
        if not self.IsReferrableElementExists(short_name, DiagnosticIoControlClass):
            io_control_class = DiagnosticIoControlClass(self, short_name)
            self.addReferrableElement(io_control_class)
        return cast(DiagnosticIoControlClass, self.getReferrableElement(short_name, DiagnosticIoControlClass))

    def createDiagnosticReadDTCInformation(self, short_name: str) -> DiagnosticReadDTCInformation:
        """
        Creates a new DiagnosticReadDTCInformation with the given short name,
        or returns an existing one if it already exists in this package.

        DiagnosticReadDTCInformation represents an instance of the
        "Read DTC Information" diagnostic service.

        Args:
            short_name: The short name for the new DiagnosticReadDTCInformation

        Returns:
            The newly created or existing DiagnosticReadDTCInformation instance
        """
        if not self.IsReferrableElementExists(short_name, DiagnosticReadDTCInformation):
            read_dtc_information = DiagnosticReadDTCInformation(self, short_name)
            self.addReferrableElement(read_dtc_information)
        return cast(DiagnosticReadDTCInformation, self.getReferrableElement(short_name, DiagnosticReadDTCInformation))

    def createDiagnosticReadDTCInformationClass(self, short_name: str) -> DiagnosticReadDTCInformationClass:
        """
        Creates a new DiagnosticReadDTCInformationClass with the given short
        name, or returns an existing one if it already exists in this package.

        DiagnosticReadDTCInformationClass contains attributes shared by all
        instances of the "ReadDTCInformation" diagnostic service.

        Args:
            short_name: The short name for the new DiagnosticReadDTCInformationClass

        Returns:
            The newly created or existing DiagnosticReadDTCInformationClass instance
        """
        if not self.IsReferrableElementExists(short_name, DiagnosticReadDTCInformationClass):
            read_dtc_information_class = DiagnosticReadDTCInformationClass(self, short_name)
            self.addReferrableElement(read_dtc_information_class)
        return cast(DiagnosticReadDTCInformationClass, self.getReferrableElement(short_name, DiagnosticReadDTCInformationClass))

    def createDiagnosticReadDataByIdentifier(self, short_name: str) -> DiagnosticReadDataByIdentifier:
        """
        Creates a new DiagnosticReadDataByIdentifier with the given short name,
        or returns an existing one if it already exists in this package.

        DiagnosticReadDataByIdentifier represents an instance of the "Read Data by Identifier" diagnostic service.

        Args:
            short_name: The short name for the new DiagnosticReadDataByIdentifier

        Returns:
            The newly created or existing DiagnosticReadDataByIdentifier instance
        """
        if not self.IsReferrableElementExists(short_name, DiagnosticReadDataByIdentifier):
            read_data_by_identifier = DiagnosticReadDataByIdentifier(self, short_name)
            self.addReferrableElement(read_data_by_identifier)
        return cast(DiagnosticReadDataByIdentifier, self.getReferrableElement(short_name, DiagnosticReadDataByIdentifier))

    def createDiagnosticReadDataByIdentifierClass(self, short_name: str) -> DiagnosticReadDataByIdentifierClass:
        """
        Creates a new DiagnosticReadDataByIdentifierClass with the given short name,
        or returns an existing one if it already exists in this package.

        DiagnosticReadDataByIdentifierClass contains attributes shared by all
        instances of the "Read Data by Identifier" diagnostic service.

        Args:
            short_name: The short name for the new DiagnosticReadDataByIdentifierClass

        Returns:
            The newly created or existing DiagnosticReadDataByIdentifierClass instance
        """
        if not self.IsReferrableElementExists(short_name, DiagnosticReadDataByIdentifierClass):
            read_data_by_identifier_class = DiagnosticReadDataByIdentifierClass(self, short_name)
            self.addReferrableElement(read_data_by_identifier_class)
        return cast(DiagnosticReadDataByIdentifierClass, self.getReferrableElement(short_name, DiagnosticReadDataByIdentifierClass))

    def createDiagnosticReadDataByPeriodicID(self, short_name: str) -> DiagnosticReadDataByPeriodicID:
        """
        Creates a new DiagnosticReadDataByPeriodicID with the given short name,
        or returns an existing one if it already exists in this package.

        DiagnosticReadDataByPeriodicID represents an instance of the
        "Read Data by periodic Identifier" diagnostic service.

        Args:
            short_name: The short name for the new DiagnosticReadDataByPeriodicID

        Returns:
            The newly created or existing DiagnosticReadDataByPeriodicID instance
        """
        if not self.IsReferrableElementExists(short_name, DiagnosticReadDataByPeriodicID):
            read_data_by_periodic_id = DiagnosticReadDataByPeriodicID(self, short_name)
            self.addReferrableElement(read_data_by_periodic_id)
        return cast(DiagnosticReadDataByPeriodicID, self.getReferrableElement(short_name, DiagnosticReadDataByPeriodicID))

    def createDiagnosticReadDataByPeriodicIDClass(self, short_name: str) -> DiagnosticReadDataByPeriodicIDClass:
        """
        Creates a new DiagnosticReadDataByPeriodicIDClass with the given short name,
        or returns an existing one if it already exists in this package.

        DiagnosticReadDataByPeriodicIDClass contains attributes shared by all
        instances of the "Read Data by periodic Identifier" diagnostic service.

        Args:
            short_name: The short name for the new DiagnosticReadDataByPeriodicIDClass

        Returns:
            The newly created or existing DiagnosticReadDataByPeriodicIDClass instance
        """
        if not self.IsReferrableElementExists(short_name, DiagnosticReadDataByPeriodicIDClass):
            read_data_by_periodic_id_class = DiagnosticReadDataByPeriodicIDClass(self, short_name)
            self.addReferrableElement(read_data_by_periodic_id_class)
        return cast(DiagnosticReadDataByPeriodicIDClass, self.getReferrableElement(short_name, DiagnosticReadDataByPeriodicIDClass))

    def createDiagnosticReadScalingDataByIdentifier(self, short_name: str) -> DiagnosticReadScalingDataByIdentifier:
        """
        Creates a new DiagnosticReadScalingDataByIdentifier with the given short name,
        or returns an existing one if it already exists in this package.

        DiagnosticReadScalingDataByIdentifier represents an instance of the "Read Scaling Data by Identifier" diagnostic service.

        Args:
            short_name: The short name for the new DiagnosticReadScalingDataByIdentifier

        Returns:
            The newly created or existing DiagnosticReadScalingDataByIdentifier instance
        """
        if not self.IsReferrableElementExists(short_name, DiagnosticReadScalingDataByIdentifier):
            read_scaling_data_by_identifier = DiagnosticReadScalingDataByIdentifier(self, short_name)
            self.addReferrableElement(read_scaling_data_by_identifier)
        return cast(DiagnosticReadScalingDataByIdentifier, self.getReferrableElement(short_name, DiagnosticReadScalingDataByIdentifier))

    def createDiagnosticReadScalingDataByIdentifierClass(self, short_name: str) -> DiagnosticReadScalingDataByIdentifierClass:
        """
        Creates a new DiagnosticReadScalingDataByIdentifierClass with the given short name,
        or returns an existing one if it already exists in this package.

        DiagnosticReadScalingDataByIdentifierClass contains attributes shared by all
        instances of the "Read Scaling Data by Identifier" diagnostic service.

        Args:
            short_name: The short name for the new DiagnosticReadScalingDataByIdentifierClass

        Returns:
            The newly created or existing DiagnosticReadScalingDataByIdentifierClass instance
        """
        if not self.IsReferrableElementExists(short_name, DiagnosticReadScalingDataByIdentifierClass):
            read_scaling_data_by_identifier_class = DiagnosticReadScalingDataByIdentifierClass(self, short_name)
            self.addReferrableElement(read_scaling_data_by_identifier_class)
        return cast(DiagnosticReadScalingDataByIdentifierClass, self.getReferrableElement(short_name, DiagnosticReadScalingDataByIdentifierClass))

    def createDiagnosticReadMemoryByAddress(self, short_name: str) -> DiagnosticReadMemoryByAddress:
        """
        Creates a new DiagnosticReadMemoryByAddress with the given short name,
        or returns an existing one if it already exists in this package.

        DiagnosticReadMemoryByAddress: This represents an instance of the "Read Memory by Address" diagnostic service.

        Args:
            short_name: The short name for the new DiagnosticReadMemoryByAddress

        Returns:
            The newly created or existing DiagnosticReadMemoryByAddress instance
        """
        if not self.IsReferrableElementExists(short_name, DiagnosticReadMemoryByAddress):
            element = DiagnosticReadMemoryByAddress(self, short_name)
            self.addReferrableElement(element)
        return cast(DiagnosticReadMemoryByAddress, self.getReferrableElement(short_name, DiagnosticReadMemoryByAddress))

    def createDiagnosticReadMemoryByAddressClass(self, short_name: str) -> DiagnosticReadMemoryByAddressClass:
        """
        Creates a new DiagnosticReadMemoryByAddressClass with the given short
        name, or returns an existing one if it already exists in this package.

        DiagnosticReadMemoryByAddressClass contains attributes shared by all
        instances of the "Read Memory by Address" diagnostic service.

        Args:
            short_name: The short name for the new DiagnosticReadMemoryByAddressClass

        Returns:
            The newly created or existing DiagnosticReadMemoryByAddressClass instance
        """
        if not self.IsReferrableElementExists(short_name, DiagnosticReadMemoryByAddressClass):
            read_memory_by_address_class = DiagnosticReadMemoryByAddressClass(self, short_name)
            self.addReferrableElement(read_memory_by_address_class)
        return cast(DiagnosticReadMemoryByAddressClass, self.getReferrableElement(short_name, DiagnosticReadMemoryByAddressClass))

    def createDiagnosticTransferExit(self, short_name: str) -> DiagnosticTransferExit:
        """
        Creates a new DiagnosticTransferExit with the given short name, or
        returns an existing one if it already exists in this package.

        DiagnosticTransferExit represents an instance of the "Transfer Exit" diagnostic service.

        Args:
            short_name: The short name for the new DiagnosticTransferExit

        Returns:
            The newly created or existing DiagnosticTransferExit instance
        """
        if not self.IsReferrableElementExists(short_name, DiagnosticTransferExit):
            transfer_exit = DiagnosticTransferExit(self, short_name)
            self.addReferrableElement(transfer_exit)
        return cast(DiagnosticTransferExit, self.getReferrableElement(short_name, DiagnosticTransferExit))

    def createDiagnosticTransferExitClass(self, short_name: str) -> DiagnosticTransferExitClass:
        """
        Creates a new DiagnosticTransferExitClass with the given short name,
        or returns an existing one if it already exists in this package.

        DiagnosticTransferExitClass contains attributes shared by all
        instances of the "Transfer Exit" diagnostic service.

        Args:
            short_name: The short name for the new DiagnosticTransferExitClass

        Returns:
            The newly created or existing DiagnosticTransferExitClass instance
        """
        if not self.IsReferrableElementExists(short_name, DiagnosticTransferExitClass):
            transfer_exit_class = DiagnosticTransferExitClass(self, short_name)
            self.addReferrableElement(transfer_exit_class)
        return cast(DiagnosticTransferExitClass, self.getReferrableElement(short_name, DiagnosticTransferExitClass))

    def createDiagnosticDataTransfer(self, short_name: str) -> DiagnosticDataTransfer:
        """
        Creates a new DiagnosticDataTransfer with the given short name, or
        returns an existing one if it already exists in this package.

        DiagnosticDataTransfer represents an instance of the "Data Transfer" diagnostic service.

        Args:
            short_name: The short name for the new DiagnosticDataTransfer

        Returns:
            The newly created or existing DiagnosticDataTransfer instance
        """
        if not self.IsReferrableElementExists(short_name, DiagnosticDataTransfer):
            data_transfer = DiagnosticDataTransfer(self, short_name)
            self.addReferrableElement(data_transfer)
        return cast(DiagnosticDataTransfer, self.getReferrableElement(short_name, DiagnosticDataTransfer))

    def createDiagnosticDataTransferClass(self, short_name: str) -> DiagnosticDataTransferClass:
        """
        Creates a new DiagnosticDataTransferClass with the given short name,
        or returns an existing one if it already exists in this package.

        DiagnosticDataTransferClass contains attributes shared by all
        instances of the "Data Transfer" diagnostic service.

        Args:
            short_name: The short name for the new DiagnosticDataTransferClass

        Returns:
            The newly created or existing DiagnosticDataTransferClass instance
        """
        if not self.IsReferrableElementExists(short_name, DiagnosticDataTransferClass):
            data_transfer_class = DiagnosticDataTransferClass(self, short_name)
            self.addReferrableElement(data_transfer_class)
        return cast(DiagnosticDataTransferClass, self.getReferrableElement(short_name, DiagnosticDataTransferClass))

    def createDiagnosticRequestDownload(self, short_name: str) -> DiagnosticRequestDownload:
        """
        Creates a new DiagnosticRequestDownload with the given short name, or
        returns an existing one if it already exists in this package.

        DiagnosticRequestDownload represents an instance of the "Request Download" diagnostic service.

        Args:
            short_name: The short name for the new DiagnosticRequestDownload

        Returns:
            The newly created or existing DiagnosticRequestDownload instance
        """
        if not self.IsReferrableElementExists(short_name, DiagnosticRequestDownload):
            request_download = DiagnosticRequestDownload(self, short_name)
            self.addReferrableElement(request_download)
        return cast(DiagnosticRequestDownload, self.getReferrableElement(short_name, DiagnosticRequestDownload))

    def createDiagnosticRequestDownloadClass(self, short_name: str) -> DiagnosticRequestDownloadClass:
        """
        Creates a new DiagnosticRequestDownloadClass with the given short name,
        or returns an existing one if it already exists in this package.

        DiagnosticRequestDownloadClass contains attributes shared by all
        instances of the "Request Download" diagnostic service.

        Args:
            short_name: The short name for the new DiagnosticRequestDownloadClass

        Returns:
            The newly created or existing DiagnosticRequestDownloadClass instance
        """
        if not self.IsReferrableElementExists(short_name, DiagnosticRequestDownloadClass):
            request_download_class = DiagnosticRequestDownloadClass(self, short_name)
            self.addReferrableElement(request_download_class)
        return cast(DiagnosticRequestDownloadClass, self.getReferrableElement(short_name, DiagnosticRequestDownloadClass))

    def createDiagnosticRequestEmissionRelatedDTC(self, short_name: str) -> DiagnosticRequestEmissionRelatedDTC:
        """
        Creates a new DiagnosticRequestEmissionRelatedDTC with the given short name, or
        returns an existing one if it already exists in this package.

        DiagnosticRequestEmissionRelatedDTC represents an instance of the OBD mode 0x03/0x07 service.

        Args:
            short_name: The short name for the new DiagnosticRequestEmissionRelatedDTC

        Returns:
            The newly created or existing DiagnosticRequestEmissionRelatedDTC instance
        """
        if not self.IsReferrableElementExists(short_name, DiagnosticRequestEmissionRelatedDTC):
            request_emission_related_dtc = DiagnosticRequestEmissionRelatedDTC(self, short_name)
            self.addReferrableElement(request_emission_related_dtc)
        return cast(DiagnosticRequestEmissionRelatedDTC, self.getReferrableElement(short_name, DiagnosticRequestEmissionRelatedDTC))

    def createDiagnosticRequestEmissionRelatedDTCClass(self, short_name: str) -> DiagnosticRequestEmissionRelatedDTCClass:
        """
        Creates a new DiagnosticRequestEmissionRelatedDTCClass with the given short name,
        or returns an existing one if it already exists in this package.

        DiagnosticRequestEmissionRelatedDTCClass contains attributes shared by all
        instances of the "Request Emission Related DTC" OBD diagnostic service.

        Args:
            short_name: The short name for the new DiagnosticRequestEmissionRelatedDTCClass

        Returns:
            The newly created or existing DiagnosticRequestEmissionRelatedDTCClass instance
        """
        if not self.IsReferrableElementExists(short_name, DiagnosticRequestEmissionRelatedDTCClass):
            request_emission_related_dtc_class = DiagnosticRequestEmissionRelatedDTCClass(self, short_name)
            self.addReferrableElement(request_emission_related_dtc_class)
        return cast(DiagnosticRequestEmissionRelatedDTCClass, self.getReferrableElement(short_name, DiagnosticRequestEmissionRelatedDTCClass))

    def createDiagnosticRequestEmissionRelatedDTCPermanentStatus(self, short_name: str) -> DiagnosticRequestEmissionRelatedDTCPermanentStatus:
        """
        Creates a new DiagnosticRequestEmissionRelatedDTCPermanentStatus with the given short name, or
        returns an existing one if it already exists in this package.

        DiagnosticRequestEmissionRelatedDTCPermanentStatus represents an instance of the OBD mode 0x0A service.

        Args:
            short_name: The short name for the new DiagnosticRequestEmissionRelatedDTCPermanentStatus

        Returns:
            The newly created or existing DiagnosticRequestEmissionRelatedDTCPermanentStatus instance
        """
        if not self.IsReferrableElementExists(short_name, DiagnosticRequestEmissionRelatedDTCPermanentStatus):
            request_emission_related_dtc_permanent_status = DiagnosticRequestEmissionRelatedDTCPermanentStatus(self, short_name)
            self.addReferrableElement(request_emission_related_dtc_permanent_status)
        return cast(DiagnosticRequestEmissionRelatedDTCPermanentStatus, self.getReferrableElement(short_name, DiagnosticRequestEmissionRelatedDTCPermanentStatus))

    def createDiagnosticRequestEmissionRelatedDTCPermanentStatusClass(self, short_name: str) -> DiagnosticRequestEmissionRelatedDTCPermanentStatusClass:
        """
        Creates a new DiagnosticRequestEmissionRelatedDTCPermanentStatusClass with the given short name,
        or returns an existing one if it already exists in this package.

        DiagnosticRequestEmissionRelatedDTCPermanentStatusClass defines common properties for all
        instances of the "Request Emission Related DTC Permanent Status" OBD diagnostic service.

        Args:
            short_name: The short name for the new DiagnosticRequestEmissionRelatedDTCPermanentStatusClass

        Returns:
            The newly created or existing DiagnosticRequestEmissionRelatedDTCPermanentStatusClass instance
        """
        if not self.IsReferrableElementExists(short_name, DiagnosticRequestEmissionRelatedDTCPermanentStatusClass):
            request_emission_related_dtc_permanent_status_class = DiagnosticRequestEmissionRelatedDTCPermanentStatusClass(self, short_name)
            self.addReferrableElement(request_emission_related_dtc_permanent_status_class)
        return cast(DiagnosticRequestEmissionRelatedDTCPermanentStatusClass, self.getReferrableElement(short_name, DiagnosticRequestEmissionRelatedDTCPermanentStatusClass))

    def createDiagnosticRequestUpload(self, short_name: str) -> DiagnosticRequestUpload:
        """
        Creates a new DiagnosticRequestUpload with the given short name, or
        returns an existing one if it already exists in this package.

        DiagnosticRequestUpload represents an instance of the "Request Upload" diagnostic service.

        Args:
            short_name: The short name for the new DiagnosticRequestUpload

        Returns:
            The newly created or existing DiagnosticRequestUpload instance
        """
        if not self.IsReferrableElementExists(short_name, DiagnosticRequestUpload):
            request_upload = DiagnosticRequestUpload(self, short_name)
            self.addReferrableElement(request_upload)
        return cast(DiagnosticRequestUpload, self.getReferrableElement(short_name, DiagnosticRequestUpload))

    def createDiagnosticRequestUploadClass(self, short_name: str) -> DiagnosticRequestUploadClass:
        """
        Creates a new DiagnosticRequestUploadClass with the given short name,
        or returns an existing one if it already exists in this package.

        DiagnosticRequestUploadClass contains attributes shared by all
        instances of the "Request Upload" diagnostic service.

        Args:
            short_name: The short name for the new DiagnosticRequestUploadClass

        Returns:
            The newly created or existing DiagnosticRequestUploadClass instance
        """
        if not self.IsReferrableElementExists(short_name, DiagnosticRequestUploadClass):
            request_upload_class = DiagnosticRequestUploadClass(self, short_name)
            self.addReferrableElement(request_upload_class)
        return cast(DiagnosticRequestUploadClass, self.getReferrableElement(short_name, DiagnosticRequestUploadClass))

    def createDiagnosticRequestVehicleInfo(self, short_name: str) -> DiagnosticRequestVehicleInfo:
        """
        Creates a new DiagnosticRequestVehicleInfo with the given short name, or
        returns an existing one if it already exists in this package.

        DiagnosticRequestVehicleInfo represents an instance of the OBD mode 0x09 service.

        Args:
            short_name: The short name for the new DiagnosticRequestVehicleInfo

        Returns:
            The newly created or existing DiagnosticRequestVehicleInfo instance
        """
        if not self.IsReferrableElementExists(short_name, DiagnosticRequestVehicleInfo):
            request_vehicle_info = DiagnosticRequestVehicleInfo(self, short_name)
            self.addReferrableElement(request_vehicle_info)
        return cast(DiagnosticRequestVehicleInfo, self.getReferrableElement(short_name, DiagnosticRequestVehicleInfo))

    def createDiagnosticRequestVehicleInfoClass(self, short_name: str) -> DiagnosticRequestVehicleInfoClass:
        """
        Creates a new DiagnosticRequestVehicleInfoClass with the given short name,
        or returns an existing one if it already exists in this package.

        DiagnosticRequestVehicleInfoClass contains attributes shared by all
        instances of the "Request Vehicle Info" OBD diagnostic service.

        Args:
            short_name: The short name for the new DiagnosticRequestVehicleInfoClass

        Returns:
            The newly created or existing DiagnosticRequestVehicleInfoClass instance
        """
        if not self.IsReferrableElementExists(short_name, DiagnosticRequestVehicleInfoClass):
            request_vehicle_info_class = DiagnosticRequestVehicleInfoClass(self, short_name)
            self.addReferrableElement(request_vehicle_info_class)
        return cast(DiagnosticRequestVehicleInfoClass, self.getReferrableElement(short_name, DiagnosticRequestVehicleInfoClass))

    def createDiagnosticRequestFileTransfer(self, short_name: str) -> DiagnosticRequestFileTransfer:
        """
        Creates a new DiagnosticRequestFileTransfer with the given short name, or
        returns an existing one if it already exists in this package.

        DiagnosticRequestFileTransfer represents an instance of the "Request File transfer" diagnostic service.

        Args:
            short_name: The short name for the new DiagnosticRequestFileTransfer

        Returns:
            The newly created or existing DiagnosticRequestFileTransfer instance
        """
        if not self.IsReferrableElementExists(short_name, DiagnosticRequestFileTransfer):
            request_file_transfer = DiagnosticRequestFileTransfer(self, short_name)
            self.addReferrableElement(request_file_transfer)
        return cast(DiagnosticRequestFileTransfer, self.getReferrableElement(short_name, DiagnosticRequestFileTransfer))

    def createDiagnosticRequestFileTransferClass(self, short_name: str) -> DiagnosticRequestFileTransferClass:
        """
        Creates a new DiagnosticRequestFileTransferClass with the given short name,
        or returns an existing one if it already exists in this package.

        DiagnosticRequestFileTransferClass contains attributes shared by all
        instances of the "Request File transfer" diagnostic service.

        Args:
            short_name: The short name for the new DiagnosticRequestFileTransferClass

        Returns:
            The newly created or existing DiagnosticRequestFileTransferClass instance
        """
        if not self.IsReferrableElementExists(short_name, DiagnosticRequestFileTransferClass):
            request_file_transfer_class = DiagnosticRequestFileTransferClass(self, short_name)
            self.addReferrableElement(request_file_transfer_class)
        return cast(DiagnosticRequestFileTransferClass, self.getReferrableElement(short_name, DiagnosticRequestFileTransferClass))

    def createDiagnosticParameterIdentifier(self, short_name: str) -> DiagnosticParameterIdentifier:
        """
        Creates a new DiagnosticParameterIdentifier with the given short name, or
        returns an existing one if it already exists in this package.

        DiagnosticParameterIdentifier represents the ability to model a diagnostic
        parameter identifier (PID) for the purpose of executing on-board diagnostics (OBD).

        Args:
            short_name: The short name for the new DiagnosticParameterIdentifier

        Returns:
            The newly created or existing DiagnosticParameterIdentifier instance
        """
        if not self.IsReferrableElementExists(short_name, DiagnosticParameterIdentifier):
            parameter_identifier = DiagnosticParameterIdentifier(self, short_name)
            self.addReferrableElement(parameter_identifier)
        return cast(DiagnosticParameterIdentifier, self.getReferrableElement(short_name, DiagnosticParameterIdentifier))

    def createDiagnosticRequestCurrentPowertrainData(self, short_name: str) -> DiagnosticRequestCurrentPowertrainData:
        """
        Creates a new DiagnosticRequestCurrentPowertrainData with the given short name, or
        returns an existing one if it already exists in this package.

        DiagnosticRequestCurrentPowertrainData represents an instance of the OBD mode 0x01 service.

        Args:
            short_name: The short name for the new DiagnosticRequestCurrentPowertrainData

        Returns:
            The newly created or existing DiagnosticRequestCurrentPowertrainData instance
        """
        if not self.IsReferrableElementExists(short_name, DiagnosticRequestCurrentPowertrainData):
            request_current_powertrain_data = DiagnosticRequestCurrentPowertrainData(self, short_name)
            self.addReferrableElement(request_current_powertrain_data)
        return cast(DiagnosticRequestCurrentPowertrainData, self.getReferrableElement(short_name, DiagnosticRequestCurrentPowertrainData))

    def createDiagnosticRequestCurrentPowertrainDataClass(self, short_name: str) -> DiagnosticRequestCurrentPowertrainDataClass:
        """
        Creates a new DiagnosticRequestCurrentPowertrainDataClass with the given short name,
        or returns an existing one if it already exists in this package.

        DiagnosticRequestCurrentPowertrainDataClass contains attributes shared by all
        instances of the "Request current Powertrain Data" OBD diagnostic service.

        Args:
            short_name: The short name for the new DiagnosticRequestCurrentPowertrainDataClass

        Returns:
            The newly created or existing DiagnosticRequestCurrentPowertrainDataClass instance
        """
        if not self.IsReferrableElementExists(short_name, DiagnosticRequestCurrentPowertrainDataClass):
            request_current_powertrain_data_class = DiagnosticRequestCurrentPowertrainDataClass(self, short_name)
            self.addReferrableElement(request_current_powertrain_data_class)
        return cast(DiagnosticRequestCurrentPowertrainDataClass, self.getReferrableElement(short_name, DiagnosticRequestCurrentPowertrainDataClass))

    def createDiagnosticRequestOnBoardMonitoringTestResults(self, short_name: str) -> DiagnosticRequestOnBoardMonitoringTestResults:
        """
        Creates a new DiagnosticRequestOnBoardMonitoringTestResults with the given short name, or
        returns an existing one if it already exists in this package.

        DiagnosticRequestOnBoardMonitoringTestResults represents an instance of the OBD mode 0x06 service.

        Args:
            short_name: The short name for the new DiagnosticRequestOnBoardMonitoringTestResults

        Returns:
            The newly created or existing DiagnosticRequestOnBoardMonitoringTestResults instance
        """
        if not self.IsReferrableElementExists(short_name, DiagnosticRequestOnBoardMonitoringTestResults):
            request_on_board_monitoring_test_results = DiagnosticRequestOnBoardMonitoringTestResults(self, short_name)
            self.addReferrableElement(request_on_board_monitoring_test_results)
        return cast(DiagnosticRequestOnBoardMonitoringTestResults, self.getReferrableElement(short_name, DiagnosticRequestOnBoardMonitoringTestResults))

    def createDiagnosticRequestOnBoardMonitoringTestResultsClass(self, short_name: str) -> DiagnosticRequestOnBoardMonitoringTestResultsClass:
        """
        Creates a new DiagnosticRequestOnBoardMonitoringTestResultsClass with the given short name,
        or returns an existing one if it already exists in this package.

        DiagnosticRequestOnBoardMonitoringTestResultsClass contains attributes shared by all
        instances of the "Request On-Board Monitoring Test Results" OBD diagnostic service.

        Args:
            short_name: The short name for the new DiagnosticRequestOnBoardMonitoringTestResultsClass

        Returns:
            The newly created or existing DiagnosticRequestOnBoardMonitoringTestResultsClass instance
        """
        if not self.IsReferrableElementExists(short_name, DiagnosticRequestOnBoardMonitoringTestResultsClass):
            request_on_board_monitoring_test_results_class = DiagnosticRequestOnBoardMonitoringTestResultsClass(self, short_name)
            self.addReferrableElement(request_on_board_monitoring_test_results_class)
        return cast(DiagnosticRequestOnBoardMonitoringTestResultsClass, self.getReferrableElement(short_name, DiagnosticRequestOnBoardMonitoringTestResultsClass))

    def createDiagnosticRequestPowertrainFreezeFrameData(self, short_name: str) -> DiagnosticRequestPowertrainFreezeFrameData:
        """
        Creates a new DiagnosticRequestPowertrainFreezeFrameData with the given short name, or
        returns an existing one if it already exists in this package.

        DiagnosticRequestPowertrainFreezeFrameData represents an instance of the OBD mode 0x02 service.

        Args:
            short_name: The short name for the new DiagnosticRequestPowertrainFreezeFrameData

        Returns:
            The newly created or existing DiagnosticRequestPowertrainFreezeFrameData instance
        """
        if not self.IsReferrableElementExists(short_name, DiagnosticRequestPowertrainFreezeFrameData):
            request_powertrain_freeze_frame_data = DiagnosticRequestPowertrainFreezeFrameData(self, short_name)
            self.addReferrableElement(request_powertrain_freeze_frame_data)
        return cast(DiagnosticRequestPowertrainFreezeFrameData, self.getReferrableElement(short_name, DiagnosticRequestPowertrainFreezeFrameData))

    def createDiagnosticRequestPowertrainFreezeFrameDataClass(self, short_name: str) -> DiagnosticRequestPowertrainFreezeFrameDataClass:
        """
        Creates a new DiagnosticRequestPowertrainFreezeFrameDataClass with the given short name,
        or returns an existing one if it already exists in this package.

        DiagnosticRequestPowertrainFreezeFrameDataClass contains attributes shared by all
        instances of the "Request Powertrain Freeze Frame Data" OBD diagnostic service.

        Args:
            short_name: The short name for the new DiagnosticRequestPowertrainFreezeFrameDataClass

        Returns:
            The newly created or existing DiagnosticRequestPowertrainFreezeFrameDataClass instance
        """
        if not self.IsReferrableElementExists(short_name, DiagnosticRequestPowertrainFreezeFrameDataClass):
            request_powertrain_freeze_frame_data_class = DiagnosticRequestPowertrainFreezeFrameDataClass(self, short_name)
            self.addReferrableElement(request_powertrain_freeze_frame_data_class)
        return cast(DiagnosticRequestPowertrainFreezeFrameDataClass, self.getReferrableElement(short_name, DiagnosticRequestPowertrainFreezeFrameDataClass))

    def createDiagnosticPowertrainFreezeFrame(self, short_name: str) -> DiagnosticPowertrainFreezeFrame:
        """
        Creates a new DiagnosticPowertrainFreezeFrame with the given short name, or
        returns an existing one if it already exists in this package.

        DiagnosticPowertrainFreezeFrame represents a powertrain-related freeze-frame.

        Args:
            short_name: The short name for the new DiagnosticPowertrainFreezeFrame

        Returns:
            The newly created or existing DiagnosticPowertrainFreezeFrame instance
        """
        if not self.IsReferrableElementExists(short_name, DiagnosticPowertrainFreezeFrame):
            powertrain_freeze_frame = DiagnosticPowertrainFreezeFrame(self, short_name)
            self.addReferrableElement(powertrain_freeze_frame)
        return cast(DiagnosticPowertrainFreezeFrame, self.getReferrableElement(short_name, DiagnosticPowertrainFreezeFrame))

    def createDiagnosticResponseOnEvent(self, short_name: str) -> DiagnosticResponseOnEvent:
        """
        Creates a new DiagnosticResponseOnEvent with the given short name,
        or returns an existing one if it already exists in this package.

        DiagnosticResponseOnEvent represents an instance of the
        "Response on Event" diagnostic service.

        Args:
            short_name: The short name for the new DiagnosticResponseOnEvent

        Returns:
            The newly created or existing DiagnosticResponseOnEvent instance
        """
        if not self.IsReferrableElementExists(short_name, DiagnosticResponseOnEvent):
            response_on_event = DiagnosticResponseOnEvent(self, short_name)
            self.addReferrableElement(response_on_event)
        return cast(DiagnosticResponseOnEvent, self.getReferrableElement(short_name, DiagnosticResponseOnEvent))

    def createDiagnosticResponseOnEventClass(self, short_name: str) -> DiagnosticResponseOnEventClass:
        """
        Creates a new DiagnosticResponseOnEventClass with the given short
        name, or returns an existing one if it already exists in this package.

        DiagnosticResponseOnEventClass contains attributes shared by all
        instances of the "Response on Event" diagnostic service.

        Args:
            short_name: The short name for the new DiagnosticResponseOnEventClass

        Returns:
            The newly created or existing DiagnosticResponseOnEventClass instance
        """
        if not self.IsReferrableElementExists(short_name, DiagnosticResponseOnEventClass):
            response_on_event_class = DiagnosticResponseOnEventClass(self, short_name)
            self.addReferrableElement(response_on_event_class)
        return cast(DiagnosticResponseOnEventClass, self.getReferrableElement(short_name, DiagnosticResponseOnEventClass))

    def createDiagnosticRoutine(self, short_name: str) -> DiagnosticRoutine:
        """
        Creates a new DiagnosticRoutine with the given short name,
        or returns an existing one if it already exists in this package.

        DiagnosticRoutine represents the ability to define a diagnostic routine.

        Args:
            short_name: The short name for the new DiagnosticRoutine

        Returns:
            The newly created or existing DiagnosticRoutine instance
        """
        if not self.IsReferrableElementExists(short_name, DiagnosticRoutine):
            routine = DiagnosticRoutine(self, short_name)
            self.addReferrableElement(routine)
        return cast(DiagnosticRoutine, self.getReferrableElement(short_name, DiagnosticRoutine))

    def createDiagnosticRoutineControl(self, short_name: str) -> DiagnosticRoutineControl:
        """
        Creates a new DiagnosticRoutineControl with the given short name,
        or returns an existing one if it already exists in this package.

        DiagnosticRoutineControl represents an instance of the "Routine Control"
        diagnostic service.

        Args:
            short_name: The short name for the new DiagnosticRoutineControl

        Returns:
            The newly created or existing DiagnosticRoutineControl instance
        """
        if not self.IsReferrableElementExists(short_name, DiagnosticRoutineControl):
            routine_control = DiagnosticRoutineControl(self, short_name)
            self.addReferrableElement(routine_control)
        return cast(DiagnosticRoutineControl, self.getReferrableElement(short_name, DiagnosticRoutineControl))

    def createDiagnosticRoutineControlClass(self, short_name: str) -> DiagnosticRoutineControlClass:
        """
        Creates a new DiagnosticRoutineControlClass with the given short name,
        or returns an existing one if it already exists in this package.

        DiagnosticRoutineControlClass contains attributes shared by all
        instances of the "Routine Control" diagnostic service.

        Args:
            short_name: The short name for the new DiagnosticRoutineControlClass

        Returns:
            The newly created or existing DiagnosticRoutineControlClass instance
        """
        if not self.IsReferrableElementExists(short_name, DiagnosticRoutineControlClass):
            routine_control_class = DiagnosticRoutineControlClass(self, short_name)
            self.addReferrableElement(routine_control_class)
        return cast(DiagnosticRoutineControlClass, self.getReferrableElement(short_name, DiagnosticRoutineControlClass))

    def createDiagnosticWriteDataByIdentifier(self, short_name: str) -> DiagnosticWriteDataByIdentifier:
        """
        Creates a new DiagnosticWriteDataByIdentifier with the given short name,
        or returns an existing one if it already exists in this package.

        DiagnosticWriteDataByIdentifier represents an instance of the "Write Data by Identifier" diagnostic service.

        Args:
            short_name: The short name for the new DiagnosticWriteDataByIdentifier

        Returns:
            The newly created or existing DiagnosticWriteDataByIdentifier instance
        """
        if not self.IsReferrableElementExists(short_name, DiagnosticWriteDataByIdentifier):
            write_data_by_identifier = DiagnosticWriteDataByIdentifier(self, short_name)
            self.addReferrableElement(write_data_by_identifier)
        return cast(DiagnosticWriteDataByIdentifier, self.getReferrableElement(short_name, DiagnosticWriteDataByIdentifier))

    def createDiagnosticWriteDataByIdentifierClass(self, short_name: str) -> DiagnosticWriteDataByIdentifierClass:
        """
        Creates a new DiagnosticWriteDataByIdentifierClass with the given short name,
        or returns an existing one if it already exists in this package.

        DiagnosticWriteDataByIdentifierClass contains attributes shared by all
        instances of the "Write Data by Identifier" diagnostic service.

        Args:
            short_name: The short name for the new DiagnosticWriteDataByIdentifierClass

        Returns:
            The newly created or existing DiagnosticWriteDataByIdentifierClass instance
        """
        if not self.IsReferrableElementExists(short_name, DiagnosticWriteDataByIdentifierClass):
            write_data_by_identifier_class = DiagnosticWriteDataByIdentifierClass(self, short_name)
            self.addReferrableElement(write_data_by_identifier_class)
        return cast(DiagnosticWriteDataByIdentifierClass, self.getReferrableElement(short_name, DiagnosticWriteDataByIdentifierClass))

    def createDiagnosticWriteMemoryByAddress(self, short_name: str) -> DiagnosticWriteMemoryByAddress:
        """
        Creates a new DiagnosticWriteMemoryByAddress with the given short name,
        or returns an existing one if it already exists in this package.

        DiagnosticWriteMemoryByAddress: This represents an instance of the "Write Memory by Address" diagnostic service.

        Args:
            short_name: The short name for the new DiagnosticWriteMemoryByAddress

        Returns:
            The newly created or existing DiagnosticWriteMemoryByAddress instance
        """
        if not self.IsReferrableElementExists(short_name, DiagnosticWriteMemoryByAddress):
            element = DiagnosticWriteMemoryByAddress(self, short_name)
            self.addReferrableElement(element)
        return cast(DiagnosticWriteMemoryByAddress, self.getReferrableElement(short_name, DiagnosticWriteMemoryByAddress))

    def createDiagnosticWriteMemoryByAddressClass(self, short_name: str) -> DiagnosticWriteMemoryByAddressClass:
        """
        Creates a new DiagnosticWriteMemoryByAddressClass with the given short
        name, or returns an existing one if it already exists in this package.

        DiagnosticWriteMemoryByAddressClass contains attributes shared by all
        instances of the "Write Memory by Address" diagnostic service.

        Args:
            short_name: The short name for the new DiagnosticWriteMemoryByAddressClass

        Returns:
            The newly created or existing DiagnosticWriteMemoryByAddressClass instance
        """
        if not self.IsReferrableElementExists(short_name, DiagnosticWriteMemoryByAddressClass):
            write_memory_by_address_class = DiagnosticWriteMemoryByAddressClass(self, short_name)
            self.addReferrableElement(write_memory_by_address_class)
        return cast(DiagnosticWriteMemoryByAddressClass, self.getReferrableElement(short_name, DiagnosticWriteMemoryByAddressClass))

    def createEcuAbstractionSwComponentType(self, short_name: str) -> EcuAbstractionSwComponentType:

        if not self.IsReferrableElementExists(short_name, EcuAbstractionSwComponentType):
            sw_component = EcuAbstractionSwComponentType(self, short_name)
            self.addReferrableElement(sw_component)
        return cast(EcuAbstractionSwComponentType, self.getReferrableElement(short_name, EcuAbstractionSwComponentType))

    def createParameterSwComponentType(self, short_name: str) -> ParameterSwComponentType:
        if not self.IsReferrableElementExists(short_name, ParameterSwComponentType):
            sw_component = ParameterSwComponentType(self, short_name)
            self.addReferrableElement(sw_component)
        return cast(ParameterSwComponentType, self.getReferrableElement(short_name, ParameterSwComponentType))

    def createApplicationSwComponentType(self, short_name: str) -> ApplicationSwComponentType:
        """
        Creates a new Application Software Component Type with the given short name,
        or returns an existing one if it already exists in this package.

        ApplicationSwComponentType represents a software component that implements
        application-specific functionality, typically containing runnables and
        communication interfaces.

        Args:
            short_name: The short name for the new ApplicationSwComponentType

        Returns:
            The newly created or existing ApplicationSwComponentType instance
        """

        if not self.IsReferrableElementExists(short_name, ApplicationSwComponentType):
            sw_component = ApplicationSwComponentType(self, short_name)
            self.addReferrableElement(sw_component)
        return cast(ApplicationSwComponentType, self.getReferrableElement(short_name, ApplicationSwComponentType))

    def createComplexDeviceDriverSwComponentType(self, short_name: str) -> ComplexDeviceDriverSwComponentType:

        if not self.IsReferrableElementExists(short_name, ComplexDeviceDriverSwComponentType):
            sw_component = ComplexDeviceDriverSwComponentType(self, short_name)
            self.addReferrableElement(sw_component)
        return cast(ComplexDeviceDriverSwComponentType, self.getReferrableElement(short_name, ComplexDeviceDriverSwComponentType))

    def createServiceSwComponentType(self, short_name: str) -> ServiceSwComponentType:

        if not self.IsReferrableElementExists(short_name, ServiceSwComponentType):
            sw_component = ServiceSwComponentType(self, short_name)
            self.addReferrableElement(sw_component)
        return cast(ServiceSwComponentType, self.getReferrableElement(short_name, ServiceSwComponentType))

    def createSensorActuatorSwComponentType(self, short_name: str) -> SensorActuatorSwComponentType:

        if not self.IsReferrableElementExists(short_name, SensorActuatorSwComponentType):
            sw_component = SensorActuatorSwComponentType(self, short_name)
            self.addReferrableElement(sw_component)
        return cast(SensorActuatorSwComponentType, self.getReferrableElement(short_name, SensorActuatorSwComponentType))

    def createNvBlockSwComponentType(self, short_name: str) -> NvBlockSwComponentType:

        if not self.IsReferrableElementExists(short_name, NvBlockSwComponentType):
            sw_component = NvBlockSwComponentType(self, short_name)
            self.addReferrableElement(sw_component)
        return cast(NvBlockSwComponentType, self.getReferrableElement(short_name, NvBlockSwComponentType))

    def createServiceProxySwComponentType(self, short_name: str) -> ServiceProxySwComponentType:

        if not self.IsReferrableElementExists(short_name, ServiceProxySwComponentType):
            sw_component = ServiceProxySwComponentType(self, short_name)
            self.addReferrableElement(sw_component)
        return cast(ServiceProxySwComponentType, self.getReferrableElement(short_name, ServiceProxySwComponentType))

    def createCompositionSwComponentType(self, short_name: str) -> CompositionSwComponentType:

        if not self.IsReferrableElementExists(short_name, CompositionSwComponentType):
            sw_component = CompositionSwComponentType(self, short_name)
            self.addReferrableElement(sw_component)
        return cast(CompositionSwComponentType, self.getReferrableElement(short_name, CompositionSwComponentType))

    def createSenderReceiverInterface(self, short_name: str) -> SenderReceiverInterface:
        """
        Creates a new Sender-Receiver Interface with the given short name,
        or returns an existing one if it already exists in this package.

        SenderReceiverInterface is a communication interface type in AUTOSAR
        that enables data exchange between software components through
        sender and receiver ports.

        Args:
            short_name: The short name for the new SenderReceiverInterface

        Returns:
            The newly created or existing SenderReceiverInterface instance
        """

        if not self.IsReferrableElementExists(short_name, SenderReceiverInterface):
            sr_interface = SenderReceiverInterface(self, short_name)
            self.addReferrableElement(sr_interface)
        return cast(SenderReceiverInterface, self.getReferrableElement(short_name, SenderReceiverInterface))

    def createParameterInterface(self, short_name: str) -> ParameterInterface:

        if not self.IsReferrableElementExists(short_name, ParameterInterface):
            sr_interface = ParameterInterface(self, short_name)
            self.addReferrableElement(sr_interface)
        return cast(ParameterInterface, self.getReferrableElement(short_name, ParameterInterface))

    def createNvDataInterface(self, short_name: str) -> NvDataInterface:

        if not self.IsReferrableElementExists(short_name, NvDataInterface):
            nv_interface = NvDataInterface(self, short_name)
            self.addReferrableElement(nv_interface)
        return cast(NvDataInterface, self.getReferrableElement(short_name, NvDataInterface))

    def createGenericEthernetFrame(self, short_name: str) -> GenericEthernetFrame:

        if not self.IsReferrableElementExists(short_name, GenericEthernetFrame):
            frame = GenericEthernetFrame(self, short_name)
            self.addReferrableElement(frame)
        return cast(GenericEthernetFrame, self.getReferrableElement(short_name, GenericEthernetFrame))

    def createLifeCycleInfoSet(self, short_name: str) -> LifeCycleInfoSet:

        if not self.IsReferrableElementExists(short_name, LifeCycleInfoSet):
            set = LifeCycleInfoSet(self, short_name)
            self.addReferrableElement(set)
        return cast(LifeCycleInfoSet, self.getReferrableElement(short_name, LifeCycleInfoSet))

    def createDocumentation(self, short_name: str) -> Documentation:

        if not self.IsReferrableElementExists(short_name, Documentation):
            documentation = Documentation(self, short_name)
            self.addReferrableElement(documentation)
        return cast(Documentation, self.getReferrableElement(short_name, Documentation))

    def createClientServerInterface(self, short_name: str) -> ClientServerInterface:

        if not self.IsReferrableElementExists(short_name, ClientServerInterface):
            cs_interface = ClientServerInterface(self, short_name)
            self.addReferrableElement(cs_interface)
        return cast(ClientServerInterface, self.getReferrableElement(short_name, ClientServerInterface))

    def createApplicationPrimitiveDataType(self, short_name: str) -> ApplicationPrimitiveDataType:

        if not self.IsReferrableElementExists(short_name, ApplicationPrimitiveDataType):
            data_type = ApplicationPrimitiveDataType(self, short_name)
            self.addReferrableElement(data_type)
        return cast(ApplicationPrimitiveDataType, self.getReferrableElement(short_name, ApplicationPrimitiveDataType))

    def createApplicationRecordDataType(self, short_name: str) -> ApplicationRecordDataType:

        if not self.IsReferrableElementExists(short_name, ApplicationRecordDataType):
            data_type = ApplicationRecordDataType(self, short_name)
            self.addReferrableElement(data_type)
        return cast(ApplicationRecordDataType, self.getReferrableElement(short_name, ApplicationRecordDataType))

    def createApplicationDeferredDataType(self, short_name: str) -> ApplicationDeferredDataType:
        """
        Creates a new ApplicationDeferredDataType with the given short name,
        or returns an existing one if it already exists in this package.

        ApplicationDeferredDataType is a placeholder data type in which the precise
        application data type is deferred to a later stage.

        Args:
            short_name: The short name for the new ApplicationDeferredDataType

        Returns:
            The newly created or existing ApplicationDeferredDataType instance
        """

        if not self.IsReferrableElementExists(short_name, ApplicationDeferredDataType):
            data_type = ApplicationDeferredDataType(self, short_name)
            self.addReferrableElement(data_type)
        return cast(ApplicationDeferredDataType, self.getReferrableElement(short_name, ApplicationDeferredDataType))

    def createImplementationDataType(self, short_name: str) -> ImplementationDataType:
        """
        Creates a new Implementation Data Type with the given short name,
        or returns an existing one if it already exists in this package.

        ImplementationDataType represents data types used in the implementation
        layer of AUTOSAR, typically describing how application data types
        are mapped to implementation-specific types.

        Args:
            short_name: The short name for the new ImplementationDataType

        Returns:
            The newly created or existing ImplementationDataType instance
        """

        if not self.IsReferrableElementExists(short_name, ImplementationDataType):
            data_type = ImplementationDataType(self, short_name)
            self.addReferrableElement(data_type)
        return cast(ImplementationDataType, self.getReferrableElement(short_name, ImplementationDataType))

    def createSwBaseType(self, short_name: str) -> SwBaseType:

        if not self.IsReferrableElementExists(short_name, SwBaseType):
            base_type = SwBaseType(self, short_name)
            self.addReferrableElement(base_type)
        return cast(SwBaseType, self.getReferrableElement(short_name, SwBaseType))

    def createDataTypeMappingSet(self, short_name: str) -> DataTypeMappingSet:

        if not self.IsReferrableElementExists(short_name, DataTypeMappingSet):
            mapping_set = DataTypeMappingSet(self, short_name)
            self.addReferrableElement(mapping_set)
        return cast(DataTypeMappingSet, self.getReferrableElement(short_name, DataTypeMappingSet))

    def createCompuMethod(self, short_name: str) -> CompuMethod:

        if not self.IsReferrableElementExists(short_name, CompuMethod):
            compu_method = CompuMethod(self, short_name)
            self.addReferrableElement(compu_method)
        return cast(CompuMethod, self.getReferrableElement(short_name, CompuMethod))

    def createBswModuleDescription(self, short_name: str) -> BswModuleDescription:
        """
        Creates a new Basic Software Module Description with the given short name,
        or returns an existing one if it already exists in this package.

        BswModuleDescription represents the description of a basic software
        module in AUTOSAR, containing information about its functionality,
        interfaces, and configuration.

        Args:
            short_name: The short name for the new BswModuleDescription

        Returns:
            The newly created or existing BswModuleDescription instance
        """

        if not self.IsReferrableElementExists(short_name, BswModuleDescription):
            desc = BswModuleDescription(self, short_name)
            self.addReferrableElement(desc)
        return cast(BswModuleDescription, self.getReferrableElement(short_name, BswModuleDescription))

    def createBswModuleEntry(self, short_name: str) -> BswModuleEntry:

        if not self.IsReferrableElementExists(short_name, BswModuleEntry):
            entry = BswModuleEntry(self, short_name)
            self.addReferrableElement(entry)
        return cast(BswModuleEntry, self.getReferrableElement(short_name, BswModuleEntry))

    def createBswImplementation(self, short_name: str) -> BswImplementation:

        if not self.IsReferrableElementExists(short_name, BswImplementation):
            impl = BswImplementation(self, short_name)
            self.addReferrableElement(impl)
        return cast(BswImplementation, self.getReferrableElement(short_name, BswImplementation))

    def createSwcImplementation(self, short_name: str) -> SwcImplementation:

        if not self.IsReferrableElementExists(short_name, SwcImplementation):
            impl = SwcImplementation(self, short_name)
            self.addReferrableElement(impl)
        return cast(SwcImplementation, self.getReferrableElement(short_name, SwcImplementation))

    def createSwcBswMapping(self, short_name: str) -> SwcBswMapping:

        if not self.IsReferrableElementExists(short_name, SwcBswMapping):
            mapping = SwcBswMapping(self, short_name)
            self.addReferrableElement(mapping)
        return cast(SwcBswMapping, self.getReferrableElement(short_name, SwcBswMapping))

    def createBswEntryRelationshipSet(self, short_name: str) -> BswEntryRelationshipSet:

        if not self.IsReferrableElementExists(short_name, BswEntryRelationshipSet):
            entry_set = BswEntryRelationshipSet(self, short_name)
            self.addReferrableElement(entry_set)
        return cast(BswEntryRelationshipSet, self.getReferrableElement(short_name, BswEntryRelationshipSet))

    def createFirewallRule(self, short_name: str) -> FirewallRule:
        """
        Creates a FirewallRule element in this package.
        If a rule with the given short name already exists, it is returned instead.

        Args:
            short_name: The unique short name of the rule

        Returns:
            The created (or existing) FirewallRule
        """

        if not self.IsReferrableElementExists(short_name, FirewallRule):
            rule = FirewallRule(self, short_name)
            self.addReferrableElement(rule)
        return cast(FirewallRule, self.getReferrableElement(short_name, FirewallRule))

    def createBlueprintMappingSet(self, short_name: str) -> BlueprintMappingSet:
        """
        Creates a BlueprintMappingSet element in this package.
        If a set with the given short name already exists, it is returned instead.

        Args:
            short_name: The unique short name of the set

        Returns:
            The created (or existing) BlueprintMappingSet
        """

        if not self.IsReferrableElementExists(short_name, BlueprintMappingSet):
            blueprint_mapping_set = BlueprintMappingSet(self, short_name)
            self.addReferrableElement(blueprint_mapping_set)
        return cast(BlueprintMappingSet, self.getReferrableElement(short_name, BlueprintMappingSet))

    def getBlueprintMappingSets(self) -> List[BlueprintMappingSet]:
        """
        This represents a container of mappings between "actual" model elements and the "blueprint" that has been taken for their creation.
        """
        return list(a for a in self.referrableElements if isinstance(a, BlueprintMappingSet))

    def createConstantSpecificationMappingSet(self, short_name: str) -> ConstantSpecificationMappingSet:
        """
        Creates a ConstantSpecificationMappingSet element in this package.
        If a set with the given short name already exists, it is returned instead.

        Args:
            short_name: The unique short name of the set

        Returns:
            The created (or existing) ConstantSpecificationMappingSet
        """

        if not self.IsReferrableElementExists(short_name, ConstantSpecificationMappingSet):
            constant_specification_mapping_set = ConstantSpecificationMappingSet(self, short_name)
            self.addReferrableElement(constant_specification_mapping_set)
        return cast(ConstantSpecificationMappingSet, self.getReferrableElement(short_name, ConstantSpecificationMappingSet))

    def getConstantSpecificationMappingSets(self) -> List[ConstantSpecificationMappingSet]:
        """
        This meta-class represents the ability to map two ConstantSpecifications to each others. One Constant Specification is supposed to be described in the application domain and the other should be described in the implementation domain.
        """
        return list(a for a in self.referrableElements if isinstance(a, ConstantSpecificationMappingSet))

    def createStateDependentFirewall(self, short_name: str) -> StateDependentFirewall:
        """
        Creates a StateDependentFirewall element in this package.
        If a firewall with the given short name already exists, it is returned instead.

        Args:
            short_name: The unique short name of the firewall

        Returns:
            The created (or existing) StateDependentFirewall
        """

        if not self.IsReferrableElementExists(short_name, StateDependentFirewall):
            firewall = StateDependentFirewall(self, short_name)
            self.addReferrableElement(firewall)
        return cast(StateDependentFirewall, self.getReferrableElement(short_name, StateDependentFirewall))

    def createPlatformModuleEthernetEndpointConfiguration(self, short_name: str) -> PlatformModuleEthernetEndpointConfiguration:
        """
        Creates a PlatformModuleEthernetEndpointConfiguration element in this package.
        If a configuration with the given short name already exists, it is returned instead.

        Args:
            short_name: The unique short name of the configuration

        Returns:
            The created (or existing) PlatformModuleEthernetEndpointConfiguration
        """

        if not self.IsReferrableElementExists(short_name, PlatformModuleEthernetEndpointConfiguration):
            configuration = PlatformModuleEthernetEndpointConfiguration(self, short_name)
            self.addReferrableElement(configuration)
        return cast(PlatformModuleEthernetEndpointConfiguration, self.getReferrableElement(short_name, PlatformModuleEthernetEndpointConfiguration))

    def createMcFunction(self, short_name: str) -> McFunction:
        """
        Creates an McFunction element in this package.
        If a function with the given short name already exists, it is returned instead.

        Args:
            short_name: The unique short name of the function

        Returns:
            The created (or existing) McFunction
        """

        if not self.IsReferrableElementExists(short_name, McFunction):
            func = McFunction(self, short_name)
            self.addReferrableElement(func)
        return cast(McFunction, self.getReferrableElement(short_name, McFunction))

    def createMcGroup(self, short_name: str) -> McGroup:
        """
        Creates an McGroup element in this package.
        If a group with the given short name already exists, it is returned instead.

        Args:
            short_name: The unique short name of the group

        Returns:
            The created (or existing) McGroup
        """

        if not self.IsReferrableElementExists(short_name, McGroup):
            group = McGroup(self, short_name)
            self.addReferrableElement(group)
        return cast(McGroup, self.getReferrableElement(short_name, McGroup))

    def createConstantSpecification(self, short_name: str) -> ConstantSpecification:

        if not self.IsReferrableElementExists(short_name, ConstantSpecification):
            spec = ConstantSpecification(self, short_name)
            self.addReferrableElement(spec)
        return cast(ConstantSpecification, self.getReferrableElement(short_name, ConstantSpecification))

    def createCryptoEllipticCurveProps(self, short_name: str) -> CryptoEllipticCurveProps:

        if not self.IsReferrableElementExists(short_name, CryptoEllipticCurveProps):
            props = CryptoEllipticCurveProps(self, short_name)
            self.addReferrableElement(props)
        return cast(CryptoEllipticCurveProps, self.getReferrableElement(short_name, CryptoEllipticCurveProps))

    def createCryptoSignatureScheme(self, short_name: str) -> CryptoSignatureScheme:

        if not self.IsReferrableElementExists(short_name, CryptoSignatureScheme):
            scheme = CryptoSignatureScheme(self, short_name)
            self.addReferrableElement(scheme)
        return cast(CryptoSignatureScheme, self.getReferrableElement(short_name, CryptoSignatureScheme))

    def createCryptoServiceCertificate(self, short_name: str) -> CryptoServiceCertificate:

        if not self.IsReferrableElementExists(short_name, CryptoServiceCertificate):
            certificate = CryptoServiceCertificate(self, short_name)
            self.addReferrableElement(certificate)
        return cast(CryptoServiceCertificate, self.getReferrableElement(short_name, CryptoServiceCertificate))

    def createIPSecConfigProps(self, short_name: str) -> IPSecConfigProps:

        if not self.IsReferrableElementExists(short_name, IPSecConfigProps):
            props = IPSecConfigProps(self, short_name)
            self.addReferrableElement(props)
        return cast(IPSecConfigProps, self.getReferrableElement(short_name, IPSecConfigProps))

    def createCryptoServicePrimitive(self, short_name: str) -> CryptoServicePrimitive:

        if not self.IsReferrableElementExists(short_name, CryptoServicePrimitive):
            primitive = CryptoServicePrimitive(self, short_name)
            self.addReferrableElement(primitive)
        return cast(CryptoServicePrimitive, self.getReferrableElement(short_name, CryptoServicePrimitive))

    def createDataConstr(self, short_name: str) -> DataConstr:

        if not self.IsReferrableElementExists(short_name, DataConstr):
            constr = DataConstr(self, short_name)
            self.addReferrableElement(constr)
        return cast(DataConstr, self.getReferrableElement(short_name, DataConstr))

    def createUnit(self, short_name: str) -> Unit:

        if not self.IsReferrableElementExists(short_name, Unit):
            unit = Unit(self, short_name)
            self.addReferrableElement(unit)
        return cast(Unit, self.getReferrableElement(short_name, Unit))

    def createUnitGroup(self, short_name: str) -> UnitGroup:

        if not self.IsReferrableElementExists(short_name, UnitGroup):
            unit_group = UnitGroup(self, short_name)
            self.addReferrableElement(unit_group)
        return cast(UnitGroup, self.getReferrableElement(short_name, UnitGroup))

    def createEndToEndProtectionSet(self, short_name: str) -> EndToEndProtectionSet:

        if not self.IsReferrableElementExists(short_name, EndToEndProtectionSet):
            e2d_set = EndToEndProtectionSet(self, short_name)
            self.addReferrableElement(e2d_set)
        return cast(EndToEndProtectionSet, self.getReferrableElement(short_name, EndToEndProtectionSet))

    def createApplicationArrayDataType(self, short_name: str) -> ApplicationArrayDataType:

        if not self.IsReferrableElementExists(short_name, ApplicationArrayDataType):
            data_type = ApplicationArrayDataType(self, short_name)
            self.addReferrableElement(data_type)
        return cast(ApplicationArrayDataType, self.getReferrableElement(short_name, ApplicationArrayDataType))

    def createSwRecordLayout(self, short_name: str) -> SwRecordLayout:

        if not self.IsReferrableElementExists(short_name, SwRecordLayout):
            layout = SwRecordLayout(self, short_name)
            self.addReferrableElement(layout)
        return cast(SwRecordLayout, self.getReferrableElement(short_name, SwRecordLayout))

    def createSwAddrMethod(self, short_name: str) -> SwAddrMethod:

        if not self.IsReferrableElementExists(short_name, SwAddrMethod):
            method = SwAddrMethod(self, short_name)
            self.addReferrableElement(method)
        return cast(SwAddrMethod, self.getReferrableElement(short_name, SwAddrMethod))

    def createTriggerInterface(self, short_name: str) -> TriggerInterface:

        if not self.IsReferrableElementExists(short_name, TriggerInterface):
            trigger_interface = TriggerInterface(self, short_name)
            self.addReferrableElement(trigger_interface)
        return cast(TriggerInterface, self.getReferrableElement(short_name, TriggerInterface))

    def createDataPrototypeGroup(self, short_name: str) -> DataPrototypeGroup:

        if not self.IsReferrableElementExists(short_name, DataPrototypeGroup):
            data_group = DataPrototypeGroup(self, short_name)
            self.addReferrableElement(data_group)
        return cast(DataPrototypeGroup, self.getReferrableElement(short_name, DataPrototypeGroup))

    def createRunnableEntityGroup(self, short_name: str) -> RunnableEntityGroup:

        if not self.IsReferrableElementExists(short_name, RunnableEntityGroup):
            runnable_group = RunnableEntityGroup(self, short_name)
            self.addReferrableElement(runnable_group)
        return cast(RunnableEntityGroup, self.getReferrableElement(short_name, RunnableEntityGroup))

    def createConsistencyNeeds(self, short_name: str) -> ConsistencyNeeds:

        if not self.IsReferrableElementExists(short_name, ConsistencyNeeds):
            consistency_needs = ConsistencyNeeds(self, short_name)
            self.addReferrableElement(consistency_needs)
        return cast(ConsistencyNeeds, self.getReferrableElement(short_name, ConsistencyNeeds))

    def createModeDeclarationGroup(self, short_name: str) -> ModeDeclarationGroup:

        if not self.IsReferrableElementExists(short_name, ModeDeclarationGroup):
            group = ModeDeclarationGroup(self, short_name)
            self.addReferrableElement(group)
        return cast(ModeDeclarationGroup, self.getReferrableElement(short_name, ModeDeclarationGroup))

    def createModeSwitchInterface(self, short_name: str) -> ModeSwitchInterface:

        if not self.IsReferrableElementExists(short_name, ModeSwitchInterface):
            switch_interface = ModeSwitchInterface(self, short_name)
            self.addReferrableElement(switch_interface)
        return cast(ModeSwitchInterface, self.getReferrableElement(short_name, ModeSwitchInterface))

    def createSwcTiming(self, short_name: str) -> SwcTiming:

        if not self.IsReferrableElementExists(short_name, SwcTiming):
            timing = SwcTiming(self, short_name)
            self.addReferrableElement(timing)
        return cast(SwcTiming, self.getReferrableElement(short_name, SwcTiming))

    def createVfbTiming(self, short_name: str) -> VfbTiming:

        if not self.IsReferrableElementExists(short_name, VfbTiming):
            timing = VfbTiming(self, short_name)
            self.addReferrableElement(timing)
        return cast(VfbTiming, self.getReferrableElement(short_name, VfbTiming))

    def createSystemTiming(self, short_name: str) -> SystemTiming:

        if not self.IsReferrableElementExists(short_name, SystemTiming):
            timing = SystemTiming(self, short_name)
            self.addReferrableElement(timing)
        return cast(SystemTiming, self.getReferrableElement(short_name, SystemTiming))

    def createBswModuleTiming(self, short_name: str) -> BswModuleTiming:

        if not self.IsReferrableElementExists(short_name, BswModuleTiming):
            timing = BswModuleTiming(self, short_name)
            self.addReferrableElement(timing)
        return cast(BswModuleTiming, self.getReferrableElement(short_name, BswModuleTiming))

    def createBswCompositionTiming(self, short_name: str) -> BswCompositionTiming:

        if not self.IsReferrableElementExists(short_name, BswCompositionTiming):
            timing = BswCompositionTiming(self, short_name)
            self.addReferrableElement(timing)
        return cast(BswCompositionTiming, self.getReferrableElement(short_name, BswCompositionTiming))

    def createEcuTiming(self, short_name: str) -> EcuTiming:

        if not self.IsReferrableElementExists(short_name, EcuTiming):
            timing = EcuTiming(self, short_name)
            self.addReferrableElement(timing)
        return cast(EcuTiming, self.getReferrableElement(short_name, EcuTiming))

    def createTDCpSoftwareClusterMappingSet(self, short_name: str) -> TDCpSoftwareClusterMappingSet:

        if not self.IsReferrableElementExists(short_name, TDCpSoftwareClusterMappingSet):
            mapping_set = TDCpSoftwareClusterMappingSet(self, short_name)
            self.addReferrableElement(mapping_set)
        return cast(TDCpSoftwareClusterMappingSet, self.getReferrableElement(short_name, TDCpSoftwareClusterMappingSet))

    def createLinCluster(self, short_name: str) -> LinCluster:

        if not self.IsReferrableElementExists(short_name, LinCluster):
            cluster = LinCluster(self, short_name)
            self.addReferrableElement(cluster)
        return cast(LinCluster, self.getReferrableElement(short_name, LinCluster))

    def createCanCluster(self, short_name: str) -> CanCluster:

        if not self.IsReferrableElementExists(short_name, CanCluster):
            cluster = CanCluster(self, short_name)
            self.addReferrableElement(cluster)
        return cast(CanCluster, self.getReferrableElement(short_name, CanCluster))

    def createJ1939Cluster(self, short_name: str) -> J1939Cluster:

        if not self.IsReferrableElementExists(short_name, J1939Cluster):
            cluster = J1939Cluster(self, short_name)
            self.addReferrableElement(cluster)
        return cast(J1939Cluster, self.getReferrableElement(short_name, J1939Cluster))

    def createJ1939ControllerApplication(self, short_name: str) -> J1939ControllerApplication:

        if not self.IsReferrableElementExists(short_name, J1939ControllerApplication):
            controller_application = J1939ControllerApplication(self, short_name)
            self.addReferrableElement(controller_application)
        return cast(J1939ControllerApplication, self.getReferrableElement(short_name, J1939ControllerApplication))

    def createTtcanCluster(self, short_name: str) -> TtcanCluster:

        if not self.IsReferrableElementExists(short_name, TtcanCluster):
            cluster = TtcanCluster(self, short_name)
            self.addReferrableElement(cluster)
        return cast(TtcanCluster, self.getReferrableElement(short_name, TtcanCluster))

    def createUserDefinedCluster(self, short_name: str) -> UserDefinedCluster:

        if not self.IsReferrableElementExists(short_name, UserDefinedCluster):
            cluster = UserDefinedCluster(self, short_name)
            self.addReferrableElement(cluster)
        return cast(UserDefinedCluster, self.getReferrableElement(short_name, UserDefinedCluster))

    def createLinUnconditionalFrame(self, short_name: str) -> LinUnconditionalFrame:

        if not self.IsReferrableElementExists(short_name, LinUnconditionalFrame):
            frame = LinUnconditionalFrame(self, short_name)
            self.addReferrableElement(frame)
        return cast(LinUnconditionalFrame, self.getReferrableElement(short_name, LinUnconditionalFrame))

    def createNmPdu(self, short_name: str) -> NmPdu:

        if not self.IsReferrableElementExists(short_name, NmPdu):
            element = NmPdu(self, short_name)
            self.addReferrableElement(element)
        return cast(NmPdu, self.getReferrableElement(short_name, NmPdu))

    def createNPdu(self, short_name: str) -> NPdu:

        if not self.IsReferrableElementExists(short_name, NPdu):
            element = NPdu(self, short_name)
            self.addReferrableElement(element)
        return cast(NPdu, self.getReferrableElement(short_name, NPdu))

    def createDcmIPdu(self, short_name: str) -> DcmIPdu:

        if not self.IsReferrableElementExists(short_name, DcmIPdu):
            element = DcmIPdu(self, short_name)
            self.addReferrableElement(element)
        return cast(DcmIPdu, self.getReferrableElement(short_name, DcmIPdu))

    def createJ1939DcmIPdu(self, short_name: str) -> J1939DcmIPdu:

        if not self.IsReferrableElementExists(short_name, J1939DcmIPdu):
            element = J1939DcmIPdu(self, short_name)
            self.addReferrableElement(element)
        return cast(J1939DcmIPdu, self.getReferrableElement(short_name, J1939DcmIPdu))

    def createSecuredIPdu(self, short_name: str) -> SecuredIPdu:

        if not self.IsReferrableElementExists(short_name, SecuredIPdu):
            element = SecuredIPdu(self, short_name)
            self.addReferrableElement(element)
        return cast(SecuredIPdu, self.getReferrableElement(short_name, SecuredIPdu))

    def createContainerIPdu(self, short_name: str) -> ContainerIPdu:

        if not self.IsReferrableElementExists(short_name, ContainerIPdu):
            element = ContainerIPdu(self, short_name)
            self.addReferrableElement(element)
        return cast(ContainerIPdu, self.getReferrableElement(short_name, ContainerIPdu))

    def createNmConfig(self, short_name: str) -> NmConfig:

        if not self.IsReferrableElementExists(short_name, NmConfig):
            element = NmConfig(self, short_name)
            self.addReferrableElement(element)
        return cast(NmConfig, self.getReferrableElement(short_name, NmConfig))

    def createCanTpConfig(self, short_name: str) -> CanTpConfig:

        if not self.IsReferrableElementExists(short_name, CanTpConfig):
            element = CanTpConfig(self, short_name)
            self.addReferrableElement(element)
        return cast(CanTpConfig, self.getReferrableElement(short_name, CanTpConfig))

    def createLinTpConfig(self, short_name: str) -> LinTpConfig:

        if not self.IsReferrableElementExists(short_name, LinTpConfig):
            element = LinTpConfig(self, short_name)
            self.addReferrableElement(element)
        return cast(LinTpConfig, self.getReferrableElement(short_name, LinTpConfig))

    def createFlexrayTpConfig(self, short_name: str) -> FlexrayTpConfig:

        if not self.IsReferrableElementExists(short_name, FlexrayTpConfig):
            element = FlexrayTpConfig(self, short_name)
            self.addReferrableElement(element)
        return cast(FlexrayTpConfig, self.getReferrableElement(short_name, FlexrayTpConfig))

    def createFlexrayArTpConfig(self, short_name: str) -> FlexrayArTpConfig:

        if not self.IsReferrableElementExists(short_name, FlexrayArTpConfig):
            element = FlexrayArTpConfig(self, short_name)
            self.addReferrableElement(element)
        return cast(FlexrayArTpConfig, self.getReferrableElement(short_name, FlexrayArTpConfig))

    def createEthTpConfig(self, short_name: str) -> EthTpConfig:

        if not self.IsReferrableElementExists(short_name, EthTpConfig):
            element = EthTpConfig(self, short_name)
            self.addReferrableElement(element)
        return cast(EthTpConfig, self.getReferrableElement(short_name, EthTpConfig))

    def createSomeipTpConfig(self, short_name: str) -> SomeipTpConfig:

        if not self.IsReferrableElementExists(short_name, SomeipTpConfig):
            element = SomeipTpConfig(self, short_name)
            self.addReferrableElement(element)
        return cast(SomeipTpConfig, self.getReferrableElement(short_name, SomeipTpConfig))

    def createIEEE1722TpConfig(self, short_name: str) -> IEEE1722TpConfig:

        if not self.IsReferrableElementExists(short_name, IEEE1722TpConfig):
            element = IEEE1722TpConfig(self, short_name)
            self.addReferrableElement(element)
        return cast(IEEE1722TpConfig, self.getReferrableElement(short_name, IEEE1722TpConfig))

    def createIEEE1722TpCrfConnection(self, short_name: str) -> IEEE1722TpCrfConnection:

        if not self.IsReferrableElementExists(short_name, IEEE1722TpCrfConnection):
            element = IEEE1722TpCrfConnection(self, short_name)
            self.addReferrableElement(element)
        return cast(IEEE1722TpCrfConnection, self.getReferrableElement(short_name, IEEE1722TpCrfConnection))

    def createCanFrame(self, short_name: str) -> CanFrame:
        """
        Creates a new CAN Frame with the given short name,
        or returns an existing one if it already exists in this package.

        CanFrame represents a CAN communication frame in AUTOSAR's
        communication modeling, used for defining CAN-based communication.

        Args:
            short_name: The short name for the new CanFrame

        Returns:
            The newly created or existing CanFrame instance
        """

        if not self.IsReferrableElementExists(short_name, CanFrame):
            element = CanFrame(self, short_name)
            self.addReferrableElement(element)
        return cast(CanFrame, self.getReferrableElement(short_name, CanFrame))

    def createEcuInstance(self, short_name: str) -> EcuInstance:
        """
        Creates a new ECU Instance with the given short name,
        or returns an existing one if it already exists in this package.

        EcuInstance represents an Electronic Control Unit in AUTOSAR's
        system modeling, containing information about the hardware and
        software configuration of the ECU.

        Args:
            short_name: The short name for the new EcuInstance

        Returns:
            The newly created or existing EcuInstance instance
        """

        if not self.IsReferrableElementExists(short_name, EcuInstance):
            element = EcuInstance(self, short_name)
            self.addReferrableElement(element)
        return cast(EcuInstance, self.getReferrableElement(short_name, EcuInstance))

    def createConsumedProvidedServiceInstanceGroup(self, short_name: str) -> ConsumedProvidedServiceInstanceGroup:
        """
        Creates a new ConsumedProvidedServiceInstanceGroup with the given short name,
        or returns an existing one if it already exists in this package.

        A ConsumedProvidedServiceInstanceGroup encloses ConsumedServiceInstances and
        ProvidedServiceInstances that the AUTOSAR ServiceDiscovery starts and stops
        together at runtime.

        Args:
            short_name: The short name for the new ConsumedProvidedServiceInstanceGroup

        Returns:
            The newly created or existing ConsumedProvidedServiceInstanceGroup instance
        """

        if not self.IsReferrableElementExists(short_name, ConsumedProvidedServiceInstanceGroup):
            element = ConsumedProvidedServiceInstanceGroup(self, short_name)
            self.addReferrableElement(element)
        return cast(ConsumedProvidedServiceInstanceGroup, self.getReferrableElement(short_name, ConsumedProvidedServiceInstanceGroup))

    def createGateway(self, short_name: str) -> Gateway:

        if not self.IsReferrableElementExists(short_name, Gateway):
            element = Gateway(self, short_name)
            self.addReferrableElement(element)
        return cast(Gateway, self.getReferrableElement(short_name, Gateway))

    def createISignal(self, short_name: str) -> ISignal:

        if not self.IsReferrableElementExists(short_name, ISignal):
            element = ISignal(self, short_name)
            self.addReferrableElement(element)
        return cast(ISignal, self.getReferrableElement(short_name, ISignal))

    def createSystemSignal(self, short_name: str) -> SystemSignal:
        """
        Creates a new System Signal with the given short name,
        or returns an existing one if it already exists in this package.

        SystemSignal represents signals at the system level in AUTOSAR,
        typically used for communication between ECUs or for external
        interfaces.

        Args:
            short_name: The short name for the new SystemSignal

        Returns:
            The newly created or existing SystemSignal instance
        """

        if not self.IsReferrableElementExists(short_name, SystemSignal):
            element = SystemSignal(self, short_name)
            self.addReferrableElement(element)
        return cast(SystemSignal, self.getReferrableElement(short_name, SystemSignal))

    def createSystemSignalGroup(self, short_name: str) -> SystemSignalGroup:

        if not self.IsReferrableElementExists(short_name, SystemSignalGroup):
            element = SystemSignalGroup(self, short_name)
            self.addReferrableElement(element)
        return cast(SystemSignalGroup, self.getReferrableElement(short_name, SystemSignalGroup))

    def createSignalServiceTranslationPropsSet(self, short_name: str) -> SignalServiceTranslationPropsSet:

        if not self.IsReferrableElementExists(short_name, SignalServiceTranslationPropsSet):
            element = SignalServiceTranslationPropsSet(self, short_name)
            self.addReferrableElement(element)
        return cast(SignalServiceTranslationPropsSet, self.getReferrableElement(short_name, SignalServiceTranslationPropsSet))

    def createISignalIPdu(self, short_name: str) -> ISignalIPdu:

        if not self.IsReferrableElementExists(short_name, ISignalIPdu):
            element = ISignalIPdu(self, short_name)
            self.addReferrableElement(element)
        return cast(ISignalIPdu, self.getReferrableElement(short_name, ISignalIPdu))

    def createEcucValueCollection(self, short_name: str) -> EcucValueCollection:

        if not self.IsReferrableElementExists(short_name, EcucValueCollection):
            element = EcucValueCollection(self, short_name)
            self.addReferrableElement(element)
        return cast(EcucValueCollection, self.getReferrableElement(short_name, EcucValueCollection))

    def createEthIpProps(self, short_name: str) -> EthIpProps:

        if not self.IsReferrableElementExists(short_name, EthIpProps):
            props = EthIpProps(self, short_name)
            self.addReferrableElement(props)
        return cast(EthIpProps, self.getReferrableElement(short_name, EthIpProps))

    def createEthTcpIpProps(self, short_name: str) -> EthTcpIpProps:

        if not self.IsReferrableElementExists(short_name, EthTcpIpProps):
            props = EthTcpIpProps(self, short_name)
            self.addReferrableElement(props)
        return cast(EthTcpIpProps, self.getReferrableElement(short_name, EthTcpIpProps))

    def createEthTcpIpIcmpProps(self, short_name: str) -> EthTcpIpIcmpProps:

        if not self.IsReferrableElementExists(short_name, EthTcpIpIcmpProps):
            props = EthTcpIpIcmpProps(self, short_name)
            self.addReferrableElement(props)
        return cast(EthTcpIpIcmpProps, self.getReferrableElement(short_name, EthTcpIpIcmpProps))

    def createOsTaskProxy(self, short_name: str) -> OsTaskProxy:

        if not self.IsReferrableElementExists(short_name, OsTaskProxy):
            proxy = OsTaskProxy(self, short_name)
            self.addReferrableElement(proxy)
        return cast(OsTaskProxy, self.getReferrableElement(short_name, OsTaskProxy))

    def createModuleConfiguration(self, short_name: str) -> ModuleConfiguration:

        if not self.IsReferrableElementExists(short_name, ModuleConfiguration):
            module_configuration = ModuleConfiguration(self, short_name)
            self.addReferrableElement(module_configuration)
        return cast(ModuleConfiguration, self.getReferrableElement(short_name, ModuleConfiguration))

    def createEcucModuleConfigurationValues(self, short_name: str) -> EcucModuleConfigurationValues:

        if not self.IsReferrableElementExists(short_name, EcucModuleConfigurationValues):
            element = EcucModuleConfigurationValues(self, short_name)
            self.addReferrableElement(element)
        return cast(EcucModuleConfigurationValues, self.getReferrableElement(short_name, EcucModuleConfigurationValues))

    def createEcucModuleDef(self, short_name: str) -> EcucModuleDef:

        if not self.IsReferrableElementExists(short_name, EcucModuleDef):
            element = EcucModuleDef(self, short_name)
            self.addReferrableElement(element)
        return cast(EcucModuleDef, self.getReferrableElement(short_name, EcucModuleDef))

    def createEcucDefinitionCollection(self, short_name: str) -> EcucDefinitionCollection:

        if not self.IsReferrableElementExists(short_name, EcucDefinitionCollection):
            element = EcucDefinitionCollection(self, short_name)
            self.addReferrableElement(element)
        return cast(EcucDefinitionCollection, self.getReferrableElement(short_name, EcucDefinitionCollection))

    def createEcucDestinationUriDefSet(self, short_name: str) -> EcucDestinationUriDefSet:

        if not self.IsReferrableElementExists(short_name, EcucDestinationUriDefSet):
            element = EcucDestinationUriDefSet(self, short_name)
            self.addReferrableElement(element)
        return cast(EcucDestinationUriDefSet, self.getReferrableElement(short_name, EcucDestinationUriDefSet))

    def createSwSystemConst(self, short_name: str) -> SwSystemconst:

        if not self.IsReferrableElementExists(short_name, SwSystemconst):
            element = SwSystemconst(self, short_name)
            self.addReferrableElement(element)
        return cast(SwSystemconst, self.getReferrableElement(short_name, SwSystemconst))

    def createSwSystemconstantValueSet(self, short_name: str) -> SwSystemconstantValueSet:

        if not self.IsReferrableElementExists(short_name, SwSystemconstantValueSet):
            element = SwSystemconstantValueSet(self, short_name)
            self.addReferrableElement(element)
        return cast(SwSystemconstantValueSet, self.getReferrableElement(short_name, SwSystemconstantValueSet))

    def createEvaluatedVariantSet(self, short_name: str) -> EvaluatedVariantSet:

        if not self.IsReferrableElementExists(short_name, EvaluatedVariantSet):
            element = EvaluatedVariantSet(self, short_name)
            self.addReferrableElement(element)
        return cast(EvaluatedVariantSet, self.getReferrableElement(short_name, EvaluatedVariantSet))

    def createSdgDef(self, short_name: str) -> SdgDef:

        if not self.IsReferrableElementExists(short_name, SdgDef):
            element = SdgDef(self, short_name)
            self.addReferrableElement(element)
        return cast(SdgDef, self.getReferrableElement(short_name, SdgDef))

    def createPredefinedVariant(self, short_name: str) -> PredefinedVariant:

        if not self.IsReferrableElementExists(short_name, PredefinedVariant):
            element = PredefinedVariant(self, short_name)
            self.addReferrableElement(element)
        return cast(PredefinedVariant, self.getReferrableElement(short_name, PredefinedVariant))

    def createPostBuildVariantCriterion(self, short_name: str) -> PostBuildVariantCriterion:

        if not self.IsReferrableElementExists(short_name, PostBuildVariantCriterion):
            element = PostBuildVariantCriterion(self, short_name)
            self.addReferrableElement(element)
        return cast(PostBuildVariantCriterion, self.getReferrableElement(short_name, PostBuildVariantCriterion))

    def createPhysicalDimension(self, short_name: str) -> PhysicalDimension:

        if not self.IsReferrableElementExists(short_name, PhysicalDimension):
            element = PhysicalDimension(self, short_name)
            self.addReferrableElement(element)
        return cast(PhysicalDimension, self.getReferrableElement(short_name, PhysicalDimension))

    def createPhysicalDimensionMappingSet(self, short_name: str) -> PhysicalDimensionMappingSet:

        if not self.IsReferrableElementExists(short_name, PhysicalDimensionMappingSet):
            element = PhysicalDimensionMappingSet(self, short_name)
            self.addReferrableElement(element)
        return cast(PhysicalDimensionMappingSet, self.getReferrableElement(short_name, PhysicalDimensionMappingSet))

    def createCalibrationParameterValueSet(self, short_name: str) -> CalibrationParameterValueSet:

        if not self.IsReferrableElementExists(short_name, CalibrationParameterValueSet):
            element = CalibrationParameterValueSet(self, short_name)
            self.addReferrableElement(element)
        return cast(CalibrationParameterValueSet, self.getReferrableElement(short_name, CalibrationParameterValueSet))

    def createISignalGroup(self, short_name: str) -> ISignalGroup:

        if not self.IsReferrableElementExists(short_name, ISignalGroup):
            element = ISignalGroup(self, short_name)
            self.addReferrableElement(element)
        return cast(ISignalGroup, self.getReferrableElement(short_name, ISignalGroup))

    def createISignalIPduGroup(self, short_name: str) -> ISignalIPduGroup:

        if not self.IsReferrableElementExists(short_name, ISignalIPduGroup):
            element = ISignalIPduGroup(self, short_name)
            self.addReferrableElement(element)
        return cast(ISignalIPduGroup, self.getReferrableElement(short_name, ISignalIPduGroup))

    def createPdurIPduGroup(self, short_name: str) -> PdurIPduGroup:

        if not self.IsReferrableElementExists(short_name, PdurIPduGroup):
            element = PdurIPduGroup(self, short_name)
            self.addReferrableElement(element)
        return cast(PdurIPduGroup, self.getReferrableElement(short_name, PdurIPduGroup))

    def createClientIdDefinitionSet(self, short_name: str) -> ClientIdDefinitionSet:

        if not self.IsReferrableElementExists(short_name, ClientIdDefinitionSet):
            element = ClientIdDefinitionSet(self, short_name)
            self.addReferrableElement(element)
        return cast(ClientIdDefinitionSet, self.getReferrableElement(short_name, ClientIdDefinitionSet))

    def createInterpolationRoutineMappingSet(self, short_name: str) -> InterpolationRoutineMappingSet:

        if not self.IsReferrableElementExists(short_name, InterpolationRoutineMappingSet):
            element = InterpolationRoutineMappingSet(self, short_name)
            self.addReferrableElement(element)
        return cast(InterpolationRoutineMappingSet, self.getReferrableElement(short_name, InterpolationRoutineMappingSet))

    def createCpSoftwareCluster(self, short_name: str) -> CpSoftwareCluster:

        if not self.IsReferrableElementExists(short_name, CpSoftwareCluster):
            element = CpSoftwareCluster(self, short_name)
            self.addReferrableElement(element)
        return cast(CpSoftwareCluster, self.getReferrableElement(short_name, CpSoftwareCluster))

    def createCpSoftwareClusterMappingSet(self, short_name: str) -> CpSoftwareClusterMappingSet:

        if not self.IsReferrableElementExists(short_name, CpSoftwareClusterMappingSet):
            element = CpSoftwareClusterMappingSet(self, short_name)
            self.addReferrableElement(element)
        return cast(CpSoftwareClusterMappingSet, self.getReferrableElement(short_name, CpSoftwareClusterMappingSet))

    def createSystem(self, short_name: str) -> System:

        if not self.IsReferrableElementExists(short_name, System):
            element = System(self, short_name)
            self.addReferrableElement(element)
        return cast(System, self.getReferrableElement(short_name, System))

    def createFlatMap(self, short_name: str) -> FlatMap:

        if not self.IsReferrableElementExists(short_name, FlatMap):
            map = FlatMap(self, short_name)
            self.addReferrableElement(map)
        return cast(FlatMap, self.getReferrableElement(short_name, FlatMap))

    def createBuildActionManifest(self, short_name: str) -> BuildActionManifest:
        if not self.IsReferrableElementExists(short_name, BuildActionManifest):
            manifest = BuildActionManifest(self, short_name)
            self.addReferrableElement(manifest)
        return cast(BuildActionManifest, self.getReferrableElement(short_name, BuildActionManifest))

    def createPortInterfaceMappingSet(self, short_name: str) -> PortInterfaceMappingSet:

        if not self.IsReferrableElementExists(short_name, PortInterfaceMappingSet):
            map_set = PortInterfaceMappingSet(self, short_name)
            self.addReferrableElement(map_set)
        return cast(PortInterfaceMappingSet, self.getReferrableElement(short_name, PortInterfaceMappingSet))

    def createEthernetCluster(self, short_name: str) -> EthernetCluster:

        if not self.IsReferrableElementExists(short_name, EthernetCluster):
            cluster = EthernetCluster(self, short_name)
            self.addReferrableElement(cluster)
        return cast(EthernetCluster, self.getReferrableElement(short_name, EthernetCluster))

    def createApplicationPartition(self, short_name: str) -> ApplicationPartition:

        if not self.IsReferrableElementExists(short_name, ApplicationPartition):
            app_partition = ApplicationPartition(self, short_name)
            self.addReferrableElement(app_partition)
        return cast(ApplicationPartition, self.getReferrableElement(short_name, ApplicationPartition))

    def createCouplingElement(self, short_name: str) -> CouplingElement:

        if not self.IsReferrableElementExists(short_name, CouplingElement):
            coupling_element = CouplingElement(self, short_name)
            self.addReferrableElement(coupling_element)
        return cast(CouplingElement, self.getReferrableElement(short_name, CouplingElement))

    def createEthernetWakeupSleepOnDatalineConfigSet(self, short_name: str) -> EthernetWakeupSleepOnDatalineConfigSet:

        if not self.IsReferrableElementExists(short_name, EthernetWakeupSleepOnDatalineConfigSet):
            config_set = EthernetWakeupSleepOnDatalineConfigSet(self, short_name)
            self.addReferrableElement(config_set)
        return cast(EthernetWakeupSleepOnDatalineConfigSet, self.getReferrableElement(short_name, EthernetWakeupSleepOnDatalineConfigSet))

    def createMacSecGlobalKayProps(self, short_name: str) -> MacSecGlobalKayProps:

        if not self.IsReferrableElementExists(short_name, MacSecGlobalKayProps):
            props = MacSecGlobalKayProps(self, short_name)
            self.addReferrableElement(props)
        return cast(MacSecGlobalKayProps, self.getReferrableElement(short_name, MacSecGlobalKayProps))

    def createMacSecParticipantSet(self, short_name: str) -> MacSecParticipantSet:

        if not self.IsReferrableElementExists(short_name, MacSecParticipantSet):
            participant_set = MacSecParticipantSet(self, short_name)
            self.addReferrableElement(participant_set)
        return cast(MacSecParticipantSet, self.getReferrableElement(short_name, MacSecParticipantSet))

    def createDiagnosticAging(self, short_name: str) -> DiagnosticAging:
        """
        Creates a new DiagnosticAging with the given short name,
        or returns an existing one if it already exists in this package.

        DiagnosticAging defines the aging algorithm.

        Args:
            short_name: The short name for the new DiagnosticAging

        Returns:
            The newly created or existing DiagnosticAging instance
        """
        if not self.IsReferrableElementExists(short_name, DiagnosticAging):
            aging = DiagnosticAging(self, short_name)
            self.addReferrableElement(aging)
        return cast(DiagnosticAging, self.getReferrableElement(short_name, DiagnosticAging))

    def createDiagnosticAuthRole(self, short_name: str) -> DiagnosticAuthRole:
        """
        Creates a new DiagnosticAuthRole with the given short name,
        or returns an existing one if it already exists in this package.

        DiagnosticAuthRole represents the ability to specify an authentication
        role that can be used to deliver fine-grained access rights.

        Args:
            short_name: The short name for the new DiagnosticAuthRole

        Returns:
            The newly created or existing DiagnosticAuthRole instance
        """
        if not self.IsReferrableElementExists(short_name, DiagnosticAuthRole):
            auth_role = DiagnosticAuthRole(self, short_name)
            self.addReferrableElement(auth_role)
        return cast(DiagnosticAuthRole, self.getReferrableElement(short_name, DiagnosticAuthRole))

    def createDiagnosticAuthenticationClass(self, short_name: str) -> DiagnosticAuthenticationClass:
        """
        Creates a new DiagnosticAuthenticationClass with the given short name,
        or returns an existing one if it already exists in this package.

        DiagnosticAuthenticationClass contains configuration shared by all
        instances of the Authentication diagnostic service.

        Args:
            short_name: The short name for the new DiagnosticAuthenticationClass

        Returns:
            The newly created or existing DiagnosticAuthenticationClass instance
        """
        if not self.IsReferrableElementExists(short_name, DiagnosticAuthenticationClass):
            authentication_class = DiagnosticAuthenticationClass(self, short_name)
            self.addReferrableElement(authentication_class)
        return cast(DiagnosticAuthenticationClass, self.getReferrableElement(short_name, DiagnosticAuthenticationClass))

    def createDiagnosticAuthenticationConfiguration(self, short_name: str) -> DiagnosticAuthenticationConfiguration:
        """
        Creates a new DiagnosticAuthenticationConfiguration with the given short name,
        or returns an existing one if it already exists in this package.

        DiagnosticAuthenticationConfiguration represents the subfunction to
        configure the authentication.

        Args:
            short_name: The short name for the new DiagnosticAuthenticationConfiguration

        Returns:
            The newly created or existing DiagnosticAuthenticationConfiguration instance
        """
        if not self.IsReferrableElementExists(short_name, DiagnosticAuthenticationConfiguration):
            configuration = DiagnosticAuthenticationConfiguration(self, short_name)
            self.addReferrableElement(configuration)
        return cast(DiagnosticAuthenticationConfiguration, self.getReferrableElement(short_name, DiagnosticAuthenticationConfiguration))

    def createDiagnosticAuthTransmitCertificate(self, short_name: str) -> DiagnosticAuthTransmitCertificate:
        """
        Creates a new DiagnosticAuthTransmitCertificate with the given short name,
        or returns an existing one if it already exists in this package.

        DiagnosticAuthTransmitCertificate represents the sub-function to transmit a certificate.

        Args:
            short_name: The short name for the new DiagnosticAuthTransmitCertificate

        Returns:
            The newly created or existing DiagnosticAuthTransmitCertificate instance
        """
        if not self.IsReferrableElementExists(short_name, DiagnosticAuthTransmitCertificate):
            certificate = DiagnosticAuthTransmitCertificate(self, short_name)
            self.addReferrableElement(certificate)
        return cast(DiagnosticAuthTransmitCertificate, self.getReferrableElement(short_name, DiagnosticAuthTransmitCertificate))

    def createDiagnosticDeAuthentication(self, short_name: str) -> DiagnosticDeAuthentication:
        """
        Creates a new DiagnosticDeAuthentication with the given short name,
        or returns an existing one if it already exists in this package.

        DiagnosticDeAuthentication represents the subfunction to remove the authentication.

        Args:
            short_name: The short name for the new DiagnosticDeAuthentication

        Returns:
            The newly created or existing DiagnosticDeAuthentication instance
        """
        if not self.IsReferrableElementExists(short_name, DiagnosticDeAuthentication):
            de_authentication = DiagnosticDeAuthentication(self, short_name)
            self.addReferrableElement(de_authentication)
        return cast(DiagnosticDeAuthentication, self.getReferrableElement(short_name, DiagnosticDeAuthentication))

    def createDiagnosticProofOfOwnership(self, short_name: str) -> DiagnosticProofOfOwnership:
        """
        Creates a new DiagnosticProofOfOwnership with the given short name,
        or returns an existing one if it already exists in this package.

        DiagnosticProofOfOwnership represents the subfunction to provide proof of ownership.

        Args:
            short_name: The short name for the new DiagnosticProofOfOwnership

        Returns:
            The newly created or existing DiagnosticProofOfOwnership instance
        """
        if not self.IsReferrableElementExists(short_name, DiagnosticProofOfOwnership):
            proof_of_ownership = DiagnosticProofOfOwnership(self, short_name)
            self.addReferrableElement(proof_of_ownership)
        return cast(DiagnosticProofOfOwnership, self.getReferrableElement(short_name, DiagnosticProofOfOwnership))

    def createDiagnosticVerifyCertificateBidirectional(self, short_name: str) -> DiagnosticVerifyCertificateBidirectional:
        """
        Creates a new DiagnosticVerifyCertificateBidirectional with the given short name,
        or returns an existing one if it already exists in this package.

        DiagnosticVerifyCertificateBidirectional represents the subfunction to do
        a bidirectional verification of the certificate.

        Args:
            short_name: The short name for the new DiagnosticVerifyCertificateBidirectional

        Returns:
            The newly created or existing DiagnosticVerifyCertificateBidirectional instance
        """
        if not self.IsReferrableElementExists(short_name, DiagnosticVerifyCertificateBidirectional):
            verification = DiagnosticVerifyCertificateBidirectional(self, short_name)
            self.addReferrableElement(verification)
        return cast(DiagnosticVerifyCertificateBidirectional, self.getReferrableElement(short_name, DiagnosticVerifyCertificateBidirectional))

    def createDiagnosticVerifyCertificateUnidirectional(self, short_name: str) -> DiagnosticVerifyCertificateUnidirectional:
        """
        Creates a new DiagnosticVerifyCertificateUnidirectional with the given short name,
        or returns an existing one if it already exists in this package.

        DiagnosticVerifyCertificateUnidirectional represents the subfunction to do
        a unidirectional verification of the certificate.

        Args:
            short_name: The short name for the new DiagnosticVerifyCertificateUnidirectional

        Returns:
            The newly created or existing DiagnosticVerifyCertificateUnidirectional instance
        """
        if not self.IsReferrableElementExists(short_name, DiagnosticVerifyCertificateUnidirectional):
            verification = DiagnosticVerifyCertificateUnidirectional(self, short_name)
            self.addReferrableElement(verification)
        return cast(DiagnosticVerifyCertificateUnidirectional, self.getReferrableElement(short_name, DiagnosticVerifyCertificateUnidirectional))

    def createDiagnosticComControl(self, short_name: str) -> DiagnosticComControl:
        """
        Creates a new DiagnosticComControl with the given short name,
        or returns an existing one if it already exists in this package.

        DiagnosticComControl represents an instance of the "Communication Control" diagnostic service.

        Args:
            short_name: The short name for the new DiagnosticComControl

        Returns:
            The newly created or existing DiagnosticComControl instance
        """
        if not self.IsReferrableElementExists(short_name, DiagnosticComControl):
            com_control = DiagnosticComControl(self, short_name)
            self.addReferrableElement(com_control)
        return cast(DiagnosticComControl, self.getReferrableElement(short_name, DiagnosticComControl))

    def createDiagnosticConnection(self, short_name: str) -> DiagnosticConnection:

        if not self.IsReferrableElementExists(short_name, DiagnosticConnection):
            connection = DiagnosticConnection(self, short_name)
            self.addReferrableElement(connection)
        return cast(DiagnosticConnection, self.getReferrableElement(short_name, DiagnosticConnection))

    def createDiagnosticContributionSet(self, short_name: str) -> DiagnosticContributionSet:
        """
        Creates a new DiagnosticContributionSet with the given short name,
        or returns an existing one if it already exists in this package.

        DiagnosticContributionSet represents a root node of a diagnostic
        extract that bundles a given set of diagnostic model elements.

        Args:
            short_name: The short name for the new DiagnosticContributionSet

        Returns:
            The newly created or existing DiagnosticContributionSet instance
        """
        if not self.IsReferrableElementExists(short_name, DiagnosticContributionSet):
            contribution_set = DiagnosticContributionSet(self, short_name)
            self.addReferrableElement(contribution_set)
        return cast(DiagnosticContributionSet, self.getReferrableElement(short_name, DiagnosticContributionSet))

    def createDiagnosticCustomServiceClass(self, short_name: str) -> DiagnosticCustomServiceClass:
        """
        Creates a new DiagnosticCustomServiceClass with the given short name,
        or returns an existing one if it already exists in this package.

        DiagnosticCustomServiceClass represents the ability to define a custom
        diagnostic service class and assign an ID to it.

        Args:
            short_name: The short name for the new DiagnosticCustomServiceClass

        Returns:
            The newly created or existing DiagnosticCustomServiceClass instance
        """
        if not self.IsReferrableElementExists(short_name, DiagnosticCustomServiceClass):
            custom_service_class = DiagnosticCustomServiceClass(self, short_name)
            self.addReferrableElement(custom_service_class)
        return cast(DiagnosticCustomServiceClass, self.getReferrableElement(short_name, DiagnosticCustomServiceClass))

    def createDiagnosticCustomServiceInstance(self, short_name: str) -> DiagnosticCustomServiceInstance:
        """
        Creates a new DiagnosticCustomServiceInstance with the given short name,
        or returns an existing one if it already exists in this package.

        DiagnosticCustomServiceInstance represents an instance of a custom
        diagnostic service referring its corresponding DiagnosticCustomServiceClass.

        Args:
            short_name: The short name for the new DiagnosticCustomServiceInstance

        Returns:
            The newly created or existing DiagnosticCustomServiceInstance instance
        """
        if not self.IsReferrableElementExists(short_name, DiagnosticCustomServiceInstance):
            custom_service_instance = DiagnosticCustomServiceInstance(self, short_name)
            self.addReferrableElement(custom_service_instance)
        return cast(DiagnosticCustomServiceInstance, self.getReferrableElement(short_name, DiagnosticCustomServiceInstance))

    def createDiagnosticProtocol(self, short_name: str) -> DiagnosticProtocol:
        """
        Creates a new DiagnosticProtocol with the given short name,
        or returns an existing one if it already exists in this package.

        DiagnosticProtocol represents the ability to define a diagnostic
        protocol.

        Args:
            short_name: The short name for the new DiagnosticProtocol

        Returns:
            The newly created or existing DiagnosticProtocol instance
        """
        if not self.IsReferrableElementExists(short_name, DiagnosticProtocol):
            protocol = DiagnosticProtocol(self, short_name)
            self.addReferrableElement(protocol)
        return cast(DiagnosticProtocol, self.getReferrableElement(short_name, DiagnosticProtocol))

    def createDiagnosticServiceTable(self, short_name: str) -> DiagnosticServiceTable:
        """
        Creates a new Diagnostic Service Table with the given short name,
        or returns an existing one if it already exists in this package.

        DiagnosticServiceTable represents a collection of diagnostic services
        defined in the diagnostic extract template of AUTOSAR, used for
        specifying diagnostic functionality.

        Args:
            short_name: The short name for the new DiagnosticServiceTable

        Returns:
            The newly created or existing DiagnosticServiceTable instance
        """

        if not self.IsReferrableElementExists(short_name, DiagnosticServiceTable):
            table = DiagnosticServiceTable(self, short_name)
            self.addReferrableElement(table)
        return cast(DiagnosticServiceTable, self.getReferrableElement(short_name, DiagnosticServiceTable))

    def createDiagnosticSession(self, short_name: str) -> DiagnosticSession:
        """
        Creates a new DiagnosticSession with the given short name,
        or returns an existing one if it already exists in this package.

        DiagnosticSession represents the ability to define a diagnostic
        session in the diagnostic extract template of AUTOSAR.

        Args:
            short_name: The short name for the new DiagnosticSession

        Returns:
            The newly created or existing DiagnosticSession instance
        """
        if not self.IsReferrableElementExists(short_name, DiagnosticSession):
            session = DiagnosticSession(self, short_name)
            self.addReferrableElement(session)
        return cast(DiagnosticSession, self.getReferrableElement(short_name, DiagnosticSession))

    def createDiagnosticSessionControl(self, short_name: str) -> DiagnosticSessionControl:
        """
        Creates a new DiagnosticSessionControl with the given short name,
        or returns an existing one if it already exists in this package.

        DiagnosticSessionControl represents an instance of the "Session
        Control" diagnostic service.

        Args:
            short_name: The short name for the new DiagnosticSessionControl

        Returns:
            The newly created or existing DiagnosticSessionControl instance
        """
        if not self.IsReferrableElementExists(short_name, DiagnosticSessionControl):
            session_control = DiagnosticSessionControl(self, short_name)
            self.addReferrableElement(session_control)
        return cast(DiagnosticSessionControl, self.getReferrableElement(short_name, DiagnosticSessionControl))

    def createDiagnosticSessionControlClass(self, short_name: str) -> DiagnosticSessionControlClass:
        """
        Creates a new DiagnosticSessionControlClass with the given short name,
        or returns an existing one if it already exists in this package.

        DiagnosticSessionControlClass contains attributes shared by all
        instances of the "Session Control" diagnostic service.

        Args:
            short_name: The short name for the new DiagnosticSessionControlClass

        Returns:
            The newly created or existing DiagnosticSessionControlClass instance
        """
        if not self.IsReferrableElementExists(short_name, DiagnosticSessionControlClass):
            session_control_class = DiagnosticSessionControlClass(self, short_name)
            self.addReferrableElement(session_control_class)
        return cast(DiagnosticSessionControlClass, self.getReferrableElement(short_name, DiagnosticSessionControlClass))

    def createDiagnosticSecurityAccess(self, short_name: str) -> DiagnosticSecurityAccess:
        """
        Creates a new DiagnosticSecurityAccess with the given short name,
        or returns an existing one if it already exists in this package.

        DiagnosticSecurityAccess represents an instance of the "Security
        Access" diagnostic service.

        Args:
            short_name: The short name for the new DiagnosticSecurityAccess

        Returns:
            The newly created or existing DiagnosticSecurityAccess instance
        """
        if not self.IsReferrableElementExists(short_name, DiagnosticSecurityAccess):
            security_access = DiagnosticSecurityAccess(self, short_name)
            self.addReferrableElement(security_access)
        return cast(DiagnosticSecurityAccess, self.getReferrableElement(short_name, DiagnosticSecurityAccess))

    def createDiagnosticSecurityAccessClass(self, short_name: str) -> DiagnosticSecurityAccessClass:
        """
        Creates a new DiagnosticSecurityAccessClass with the given short name,
        or returns an existing one if it already exists in this package.

        DiagnosticSecurityAccessClass contains attributes shared by all
        instances of the "Security Access" diagnostic service.

        Args:
            short_name: The short name for the new DiagnosticSecurityAccessClass

        Returns:
            The newly created or existing DiagnosticSecurityAccessClass instance
        """
        if not self.IsReferrableElementExists(short_name, DiagnosticSecurityAccessClass):
            security_access_class = DiagnosticSecurityAccessClass(self, short_name)
            self.addReferrableElement(security_access_class)
        return cast(DiagnosticSecurityAccessClass, self.getReferrableElement(short_name, DiagnosticSecurityAccessClass))

    def createDiagnosticSecurityLevel(self, short_name: str) -> DiagnosticSecurityLevel:
        """
        Creates a new DiagnosticSecurityLevel with the given short name,
        or returns an existing one if it already exists in this package.

        DiagnosticSecurityLevel represents the ability to define a security
        level considered for diagnostic purposes in the diagnostic extract
        template of AUTOSAR.

        Args:
            short_name: The short name for the new DiagnosticSecurityLevel

        Returns:
            The newly created or existing DiagnosticSecurityLevel instance
        """
        if not self.IsReferrableElementExists(short_name, DiagnosticSecurityLevel):
            security_level = DiagnosticSecurityLevel(self, short_name)
            self.addReferrableElement(security_level)
        return cast(DiagnosticSecurityLevel, self.getReferrableElement(short_name, DiagnosticSecurityLevel))

    def createDiagnosticDataIdentifier(self, short_name: str) -> DiagnosticDataIdentifier:
        """
        Creates a new DiagnosticDataIdentifier with the given short name,
        or returns an existing one if it already exists in this package.

        DiagnosticDataIdentifier represents the ability to model a diagnostic
        data identifier (DID) that is fully specified regarding the payload
        at configuration-time.

        Args:
            short_name: The short name for the new DiagnosticDataIdentifier

        Returns:
            The newly created or existing DiagnosticDataIdentifier instance
        """
        if not self.IsReferrableElementExists(short_name, DiagnosticDataIdentifier):
            did = DiagnosticDataIdentifier(self, short_name)
            self.addReferrableElement(did)
        return cast(DiagnosticDataIdentifier, self.getReferrableElement(short_name, DiagnosticDataIdentifier))

    def createDiagnosticDataIdentifierSet(self, short_name: str) -> DiagnosticDataIdentifierSet:
        """
        Creates a new DiagnosticDataIdentifierSet with the given short name,
        or returns an existing one if it already exists in this package.

        DiagnosticDataIdentifierSet represents the ability to define a list
        of DiagnosticDataIdentifiers that can be reused in different contexts.

        Args:
            short_name: The short name for the new DiagnosticDataIdentifierSet

        Returns:
            The newly created or existing DiagnosticDataIdentifierSet instance
        """
        if not self.IsReferrableElementExists(short_name, DiagnosticDataIdentifierSet):
            data_identifier_set = DiagnosticDataIdentifierSet(self, short_name)
            self.addReferrableElement(data_identifier_set)
        return cast(DiagnosticDataIdentifierSet, self.getReferrableElement(short_name, DiagnosticDataIdentifierSet))

    def createDiagnosticDynamicDataIdentifier(self, short_name: str) -> DiagnosticDynamicDataIdentifier:
        """
        Creates a new DiagnosticDynamicDataIdentifier with the given short name,
        or returns an existing one if it already exists in this package.

        DiagnosticDynamicDataIdentifier represents the ability to define a
        diagnostic data identifier (DID) at run-time.

        Args:
            short_name: The short name for the new DiagnosticDynamicDataIdentifier

        Returns:
            The newly created or existing DiagnosticDynamicDataIdentifier instance
        """
        if not self.IsReferrableElementExists(short_name, DiagnosticDynamicDataIdentifier):
            did = DiagnosticDynamicDataIdentifier(self, short_name)
            self.addReferrableElement(did)
        return cast(DiagnosticDynamicDataIdentifier, self.getReferrableElement(short_name, DiagnosticDynamicDataIdentifier))

    def createDiagnosticEcuInstanceProps(self, short_name: str) -> DiagnosticEcuInstanceProps:
        """
        Creates a new DiagnosticEcuInstanceProps with the given short name,
        or returns an existing one if it already exists in this package.

        DiagnosticEcuInstanceProps: This meta-class represents the ability to model properties that are specific for a given EcuInstance but on the other hand represent purely diagnostic-related information.

        Args:
            short_name: The short name for the new DiagnosticEcuInstanceProps

        Returns:
            The newly created or existing DiagnosticEcuInstanceProps instance
        """
        if not self.IsReferrableElementExists(short_name, DiagnosticEcuInstanceProps):
            element = DiagnosticEcuInstanceProps(self, short_name)
            self.addReferrableElement(element)
        return cast(DiagnosticEcuInstanceProps, self.getReferrableElement(short_name, DiagnosticEcuInstanceProps))

    def createDiagnosticEcuReset(self, short_name: str) -> DiagnosticEcuReset:
        """
        Creates a new DiagnosticEcuReset with the given short name,
        or returns an existing one if it already exists in this package.

        DiagnosticEcuReset represents an instance of the "ECU Reset" diagnostic service.

        Args:
            short_name: The short name for the new DiagnosticEcuReset

        Returns:
            The newly created or existing DiagnosticEcuReset instance
        """
        if not self.IsReferrableElementExists(short_name, DiagnosticEcuReset):
            ecu_reset = DiagnosticEcuReset(self, short_name)
            self.addReferrableElement(ecu_reset)
        return cast(DiagnosticEcuReset, self.getReferrableElement(short_name, DiagnosticEcuReset))

    def createDiagnosticEcuResetClass(self, short_name: str) -> DiagnosticEcuResetClass:
        """
        Creates a new DiagnosticEcuResetClass with the given short name,
        or returns an existing one if it already exists in this package.

        DiagnosticEcuResetClass contains attributes shared by all
        instances of the "Ecu Reset" diagnostic service.

        Args:
            short_name: The short name for the new DiagnosticEcuResetClass

        Returns:
            The newly created or existing DiagnosticEcuResetClass instance
        """
        if not self.IsReferrableElementExists(short_name, DiagnosticEcuResetClass):
            ecu_reset_class = DiagnosticEcuResetClass(self, short_name)
            self.addReferrableElement(ecu_reset_class)
        return cast(DiagnosticEcuResetClass, self.getReferrableElement(short_name, DiagnosticEcuResetClass))

    def createDiagnosticEnvironmentalCondition(self, short_name: str) -> DiagnosticEnvironmentalCondition:
        """
        Creates a new DiagnosticEnvironmentalCondition with the given short
        name, or returns an existing one if it already exists in this package.

        DiagnosticEnvironmentalCondition represents a condition which is
        evaluated during runtime of the ECU in the diagnostic extract
        template of AUTOSAR.

        Args:
            short_name: The short name for the new DiagnosticEnvironmentalCondition

        Returns:
            The newly created or existing DiagnosticEnvironmentalCondition instance
        """
        if not self.IsReferrableElementExists(short_name, DiagnosticEnvironmentalCondition):
            condition = DiagnosticEnvironmentalCondition(self, short_name)
            self.addReferrableElement(condition)
        return cast(DiagnosticEnvironmentalCondition, self.getReferrableElement(short_name, DiagnosticEnvironmentalCondition))

    def createDiagnosticFimEventGroup(self, short_name: str) -> DiagnosticFimEventGroup:
        """
        Creates a new DiagnosticFimEventGroup with the given short name,
        or returns an existing one if it already exists in this package.

        DiagnosticFimEventGroup represents the ability to model a Fim event
        group, also known as a summary event in Fim terminology.

        Args:
            short_name: The short name for the new DiagnosticFimEventGroup

        Returns:
            The newly created or existing DiagnosticFimEventGroup instance
        """
        if not self.IsReferrableElementExists(short_name, DiagnosticFimEventGroup):
            fim_event_group = DiagnosticFimEventGroup(self, short_name)
            self.addReferrableElement(fim_event_group)
        return cast(DiagnosticFimEventGroup, self.getReferrableElement(short_name, DiagnosticFimEventGroup))

    def createDiagnosticFreezeFrame(self, short_name: str) -> DiagnosticFreezeFrame:
        """
        Creates a new DiagnosticFreezeFrame with the given short name,
        or returns an existing one if it already exists in this package.

        DiagnosticFreezeFrame: This element describes combinations of DIDs for a non OBD relevant freeze frame.

        Args:
            short_name: The short name for the new DiagnosticFreezeFrame

        Returns:
            The newly created or existing DiagnosticFreezeFrame instance
        """
        if not self.IsReferrableElementExists(short_name, DiagnosticFreezeFrame):
            element = DiagnosticFreezeFrame(self, short_name)
            self.addReferrableElement(element)
        return cast(DiagnosticFreezeFrame, self.getReferrableElement(short_name, DiagnosticFreezeFrame))

    def createDiagnosticFunctionIdentifier(self, short_name: str) -> DiagnosticFunctionIdentifier:
        """
        Creates a new DiagnosticFunctionIdentifier with the given short name,
        or returns an existing one if it already exists in this package.

        DiagnosticFunctionIdentifier: This meta-class represents a diagnostic function identifier (a.k.a. FID). Tags: atp.recommendedPackage=DiagnosticFunctionIdentifiers.

        Args:
            short_name: The short name for the new DiagnosticFunctionIdentifier

        Returns:
            The newly created or existing DiagnosticFunctionIdentifier instance
        """
        if not self.IsReferrableElementExists(short_name, DiagnosticFunctionIdentifier):
            element = DiagnosticFunctionIdentifier(self, short_name)
            self.addReferrableElement(element)
        return cast(DiagnosticFunctionIdentifier, self.getReferrableElement(short_name, DiagnosticFunctionIdentifier))

    def createDiagnosticJ1939Spn(self, short_name: str) -> DiagnosticJ1939Spn:
        """
        Creates a new DiagnosticJ1939Spn with the given short name,
        or returns an existing one if it already exists in this package.

        DiagnosticJ1939Spn represents the ability to model a J1939 Suspect
        Parameter Number (SPN).

        Args:
            short_name: The short name for the new DiagnosticJ1939Spn

        Returns:
            The newly created or existing DiagnosticJ1939Spn instance
        """
        if not self.IsReferrableElementExists(short_name, DiagnosticJ1939Spn):
            j1939_spn = DiagnosticJ1939Spn(self, short_name)
            self.addReferrableElement(j1939_spn)
        return cast(DiagnosticJ1939Spn, self.getReferrableElement(short_name, DiagnosticJ1939Spn))

    def createDiagnosticJ1939ExpandedFreezeFrame(self, short_name: str) -> DiagnosticJ1939ExpandedFreezeFrame:
        """
        Creates a new DiagnosticJ1939ExpandedFreezeFrame with the given short name,
        or returns an existing one if it already exists in this package.

        DiagnosticJ1939ExpandedFreezeFrame represents the ability to model an
        expanded J1939 Freeze Frame.

        Args:
            short_name: The short name for the new DiagnosticJ1939ExpandedFreezeFrame

        Returns:
            The newly created or existing DiagnosticJ1939ExpandedFreezeFrame instance
        """
        if not self.IsReferrableElementExists(short_name, DiagnosticJ1939ExpandedFreezeFrame):
            expanded_freeze_frame = DiagnosticJ1939ExpandedFreezeFrame(self, short_name)
            self.addReferrableElement(expanded_freeze_frame)
        return cast(DiagnosticJ1939ExpandedFreezeFrame, self.getReferrableElement(short_name, DiagnosticJ1939ExpandedFreezeFrame))

    def createDiagnosticJ1939FreezeFrame(self, short_name: str) -> DiagnosticJ1939FreezeFrame:
        """
        Creates a new DiagnosticJ1939FreezeFrame with the given short name,
        or returns an existing one if it already exists in this package.

        DiagnosticJ1939FreezeFrame represents the ability to model a J1939 Freeze Frame.

        Args:
            short_name: The short name for the new DiagnosticJ1939FreezeFrame

        Returns:
            The newly created or existing DiagnosticJ1939FreezeFrame instance
        """
        if not self.IsReferrableElementExists(short_name, DiagnosticJ1939FreezeFrame):
            freeze_frame = DiagnosticJ1939FreezeFrame(self, short_name)
            self.addReferrableElement(freeze_frame)
        return cast(DiagnosticJ1939FreezeFrame, self.getReferrableElement(short_name, DiagnosticJ1939FreezeFrame))

    def createDiagnosticTroubleCode(self, short_name: str) -> DiagnosticTroubleCode:
        """
        Creates a new DiagnosticTroubleCode with the given short name,
        or returns an existing one if it already exists in this package.

        DiagnosticTroubleCode: A diagnostic trouble code defines a unique identifier that is shown to the diagnostic tester.

        Args:
            short_name: The short name for the new DiagnosticTroubleCode

        Returns:
            The newly created or existing DiagnosticTroubleCode instance
        """
        if not self.IsReferrableElementExists(short_name, DiagnosticTroubleCode):
            trouble_code = DiagnosticTroubleCode(self, short_name)
            self.addReferrableElement(trouble_code)
        return cast(DiagnosticTroubleCode, self.getReferrableElement(short_name, DiagnosticTroubleCode))

    def createDiagnosticTroubleCodeGroup(self, short_name: str) -> DiagnosticTroubleCodeGroup:
        """
        Creates a new DiagnosticTroubleCodeGroup with the given short name,
        or returns an existing one if it already exists in this package.

        DiagnosticTroubleCodeGroup: The diagnostic trouble code group defines the DTCs belonging together and thereby forming a group.

        Args:
            short_name: The short name for the new DiagnosticTroubleCodeGroup

        Returns:
            The newly created or existing DiagnosticTroubleCodeGroup instance
        """
        if not self.IsReferrableElementExists(short_name, DiagnosticTroubleCodeGroup):
            element = DiagnosticTroubleCodeGroup(self, short_name)
            self.addReferrableElement(element)
        return cast(DiagnosticTroubleCodeGroup, self.getReferrableElement(short_name, DiagnosticTroubleCodeGroup))

    def createDiagnosticTroubleCodeJ1939(self, short_name: str) -> DiagnosticTroubleCodeJ1939:
        """
        Creates a new DiagnosticTroubleCodeJ1939 with the given short name,
        or returns an existing one if it already exists in this package.

        DiagnosticTroubleCodeJ1939 represents the ability to model specific
        trouble-code related properties for J1939.

        Args:
            short_name: The short name for the new DiagnosticTroubleCodeJ1939

        Returns:
            The newly created or existing DiagnosticTroubleCodeJ1939 instance
        """
        if not self.IsReferrableElementExists(short_name, DiagnosticTroubleCodeJ1939):
            trouble_code = DiagnosticTroubleCodeJ1939(self, short_name)
            self.addReferrableElement(trouble_code)
        return cast(DiagnosticTroubleCodeJ1939, self.getReferrableElement(short_name, DiagnosticTroubleCodeJ1939))

    def createDiagnosticTroubleCodeUdsToTroubleCodeObdMapping(self, short_name: str) -> DiagnosticTroubleCodeUdsToTroubleCodeObdMapping:
        """
        Creates a new DiagnosticTroubleCodeUdsToTroubleCodeObdMapping with the given short name,
        or returns an existing one if it already exists in this package.

        DiagnosticTroubleCodeUdsToTroubleCodeObdMapping: This meta-class represents the ability to associate a UDS trouble code to an OBD trouble code.

        Args:
            short_name: The short name for the new DiagnosticTroubleCodeUdsToTroubleCodeObdMapping

        Returns:
            The newly created or existing DiagnosticTroubleCodeUdsToTroubleCodeObdMapping instance
        """
        if not self.IsReferrableElementExists(short_name, DiagnosticTroubleCodeUdsToTroubleCodeObdMapping):
            element = DiagnosticTroubleCodeUdsToTroubleCodeObdMapping(self, short_name)
            self.addReferrableElement(element)
        return cast(DiagnosticTroubleCodeUdsToTroubleCodeObdMapping, self.getReferrableElement(short_name, DiagnosticTroubleCodeUdsToTroubleCodeObdMapping))

    def createDiagnosticServiceDataMapping(self, short_name: str) -> DiagnosticServiceDataMapping:
        """
        Creates a new DiagnosticServiceDataMapping with the given short name,
        or returns an existing one if it already exists in this package.

        DiagnosticServiceDataMapping represents the ability to define a mapping
        of a diagnostic service to a software-component.

        Args:
            short_name: The short name for the new DiagnosticServiceDataMapping

        Returns:
            The newly created or existing DiagnosticServiceDataMapping instance
        """
        if not self.IsReferrableElementExists(short_name, DiagnosticServiceDataMapping):
            service_data_mapping = DiagnosticServiceDataMapping(self, short_name)
            self.addReferrableElement(service_data_mapping)
        return cast(DiagnosticServiceDataMapping, self.getReferrableElement(short_name, DiagnosticServiceDataMapping))

    def createDiagnosticStorageConditionPortMapping(self, short_name: str) -> DiagnosticStorageConditionPortMapping:
        """
        Creates a new DiagnosticStorageConditionPortMapping with the given short name,
        or returns an existing one if it already exists in this package.

        DiagnosticStorageConditionPortMapping: Defines to which SWC service ports with DiagnosticStorageConditionNeeds the DiagnosticStorageCondition is mapped..

        Args:
            short_name: The short name for the new DiagnosticStorageConditionPortMapping

        Returns:
            The newly created or existing DiagnosticStorageConditionPortMapping instance
        """
        if not self.IsReferrableElementExists(short_name, DiagnosticStorageConditionPortMapping):
            element = DiagnosticStorageConditionPortMapping(self, short_name)
            self.addReferrableElement(element)
        return cast(DiagnosticStorageConditionPortMapping, self.getReferrableElement(short_name, DiagnosticStorageConditionPortMapping))

    def createDiagnosticEventToSecurityEventMapping(self, short_name: str) -> DiagnosticEventToSecurityEventMapping:
        """
        Creates a new DiagnosticEventToSecurityEventMapping with the given short name,
        or returns an existing one if it already exists in this package.

        DiagnosticEventToSecurityEventMapping: This meta-class represents the ability to map a security event that is defined in the context of the Security Extract to a diagnostic event defined on the context of the DiagnosticExtract..

        Args:
            short_name: The short name for the new DiagnosticEventToSecurityEventMapping

        Returns:
            The newly created or existing DiagnosticEventToSecurityEventMapping instance
        """
        if not self.IsReferrableElementExists(short_name, DiagnosticEventToSecurityEventMapping):
            element = DiagnosticEventToSecurityEventMapping(self, short_name)
            self.addReferrableElement(element)
        return cast(DiagnosticEventToSecurityEventMapping, self.getReferrableElement(short_name, DiagnosticEventToSecurityEventMapping))

    def createDiagnosticFimAliasEventGroupMapping(self, short_name: str) -> DiagnosticFimAliasEventGroupMapping:
        """
        Creates a new DiagnosticFimAliasEventGroupMapping with the given short name,
        or returns an existing one if it already exists in this package.

        DiagnosticFimAliasEventGroupMapping: This meta-class represents the ability to map a DiagnosticFimEventGroup to a DiagnosticFimAliasEventGroup. By this means the "preliminary" modeling by way of a DiagnosticFimAliasEventGroup is further substantiated..

        Args:
            short_name: The short name for the new DiagnosticFimAliasEventGroupMapping

        Returns:
            The newly created or existing DiagnosticFimAliasEventGroupMapping instance
        """
        if not self.IsReferrableElementExists(short_name, DiagnosticFimAliasEventGroupMapping):
            element = DiagnosticFimAliasEventGroupMapping(self, short_name)
            self.addReferrableElement(element)
        return cast(DiagnosticFimAliasEventGroupMapping, self.getReferrableElement(short_name, DiagnosticFimAliasEventGroupMapping))

    def createDiagnosticFimFunctionMapping(self, short_name: str) -> DiagnosticFimFunctionMapping:
        """
        Creates a new DiagnosticFimFunctionMapping with the given short name,
        or returns an existing one if it already exists in this package.

        DiagnosticFimFunctionMapping: This meta-class represents the ability to define a mapping between a function identifier (FID) and the corresponding SwcServiceDependency in the application software resp. basic software..

        Args:
            short_name: The short name for the new DiagnosticFimFunctionMapping

        Returns:
            The newly created or existing DiagnosticFimFunctionMapping instance
        """
        if not self.IsReferrableElementExists(short_name, DiagnosticFimFunctionMapping):
            element = DiagnosticFimFunctionMapping(self, short_name)
            self.addReferrableElement(element)
        return cast(DiagnosticFimFunctionMapping, self.getReferrableElement(short_name, DiagnosticFimFunctionMapping))

    def createDiagnosticJ1939SwMapping(self, short_name: str) -> DiagnosticJ1939SwMapping:
        """
        Creates a new DiagnosticJ1939SwMapping with the given short name,
        or returns an existing one if it already exists in this package.

        DiagnosticJ1939SwMapping: This meta-class represents the ability to map a piece of application software to a J1939DiagnosticNode. By this means the diagnostic configuration can be associated with the application software..

        Args:
            short_name: The short name for the new DiagnosticJ1939SwMapping

        Returns:
            The newly created or existing DiagnosticJ1939SwMapping instance
        """
        if not self.IsReferrableElementExists(short_name, DiagnosticJ1939SwMapping):
            element = DiagnosticJ1939SwMapping(self, short_name)
            self.addReferrableElement(element)
        return cast(DiagnosticJ1939SwMapping, self.getReferrableElement(short_name, DiagnosticJ1939SwMapping))

    def createDiagnosticJ1939Node(self, short_name: str) -> DiagnosticJ1939Node:
        """
        Creates a new DiagnosticJ1939Node with the given short name,
        or returns an existing one if it already exists in this package.

        DiagnosticJ1939Node: This meta-class represents the diagnostic configuration of a J1939 Nm node, which in turn represents a "virtual Ecu" on the J1939 communication bus..

        Args:
            short_name: The short name for the new DiagnosticJ1939Node

        Returns:
            The newly created or existing DiagnosticJ1939Node instance
        """
        if not self.IsReferrableElementExists(short_name, DiagnosticJ1939Node):
            element = DiagnosticJ1939Node(self, short_name)
            self.addReferrableElement(element)
        return cast(DiagnosticJ1939Node, self.getReferrableElement(short_name, DiagnosticJ1939Node))

    def createDiagnosticJ1939SpnMapping(self, short_name: str) -> DiagnosticJ1939SpnMapping:
        """
        Creates a new DiagnosticJ1939SpnMapping with the given short name,
        or returns an existing one if it already exists in this package.

        DiagnosticJ1939SpnMapping: This meta-class represents the ability to define a mapping between an SPN and a SystemSignal. The existence of a mapping means that neither the SPN nor the SystemSignal need to be updated if the relation between the two changes..

        Args:
            short_name: The short name for the new DiagnosticJ1939SpnMapping

        Returns:
            The newly created or existing DiagnosticJ1939SpnMapping instance
        """
        if not self.IsReferrableElementExists(short_name, DiagnosticJ1939SpnMapping):
            element = DiagnosticJ1939SpnMapping(self, short_name)
            self.addReferrableElement(element)
        return cast(DiagnosticJ1939SpnMapping, self.getReferrableElement(short_name, DiagnosticJ1939SpnMapping))

    def createDiagnosticIumpr(self, short_name: str) -> DiagnosticIumpr:
        """
        Creates a new DiagnosticIumpr with the given short name,
        or returns an existing one if it already exists in this package.

        DiagnosticIumpr: This meta-class represents the ability to model the in-use monitor performance ratio. The latter computes to the number of times a fault could have been found divided by the number of times the vehicle conditions have been properly fulfilled. Tags: atp.recommendedPackage=DiagnosticIumprs

        Args:
            short_name: The short name for the new DiagnosticIumpr

        Returns:
            The newly created or existing DiagnosticIumpr instance
        """
        if not self.IsReferrableElementExists(short_name, DiagnosticIumpr):
            element = DiagnosticIumpr(self, short_name)
            self.addReferrableElement(element)
        return cast(DiagnosticIumpr, self.getReferrableElement(short_name, DiagnosticIumpr))

    def createDiagnosticIumprDenominatorGroup(self, short_name: str) -> DiagnosticIumprDenominatorGroup:
        """
        Creates a new DiagnosticIumprDenominatorGroup with the given short name,
        or returns an existing one if it already exists in this package.

        DiagnosticIumprDenominatorGroup: This meta-class represents the ability to model a IUMPR denominator groups. Tags: atp.recommendedPackage=DiagnosticIumprDenominatorGroup

        Args:
            short_name: The short name for the new DiagnosticIumprDenominatorGroup

        Returns:
            The newly created or existing DiagnosticIumprDenominatorGroup instance
        """
        if not self.IsReferrableElementExists(short_name, DiagnosticIumprDenominatorGroup):
            element = DiagnosticIumprDenominatorGroup(self, short_name)
            self.addReferrableElement(element)
        return cast(DiagnosticIumprDenominatorGroup, self.getReferrableElement(short_name, DiagnosticIumprDenominatorGroup))

    def createDiagnosticIumprGroup(self, short_name: str) -> DiagnosticIumprGroup:
        """
        Creates a new DiagnosticIumprGroup with the given short name,
        or returns an existing one if it already exists in this package.

        DiagnosticIumprGroup: This meta-class represents the ability to model a IUMPR groups. Tags: atp.recommendedPackage=DiagnosticIumprGroups

        Args:
            short_name: The short name for the new DiagnosticIumprGroup

        Returns:
            The newly created or existing DiagnosticIumprGroup instance
        """
        if not self.IsReferrableElementExists(short_name, DiagnosticIumprGroup):
            element = DiagnosticIumprGroup(self, short_name)
            self.addReferrableElement(element)
        return cast(DiagnosticIumprGroup, self.getReferrableElement(short_name, DiagnosticIumprGroup))

    def createDiagnosticIumprToFunctionIdentifierMapping(self, short_name: str) -> DiagnosticIumprToFunctionIdentifierMapping:
        """
        Creates a new DiagnosticIumprToFunctionIdentifierMapping with the given short name,
        or returns an existing one if it already exists in this package.

        DiagnosticIumprToFunctionIdentifierMapping: This meta-class represents the ability to associate a DiagnosticFunctionIdentifier with a DiagnosticIumpr..

        Args:
            short_name: The short name for the new DiagnosticIumprToFunctionIdentifierMapping

        Returns:
            The newly created or existing DiagnosticIumprToFunctionIdentifierMapping instance
        """
        if not self.IsReferrableElementExists(short_name, DiagnosticIumprToFunctionIdentifierMapping):
            element = DiagnosticIumprToFunctionIdentifierMapping(self, short_name)
            self.addReferrableElement(element)
        return cast(DiagnosticIumprToFunctionIdentifierMapping, self.getReferrableElement(short_name, DiagnosticIumprToFunctionIdentifierMapping))

    def createDiagnosticEventToTroubleCodeJ1939Mapping(self, short_name: str) -> DiagnosticEventToTroubleCodeJ1939Mapping:
        """
        Creates a new DiagnosticEventToTroubleCodeJ1939Mapping with the given short name,
        or returns an existing one if it already exists in this package.

        DiagnosticEventToTroubleCodeJ1939Mapping: By means of this meta-class it is possible to associate a DiagnosticEvent to a DiagnosticTroubleCodeJ1939..

        Args:
            short_name: The short name for the new DiagnosticEventToTroubleCodeJ1939Mapping

        Returns:
            The newly created or existing DiagnosticEventToTroubleCodeJ1939Mapping instance
        """
        if not self.IsReferrableElementExists(short_name, DiagnosticEventToTroubleCodeJ1939Mapping):
            element = DiagnosticEventToTroubleCodeJ1939Mapping(self, short_name)
            self.addReferrableElement(element)
        return cast(DiagnosticEventToTroubleCodeJ1939Mapping, self.getReferrableElement(short_name, DiagnosticEventToTroubleCodeJ1939Mapping))

    def createDiagnosticServiceSwMapping(self, short_name: str) -> DiagnosticServiceSwMapping:
        """
        Creates a new DiagnosticServiceSwMapping with the given short name,
        or returns an existing one if it already exists in this package.

        DiagnosticServiceSwMapping: This represents the ability to define a mapping of a diagnostic service to a software-component or a basic-software module.

        Args:
            short_name: The short name for the new DiagnosticServiceSwMapping

        Returns:
            The newly created or existing DiagnosticServiceSwMapping instance
        """
        if not self.IsReferrableElementExists(short_name, DiagnosticServiceSwMapping):
            element = DiagnosticServiceSwMapping(self, short_name)
            self.addReferrableElement(element)
        return cast(DiagnosticServiceSwMapping, self.getReferrableElement(short_name, DiagnosticServiceSwMapping))

    def createCpSwClusterResourceToDiagFunctionIdMapping(self, short_name: str) -> CpSwClusterResourceToDiagFunctionIdMapping:
        """
        Creates a new CpSwClusterResourceToDiagFunctionIdMapping with the given short name,
        or returns an existing one if it already exists in this package.

        CpSwClusterResourceToDiagFunctionIdMapping: This meta-class represents the ability to associate a CpSoftwareClusterResource with a subfunction of a DiagnosticFunctionIdentifier. This allows for indicating that the CpSoftwareClusterResource is used to convey the execution permission associated with the mapped function identifier..

        Args:
            short_name: The short name for the new CpSwClusterResourceToDiagFunctionIdMapping

        Returns:
            The newly created or existing CpSwClusterResourceToDiagFunctionIdMapping instance
        """
        if not self.IsReferrableElementExists(short_name, CpSwClusterResourceToDiagFunctionIdMapping):
            element = CpSwClusterResourceToDiagFunctionIdMapping(self, short_name)
            self.addReferrableElement(element)
        return cast(CpSwClusterResourceToDiagFunctionIdMapping, self.getReferrableElement(short_name, CpSwClusterResourceToDiagFunctionIdMapping))

    def createCpSwClusterToDiagRoutineSubfunctionMapping(self, short_name: str) -> CpSwClusterToDiagRoutineSubfunctionMapping:
        """
        Creates a new CpSwClusterToDiagRoutineSubfunctionMapping with the given short name,
        or returns an existing one if it already exists in this package.

        CpSwClusterToDiagRoutineSubfunctionMapping: This meta-class represents the ability to associate a CpSoftwareClusterResource with a subfunction of a DiagnosticRoutine. This allows for indicating that the CpSoftwareClusterResource is used to convey the calling or result return of the mapped DiagnosticRoutine..

        Args:
            short_name: The short name for the new CpSwClusterToDiagRoutineSubfunctionMapping

        Returns:
            The newly created or existing CpSwClusterToDiagRoutineSubfunctionMapping instance
        """
        if not self.IsReferrableElementExists(short_name, CpSwClusterToDiagRoutineSubfunctionMapping):
            element = CpSwClusterToDiagRoutineSubfunctionMapping(self, short_name)
            self.addReferrableElement(element)
        return cast(CpSwClusterToDiagRoutineSubfunctionMapping, self.getReferrableElement(short_name, CpSwClusterToDiagRoutineSubfunctionMapping))

    def createCpSwClusterResourceToDiagDataElemMapping(self, short_name: str) -> CpSwClusterResourceToDiagDataElemMapping:
        """
        Creates a new CpSwClusterResourceToDiagDataElemMapping with the given short name,
        or returns an existing one if it already exists in this package.

        CpSwClusterResourceToDiagDataElemMapping: This meta-class represents the ability to associate a CpSoftwareClusterResource with a DiagnosticDataElement. This allows for indicating that the CpSoftwareClusterResource is used to convey the DiagnosticDataElement..

        Args:
            short_name: The short name for the new CpSwClusterResourceToDiagDataElemMapping

        Returns:
            The newly created or existing CpSwClusterResourceToDiagDataElemMapping instance
        """
        if not self.IsReferrableElementExists(short_name, CpSwClusterResourceToDiagDataElemMapping):
            element = CpSwClusterResourceToDiagDataElemMapping(self, short_name)
            self.addReferrableElement(element)
        return cast(CpSwClusterResourceToDiagDataElemMapping, self.getReferrableElement(short_name, CpSwClusterResourceToDiagDataElemMapping))

    def createCpSwClusterToDiagEventMapping(self, short_name: str) -> CpSwClusterToDiagEventMapping:
        """
        Creates a new CpSwClusterToDiagEventMapping with the given short name,
        or returns an existing one if it already exists in this package.

        CpSwClusterToDiagEventMapping: This meta-class represents the ability to associate a CpSoftwareClusterResource with a DiagnosticEvent. This allows for indicating that the CpSoftwareClusterResource is used to convey the reporting or status query of the mapped DiagnosticEvent..

        Args:
            short_name: The short name for the new CpSwClusterToDiagEventMapping

        Returns:
            The newly created or existing CpSwClusterToDiagEventMapping instance
        """
        if not self.IsReferrableElementExists(short_name, CpSwClusterToDiagEventMapping):
            element = CpSwClusterToDiagEventMapping(self, short_name)
            self.addReferrableElement(element)
        return cast(CpSwClusterToDiagEventMapping, self.getReferrableElement(short_name, CpSwClusterToDiagEventMapping))

    def createDiagnosticFimAliasEvent(self, short_name: str) -> DiagnosticFimAliasEvent:
        """
        Creates a new DiagnosticFimAliasEvent with the given short name,
        or returns an existing one if it already exists in this package.

        DiagnosticFimAliasEvent: This meta-class is used to represent a given event semantics. However, the name of the actual events used in a specific project is sometimes not defined yet, not known or not in the responsibility of the author. Therefore, the DiagnosticFimAliasEvent has a reference to the actual DiagnosticEvent and by this the final connection is created..

        Args:
            short_name: The short name for the new DiagnosticFimAliasEvent

        Returns:
            The newly created or existing DiagnosticFimAliasEvent instance
        """
        if not self.IsReferrableElementExists(short_name, DiagnosticFimAliasEvent):
            element = DiagnosticFimAliasEvent(self, short_name)
            self.addReferrableElement(element)
        return cast(DiagnosticFimAliasEvent, self.getReferrableElement(short_name, DiagnosticFimAliasEvent))

    def createDiagnosticFimAliasEventGroup(self, short_name: str) -> DiagnosticFimAliasEventGroup:
        """
        Creates a new DiagnosticFimAliasEventGroup with the given short name,
        or returns an existing one if it already exists in this package.

        DiagnosticFimAliasEventGroup: This meta-class represents the ability to define an alias for a Fim summarized event. This alias can be used in early phases of the configuration process until a further refinement is possible..

        Args:
            short_name: The short name for the new DiagnosticFimAliasEventGroup

        Returns:
            The newly created or existing DiagnosticFimAliasEventGroup instance
        """
        if not self.IsReferrableElementExists(short_name, DiagnosticFimAliasEventGroup):
            element = DiagnosticFimAliasEventGroup(self, short_name)
            self.addReferrableElement(element)
        return cast(DiagnosticFimAliasEventGroup, self.getReferrableElement(short_name, DiagnosticFimAliasEventGroup))

    def createDiagnosticFimAliasEventMapping(self, short_name: str) -> DiagnosticFimAliasEventMapping:
        """
        Creates a new DiagnosticFimAliasEventMapping with the given short name,
        or returns an existing one if it already exists in this package.

        DiagnosticFimAliasEventMapping: This meta-class represents the ability to model the mapping of a DiagnosticEvent to a DiagnosticAliasEvent. By this means the "preliminary" modeling by way of a DiagnosticAliasEvent is further substantiated..

        Args:
            short_name: The short name for the new DiagnosticFimAliasEventMapping

        Returns:
            The newly created or existing DiagnosticFimAliasEventMapping instance
        """
        if not self.IsReferrableElementExists(short_name, DiagnosticFimAliasEventMapping):
            element = DiagnosticFimAliasEventMapping(self, short_name)
            self.addReferrableElement(element)
        return cast(DiagnosticFimAliasEventMapping, self.getReferrableElement(short_name, DiagnosticFimAliasEventMapping))

    def createDiagnosticInhibitSourceEventMapping(self, short_name: str) -> DiagnosticInhibitSourceEventMapping:
        """
        Creates a new DiagnosticInhibitSourceEventMapping with the given short name,
        or returns an existing one if it already exists in this package.

        DiagnosticInhibitSourceEventMapping: This meta-class represents the ability to map a DiagnosticFunctionInhibitSource directly to alternatively one DiagnosticEvent or one DiagnosticFimSummaryEvent. This model element shall be used if the approach via the alias events is not applicable, i.e. when diagnostic events defined by the Dem are already available at the time the Fim configuration within the diagnostic extract is created..

        Args:
            short_name: The short name for the new DiagnosticInhibitSourceEventMapping

        Returns:
            The newly created or existing DiagnosticInhibitSourceEventMapping instance
        """
        if not self.IsReferrableElementExists(short_name, DiagnosticInhibitSourceEventMapping):
            element = DiagnosticInhibitSourceEventMapping(self, short_name)
            self.addReferrableElement(element)
        return cast(DiagnosticInhibitSourceEventMapping, self.getReferrableElement(short_name, DiagnosticInhibitSourceEventMapping))

    def createDiagnosticMasterToSlaveEventMapping(self, short_name: str) -> DiagnosticMasterToSlaveEventMapping:
        """
        Creates a new DiagnosticMasterToSlaveEventMapping with the given short name,
        or returns an existing one if it already exists in this package.

        DiagnosticMasterToSlaveEventMapping: This meta-class provides the ability to map a master diagnostic event with a slave diagnostic event such that reporting of the master event with a given value also reports the slave event with the same value.

        Args:
            short_name: The short name for the new DiagnosticMasterToSlaveEventMapping

        Returns:
            The newly created or existing DiagnosticMasterToSlaveEventMapping instance
        """
        if not self.IsReferrableElementExists(short_name, DiagnosticMasterToSlaveEventMapping):
            element = DiagnosticMasterToSlaveEventMapping(self, short_name)
            self.addReferrableElement(element)
        return cast(DiagnosticMasterToSlaveEventMapping, self.getReferrableElement(short_name, DiagnosticMasterToSlaveEventMapping))

    def createDiagnosticMeasurementIdentifier(self, short_name: str) -> DiagnosticMeasurementIdentifier:
        """
        Creates a new DiagnosticMeasurementIdentifier with the given short name,
        or returns an existing one if it already exists in this package.

        DiagnosticMeasurementIdentifier: This meta-class represents the ability to describe a measurement identifier.

        Args:
            short_name: The short name for the new DiagnosticMeasurementIdentifier

        Returns:
            The newly created or existing DiagnosticMeasurementIdentifier instance
        """
        if not self.IsReferrableElementExists(short_name, DiagnosticMeasurementIdentifier):
            element = DiagnosticMeasurementIdentifier(self, short_name)
            self.addReferrableElement(element)
        return cast(DiagnosticMeasurementIdentifier, self.getReferrableElement(short_name, DiagnosticMeasurementIdentifier))

    def createDiagnosticMemoryDestinationPrimary(self, short_name: str) -> DiagnosticMemoryDestinationPrimary:
        """
        Creates a new DiagnosticMemoryDestinationPrimary with the given short name,
        or returns an existing one if it already exists in this package.

        DiagnosticMemoryDestinationPrimary: This represents a primary memory for a diagnostic event.

        Args:
            short_name: The short name for the new DiagnosticMemoryDestinationPrimary

        Returns:
            The newly created or existing DiagnosticMemoryDestinationPrimary instance
        """
        if not self.IsReferrableElementExists(short_name, DiagnosticMemoryDestinationPrimary):
            element = DiagnosticMemoryDestinationPrimary(self, short_name)
            self.addReferrableElement(element)
        return cast(DiagnosticMemoryDestinationPrimary, self.getReferrableElement(short_name, DiagnosticMemoryDestinationPrimary))

    def createDiagnosticMemoryIdentifier(self, short_name: str) -> DiagnosticMemoryIdentifier:
        """
        Creates a new DiagnosticMemoryIdentifier with the given short name,
        or returns an existing one if it already exists in this package.

        DiagnosticMemoryIdentifier: This meta-class represents the ability to define memory properties from the diagnostics point of view..

        Args:
            short_name: The short name for the new DiagnosticMemoryIdentifier

        Returns:
            The newly created or existing DiagnosticMemoryIdentifier instance
        """
        if not self.IsReferrableElementExists(short_name, DiagnosticMemoryIdentifier):
            element = DiagnosticMemoryIdentifier(self, short_name)
            self.addReferrableElement(element)
        return cast(DiagnosticMemoryIdentifier, self.getReferrableElement(short_name, DiagnosticMemoryIdentifier))

    def createDiagnosticDemProvidedDataMapping(self, short_name: str) -> DiagnosticDemProvidedDataMapping:
        """
        Creates a new DiagnosticDemProvidedDataMapping with the given short name,
        or returns an existing one if it already exists in this package.

        DiagnosticDemProvidedDataMapping: This represents the ability to define the nature of a data access for a DiagnosticDataElement in the Dem..

        Args:
            short_name: The short name for the new DiagnosticDemProvidedDataMapping

        Returns:
            The newly created or existing DiagnosticDemProvidedDataMapping instance
        """
        if not self.IsReferrableElementExists(short_name, DiagnosticDemProvidedDataMapping):
            element = DiagnosticDemProvidedDataMapping(self, short_name)
            self.addReferrableElement(element)
        return cast(DiagnosticDemProvidedDataMapping, self.getReferrableElement(short_name, DiagnosticDemProvidedDataMapping))

    def createDiagnosticSecurityEventReportingModeMapping(self, short_name: str) -> DiagnosticSecurityEventReportingModeMapping:
        """
        Creates a new DiagnosticSecurityEventReportingModeMapping with the given short name,
        or returns an existing one if it already exists in this package.

        DiagnosticSecurityEventReportingModeMapping: This meta-class represents the ability to associate a location in a DID with a security event. The purpose of this mapping is that the location in the DID contains the setting of the reporting mode for the specific security event. This means that the reporting mode of the security event can be set via the diagnostic service WriteDataByIdentifier..

        Args:
            short_name: The short name for the new DiagnosticSecurityEventReportingModeMapping

        Returns:
            The newly created or existing DiagnosticSecurityEventReportingModeMapping instance
        """
        if not self.IsReferrableElementExists(short_name, DiagnosticSecurityEventReportingModeMapping):
            element = DiagnosticSecurityEventReportingModeMapping(self, short_name)
            self.addReferrableElement(element)
        return cast(DiagnosticSecurityEventReportingModeMapping, self.getReferrableElement(short_name, DiagnosticSecurityEventReportingModeMapping))

    def createDiagnosticAuthTransmitCertificateMapping(self, short_name: str) -> DiagnosticAuthTransmitCertificateMapping:
        """
        Creates a new DiagnosticAuthTransmitCertificateMapping with the given short name,
        or returns an existing one if it already exists in this package.

        DiagnosticAuthTransmitCertificateMapping: This meta-class represents the ability to associate a CryptoServiceCertificate with a DiagnosticAuthCertificateEvaluation with the purpose to configure the evaluation of the certificate..

        Args:
            short_name: The short name for the new DiagnosticAuthTransmitCertificateMapping

        Returns:
            The newly created or existing DiagnosticAuthTransmitCertificateMapping instance
        """
        if not self.IsReferrableElementExists(short_name, DiagnosticAuthTransmitCertificateMapping):
            element = DiagnosticAuthTransmitCertificateMapping(self, short_name)
            self.addReferrableElement(element)
        return cast(DiagnosticAuthTransmitCertificateMapping, self.getReferrableElement(short_name, DiagnosticAuthTransmitCertificateMapping))

    def createDiagnosticEnableCondition(self, short_name: str) -> DiagnosticEnableCondition:
        """
        Creates a new DiagnosticEnableCondition with the given short name,
        or returns an existing one if it already exists in this package.

        DiagnosticEnableCondition: Specification of an enable condition..

        Args:
            short_name: The short name for the new DiagnosticEnableCondition

        Returns:
            The newly created or existing DiagnosticEnableCondition instance
        """
        if not self.IsReferrableElementExists(short_name, DiagnosticEnableCondition):
            element = DiagnosticEnableCondition(self, short_name)
            self.addReferrableElement(element)
        return cast(DiagnosticEnableCondition, self.getReferrableElement(short_name, DiagnosticEnableCondition))

    def createDiagnosticStorageCondition(self, short_name: str) -> DiagnosticStorageCondition:
        """
        Creates a new DiagnosticStorageCondition with the given short name,
        or returns an existing one if it already exists in this package.

        DiagnosticStorageCondition: Specification of a storage condition..

        Args:
            short_name: The short name for the new DiagnosticStorageCondition

        Returns:
            The newly created or existing DiagnosticStorageCondition instance
        """
        if not self.IsReferrableElementExists(short_name, DiagnosticStorageCondition):
            element = DiagnosticStorageCondition(self, short_name)
            self.addReferrableElement(element)
        return cast(DiagnosticStorageCondition, self.getReferrableElement(short_name, DiagnosticStorageCondition))

    def createDiagnosticStorageConditionGroup(self, short_name: str) -> DiagnosticStorageConditionGroup:
        """
        Creates a new DiagnosticStorageConditionGroup with the given short name,
        or returns an existing one if it already exists in this package.

        DiagnosticStorageConditionGroup: Storage condition group which includes one or several storage conditions..

        Args:
            short_name: The short name for the new DiagnosticStorageConditionGroup

        Returns:
            The newly created or existing DiagnosticStorageConditionGroup instance
        """
        if not self.IsReferrableElementExists(short_name, DiagnosticStorageConditionGroup):
            element = DiagnosticStorageConditionGroup(self, short_name)
            self.addReferrableElement(element)
        return cast(DiagnosticStorageConditionGroup, self.getReferrableElement(short_name, DiagnosticStorageConditionGroup))

    def createDiagnosticEnableConditionGroup(self, short_name: str) -> DiagnosticEnableConditionGroup:
        """
        Creates a new DiagnosticEnableConditionGroup with the given short name,
        or returns an existing one if it already exists in this package.

        DiagnosticEnableConditionGroup: Enable condition group which includes one or several enable conditions..

        Args:
            short_name: The short name for the new DiagnosticEnableConditionGroup

        Returns:
            The newly created or existing DiagnosticEnableConditionGroup instance
        """
        if not self.IsReferrableElementExists(short_name, DiagnosticEnableConditionGroup):
            element = DiagnosticEnableConditionGroup(self, short_name)
            self.addReferrableElement(element)
        return cast(DiagnosticEnableConditionGroup, self.getReferrableElement(short_name, DiagnosticEnableConditionGroup))

    def createDiagnosticEnableConditionPortMapping(self, short_name: str) -> DiagnosticEnableConditionPortMapping:
        """
        Creates a new DiagnosticEnableConditionPortMapping with the given short name,
        or returns an existing one if it already exists in this package.

        DiagnosticEnableConditionPortMapping: Defines to which SWC service ports the DiagnosticEnableCondition is mapped..

        Args:
            short_name: The short name for the new DiagnosticEnableConditionPortMapping

        Returns:
            The newly created or existing DiagnosticEnableConditionPortMapping instance
        """
        if not self.IsReferrableElementExists(short_name, DiagnosticEnableConditionPortMapping):
            element = DiagnosticEnableConditionPortMapping(self, short_name)
            self.addReferrableElement(element)
        return cast(DiagnosticEnableConditionPortMapping, self.getReferrableElement(short_name, DiagnosticEnableConditionPortMapping))

    def createDiagnosticOperationCycle(self, short_name: str) -> DiagnosticOperationCycle:
        """
        Creates a new DiagnosticOperationCycle with the given short name,
        or returns an existing one if it already exists in this package.

        DiagnosticOperationCycle: Definition of an operation cycle that is the base of the event qualifying and for Dem scheduling.

        Args:
            short_name: The short name for the new DiagnosticOperationCycle

        Returns:
            The newly created or existing DiagnosticOperationCycle instance
        """
        if not self.IsReferrableElementExists(short_name, DiagnosticOperationCycle):
            element = DiagnosticOperationCycle(self, short_name)
            self.addReferrableElement(element)
        return cast(DiagnosticOperationCycle, self.getReferrableElement(short_name, DiagnosticOperationCycle))

    def createDiagnosticOperationCyclePortMapping(self, short_name: str) -> DiagnosticOperationCyclePortMapping:
        """
        Creates a new DiagnosticOperationCyclePortMapping with the given short name,
        or returns an existing one if it already exists in this package.

        DiagnosticOperationCyclePortMapping: Defines to which SWC service ports the DiagnosticOperationCycle is mapped..

        Args:
            short_name: The short name for the new DiagnosticOperationCyclePortMapping

        Returns:
            The newly created or existing DiagnosticOperationCyclePortMapping instance
        """
        if not self.IsReferrableElementExists(short_name, DiagnosticOperationCyclePortMapping):
            element = DiagnosticOperationCyclePortMapping(self, short_name)
            self.addReferrableElement(element)
        return cast(DiagnosticOperationCyclePortMapping, self.getReferrableElement(short_name, DiagnosticOperationCyclePortMapping))

    def createDiagnosticEvent(self, short_name: str) -> DiagnosticEvent:
        """
        Creates a new DiagnosticEvent with the given short name,
        or returns an existing one if it already exists in this package.

        DiagnosticEvent: This element is used to configure DiagnosticEvents..

        Args:
            short_name: The short name for the new DiagnosticEvent

        Returns:
            The newly created or existing DiagnosticEvent instance
        """
        if not self.IsReferrableElementExists(short_name, DiagnosticEvent):
            element = DiagnosticEvent(self, short_name)
            self.addReferrableElement(element)
        return cast(DiagnosticEvent, self.getReferrableElement(short_name, DiagnosticEvent))

    def createDiagnosticEventPortMapping(self, short_name: str) -> DiagnosticEventPortMapping:
        """
        Creates a new DiagnosticEventPortMapping with the given short name,
        or returns an existing one if it already exists in this package.

        DiagnosticEventPortMapping: Defines to which SWC service ports the DiagnosticEvent is mapped..

        Args:
            short_name: The short name for the new DiagnosticEventPortMapping

        Returns:
            The newly created or existing DiagnosticEventPortMapping instance
        """
        if not self.IsReferrableElementExists(short_name, DiagnosticEventPortMapping):
            element = DiagnosticEventPortMapping(self, short_name)
            self.addReferrableElement(element)
        return cast(DiagnosticEventPortMapping, self.getReferrableElement(short_name, DiagnosticEventPortMapping))

    def createDiagnosticExtendedDataRecord(self, short_name: str) -> DiagnosticExtendedDataRecord:
        """
        Creates a new DiagnosticExtendedDataRecord with the given short name,
        or returns an existing one if it already exists in this package.

        DiagnosticExtendedDataRecord: Description of an extended data record.

        Args:
            short_name: The short name for the new DiagnosticExtendedDataRecord

        Returns:
            The newly created or existing DiagnosticExtendedDataRecord instance
        """
        if not self.IsReferrableElementExists(short_name, DiagnosticExtendedDataRecord):
            element = DiagnosticExtendedDataRecord(self, short_name)
            self.addReferrableElement(element)
        return cast(DiagnosticExtendedDataRecord, self.getReferrableElement(short_name, DiagnosticExtendedDataRecord))

    def createDiagnosticEventToTroubleCodeUdsMapping(self, short_name: str) -> DiagnosticEventToTroubleCodeUdsMapping:
        """
        Creates a new DiagnosticEventToTroubleCodeUdsMapping with the given short name,
        or returns an existing one if it already exists in this package.

        DiagnosticEventToTroubleCodeUdsMapping: Defines which UDS Diagnostic Trouble Code is applicable for a DiagnosticEvent..

        Args:
            short_name: The short name for the new DiagnosticEventToTroubleCodeUdsMapping

        Returns:
            The newly created or existing DiagnosticEventToTroubleCodeUdsMapping instance
        """
        if not self.IsReferrableElementExists(short_name, DiagnosticEventToTroubleCodeUdsMapping):
            element = DiagnosticEventToTroubleCodeUdsMapping(self, short_name)
            self.addReferrableElement(element)
        return cast(DiagnosticEventToTroubleCodeUdsMapping, self.getReferrableElement(short_name, DiagnosticEventToTroubleCodeUdsMapping))

    def createDiagnosticEventToStorageConditionGroupMapping(self, short_name: str) -> DiagnosticEventToStorageConditionGroupMapping:
        """
        Creates a new DiagnosticEventToStorageConditionGroupMapping with the given short name,
        or returns an existing one if it already exists in this package.

        DiagnosticEventToStorageConditionGroupMapping: Defines which StorageConditionGroup is applicable for a DiagnosticEvent..

        Args:
            short_name: The short name for the new DiagnosticEventToStorageConditionGroupMapping

        Returns:
            The newly created or existing DiagnosticEventToStorageConditionGroupMapping instance
        """
        if not self.IsReferrableElementExists(short_name, DiagnosticEventToStorageConditionGroupMapping):
            element = DiagnosticEventToStorageConditionGroupMapping(self, short_name)
            self.addReferrableElement(element)
        return cast(DiagnosticEventToStorageConditionGroupMapping, self.getReferrableElement(short_name, DiagnosticEventToStorageConditionGroupMapping))

    def createDiagnosticEventToOperationCycleMapping(self, short_name: str) -> DiagnosticEventToOperationCycleMapping:
        """
        Creates a new DiagnosticEventToOperationCycleMapping with the given short name,
        or returns an existing one if it already exists in this package.

        DiagnosticEventToOperationCycleMapping: Defines which OperationCycle is applicable for a DiagnosticEvent..

        Args:
            short_name: The short name for the new DiagnosticEventToOperationCycleMapping

        Returns:
            The newly created or existing DiagnosticEventToOperationCycleMapping instance
        """
        if not self.IsReferrableElementExists(short_name, DiagnosticEventToOperationCycleMapping):
            element = DiagnosticEventToOperationCycleMapping(self, short_name)
            self.addReferrableElement(element)
        return cast(DiagnosticEventToOperationCycleMapping, self.getReferrableElement(short_name, DiagnosticEventToOperationCycleMapping))

    def createDiagnosticEventToEnableConditionGroupMapping(self, short_name: str) -> DiagnosticEventToEnableConditionGroupMapping:
        """
        Creates a new DiagnosticEventToEnableConditionGroupMapping with the given short name,
        or returns an existing one if it already exists in this package.

        DiagnosticEventToEnableConditionGroupMapping: Defines which EnableConditionGroup is applicable for a DiagnosticEvent..

        Args:
            short_name: The short name for the new DiagnosticEventToEnableConditionGroupMapping

        Returns:
            The newly created or existing DiagnosticEventToEnableConditionGroupMapping instance
        """
        if not self.IsReferrableElementExists(short_name, DiagnosticEventToEnableConditionGroupMapping):
            element = DiagnosticEventToEnableConditionGroupMapping(self, short_name)
            self.addReferrableElement(element)
        return cast(DiagnosticEventToEnableConditionGroupMapping, self.getReferrableElement(short_name, DiagnosticEventToEnableConditionGroupMapping))

    def createDiagnosticEventToDebounceAlgorithmMapping(self, short_name: str) -> DiagnosticEventToDebounceAlgorithmMapping:
        """
        Creates a new DiagnosticEventToDebounceAlgorithmMapping with the given short name,
        or returns an existing one if it already exists in this package.

        DiagnosticEventToDebounceAlgorithmMapping: Defines which Debounce Algorithm is applicable for a DiagnosticEvent..

        Args:
            short_name: The short name for the new DiagnosticEventToDebounceAlgorithmMapping

        Returns:
            The newly created or existing DiagnosticEventToDebounceAlgorithmMapping instance
        """
        if not self.IsReferrableElementExists(short_name, DiagnosticEventToDebounceAlgorithmMapping):
            element = DiagnosticEventToDebounceAlgorithmMapping(self, short_name)
            self.addReferrableElement(element)
        return cast(DiagnosticEventToDebounceAlgorithmMapping, self.getReferrableElement(short_name, DiagnosticEventToDebounceAlgorithmMapping))

    def createDiagnosticAccessPermission(self, short_name: str) -> DiagnosticAccessPermission:
        """
        Creates a new DiagnosticAccessPermission with the given short name,
        or returns an existing one if it already exists in this package.

        DiagnosticAccessPermission represents the specification of whether a
        given service can be accessed in the diagnostic extract template of
        AUTOSAR.

        Args:
            short_name: The short name for the new DiagnosticAccessPermission

        Returns:
            The newly created or existing DiagnosticAccessPermission instance
        """
        if not self.IsReferrableElementExists(short_name, DiagnosticAccessPermission):
            permission = DiagnosticAccessPermission(self, short_name)
            self.addReferrableElement(permission)
        return cast(DiagnosticAccessPermission, self.getReferrableElement(short_name, DiagnosticAccessPermission))

    def createDltContext(self, short_name: str) -> DltContext:

        if not self.IsReferrableElementExists(short_name, DltContext):
            context = DltContext(self, short_name)
            self.addReferrableElement(context)
        return cast(DltContext, self.getReferrableElement(short_name, DltContext))

    def createDltEcu(self, short_name: str) -> DltEcu:

        if not self.IsReferrableElementExists(short_name, DltEcu):
            ecu = DltEcu(self, short_name)
            self.addReferrableElement(ecu)
        return cast(DltEcu, self.getReferrableElement(short_name, DltEcu))

    def createMultiplexedIPdu(self, short_name: str) -> MultiplexedIPdu:

        if not self.IsReferrableElementExists(short_name, MultiplexedIPdu):
            ipdu = MultiplexedIPdu(self, short_name)
            self.addReferrableElement(ipdu)
        return cast(MultiplexedIPdu, self.getReferrableElement(short_name, MultiplexedIPdu))

    def createUserDefinedIPdu(self, short_name: str) -> UserDefinedIPdu:

        if not self.IsReferrableElementExists(short_name, UserDefinedIPdu):
            ipdu = UserDefinedIPdu(self, short_name)
            self.addReferrableElement(ipdu)
        return cast(UserDefinedIPdu, self.getReferrableElement(short_name, UserDefinedIPdu))

    def createUserDefinedPdu(self, short_name: str) -> UserDefinedPdu:

        if not self.IsReferrableElementExists(short_name, UserDefinedPdu):
            pdu = UserDefinedPdu(self, short_name)
            self.addReferrableElement(pdu)
        return cast(UserDefinedPdu, self.getReferrableElement(short_name, UserDefinedPdu))

    def createGeneralPurposeIPdu(self, short_name: str) -> GeneralPurposeIPdu:

        if not self.IsReferrableElementExists(short_name, GeneralPurposeIPdu):
            i_pdu = GeneralPurposeIPdu(self, short_name)
            self.addReferrableElement(i_pdu)
        return cast(GeneralPurposeIPdu, self.getReferrableElement(short_name, GeneralPurposeIPdu))

    def createGeneralPurposePdu(self, short_name: str) -> GeneralPurposePdu:

        if not self.IsReferrableElementExists(short_name, GeneralPurposePdu):
            pdu = GeneralPurposePdu(self, short_name)
            self.addReferrableElement(pdu)
        return cast(GeneralPurposePdu, self.getReferrableElement(short_name, GeneralPurposePdu))

    def createSecureCommunicationPropsSet(self, short_name: str) -> SecureCommunicationPropsSet:

        if not self.IsReferrableElementExists(short_name, SecureCommunicationPropsSet):
            props_set = SecureCommunicationPropsSet(self, short_name)
            self.addReferrableElement(props_set)
        return cast(SecureCommunicationPropsSet, self.getReferrableElement(short_name, SecureCommunicationPropsSet))

    def createSoAdRoutingGroup(self, short_name: str) -> SoAdRoutingGroup:

        if not self.IsReferrableElementExists(short_name, SoAdRoutingGroup):
            group = SoAdRoutingGroup(self, short_name)
            self.addReferrableElement(group)
        return cast(SoAdRoutingGroup, self.getReferrableElement(short_name, SoAdRoutingGroup))

    def createTcpOptionFilterSet(self, short_name: str) -> TcpOptionFilterSet:

        if not self.IsReferrableElementExists(short_name, TcpOptionFilterSet):
            tcp_option_filter_set = TcpOptionFilterSet(self, short_name)
            self.addReferrableElement(tcp_option_filter_set)
        return cast(TcpOptionFilterSet, self.getReferrableElement(short_name, TcpOptionFilterSet))

    def createIPv6ExtHeaderFilterSet(self, short_name: str) -> IPv6ExtHeaderFilterSet:

        if not self.IsReferrableElementExists(short_name, IPv6ExtHeaderFilterSet):
            ipv6_ext_header_filter_set = IPv6ExtHeaderFilterSet(self, short_name)
            self.addReferrableElement(ipv6_ext_header_filter_set)
        return cast(IPv6ExtHeaderFilterSet, self.getReferrableElement(short_name, IPv6ExtHeaderFilterSet))

    def createDdsConfig(self, short_name: str) -> DdsCpConfig:
        if not self.IsReferrableElementExists(short_name, DdsCpConfig):
            config = DdsCpConfig(self, short_name)
            self.addReferrableElement(config)
        return cast(DdsCpConfig, self.getReferrableElement(short_name, DdsCpConfig))

    def createCanXlProps(self, short_name: str) -> CanXlProps:

        if not self.IsReferrableElementExists(short_name, CanXlProps):
            can_xl_props = CanXlProps(self, short_name)
            self.addReferrableElement(can_xl_props)
        return cast(CanXlProps, self.getReferrableElement(short_name, CanXlProps))

    def createSomeipSdClientServiceInstanceConfig(self, short_name: str) -> SomeipSdClientServiceInstanceConfig:

        if not self.IsReferrableElementExists(short_name, SomeipSdClientServiceInstanceConfig):
            config = SomeipSdClientServiceInstanceConfig(self, short_name)
            self.addReferrableElement(config)
        return cast(SomeipSdClientServiceInstanceConfig, self.getReferrableElement(short_name, SomeipSdClientServiceInstanceConfig))

    def createServiceInstanceCollectionSet(self, short_name: str) -> ServiceInstanceCollectionSet:

        if not self.IsReferrableElementExists(short_name, ServiceInstanceCollectionSet):
            collection_set = ServiceInstanceCollectionSet(self, short_name)
            self.addReferrableElement(collection_set)
        return cast(ServiceInstanceCollectionSet, self.getReferrableElement(short_name, ServiceInstanceCollectionSet))

    def createSocketConnectionIpduIdentifierSet(self, short_name: str) -> SocketConnectionIpduIdentifierSet:

        if not self.IsReferrableElementExists(short_name, SocketConnectionIpduIdentifierSet):
            identifier_set = SocketConnectionIpduIdentifierSet(self, short_name)
            self.addReferrableElement(identifier_set)
        return cast(SocketConnectionIpduIdentifierSet, self.getReferrableElement(short_name, SocketConnectionIpduIdentifierSet))

    def createSomeipSdServerServiceInstanceConfig(self, short_name: str) -> SomeipSdServerServiceInstanceConfig:

        if not self.IsReferrableElementExists(short_name, SomeipSdServerServiceInstanceConfig):
            config = SomeipSdServerServiceInstanceConfig(self, short_name)
            self.addReferrableElement(config)
        return cast(SomeipSdServerServiceInstanceConfig, self.getReferrableElement(short_name, SomeipSdServerServiceInstanceConfig))

    def createSomeipSdClientEventGroupTimingConfig(self, short_name: str) -> SomeipSdClientEventGroupTimingConfig:

        if not self.IsReferrableElementExists(short_name, SomeipSdClientEventGroupTimingConfig):
            config = SomeipSdClientEventGroupTimingConfig(self, short_name)
            self.addReferrableElement(config)
        return cast(SomeipSdClientEventGroupTimingConfig, self.getReferrableElement(short_name, SomeipSdClientEventGroupTimingConfig))

    def createSomeipSdServerEventGroupTimingConfig(self, short_name: str) -> SomeipSdServerEventGroupTimingConfig:

        if not self.IsReferrableElementExists(short_name, SomeipSdServerEventGroupTimingConfig):
            config = SomeipSdServerEventGroupTimingConfig(self, short_name)
            self.addReferrableElement(config)
        return cast(SomeipSdServerEventGroupTimingConfig, self.getReferrableElement(short_name, SomeipSdServerEventGroupTimingConfig))

    def createDoIpTpConfig(self, short_name: str) -> DoIpTpConfig:

        if not self.IsReferrableElementExists(short_name, DoIpTpConfig):
            tp_config = DoIpTpConfig(self, short_name)
            self.addReferrableElement(tp_config)
        return cast(DoIpTpConfig, self.getReferrableElement(short_name, DoIpTpConfig))

    def createHwElement(self, short_name: str) -> HwElement:

        if not self.IsReferrableElementExists(short_name, HwElement):
            hw_element = HwElement(self, short_name)
            self.addReferrableElement(hw_element)
        return cast(HwElement, self.getReferrableElement(short_name, HwElement))

    def createHwCategory(self, short_name: str) -> HwCategory:

        if not self.IsReferrableElementExists(short_name, HwCategory):
            hw_category = HwCategory(self, short_name)
            self.addReferrableElement(hw_category)
        return cast(HwCategory, self.getReferrableElement(short_name, HwCategory))

    def createHwType(self, short_name: str) -> HwType:

        if not self.IsReferrableElementExists(short_name, HwType):
            hw_category = HwType(self, short_name)
            self.addReferrableElement(hw_category)
        return cast(HwType, self.getReferrableElement(short_name, HwType))

    def createFlexrayFrame(self, short_name: str) -> FlexrayFrame:

        if not self.IsReferrableElementExists(short_name, FlexrayFrame):
            frame = FlexrayFrame(self, short_name)
            self.addReferrableElement(frame)
        return cast(FlexrayFrame, self.getReferrableElement(short_name, FlexrayFrame))

    def createFlexrayCluster(self, short_name: str) -> FlexrayCluster:

        if not self.IsReferrableElementExists(short_name, FlexrayCluster):
            frame = FlexrayCluster(self, short_name)
            self.addReferrableElement(frame)
        return cast(FlexrayCluster, self.getReferrableElement(short_name, FlexrayCluster))

    def createDataTransformationSet(self, short_name: str) -> DataTransformationSet:

        if not self.IsReferrableElementExists(short_name, DataTransformationSet):
            transform_set = DataTransformationSet(self, short_name)
            self.addReferrableElement(transform_set)
        return cast(DataTransformationSet, self.getReferrableElement(short_name, DataTransformationSet))

    def createE2EProfileCompatibilityProps(self, short_name: str) -> E2EProfileCompatibilityProps:

        if not self.IsReferrableElementExists(short_name, E2EProfileCompatibilityProps):
            props = E2EProfileCompatibilityProps(self, short_name)
            self.addReferrableElement(props)
        return cast(E2EProfileCompatibilityProps, self.getReferrableElement(short_name, E2EProfileCompatibilityProps))

    def createSwAxisType(self, short_name: str) -> SwAxisType:

        if not self.IsReferrableElementExists(short_name, SwAxisType):
            axis_type = SwAxisType(self, short_name)
            self.addReferrableElement(axis_type)
        return cast(SwAxisType, self.getReferrableElement(short_name, SwAxisType))

    def createTlvDataIdDefinitionSet(self, short_name: str) -> TlvDataIdDefinitionSet:

        if not self.IsReferrableElementExists(short_name, TlvDataIdDefinitionSet):
            tlv_data_id_definition_set = TlvDataIdDefinitionSet(self, short_name)
            self.addReferrableElement(tlv_data_id_definition_set)
        return cast(TlvDataIdDefinitionSet, self.getReferrableElement(short_name, TlvDataIdDefinitionSet))

    def createCollection(self, short_name: str) -> Collection:
        from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ElementCollection import Collection

        if not self.IsReferrableElementExists(short_name, Collection):
            collection = Collection(self, short_name)
            self.addReferrableElement(collection)
        return cast(Collection, self.getReferrableElement(short_name, Collection))

    def createApplicationInterface(self, short_name: str) -> ApplicationInterface:
        from armodel.models.M2.AUTOSARTemplates.AbstractPlatform import ApplicationInterface

        if not self.IsReferrableElementExists(short_name, ApplicationInterface):
            interface = ApplicationInterface(self, short_name)
            self.addReferrableElement(interface)
        return cast(ApplicationInterface, self.getReferrableElement(short_name, ApplicationInterface))

    def createAliasNameSet(self, short_name: str) -> AliasNameSet:
        from armodel.models.M2.AUTOSARTemplates.CommonStructure.FlatMap import AliasNameSet

        if not self.IsReferrableElementExists(short_name, AliasNameSet):
            alias_name_set = AliasNameSet(self, short_name)
            self.addReferrableElement(alias_name_set)
        return cast(AliasNameSet, self.getReferrableElement(short_name, AliasNameSet))

    def createKeywordSet(self, short_name: str) -> KeywordSet:

        if not self.IsReferrableElementExists(short_name, KeywordSet):
            keyword_set = KeywordSet(self, short_name)
            self.addReferrableElement(keyword_set)
        return cast(KeywordSet, self.getReferrableElement(short_name, KeywordSet))

    def createPortPrototypeBlueprint(self, short_name: str) -> PortPrototypeBlueprint:

        if not self.IsReferrableElementExists(short_name, PortPrototypeBlueprint):
            keyword_set = PortPrototypeBlueprint(self, short_name)
            self.addReferrableElement(keyword_set)
        return cast(PortPrototypeBlueprint, self.getReferrableElement(short_name, PortPrototypeBlueprint))

    def createModeDeclarationMappingSet(self, short_name: str) -> ModeDeclarationMappingSet:

        if not self.IsReferrableElementExists(short_name, ModeDeclarationMappingSet):
            mapping_set = ModeDeclarationMappingSet(self, short_name)
            self.addReferrableElement(mapping_set)
        return cast(ModeDeclarationMappingSet, self.getReferrableElement(short_name, ModeDeclarationMappingSet))

    def createAclPermission(self, short_name: str) -> AclPermission:

        if not self.IsReferrableElementExists(short_name, AclPermission):
            acl_permission = AclPermission(self, short_name)
            self.addReferrableElement(acl_permission)
        return cast(AclPermission, self.getReferrableElement(short_name, AclPermission))

    def createAclObjectSet(self, short_name: str) -> AclObjectSet:

        if not self.IsReferrableElementExists(short_name, AclObjectSet):
            acl_object_set = AclObjectSet(self, short_name)
            self.addReferrableElement(acl_object_set)
        return cast(AclObjectSet, self.getReferrableElement(short_name, AclObjectSet))

    def createAclOperation(self, short_name: str) -> AclOperation:

        if not self.IsReferrableElementExists(short_name, AclOperation):
            acl_operation = AclOperation(self, short_name)
            self.addReferrableElement(acl_operation)
        return cast(AclOperation, self.getReferrableElement(short_name, AclOperation))

    def createAclRole(self, short_name: str) -> AclRole:

        if not self.IsReferrableElementExists(short_name, AclRole):
            acl_role = AclRole(self, short_name)
            self.addReferrableElement(acl_role)
        return cast(AclRole, self.getReferrableElement(short_name, AclRole))

    def createLifeCycleStateDefinitionGroup(self, short_name: str) -> LifeCycleStateDefinitionGroup:

        if not self.IsReferrableElementExists(short_name, LifeCycleStateDefinitionGroup):
            group = LifeCycleStateDefinitionGroup(self, short_name)
            self.addReferrableElement(group)
        return cast(LifeCycleStateDefinitionGroup, self.getReferrableElement(short_name, LifeCycleStateDefinitionGroup))

    def createViewMapSet(self, short_name: str) -> ViewMapSet:

        if not self.IsReferrableElementExists(short_name, ViewMapSet):
            view_map_set = ViewMapSet(self, short_name)
            self.addReferrableElement(view_map_set)
        return cast(ViewMapSet, self.getReferrableElement(short_name, ViewMapSet))

    def createRapidPrototypingScenario(self, short_name: str) -> RapidPrototypingScenario:

        if not self.IsReferrableElementExists(short_name, RapidPrototypingScenario):
            scenario = RapidPrototypingScenario(self, short_name)
            self.addReferrableElement(scenario)
        return cast(RapidPrototypingScenario, self.getReferrableElement(short_name, RapidPrototypingScenario))

    def getApplicationPrimitiveDataTypes(self) -> List[ApplicationPrimitiveDataType]:

        return list(sorted((a for a in self.referrableElements if isinstance(a, ApplicationPrimitiveDataType)), key=lambda o: o.short_name))

    def getApplicationDataType(self) -> List[ApplicationDataType]:

        return list(sorted((a for a in self.referrableElements if isinstance(a, ApplicationDataType)), key=lambda o: o.short_name))

    def getImplementationDataTypes(self) -> List[ImplementationDataType]:

        return list(sorted((a for a in self.referrableElements if isinstance(a, ImplementationDataType)), key=lambda o: o.short_name))

    def getSwBaseTypes(self) -> List[SwBaseType]:

        return list(a for a in self.referrableElements if isinstance(a, SwBaseType))

    def getSwComponentTypes(self) -> List[SwComponentType]:

        return list(a for a in self.referrableElements if isinstance(a, SwComponentType))

    def getSensorActuatorSwComponentType(self) -> List[SensorActuatorSwComponentType]:

        return list(a for a in self.referrableElements if isinstance(a, SensorActuatorSwComponentType))

    def getAtomicSwComponentTypes(self) -> List[AtomicSwComponentType]:

        return list(a for a in self.referrableElements if isinstance(a, AtomicSwComponentType))

    def getCompositionSwComponentTypes(self) -> List[CompositionSwComponentType]:

        return list(a for a in self.referrableElements if isinstance(a, CompositionSwComponentType))

    def getComplexDeviceDriverSwComponentTypes(self) -> List[ComplexDeviceDriverSwComponentType]:

        return list(sorted((a for a in self.referrableElements if isinstance(a, ComplexDeviceDriverSwComponentType)), key=lambda a: a.short_name))

    def getSenderReceiverInterfaces(self) -> List[SenderReceiverInterface]:

        return list(sorted((a for a in self.referrableElements if isinstance(a, SenderReceiverInterface)), key=lambda a: a.short_name))

    def getParameterInterfaces(self) -> List[ParameterInterface]:

        return list(sorted((a for a in self.referrableElements if isinstance(a, ParameterInterface)), key=lambda a: a.short_name))

    def getClientServerInterfaces(self) -> List[ClientServerInterface]:

        return list(sorted((a for a in self.referrableElements if isinstance(a, ClientServerInterface)), key=lambda a: a.short_name))

    def getDataTypeMappingSets(self) -> List[DataTypeMappingSet]:

        return list(sorted((a for a in self.referrableElements if isinstance(a, DataTypeMappingSet)), key=lambda a: a.short_name))

    def getCompuMethods(self) -> List[CompuMethod]:

        return list(a for a in self.referrableElements if isinstance(a, CompuMethod))

    def getBswModuleDescriptions(self) -> List[BswModuleDescription]:

        return list(a for a in self.referrableElements if isinstance(a, BswModuleDescription))

    def getBswModuleEntries(self) -> List[BswModuleEntry]:

        return list(a for a in self.referrableElements if isinstance(a, BswModuleEntry))

    def getBswImplementations(self) -> List[BswImplementation]:

        return list(a for a in self.referrableElements if isinstance(a, BswImplementation))

    def getSwcImplementations(self) -> List[SwcImplementation]:

        return list(a for a in self.referrableElements if isinstance(a, SwcImplementation))

    def getImplementations(self) -> List[Implementation]:

        return list(a for a in self.referrableElements if isinstance(a, Implementation))

    def getSwcBswMappings(self) -> List[SwcBswMapping]:

        return list(a for a in self.referrableElements if isinstance(a, SwcBswMapping))

    def getBswEntryRelationshipSets(self) -> List[BswEntryRelationshipSet]:

        return list(a for a in self.referrableElements if isinstance(a, BswEntryRelationshipSet))

    def getMcFunctions(self) -> List[McFunction]:
        """
        Gets the McFunction elements contained in this package.

        Returns:
            List of McFunction instances
        """

        return list(a for a in self.referrableElements if isinstance(a, McFunction))

    def getMcGroups(self) -> List[McGroup]:
        """
        Gets the McGroup elements contained in this package.

        Returns:
            List of McGroup instances
        """

        return list(a for a in self.referrableElements if isinstance(a, McGroup))

    def getConstantSpecifications(self) -> List[ConstantSpecification]:

        return list(a for a in self.referrableElements if isinstance(a, ConstantSpecification))

    def getDataConstrs(self) -> List[DataConstr]:

        return list(a for a in self.referrableElements if isinstance(a, DataConstr))

    def getUnits(self) -> List[Unit]:

        return list(a for a in self.referrableElements if isinstance(a, Unit))

    def getPhysicalDimensionMappingSets(self) -> List[PhysicalDimensionMappingSet]:

        return list(a for a in self.referrableElements if isinstance(a, PhysicalDimensionMappingSet))

    def getCalibrationParameterValueSets(self) -> List[CalibrationParameterValueSet]:

        return list(a for a in self.referrableElements if isinstance(a, CalibrationParameterValueSet))

    def getUnitGroups(self) -> List[UnitGroup]:

        return list(a for a in self.referrableElements if isinstance(a, UnitGroup))

    def getApplicationArrayDataTypes(self) -> List[ApplicationArrayDataType]:

        return list(sorted((a for a in self.referrableElements if isinstance(a, ApplicationArrayDataType)), key=lambda a: a.short_name))

    def getSwRecordLayouts(self) -> List[SwRecordLayout]:

        return list(sorted((a for a in self.referrableElements if isinstance(a, SwRecordLayout)), key=lambda a: a.short_name))

    def getSwAddrMethods(self) -> List[SwAddrMethod]:

        return list(sorted((a for a in self.referrableElements if isinstance(a, SwAddrMethod)), key=lambda a: a.short_name))

    def getTriggerInterfaces(self) -> List[TriggerInterface]:

        return list(sorted((a for a in self.referrableElements if isinstance(a, TriggerInterface)), key=lambda a: a.short_name))

    def getModeDeclarationGroups(self) -> List[ModeDeclarationGroup]:

        return list(sorted((a for a in self.referrableElements if isinstance(a, ModeDeclarationGroup)), key=lambda a: a.short_name))

    def getModeSwitchInterfaces(self) -> List[ModeSwitchInterface]:

        return list(sorted((a for a in self.referrableElements if isinstance(a, ModeSwitchInterface)), key=lambda a: a.short_name))

    def getSwcTimings(self) -> List[SwcTiming]:

        return list(sorted((a for a in self.referrableElements if isinstance(a, SwcTiming)), key=lambda a: a.short_name))

    def getLinClusters(self) -> List[LinCluster]:

        return list(sorted((a for a in self.referrableElements if isinstance(a, LinCluster)), key=lambda a: a.short_name))

    def getCanClusters(self) -> List[CanCluster]:

        return list(sorted((a for a in self.referrableElements if isinstance(a, CanCluster)), key=lambda a: a.short_name))

    def getLinUnconditionalFrames(self) -> List[LinUnconditionalFrame]:

        return list(sorted((a for a in self.referrableElements if isinstance(a, LinUnconditionalFrame)), key=lambda a: a.short_name))

    def getNmPdus(self) -> List[NmPdu]:

        return list(sorted((a for a in self.referrableElements if isinstance(a, NmPdu)), key=lambda a: a.short_name))

    def getNPdus(self) -> List[NPdu]:

        return list(sorted((a for a in self.referrableElements if isinstance(a, NPdu)), key=lambda a: a.short_name))

    def getDcmIPdus(self) -> List[DcmIPdu]:

        return list(sorted((a for a in self.referrableElements if isinstance(a, DcmIPdu)), key=lambda a: a.short_name))

    def getSecuredIPdus(self) -> List[SecuredIPdu]:

        return list(sorted((a for a in self.referrableElements if isinstance(a, SecuredIPdu)), key=lambda a: a.short_name))

    def getContainerIPdus(self) -> List[ContainerIPdu]:

        return list(sorted((a for a in self.referrableElements if isinstance(a, ContainerIPdu)), key=lambda a: a.short_name))

    def getNmConfigs(self) -> List[NmConfig]:

        return list(sorted((a for a in self.referrableElements if isinstance(a, NmConfig)), key=lambda a: a.short_name))

    def getCanTpConfigs(self) -> List[CanTpConfig]:

        return list(sorted((a for a in self.referrableElements if isinstance(a, CanTpConfig)), key=lambda a: a.short_name))

    def getCanFrames(self) -> List[CanFrame]:

        return list(sorted((a for a in self.referrableElements if isinstance(a, CanFrame)), key=lambda a: a.short_name))

    def getEcuInstances(self) -> List[EcuInstance]:

        return list(sorted((a for a in self.referrableElements if isinstance(a, EcuInstance)), key=lambda a: a.short_name))

    def getGateways(self) -> List[Gateway]:

        return list(sorted((a for a in self.referrableElements if isinstance(a, Gateway)), key=lambda a: a.short_name))

    def getISignals(self) -> List[ISignal]:

        return list(sorted((a for a in self.referrableElements if isinstance(a, ISignal)), key=lambda a: a.short_name))

    def getEcucValueCollections(self) -> List[EcucValueCollection]:

        return list(sorted((a for a in self.referrableElements if isinstance(a, EcucValueCollection)), key=lambda a: a.short_name))

    def getEcucModuleConfigurationValues(self) -> List[EcucModuleConfigurationValues]:

        return list(sorted((a for a in self.referrableElements if isinstance(a, EcucModuleConfigurationValues)), key=lambda a: a.short_name))

    def getEcucModuleDefs(self) -> List[EcucModuleDef]:

        return list(sorted((a for a in self.referrableElements if isinstance(a, EcucModuleDef)), key=lambda a: a.short_name))

    def getEcucDefinitionCollections(self) -> List[EcucDefinitionCollection]:

        return list(sorted((a for a in self.referrableElements if isinstance(a, EcucDefinitionCollection)), key=lambda a: a.short_name))

    def getSwSystemConsts(self) -> List[SwSystemconst]:

        return list(sorted((a for a in self.referrableElements if isinstance(a, SwSystemconst)), key=lambda a: a.short_name))

    def getSwSystemconstantValueSets(self) -> List[SwSystemconstantValueSet]:

        return list(sorted((a for a in self.referrableElements if isinstance(a, SwSystemconstantValueSet)), key=lambda a: a.short_name))

    def getPredefinedVariants(self) -> List[PredefinedVariant]:

        return list(
            sorted(
                (a for a in self.referrableElements if isinstance(a, PredefinedVariant)),
                key=lambda a: a.short_name,
            )
        )

    def getPostBuildVariantCriterions(self) -> List[PostBuildVariantCriterion]:

        return list(
            sorted(
                (a for a in self.referrableElements if isinstance(a, PostBuildVariantCriterion)),
                key=lambda a: a.short_name,
            )
        )

    def getEcucPhysicalDimensions(self) -> List[PhysicalDimension]:

        return list(sorted((a for a in self.referrableElements if isinstance(a, PhysicalDimension)), key=lambda a: a.short_name))

    def getISignalGroups(self) -> List[ISignalGroup]:

        return list(sorted((a for a in self.referrableElements if isinstance(a, ISignalGroup)), key=lambda a: a.short_name))

    def getSystemSignals(self) -> List[SystemSignal]:

        return list(sorted((a for a in self.referrableElements if isinstance(a, SystemSignal)), key=lambda a: a.short_name))

    def getSystemSignalGroups(self) -> List[SystemSignalGroup]:

        return list(sorted((a for a in self.referrableElements if isinstance(a, SystemSignalGroup)), key=lambda a: a.short_name))

    def getISignalIPdus(self) -> List[ISignalIPdu]:

        return list(sorted((a for a in self.referrableElements if isinstance(a, ISignalIPdu)), key=lambda a: a.short_name))

    def getSystems(self) -> List[System]:

        return list(sorted((a for a in self.referrableElements if isinstance(a, System)), key=lambda a: a.short_name))

    def getHwElements(self) -> List[HwElement]:

        return list(sorted((a for a in self.referrableElements if isinstance(a, HwElement)), key=lambda a: a.short_name))

    def getHwCategories(self) -> List[HwCategory]:

        return list(sorted((a for a in self.referrableElements if isinstance(a, HwCategory)), key=lambda a: a.short_name))

    def getFlexrayFrames(self) -> List[FlexrayFrame]:

        return list(sorted((a for a in self.referrableElements if isinstance(a, FlexrayFrame)), key=lambda a: a.short_name))

    def getDataTransformationSets(self) -> List[DataTransformationSet]:

        return list(sorted((a for a in self.referrableElements if isinstance(a, DataTransformationSet)), key=lambda a: a.short_name))

    def getCollections(self) -> List[Collection]:
        from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ElementCollection import Collection

        return list(sorted((a for a in self.referrableElements if isinstance(a, Collection)), key=lambda a: a.short_name))

    def getKeywordSets(self) -> List[KeywordSet]:

        return list(sorted((a for a in self.referrableElements if isinstance(a, KeywordSet)), key=lambda a: a.short_name))

    def getPortPrototypeBlueprints(self) -> List[PortPrototypeBlueprint]:

        return list(sorted((a for a in self.referrableElements if isinstance(a, PortPrototypeBlueprint)), key=lambda a: a.short_name))

    def getModeDeclarationMappingSets(self) -> List[ModeDeclarationMappingSet]:

        return list(sorted((a for a in self.referrableElements if isinstance(a, ModeDeclarationMappingSet)), key=lambda a: a.short_name))

    def getAclPermissions(self) -> List[AclPermission]:

        return list(sorted((a for a in self.referrableElements if isinstance(a, AclPermission)), key=lambda a: a.short_name))

    def getAclObjectSets(self) -> List[AclObjectSet]:

        return list(sorted((a for a in self.referrableElements if isinstance(a, AclObjectSet)), key=lambda a: a.short_name))

    def getAclOperations(self) -> List[AclOperation]:

        return list(sorted((a for a in self.referrableElements if isinstance(a, AclOperation)), key=lambda a: a.short_name))

    def getAclRoles(self) -> List[AclRole]:

        return list(sorted((a for a in self.referrableElements if isinstance(a, AclRole)), key=lambda a: a.short_name))

    def getLifeCycleStateDefinitionGroups(self) -> List[LifeCycleStateDefinitionGroup]:

        return list(sorted((a for a in self.referrableElements if isinstance(a, LifeCycleStateDefinitionGroup)), key=lambda a: a.short_name))

    def getViewMapSets(self) -> List[ViewMapSet]:

        return list(sorted((a for a in self.referrableElements if isinstance(a, ViewMapSet)), key=lambda a: a.short_name))

    def getRapidPrototypingScenarios(self) -> List[RapidPrototypingScenario]:

        return list(sorted((a for a in self.referrableElements if isinstance(a, RapidPrototypingScenario)), key=lambda a: a.short_name))

    def getReferenceBases(self) -> List[ReferenceBase]:
        """
        This denotes the reference bases for the package. This is the basis for all relative references within the package. The base needs to be selected according to the base attribute within the references.
        """
        return self.referenceBases

    def addReferenceBase(self, value: Optional[ReferenceBase]) -> ARPackage:
        """
        This denotes the reference bases for the package. This is the basis for all relative references within the package. The base needs to be selected according to the base attribute within the references. A None value is a no-op and does not append to referenceBases.
        """
        if value is not None:
            self.referenceBases.append(value)
        return self


# Element-class names are re-exported eagerly. Every models/ module that imports
# from this module only needs ARElement/PackageableElement, which are defined above,
# so partial-module initialization resolves the cycle without lazy machinery.
from armodel.models.M2.AUTOSARTemplates.AdaptivePlatform.PlatformModuleDeployment.AdaptiveModuleImplementation import PlatformModuleEthernetEndpointConfiguration  # noqa: E402
from armodel.models.M2.AUTOSARTemplates.AdaptivePlatform.PlatformModuleDeployment.Firewall import FirewallRule, StateDependentFirewall  # noqa: E402
from armodel.models.M2.AUTOSARTemplates.BswModuleTemplate.BswImplementation import BswImplementation  # noqa: E402
from armodel.models.M2.AUTOSARTemplates.BswModuleTemplate.BswInterfaces import BswEntryRelationshipSet  # noqa: E402
from armodel.models.M2.AUTOSARTemplates.BswModuleTemplate.BswInterfaces import BswModuleEntry  # noqa: E402
from armodel.models.M2.AUTOSARTemplates.BswModuleTemplate.BswOverview import BswModuleDescription  # noqa: E402
from armodel.models.M2.AUTOSARTemplates.CommonStructure import ConstantSpecification  # noqa: E402
from armodel.models.M2.AUTOSARTemplates.CommonStructure.Constants import ConstantSpecificationMappingSet  # noqa: E402
from armodel.models.M2.AUTOSARTemplates.CommonStructure.FlatMap import FlatMap  # noqa: E402
from armodel.models.M2.AUTOSARTemplates.CommonStructure.StandardizationTemplate.BlueprintMapping import (  # noqa: E402
    BlueprintMappingSet,
)
from armodel.models.M2.AUTOSARTemplates.CommonStructure.Implementation import Implementation  # noqa: E402
from armodel.models.M2.AUTOSARTemplates.CommonStructure.ImplementationDataTypes import ImplementationDataType  # noqa: E402
from armodel.models.M2.AUTOSARTemplates.CommonStructure.McGroups import McGroup  # noqa: E402
from armodel.models.M2.AUTOSARTemplates.CommonStructure.MeasurementCalibrationSupport import McFunction  # noqa: E402
from armodel.models.M2.AUTOSARTemplates.CommonStructure.ModeDeclaration import ModeDeclarationGroup  # noqa: E402
from armodel.models.M2.AUTOSARTemplates.CommonStructure.ServiceNeeds import DiagnosticIndicatorTypeEnum  # noqa: E402
from armodel.models.M2.AUTOSARTemplates.CommonStructure.SignalServiceTranslation import SignalServiceTranslationPropsSet  # noqa: E402
from armodel.models.M2.AUTOSARTemplates.CommonStructure.StandardizationTemplate.BlueprintDedicated.PortPrototypeBlueprint import PortPrototypeBlueprint  # noqa: E402
from armodel.models.M2.AUTOSARTemplates.CommonStructure.StandardizationTemplate.Keyword import KeywordSet  # noqa: E402
from armodel.models.M2.AUTOSARTemplates.CommonStructure.SwcBswMapping import SwcBswMapping  # noqa: E402
from armodel.models.M2.AUTOSARTemplates.CommonStructure.Timing.TimingExtensions import BswCompositionTiming, BswModuleTiming, EcuTiming, SwcTiming, SystemTiming, VfbTiming  # noqa: E402
from armodel.models.M2.AUTOSARTemplates.CommonStructure.Timing.TimingCpSoftwareCluster import TDCpSoftwareClusterMappingSet  # noqa: E402
from armodel.models.M2.AUTOSARTemplates.DiagnosticExtract.CommonService import DiagnosticAuthenticationClass  # noqa: E402
from armodel.models.M2.AUTOSARTemplates.DiagnosticExtract.CommonService import DiagnosticCustomServiceClass, DiagnosticServiceInstance, DiagnosticSessionControlClass  # noqa: E402
from armodel.models.M2.AUTOSARTemplates.DiagnosticExtract.CommonService import DiagnosticEcuResetClass  # noqa: E402
from armodel.models.M2.AUTOSARTemplates.DiagnosticExtract.CommonService import DiagnosticSecurityAccessClass  # noqa: E402
from armodel.models.M2.AUTOSARTemplates.DiagnosticExtract.CommonDiagnostics import DiagnosticCommonElement  # noqa: E402
from armodel.models.M2.AUTOSARTemplates.DiagnosticExtract.DiagnosticContribution import DiagnosticServiceTable  # noqa: E402
from armodel.models.M2.AUTOSARTemplates.ECUCDescriptionTemplate import (  # noqa: E402
    EcucModuleConfigurationValues,
    EcucValueCollection,
    ModuleConfiguration,
)
from armodel.models.M2.AUTOSARTemplates.ECUCParameterDefTemplate import (  # noqa: E402
    EcucDefinitionCollection,
    EcucDestinationUriDefSet,
    EcucModuleDef,
)
from armodel.models.M2.AUTOSARTemplates.EcuResourceTemplate import HwElement  # noqa: E402
from armodel.models.M2.AUTOSARTemplates.EcuResourceTemplate.HwElementCategory import (  # noqa: E402
    HwCategory,
    HwType,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.DocumentationOnM1 import Documentation  # noqa: E402
from armodel.models.M2.AUTOSARTemplates.GenericStructure.LifeCycles import LifeCycleInfoSet  # noqa: E402
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.SpecialDataDef import (  # noqa: E402
    SdgDef,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.VariantHandling import (  # noqa: E402
    EvaluatedVariantSet,
    PostBuildVariantCriterion,
    PredefinedVariant,
    SwSystemconstantValueSet,
)
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.Components import (  # noqa: E402
    ApplicationSwComponentType,
    AtomicSwComponentType,
    ComplexDeviceDriverSwComponentType,
    EcuAbstractionSwComponentType,
    NvBlockSwComponentType,
    ParameterSwComponentType,
    SensorActuatorSwComponentType,
    ServiceProxySwComponentType,
    ServiceSwComponentType,
    SwComponentType,
)
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.Composition import CompositionSwComponentType  # noqa: E402
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.Datatype.Datatypes import (  # noqa: E402
    ApplicationArrayDataType,
    ApplicationDataType,
    ApplicationPrimitiveDataType,
    ApplicationRecordDataType,
    DataTypeMappingSet,
)
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.EndToEndProtection import EndToEndProtectionSet  # noqa: E402
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.ImplicitCommunicationBehavior import (  # noqa: E402
    ConsistencyNeeds,
    DataPrototypeGroup,
    RunnableEntityGroup,
)
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.PortInterface import (  # noqa: E402
    ClientServerInterface,
    ModeDeclarationMappingSet,
    ModeSwitchInterface,
    NvDataInterface,
    ParameterInterface,
    PortInterfaceMappingSet,
    SenderReceiverInterface,
    TriggerInterface,
)
from armodel.models.M2.AUTOSARTemplates.LogAndTraceExtract import DltContext, DltEcu  # noqa: E402
from armodel.models.M2.AUTOSARTemplates.DiagnosticExtract.Dcm import DiagnosticAccessPermission, DiagnosticSecurityLevel, DiagnosticSession  # noqa: E402
from armodel.models.M2.AUTOSARTemplates.DiagnosticExtract.EnvironmentalCondition import DiagnosticEnvironmentalCondition  # noqa: E402
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.MeasurementAndCalibration.InterpolationRoutineMappingSet import InterpolationRoutineMappingSet  # noqa: E402
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.SwcImplementation import SwcImplementation  # noqa: E402
from armodel.models.M2.AUTOSARTemplates.SystemTemplate import ClientIdDefinitionSet, CpSoftwareCluster, CpSoftwareClusterMappingSet, System  # noqa: E402
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.DiagnosticConnection import DiagnosticConnection  # noqa: E402
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.RteEventToOsTaskMapping import OsTaskProxy  # noqa: E402
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.SWmapping import ApplicationPartition, J1939ControllerApplication  # noqa: E402
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Can.CanCommunication import CanFrame  # noqa: E402
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Can.CanTopology import CanXlProps, J1939Cluster  # noqa: E402
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Ethernet.EthernetFrame import GenericEthernetFrame  # noqa: E402
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Ethernet.EthernetTopology import CouplingElement, EthIpProps, EthTcpIpIcmpProps, EthernetCluster, EthTcpIpProps  # noqa: E402
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Ethernet.EthernetTopology import EthernetWakeupSleepOnDatalineConfigSet  # noqa: E402
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Ethernet.ObsoleteModel import SoAdRoutingGroup  # noqa: E402
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Ethernet.ServiceInstances import (  # noqa: E402
    ConsumedProvidedServiceInstanceGroup,
    SomeipSdClientEventGroupTimingConfig,
    SomeipSdClientServiceInstanceConfig,
    SomeipSdServerEventGroupTimingConfig,
    SomeipSdServerServiceInstanceConfig,
    ServiceInstanceCollectionSet,
    SocketConnectionIpduIdentifierSet,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Ethernet.IPv6HeaderFilterList import IPv6ExtHeaderFilterSet  # noqa: E402
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Ethernet.Dds import DdsCpConfig  # noqa: E402
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Ethernet.TcpOptionFilterSet import TcpOptionFilterSet  # noqa: E402
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Flexray.FlexrayCommunication import FlexrayFrame  # noqa: E402
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Flexray.FlexrayTopology import FlexrayCluster  # noqa: E402
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Lin.LinCommunication import LinUnconditionalFrame  # noqa: E402
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Lin.LinTopology import LinCluster  # noqa: E402
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Multiplatform import Gateway  # noqa: E402
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore.CoreCommunication import (  # noqa: E402
    DcmIPdu,
    GeneralPurposeIPdu,
    GeneralPurposePdu,
    ISignal,
    ISignalGroup,
    ISignalIPdu,
    ISignalIPduGroup,
    J1939DcmIPdu,
    MultiplexedIPdu,
    NPdu,
    NmPdu,
    PdurIPduGroup,
    ContainerIPdu,
    SecureCommunicationPropsSet,
    SecuredIPdu,
    SystemSignal,
    SystemSignalGroup,
    UserDefinedIPdu,
    UserDefinedPdu,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore.CoreTopology import (  # noqa: E402
    CanCluster,
    EcuInstance,
    TtcanCluster,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.CddSupport import UserDefinedCluster  # noqa: E402
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.NetworkManagement import NmConfig  # noqa: E402
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.SecureCommunication import (  # noqa: E402
    CryptoEllipticCurveProps,
    CryptoServiceCertificate,
    CryptoServicePrimitive,
    CryptoSignatureScheme,
    IPSecConfigProps,
    MacSecGlobalKayProps,
    MacSecParticipantSet,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Transformer import (  # noqa: E402
    DataTransformationSet,
    E2EProfileCompatibilityProps,
    TlvDataIdDefinitionSet,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.TransportProtocols import (  # noqa: E402
    CanTpConfig,
    DoIpTpConfig,
    LinTpConfig,
    EthTpConfig,
    SomeipTpConfig,
    FlexrayArTpConfig,
    FlexrayTpConfig,
    IEEE1722TpConfig,
    IEEE1722TpConnection,
    IEEE1722TpAvConnection,
    IEEE1722TpCrfConnection,
)
from armodel.models.M2.MSR.AsamHdo.AdminData import AdminData  # noqa: E402
from armodel.models.M2.MSR.AsamHdo.ComputationMethod import CompuMethod  # noqa: E402
from armodel.models.M2.MSR.AsamHdo.Constraints.GlobalConstraints import DataConstr  # noqa: E402
from armodel.models.M2.MSR.AsamHdo.Units import (  # noqa: E402
    PhysicalDimension,
    Unit,
    UnitGroup,
)
from armodel.models.M2.MSR.DataDictionary.AuxillaryObjects import SwAddrMethod  # noqa: E402
from armodel.models.M2.MSR.DataDictionary.RecordLayout import SwRecordLayout  # noqa: E402
from armodel.models.M2.MSR.DataDictionary.SystemConstant import SwSystemconst  # noqa: E402
from armodel.models.M2.MSR.Documentation.Annotation import Annotation  # noqa: E402
from armodel.models.M2.MSR.Documentation.TextModel.BlockElements import DocumentationBlock  # noqa: E402
from armodel.models.M2.MSR.Documentation.TextModel.MultilanguageData import (  # noqa: E402
    MultiLanguageOverviewParagraph,
    MultilanguageLongName,
)

# Bind late-defined element bases now that this module is fully defined. Collection is
# declared in ElementCollection with a placeholder base to avoid an import cycle: ElementCollection
# is imported for CollectableElement at class-definition time (PackageableElement re-parents to
# CollectableElement), and Collection's spec base ARElement lives here, so binding it here keeps
# both modules importable. After this, isinstance(coll, ARElement) holds.
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ElementCollection import Collection  # noqa: E402

Collection.__bases__ = (ARElement,)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.RolesAndRights import (  # noqa: E402
    AclObjectSet,
    AclOperation,
    AclPermission,
    AclRole,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.ViewMapSet import ViewMapSet  # noqa: E402

AclObjectSet.__bases__ = (ARElement,)
AclOperation.__bases__ = (ARElement,)
AclPermission.__bases__ = (ARElement,)
AclRole.__bases__ = (ARElement,)
ViewMapSet.__bases__ = (ARElement,)
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.RPTScenario import RapidPrototypingScenario  # noqa: E402
from armodel.models.M2.AUTOSARTemplates.CommonStructure.StandardizationTemplate.AbstractBlueprintStructure import LifeCycleState  # noqa: E402
from armodel.models.M2.AUTOSARTemplates.GenericStructure.BuildActionManifest import BuildActionManifest  # noqa: E402
from armodel.models.M2.AUTOSARTemplates.DiagnosticExtract.CommonService import DiagnosticClearDiagnosticInformationClass  # noqa: E402
from armodel.models.M2.AUTOSARTemplates.DiagnosticExtract.CommonService import DiagnosticClearResetEmissionRelatedInfoClass  # noqa: E402
from armodel.models.M2.AUTOSARTemplates.DiagnosticExtract.CommonService import DiagnosticComControlClass  # noqa: E402
from armodel.models.M2.AUTOSARTemplates.DiagnosticExtract.CommonService import DiagnosticControlDTCSettingClass  # noqa: E402
from armodel.models.M2.AUTOSARTemplates.DiagnosticExtract.CommonService import DiagnosticDynamicallyDefineDataIdentifierClass  # noqa: E402
from armodel.models.M2.AUTOSARTemplates.DiagnosticExtract.CommonService import DiagnosticIoControlClass  # noqa: E402
from armodel.models.M2.AUTOSARTemplates.DiagnosticExtract.CommonService import DiagnosticReadDTCInformationClass  # noqa: E402
from armodel.models.M2.AUTOSARTemplates.DiagnosticExtract.CommonService import DiagnosticDataTransferClass  # noqa: E402
from armodel.models.M2.AUTOSARTemplates.DiagnosticExtract.CommonService import DiagnosticRequestControlOfOnBoardDeviceClass  # noqa: E402
from armodel.models.M2.AUTOSARTemplates.DiagnosticExtract.CommonService import DiagnosticRequestCurrentPowertrainDataClass  # noqa: E402
from armodel.models.M2.AUTOSARTemplates.DiagnosticExtract.CommonService import DiagnosticRequestDownloadClass  # noqa: E402
from armodel.models.M2.AUTOSARTemplates.DiagnosticExtract.CommonService import DiagnosticRequestEmissionRelatedDTCClass  # noqa: E402
from armodel.models.M2.AUTOSARTemplates.DiagnosticExtract.CommonService import DiagnosticRequestEmissionRelatedDTCPermanentStatusClass  # noqa: E402
from armodel.models.M2.AUTOSARTemplates.DiagnosticExtract.CommonService import DiagnosticRequestFileTransferClass  # noqa: E402
from armodel.models.M2.AUTOSARTemplates.DiagnosticExtract.CommonService import DiagnosticRequestOnBoardMonitoringTestResultsClass  # noqa: E402
from armodel.models.M2.AUTOSARTemplates.DiagnosticExtract.CommonService import DiagnosticRequestPowertrainFreezeFrameDataClass  # noqa: E402
from armodel.models.M2.AUTOSARTemplates.DiagnosticExtract.CommonService import DiagnosticRequestUploadClass  # noqa: E402
from armodel.models.M2.AUTOSARTemplates.DiagnosticExtract.CommonService import DiagnosticReadMemoryByAddressClass  # noqa: E402
from armodel.models.M2.AUTOSARTemplates.DiagnosticExtract.CommonService import DiagnosticTransferExitClass  # noqa: E402
from armodel.models.M2.AUTOSARTemplates.DiagnosticExtract.CommonService import DiagnosticReadDataByIdentifierClass  # noqa: E402
from armodel.models.M2.AUTOSARTemplates.DiagnosticExtract.CommonService import DiagnosticReadDataByPeriodicIDClass  # noqa: E402
from armodel.models.M2.AUTOSARTemplates.DiagnosticExtract.CommonService import DiagnosticReadScalingDataByIdentifierClass  # noqa: E402
from armodel.models.M2.AUTOSARTemplates.DiagnosticExtract.CommonService import DiagnosticRequestVehicleInfoClass  # noqa: E402
from armodel.models.M2.AUTOSARTemplates.DiagnosticExtract.CommonService import DiagnosticResponseOnEventClass  # noqa: E402
from armodel.models.M2.AUTOSARTemplates.DiagnosticExtract.CommonService import DiagnosticRoutineControlClass  # noqa: E402
from armodel.models.M2.AUTOSARTemplates.DiagnosticExtract.CommonService import DiagnosticWriteDataByIdentifierClass  # noqa: E402
from armodel.models.M2.AUTOSARTemplates.DiagnosticExtract.CommonService import DiagnosticWriteMemoryByAddressClass  # noqa: E402

BuildActionManifest.__bases__ = (ARElement,)


class CalibrationParameterValueSet(ARElement):
    """Specification of a constant that can be part of a package, i.e. it can be defined stand-alone. Tags: atp.recommendedPackage=CalibrationParameterValueSets"""

    # CalibrationParameterValueSet method parity checklist:
    # Spec: AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf, Table 5.137, p.477
    # Columns: impl / docstring / test / reader / writer / release   ([—] = no XML element)
    # [x] __init__                      [x] impl  [x] docstring  [x] test  [—] reader  [—] writer  R23-11
    # [x] addCalibrationParameterValue   [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getCalibrationParameterValues  [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11

    def __init__(self, parent: ARObject, short_name: str):
        super().__init__(parent, short_name)

        # This represents single CalibrationParameterValues in the CalibrationParameterValueSet. Stereotypes: atpSplitable; atpVariation Tags: atp.Splitkey=calibrationParameterValue, calibrationParameterValue.variationPoint.shortLabel vh.latestBindingTime=preCompileTime
        self.calibrationParameterValues: List[CalibrationParameterValue] = []

    def addCalibrationParameterValue(self, value: Optional[CalibrationParameterValue]) -> CalibrationParameterValueSet:
        """
        This represents single CalibrationParameterValues in the CalibrationParameterValueSet. Stereotypes: atpSplitable; atpVariation Tags: atp.Splitkey=calibrationParameterValue, calibrationParameterValue.variationPoint.shortLabel vh.latestBindingTime=preCompileTime

        A None value is a no-op and does not append a calibrationParameterValue.
        """
        if value is not None:
            self.calibrationParameterValues.append(value)
        return self

    def getCalibrationParameterValues(self) -> List[CalibrationParameterValue]:
        """
        This represents single CalibrationParameterValues in the CalibrationParameterValueSet. Stereotypes: atpSplitable; atpVariation Tags: atp.Splitkey=calibrationParameterValue, calibrationParameterValue.variationPoint.shortLabel vh.latestBindingTime=preCompileTime
        """
        return self.calibrationParameterValues


class DiagnosticMapping(ARElement, ABC):
    """
    Abstract element for different kinds of diagnostic mappings.
    """

    # DiagnosticMapping method parity checklist:
    # Spec: AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf, Table 5.1, p.223
    # Columns: impl / docstring / test / reader / writer / release   ([—] = no XML element)
    # [x] __init__                        [x] impl  [x] docstring  [x] test  [—] reader  [—] writer  R23-11
    # [x] getProviderSoftwareClusterRef   [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setProviderSoftwareClusterRef   [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getRequesterSoftwareClusterRef  [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setRequesterSoftwareClusterRef  [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11

    def __init__(self, parent: ARObject, short_name: str):
        if type(self) is DiagnosticMapping:
            raise TypeError("DiagnosticMapping is an abstract class.")

        super().__init__(parent, short_name)

        # This reference can be used in an early design phase to associate an element of a diagnostic extract with an existing provided CPSoftwareCluster.
        self.providerSoftwareClusterRef: Optional[RefType] = None

        # This reference can be used in an early design phase to associate an element of a diagnostic extract with an existing requested CPSoftwareCluster.
        self.requesterSoftwareClusterRef: Optional[RefType] = None

    def getProviderSoftwareClusterRef(self) -> Optional[RefType]:
        """
        This reference can be used in an early design phase to associate an element of a diagnostic extract with an existing provided CPSoftwareCluster.
        """
        return self.providerSoftwareClusterRef

    def setProviderSoftwareClusterRef(self, value: Optional[RefType]) -> DiagnosticMapping:
        """
        This reference can be used in an early design phase to associate an element of a diagnostic extract with an existing provided CPSoftwareCluster.
        A None value is a no-op and does not overwrite an existing providerSoftwareClusterRef.
        """
        if value is not None:
            self.providerSoftwareClusterRef = value
        return self

    def getRequesterSoftwareClusterRef(self) -> Optional[RefType]:
        """
        This reference can be used in an early design phase to associate an element of a diagnostic extract with an existing requested CPSoftwareCluster.
        """
        return self.requesterSoftwareClusterRef

    def setRequesterSoftwareClusterRef(self, value: Optional[RefType]) -> DiagnosticMapping:
        """
        This reference can be used in an early design phase to associate an element of a diagnostic extract with an existing requested CPSoftwareCluster.
        A None value is a no-op and does not overwrite an existing requesterSoftwareClusterRef.
        """
        if value is not None:
            self.requesterSoftwareClusterRef = value
        return self


class CpSwClusterResourceToDiagDataElemMapping(DiagnosticMapping):
    """This meta-class represents the ability to associate a CpSoftwareClusterResource with a DiagnosticDataElement. This allows for indicating that the CpSoftwareClusterResource is used to convey the DiagnosticDataElement. Tags: atp.Status=draft atp.recommendedPackage=CpSoftwareClusterToDiagMappings"""

    # CpSwClusterResourceToDiagDataElemMapping method parity checklist:
    # Spec: AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf, Table 5.47, p.273
    # Columns: impl / docstring / test / reader / writer / release   ([—] = no XML element)
    # [x] __init__                           [x] impl  [x] docstring  [x] test  [—] reader  [—] writer  R23-11
    # [x] getCpSoftwareClusterResourceRef       [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setCpSoftwareClusterResourceRef       [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getDiagnosticDataElementRef           [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setDiagnosticDataElementRef           [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11

    def __init__(self, parent: ARObject, short_name: str):
        super().__init__(parent, short_name)

        # This represents the affected CpSoftwareClusterResource. Tags: atp.Status=draft
        self.cpSoftwareClusterResourceRef: Optional[RefType] = None

        # This reference represents the affected DiagnosticDataElement. Tags: atp.Status=draft
        self.diagnosticDataElementRef: Optional[RefType] = None

    def getCpSoftwareClusterResourceRef(self) -> Optional[RefType]:
        """
        This represents the affected CpSoftwareClusterResource. Tags: atp.Status=draft
        """
        return self.cpSoftwareClusterResourceRef

    def setCpSoftwareClusterResourceRef(self, value: Optional[RefType]) -> CpSwClusterResourceToDiagDataElemMapping:
        """
        This represents the affected CpSoftwareClusterResource. Tags: atp.Status=draft
        A None value is a no-op and does not overwrite an existing cpSoftwareClusterResourceRef.
        """
        if value is not None:
            self.cpSoftwareClusterResourceRef = value
        return self

    def getDiagnosticDataElementRef(self) -> Optional[RefType]:
        """
        This reference represents the affected DiagnosticDataElement. Tags: atp.Status=draft
        """
        return self.diagnosticDataElementRef

    def setDiagnosticDataElementRef(self, value: Optional[RefType]) -> CpSwClusterResourceToDiagDataElemMapping:
        """
        This reference represents the affected DiagnosticDataElement. Tags: atp.Status=draft
        A None value is a no-op and does not overwrite an existing diagnosticDataElementRef.
        """
        if value is not None:
            self.diagnosticDataElementRef = value
        return self


class CpSwClusterResourceToDiagFunctionIdMapping(DiagnosticMapping):
    """This meta-class represents the ability to associate a CpSoftwareClusterResource with a subfunction of a DiagnosticFunctionIdentifier. This allows for indicating that the CpSoftwareClusterResource is used to convey the execution permission associated with the mapped function identifier. Tags: atp.Status=draft atp.recommendedPackage=CpSoftwareClusterToDiagMappings"""

    # CpSwClusterResourceToDiagFunctionIdMapping method parity checklist:
    # Spec: AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf, Table 5.49, p.275
    # Columns: impl / docstring / test / reader / writer / release   ([—] = no XML element)
    # [x] __init__                           [x] impl  [x] docstring  [x] test  [—] reader  [—] writer  R23-11
    # [x] getCpSoftwareClusterResourceRef       [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setCpSoftwareClusterResourceRef       [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getFunctionIdentifierRef              [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setFunctionIdentifierRef              [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11

    def __init__(self, parent: ARObject, short_name: str):
        super().__init__(parent, short_name)

        # This reference identifies the mapped CpSoftwareClusterResource. Tags: atp.Status=draft
        self.cpSoftwareClusterResourceRef: Optional[RefType] = None

        # This reference identifies the mapped DiagnosticFunctionIdentifier. Tags: atp.Status=draft
        self.functionIdentifierRef: Optional[RefType] = None

    def getCpSoftwareClusterResourceRef(self) -> Optional[RefType]:
        """
        This reference identifies the mapped CpSoftwareClusterResource. Tags: atp.Status=draft
        """
        return self.cpSoftwareClusterResourceRef

    def setCpSoftwareClusterResourceRef(self, value: Optional[RefType]) -> CpSwClusterResourceToDiagFunctionIdMapping:
        """
        This reference identifies the mapped CpSoftwareClusterResource. Tags: atp.Status=draft
        A None value is a no-op and does not overwrite an existing cpSoftwareClusterResourceRef.
        """
        if value is not None:
            self.cpSoftwareClusterResourceRef = value
        return self

    def getFunctionIdentifierRef(self) -> Optional[RefType]:
        """
        This reference identifies the mapped DiagnosticFunctionIdentifier. Tags: atp.Status=draft
        """
        return self.functionIdentifierRef

    def setFunctionIdentifierRef(self, value: Optional[RefType]) -> CpSwClusterResourceToDiagFunctionIdMapping:
        """
        This reference identifies the mapped DiagnosticFunctionIdentifier. Tags: atp.Status=draft
        A None value is a no-op and does not overwrite an existing functionIdentifierRef.
        """
        if value is not None:
            self.functionIdentifierRef = value
        return self


class CpSwClusterToDiagEventMapping(DiagnosticMapping):
    """This meta-class represents the ability to associate a CpSoftwareClusterResource with a DiagnosticEvent. This allows for indicating that the CpSoftwareClusterResource is used to convey the reporting or status query of the mapped DiagnosticEvent. Tags: atp.Status=draft atp.recommendedPackage=CpSoftwareClusterToDiagMappings"""

    # CpSwClusterToDiagEventMapping method parity checklist:
    # Spec: AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf, Table 5.46, p.272
    # Columns: impl / docstring / test / reader / writer / release   ([—] = no XML element)
    # [x] __init__                           [x] impl  [x] docstring  [x] test  [—] reader  [—] writer  R23-11
    # [x] getCpSoftwareClusterResourceRef       [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setCpSoftwareClusterResourceRef       [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getDiagnosticEventRef                 [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setDiagnosticEventRef                 [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11

    def __init__(self, parent: ARObject, short_name: str):
        super().__init__(parent, short_name)

        # This reference identifies the mapped CpSoftwareClusterResource. Tags: atp.Status=draft
        self.cpSoftwareClusterResourceRef: Optional[RefType] = None

        # This reference identifies the mapped DiagnosticEvent. Tags: atp.Status=draft
        self.diagnosticEventRef: Optional[RefType] = None

    def getCpSoftwareClusterResourceRef(self) -> Optional[RefType]:
        """
        This reference identifies the mapped CpSoftwareClusterResource. Tags: atp.Status=draft
        """
        return self.cpSoftwareClusterResourceRef

    def setCpSoftwareClusterResourceRef(self, value: Optional[RefType]) -> CpSwClusterToDiagEventMapping:
        """
        This reference identifies the mapped CpSoftwareClusterResource. Tags: atp.Status=draft
        A None value is a no-op and does not overwrite an existing cpSoftwareClusterResourceRef.
        """
        if value is not None:
            self.cpSoftwareClusterResourceRef = value
        return self

    def getDiagnosticEventRef(self) -> Optional[RefType]:
        """
        This reference identifies the mapped DiagnosticEvent. Tags: atp.Status=draft
        """
        return self.diagnosticEventRef

    def setDiagnosticEventRef(self, value: Optional[RefType]) -> CpSwClusterToDiagEventMapping:
        """
        This reference identifies the mapped DiagnosticEvent. Tags: atp.Status=draft
        A None value is a no-op and does not overwrite an existing diagnosticEventRef.
        """
        if value is not None:
            self.diagnosticEventRef = value
        return self


class CpSwClusterToDiagRoutineSubfunctionMapping(DiagnosticMapping):
    """This meta-class represents the ability to associate a CpSoftwareClusterResource with a subfunction of a DiagnosticRoutine. This allows for indicating that the CpSoftwareClusterResource is used to convey the calling or result return of the mapped DiagnosticRoutine. Tags: atp.Status=draft atp.recommendedPackage=CpSoftwareClusterToDiagMappings"""

    # CpSwClusterToDiagRoutineSubfunctionMapping method parity checklist:
    # Spec: AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf, Table 5.48, p.274
    # Columns: impl / docstring / test / reader / writer / release   ([—] = no XML element)
    # [x] __init__                           [x] impl  [x] docstring  [x] test  [—] reader  [—] writer  R23-11
    # [x] getCpSoftwareClusterResourceRef       [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setCpSoftwareClusterResourceRef       [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getRoutineSubfunctionRef              [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setRoutineSubfunctionRef              [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11

    def __init__(self, parent: ARObject, short_name: str):
        super().__init__(parent, short_name)

        # This reference identifies the mapped CpSoftwareClusterResource. Tags: atp.Status=draft
        self.cpSoftwareClusterResourceRef: Optional[RefType] = None

        # This reference identifies the mapped subfunction of a DiagnosticRoutine. Tags: atp.Status=draft
        self.routineSubfunctionRef: Optional[RefType] = None

    def getCpSoftwareClusterResourceRef(self) -> Optional[RefType]:
        """
        This reference identifies the mapped CpSoftwareClusterResource. Tags: atp.Status=draft
        """
        return self.cpSoftwareClusterResourceRef

    def setCpSoftwareClusterResourceRef(self, value: Optional[RefType]) -> CpSwClusterToDiagRoutineSubfunctionMapping:
        """
        This reference identifies the mapped CpSoftwareClusterResource. Tags: atp.Status=draft
        A None value is a no-op and does not overwrite an existing cpSoftwareClusterResourceRef.
        """
        if value is not None:
            self.cpSoftwareClusterResourceRef = value
        return self

    def getRoutineSubfunctionRef(self) -> Optional[RefType]:
        """
        This reference identifies the mapped subfunction of a DiagnosticRoutine. Tags: atp.Status=draft
        """
        return self.routineSubfunctionRef

    def setRoutineSubfunctionRef(self, value: Optional[RefType]) -> CpSwClusterToDiagRoutineSubfunctionMapping:
        """
        This reference identifies the mapped subfunction of a DiagnosticRoutine. Tags: atp.Status=draft
        A None value is a no-op and does not overwrite an existing routineSubfunctionRef.
        """
        if value is not None:
            self.routineSubfunctionRef = value
        return self


class DataExchangePoint(ARElement):
    pass


class DiagnosticAbstractAliasEvent(ARElement, ABC):
    """This meta-class represents an abstract base class for all diagnostic alias events."""

    # DiagnosticAbstractAliasEvent method parity checklist:
    # Spec: AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf, Table 4.213, p.214
    # Columns: impl / docstring / test / reader / writer / release   ([—] = no XML element)
    # [x] __init__  [x] impl  [x] docstring  [x] test  [—] reader  [—] writer  R23-11

    def __init__(self, parent: ARObject, short_name: str):
        if type(self) is DiagnosticAbstractAliasEvent:
            raise TypeError("DiagnosticAbstractAliasEvent is an abstract class.")

        super().__init__(parent, short_name)


class DiagnosticAbstractDataIdentifier(ARElement, ABC):
    """
    This meta-class represents an abstract base class for the modeling of a diagnostic data identifier (DID).

    [constr_1793] Existence of attribute DiagnosticAbstractDataIdentifier.id: For each DiagnosticAbstractDataIdentifier, attribute id shall exist at the time when the DEXT is complete.
    """

    # DiagnosticAbstractDataIdentifier method parity checklist:
    # Spec: AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf, Table 4.4, p.34
    # Columns: impl / docstring / test / reader / writer / release   ([—] = no XML element)
    # [x] __init__  [x] impl  [x] docstring  [x] test  [—] reader  [—] writer  R23-11
    # [x] getId     [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setId     [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11

    def __init__(self, parent: ARObject, short_name: str):
        if type(self) is DiagnosticAbstractDataIdentifier:
            raise TypeError("DiagnosticAbstractDataIdentifier is an abstract class.")

        super().__init__(parent, short_name)

        # This is the numerical identifier used to identify the DiagnosticAbstractDataIdentifier in the scope of diagnostic workflow Stereotypes: atpVariation Tags: vh.latestBindingTime=preCompileTime
        self.id: Optional[PositiveInteger] = None

    def getId(self) -> Optional[PositiveInteger]:
        """
        This is the numerical identifier used to identify the DiagnosticAbstractDataIdentifier in the scope of diagnostic workflow
        """
        return self.id

    def setId(self, value: Optional[PositiveInteger]) -> DiagnosticAbstractDataIdentifier:
        """
        This is the numerical identifier used to identify the DiagnosticAbstractDataIdentifier in the scope of diagnostic workflow
        A None value is a no-op and does not overwrite an existing id.
        """
        if value is not None:
            self.id = value
        return self


class DiagnosticAging(ARElement):
    """
    Defines the aging algorithm. Tags: atp.recommendedPackage=DiagnosticAgings

    [constr_1848] Existence of attribute DiagnosticAging.agingCycle: For each DiagnosticAging, attribute agingCycle shall exist at the time when the DEXT is complete.
    [constr_1849] Existence of attribute DiagnosticAging.threshold: For each DiagnosticAging, attribute threshold shall exist at the time when the DEXT is complete.
    """

    # DiagnosticAging method parity checklist:
    # Spec: AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf, Table 4.198, p.202
    # Columns: impl / docstring / test / reader / writer / release   ([—] = no XML element)
    # [x] __init__          [x] impl  [x] docstring  [x] test  [—] reader  [—] writer  R23-11
    # [x] getAgingCycleRef  [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setAgingCycleRef  [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getThreshold      [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setThreshold      [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11

    def __init__(self, parent: ARObject, short_name: str):
        super().__init__(parent, short_name)

        # This represents the applicable aging cycle.
        self.agingCycleRef: Optional[RefType] = None

        # Number of aging cycles needed to unlearn/delete the event.
        self.threshold: Optional[PositiveInteger] = None

    def getAgingCycleRef(self) -> Optional[RefType]:
        """
        This represents the applicable aging cycle.
        """
        return self.agingCycleRef

    def setAgingCycleRef(self, value: Optional[RefType]) -> DiagnosticAging:
        """
        This represents the applicable aging cycle.

        A None value is a no-op and does not overwrite an existing agingCycleRef.
        """
        if value is not None:
            self.agingCycleRef = value
        return self

    def getThreshold(self) -> Optional[PositiveInteger]:
        """
        Number of aging cycles needed to unlearn/delete the event.
        """
        return self.threshold

    def setThreshold(self, value: Optional[PositiveInteger]) -> DiagnosticAging:
        """
        Number of aging cycles needed to unlearn/delete the event.

        A None value is a no-op and does not overwrite an existing threshold.
        """
        if value is not None:
            self.threshold = value
        return self


class DiagnosticAuthRole(ARElement):
    """This meta-class represents the ability to specify an authentication role that can be used to deliver fine-grained access rights."""

    # DiagnosticAuthRole method parity checklist:
    # Spec: AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf, Table 4.34, p.77
    # Columns: impl / docstring / test / reader / writer / release   ([—] = no XML element)
    # [x] __init__         [x] impl  [x] docstring  [x] test  [—] reader  [—] writer  R23-11
    # [x] getBitPosition   [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setBitPosition   [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getIsDefault     [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setIsDefault     [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11

    def __init__(self, parent: ARObject, short_name: str):
        super().__init__(parent, short_name)

        # This attribute allows for the specification of the position of the enclosing role in a bitfield of roles.
        self.bitPosition: Optional[PositiveInteger] = None

        # This attribute indicates whether the enclosing role is considered a default role.
        self.isDefault: Optional[Boolean] = None

    def getBitPosition(self) -> Optional[PositiveInteger]:
        """
        This attribute allows for the specification of the position of the enclosing role in a bitfield of roles.
        """
        return self.bitPosition

    def setBitPosition(self, value: Optional[PositiveInteger]):
        """
        This attribute allows for the specification of the position of the enclosing role in a bitfield of roles.

        A None value is a no-op and does not overwrite an existing bitPosition.
        """
        if value is not None:
            self.bitPosition = value
        return self

    def getIsDefault(self) -> Optional[Boolean]:
        """
        This attribute indicates whether the enclosing role is considered a default role.
        """
        return self.isDefault

    def setIsDefault(self, value: Optional[Boolean]):
        """
        This attribute indicates whether the enclosing role is considered a default role.

        A None value is a no-op and does not overwrite an existing isDefault.
        """
        if value is not None:
            self.isDefault = value
        return self


class DiagnosticAuthentication(ARElement, ABC):
    """This meta-class represents the ability to configure the usage of the UDS service Authentication in the Diagnostic extract."""

    # DiagnosticAuthentication method parity checklist:
    # Spec: AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf, Table 4.51, p.99
    # Columns: impl / docstring / test / reader / writer / release   ([—] = no XML element)
    # [x] __init__                   [x] impl  [x] docstring  [x] test  [—] reader  [—] writer  R23-11
    # [x] getAuthenticationClass     [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setAuthenticationClass     [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11

    def __init__(self, parent: ARObject, short_name: str):
        if type(self) is DiagnosticAuthentication:
            raise TypeError("DiagnosticAuthentication is an abstract class.")
        super().__init__(parent, short_name)

        # This represents the corresponding "class", i.e. this meta-class provides properties that are shared among all instances of applicable sub-classes of DiagnosticServiceInstance. The subclasses that affected by this pattern implement references to the applicable "class"-role that substantiate this abstract reference.
        self.authenticationClass: Optional[RefType] = None

    def getAuthenticationClass(self) -> Optional[RefType]:
        """
        This represents the corresponding "class", i.e. this meta-class provides properties that are shared among all instances of applicable sub-classes of DiagnosticServiceInstance. The subclasses that affected by this pattern implement references to the applicable "class"-role that substantiate this abstract reference.
        """
        return self.authenticationClass

    def setAuthenticationClass(self, value: Optional[RefType]):
        """
        This represents the corresponding "class", i.e. this meta-class provides properties that are shared among all instances of applicable sub-classes of DiagnosticServiceInstance. The subclasses that affected by this pattern implement references to the applicable "class"-role that substantiate this abstract reference.

        A None value is a no-op and does not overwrite an existing authenticationClass.
        """
        if value is not None:
            self.authenticationClass = value
        return self


class DiagnosticAuthTransmitCertificate(DiagnosticAuthentication):
    """This meta-class represents the sub-function to transmit a certificate"""

    # DiagnosticAuthTransmitCertificate method parity checklist:
    # Spec: AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf, Table 4.58, p.100
    # Columns: impl / docstring / test / reader / writer / release   ([—] = no XML element)
    # [x] __init__                                           [x] impl  [x] docstring  [x] test  [—] reader  [—] writer  R23-11
    # [x] getCertificateEvaluations                          [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] createDiagnosticAuthTransmitCertificateEvaluation  [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11

    def __init__(self, parent: ARObject, short_name: str):
        super().__init__(parent, short_name)

        # This aggregation represents a collection of certificate evaluation configurations.
        self.certificateEvaluations: List[DiagnosticAuthTransmitCertificateEvaluation] = []

    def getCertificateEvaluations(self) -> List[DiagnosticAuthTransmitCertificateEvaluation]:
        """
        This aggregation represents a collection of certificate evaluation configurations.
        """
        return self.certificateEvaluations

    def createDiagnosticAuthTransmitCertificateEvaluation(self, short_name: str) -> DiagnosticAuthTransmitCertificateEvaluation:
        """
        This aggregation represents a collection of certificate evaluation configurations.
        The existing evaluation is returned when the short name already exists (no duplicate creation).
        """
        if not self.IsReferrableElementExists(short_name, DiagnosticAuthTransmitCertificateEvaluation):
            evaluation = DiagnosticAuthTransmitCertificateEvaluation(self, short_name)
            self.addReferrableElement(evaluation)
            self.certificateEvaluations.append(evaluation)
        return cast(DiagnosticAuthTransmitCertificateEvaluation, self.getReferrableElement(short_name, DiagnosticAuthTransmitCertificateEvaluation))


class DiagnosticAuthTransmitCertificateMapping(DiagnosticMapping):
    """This meta-class represents the ability to associate a CryptoServiceCertificate with a DiagnosticAuthCertificateEvaluation with the purpose to configure the evaluation of the certificate. Tags: atp.recommendedPackage=DiagnosticMappings"""

    # DiagnosticAuthTransmitCertificateMapping method parity checklist:
    # Spec: AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf, Table 5.17, p.242
    # Columns: impl / docstring / test / reader / writer / release   ([—] = no XML element)
    # [x] __init__                           [x] impl  [x] docstring  [x] test  [—] reader  [—] writer  R23-11
    # [x] addCryptoServiceCertificateRef        [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getCryptoServiceCertificateRefs       [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] getServiceInstanceRef                 [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setServiceInstanceRef                 [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11

    def __init__(self, parent: ARObject, short_name: str):
        super().__init__(parent, short_name)

        # This reference identifies the description of the applicable crypto certificate.
        self.cryptoServiceCertificateRefs: List[RefType] = []

        # This reference identifies the applicable DiagnosticAuthTransmitCertificate service instance (via the aggregation in the role certificateEvaluation).
        self.serviceInstanceRef: Optional[RefType] = None

    def addCryptoServiceCertificateRef(self, value: Optional[RefType]) -> DiagnosticAuthTransmitCertificateMapping:
        """
        This reference identifies the description of the applicable crypto certificate.
        A None value is a no-op and does not append a cryptoServiceCertificateRef.
        """
        if value is not None:
            self.cryptoServiceCertificateRefs.append(value)
        return self

    def getCryptoServiceCertificateRefs(self) -> List[RefType]:
        """
        This reference identifies the description of the applicable crypto certificate.
        """
        return self.cryptoServiceCertificateRefs

    def getServiceInstanceRef(self) -> Optional[RefType]:
        """
        This reference identifies the applicable DiagnosticAuthTransmitCertificate service instance (via the aggregation in the role certificateEvaluation).
        """
        return self.serviceInstanceRef

    def setServiceInstanceRef(self, value: Optional[RefType]) -> DiagnosticAuthTransmitCertificateMapping:
        """
        This reference identifies the applicable DiagnosticAuthTransmitCertificate service instance (via the aggregation in the role certificateEvaluation).
        A None value is a no-op and does not overwrite an existing serviceInstanceRef.
        """
        if value is not None:
            self.serviceInstanceRef = value
        return self


class DiagnosticAuthenticationConfiguration(DiagnosticAuthentication):
    """This meta-class represents the subfunction to configure the authentication."""

    # DiagnosticAuthenticationConfiguration method parity checklist:
    # Spec: AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf, Table 4.53, p.99
    # Columns: impl / docstring / test / reader / writer / release   ([—] = no XML element)
    # [x] __init__  [x] impl  [x] docstring  [x] test  [—] reader  [—] writer  R23-11

    def __init__(self, parent: ARObject, short_name: str):
        super().__init__(parent, short_name)


class DiagnosticClearDiagnosticInformation(ARElement):
    """This represents an instance of the "Clear Diagnostic Information" diagnostic service."""

    # DiagnosticClearDiagnosticInformation method parity checklist:
    # Spec: AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf, Table 4.108, p.137
    # Columns: impl / docstring / test / reader / writer / release   ([—] = no XML element)
    # [x] __init__                                [x] impl  [x] docstring  [x] test  [—] reader  [—] writer  R23-11
    # [x] getClearDiagnosticInformationClass      [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setClearDiagnosticInformationClass      [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11

    def __init__(self, parent: ARObject, short_name: str):
        super().__init__(parent, short_name)

        # This reference substantiates that abstract reference in the role serviceClass for this specific concrete class. Thereby, the reference represents the ability to access shared attributes among all DiagnosticClearDiagnosticInformation in the given context.
        self.clearDiagnosticInformationClass: Optional[RefType] = None

    def getClearDiagnosticInformationClass(self) -> Optional[RefType]:
        """
        This reference substantiates that abstract reference in the role serviceClass for this specific concrete class. Thereby, the reference represents the ability to access shared attributes among all DiagnosticClearDiagnosticInformation in the given context.
        """
        return self.clearDiagnosticInformationClass

    def setClearDiagnosticInformationClass(self, value: Optional[RefType]) -> DiagnosticClearDiagnosticInformation:
        """
        This reference substantiates that abstract reference in the role serviceClass for this specific concrete class. Thereby, the reference represents the ability to access shared attributes among all DiagnosticClearDiagnosticInformation in the given context.

        A None value is a no-op and does not overwrite an existing clearDiagnosticInformationClass.
        """
        if value is not None:
            self.clearDiagnosticInformationClass = value
        return self


class DiagnosticComControl(ARElement):
    """This represents an instance of the "Communication Control" diagnostic service."""

    # DiagnosticComControl method parity checklist:
    # Spec: AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf, Table 4.64, p.108
    # Columns: impl / docstring / test / reader / writer / release   ([—] = no XML element)
    # [x] __init__                     [x] impl  [x] docstring  [x] test  [—] reader  [—] writer  R23-11
    # [x] getComControlClass           [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setComControlClass           [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getCustomSubFunctionNumber   [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setCustomSubFunctionNumber   [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11

    def __init__(self, parent: ARObject, short_name: str):
        super().__init__(parent, short_name)

        # This reference substantiates that abstract reference in the role serviceClass for this specific concrete class. Thereby, the reference represents the ability to access shared attributes among all DiagnosticComControl in the given context.
        self.comControlClass: Optional[RefType] = None

        # This attribute shall be used to define a custom sub-function number if none of the standardized values of category shall be used.
        self.customSubFunctionNumber: Optional[PositiveInteger] = None

    def getComControlClass(self) -> Optional[RefType]:
        """
        This reference substantiates that abstract reference in the role serviceClass for this specific concrete class. Thereby, the reference represents the ability to access shared attributes among all DiagnosticComControl in the given context.
        """
        return self.comControlClass

    def setComControlClass(self, value: Optional[RefType]) -> DiagnosticComControl:
        """
        This reference substantiates that abstract reference in the role serviceClass for this specific concrete class. Thereby, the reference represents the ability to access shared attributes among all DiagnosticComControl in the given context.

        A None value is a no-op and does not overwrite an existing comControlClass.
        """
        if value is not None:
            self.comControlClass = value
        return self

    def getCustomSubFunctionNumber(self) -> Optional[PositiveInteger]:
        """
        This attribute shall be used to define a custom sub-function number if none of the standardized values of category shall be used.
        """
        return self.customSubFunctionNumber

    def setCustomSubFunctionNumber(self, value: Optional[PositiveInteger]) -> DiagnosticComControl:
        """
        This attribute shall be used to define a custom sub-function number if none of the standardized values of category shall be used.

        A None value is a no-op and does not overwrite an existing customSubFunctionNumber.
        """
        if value is not None:
            self.customSubFunctionNumber = value
        return self


class DiagnosticCondition(DiagnosticCommonElement, ABC):
    """Abstract element for StorageConditions and EnableConditions."""

    # DiagnosticCondition method parity checklist:
    # Spec: AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf, Table 4.184, p.194
    # Columns: impl / docstring / test / reader / writer / release   ([—] = no XML element)
    # [x] __init__       [x] impl  [x] docstring  [x] test  [—] reader  [—] writer  R23-11
    # [x] getInitValue   [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setInitValue   [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11

    def __init__(self, parent: ARObject, short_name: str):
        if type(self) is DiagnosticCondition:
            raise TypeError("DiagnosticCondition is an abstract class.")
        super().__init__(parent, short_name)

        # Defines the initial status for enable or disable of acceptance/storage of event reports of a diagnostic event. The value is the initialization after power up (before this condition is reported the first time). true: acceptance/storage of a diagnostic event enabled false: acceptance/storage of a diagnostic event disabled
        self.initValue: Optional[Boolean] = None

    def getInitValue(self) -> Optional[Boolean]:
        """
        Defines the initial status for enable or disable of acceptance/storage of event reports of a diagnostic event. The value is the initialization after power up (before this condition is reported the first time). true: acceptance/storage of a diagnostic event enabled false: acceptance/storage of a diagnostic event disabled
        """
        return self.initValue

    def setInitValue(self, value: Optional[Boolean]) -> DiagnosticCondition:
        """
        Defines the initial status for enable or disable of acceptance/storage of event reports of a diagnostic event. The value is the initialization after power up (before this condition is reported the first time). true: acceptance/storage of a diagnostic event enabled false: acceptance/storage of a diagnostic event disabled

        A None value is a no-op and does not overwrite an existing initValue.
        """
        if value is not None:
            self.initValue = value
        return self


class DiagnosticConditionGroup(DiagnosticCommonElement, ABC):
    """Abstract element for StorageConditionGroups and EnableConditionGroups."""

    # DiagnosticConditionGroup method parity checklist:
    # Spec: AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf, Table 4.193, p.200
    # Columns: impl / docstring / test / reader / writer / release   ([—] = no XML element)
    # [x] __init__  [x] impl  [x] docstring  [x] test  [—] reader  [—] writer  R23-11

    def __init__(self, parent: ARObject, short_name: str):
        if type(self) is DiagnosticConditionGroup:
            raise TypeError("DiagnosticConditionGroup is an abstract class.")
        super().__init__(parent, short_name)


class DiagnosticControlDTCSetting(ARElement):
    """This represents an instance of the "Control DTC Setting" diagnostic service."""

    # DiagnosticControlDTCSetting method parity checklist:
    # Spec: AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf, Table 4.68, p.111
    # Columns: impl / docstring / test / reader / writer / release   ([—] = no XML element)
    # [x] __init__               [x] impl  [x] docstring  [x] test  [—] reader  [—] writer  R23-11
    # [x] getDtcSettingClass     [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setDtcSettingClass     [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    #
    # Table 4.68 is a minimal 2-row table (Class + dtcSettingClass only) — the Note
    # comes from R4.3.1 Table 5.62 (R23-11 XSD documentation agrees); the Base chain
    # (R4.3.1 Table 5.62 / R23-11 XSD group chain) names DiagnosticServiceInstance,
    # but the concrete sibling instance classes (DiagnosticComControl Table 4.64,
    # DiagnosticEcuReset) model ARElement — same choice here. R23-11 marks
    # dtcSettingParameter atp.Status="removed" (absent from the R23-11 table) — not modeled.

    def __init__(self, parent: ARObject, short_name: str):
        super().__init__(parent, short_name)

        # This reference substantiates that abstract reference in the role serviceClass for this specific concrete class. Thereby, the reference represents the ability to access shared attributes among all DiagnosticControlDTCSetting in the given context.
        self.dtcSettingClass: Optional[RefType] = None

    def getDtcSettingClass(self) -> Optional[RefType]:
        """
        This reference substantiates that abstract reference in the role serviceClass for this specific concrete class. Thereby, the reference represents the ability to access shared attributes among all DiagnosticControlDTCSetting in the given context.
        """
        return self.dtcSettingClass

    def setDtcSettingClass(self, value: Optional[RefType]) -> DiagnosticControlDTCSetting:
        """
        This reference substantiates that abstract reference in the role serviceClass for this specific concrete class. Thereby, the reference represents the ability to access shared attributes among all DiagnosticControlDTCSetting in the given context.

        A None value is a no-op and does not overwrite an existing dtcSettingClass.
        """
        if value is not None:
            self.dtcSettingClass = value
        return self


class DiagnosticContributionSet(ARElement):
    """
    This meta-class represents a root node of a diagnostic extract. It bundles a given set of diagnostic model elements. The granularity of the DiagonsticContributionSet is arbitrary in order to support the aspect of decentralized configuration, i.e. different contributors can come up with an own DiagnosticContribution Set.
    """

    # DiagnosticContributionSet method parity checklist:
    # Spec: AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf, Table 4.14, p.57
    # Columns: impl / docstring / test / reader / writer / release   ([—] = no XML element)
    # [x] __init__             [x] impl  [x] docstring  [x] test  [—] reader  [—] writer  R23-11
    # [x] getCommonProperties  [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setCommonProperties  [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] addElementRef        [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getReferrableElementRefs       [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] addServiceTableRef   [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getServiceTableRefs  [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11

    def __init__(self, parent: ARObject, short_name: str):
        super().__init__(parent, short_name)

        # This attribute represents a collection of diagnostic properties that are shared among the entire DiagnosticContributionSet.
        self.commonProperties: Optional[DiagnosticCommonProps] = None

        # This represents a DiagnosticCommonElement considered in the context of the DiagnosticContributionSet
        self.elementRefs: List[RefType] = []

        # This represents the collection of DiagnosticServiceTables to be considered in the scope of this DiagnosticContributionSet.
        self.serviceTableRefs: List[RefType] = []

    def getCommonProperties(self) -> Optional[DiagnosticCommonProps]:
        """
        This attribute represents a collection of diagnostic properties that are shared among the entire DiagnosticContributionSet.
        """
        return self.commonProperties

    def setCommonProperties(self, value: Optional[DiagnosticCommonProps]) -> DiagnosticContributionSet:
        """
        This attribute represents a collection of diagnostic properties that are shared among the entire DiagnosticContributionSet.
        A None value is a no-op and does not overwrite an existing commonProperties.
        """
        if value is not None:
            self.commonProperties = value
        return self

    def addElementRef(self, value: Optional[RefType]) -> DiagnosticContributionSet:
        """
        This represents a DiagnosticCommonElement considered in the context of the DiagnosticContributionSet
        A None value is a no-op and does not append an elementRef.
        """
        if value is not None:
            self.elementRefs.append(value)
        return self

    def getElementRefs(self) -> List[RefType]:
        """
        This represents a DiagnosticCommonElement considered in the context of the DiagnosticContributionSet
        """
        return self.elementRefs

    def addServiceTableRef(self, value: Optional[RefType]) -> DiagnosticContributionSet:
        """
        This represents the collection of DiagnosticServiceTables to be considered in the scope of this DiagnosticContributionSet.
        A None value is a no-op and does not append a serviceTableRef.
        """
        if value is not None:
            self.serviceTableRefs.append(value)
        return self

    def getServiceTableRefs(self) -> List[RefType]:
        """
        This represents the collection of DiagnosticServiceTables to be considered in the scope of this DiagnosticContributionSet.
        """
        return self.serviceTableRefs


class DiagnosticCustomServiceInstance(DiagnosticServiceInstance):
    """
    This meta-class has the ability to define an instance of a custom diagnostic service.
    """

    # DiagnosticCustomServiceInstance method parity checklist:
    # Spec: AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf, Table 4.27, p.70
    # Columns: impl / docstring / test / reader / writer / release   ([—] = no XML element)
    # [x] __init__                  [x] impl  [x] docstring  [x] test  [—] reader  [—] writer  R23-11
    # [x] setCustomServiceClassRef  [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getCustomServiceClassRef  [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11

    def __init__(self, parent: ARObject, short_name: str):
        super().__init__(parent, short_name)

        # Reference to the corresponding DiagnosticCustomServiceClass.
        self.customServiceClassRef: Optional[RefType] = None

    def getCustomServiceClassRef(self) -> Optional[RefType]:
        """
        Reference to the corresponding DiagnosticCustomServiceClass.
        """
        return self.customServiceClassRef

    def setCustomServiceClassRef(self, value: Optional[RefType]):
        """
        Reference to the corresponding DiagnosticCustomServiceClass.

        A None value is a no-op and does not overwrite an existing customServiceClassRef.
        """
        if value is not None:
            self.customServiceClassRef = value
        return self


class DiagnosticRequestCurrentPowertrainData(DiagnosticServiceInstance):
    """This meta-class represents the ability to model an instance of the OBD mode 0x01 service. Tags: atp.recommendedPackage=DiagnosticRequestCurrentPowertrainDatas"""

    # DiagnosticRequestCurrentPowertrainData method parity checklist:
    # Spec: AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf, Table 4.130, p.151
    # Columns: impl / docstring / test / reader / writer / release   ([—] = no XML element)
    # [x] __init__                                             [x] impl  [x] docstring  [x] test  [—] reader  [—] writer  R23-11
    # [x] getPidRef                                            [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setPidRef                                            [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getRequestCurrentPowertrainDiagnosticDataClassRef    [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setRequestCurrentPowertrainDiagnosticDataClassRef    [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11

    def __init__(self, parent: ARObject, short_name: str):
        super().__init__(parent, short_name)

        # This represents the PID associated with this instance of the OBD mode 0x01 service.
        self.pidRef: Optional[RefType] = None

        # This reference substantiates that abstract reference in the role serviceClass for this specific concrete class. Thereby, the reference represents the ability to access shared attributes among all DiagnosticRequestCurrentPowertrainData in the given context.
        self.requestCurrentPowertrainDiagnosticDataClassRef: Optional[RefType] = None

    def getPidRef(self) -> Optional[RefType]:
        """
        This represents the PID associated with this instance of the OBD mode 0x01 service.
        """
        return self.pidRef

    def setPidRef(self, value: Optional[RefType]) -> DiagnosticRequestCurrentPowertrainData:
        """
        This represents the PID associated with this instance of the OBD mode 0x01 service.

        A None value is a no-op and does not overwrite an existing pidRef.
        """
        if value is not None:
            self.pidRef = value
        return self

    def getRequestCurrentPowertrainDiagnosticDataClassRef(self) -> Optional[RefType]:
        """
        This reference substantiates that abstract reference in the role serviceClass for this specific concrete class. Thereby, the reference represents the ability to access shared attributes among all DiagnosticRequestCurrentPowertrainData in the given context.
        """
        return self.requestCurrentPowertrainDiagnosticDataClassRef

    def setRequestCurrentPowertrainDiagnosticDataClassRef(self, value: Optional[RefType]) -> DiagnosticRequestCurrentPowertrainData:
        """
        This reference substantiates that abstract reference in the role serviceClass for this specific concrete class. Thereby, the reference represents the ability to access shared attributes among all DiagnosticRequestCurrentPowertrainData in the given context.

        A None value is a no-op and does not overwrite an existing requestCurrentPowertrainDiagnosticDataClassRef.
        """
        if value is not None:
            self.requestCurrentPowertrainDiagnosticDataClassRef = value
        return self


class DiagnosticRequestEmissionRelatedDTC(DiagnosticServiceInstance):
    """This meta-class represents the ability to model an instance of the OBD mode 0x03/0x07 service. Tags: atp.recommendedPackage=DiagnosticRequestEmissionRelatedDTCs"""

    # DiagnosticRequestEmissionRelatedDTC method parity checklist:
    # Spec: AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf, Table 4.135, p.154
    # Columns: impl / docstring / test / reader / writer / release   ([—] = no XML element)
    # [x] __init__                                     [x] impl  [x] docstring  [x] test  [—] reader  [—] writer  R23-11
    # [x] getRequestEmissionRelatedDtcClassRef         [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setRequestEmissionRelatedDtcClassRef         [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11

    def __init__(self, parent: ARObject, short_name: str):
        super().__init__(parent, short_name)

        # This reference substantiates that abstract reference in the role serviceClass for this specific concrete class. Thereby, the reference represents the ability to access shared attributes among all DiagnosticRequestEmissionRelatedDTC in the given context.
        self.requestEmissionRelatedDtcClassRef: Optional[RefType] = None

    def getRequestEmissionRelatedDtcClassRef(self) -> Optional[RefType]:
        """
        This reference substantiates that abstract reference in the role serviceClass for this specific concrete class. Thereby, the reference represents the ability to access shared attributes among all DiagnosticRequestEmissionRelatedDTC in the given context.
        """
        return self.requestEmissionRelatedDtcClassRef

    def setRequestEmissionRelatedDtcClassRef(self, value: Optional[RefType]) -> DiagnosticRequestEmissionRelatedDTC:
        """
        This reference substantiates that abstract reference in the role serviceClass for this specific concrete class. Thereby, the reference represents the ability to access shared attributes among all DiagnosticRequestEmissionRelatedDTC in the given context.

        A None value is a no-op and does not overwrite an existing requestEmissionRelatedDtcClassRef.
        """
        if value is not None:
            self.requestEmissionRelatedDtcClassRef = value
        return self


class DiagnosticClearResetEmissionRelatedInfo(DiagnosticServiceInstance):
    """This meta-class represents the ability to model an instance of the OBD mode 0x04 service. Tags: atp.recommendedPackage=DiagnosticClearResetEmissionRelatedInfos"""

    # DiagnosticClearResetEmissionRelatedInfo method parity checklist:
    # Spec: AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf, Table 4.137, p.155
    # Columns: impl / docstring / test / reader / writer / release   ([—] = no XML element)
    # [x] __init__                                                 [x] impl  [x] docstring  [x] test  [—] reader  [—] writer  R23-11
    # [x] getClearResetEmissionRelatedDiagnosticInfoClassRef       [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setClearResetEmissionRelatedDiagnosticInfoClassRef       [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11

    def __init__(self, parent: ARObject, short_name: str):
        super().__init__(parent, short_name)

        # This reference substantiates that abstract reference in the role serviceClass for this specific concrete class. Thereby, the reference represents the ability to access shared attributes among all DiagnosticClearResteEmissionRelatedInfo in the given context.
        self.clearResetEmissionRelatedDiagnosticInfoClassRef: Optional[RefType] = None

    def getClearResetEmissionRelatedDiagnosticInfoClassRef(self) -> Optional[RefType]:
        """
        This reference substantiates that abstract reference in the role serviceClass for this specific concrete class. Thereby, the reference represents the ability to access shared attributes among all DiagnosticClearResteEmissionRelatedInfo in the given context.
        """
        return self.clearResetEmissionRelatedDiagnosticInfoClassRef

    def setClearResetEmissionRelatedDiagnosticInfoClassRef(self, value: Optional[RefType]) -> DiagnosticClearResetEmissionRelatedInfo:
        """
        This reference substantiates that abstract reference in the role serviceClass for this specific concrete class. Thereby, the reference represents the ability to access shared attributes among all DiagnosticClearResteEmissionRelatedInfo in the given context.

        A None value is a no-op and does not overwrite an existing clearResetEmissionRelatedDiagnosticInfoClassRef.
        """
        if value is not None:
            self.clearResetEmissionRelatedDiagnosticInfoClassRef = value
        return self


class DiagnosticDataByIdentifier(ARElement, ABC):
    """This represents an abstract base class for all diagnostic services that access data by identifier."""

    # DiagnosticDataByIdentifier method parity checklist:
    # Spec: AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf, Table 4.73, p.113
    # Columns: impl / docstring / test / reader / writer / release   ([—] = no XML element)
    # [x] __init__               [x] impl  [x] docstring  [x] test  [—] reader  [—] writer  R23-11
    # [x] getDataIdentifier      [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setDataIdentifier      [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11

    def __init__(self, parent: ARObject, short_name: str):
        if type(self) is DiagnosticDataByIdentifier:
            raise TypeError("DiagnosticDataByIdentifier is an abstract class.")

        super().__init__(parent, short_name)

        # This represents the linked DiagnosticDataIdentifier.
        self.dataIdentifier: Optional[RefType] = None

    def getDataIdentifier(self) -> Optional[RefType]:
        """
        This represents the linked DiagnosticDataIdentifier.
        """
        return self.dataIdentifier

    def setDataIdentifier(self, value: Optional[RefType]) -> DiagnosticDataByIdentifier:
        """
        This represents the linked DiagnosticDataIdentifier.

        A None value is a no-op and does not overwrite an existing dataIdentifier.
        """
        if value is not None:
            self.dataIdentifier = value
        return self


class DiagnosticDataIdentifier(DiagnosticAbstractDataIdentifier):
    """
    This meta-class represents the ability to model a diagnostic data identifier (DID) that is fully specified regarding the payload at configuration-time.
    """

    # DiagnosticDataIdentifier method parity checklist:
    # Spec: AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf, Table 4.2, p.34
    # Columns: impl / docstring / test / reader / writer / release   ([—] = no XML element)
    # [x] __init__            [x] impl  [x] docstring  [x] test  [—] reader  [—] writer  R23-11
    # [x] addDataElement      [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getDataElements     [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] getDidSize          [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setDidSize          [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getRepresentsVin    [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setRepresentsVin    [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getSupportInfoByte  [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setSupportInfoByte  [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11

    def __init__(self, parent: ARObject, short_name: str):
        super().__init__(parent, short_name)

        # This is the dataElement associated with the Diagnostic DataIdentifier. Stereotypes: atpSplitable; atpVariation Tags: atp.Splitkey=dataElement.bitOffset, data Element.ident.shortName, dataElement.variation Point.shortLabel vh.latestBindingTime=postBuild
        self.dataElements: List[DiagnosticParameter] = []

        # This attribute indicates the size in bytes of the Diagnostic DataIdentifier.
        self.didSize: Optional[PositiveInteger] = None

        # This attributes indicates whether the specific Diagnostic DataIdentifier represents the vehicle identification.
        self.representsVin: Optional[Boolean] = None

        # This attribute represents the supported information associated with the DiagnosticDataIdentifier.
        self.supportInfoByte: Optional[DiagnosticSupportInfoByte] = None

    def addDataElement(self, value: Optional[DiagnosticParameter]) -> DiagnosticDataIdentifier:
        """
        This is the dataElement associated with the Diagnostic DataIdentifier.
        A None value is a no-op and does not append a dataElement.
        """
        if value is not None:
            self.dataElements.append(value)
        return self

    def getDataElements(self) -> List[DiagnosticParameter]:
        """
        This is the dataElement associated with the Diagnostic DataIdentifier.
        """
        return self.dataElements

    def getDidSize(self) -> Optional[PositiveInteger]:
        """
        This attribute indicates the size in bytes of the Diagnostic DataIdentifier.
        """
        return self.didSize

    def setDidSize(self, value: Optional[PositiveInteger]) -> DiagnosticDataIdentifier:
        """
        This attribute indicates the size in bytes of the Diagnostic DataIdentifier.
        A None value is a no-op and does not overwrite an existing didSize.
        """
        if value is not None:
            self.didSize = value
        return self

    def getRepresentsVin(self) -> Optional[Boolean]:
        """
        This attributes indicates whether the specific Diagnostic DataIdentifier represents the vehicle identification.
        """
        return self.representsVin

    def setRepresentsVin(self, value: Optional[Boolean]) -> DiagnosticDataIdentifier:
        """
        This attributes indicates whether the specific Diagnostic DataIdentifier represents the vehicle identification.
        A None value is a no-op and does not overwrite an existing representsVin.
        """
        if value is not None:
            self.representsVin = value
        return self

    def getSupportInfoByte(self) -> Optional[DiagnosticSupportInfoByte]:
        """
        This attribute represents the supported information associated with the DiagnosticDataIdentifier.
        """
        return self.supportInfoByte

    def setSupportInfoByte(self, value: Optional[DiagnosticSupportInfoByte]) -> DiagnosticDataIdentifier:
        """
        This attribute represents the supported information associated with the DiagnosticDataIdentifier.
        A None value is a no-op and does not overwrite an existing supportInfoByte.
        """
        if value is not None:
            self.supportInfoByte = value
        return self


class DiagnosticDataIdentifierSet(DiagnosticCommonElement):
    """
    This represents the ability to define a list of DiagnosticDataIdentifiers that can be reused in different contexts. Tags: atp.recommendedPackage=DiagnosticDataIdentifierSets
    """

    # DiagnosticDataIdentifierSet method parity checklist:
    # Spec: AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf, Table 4.178, p.187
    # Columns: impl / docstring / test / reader / writer / release   ([—] = no XML element)
    # [x] __init__               [x] impl  [x] docstring  [x] test  [—] reader  [—] writer  R23-11
    # [x] addDataIdentifierRef   [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getDataIdentifierRefs  [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11

    def __init__(self, parent: ARObject, short_name: str):
        super().__init__(parent, short_name)

        # Reference to an ordered list of Data Identifiers.
        self.dataIdentifierRefs: List[RefType] = []

    def addDataIdentifierRef(self, ref: Optional[RefType]) -> DiagnosticDataIdentifierSet:
        """
        Reference to an ordered list of Data Identifiers.

        A None value is a no-op and does not extend the dataIdentifierRefs list.
        """
        if ref is not None:
            self.dataIdentifierRefs.append(ref)
        return self

    def getDataIdentifierRefs(self) -> List[RefType]:
        """
        Reference to an ordered list of Data Identifiers.
        """
        return self.dataIdentifierRefs


class DiagnosticMemoryByAddress(ARElement, ABC):
    """This represents an abstract base class for diagnostic services that deal with accessing memory by address."""

    # DiagnosticMemoryByAddress method parity checklist:
    # Spec: AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf, Table 4.110, p.139
    # Columns: impl / docstring / test / reader / writer / release   ([—] = no XML element)
    # [x] __init__  [x] impl  [x] docstring  [x] test  [—] reader  [—] writer  R23-11

    def __init__(self, parent: ARObject, short_name: str):
        if type(self) is DiagnosticMemoryByAddress:
            raise TypeError("DiagnosticMemoryByAddress is an abstract class.")

        super().__init__(parent, short_name)


class DiagnosticDataTransfer(DiagnosticMemoryByAddress):
    """This represents an instance of the "Data Transfer" diagnostic service. Tags: atp.recommendedPackage=DiagnosticMemoryByAdresss"""

    # DiagnosticDataTransfer method parity checklist:
    # Spec: AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf, Table 4.119, p.143
    # Columns: impl / docstring / test / reader / writer / release   ([—] = no XML element)
    # [x] __init__                 [x] impl  [x] docstring  [x] test  [—] reader  [—] writer  R23-11
    # [x] getDataTransferClassRef  [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setDataTransferClassRef  [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11

    def __init__(self, parent: ARObject, short_name: str):
        super().__init__(parent, short_name)

        # This reference substantiates that abstract reference in the role serviceClass for this specific concrete class. Thereby, the reference represents the ability to access shared attributes among all DiagnosticDataTransfer in the given context.
        self.dataTransferClassRef: Optional[RefType] = None

    def getDataTransferClassRef(self) -> Optional[RefType]:
        """
        This reference substantiates that abstract reference in the role serviceClass for this specific concrete class. Thereby, the reference represents the ability to access shared attributes among all DiagnosticDataTransfer in the given context.
        """
        return self.dataTransferClassRef

    def setDataTransferClassRef(self, value: Optional[RefType]) -> DiagnosticDataTransfer:
        """
        This reference substantiates that abstract reference in the role serviceClass for this specific concrete class. Thereby, the reference represents the ability to access shared attributes among all DiagnosticDataTransfer in the given context.

        A None value is a no-op and does not overwrite an existing dataTransferClassRef.
        """
        if value is not None:
            self.dataTransferClassRef = value
        return self


class DiagnosticDeAuthentication(DiagnosticAuthentication):
    """This meta-class represents the subfunction to remove the authentication"""

    # DiagnosticDeAuthentication method parity checklist:
    # Spec: AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf, Table 4.56, p.100
    # Columns: impl / docstring / test / reader / writer / release   ([—] = no XML element)
    # [x] __init__  [x] impl  [x] docstring  [x] test  [x] reader  [x] writer  R23-11

    def __init__(self, parent: ARObject, short_name: str):
        super().__init__(parent, short_name)


class DiagnosticDemProvidedDataMapping(DiagnosticMapping):
    """This represents the ability to define the nature of a data access for a DiagnosticDataElement in the Dem. Tags: atp.recommendedPackage=DiagnosticServiceMappings"""

    # DiagnosticDemProvidedDataMapping method parity checklist:
    # Spec: AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf, Table 5.28, p.255
    # Columns: impl / docstring / test / reader / writer / release   ([—] = no XML element)
    # [x] __init__                           [x] impl  [x] docstring  [x] test  [—] reader  [—] writer  R23-11
    # [x] getDataElementRef                     [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setDataElementRef                     [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getDataProvider                       [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setDataProvider                       [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11

    def __init__(self, parent: ARObject, short_name: str):
        super().__init__(parent, short_name)

        # This represents the DiagnosticDataElement for which the access is further qualified by the DiagnosticDemProvidedDataMapping.
        self.dataElementRef: Optional[RefType] = None

        # This represents the ability to further specify the access within the Dem.
        self.dataProvider: Optional[NameToken] = None

    def getDataElementRef(self) -> Optional[RefType]:
        """
        This represents the DiagnosticDataElement for which the access is further qualified by the DiagnosticDemProvidedDataMapping.
        """
        return self.dataElementRef

    def setDataElementRef(self, value: Optional[RefType]) -> DiagnosticDemProvidedDataMapping:
        """
        This represents the DiagnosticDataElement for which the access is further qualified by the DiagnosticDemProvidedDataMapping.
        A None value is a no-op and does not overwrite an existing dataElementRef.
        """
        if value is not None:
            self.dataElementRef = value
        return self

    def getDataProvider(self) -> Optional[NameToken]:
        """
        This represents the ability to further specify the access within the Dem.
        """
        return self.dataProvider

    def setDataProvider(self, value: Optional[NameToken]) -> DiagnosticDemProvidedDataMapping:
        """
        This represents the ability to further specify the access within the Dem.
        A None value is a no-op and does not overwrite an existing dataProvider.
        """
        if value is not None:
            self.dataProvider = value
        return self


class DiagnosticDynamicDataIdentifier(DiagnosticAbstractDataIdentifier):
    """
    This meta-class represents the ability to define a diagnostic data identifier (DID) at run-time.
    """

    # DiagnosticDynamicDataIdentifier method parity checklist:
    # Spec: AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf, Table 4.3, p.34
    # Columns: impl / docstring / test / reader / writer / release   ([—] = no XML element)
    # [x] __init__  [x] impl  [x] docstring  [x] test  [—] reader  [—] writer  R23-11
    # (no own attributes; base id coverage via readDiagnosticAbstractDataIdentifier/writeDiagnosticAbstractDataIdentifier, own coverage via the DIAGNOSTIC-DYNAMIC-DATA-IDENTIFIER dispatch)

    def __init__(self, parent: ARObject, short_name: str):
        super().__init__(parent, short_name)


class DiagnosticDynamicallyDefineDataIdentifier(ARElement):
    """This represents an instance of the "Dynamically Define Data Identifier" diagnostic service."""

    # DiagnosticDynamicallyDefineDataIdentifier method parity checklist:
    # Spec: AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf, Table 4.93, p.127
    # Columns: impl / docstring / test / reader / writer / release   ([—] = no XML element)
    # [x] __init__                                 [x] impl  [x] docstring  [x] test  [—] reader  [—] writer  R23-11
    # [x] getDataIdentifier                        [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setDataIdentifier                        [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getDynamicallyDefineDataIdentifierClass  [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setDynamicallyDefineDataIdentifierClass  [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getMaxSourceElement                      [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setMaxSourceElement                      [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11

    def __init__(self, parent: ARObject, short_name: str):
        super().__init__(parent, short_name)

        # This represents the applicable DiagnosticDynamicData Identfier.
        self.dataIdentifier: Optional[RefType] = None

        # This reference substantiates that abstract reference in the role serviceClass for this specific concrete class. Thereby, the reference represents the ability to access shared attributes among all DiagnosticDynamicallyDefineDataIdentifier in the given context.
        self.dynamicallyDefineDataIdentifierClass: Optional[RefType] = None

        # This represents the maximum number of source elements of the dynamically created DID.
        self.maxSourceElement: Optional[PositiveInteger] = None

    def getDataIdentifier(self) -> Optional[RefType]:
        """
        This represents the applicable DiagnosticDynamicData Identfier.
        """
        return self.dataIdentifier

    def setDataIdentifier(self, value: Optional[RefType]) -> DiagnosticDynamicallyDefineDataIdentifier:
        """
        This represents the applicable DiagnosticDynamicData Identfier.

        A None value is a no-op and does not overwrite an existing dataIdentifier.
        """
        if value is not None:
            self.dataIdentifier = value
        return self

    def getDynamicallyDefineDataIdentifierClass(self) -> Optional[RefType]:
        """
        This reference substantiates that abstract reference in the role serviceClass for this specific concrete class. Thereby, the reference represents the ability to access shared attributes among all DiagnosticDynamicallyDefineDataIdentifier in the given context.
        """
        return self.dynamicallyDefineDataIdentifierClass

    def setDynamicallyDefineDataIdentifierClass(self, value: Optional[RefType]) -> DiagnosticDynamicallyDefineDataIdentifier:
        """
        This reference substantiates that abstract reference in the role serviceClass for this specific concrete class. Thereby, the reference represents the ability to access shared attributes among all DiagnosticDynamicallyDefineDataIdentifier in the given context.

        A None value is a no-op and does not overwrite an existing dynamicallyDefineDataIdentifierClass.
        """
        if value is not None:
            self.dynamicallyDefineDataIdentifierClass = value
        return self

    def getMaxSourceElement(self) -> Optional[PositiveInteger]:
        """
        This represents the maximum number of source elements of the dynamically created DID.
        """
        return self.maxSourceElement

    def setMaxSourceElement(self, value: Optional[PositiveInteger]) -> DiagnosticDynamicallyDefineDataIdentifier:
        """
        This represents the maximum number of source elements of the dynamically created DID.

        A None value is a no-op and does not overwrite an existing maxSourceElement.
        """
        if value is not None:
            self.maxSourceElement = value
        return self


class DiagnosticEcuInstanceProps(ARElement):
    """
    This meta-class represents the ability to model properties that are specific for a given EcuInstance but on the other hand represent purely diagnostic-related information. In the spirit of decentralized configuration it is therefore possible to specify the diagnostic-related information related to a given EcuInstance even if the EcuInstance does not yet exist. Tags: atp.recommendedPackage=DiagnosticEcuInstancePropss
    """

    # DiagnosticEcuInstanceProps method parity checklist:
    # Spec: AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf, Table 4.205, p.207
    # Columns: impl / docstring / test / reader / writer / release   ([—] = no XML element)
    # [x] __init__               [x] impl  [x] docstring  [x] test  [—] reader  [—] writer  R23-11
    # [x] addEcuInstanceRef      [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getEcuInstanceRefs     [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] getObdSupport          [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setObdSupport          [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11

    def __init__(self, parent: ARObject, short_name: str):
        super().__init__(parent, short_name)

        # This represents the actual EcuInstance to which the information contained in the DiagnosticEcuInstance contribute. Stereotypes: atpSplitable Tags: atp.Splitkey=ecuInstance
        self.ecuInstanceRefs: List[RefType] = []

        # This attribute is used to specify the role (if applicable) in which the DiagnosticEcuInstance supports OBD.
        self.obdSupport: Optional[DiagnosticObdSupportEnum] = None

    def addEcuInstanceRef(self, ref: Optional[RefType]) -> DiagnosticEcuInstanceProps:
        """
        This represents the actual EcuInstance to which the information contained in the DiagnosticEcuInstance contribute. Stereotypes: atpSplitable Tags: atp.Splitkey=ecuInstance

        A None value is a no-op and does not extend the ecuInstanceRefs list.
        """
        if ref is not None:
            self.ecuInstanceRefs.append(ref)
        return self

    def getEcuInstanceRefs(self) -> List[RefType]:
        """
        This represents the actual EcuInstance to which the information contained in the DiagnosticEcuInstance contribute. Stereotypes: atpSplitable Tags: atp.Splitkey=ecuInstance
        """
        return self.ecuInstanceRefs

    def getObdSupport(self) -> Optional[DiagnosticObdSupportEnum]:
        """
        This attribute is used to specify the role (if applicable) in which the DiagnosticEcuInstance supports OBD.
        """
        return self.obdSupport

    def setObdSupport(self, value: Optional[DiagnosticObdSupportEnum]) -> DiagnosticEcuInstanceProps:
        """
        This attribute is used to specify the role (if applicable) in which the DiagnosticEcuInstance supports OBD.

        A None value is a no-op and does not overwrite an existing obdSupport.
        """
        if value is not None:
            self.obdSupport = value
        return self


class DiagnosticEcuReset(ARElement):
    """This represents an instance of the "ECU Reset" diagnostic service."""

    # DiagnosticEcuReset method parity checklist:
    # Spec: AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf, Table 4.60, p.102
    # Columns: impl / docstring / test / reader / writer / release   ([—] = no XML element)
    # [x] __init__                    [x] impl  [x] docstring  [x] test  [—] reader  [—] writer  R23-11
    # [x] getCustomSubFunctionNumber  [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setCustomSubFunctionNumber  [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getEcuResetClass            [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setEcuResetClass            [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11

    def __init__(self, parent: ARObject, short_name: str):
        super().__init__(parent, short_name)

        # This attribute shall be used to define a custom sub-function number if none of the standardized values of category shall be used.
        self.customSubFunctionNumber: Optional[PositiveInteger] = None

        # This reference substantiates that abstract reference in the role serviceClass for this specific concrete class. Thereby, the reference represents the ability to access shared attributes among all DiagnosticEcuReset in the given context.
        self.ecuResetClass: Optional[RefType] = None

    def getCustomSubFunctionNumber(self) -> Optional[PositiveInteger]:
        """
        This attribute shall be used to define a custom sub-function number if none of the standardized values of category shall be used.
        """
        return self.customSubFunctionNumber

    def setCustomSubFunctionNumber(self, value: Optional[PositiveInteger]) -> DiagnosticEcuReset:
        """
        This attribute shall be used to define a custom sub-function number if none of the standardized values of category shall be used.

        A None value is a no-op and does not overwrite an existing customSubFunctionNumber.
        """
        if value is not None:
            self.customSubFunctionNumber = value
        return self

    def getEcuResetClass(self) -> Optional[RefType]:
        """
        This reference substantiates that abstract reference in the role serviceClass for this specific concrete class. Thereby, the reference represents the ability to access shared attributes among all DiagnosticEcuReset in the given context.
        """
        return self.ecuResetClass

    def setEcuResetClass(self, value: Optional[RefType]) -> DiagnosticEcuReset:
        """
        This reference substantiates that abstract reference in the role serviceClass for this specific concrete class. Thereby, the reference represents the ability to access shared attributes among all DiagnosticEcuReset in the given context.

        A None value is a no-op and does not overwrite an existing ecuResetClass.
        """
        if value is not None:
            self.ecuResetClass = value
        return self


class DiagnosticEnableCondition(DiagnosticCondition):
    """Specification of an enable condition. Tags: atp.recommendedPackage=DiagnosticConditions"""

    # DiagnosticEnableCondition method parity checklist:
    # Spec: AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf, Table 4.185, p.194
    # Columns: impl / docstring / test / reader / writer / release   ([—] = no XML element)
    # [x] __init__     [x] impl  [x] docstring  [x] test  [—] reader  [—] writer  R23-11

    def __init__(self, parent: ARObject, short_name: str):
        super().__init__(parent, short_name)


class DiagnosticEnableConditionGroup(DiagnosticConditionGroup):
    """
    Enable condition group which includes one or several enable conditions. Tags: atp.recommendedPackage=DiagnosticConditions

    [constr_1841] Existence of attribute DiagnosticEnableConditionGroup.enableCondition: For each DiagnosticEnableConditionGroup, attribute enableCondition shall exist at the time when the DEXT is complete.
    """

    # DiagnosticEnableConditionGroup method parity checklist:
    # Spec: AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf, Table 4.194, p.200
    # Columns: impl / docstring / test / reader / writer / release   ([—] = no XML element)
    # [x] __init__                    [x] impl  [x] docstring  [x] test  [—] reader  [—] writer  R23-11
    # [x] addEnableConditionRef       [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getEnableConditionRefs      [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11

    def __init__(self, parent: ARObject, short_name: str):
        super().__init__(parent, short_name)

        # Reference to enableConditions that are part of the Enable ConditionGroup.
        self.enableConditionRefs: List[RefType] = []

    def addEnableConditionRef(self, ref: Optional[RefType]) -> DiagnosticEnableConditionGroup:
        """
        Reference to enableConditions that are part of the Enable ConditionGroup.

        A None value is a no-op and does not extend the enableConditionRefs list.
        """
        if ref is not None:
            self.enableConditionRefs.append(ref)
        return self

    def getEnableConditionRefs(self) -> List[RefType]:
        """
        Reference to enableConditions that are part of the Enable ConditionGroup.
        """
        return self.enableConditionRefs


class DiagnosticEvent(ARElement):
    """
    This element is used to configure DiagnosticEvents.
    """

    # DiagnosticEvent method parity checklist:
    # Spec: AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf, Table 4.149, p.165
    # Columns: impl / docstring / test / reader / writer / release   ([—] = no XML element)
    # [x] __init__                           [x] impl  [x] docstring  [x] test  [—] reader  [—] writer  R23-11
    # [x] getAssociatedEventIdentification   [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setAssociatedEventIdentification   [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getClearEventAllowedBehavior       [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setClearEventAllowedBehavior       [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getConfirmationThreshold           [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setConfirmationThreshold           [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] addConnectedIndicator              [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getConnectedIndicators             [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] getEventClearAllowed               [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setEventClearAllowed               [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getEventKind                       [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setEventKind                       [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getPrestorageFreezeFrame           [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setPrestorageFreezeFrame           [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getPrestoredFreezeframeStoredInNvm [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setPrestoredFreezeframeStoredInNvm [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getRecoverableInSameOperationCycle [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setRecoverableInSameOperationCycle [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11

    def __init__(self, parent: ARObject, short_name: str):
        super().__init__(parent, short_name)

        # This attribute represents the identification number that is associated with the enclosing DiagnosticEvent and allows to identify it when placed into a snapshot record or extended data record storage. This value can be reported as internal data element in snapshot records or extended data records.
        self.associatedEventIdentification: Optional[PositiveInteger] = None

        # This attribute defines the resulting UDS status byte for the related event, which shall not be cleared according to the ClearEventAllowed callback
        self.clearEventAllowedBehavior: Optional[DiagnosticClearEventAllowedBehaviorEnum] = None

        # This attribute defines the number of operation cycles with a failed result before a confirmed DTC is set to 1. The semantic of this attribute is a by "1" increased value compared to the confirmation threshold of the "trip counter" mentioned in ISO 14229-1 in figure D.4. A value of "1" defines the immediate confirmation of the DTC along with the first reported failed. This is also sometimes called "zero trip DTC". A value of "2" defines a DTC confirmation in the operation cycle after the first occurred failed. A value of "2" is typically used in the US for OBD DTC confirmation. Stereotypes: atpVariation Tags: vh.latestBindingTime=preCompileTime
        self.confirmationThreshold: Optional[PositiveInteger] = None

        # Event specific description of Indicators. Stereotypes: atpSplitable; atpVariation Tags: atp.Splitkey=connectedIndicator.shortName, connectedIndicator.variationPoint.shortLabel vh.latestBindingTime=postBuild
        self.connectedIndicators: List[DiagnosticConnectedIndicator] = []

        # This attribute defines whether the Dem has access to a "ClearEventAllowed" callback.
        self.eventClearAllowed: Optional[DiagnosticEventClearAllowedEnum] = None

        # This attribute is used to distinguish between SWC and BSW events.
        self.eventKind: Optional[DiagnosticEventKindEnum] = None

        # This attribute describes whether the Prestorage of FreezeFrames is supported by the assigned event or not. true: Prestorage of FreezeFrames is supported fFalse: Prestorage of FreezeFrames is not supported
        self.prestorageFreezeFrame: Optional[Boolean] = None

        # If the Event uses a prestored freeze-frame (using the operations PrestoreFreezeFrame and ClearPrestoredFreezeFrame of the service interface DiagnosticMonitor) this attribute indicates if the Event requires the data to be stored in non-volatile memory. TRUE = Dem shall store the prestored data in non-volatile memory, FALSE = Data can be lost at shutdown (not stored in Nvm)
        self.prestoredFreezeframeStoredInNvm: Optional[Boolean] = None

        # If the attribute is set to true then reporting PASSED will reset the indication of a failed test in the current operation cycle. If the attribute is set to false then reporting PASSED will be ignored and not lead to a reset of the indication of a failed test.
        self.recoverableInSameOperationCycle: Optional[Boolean] = None

    def getAssociatedEventIdentification(self) -> Optional[PositiveInteger]:
        """
        This attribute represents the identification number that is associated with the enclosing DiagnosticEvent and allows to identify it when placed into a snapshot record or extended data record storage. This value can be reported as internal data element in snapshot records or extended data records.
        """
        return self.associatedEventIdentification

    def setAssociatedEventIdentification(self, value: Optional[PositiveInteger]) -> DiagnosticEvent:
        """
        This attribute represents the identification number that is associated with the enclosing DiagnosticEvent and allows to identify it when placed into a snapshot record or extended data record storage. This value can be reported as internal data element in snapshot records or extended data records.

        A None value is a no-op and does not overwrite an existing associatedEventIdentification.
        """
        if value is not None:
            self.associatedEventIdentification = value
        return self

    def getClearEventAllowedBehavior(self) -> Optional[DiagnosticClearEventAllowedBehaviorEnum]:
        """
        This attribute defines the resulting UDS status byte for the related event, which shall not be cleared according to the ClearEventAllowed callback
        """
        return self.clearEventAllowedBehavior

    def setClearEventAllowedBehavior(self, value: Optional[DiagnosticClearEventAllowedBehaviorEnum]) -> DiagnosticEvent:
        """
        This attribute defines the resulting UDS status byte for the related event, which shall not be cleared according to the ClearEventAllowed callback

        A None value is a no-op and does not overwrite an existing clearEventAllowedBehavior.
        """
        if value is not None:
            self.clearEventAllowedBehavior = value
        return self

    def getConfirmationThreshold(self) -> Optional[PositiveInteger]:
        """
        This attribute defines the number of operation cycles with a failed result before a confirmed DTC is set to 1. The semantic of this attribute is a by "1" increased value compared to the confirmation threshold of the "trip counter" mentioned in ISO 14229-1 in figure D.4. A value of "1" defines the immediate confirmation of the DTC along with the first reported failed. This is also sometimes called "zero trip DTC". A value of "2" defines a DTC confirmation in the operation cycle after the first occurred failed. A value of "2" is typically used in the US for OBD DTC confirmation. Stereotypes: atpVariation Tags: vh.latestBindingTime=preCompileTime
        """
        return self.confirmationThreshold

    def setConfirmationThreshold(self, value: Optional[PositiveInteger]) -> DiagnosticEvent:
        """
        This attribute defines the number of operation cycles with a failed result before a confirmed DTC is set to 1. The semantic of this attribute is a by "1" increased value compared to the confirmation threshold of the "trip counter" mentioned in ISO 14229-1 in figure D.4. A value of "1" defines the immediate confirmation of the DTC along with the first reported failed. This is also sometimes called "zero trip DTC". A value of "2" defines a DTC confirmation in the operation cycle after the first occurred failed. A value of "2" is typically used in the US for OBD DTC confirmation. Stereotypes: atpVariation Tags: vh.latestBindingTime=preCompileTime

        A None value is a no-op and does not overwrite an existing confirmationThreshold.
        """
        if value is not None:
            self.confirmationThreshold = value
        return self

    def addConnectedIndicator(self, indicator: Optional[DiagnosticConnectedIndicator]) -> DiagnosticEvent:
        """
        Event specific description of Indicators. Stereotypes: atpSplitable; atpVariation Tags: atp.Splitkey=connectedIndicator.shortName, connectedIndicator.variationPoint.shortLabel vh.latestBindingTime=postBuild

        A None value is a no-op and does not extend the connectedIndicators list.
        """
        if indicator is not None:
            self.connectedIndicators.append(indicator)
        return self

    def getConnectedIndicators(self) -> List[DiagnosticConnectedIndicator]:
        """
        Event specific description of Indicators. Stereotypes: atpSplitable; atpVariation Tags: atp.Splitkey=connectedIndicator.shortName, connectedIndicator.variationPoint.shortLabel vh.latestBindingTime=postBuild
        """
        return self.connectedIndicators

    def getEventClearAllowed(self) -> Optional[DiagnosticEventClearAllowedEnum]:
        """
        This attribute defines whether the Dem has access to a "ClearEventAllowed" callback.
        """
        return self.eventClearAllowed

    def setEventClearAllowed(self, value: Optional[DiagnosticEventClearAllowedEnum]) -> DiagnosticEvent:
        """
        This attribute defines whether the Dem has access to a "ClearEventAllowed" callback.

        A None value is a no-op and does not overwrite an existing eventClearAllowed.
        """
        if value is not None:
            self.eventClearAllowed = value
        return self

    def getEventKind(self) -> Optional[DiagnosticEventKindEnum]:
        """
        This attribute is used to distinguish between SWC and BSW events.
        """
        return self.eventKind

    def setEventKind(self, value: Optional[DiagnosticEventKindEnum]) -> DiagnosticEvent:
        """
        This attribute is used to distinguish between SWC and BSW events.

        A None value is a no-op and does not overwrite an existing eventKind.
        """
        if value is not None:
            self.eventKind = value
        return self

    def getPrestorageFreezeFrame(self) -> Optional[Boolean]:
        """
        This attribute describes whether the Prestorage of FreezeFrames is supported by the assigned event or not. true: Prestorage of FreezeFrames is supported fFalse: Prestorage of FreezeFrames is not supported
        """
        return self.prestorageFreezeFrame

    def setPrestorageFreezeFrame(self, value: Optional[Boolean]) -> DiagnosticEvent:
        """
        This attribute describes whether the Prestorage of FreezeFrames is supported by the assigned event or not. true: Prestorage of FreezeFrames is supported fFalse: Prestorage of FreezeFrames is not supported

        A None value is a no-op and does not overwrite an existing prestorageFreezeFrame.
        """
        if value is not None:
            self.prestorageFreezeFrame = value
        return self

    def getPrestoredFreezeframeStoredInNvm(self) -> Optional[Boolean]:
        """
        If the Event uses a prestored freeze-frame (using the operations PrestoreFreezeFrame and ClearPrestoredFreezeFrame of the service interface DiagnosticMonitor) this attribute indicates if the Event requires the data to be stored in non-volatile memory. TRUE = Dem shall store the prestored data in non-volatile memory, FALSE = Data can be lost at shutdown (not stored in Nvm)
        """
        return self.prestoredFreezeframeStoredInNvm

    def setPrestoredFreezeframeStoredInNvm(self, value: Optional[Boolean]) -> DiagnosticEvent:
        """
        If the Event uses a prestored freeze-frame (using the operations PrestoreFreezeFrame and ClearPrestoredFreezeFrame of the service interface DiagnosticMonitor) this attribute indicates if the Event requires the data to be stored in non-volatile memory. TRUE = Dem shall store the prestored data in non-volatile memory, FALSE = Data can be lost at shutdown (not stored in Nvm)

        A None value is a no-op and does not overwrite an existing prestoredFreezeframeStoredInNvm.
        """
        if value is not None:
            self.prestoredFreezeframeStoredInNvm = value
        return self

    def getRecoverableInSameOperationCycle(self) -> Optional[Boolean]:
        """
        If the attribute is set to true then reporting PASSED will reset the indication of a failed test in the current operation cycle. If the attribute is set to false then reporting PASSED will be ignored and not lead to a reset of the indication of a failed test.
        """
        return self.recoverableInSameOperationCycle

    def setRecoverableInSameOperationCycle(self, value: Optional[Boolean]) -> DiagnosticEvent:
        """
        If the attribute is set to true then reporting PASSED will reset the indication of a failed test in the current operation cycle. If the attribute is set to false then reporting PASSED will be ignored and not lead to a reset of the indication of a failed test.

        A None value is a no-op and does not overwrite an existing recoverableInSameOperationCycle.
        """
        if value is not None:
            self.recoverableInSameOperationCycle = value
        return self


class DiagnosticSwMapping(DiagnosticMapping, ABC):
    """This represents the ability to define a mapping between a diagnostic information (at this point there is no way to become more specific about the semantics) to a software-component."""

    # DiagnosticSwMapping method parity checklist:
    # Spec: AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf, Table 5.14, p.238
    # Columns: impl / docstring / test / reader / writer / release   ([—] = no XML element)
    # [x] __init__     [x] impl  [x] docstring  [x] test  [—] reader  [—] writer  R23-11

    def __init__(self, parent: ARObject, short_name: str):
        if type(self) is DiagnosticSwMapping:
            raise TypeError("DiagnosticSwMapping is an abstract class.")

        super().__init__(parent, short_name)


class DiagnosticEnableConditionPortMapping(DiagnosticSwMapping):
    """Defines to which SWC service ports the DiagnosticEnableCondition is mapped. Tags: atp.recommendedPackage=DiagnosticMappings"""

    # DiagnosticEnableConditionPortMapping method parity checklist:
    # Spec: AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf, Table 5.26, p.252
    # Columns: impl / docstring / test / reader / writer / release   ([—] = no XML element)
    # [x] __init__                [x] impl  [x] docstring  [x] test  [—] reader  [—] writer  R23-11
    # [x] getEnableConditionRef                        [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setEnableConditionRef                        [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getSwcFlatServiceDependencyRef               [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setSwcFlatServiceDependencyRef               [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getSwcServiceDependencyInSystemIRef          [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setSwcServiceDependencyInSystemIRef          [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11

    def __init__(self, parent: ARObject, short_name: str):
        super().__init__(parent, short_name)

        # Reference to the EnableCondition which is mapped to a SWC service port.
        self.enableConditionRef: Optional[RefType] = None

        # Reference to a SwcServiceDependencyType that links ServiceNeeds to SWC service ports. This reference can be used in early stages of the development in order to identify the SwcServiceDependency without a full System Context.
        self.swcFlatServiceDependencyRef: Optional[RefType] = None

        # Instance reference to a SwcServiceDependency that links ServiceNeeds to SWC service ports. InstanceRef implemented by: SwcServiceDependencyInSystemInstanceRef
        self.swcServiceDependencyInSystemIRef: Optional[RefType] = None

    def getEnableConditionRef(self) -> Optional[RefType]:
        """
        Reference to the EnableCondition which is mapped to a SWC service port.
        """
        return self.enableConditionRef

    def setEnableConditionRef(self, value: Optional[RefType]) -> DiagnosticEnableConditionPortMapping:
        """
        Reference to the EnableCondition which is mapped to a SWC service port.
        A None value is a no-op and does not overwrite an existing enableConditionRef.
        """
        if value is not None:
            self.enableConditionRef = value
        return self

    def getSwcFlatServiceDependencyRef(self) -> Optional[RefType]:
        """
        Reference to a SwcServiceDependencyType that links ServiceNeeds to SWC service ports. This reference can be used in early stages of the development in order to identify the SwcServiceDependency without a full System Context.
        """
        return self.swcFlatServiceDependencyRef

    def setSwcFlatServiceDependencyRef(self, value: Optional[RefType]) -> DiagnosticEnableConditionPortMapping:
        """
        Reference to a SwcServiceDependencyType that links ServiceNeeds to SWC service ports. This reference can be used in early stages of the development in order to identify the SwcServiceDependency without a full System Context.
        A None value is a no-op and does not overwrite an existing swcFlatServiceDependencyRef.
        """
        if value is not None:
            self.swcFlatServiceDependencyRef = value
        return self

    def getSwcServiceDependencyInSystemIRef(self) -> Optional[RefType]:
        """
        Instance reference to a SwcServiceDependency that links ServiceNeeds to SWC service ports. InstanceRef implemented by: SwcServiceDependencyInSystemInstanceRef
        """
        return self.swcServiceDependencyInSystemIRef

    def setSwcServiceDependencyInSystemIRef(self, value: Optional[RefType]) -> DiagnosticEnableConditionPortMapping:
        """
        Instance reference to a SwcServiceDependency that links ServiceNeeds to SWC service ports. InstanceRef implemented by: SwcServiceDependencyInSystemInstanceRef
        A None value is a no-op and does not overwrite an existing swcServiceDependencyInSystemIRef.
        """
        if value is not None:
            self.swcServiceDependencyInSystemIRef = value
        return self


class DiagnosticEventPortMapping(DiagnosticSwMapping):
    """Defines to which SWC service ports the DiagnosticEvent is mapped. Tags: atp.recommendedPackage=DiagnosticMappings"""

    # DiagnosticEventPortMapping method parity checklist:
    # Spec: AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf, Table 5.24, p.249
    # Columns: impl / docstring / test / reader / writer / release   ([—] = no XML element)
    # [x] __init__                [x] impl  [x] docstring  [x] test  [—] reader  [—] writer  R23-11
    # [x] getBswServiceDependencyRef                   [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setBswServiceDependencyRef                   [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getDiagnosticEventRef                        [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setDiagnosticEventRef                        [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getSwcFlatServiceDependencyRef               [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setSwcFlatServiceDependencyRef               [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getSwcServiceDependencyInSystemIRef          [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setSwcServiceDependencyInSystemIRef          [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11

    def __init__(self, parent: ARObject, short_name: str):
        super().__init__(parent, short_name)

        # Reference to a BswServiceDependency that links ServiceNeeds to BswModuleEntries.
        self.bswServiceDependencyRef: Optional[RefType] = None

        # Reference to the DiagnosticEvent that is assigned to SWC service ports.
        self.diagnosticEventRef: Optional[RefType] = None

        # Reference to a SwcServiceDependencyType that links ServiceNeeds to SWC service ports.
        self.swcFlatServiceDependencyRef: Optional[RefType] = None

        # Instance reference to a SwcServiceDependency that links ServiceNeeds to SWC service ports. InstanceRef implemented by: SwcServiceDependencyInSystemInstanceRef
        self.swcServiceDependencyInSystemIRef: Optional[RefType] = None

    def getBswServiceDependencyRef(self) -> Optional[RefType]:
        """
        Reference to a BswServiceDependency that links ServiceNeeds to BswModuleEntries.
        """
        return self.bswServiceDependencyRef

    def setBswServiceDependencyRef(self, value: Optional[RefType]) -> DiagnosticEventPortMapping:
        """
        Reference to a BswServiceDependency that links ServiceNeeds to BswModuleEntries.
        A None value is a no-op and does not overwrite an existing bswServiceDependencyRef.
        """
        if value is not None:
            self.bswServiceDependencyRef = value
        return self

    def getDiagnosticEventRef(self) -> Optional[RefType]:
        """
        Reference to the DiagnosticEvent that is assigned to SWC service ports.
        """
        return self.diagnosticEventRef

    def setDiagnosticEventRef(self, value: Optional[RefType]) -> DiagnosticEventPortMapping:
        """
        Reference to the DiagnosticEvent that is assigned to SWC service ports.
        A None value is a no-op and does not overwrite an existing diagnosticEventRef.
        """
        if value is not None:
            self.diagnosticEventRef = value
        return self

    def getSwcFlatServiceDependencyRef(self) -> Optional[RefType]:
        """
        Reference to a SwcServiceDependencyType that links ServiceNeeds to SWC service ports.
        """
        return self.swcFlatServiceDependencyRef

    def setSwcFlatServiceDependencyRef(self, value: Optional[RefType]) -> DiagnosticEventPortMapping:
        """
        Reference to a SwcServiceDependencyType that links ServiceNeeds to SWC service ports.
        A None value is a no-op and does not overwrite an existing swcFlatServiceDependencyRef.
        """
        if value is not None:
            self.swcFlatServiceDependencyRef = value
        return self

    def getSwcServiceDependencyInSystemIRef(self) -> Optional[RefType]:
        """
        Instance reference to a SwcServiceDependency that links ServiceNeeds to SWC service ports. InstanceRef implemented by: SwcServiceDependencyInSystemInstanceRef
        """
        return self.swcServiceDependencyInSystemIRef

    def setSwcServiceDependencyInSystemIRef(self, value: Optional[RefType]) -> DiagnosticEventPortMapping:
        """
        Instance reference to a SwcServiceDependency that links ServiceNeeds to SWC service ports. InstanceRef implemented by: SwcServiceDependencyInSystemInstanceRef
        A None value is a no-op and does not overwrite an existing swcServiceDependencyInSystemIRef.
        """
        if value is not None:
            self.swcServiceDependencyInSystemIRef = value
        return self


class DiagnosticEventToDebounceAlgorithmMapping(DiagnosticMapping):
    """Defines which Debounce Algorithm is applicable for a DiagnosticEvent. Tags: atp.recommendedPackage=DiagnosticMappings"""

    # DiagnosticEventToDebounceAlgorithmMapping method parity checklist:
    # Spec: AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf, Table 5.21, p.246
    # Columns: impl / docstring / test / reader / writer / release   ([—] = no XML element)
    # [x] __init__                [x] impl  [x] docstring  [x] test  [—] reader  [—] writer  R23-11
    # [x] getDebounceAlgorithmRef    [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setDebounceAlgorithmRef    [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getDiagnosticEventRef      [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setDiagnosticEventRef      [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11

    def __init__(self, parent: ARObject, short_name: str):
        super().__init__(parent, short_name)

        # Reference to a DebounceAlgorithm assigned to a DiagnosticEvent.
        self.debounceAlgorithmRef: Optional[RefType] = None

        # Reference to a DiagnosticEvent to which a DebounceAlgorithm is assigned.
        self.diagnosticEventRef: Optional[RefType] = None

    def getDebounceAlgorithmRef(self) -> Optional[RefType]:
        """
        Reference to a DebounceAlgorithm assigned to a DiagnosticEvent.
        """
        return self.debounceAlgorithmRef

    def setDebounceAlgorithmRef(self, value: Optional[RefType]) -> DiagnosticEventToDebounceAlgorithmMapping:
        """
        Reference to a DebounceAlgorithm assigned to a DiagnosticEvent.
        A None value is a no-op and does not overwrite an existing debounceAlgorithmRef.
        """
        if value is not None:
            self.debounceAlgorithmRef = value
        return self

    def getDiagnosticEventRef(self) -> Optional[RefType]:
        """
        Reference to a DiagnosticEvent to which a DebounceAlgorithm is assigned.
        """
        return self.diagnosticEventRef

    def setDiagnosticEventRef(self, value: Optional[RefType]) -> DiagnosticEventToDebounceAlgorithmMapping:
        """
        Reference to a DiagnosticEvent to which a DebounceAlgorithm is assigned.
        A None value is a no-op and does not overwrite an existing diagnosticEventRef.
        """
        if value is not None:
            self.diagnosticEventRef = value
        return self


class DiagnosticEventToEnableConditionGroupMapping(DiagnosticMapping):
    """Defines which EnableConditionGroup is applicable for a DiagnosticEvent. Tags: atp.recommendedPackage=DiagnosticMappings"""

    # DiagnosticEventToEnableConditionGroupMapping method parity checklist:
    # Spec: AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf, Table 5.22, p.247
    # Columns: impl / docstring / test / reader / writer / release   ([—] = no XML element)
    # [x] __init__                [x] impl  [x] docstring  [x] test  [—] reader  [—] writer  R23-11
    # [x] getDiagnosticEventRef      [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setDiagnosticEventRef      [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getEnableConditionGroupRef [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setEnableConditionGroupRef [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11

    def __init__(self, parent: ARObject, short_name: str):
        super().__init__(parent, short_name)

        # Reference to a DiagnosticEvent to which an EnableConditionGroup is assigned.
        self.diagnosticEventRef: Optional[RefType] = None

        # Reference to an EnableConditionGroup assigned to a DiagnosticEvent.
        self.enableConditionGroupRef: Optional[RefType] = None

    def getDiagnosticEventRef(self) -> Optional[RefType]:
        """
        Reference to a DiagnosticEvent to which an EnableConditionGroup is assigned.
        """
        return self.diagnosticEventRef

    def setDiagnosticEventRef(self, value: Optional[RefType]) -> DiagnosticEventToEnableConditionGroupMapping:
        """
        Reference to a DiagnosticEvent to which an EnableConditionGroup is assigned.
        A None value is a no-op and does not overwrite an existing diagnosticEventRef.
        """
        if value is not None:
            self.diagnosticEventRef = value
        return self

    def getEnableConditionGroupRef(self) -> Optional[RefType]:
        """
        Reference to an EnableConditionGroup assigned to a DiagnosticEvent.
        """
        return self.enableConditionGroupRef

    def setEnableConditionGroupRef(self, value: Optional[RefType]) -> DiagnosticEventToEnableConditionGroupMapping:
        """
        Reference to an EnableConditionGroup assigned to a DiagnosticEvent.
        A None value is a no-op and does not overwrite an existing enableConditionGroupRef.
        """
        if value is not None:
            self.enableConditionGroupRef = value
        return self


class DiagnosticEventToOperationCycleMapping(DiagnosticMapping):
    """Defines which OperationCycle is applicable for a DiagnosticEvent. Tags: atp.recommendedPackage=DiagnosticMappings"""

    # DiagnosticEventToOperationCycleMapping method parity checklist:
    # Spec: AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf, Table 5.20, p.245
    # Columns: impl / docstring / test / reader / writer / release   ([—] = no XML element)
    # [x] __init__                [x] impl  [x] docstring  [x] test  [—] reader  [—] writer  R23-11
    # [x] getDiagnosticEventRef      [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setDiagnosticEventRef      [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getOperationCycleRef       [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setOperationCycleRef       [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11

    def __init__(self, parent: ARObject, short_name: str):
        super().__init__(parent, short_name)

        # Reference to a DiagnosticEvent to which an OperationCycle is assigned.
        self.diagnosticEventRef: Optional[RefType] = None

        # Reference to an OperationCycle assigned to a DiagnosticEvent.
        self.operationCycleRef: Optional[RefType] = None

    def getDiagnosticEventRef(self) -> Optional[RefType]:
        """
        Reference to a DiagnosticEvent to which an OperationCycle is assigned.
        """
        return self.diagnosticEventRef

    def setDiagnosticEventRef(self, value: Optional[RefType]) -> DiagnosticEventToOperationCycleMapping:
        """
        Reference to a DiagnosticEvent to which an OperationCycle is assigned.
        A None value is a no-op and does not overwrite an existing diagnosticEventRef.
        """
        if value is not None:
            self.diagnosticEventRef = value
        return self

    def getOperationCycleRef(self) -> Optional[RefType]:
        """
        Reference to an OperationCycle assigned to a DiagnosticEvent.
        """
        return self.operationCycleRef

    def setOperationCycleRef(self, value: Optional[RefType]) -> DiagnosticEventToOperationCycleMapping:
        """
        Reference to an OperationCycle assigned to a DiagnosticEvent.
        A None value is a no-op and does not overwrite an existing operationCycleRef.
        """
        if value is not None:
            self.operationCycleRef = value
        return self


class DiagnosticEventToSecurityEventMapping(DiagnosticMapping):
    """This meta-class represents the ability to map a security event that is defined in the context of the Security Extract to a diagnostic event defined on the context of the DiagnosticExtract. Tags: atp.Status=candidate atp.recommendedPackage=DiagnosticMappings"""

    # DiagnosticEventToSecurityEventMapping method parity checklist:
    # Spec: AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf, Table 5.30, p.257
    # Columns: impl / docstring / test / reader / writer / release   ([—] = no XML element)
    # [x] __init__                           [x] impl  [x] docstring  [x] test  [—] reader  [—] writer  R23-11
    # [x] getDiagnosticEventRef                 [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setDiagnosticEventRef                 [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getSecurityEventPropsRef              [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setSecurityEventPropsRef              [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11

    def __init__(self, parent: ARObject, short_name: str):
        super().__init__(parent, short_name)

        # This reference identifies the applicable diagnostic event. Tags: atp.Status=candidate
        self.diagnosticEventRef: Optional[RefType] = None

        # This reference identifies the qualification of the applicable security event Tags: atp.Status=candidate
        self.securityEventPropsRef: Optional[RefType] = None

    def getDiagnosticEventRef(self) -> Optional[RefType]:
        """
        This reference identifies the applicable diagnostic event. Tags: atp.Status=candidate
        """
        return self.diagnosticEventRef

    def setDiagnosticEventRef(self, value: Optional[RefType]) -> DiagnosticEventToSecurityEventMapping:
        """
        This reference identifies the applicable diagnostic event. Tags: atp.Status=candidate
        A None value is a no-op and does not overwrite an existing diagnosticEventRef.
        """
        if value is not None:
            self.diagnosticEventRef = value
        return self

    def getSecurityEventPropsRef(self) -> Optional[RefType]:
        """
        This reference identifies the qualification of the applicable security event Tags: atp.Status=candidate
        """
        return self.securityEventPropsRef

    def setSecurityEventPropsRef(self, value: Optional[RefType]) -> DiagnosticEventToSecurityEventMapping:
        """
        This reference identifies the qualification of the applicable security event Tags: atp.Status=candidate
        A None value is a no-op and does not overwrite an existing securityEventPropsRef.
        """
        if value is not None:
            self.securityEventPropsRef = value
        return self


class DiagnosticEventToStorageConditionGroupMapping(DiagnosticMapping):
    """Defines which StorageConditionGroup is applicable for a DiagnosticEvent. Tags: atp.recommendedPackage=DiagnosticMappings"""

    # DiagnosticEventToStorageConditionGroupMapping method parity checklist:
    # Spec: AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf, Table 5.23, p.248
    # Columns: impl / docstring / test / reader / writer / release   ([—] = no XML element)
    # [x] __init__                [x] impl  [x] docstring  [x] test  [—] reader  [—] writer  R23-11
    # [x] getDiagnosticEventRef      [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setDiagnosticEventRef      [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getStorageConditionGroupRef [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setStorageConditionGroupRef [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11

    def __init__(self, parent: ARObject, short_name: str):
        super().__init__(parent, short_name)

        # Reference to a DiagnosticEvent to which a StorageConditionGroup is assigned.
        self.diagnosticEventRef: Optional[RefType] = None

        # Reference to a StorageConditionGroup assigned to a DiagnosticEvent.
        self.storageConditionGroupRef: Optional[RefType] = None

    def getDiagnosticEventRef(self) -> Optional[RefType]:
        """
        Reference to a DiagnosticEvent to which a StorageConditionGroup is assigned.
        """
        return self.diagnosticEventRef

    def setDiagnosticEventRef(self, value: Optional[RefType]) -> DiagnosticEventToStorageConditionGroupMapping:
        """
        Reference to a DiagnosticEvent to which a StorageConditionGroup is assigned.
        A None value is a no-op and does not overwrite an existing diagnosticEventRef.
        """
        if value is not None:
            self.diagnosticEventRef = value
        return self

    def getStorageConditionGroupRef(self) -> Optional[RefType]:
        """
        Reference to a StorageConditionGroup assigned to a DiagnosticEvent.
        """
        return self.storageConditionGroupRef

    def setStorageConditionGroupRef(self, value: Optional[RefType]) -> DiagnosticEventToStorageConditionGroupMapping:
        """
        Reference to a StorageConditionGroup assigned to a DiagnosticEvent.
        A None value is a no-op and does not overwrite an existing storageConditionGroupRef.
        """
        if value is not None:
            self.storageConditionGroupRef = value
        return self


class DiagnosticEventToTroubleCodeJ1939Mapping(DiagnosticMapping):
    """By means of this meta-class it is possible to associate a DiagnosticEvent to a DiagnosticTroubleCodeJ1939. Tags: atp.recommendedPackage=DiagnosticMappings"""

    # DiagnosticEventToTroubleCodeJ1939Mapping method parity checklist:
    # Spec: AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf, Table 5.43, p.269
    # Columns: impl / docstring / test / reader / writer / release   ([—] = no XML element)
    # [x] __init__                           [x] impl  [x] docstring  [x] test  [—] reader  [—] writer  R23-11
    # [x] getDiagnosticEventRef                 [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setDiagnosticEventRef                 [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getTroubleCodeJ1939Ref                [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setTroubleCodeJ1939Ref                [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11

    def __init__(self, parent: ARObject, short_name: str):
        super().__init__(parent, short_name)

        # Reference to a DiagnosticEvent to which a J1939 Diagnostic Trouble Code is assigned.
        self.diagnosticEventRef: Optional[RefType] = None

        # Reference to a J1939 Diagnostic Trouble Code to which a DiagnosticEvent is assigned.
        self.troubleCodeJ1939Ref: Optional[RefType] = None

    def getDiagnosticEventRef(self) -> Optional[RefType]:
        """
        Reference to a DiagnosticEvent to which a J1939 Diagnostic Trouble Code is assigned.
        """
        return self.diagnosticEventRef

    def setDiagnosticEventRef(self, value: Optional[RefType]) -> DiagnosticEventToTroubleCodeJ1939Mapping:
        """
        Reference to a DiagnosticEvent to which a J1939 Diagnostic Trouble Code is assigned.
        A None value is a no-op and does not overwrite an existing diagnosticEventRef.
        """
        if value is not None:
            self.diagnosticEventRef = value
        return self

    def getTroubleCodeJ1939Ref(self) -> Optional[RefType]:
        """
        Reference to a J1939 Diagnostic Trouble Code to which a DiagnosticEvent is assigned.
        """
        return self.troubleCodeJ1939Ref

    def setTroubleCodeJ1939Ref(self, value: Optional[RefType]) -> DiagnosticEventToTroubleCodeJ1939Mapping:
        """
        Reference to a J1939 Diagnostic Trouble Code to which a DiagnosticEvent is assigned.
        A None value is a no-op and does not overwrite an existing troubleCodeJ1939Ref.
        """
        if value is not None:
            self.troubleCodeJ1939Ref = value
        return self


class DiagnosticEventToTroubleCodeUdsMapping(DiagnosticMapping):
    """Defines which UDS Diagnostic Trouble Code is applicable for a DiagnosticEvent. Tags: atp.recommendedPackage=DiagnosticMappings"""

    # DiagnosticEventToTroubleCodeUdsMapping method parity checklist:
    # Spec: AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf, Table 5.19, p.245
    # Columns: impl / docstring / test / reader / writer / release   ([—] = no XML element)
    # [x] __init__                [x] impl  [x] docstring  [x] test  [—] reader  [—] writer  R23-11
    # [x] getDiagnosticEventRef      [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setDiagnosticEventRef      [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getTroubleCodeUdsRef       [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setTroubleCodeUdsRef       [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11

    def __init__(self, parent: ARObject, short_name: str):
        super().__init__(parent, short_name)

        # Reference to a DiagnosticEvent to which a UDS Diagnostic Trouble Code is assigned.
        self.diagnosticEventRef: Optional[RefType] = None

        # Reference to an UDS Diagnostic Trouble Code assigned to a DiagnosticEvent.
        self.troubleCodeUdsRef: Optional[RefType] = None

    def getDiagnosticEventRef(self) -> Optional[RefType]:
        """
        Reference to a DiagnosticEvent to which a UDS Diagnostic Trouble Code is assigned.
        """
        return self.diagnosticEventRef

    def setDiagnosticEventRef(self, value: Optional[RefType]) -> DiagnosticEventToTroubleCodeUdsMapping:
        """
        Reference to a DiagnosticEvent to which a UDS Diagnostic Trouble Code is assigned.
        A None value is a no-op and does not overwrite an existing diagnosticEventRef.
        """
        if value is not None:
            self.diagnosticEventRef = value
        return self

    def getTroubleCodeUdsRef(self) -> Optional[RefType]:
        """
        Reference to an UDS Diagnostic Trouble Code assigned to a DiagnosticEvent.
        """
        return self.troubleCodeUdsRef

    def setTroubleCodeUdsRef(self, value: Optional[RefType]) -> DiagnosticEventToTroubleCodeUdsMapping:
        """
        Reference to an UDS Diagnostic Trouble Code assigned to a DiagnosticEvent.
        A None value is a no-op and does not overwrite an existing troubleCodeUdsRef.
        """
        if value is not None:
            self.troubleCodeUdsRef = value
        return self


class DiagnosticExtendedDataRecord(ARElement):
    """
    Description of an extended data record. Tags: atp.recommendedPackage=DiagnosticExtendedDataRecords
    """

    # DiagnosticExtendedDataRecord method parity checklist:
    # Spec: AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf, Table 4.181, p.190
    # Columns: impl / docstring / test / reader / writer / release   ([—] = no XML element)
    # [x] __init__            [x] impl  [x] docstring  [x] test  [—] reader  [—] writer  R23-11
    # [x] getCustomTrigger    [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setCustomTrigger    [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] addRecordElement    [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getRecordElements   [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] getRecordNumber     [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setRecordNumber     [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getTrigger          [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setTrigger          [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getUpdate           [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setUpdate           [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11

    def __init__(self, parent: ARObject, short_name: str):
        super().__init__(parent, short_name)

        # This attribute shall be taken to verbally describe the nature of the custom trigger.
        self.customTrigger: Optional[String] = None

        # Defined DataElements in the extended record element. Stereotypes: atpSplitable Tags: atp.Splitkey=recordElement.bitOffset, recordElement.ident.shortName
        self.recordElements: List[DiagnosticParameter] = []

        # This attribute specifies an unique identifier for an extended data record.
        self.recordNumber: Optional[PositiveInteger] = None

        # This attribute specifies the primary trigger to allocate an event memory entry.
        self.trigger: Optional[DiagnosticRecordTriggerEnum] = None

        # This attribute defines when an extended data record is captured. true: This extended data record is captured every time. false: This extended data record is only captured for new event memory entries.
        self.update: Optional[Boolean] = None

    def getCustomTrigger(self) -> Optional[String]:
        """
        This attribute shall be taken to verbally describe the nature of the custom trigger.
        """
        return self.customTrigger

    def setCustomTrigger(self, value: Optional[String]) -> DiagnosticExtendedDataRecord:
        """
        This attribute shall be taken to verbally describe the nature of the custom trigger.

        A None value is a no-op and does not overwrite an existing customTrigger.
        """
        if value is not None:
            self.customTrigger = value
        return self

    def addRecordElement(self, record_element: Optional[DiagnosticParameter]) -> DiagnosticExtendedDataRecord:
        """
        Defined DataElements in the extended record element. Stereotypes: atpSplitable Tags: atp.Splitkey=recordElement.bitOffset, recordElement.ident.shortName

        A None value is a no-op and does not extend the recordElements list.
        """
        if record_element is not None:
            self.recordElements.append(record_element)
        return self

    def getRecordElements(self) -> List[DiagnosticParameter]:
        """
        Defined DataElements in the extended record element. Stereotypes: atpSplitable Tags: atp.Splitkey=recordElement.bitOffset, recordElement.ident.shortName
        """
        return self.recordElements

    def getRecordNumber(self) -> Optional[PositiveInteger]:
        """
        This attribute specifies an unique identifier for an extended data record.
        """
        return self.recordNumber

    def setRecordNumber(self, value: Optional[PositiveInteger]) -> DiagnosticExtendedDataRecord:
        """
        This attribute specifies an unique identifier for an extended data record.

        A None value is a no-op and does not overwrite an existing recordNumber.
        """
        if value is not None:
            self.recordNumber = value
        return self

    def getTrigger(self) -> Optional[DiagnosticRecordTriggerEnum]:
        """
        This attribute specifies the primary trigger to allocate an event memory entry.
        """
        return self.trigger

    def setTrigger(self, value: Optional[DiagnosticRecordTriggerEnum]) -> DiagnosticExtendedDataRecord:
        """
        This attribute specifies the primary trigger to allocate an event memory entry.

        A None value is a no-op and does not overwrite an existing trigger.
        """
        if value is not None:
            self.trigger = value
        return self

    def getUpdate(self) -> Optional[Boolean]:
        """
        This attribute defines when an extended data record is captured. true: This extended data record is captured every time. false: This extended data record is only captured for new event memory entries.
        """
        return self.update

    def setUpdate(self, value: Optional[Boolean]) -> DiagnosticExtendedDataRecord:
        """
        This attribute defines when an extended data record is captured. true: This extended data record is captured every time. false: This extended data record is only captured for new event memory entries.

        A None value is a no-op and does not overwrite an existing update.
        """
        if value is not None:
            self.update = value
        return self


class DiagnosticFimAliasEvent(DiagnosticAbstractAliasEvent):
    """This meta-class is used to represent a given event semantics. However, the name of the actual events used in a specific project is sometimes not defined yet, not known or not in the responsibility of the author. Therefore, the DiagnosticFimAliasEvent has a reference to the actual DiagnosticEvent and by this the final connection is created. Tags: atp.recommendedPackage=DiagnosticFimAliasEvents"""

    # DiagnosticFimAliasEvent method parity checklist:
    # Spec: AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf, Table 4.212, p.214
    # Columns: impl / docstring / test / reader / writer / release   ([—] = no XML element)
    # [x] __init__  [x] impl  [x] docstring  [x] test  [—] reader  [—] writer  R23-11

    def __init__(self, parent: ARObject, short_name: str):
        super().__init__(parent, short_name)


class DiagnosticFimAliasEventGroup(DiagnosticAbstractAliasEvent):
    """This meta-class represents the ability to define an alias for a Fim summarized event. This alias can be used in early phases of the configuration process until a further refinement is possible. Tags: atp.recommendedPackage=DiagnosticFimAliasEventGroups"""

    # DiagnosticFimAliasEventGroup method parity checklist:
    # Spec: AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf, Table 5.35, p.263
    # Columns: impl / docstring / test / reader / writer / release   ([—] = no XML element)
    # [x] __init__                           [x] impl  [x] docstring  [x] test  [—] reader  [—] writer  R23-11
    # [x] addGroupedAliasEventRef               [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getGroupedAliasEventRefs              [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11

    def __init__(self, parent: ARObject, short_name: str):
        super().__init__(parent, short_name)

        # By means of this reference the grouping of DiagnosticAliasEvents within the DiagnosticFimSummaryEvent can be specified.
        self.groupedAliasEventRefs: List[RefType] = []

    def addGroupedAliasEventRef(self, value: Optional[RefType]) -> DiagnosticFimAliasEventGroup:
        """
        By means of this reference the grouping of DiagnosticAliasEvents within the DiagnosticFimSummaryEvent can be specified.
        A None value is a no-op and does not append a groupedAliasEventRef.
        """
        if value is not None:
            self.groupedAliasEventRefs.append(value)
        return self

    def getGroupedAliasEventRefs(self) -> List[RefType]:
        """
        By means of this reference the grouping of DiagnosticAliasEvents within the DiagnosticFimSummaryEvent can be specified.
        """
        return self.groupedAliasEventRefs


class DiagnosticInhibitSourceEventMapping(DiagnosticMapping):
    """This meta-class represents the ability to map a DiagnosticFunctionInhibitSource directly to alternatively one DiagnosticEvent or one DiagnosticFimSummaryEvent. This model element shall be used if the approach via the alias events is not applicable, i.e. when diagnostic events defined by the Dem are already available at the time the Fim configuration within the diagnostic extract is created. Tags: atp.recommendedPackage=DiagnosticInhibitSourceEventMappings"""

    # DiagnosticInhibitSourceEventMapping method parity checklist:
    # Spec: AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf, Table 5.33, p.261
    # Columns: impl / docstring / test / reader / writer / release   ([—] = no XML element)
    # [x] __init__                           [x] impl  [x] docstring  [x] test  [—] reader  [—] writer  R23-11
    # [x] getDiagnosticEventRef                 [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setDiagnosticEventRef                 [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getEventGroupRef                      [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setEventGroupRef                      [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getInhibitionSourceRef                [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setInhibitionSourceRef                [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11

    def __init__(self, parent: ARObject, short_name: str):
        super().__init__(parent, short_name)

        # This represents the reference to the diagnostic event.
        self.diagnosticEventRef: Optional[RefType] = None

        # This represents the reference to the event group
        self.eventGroupRef: Optional[RefType] = None

        # This represents the reference to the inhibition source.
        self.inhibitionSourceRef: Optional[RefType] = None

    def getDiagnosticEventRef(self) -> Optional[RefType]:
        """
        This represents the reference to the diagnostic event.
        """
        return self.diagnosticEventRef

    def setDiagnosticEventRef(self, value: Optional[RefType]) -> DiagnosticInhibitSourceEventMapping:
        """
        This represents the reference to the diagnostic event.
        A None value is a no-op and does not overwrite an existing diagnosticEventRef.
        """
        if value is not None:
            self.diagnosticEventRef = value
        return self

    def getEventGroupRef(self) -> Optional[RefType]:
        """
        This represents the reference to the event group
        """
        return self.eventGroupRef

    def setEventGroupRef(self, value: Optional[RefType]) -> DiagnosticInhibitSourceEventMapping:
        """
        This represents the reference to the event group
        A None value is a no-op and does not overwrite an existing eventGroupRef.
        """
        if value is not None:
            self.eventGroupRef = value
        return self

    def getInhibitionSourceRef(self) -> Optional[RefType]:
        """
        This represents the reference to the inhibition source.
        """
        return self.inhibitionSourceRef

    def setInhibitionSourceRef(self, value: Optional[RefType]) -> DiagnosticInhibitSourceEventMapping:
        """
        This represents the reference to the inhibition source.
        A None value is a no-op and does not overwrite an existing inhibitionSourceRef.
        """
        if value is not None:
            self.inhibitionSourceRef = value
        return self


class DiagnosticFimAliasEventGroupMapping(DiagnosticMapping):
    """This meta-class represents the ability to map a DiagnosticFimEventGroup to a DiagnosticFimAliasEventGroup. By this means the "preliminary" modeling by way of a DiagnosticFimAliasEventGroup is further substantiated. Tags: atp.recommendedPackage=DiagnosticFimAliasEventGroupMappings"""

    # DiagnosticFimAliasEventGroupMapping method parity checklist:
    # Spec: AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf, Table 5.36, p.263
    # Columns: impl / docstring / test / reader / writer / release   ([—] = no XML element)
    # [x] __init__                           [x] impl  [x] docstring  [x] test  [—] reader  [—] writer  R23-11
    # [x] getActualEventRef                     [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setActualEventRef                     [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getAliasEventRef                      [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setAliasEventRef                      [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11

    def __init__(self, parent: ARObject, short_name: str):
        super().__init__(parent, short_name)

        # This represents the reference to the actual summary event.
        self.actualEventRef: Optional[RefType] = None

        # This represents the reference to the alias summary event.
        self.aliasEventRef: Optional[RefType] = None

    def getActualEventRef(self) -> Optional[RefType]:
        """
        This represents the reference to the actual summary event.
        """
        return self.actualEventRef

    def setActualEventRef(self, value: Optional[RefType]) -> DiagnosticFimAliasEventGroupMapping:
        """
        This represents the reference to the actual summary event.
        A None value is a no-op and does not overwrite an existing actualEventRef.
        """
        if value is not None:
            self.actualEventRef = value
        return self

    def getAliasEventRef(self) -> Optional[RefType]:
        """
        This represents the reference to the alias summary event.
        """
        return self.aliasEventRef

    def setAliasEventRef(self, value: Optional[RefType]) -> DiagnosticFimAliasEventGroupMapping:
        """
        This represents the reference to the alias summary event.
        A None value is a no-op and does not overwrite an existing aliasEventRef.
        """
        if value is not None:
            self.aliasEventRef = value
        return self


class DiagnosticFimAliasEventMapping(DiagnosticMapping):
    """This meta-class represents the ability to model the mapping of a DiagnosticEvent to a DiagnosticAliasEvent. By this means the "preliminary" modeling by way of a DiagnosticAliasEvent is further substantiated. Tags: atp.recommendedPackage=DiagnosticFimEventMappings"""

    # DiagnosticFimAliasEventMapping method parity checklist:
    # Spec: AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf, Table 5.34, p.262
    # Columns: impl / docstring / test / reader / writer / release   ([—] = no XML element)
    # [x] __init__                           [x] impl  [x] docstring  [x] test  [—] reader  [—] writer  R23-11
    # [x] getActualEventRef                     [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setActualEventRef                     [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getAliasEventRef                      [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setAliasEventRef                      [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11

    def __init__(self, parent: ARObject, short_name: str):
        super().__init__(parent, short_name)

        # This represents the reference to the actual diagnostic event.
        self.actualEventRef: Optional[RefType] = None

        # This represents the reference to the alias event.
        self.aliasEventRef: Optional[RefType] = None

    def getActualEventRef(self) -> Optional[RefType]:
        """
        This represents the reference to the actual diagnostic event.
        """
        return self.actualEventRef

    def setActualEventRef(self, value: Optional[RefType]) -> DiagnosticFimAliasEventMapping:
        """
        This represents the reference to the actual diagnostic event.
        A None value is a no-op and does not overwrite an existing actualEventRef.
        """
        if value is not None:
            self.actualEventRef = value
        return self

    def getAliasEventRef(self) -> Optional[RefType]:
        """
        This represents the reference to the alias event.
        """
        return self.aliasEventRef

    def setAliasEventRef(self, value: Optional[RefType]) -> DiagnosticFimAliasEventMapping:
        """
        This represents the reference to the alias event.
        A None value is a no-op and does not overwrite an existing aliasEventRef.
        """
        if value is not None:
            self.aliasEventRef = value
        return self


class DiagnosticFimEventGroup(DiagnosticCommonElement):
    """This meta-class represents the ability to model a Fim event group, also known as a summary event in Fim terminology. This represents a group of single diagnostic events. Tags: atp.recommendedPackage=DiagnosticFimEventGroups"""

    # DiagnosticFimEventGroup method parity checklist:
    # Spec: AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf, Table 4.218, p.217
    # Columns: impl / docstring / test / reader / writer / release   ([—] = no XML element)
    # [x] __init__       [x] impl  [x] docstring  [x] test  [—] reader  [—] writer  R23-11
    # [x] addEventRef    [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getEventRefs   [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11

    def __init__(self, parent: ARObject, short_name: str):
        super().__init__(parent, short_name)

        # This reference represents the way of grouping diagnostic events into a summary event in the context of the Fim.
        self.eventRefs: List[RefType] = []

    def addEventRef(self, value: Optional[RefType]) -> DiagnosticFimEventGroup:
        """
        This reference represents the way of grouping diagnostic events into a summary event in the context of the Fim.
        A None value is a no-op and does not append an eventRef.
        """
        if value is not None:
            self.eventRefs.append(value)
        return self

    def getEventRefs(self) -> List[RefType]:
        """
        This reference represents the way of grouping diagnostic events into a summary event in the context of the Fim.
        """
        return self.eventRefs


class DiagnosticFreezeFrame(ARElement):
    """
    This element describes combinations of DIDs for a non OBD relevant freeze frame. Tags: atp.recommendedPackage=DiagnosticFreezeFrames
    """

    # DiagnosticFreezeFrame method parity checklist:
    # Spec: AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf, Table 4.183, p.192
    # Columns: impl / docstring / test / reader / writer / release   ([—] = no XML element)
    # [x] __init__            [x] impl  [x] docstring  [x] test  [—] reader  [—] writer  R23-11
    # [x] getCustomTrigger    [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setCustomTrigger    [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getRecordNumber     [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setRecordNumber     [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getTrigger          [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setTrigger          [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getUpdate           [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setUpdate           [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11

    def __init__(self, parent: ARObject, short_name: str):
        super().__init__(parent, short_name)

        # This attribute shall be taken to verbally describe the nature of the custom trigger.
        self.customTrigger: Optional[String] = None

        # This attribute defines a record number for a freeze frame record. Stereotypes: atpVariation Tags: vh.latestBindingTime=preCompileTime
        self.recordNumber: Optional[PositiveInteger] = None

        # This attribute defines the primary trigger to allocate an event memory entry.
        self.trigger: Optional[DiagnosticRecordTriggerEnum] = None

        # This attribute defines the approach when the freeze frame record is stored/updated. true: FreezeFrame record is captured every time. false: FreezeFrame record is only captured for new event memory entries.
        self.update: Optional[Boolean] = None

    def getCustomTrigger(self) -> Optional[String]:
        """
        This attribute shall be taken to verbally describe the nature of the custom trigger.
        """
        return self.customTrigger

    def setCustomTrigger(self, value: Optional[String]) -> DiagnosticFreezeFrame:
        """
        This attribute shall be taken to verbally describe the nature of the custom trigger.

        A None value is a no-op and does not overwrite an existing customTrigger.
        """
        if value is not None:
            self.customTrigger = value
        return self

    def getRecordNumber(self) -> Optional[PositiveInteger]:
        """
        This attribute defines a record number for a freeze frame record. Stereotypes: atpVariation Tags: vh.latestBindingTime=preCompileTime
        """
        return self.recordNumber

    def setRecordNumber(self, value: Optional[PositiveInteger]) -> DiagnosticFreezeFrame:
        """
        This attribute defines a record number for a freeze frame record. Stereotypes: atpVariation Tags: vh.latestBindingTime=preCompileTime

        A None value is a no-op and does not overwrite an existing recordNumber.
        """
        if value is not None:
            self.recordNumber = value
        return self

    def getTrigger(self) -> Optional[DiagnosticRecordTriggerEnum]:
        """
        This attribute defines the primary trigger to allocate an event memory entry.
        """
        return self.trigger

    def setTrigger(self, value: Optional[DiagnosticRecordTriggerEnum]) -> DiagnosticFreezeFrame:
        """
        This attribute defines the primary trigger to allocate an event memory entry.

        A None value is a no-op and does not overwrite an existing trigger.
        """
        if value is not None:
            self.trigger = value
        return self

    def getUpdate(self) -> Optional[Boolean]:
        """
        This attribute defines the approach when the freeze frame record is stored/updated. true: FreezeFrame record is captured every time. false: FreezeFrame record is only captured for new event memory entries.
        """
        return self.update

    def setUpdate(self, value: Optional[Boolean]) -> DiagnosticFreezeFrame:
        """
        This attribute defines the approach when the freeze frame record is stored/updated. true: FreezeFrame record is captured every time. false: FreezeFrame record is only captured for new event memory entries.

        A None value is a no-op and does not overwrite an existing update.
        """
        if value is not None:
            self.update = value
        return self


class DiagnosticFunctionIdentifier(ARElement):
    """This meta-class represents a diagnostic function identifier (a.k.a. FID). Tags: atp.recommendedPackage=DiagnosticFunctionIdentifiers"""

    # DiagnosticFunctionIdentifier method parity checklist:
    # Spec: AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf, Table 4.214, p.215
    # Columns: impl / docstring / test / reader / writer / release   ([—] = no XML element)
    # [x] __init__  [x] impl  [x] docstring  [x] test  [x] reader  [x] writer  R23-11

    def __init__(self, parent: ARObject, short_name: str):
        super().__init__(parent, short_name)


class DiagnosticIOControl(ARElement):
    """This represents an instance of the "I/O Control" diagnostic service."""

    # DiagnosticIOControl method parity checklist:
    # Spec: AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf, Table 4.80, p.118
    # Columns: impl / docstring / test / reader / writer / release   ([—] = no XML element)
    # [x] __init__                       [x] impl  [x] docstring  [x] test  [—] reader  [—] writer  R23-11
    # [x] addControlEnableMaskBit        [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getControlEnableMaskBits       [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] getDataIdentifier              [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setDataIdentifier              [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getFreezeCurrentState          [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setFreezeCurrentState          [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getIoControlClass              [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setIoControlClass              [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getResetToDefault              [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setResetToDefault              [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getShortTermAdjustment         [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setShortTermAdjustment         [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11

    def __init__(self, parent: ARObject, short_name: str):
        super().__init__(parent, short_name)

        # This aggregation represents the control mask record consisting of single bits.
        self.controlEnableMaskBit: List[DiagnosticControlEnableMaskBit] = []

        # This represents the corresponding DiagnosticData Identifier
        self.dataIdentifier: Optional[RefType] = None

        # Setting this attribute to true represents the ability of the Dcm to execute a freezeCurrentState.
        self.freezeCurrentState: Optional[Boolean] = None

        # This reference substantiates that abstract reference in the role serviceClass for this specific concrete class. Thereby, the reference represents the ability to access shared attributes among all DiagnosticIOControl in the given context.
        self.ioControlClass: Optional[RefType] = None

        # Setting this attribute to true represents the ability of the Dcm to execute a resetToDefault.
        self.resetToDefault: Optional[Boolean] = None

        # Setting this attribute to true represents the ability of the Dcm to execute a shortTermAdjustment.
        self.shortTermAdjustment: Optional[Boolean] = None

    def addControlEnableMaskBit(self, value: Optional[DiagnosticControlEnableMaskBit]) -> DiagnosticIOControl:
        """
        This aggregation represents the control mask record consisting of single bits.

        A None value is a no-op and does not append a controlEnableMaskBit.
        """
        if value is not None:
            self.controlEnableMaskBit.append(value)
        return self

    def getControlEnableMaskBits(self) -> List[DiagnosticControlEnableMaskBit]:
        """
        This aggregation represents the control mask record consisting of single bits.
        """
        return self.controlEnableMaskBit

    def getDataIdentifier(self) -> Optional[RefType]:
        """
        This represents the corresponding DiagnosticData Identifier
        """
        return self.dataIdentifier

    def setDataIdentifier(self, value: Optional[RefType]) -> DiagnosticIOControl:
        """
        This represents the corresponding DiagnosticData Identifier

        A None value is a no-op and does not overwrite an existing dataIdentifier.
        """
        if value is not None:
            self.dataIdentifier = value
        return self

    def getFreezeCurrentState(self) -> Optional[Boolean]:
        """
        Setting this attribute to true represents the ability of the Dcm to execute a freezeCurrentState.
        """
        return self.freezeCurrentState

    def setFreezeCurrentState(self, value: Optional[Boolean]) -> DiagnosticIOControl:
        """
        Setting this attribute to true represents the ability of the Dcm to execute a freezeCurrentState.

        A None value is a no-op and does not overwrite an existing freezeCurrentState.
        """
        if value is not None:
            self.freezeCurrentState = value
        return self

    def getIoControlClass(self) -> Optional[RefType]:
        """
        This reference substantiates that abstract reference in the role serviceClass for this specific concrete class. Thereby, the reference represents the ability to access shared attributes among all DiagnosticIOControl in the given context.
        """
        return self.ioControlClass

    def setIoControlClass(self, value: Optional[RefType]) -> DiagnosticIOControl:
        """
        This reference substantiates that abstract reference in the role serviceClass for this specific concrete class. Thereby, the reference represents the ability to access shared attributes among all DiagnosticIOControl in the given context.

        A None value is a no-op and does not overwrite an existing ioControlClass.
        """
        if value is not None:
            self.ioControlClass = value
        return self

    def getResetToDefault(self) -> Optional[Boolean]:
        """
        Setting this attribute to true represents the ability of the Dcm to execute a resetToDefault.
        """
        return self.resetToDefault

    def setResetToDefault(self, value: Optional[Boolean]) -> DiagnosticIOControl:
        """
        Setting this attribute to true represents the ability of the Dcm to execute a resetToDefault.

        A None value is a no-op and does not overwrite an existing resetToDefault.
        """
        if value is not None:
            self.resetToDefault = value
        return self

    def getShortTermAdjustment(self) -> Optional[Boolean]:
        """
        Setting this attribute to true represents the ability of the Dcm to execute a shortTermAdjustment.
        """
        return self.shortTermAdjustment

    def setShortTermAdjustment(self, value: Optional[Boolean]) -> DiagnosticIOControl:
        """
        Setting this attribute to true represents the ability of the Dcm to execute a shortTermAdjustment.

        A None value is a no-op and does not overwrite an existing shortTermAdjustment.
        """
        if value is not None:
            self.shortTermAdjustment = value
        return self


class DiagnosticIndicator(ARElement):
    """
    Definition of an indicator. Tags: atp.recommendedPackage=DiagnosticIndicators
    """

    # DiagnosticIndicator method parity checklist:
    # Spec: AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf, Table 4.199, p.203
    # Columns: impl / docstring / test / reader / writer / release   ([—] = no XML element)
    # [x] __init__    [x] impl  [x] docstring  [x] test  [—] reader  [—] writer  R23-11
    # [x] getType     [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setType     [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11

    def __init__(self, parent: ARObject, short_name: str):
        super().__init__(parent, short_name)

        # Defines the type of the indicator. Stereotypes: atpVariation Tags: vh.latestBindingTime=preCompileTime
        self.type: Optional[DiagnosticIndicatorTypeEnum] = None

    def getType(self) -> Optional[DiagnosticIndicatorTypeEnum]:
        """
        Defines the type of the indicator. Stereotypes: atpVariation Tags: vh.latestBindingTime=preCompileTime
        """
        return self.type

    def setType(self, value: Optional[DiagnosticIndicatorTypeEnum]) -> DiagnosticIndicator:
        """
        Defines the type of the indicator. Stereotypes: atpVariation Tags: vh.latestBindingTime=preCompileTime

        A None value is a no-op and does not overwrite an existing type.
        """
        if value is not None:
            self.type = value
        return self


class DiagnosticInfoType(ARElement):
    """This meta-class represents the ability to model an OBD info type. Tags: atp.recommendedPackage=DiagnosticInfoTypes"""

    # DiagnosticInfoType method parity checklist:
    # Spec: AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf, Table 4.146, p.160
    # Columns: impl / docstring / test / reader / writer / release   ([—] = no XML element)
    # [x] __init__                    [x] impl  [x] docstring  [x] test  [—] reader  [—] writer  R23-11
    # [x] getDataElements              [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] addDataElement               [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getId                        [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setId                        [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11

    def __init__(self, parent: ARObject, short_name: str):
        super().__init__(parent, short_name)

        # This represents the data associated with the enclosing DiagnosticInfoType. Stereotypes: atpSplitable Tags: atp.Splitkey=dataElement.bitOffset, dataElement.ident.shortName
        self.dataElements: List[DiagnosticParameter] = []

        # This attribute represents the value of InfoType (see SAE J1979-DA).
        self.id: Optional[PositiveInteger] = None

    def getDataElements(self) -> List[DiagnosticParameter]:
        """
        This represents the data associated with the enclosing DiagnosticInfoType. Stereotypes: atpSplitable Tags: atp.Splitkey=dataElement.bitOffset, dataElement.ident.shortName
        """
        return self.dataElements

    def addDataElement(self, value: Optional[DiagnosticParameter]) -> DiagnosticInfoType:
        """
        This represents the data associated with the enclosing DiagnosticInfoType. Stereotypes: atpSplitable Tags: atp.Splitkey=dataElement.bitOffset, dataElement.ident.shortName

        A None value is a no-op and does not append a dataElement.
        """
        if value is not None:
            self.dataElements.append(value)
        return self

    def getId(self) -> Optional[PositiveInteger]:
        """
        This attribute represents the value of InfoType (see SAE J1979-DA).
        """
        return self.id

    def setId(self, value: Optional[PositiveInteger]) -> DiagnosticInfoType:
        """
        This attribute represents the value of InfoType (see SAE J1979-DA).

        A None value is a no-op and does not overwrite an existing id.
        """
        if value is not None:
            self.id = value
        return self


class DiagnosticIumpr(ARElement):
    """
    This meta-class represents the ability to model the in-use monitor performance ratio. The latter computes to the number of times a fault could have been found divided by the number of times the vehicle conditions have been properly fulfilled. Tags: atp.recommendedPackage=DiagnosticIumprs
    """

    # DiagnosticIumpr method parity checklist:
    # Spec: AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf, Table 4.207, p.210
    # Columns: impl / docstring / test / reader / writer / release   ([—] = no XML element)
    # [x] __init__       [x] impl  [x] docstring  [x] test  [—] reader  [—] writer  R23-11
    # [x] getEventRef    [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setEventRef    [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getRatioKind   [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setRatioKind   [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11

    def __init__(self, parent: ARObject, short_name: str):
        super().__init__(parent, short_name)

        # This reference represents the DiagnosticEvent that corresponds to the IUMPR computation.
        self.eventRef: Optional[RefType] = None

        # This attribute controls the behavior of how the ratio is calculated.
        self.ratioKind: Optional[DiagnosticIumprKindEnum] = None

    def getEventRef(self) -> Optional[RefType]:
        """
        This reference represents the DiagnosticEvent that corresponds to the IUMPR computation.
        """
        return self.eventRef

    def setEventRef(self, value: Optional[RefType]) -> DiagnosticIumpr:
        """
        This reference represents the DiagnosticEvent that corresponds to the IUMPR computation.

        A None value is a no-op and does not overwrite an existing eventRef.
        """
        if value is not None:
            self.eventRef = value
        return self

    def getRatioKind(self) -> Optional[DiagnosticIumprKindEnum]:
        """
        This attribute controls the behavior of how the ratio is calculated.
        """
        return self.ratioKind

    def setRatioKind(self, value: Optional[DiagnosticIumprKindEnum]) -> DiagnosticIumpr:
        """
        This attribute controls the behavior of how the ratio is calculated.

        A None value is a no-op and does not overwrite an existing ratioKind.
        """
        if value is not None:
            self.ratioKind = value
        return self


class DiagnosticIumprDenominatorGroup(ARElement):
    """
    This meta-class represents the ability to model a IUMPR denominator groups. Tags: atp.recommendedPackage=DiagnosticIumprDenominatorGroup
    """

    # DiagnosticIumprDenominatorGroup method parity checklist:
    # Spec: AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf, Table 4.211, p.211
    # Columns: impl / docstring / test / reader / writer / release   ([—] = no XML element)
    # [x] __init__      [x] impl  [x] docstring  [x] test  [—] reader  [—] writer  R23-11
    # [x] addIumprRef   [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getIumprRefs  [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11

    def __init__(self, parent: ARObject, short_name: str):
        super().__init__(parent, short_name)

        # This reference collects DiagnosticIumpr to a Diagnostic IumprDenominatorGroup. Stereotypes: atpSplitable Tags: atp.Splitkey=iumpr
        self.iumprRefs: List[RefType] = []

    def addIumprRef(self, ref: Optional[RefType]) -> DiagnosticIumprDenominatorGroup:
        """
        This reference collects DiagnosticIumpr to a Diagnostic IumprDenominatorGroup. Stereotypes: atpSplitable Tags: atp.Splitkey=iumpr

        A None value is a no-op and does not extend the iumprRefs list.
        """
        if ref is not None:
            self.iumprRefs.append(ref)
        return self

    def getIumprRefs(self) -> List[RefType]:
        """
        This reference collects DiagnosticIumpr to a Diagnostic IumprDenominatorGroup. Stereotypes: atpSplitable Tags: atp.Splitkey=iumpr
        """
        return self.iumprRefs


class DiagnosticIumprGroup(ARElement):
    """
    This meta-class represents the ability to model a IUMPR groups. Tags: atp.recommendedPackage=DiagnosticIumprGroups
    """

    # DiagnosticIumprGroup method parity checklist:
    # Spec: AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf, Table 4.209, p.210
    # Columns: impl / docstring / test / reader / writer / release   ([—] = no XML element)
    # [x] __init__                 [x] impl  [x] docstring  [x] test  [—] reader  [—] writer  R23-11
    # [x] addIumprRef              [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getIumprRefs             [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] getIumprGroupIdentifier  [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setIumprGroupIdentifier  [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11

    def __init__(self, parent: ARObject, short_name: str):
        super().__init__(parent, short_name)

        # This reference collects DiagnosticIumpr to a Diagnostic IumprGroup. Stereotypes: atpSplitable Tags: atp.Splitkey=iumpr
        self.iumprRefs: List[RefType] = []

        # This aggregation allows for the variant modeling of the groupIdentifier. Stereotypes: atpSplitable; atpVariation Tags: atp.Splitkey=iumprGroupIdentifier.groupId, iumprGroup Identifier.variationPoint.shortLabel vh.latestBindingTime=postBuild
        self.iumprGroupIdentifier: Optional[DiagnosticIumprGroupIdentifier] = None

    def addIumprRef(self, ref: Optional[RefType]) -> DiagnosticIumprGroup:
        """
        This reference collects DiagnosticIumpr to a Diagnostic IumprGroup. Stereotypes: atpSplitable Tags: atp.Splitkey=iumpr

        A None value is a no-op and does not extend the iumprRefs list.
        """
        if ref is not None:
            self.iumprRefs.append(ref)
        return self

    def getIumprRefs(self) -> List[RefType]:
        """
        This reference collects DiagnosticIumpr to a Diagnostic IumprGroup. Stereotypes: atpSplitable Tags: atp.Splitkey=iumpr
        """
        return self.iumprRefs

    def getIumprGroupIdentifier(self) -> Optional[DiagnosticIumprGroupIdentifier]:
        """
        This aggregation allows for the variant modeling of the groupIdentifier. Stereotypes: atpSplitable; atpVariation Tags: atp.Splitkey=iumprGroupIdentifier.groupId, iumprGroup Identifier.variationPoint.shortLabel vh.latestBindingTime=postBuild
        """
        return self.iumprGroupIdentifier

    def setIumprGroupIdentifier(self, value: Optional[DiagnosticIumprGroupIdentifier]) -> DiagnosticIumprGroup:
        """
        This aggregation allows for the variant modeling of the groupIdentifier. Stereotypes: atpSplitable; atpVariation Tags: atp.Splitkey=iumprGroupIdentifier.groupId, iumprGroup Identifier.variationPoint.shortLabel vh.latestBindingTime=postBuild

        A None value is a no-op and does not overwrite an existing iumprGroupIdentifier.
        """
        if value is not None:
            self.iumprGroupIdentifier = value
        return self


class DiagnosticIumprToFunctionIdentifierMapping(DiagnosticMapping):
    """This meta-class represents the ability to associate a DiagnosticFunctionIdentifier with a DiagnosticIumpr. Tags: atp.recommendedPackage=DiagnosticMappings"""

    # DiagnosticIumprToFunctionIdentifierMapping method parity checklist:
    # Spec: AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf, Table 5.39, p.265
    # Columns: impl / docstring / test / reader / writer / release   ([—] = no XML element)
    # [x] __init__                           [x] impl  [x] docstring  [x] test  [—] reader  [—] writer  R23-11
    # [x] getFunctionIdentifierRef              [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setFunctionIdentifierRef              [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getIumprRef                           [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setIumprRef                           [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11

    def __init__(self, parent: ARObject, short_name: str):
        super().__init__(parent, short_name)

        # This reference identifies the applicable DiagnosticFunctionIdentifier.
        self.functionIdentifierRef: Optional[RefType] = None

        # This reference identifies the applicable DiagnosticIumpr.
        self.iumprRef: Optional[RefType] = None

    def getFunctionIdentifierRef(self) -> Optional[RefType]:
        """
        This reference identifies the applicable DiagnosticFunctionIdentifier.
        """
        return self.functionIdentifierRef

    def setFunctionIdentifierRef(self, value: Optional[RefType]) -> DiagnosticIumprToFunctionIdentifierMapping:
        """
        This reference identifies the applicable DiagnosticFunctionIdentifier.
        A None value is a no-op and does not overwrite an existing functionIdentifierRef.
        """
        if value is not None:
            self.functionIdentifierRef = value
        return self

    def getIumprRef(self) -> Optional[RefType]:
        """
        This reference identifies the applicable DiagnosticIumpr.
        """
        return self.iumprRef

    def setIumprRef(self, value: Optional[RefType]) -> DiagnosticIumprToFunctionIdentifierMapping:
        """
        This reference identifies the applicable DiagnosticIumpr.
        A None value is a no-op and does not overwrite an existing iumprRef.
        """
        if value is not None:
            self.iumprRef = value
        return self


class DiagnosticJ1939ExpandedFreezeFrame(DiagnosticCommonElement):
    """This meta-class represents the ability to model an expanded J1939 Freeze Frame. Tags: atp.recommendedPackage=DiagnosticJ1939ExpandedFreezeFrames"""

    # DiagnosticJ1939ExpandedFreezeFrame method parity checklist:
    # Spec: AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf, Table 4.221, p.221
    # Columns: impl / docstring / test / reader / writer / release   ([—] = no XML element)
    # [x] __init__     [x] impl  [x] docstring  [x] test  [—] reader  [—] writer  R23-11
    # [x] addSpnRef    [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getSpnRefs   [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] getNodeRef   [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setNodeRef   [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11

    def __init__(self, parent: ARObject, short_name: str):
        super().__init__(parent, short_name)

        # This represents the DiagnosticJ1939Node to which the J1939 expanded freeze frame is associated.
        self.nodeRef: Optional[RefType] = None

        # This represents the collection of SPNs that make the expanded J1939 Freeze Frame.
        self.spnRefs: List[RefType] = []

    def addSpnRef(self, value: Optional[RefType]) -> DiagnosticJ1939ExpandedFreezeFrame:
        """
        This represents the collection of SPNs that make the expanded J1939 Freeze Frame.
        A None value is a no-op and does not append an spnRef.
        """
        if value is not None:
            self.spnRefs.append(value)
        return self

    def getSpnRefs(self) -> List[RefType]:
        """
        This represents the collection of SPNs that make the expanded J1939 Freeze Frame.
        """
        return self.spnRefs

    def getNodeRef(self) -> Optional[RefType]:
        """
        This represents the DiagnosticJ1939Node to which the J1939 expanded freeze frame is associated.
        """
        return self.nodeRef

    def setNodeRef(self, value: Optional[RefType]) -> DiagnosticJ1939ExpandedFreezeFrame:
        """
        This represents the DiagnosticJ1939Node to which the J1939 expanded freeze frame is associated.
        A None value is a no-op and does not overwrite an existing node reference.
        """
        if value is not None:
            self.nodeRef = value
        return self


class DiagnosticJ1939FreezeFrame(DiagnosticCommonElement):
    """This meta-class represents the ability to model a J1939 Freeze Frame. Tags: atp.recommendedPackage=DiagnosticJ1939FreezeFrames"""

    # DiagnosticJ1939FreezeFrame method parity checklist:
    # Spec: AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf, Table 4.220, p.220
    # Columns: impl / docstring / test / reader / writer / release   ([—] = no XML element)
    # [x] __init__     [x] impl  [x] docstring  [x] test  [—] reader  [—] writer  R23-11
    # [x] addSpnRef    [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getSpnRefs   [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] getNodeRef   [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setNodeRef   [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11

    def __init__(self, parent: ARObject, short_name: str):
        super().__init__(parent, short_name)

        # This represents the DiagnosticJ1939Node to which the J1939 freeze frame is associated.
        self.nodeRef: Optional[RefType] = None

        # This represents the collection of SPNs that make the J1939 Freeze Frame.
        self.spnRefs: List[RefType] = []

    def addSpnRef(self, value: Optional[RefType]) -> DiagnosticJ1939FreezeFrame:
        """
        This represents the collection of SPNs that make the J1939 Freeze Frame.
        A None value is a no-op and does not append an spnRef.
        """
        if value is not None:
            self.spnRefs.append(value)
        return self

    def getSpnRefs(self) -> List[RefType]:
        """
        This represents the collection of SPNs that make the J1939 Freeze Frame.
        """
        return self.spnRefs

    def getNodeRef(self) -> Optional[RefType]:
        """
        This represents the DiagnosticJ1939Node to which the J1939 freeze frame is associated.
        """
        return self.nodeRef

    def setNodeRef(self, value: Optional[RefType]) -> DiagnosticJ1939FreezeFrame:
        """
        This represents the DiagnosticJ1939Node to which the J1939 freeze frame is associated.
        A None value is a no-op and does not overwrite an existing node reference.
        """
        if value is not None:
            self.nodeRef = value
        return self


class DiagnosticJ1939Node(DiagnosticCommonElement):
    """This meta-class represents the diagnostic configuration of a J1939 Nm node, which in turn represents a "virtual Ecu" on the J1939 communication bus. Tags: atp.recommendedPackage=DiagnosticJ1939Nodes"""

    # DiagnosticJ1939Node method parity checklist:
    # Spec: AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf, Table 5.41, p.267
    # Columns: impl / docstring / test / reader / writer / release   ([—] = no XML element)
    # [x] __init__                           [x] impl  [x] docstring  [x] test  [—] reader  [—] writer  R23-11
    # [x] getNmNodeRef                          [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setNmNodeRef                          [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11

    def __init__(self, parent: ARObject, short_name: str):
        super().__init__(parent, short_name)

        # This represents the reference to the "virtual Ecu" to which the enclosing DiagnosticJ1939Node is associated.
        self.nmNodeRef: Optional[RefType] = None

    def getNmNodeRef(self) -> Optional[RefType]:
        """
        This represents the reference to the "virtual Ecu" to which the enclosing DiagnosticJ1939Node is associated.
        """
        return self.nmNodeRef

    def setNmNodeRef(self, value: Optional[RefType]) -> DiagnosticJ1939Node:
        """
        This represents the reference to the "virtual Ecu" to which the enclosing DiagnosticJ1939Node is associated.
        A None value is a no-op and does not overwrite an existing nmNodeRef.
        """
        if value is not None:
            self.nmNodeRef = value
        return self


class DiagnosticFimFunctionMapping(DiagnosticSwMapping):
    """This meta-class represents the ability to define a mapping between a function identifier (FID) and the corresponding SwcServiceDependency in the application software resp. basic software. Tags: atp.recommendedPackage=DiagnosticFimFunctionMappings"""

    # DiagnosticFimFunctionMapping method parity checklist:
    # Spec: AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf, Table 5.37, p.265
    # Columns: impl / docstring / test / reader / writer / release   ([—] = no XML element)
    # [x] __init__                           [x] impl  [x] docstring  [x] test  [—] reader  [—] writer  R23-11
    # [x] getMappedBswServiceDependencyRef      [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setMappedBswServiceDependencyRef      [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getMappedFlatSwcServiceDependencyRef  [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setMappedFlatSwcServiceDependencyRef  [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getMappedFunctionRef                  [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setMappedFunctionRef                  [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getMappedSwcServiceDependencyRef      [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setMappedSwcServiceDependencyRef      [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11

    def __init__(self, parent: ARObject, short_name: str):
        super().__init__(parent, short_name)

        # This is supposed to represent a reference to a BswServiceDependency. the latter is not derived from Referrable and therefore this detour needs to be implemented to still let BswServiceDependency become the target of a reference.
        self.mappedBswServiceDependencyRef: Optional[RefType] = None

        # This represents the ability to refer to an AtomicSwComponentType that is available without the definition of how it will be embedded into the component hierarchy.
        self.mappedFlatSwcServiceDependencyRef: Optional[RefType] = None

        # This represents the mapped FID.
        self.mappedFunctionRef: Optional[RefType] = None

        # This represents the ability to point into the component hierarchy (under possible consideration of the rootSoftwareComposition). InstanceRef implemented by: SwcServiceDependencyInSystemInstanceRef
        self.mappedSwcServiceDependencyRef: Optional[RefType] = None

    def getMappedBswServiceDependencyRef(self) -> Optional[RefType]:
        """
        This is supposed to represent a reference to a BswServiceDependency. the latter is not derived from Referrable and therefore this detour needs to be implemented to still let BswServiceDependency become the target of a reference.
        """
        return self.mappedBswServiceDependencyRef

    def setMappedBswServiceDependencyRef(self, value: Optional[RefType]) -> DiagnosticFimFunctionMapping:
        """
        This is supposed to represent a reference to a BswServiceDependency. the latter is not derived from Referrable and therefore this detour needs to be implemented to still let BswServiceDependency become the target of a reference.
        A None value is a no-op and does not overwrite an existing mappedBswServiceDependencyRef.
        """
        if value is not None:
            self.mappedBswServiceDependencyRef = value
        return self

    def getMappedFlatSwcServiceDependencyRef(self) -> Optional[RefType]:
        """
        This represents the ability to refer to an AtomicSwComponentType that is available without the definition of how it will be embedded into the component hierarchy.
        """
        return self.mappedFlatSwcServiceDependencyRef

    def setMappedFlatSwcServiceDependencyRef(self, value: Optional[RefType]) -> DiagnosticFimFunctionMapping:
        """
        This represents the ability to refer to an AtomicSwComponentType that is available without the definition of how it will be embedded into the component hierarchy.
        A None value is a no-op and does not overwrite an existing mappedFlatSwcServiceDependencyRef.
        """
        if value is not None:
            self.mappedFlatSwcServiceDependencyRef = value
        return self

    def getMappedFunctionRef(self) -> Optional[RefType]:
        """
        This represents the mapped FID.
        """
        return self.mappedFunctionRef

    def setMappedFunctionRef(self, value: Optional[RefType]) -> DiagnosticFimFunctionMapping:
        """
        This represents the mapped FID.
        A None value is a no-op and does not overwrite an existing mappedFunctionRef.
        """
        if value is not None:
            self.mappedFunctionRef = value
        return self

    def getMappedSwcServiceDependencyRef(self) -> Optional[RefType]:
        """
        This represents the ability to point into the component hierarchy (under possible consideration of the rootSoftwareComposition). InstanceRef implemented by: SwcServiceDependencyInSystemInstanceRef
        """
        return self.mappedSwcServiceDependencyRef

    def setMappedSwcServiceDependencyRef(self, value: Optional[RefType]) -> DiagnosticFimFunctionMapping:
        """
        This represents the ability to point into the component hierarchy (under possible consideration of the rootSoftwareComposition). InstanceRef implemented by: SwcServiceDependencyInSystemInstanceRef
        A None value is a no-op and does not overwrite an existing mappedSwcServiceDependencyRef.
        """
        if value is not None:
            self.mappedSwcServiceDependencyRef = value
        return self


class DiagnosticJ1939Spn(DiagnosticCommonElement):
    """This meta-class represents the ability to model a J1939 Suspect Parameter Number (SPN). Tags: atp.recommendedPackage=DiagnosticJ1939Spns"""

    # DiagnosticJ1939Spn method parity checklist:
    # Spec: AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf, Table 4.219, p.219
    # Columns: impl / docstring / test / reader / writer / release   ([—] = no XML element)
    # [x] __init__     [x] impl  [x] docstring  [x] test  [—] reader  [—] writer  R23-11
    # [x] getSpn       [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setSpn       [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11

    def __init__(self, parent: ARObject, short_name: str):
        super().__init__(parent, short_name)

        # This attribute represents the concrete numerical identification for the enclosing SPN.
        self.spn: Optional[PositiveInteger] = None

    def getSpn(self) -> Optional[PositiveInteger]:
        """
        This attribute represents the concrete numerical identification for the enclosing SPN.
        """
        return self.spn

    def setSpn(self, value: Optional[PositiveInteger]) -> DiagnosticJ1939Spn:
        """
        This attribute represents the concrete numerical identification for the enclosing SPN.
        A None value is a no-op and does not overwrite an existing spn.
        """
        if value is not None:
            self.spn = value
        return self


class DiagnosticJ1939SpnMapping(DiagnosticMapping):
    """This meta-class represents the ability to define a mapping between an SPN and a SystemSignal. The existence of a mapping means that neither the SPN nor the SystemSignal need to be updated if the relation between the two changes. Tags: atp.recommendedPackage=DiagnosticJ1939SpnMappings"""

    # DiagnosticJ1939SpnMapping method parity checklist:
    # Spec: AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf, Table 5.40, p.267
    # Columns: impl / docstring / test / reader / writer / release   ([—] = no XML element)
    # [x] __init__                           [x] impl  [x] docstring  [x] test  [—] reader  [—] writer  R23-11
    # [x] addSendingNodeRef                     [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getSendingNodeRefs                    [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] getSpnRef                             [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setSpnRef                             [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getSystemSignalRef                    [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setSystemSignalRef                    [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11

    def __init__(self, parent: ARObject, short_name: str):
        super().__init__(parent, short_name)

        # This additional reference has a supporting role in that it identifies all sending nodes of a given SPN. It is positively possible that a given SPN is sent by more than one node. Even tough the reference targets the DiagnosticJ1939Node the semantics of the reference is bound to the J1939NmNode that is in turn referenced by the DiagnosticJ1939Node.
        self.sendingNodeRefs: List[RefType] = []

        # This reference goes to the SPN that shall be associated with a SystemSignal.
        self.spnRef: Optional[RefType] = None

        # This reference goes to the SystemSignal that shall be associated with an SPN.
        self.systemSignalRef: Optional[RefType] = None

    def addSendingNodeRef(self, value: Optional[RefType]) -> DiagnosticJ1939SpnMapping:
        """
        This additional reference has a supporting role in that it identifies all sending nodes of a given SPN. It is positively possible that a given SPN is sent by more than one node. Even tough the reference targets the DiagnosticJ1939Node the semantics of the reference is bound to the J1939NmNode that is in turn referenced by the DiagnosticJ1939Node.
        A None value is a no-op and does not append a sendingNodeRef.
        """
        if value is not None:
            self.sendingNodeRefs.append(value)
        return self

    def getSendingNodeRefs(self) -> List[RefType]:
        """
        This additional reference has a supporting role in that it identifies all sending nodes of a given SPN. It is positively possible that a given SPN is sent by more than one node. Even tough the reference targets the DiagnosticJ1939Node the semantics of the reference is bound to the J1939NmNode that is in turn referenced by the DiagnosticJ1939Node.
        """
        return self.sendingNodeRefs

    def getSpnRef(self) -> Optional[RefType]:
        """
        This reference goes to the SPN that shall be associated with a SystemSignal.
        """
        return self.spnRef

    def setSpnRef(self, value: Optional[RefType]) -> DiagnosticJ1939SpnMapping:
        """
        This reference goes to the SPN that shall be associated with a SystemSignal.
        A None value is a no-op and does not overwrite an existing spnRef.
        """
        if value is not None:
            self.spnRef = value
        return self

    def getSystemSignalRef(self) -> Optional[RefType]:
        """
        This reference goes to the SystemSignal that shall be associated with an SPN.
        """
        return self.systemSignalRef

    def setSystemSignalRef(self, value: Optional[RefType]) -> DiagnosticJ1939SpnMapping:
        """
        This reference goes to the SystemSignal that shall be associated with an SPN.
        A None value is a no-op and does not overwrite an existing systemSignalRef.
        """
        if value is not None:
            self.systemSignalRef = value
        return self


class DiagnosticJ1939SwMapping(DiagnosticSwMapping):
    """This meta-class represents the ability to map a piece of application software to a J1939DiagnosticNode. By this means the diagnostic configuration can be associated with the application software. Tags: atp.recommendedPackage=DiagnosticJ1939SwMappings"""

    # DiagnosticJ1939SwMapping method parity checklist:
    # Spec: AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf, Table 5.42, p.268
    # Columns: impl / docstring / test / reader / writer / release   ([—] = no XML element)
    # [x] __init__                           [x] impl  [x] docstring  [x] test  [—] reader  [—] writer  R23-11
    # [x] getNodeRef                            [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setNodeRef                            [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getSwComponentPrototypeRef            [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setSwComponentPrototypeRef            [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11

    def __init__(self, parent: ARObject, short_name: str):
        super().__init__(parent, short_name)

        # This represents the mapped DiagnosticJ1939Node.
        self.nodeRef: Optional[RefType] = None

        # This represents the mapped SwComponentPrototype. InstanceRef implemented by: ComponentInCompositionInstanceRef
        self.swComponentPrototypeRef: Optional[RefType] = None

    def getNodeRef(self) -> Optional[RefType]:
        """
        This represents the mapped DiagnosticJ1939Node.
        """
        return self.nodeRef

    def setNodeRef(self, value: Optional[RefType]) -> DiagnosticJ1939SwMapping:
        """
        This represents the mapped DiagnosticJ1939Node.
        A None value is a no-op and does not overwrite an existing nodeRef.
        """
        if value is not None:
            self.nodeRef = value
        return self

    def getSwComponentPrototypeRef(self) -> Optional[RefType]:
        """
        This represents the mapped SwComponentPrototype. InstanceRef implemented by: ComponentInCompositionInstanceRef
        """
        return self.swComponentPrototypeRef

    def setSwComponentPrototypeRef(self, value: Optional[RefType]) -> DiagnosticJ1939SwMapping:
        """
        This represents the mapped SwComponentPrototype. InstanceRef implemented by: ComponentInCompositionInstanceRef
        A None value is a no-op and does not overwrite an existing swComponentPrototypeRef.
        """
        if value is not None:
            self.swComponentPrototypeRef = value
        return self


class DiagnosticMasterToSlaveEventMapping(DiagnosticMapping):
    """This meta-class provides the ability to map a master diagnostic event with a slave diagnostic event such that reporting of the master event with a given value also reports the slave event with the same value Tags: atp.recommendedPackage=DiagnosticMappings"""

    # DiagnosticMasterToSlaveEventMapping method parity checklist:
    # Spec: AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf, Table 5.29, p.256
    # Columns: impl / docstring / test / reader / writer / release   ([—] = no XML element)
    # [x] __init__                           [x] impl  [x] docstring  [x] test  [—] reader  [—] writer  R23-11
    # [x] getMasterEventRef                     [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setMasterEventRef                     [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getSlaveEventRef                      [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setSlaveEventRef                      [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11

    def __init__(self, parent: ARObject, short_name: str):
        super().__init__(parent, short_name)

        # This represents the master diagnostic event.
        self.masterEventRef: Optional[RefType] = None

        # This represents the slave diagnostic event.
        self.slaveEventRef: Optional[RefType] = None

    def getMasterEventRef(self) -> Optional[RefType]:
        """
        This represents the master diagnostic event.
        """
        return self.masterEventRef

    def setMasterEventRef(self, value: Optional[RefType]) -> DiagnosticMasterToSlaveEventMapping:
        """
        This represents the master diagnostic event.
        A None value is a no-op and does not overwrite an existing masterEventRef.
        """
        if value is not None:
            self.masterEventRef = value
        return self

    def getSlaveEventRef(self) -> Optional[RefType]:
        """
        This represents the slave diagnostic event.
        """
        return self.slaveEventRef

    def setSlaveEventRef(self, value: Optional[RefType]) -> DiagnosticMasterToSlaveEventMapping:
        """
        This represents the slave diagnostic event.
        A None value is a no-op and does not overwrite an existing slaveEventRef.
        """
        if value is not None:
            self.slaveEventRef = value
        return self


class DiagnosticMeasurementIdentifier(ARElement):
    """
    This meta-class represents the ability to describe a measurement identifier.

    [constr_10414] Existence of attribute DiagnosticMeasurementIdentifier.obdMid: For each DiagnosticMeasurementIdentifier, attribute obdMid shall exist at the time when the DEXT is complete.
    """

    # DiagnosticMeasurementIdentifier method parity checklist:
    # Spec: AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf, Table 4.204, p.206
    # Columns: impl / docstring / test / reader / writer / release   ([—] = no XML element)
    # [x] __init__   [x] impl  [x] docstring  [x] test  [—] reader  [—] writer  R23-11
    # [x] getObdMid  [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setObdMid  [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11

    def __init__(self, parent: ARObject, short_name: str):
        super().__init__(parent, short_name)

        # This represents the numerical measurement Id Stereotypes: atpVariation Tags: vh.latestBindingTime=preCompileTime
        self.obdMid: Optional[PositiveInteger] = None

    def getObdMid(self) -> Optional[PositiveInteger]:
        """
        This represents the numerical measurement Id Stereotypes: atpVariation Tags: vh.latestBindingTime=preCompileTime
        """
        return self.obdMid

    def setObdMid(self, value: Optional[PositiveInteger]) -> DiagnosticMeasurementIdentifier:
        """
        This represents the numerical measurement Id Stereotypes: atpVariation Tags: vh.latestBindingTime=preCompileTime

        A None value is a no-op and does not overwrite an existing obdMid.
        """
        if value is not None:
            self.obdMid = value
        return self


class DiagnosticMemoryAddressableRangeAccess(DiagnosticMemoryByAddress, ABC):
    """This abstract base class"""

    # DiagnosticMemoryAddressableRangeAccess method parity checklist:
    # Spec: AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf, Table 4.111, p.140
    # Columns: impl / docstring / test / reader / writer / release   ([—] = no XML element)
    # [x] __init__           [x] impl  [x] docstring  [x] test  [—] reader  [—] writer  R23-11
    # [x] addMemoryRange     [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getMemoryRanges    [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11

    def __init__(self, parent: ARObject, short_name: str):
        if type(self) is DiagnosticMemoryAddressableRangeAccess:
            raise TypeError("DiagnosticMemoryAddressableRangeAccess is an abstract class.")

        super().__init__(parent, short_name)

        # This represents the formal description of the memory segment to which the DiagnosticMemoryByAddress applies.
        self.memoryRanges: List[RefType] = []

    def addMemoryRange(self, value: Optional[RefType]) -> DiagnosticMemoryAddressableRangeAccess:
        """
        This represents the formal description of the memory segment to which the DiagnosticMemoryByAddress applies.

        A None value is a no-op and does not append a memoryRange.
        """
        if value is not None:
            self.memoryRanges.append(value)
        return self

    def getMemoryRanges(self) -> List[RefType]:
        """
        This represents the formal description of the memory segment to which the DiagnosticMemoryByAddress applies.
        """
        return self.memoryRanges


class DiagnosticMemoryDestinationPrimary(ARElement, DiagnosticMemoryDestination):
    """This represents a primary memory for a diagnostic event. Tags: atp.recommendedPackage=DiagnosticMemoryDestinations"""

    # DiagnosticMemoryDestinationPrimary method parity checklist:
    # Spec: AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf, Table 4.173, p.184
    # Columns: impl / docstring / test / reader / writer / release   ([—] = no XML element)
    # [x] __init__                       [x] impl  [x] docstring  [x] test  [—] reader  [—] writer  R23-11
    # [x] getTypeOfDtcSupported          [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setTypeOfDtcSupported          [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11

    def __init__(self, parent: ARObject, short_name: str):
        DiagnosticMemoryDestination.__init__(self)
        super().__init__(parent, short_name)

        # This attribute defines the format returned by Dem_Dcm GetTranslationType and does not relate to/influence the supported Dem functionality.
        self.typeOfDtcSupported: Optional[DiagnosticTypeOfDtcSupportedEnum] = None

    def getTypeOfDtcSupported(self) -> Optional[DiagnosticTypeOfDtcSupportedEnum]:
        """
        This attribute defines the format returned by Dem_Dcm GetTranslationType and does not relate to/influence the supported Dem functionality.
        """
        return self.typeOfDtcSupported

    def setTypeOfDtcSupported(self, value: Optional[DiagnosticTypeOfDtcSupportedEnum]) -> DiagnosticMemoryDestinationPrimary:
        """
        This attribute defines the format returned by Dem_Dcm GetTranslationType and does not relate to/influence the supported Dem functionality.

        A None value is a no-op and does not overwrite an existing typeOfDtcSupported.
        """
        if value is not None:
            self.typeOfDtcSupported = value
        return self


class DiagnosticMemoryIdentifier(ARElement):
    """This meta-class represents the ability to define memory properties from the diagnostics point of view. Tags: atp.recommendedPackage=DiagnosticMemoryByAdresss"""

    # DiagnosticMemoryIdentifier method parity checklist:
    # Spec: AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf, Table 4.112, p.140
    # Columns: impl / docstring / test / reader / writer / release   ([—] = no XML element)
    # [x] __init__                       [x] impl  [x] docstring  [x] test  [—] reader  [—] writer  R23-11
    # [x] getAccessPermissionRef         [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setAccessPermissionRef         [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getId                          [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setId                          [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getMemoryHighAddress           [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setMemoryHighAddress           [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getMemoryHighAddressLabel      [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setMemoryHighAddressLabel      [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getMemoryLowAddress            [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setMemoryLowAddress            [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getMemoryLowAddressLabel       [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setMemoryLowAddressLabel       [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11

    def __init__(self, parent: ARObject, short_name: str):
        super().__init__(parent, short_name)

        # This represents that access permission defined for the specific DiagnosticMemoryIdentifier. Stereotypes: atpSplitable Tags: atp.Splitkey=accessPermission
        self.accessPermissionRef: Optional[RefType] = None

        # This represents the identification of the memory segment.
        self.id: Optional[PositiveInteger] = None

        # This represents the upper bound for addresses of the memory segment.
        self.memoryHighAddress: Optional[PositiveInteger] = None

        # This represents a symbolic label for the upper bound for addresses of the memory segment.
        self.memoryHighAddressLabel: Optional[String] = None

        # This represents the lower bound for addresses of the memory segment.
        self.memoryLowAddress: Optional[PositiveInteger] = None

        # This represents a symbolic label for the lower bound for addresses of the memory segment.
        self.memoryLowAddressLabel: Optional[String] = None

    def getAccessPermissionRef(self) -> Optional[RefType]:
        """
        This represents that access permission defined for the specific DiagnosticMemoryIdentifier. Stereotypes: atpSplitable Tags: atp.Splitkey=accessPermission
        """
        return self.accessPermissionRef

    def setAccessPermissionRef(self, value: Optional[RefType]) -> DiagnosticMemoryIdentifier:
        """
        This represents that access permission defined for the specific DiagnosticMemoryIdentifier. Stereotypes: atpSplitable Tags: atp.Splitkey=accessPermission

        A None value is a no-op and does not overwrite an existing accessPermissionRef.
        """
        if value is not None:
            self.accessPermissionRef = value
        return self

    def getId(self) -> Optional[PositiveInteger]:
        """
        This represents the identification of the memory segment.
        """
        return self.id

    def setId(self, value: Optional[PositiveInteger]) -> DiagnosticMemoryIdentifier:
        """
        This represents the identification of the memory segment.

        A None value is a no-op and does not overwrite an existing id.
        """
        if value is not None:
            self.id = value
        return self

    def getMemoryHighAddress(self) -> Optional[PositiveInteger]:
        """
        This represents the upper bound for addresses of the memory segment.
        """
        return self.memoryHighAddress

    def setMemoryHighAddress(self, value: Optional[PositiveInteger]) -> DiagnosticMemoryIdentifier:
        """
        This represents the upper bound for addresses of the memory segment.

        A None value is a no-op and does not overwrite an existing memoryHighAddress.
        """
        if value is not None:
            self.memoryHighAddress = value
        return self

    def getMemoryHighAddressLabel(self) -> Optional[String]:
        """
        This represents a symbolic label for the upper bound for addresses of the memory segment.
        """
        return self.memoryHighAddressLabel

    def setMemoryHighAddressLabel(self, value: Optional[String]) -> DiagnosticMemoryIdentifier:
        """
        This represents a symbolic label for the upper bound for addresses of the memory segment.

        A None value is a no-op and does not overwrite an existing memoryHighAddressLabel.
        """
        if value is not None:
            self.memoryHighAddressLabel = value
        return self

    def getMemoryLowAddress(self) -> Optional[PositiveInteger]:
        """
        This represents the lower bound for addresses of the memory segment.
        """
        return self.memoryLowAddress

    def setMemoryLowAddress(self, value: Optional[PositiveInteger]) -> DiagnosticMemoryIdentifier:
        """
        This represents the lower bound for addresses of the memory segment.

        A None value is a no-op and does not overwrite an existing memoryLowAddress.
        """
        if value is not None:
            self.memoryLowAddress = value
        return self

    def getMemoryLowAddressLabel(self) -> Optional[String]:
        """
        This represents a symbolic label for the lower bound for addresses of the memory segment.
        """
        return self.memoryLowAddressLabel

    def setMemoryLowAddressLabel(self, value: Optional[String]) -> DiagnosticMemoryIdentifier:
        """
        This represents a symbolic label for the lower bound for addresses of the memory segment.

        A None value is a no-op and does not overwrite an existing memoryLowAddressLabel.
        """
        if value is not None:
            self.memoryLowAddressLabel = value
        return self


class DiagnosticOperationCycle(ARElement):
    """Definition of an operation cycle that is the base of the event qualifying and for Dem scheduling. Tags: atp.recommendedPackage=DiagnosticOperationCycles"""

    # DiagnosticOperationCycle method parity checklist:
    # Spec: AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf, Table 4.196, p.201
    # Columns: impl / docstring / test / reader / writer / release   ([—] = no XML element)
    # [x] __init__  [x] impl  [x] docstring  [x] test  [—] reader  [—] writer  R23-11
    # [x] getType   [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setType   [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11

    def __init__(self, parent: ARObject, short_name: str):
        super().__init__(parent, short_name)

        # Operation cycles types for the Dem.
        self.type: Optional[DiagnosticOperationCycleTypeEnum] = None

    def getType(self) -> Optional[DiagnosticOperationCycleTypeEnum]:
        """
        Operation cycles types for the Dem.
        """
        return self.type

    def setType(self, value: Optional[DiagnosticOperationCycleTypeEnum]) -> DiagnosticOperationCycle:
        """
        Operation cycles types for the Dem.

        A None value is a no-op and does not overwrite an existing type.
        """
        if value is not None:
            self.type = value
        return self


class DiagnosticOperationCyclePortMapping(DiagnosticSwMapping):
    """Defines to which SWC service ports the DiagnosticOperationCycle is mapped. Tags: atp.recommendedPackage=DiagnosticMappings"""

    # DiagnosticOperationCyclePortMapping method parity checklist:
    # Spec: AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf, Table 5.25, p.250
    # Columns: impl / docstring / test / reader / writer / release   ([—] = no XML element)
    # [x] __init__                [x] impl  [x] docstring  [x] test  [—] reader  [—] writer  R23-11
    # [x] getOperationCycleRef                         [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setOperationCycleRef                         [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getSwcFlatServiceDependencyRef               [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setSwcFlatServiceDependencyRef               [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getSwcServiceDependencyInSystemIRef          [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setSwcServiceDependencyInSystemIRef          [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11

    def __init__(self, parent: ARObject, short_name: str):
        super().__init__(parent, short_name)

        # Reference to the DiagnosticOperationCycle that is assigned to SWC service ports.
        self.operationCycleRef: Optional[RefType] = None

        # Reference to a SwcServiceDependencyType that links ServiceNeeds to SWC service ports.
        self.swcFlatServiceDependencyRef: Optional[RefType] = None

        # Instance reference to a SwcServiceDependency that links ServiceNeeds to SWC service ports. InstanceRef implemented by: SwcServiceDependencyInSystemInstanceRef
        self.swcServiceDependencyInSystemIRef: Optional[RefType] = None

    def getOperationCycleRef(self) -> Optional[RefType]:
        """
        Reference to the DiagnosticOperationCycle that is assigned to SWC service ports.
        """
        return self.operationCycleRef

    def setOperationCycleRef(self, value: Optional[RefType]) -> DiagnosticOperationCyclePortMapping:
        """
        Reference to the DiagnosticOperationCycle that is assigned to SWC service ports.
        A None value is a no-op and does not overwrite an existing operationCycleRef.
        """
        if value is not None:
            self.operationCycleRef = value
        return self

    def getSwcFlatServiceDependencyRef(self) -> Optional[RefType]:
        """
        Reference to a SwcServiceDependencyType that links ServiceNeeds to SWC service ports.
        """
        return self.swcFlatServiceDependencyRef

    def setSwcFlatServiceDependencyRef(self, value: Optional[RefType]) -> DiagnosticOperationCyclePortMapping:
        """
        Reference to a SwcServiceDependencyType that links ServiceNeeds to SWC service ports.
        A None value is a no-op and does not overwrite an existing swcFlatServiceDependencyRef.
        """
        if value is not None:
            self.swcFlatServiceDependencyRef = value
        return self

    def getSwcServiceDependencyInSystemIRef(self) -> Optional[RefType]:
        """
        Instance reference to a SwcServiceDependency that links ServiceNeeds to SWC service ports. InstanceRef implemented by: SwcServiceDependencyInSystemInstanceRef
        """
        return self.swcServiceDependencyInSystemIRef

    def setSwcServiceDependencyInSystemIRef(self, value: Optional[RefType]) -> DiagnosticOperationCyclePortMapping:
        """
        Instance reference to a SwcServiceDependency that links ServiceNeeds to SWC service ports. InstanceRef implemented by: SwcServiceDependencyInSystemInstanceRef
        A None value is a no-op and does not overwrite an existing swcServiceDependencyInSystemIRef.
        """
        if value is not None:
            self.swcServiceDependencyInSystemIRef = value
        return self


class DiagnosticParameterIdentifier(ARElement):
    """This meta-class represents the ability to model a diagnostic parameter identifier (PID) for the purpose of executing on-board diagnostics (OBD). Tags: atp.recommendedPackage=DiagnosticParameterIdentifiers"""

    # DiagnosticParameterIdentifier method parity checklist:
    # Spec: AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf, Table 4.127, p.149
    # Columns: impl / docstring / test / reader / writer / release   ([—] = no XML element)
    # [x] __init__                [x] impl  [x] docstring  [x] test  [—] reader  [—] writer  R23-11
    # [x] getDataElements         [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] addDataElement          [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getId                   [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setId                   [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getPidSize              [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setPidSize              [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getSupportInfoByte      [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setSupportInfoByte      [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11

    def __init__(self, parent: ARObject, short_name: str):
        super().__init__(parent, short_name)

        # This represents the data carried by the DiagnosticParameterIdentifier. Stereotypes: atpSplitable; atpVariation Tags: atp.Splitkey=dataElement.bitOffset, dataElement.ident.shortName, dataElement.variationPoint.shortLabel vh.latestBindingTime=postBuild
        self.dataElements: List[DiagnosticParameter] = []

        # This is the numerical identifier used to identify the DiagnosticParameterIdentifier in the scope of diagnostic workflow (see SAE J1979-DA).
        self.id: Optional[PositiveInteger] = None

        # The size of the entire PID can be greater than the sum of the data elements because padding might be applied. Unit: byte.
        self.pidSize: Optional[PositiveInteger] = None

        # This represents the supported information associated with the DiagnosticParameterIdentifier.
        self.supportInfoByte: Optional[DiagnosticSupportInfoByte] = None

    def getDataElements(self) -> List[DiagnosticParameter]:
        """
        This represents the data carried by the DiagnosticParameterIdentifier. Stereotypes: atpSplitable; atpVariation Tags: atp.Splitkey=dataElement.bitOffset, dataElement.ident.shortName, dataElement.variationPoint.shortLabel vh.latestBindingTime=postBuild
        """
        return self.dataElements

    def addDataElement(self, value: Optional[DiagnosticParameter]) -> DiagnosticParameterIdentifier:
        """
        This represents the data carried by the DiagnosticParameterIdentifier. Stereotypes: atpSplitable; atpVariation Tags: atp.Splitkey=dataElement.bitOffset, dataElement.ident.shortName, dataElement.variationPoint.shortLabel vh.latestBindingTime=postBuild

        A None value is a no-op and does not append a dataElement.
        """
        if value is not None:
            self.dataElements.append(value)
        return self

    def getId(self) -> Optional[PositiveInteger]:
        """
        This is the numerical identifier used to identify the DiagnosticParameterIdentifier in the scope of diagnostic workflow (see SAE J1979-DA).
        """
        return self.id

    def setId(self, value: Optional[PositiveInteger]) -> DiagnosticParameterIdentifier:
        """
        This is the numerical identifier used to identify the DiagnosticParameterIdentifier in the scope of diagnostic workflow (see SAE J1979-DA).

        A None value is a no-op and does not overwrite an existing id.
        """
        if value is not None:
            self.id = value
        return self

    def getPidSize(self) -> Optional[PositiveInteger]:
        """
        The size of the entire PID can be greater than the sum of the data elements because padding might be applied. Unit: byte.
        """
        return self.pidSize

    def setPidSize(self, value: Optional[PositiveInteger]) -> DiagnosticParameterIdentifier:
        """
        The size of the entire PID can be greater than the sum of the data elements because padding might be applied. Unit: byte.

        A None value is a no-op and does not overwrite an existing pidSize.
        """
        if value is not None:
            self.pidSize = value
        return self

    def getSupportInfoByte(self) -> Optional[DiagnosticSupportInfoByte]:
        """
        This represents the supported information associated with the DiagnosticParameterIdentifier.
        """
        return self.supportInfoByte

    def setSupportInfoByte(self, value: Optional[DiagnosticSupportInfoByte]) -> DiagnosticParameterIdentifier:
        """
        This represents the supported information associated with the DiagnosticParameterIdentifier.

        A None value is a no-op and does not overwrite an existing supportInfoByte.
        """
        if value is not None:
            self.supportInfoByte = value
        return self


class DiagnosticPowertrainFreezeFrame(ARElement):
    """This meta-class represents a powertrain-related freeze-frame. In theory, this meta-class would need an additional id attribute. However, legal regulations requires only a single value for this attribute anyway. Tags: atp.recommendedPackage=DiagnosticPowertrainFreezeFrames"""

    # DiagnosticPowertrainFreezeFrame method parity checklist:
    # Spec: AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf, Table 4.134, p.153
    # Columns: impl / docstring / test / reader / writer / release   ([—] = no XML element)
    # [x] __init__      [x] impl  [x] docstring  [x] test  [—] reader  [—] writer  R23-11
    # [x] getPidRefs    [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] addPidRef     [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11

    def __init__(self, parent: ARObject, short_name: str):
        super().__init__(parent, short_name)

        # This represents the PID associated with this instance of the OBD mode 0x02 service.
        self.pidRefs: List[RefType] = []

    def getPidRefs(self) -> List[RefType]:
        """
        This represents the PID associated with this instance of the OBD mode 0x02 service.
        """
        return self.pidRefs

    def addPidRef(self, value: Optional[RefType]) -> DiagnosticPowertrainFreezeFrame:
        """
        This represents the PID associated with this instance of the OBD mode 0x02 service.

        A None value is a no-op and does not append a pidRef.
        """
        if value is not None:
            self.pidRefs.append(value)
        return self


class DiagnosticProofOfOwnership(DiagnosticAuthentication):
    """This meta-class represents the subfunction to provide proof of ownership."""

    # DiagnosticProofOfOwnership method parity checklist:
    # Spec: AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf, Table 4.57, p.100
    # Columns: impl / docstring / test / reader / writer / release   ([—] = no XML element)
    # [x] __init__  [x] impl  [x] docstring  [x] test  [x] reader  [x] writer  R23-11

    def __init__(self, parent: ARObject, short_name: str):
        super().__init__(parent, short_name)


class DiagnosticProtocol(ARElement):
    """
    This meta-class represents the ability to define a diagnostic protocol.

    [constr_1794] Existence of attribute DiagnosticProtocol.priority: For each DiagnosticProtocol, attribute priority shall exist at the time when the DEXT is complete.
    [constr_1795] Existence of attribute DiagnosticProtocol.protocolKind: For each DiagnosticProtocol, attribute protocolKind shall exist at the time when the DEXT is complete.
    """

    # DiagnosticProtocol method parity checklist:
    # Spec: AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf, Table 4.15, p.58
    # Columns: impl / docstring / test / reader / writer / release   ([—] = no XML element)
    # [x] __init__                        [x] impl  [x] docstring  [x] test  [—] reader  [—] writer  R23-11
    # [x] addDiagnosticConnectionRef      [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getDiagnosticConnectionRefs     [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] getPriority                     [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setPriority                     [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getProtocolKind                 [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setProtocolKind                 [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getSendRespPendOnTransToBoot    [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setSendRespPendOnTransToBoot    [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getServiceTableRef              [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setServiceTableRef              [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11

    def __init__(self, parent: ARObject, short_name: str):
        super().__init__(parent, short_name)

        # This represents the collection of applicable Diagnostic Connections for this DiagnosticProtocol.
        self.diagnosticConnectionRefs: List[RefType] = []

        # This represents the priority of the diagnostic protocol in comparison to other diagnostic protocols. Lower numeric values represent higher protocol priority: • 0 - Highest protocol priority • 255 - Lowest protocol priority
        self.priority: Optional[PositiveInteger] = None

        # This identifies the applicable protocol.
        self.protocolKind: Optional[NameToken] = None

        # The purpose of this attribute is to define whether or not the ECU should send a NRC 0x78 (response pending) before transitioning to the bootloader (in this case the attribute shall be set to "true") or if the transition shall be initiated without sending NRC 0x78 (in this case the attribute shall be set to "false").
        self.sendRespPendOnTransToBoot: Optional[Boolean] = None

        # This represents the service table applicable for the given diagnostic protocol.
        self.serviceTableRef: Optional[RefType] = None

    def addDiagnosticConnectionRef(self, value: Optional[RefType]) -> DiagnosticProtocol:
        """
        This represents the collection of applicable Diagnostic Connections for this DiagnosticProtocol.
        A None value is a no-op and does not append a diagnosticConnectionRef.
        """
        if value is not None:
            self.diagnosticConnectionRefs.append(value)
        return self

    def getDiagnosticConnectionRefs(self) -> List[RefType]:
        """
        This represents the collection of applicable Diagnostic Connections for this DiagnosticProtocol.
        """
        return self.diagnosticConnectionRefs

    def getPriority(self) -> Optional[PositiveInteger]:
        """
        This represents the priority of the diagnostic protocol in comparison to other diagnostic protocols. Lower numeric values represent higher protocol priority: • 0 - Highest protocol priority • 255 - Lowest protocol priority
        """
        return self.priority

    def setPriority(self, value: Optional[PositiveInteger]) -> DiagnosticProtocol:
        """
        This represents the priority of the diagnostic protocol in comparison to other diagnostic protocols. Lower numeric values represent higher protocol priority: • 0 - Highest protocol priority • 255 - Lowest protocol priority
        A None value is a no-op and does not overwrite an existing priority.
        """
        if value is not None:
            self.priority = value
        return self

    def getProtocolKind(self) -> Optional[NameToken]:
        """
        This identifies the applicable protocol.
        """
        return self.protocolKind

    def setProtocolKind(self, value: Optional[NameToken]) -> DiagnosticProtocol:
        """
        This identifies the applicable protocol.
        A None value is a no-op and does not overwrite an existing protocolKind.
        """
        if value is not None:
            self.protocolKind = value
        return self

    def getSendRespPendOnTransToBoot(self) -> Optional[Boolean]:
        """
        The purpose of this attribute is to define whether or not the ECU should send a NRC 0x78 (response pending) before transitioning to the bootloader (in this case the attribute shall be set to "true") or if the transition shall be initiated without sending NRC 0x78 (in this case the attribute shall be set to "false").
        """
        return self.sendRespPendOnTransToBoot

    def setSendRespPendOnTransToBoot(self, value: Optional[Boolean]) -> DiagnosticProtocol:
        """
        The purpose of this attribute is to define whether or not the ECU should send a NRC 0x78 (response pending) before transitioning to the bootloader (in this case the attribute shall be set to "true") or if the transition shall be initiated without sending NRC 0x78 (in this case the attribute shall be set to "false").
        A None value is a no-op and does not overwrite an existing sendRespPendOnTransToBoot.
        """
        if value is not None:
            self.sendRespPendOnTransToBoot = value
        return self

    def getServiceTableRef(self) -> Optional[RefType]:
        """
        This represents the service table applicable for the given diagnostic protocol.
        """
        return self.serviceTableRef

    def setServiceTableRef(self, value: Optional[RefType]) -> DiagnosticProtocol:
        """
        This represents the service table applicable for the given diagnostic protocol.
        A None value is a no-op and does not overwrite an existing serviceTableRef.
        """
        if value is not None:
            self.serviceTableRef = value
        return self


class DiagnosticReadDTCInformation(ARElement):
    """This represents an instance of the "Read DTC Information" diagnostic service."""

    # DiagnosticReadDTCInformation method parity checklist:
    # Spec: AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf, Table 4.106, p.136
    # Columns: impl / docstring / test / reader / writer / release   ([—] = no XML element)
    # [x] __init__                         [x] impl  [x] docstring  [x] test  [—] reader  [—] writer  R23-11
    # [x] getReadDTCInformationClass       [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setReadDTCInformationClass       [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11

    def __init__(self, parent: ARObject, short_name: str):
        super().__init__(parent, short_name)

        # This reference substantiates that abstract reference in the role serviceClass for this specific concrete class. Thereby, the reference represents the ability to access shared attributes among all DiagnosticReadDTCInformation in the given context.
        self.readDTCInformationClass: Optional[RefType] = None

    def getReadDTCInformationClass(self) -> Optional[RefType]:
        """
        This reference substantiates that abstract reference in the role serviceClass for this specific concrete class. Thereby, the reference represents the ability to access shared attributes among all DiagnosticReadDTCInformation in the given context.
        """
        return self.readDTCInformationClass

    def setReadDTCInformationClass(self, value: Optional[RefType]) -> DiagnosticReadDTCInformation:
        """
        This reference substantiates that abstract reference in the role serviceClass for this specific concrete class. Thereby, the reference represents the ability to access shared attributes among all DiagnosticReadDTCInformation in the given context.

        A None value is a no-op and does not overwrite an existing readDTCInformationClass.
        """
        if value is not None:
            self.readDTCInformationClass = value
        return self


class DiagnosticReadDataByIdentifier(DiagnosticDataByIdentifier):
    """This represents an instance of the "Read Data by Identifier" diagnostic service."""

    # DiagnosticReadDataByIdentifier method parity checklist:
    # Spec: AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf, Table 4.70, p.112
    # Columns: impl / docstring / test / reader / writer / release   ([—] = no XML element)
    # [x] __init__          [x] impl  [x] docstring  [x] test  [—] reader  [—] writer  R23-11
    # [x] getReadClass      [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setReadClass      [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11

    def __init__(self, parent: ARObject, short_name: str):
        super().__init__(parent, short_name)

        # This reference substantiates that abstract reference in the role serviceClass for this specific concrete class. Thereby, the reference represents the ability to access shared attributes among all DiagnosticReadDataByIdentifier in the given context.
        self.readClass: Optional[RefType] = None

    def getReadClass(self) -> Optional[RefType]:
        """
        This reference substantiates that abstract reference in the role serviceClass for this specific concrete class. Thereby, the reference represents the ability to access shared attributes among all DiagnosticReadDataByIdentifier in the given context.
        """
        return self.readClass

    def setReadClass(self, value: Optional[RefType]) -> DiagnosticReadDataByIdentifier:
        """
        This reference substantiates that abstract reference in the role serviceClass for this specific concrete class. Thereby, the reference represents the ability to access shared attributes among all DiagnosticReadDataByIdentifier in the given context.

        A None value is a no-op and does not overwrite an existing readClass.
        """
        if value is not None:
            self.readClass = value
        return self


class DiagnosticReadDataByPeriodicID(ARElement):
    """This represents an instance of the "Read Data by periodic Identifier" diagnostic service."""

    # DiagnosticReadDataByPeriodicID method parity checklist:
    # Spec: AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf, Table 4.97, p.130
    # Columns: impl / docstring / test / reader / writer / release   ([—] = no XML element)
    # [x] __init__               [x] impl  [x] docstring  [x] test  [—] reader  [—] writer  R23-11
    # [x] getReadDataClass       [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setReadDataClass       [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11

    def __init__(self, parent: ARObject, short_name: str):
        super().__init__(parent, short_name)

        # This reference substantiates that abstract reference in the role serviceClass for this specific concrete class. Thereby, the reference represents the ability to access shared attributes among all DiagnosticReadDataByPeriodicID in the given context.
        self.readDataClass: Optional[RefType] = None

    def getReadDataClass(self) -> Optional[RefType]:
        """
        This reference substantiates that abstract reference in the role serviceClass for this specific concrete class. Thereby, the reference represents the ability to access shared attributes among all DiagnosticReadDataByPeriodicID in the given context.
        """
        return self.readDataClass

    def setReadDataClass(self, value: Optional[RefType]) -> DiagnosticReadDataByPeriodicID:
        """
        This reference substantiates that abstract reference in the role serviceClass for this specific concrete class. Thereby, the reference represents the ability to access shared attributes among all DiagnosticReadDataByPeriodicID in the given context.

        A None value is a no-op and does not overwrite an existing readDataClass.
        """
        if value is not None:
            self.readDataClass = value
        return self


class DiagnosticReadScalingDataByIdentifier(DiagnosticDataByIdentifier):
    """This represents an instance of the "Read Scaling Data by Identifier" diagnostic service."""

    # DiagnosticReadScalingDataByIdentifier method parity checklist:
    # Spec: AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf, Table 4.78, p.116
    # Columns: impl / docstring / test / reader / writer / release   ([—] = no XML element)
    # [x] __init__                  [x] impl  [x] docstring  [x] test  [—] reader  [—] writer  R23-11
    # [x] getReadScalingDataClass   [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setReadScalingDataClass   [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11

    def __init__(self, parent: ARObject, short_name: str):
        super().__init__(parent, short_name)

        # This reference substantiates that abstract reference in the role serviceClass for this specific concrete class. Thereby, the reference represents the ability to access shared attributes among all DiagnosticReadScalingDataByIdentifier in the given context.
        self.readScalingDataClass: Optional[RefType] = None

    def getReadScalingDataClass(self) -> Optional[RefType]:
        """
        This reference substantiates that abstract reference in the role serviceClass for this specific concrete class. Thereby, the reference represents the ability to access shared attributes among all DiagnosticReadScalingDataByIdentifier in the given context.
        """
        return self.readScalingDataClass

    def setReadScalingDataClass(self, value: Optional[RefType]) -> DiagnosticReadScalingDataByIdentifier:
        """
        This reference substantiates that abstract reference in the role serviceClass for this specific concrete class. Thereby, the reference represents the ability to access shared attributes among all DiagnosticReadScalingDataByIdentifier in the given context.

        A None value is a no-op and does not overwrite an existing readScalingDataClass.
        """
        if value is not None:
            self.readScalingDataClass = value
        return self


class DiagnosticRequestControlOfOnBoardDevice(DiagnosticServiceInstance):
    """This meta-class represents the ability to model an instance of the OBD mode 0x08 service. Tags: atp.recommendedPackage=DiagnosticRequestControlOfOnBoardDevices"""

    # DiagnosticRequestControlOfOnBoardDevice method parity checklist:
    # Spec: AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf, Table 4.141, p.157
    # Columns: impl / docstring / test / reader / writer / release   ([—] = no XML element)
    # [x] __init__                                          [x] impl  [x] docstring  [x] test  [—] reader  [—] writer  R23-11
    # [x] getRequestControlOfOnBoardDeviceClassRef          [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setRequestControlOfOnBoardDeviceClassRef          [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getTestIdRef                                      [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setTestIdRef                                      [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11

    def __init__(self, parent: ARObject, short_name: str):
        super().__init__(parent, short_name)

        # This reference substantiates that abstract reference in the role serviceClass for this specific concrete class. Thereby, the reference represents the ability to access shared attributes among all DiagnosticRequestControlOfOnBoardDevice in the given context.
        self.requestControlOfOnBoardDeviceClassRef: Optional[RefType] = None

        # This represents the test Id for the mode 0x08.
        self.testIdRef: Optional[RefType] = None

    def getRequestControlOfOnBoardDeviceClassRef(self) -> Optional[RefType]:
        """
        This reference substantiates that abstract reference in the role serviceClass for this specific concrete class. Thereby, the reference represents the ability to access shared attributes among all DiagnosticRequestControlOfOnBoardDevice in the given context.
        """
        return self.requestControlOfOnBoardDeviceClassRef

    def setRequestControlOfOnBoardDeviceClassRef(self, value: Optional[RefType]) -> DiagnosticRequestControlOfOnBoardDevice:
        """
        This reference substantiates that abstract reference in the role serviceClass for this specific concrete class. Thereby, the reference represents the ability to access shared attributes among all DiagnosticRequestControlOfOnBoardDevice in the given context.

        A None value is a no-op and does not overwrite an existing requestControlOfOnBoardDeviceClassRef.
        """
        if value is not None:
            self.requestControlOfOnBoardDeviceClassRef = value
        return self

    def getTestIdRef(self) -> Optional[RefType]:
        """
        This represents the test Id for the mode 0x08.
        """
        return self.testIdRef

    def setTestIdRef(self, value: Optional[RefType]) -> DiagnosticRequestControlOfOnBoardDevice:
        """
        This represents the test Id for the mode 0x08.

        A None value is a no-op and does not overwrite an existing testIdRef.
        """
        if value is not None:
            self.testIdRef = value
        return self


class DiagnosticRequestDownload(DiagnosticMemoryAddressableRangeAccess):
    """This represents an instance of the "Request Download" diagnostic service. Tags: atp.recommendedPackage=DiagnosticMemoryByAdresss"""

    # DiagnosticRequestDownload method parity checklist:
    # Spec: AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf, Table 4.121, p.144
    # Columns: impl / docstring / test / reader / writer / release   ([—] = no XML element)
    # [x] __init__                    [x] impl  [x] docstring  [x] test  [—] reader  [—] writer  R23-11
    # [x] getRequestDownloadClassRef  [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setRequestDownloadClassRef  [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11

    def __init__(self, parent: ARObject, short_name: str):
        super().__init__(parent, short_name)

        # This reference substantiates that abstract reference in the role serviceClass for this specific concrete class. Thereby, the reference represents the ability to access shared attributes among all DiagnosticRequestDownload in the given context.
        self.requestDownloadClassRef: Optional[RefType] = None

    def getRequestDownloadClassRef(self) -> Optional[RefType]:
        """
        This reference substantiates that abstract reference in the role serviceClass for this specific concrete class. Thereby, the reference represents the ability to access shared attributes among all DiagnosticRequestDownload in the given context.
        """
        return self.requestDownloadClassRef

    def setRequestDownloadClassRef(self, value: Optional[RefType]) -> DiagnosticRequestDownload:
        """
        This reference substantiates that abstract reference in the role serviceClass for this specific concrete class. Thereby, the reference represents the ability to access shared attributes among all DiagnosticRequestDownload in the given context.

        A None value is a no-op and does not overwrite an existing requestDownloadClassRef.
        """
        if value is not None:
            self.requestDownloadClassRef = value
        return self


class DiagnosticRequestEmissionRelatedDTCPermanentStatus(DiagnosticServiceInstance):
    """This meta-class represents the ability to model an instance of the OBD mode 0x0A service. Tags: atp.recommendedPackage=DiagnosticRequestEmissionRelatedDTCPermanentStatuss"""

    # DiagnosticRequestEmissionRelatedDTCPermanentStatus method parity checklist:
    # Spec: AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf, Table 4.147, p.161
    # Columns: impl / docstring / test / reader / writer / release   ([—] = no XML element)
    # [x] __init__                                             [x] impl  [x] docstring  [x] test  [—] reader  [—] writer  R23-11
    # [x] getRequestEmissionRelatedDtcClassPermanentStatusRef  [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setRequestEmissionRelatedDtcClassPermanentStatusRef  [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11

    def __init__(self, parent: ARObject, short_name: str):
        super().__init__(parent, short_name)

        # This reference substantiates that abstract reference in the role serviceClass for this specific concrete class. Thereby, the reference represents the ability to access shared attributes among all DiagnosticRequestEmissionRelatedDTCPermanentStatus in the given context.
        self.requestEmissionRelatedDtcClassPermanentStatusRef: Optional[RefType] = None

    def getRequestEmissionRelatedDtcClassPermanentStatusRef(self) -> Optional[RefType]:
        """
        This reference substantiates that abstract reference in the role serviceClass for this specific concrete class. Thereby, the reference represents the ability to access shared attributes among all DiagnosticRequestEmissionRelatedDTCPermanentStatus in the given context.
        """
        return self.requestEmissionRelatedDtcClassPermanentStatusRef

    def setRequestEmissionRelatedDtcClassPermanentStatusRef(self, value: Optional[RefType]) -> DiagnosticRequestEmissionRelatedDTCPermanentStatus:
        """
        This reference substantiates that abstract reference in the role serviceClass for this specific concrete class. Thereby, the reference represents the ability to access shared attributes among all DiagnosticRequestEmissionRelatedDTCPermanentStatus in the given context.

        A None value is a no-op and does not overwrite an existing requestEmissionRelatedDtcClassPermanentStatusRef.
        """
        if value is not None:
            self.requestEmissionRelatedDtcClassPermanentStatusRef = value
        return self


class DiagnosticRequestFileTransfer(ARElement):
    """This diagnostic service instance implements the UDS service 0x38. Tags: atp.recommendedPackage=DiagnosticRequestFileTransfers"""

    # DiagnosticRequestFileTransfer method parity checklist:
    # Spec: AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf, Table 4.125, p.147
    # Columns: impl / docstring / test / reader / writer / release   ([—] = no XML element)
    # [x] __init__                          [x] impl  [x] docstring  [x] test  [—] reader  [—] writer  R23-11
    # [x] getRequestFileTransferClassRef    [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setRequestFileTransferClassRef    [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11

    def __init__(self, parent: ARObject, short_name: str):
        super().__init__(parent, short_name)

        # This reference substantiates that abstract reference in the role serviceClass for this specific concrete class. Thereby, the reference represents the ability to access shared attributes among all DiagnosticRequestFileTransfer in the given context.
        self.requestFileTransferClassRef: Optional[RefType] = None

    def getRequestFileTransferClassRef(self) -> Optional[RefType]:
        """
        This reference substantiates that abstract reference in the role serviceClass for this specific concrete class. Thereby, the reference represents the ability to access shared attributes among all DiagnosticRequestFileTransfer in the given context.
        """
        return self.requestFileTransferClassRef

    def setRequestFileTransferClassRef(self, value: Optional[RefType]) -> DiagnosticRequestFileTransfer:
        """
        This reference substantiates that abstract reference in the role serviceClass for this specific concrete class. Thereby, the reference represents the ability to access shared attributes among all DiagnosticRequestFileTransfer in the given context.

        A None value is a no-op and does not overwrite an existing requestFileTransferClassRef.
        """
        if value is not None:
            self.requestFileTransferClassRef = value
        return self


class DiagnosticRequestOnBoardMonitoringTestResults(DiagnosticServiceInstance):
    """This meta-class represents the ability to model an instance of the OBD mode 0x06 service. Tags: atp.recommendedPackage=DiagnosticRequestOnBoardMonitoringTestResultss"""

    # DiagnosticRequestOnBoardMonitoringTestResults method parity checklist:
    # Spec: AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf, Table 4.139, p.156
    # Columns: impl / docstring / test / reader / writer / release   ([—] = no XML element)
    # [x] __init__                                               [x] impl  [x] docstring  [x] test  [—] reader  [—] writer  R23-11
    # [x] getDiagnosticTestResultRefs                            [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] addDiagnosticTestResultRef                             [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getRequestOnBoardMonitoringTestResultsClassRef         [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setRequestOnBoardMonitoringTestResultsClassRef         [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11

    def __init__(self, parent: ARObject, short_name: str):
        super().__init__(parent, short_name)

        # This reference identifies the applicable collection of test identifiers for setting up a request message for mode 0x06.
        self.diagnosticTestResultRefs: List[RefType] = []

        # This reference substantiates that abstract reference in the role serviceClass for this specific concrete class. Thereby, the reference represents the ability to access shared attributes among all DiagnosticRequestOnBoardMonitoringTestResults in the given context.
        self.requestOnBoardMonitoringTestResultsClassRef: Optional[RefType] = None

    def getDiagnosticTestResultRefs(self) -> List[RefType]:
        """
        This reference identifies the applicable collection of test identifiers for setting up a request message for mode 0x06.
        """
        return self.diagnosticTestResultRefs

    def addDiagnosticTestResultRef(self, value: Optional[RefType]) -> DiagnosticRequestOnBoardMonitoringTestResults:
        """
        This reference identifies the applicable collection of test identifiers for setting up a request message for mode 0x06.

        A None value is a no-op and does not append a diagnosticTestResultRef.
        """
        if value is not None:
            self.diagnosticTestResultRefs.append(value)
        return self

    def getRequestOnBoardMonitoringTestResultsClassRef(self) -> Optional[RefType]:
        """
        This reference substantiates that abstract reference in the role serviceClass for this specific concrete class. Thereby, the reference represents the ability to access shared attributes among all DiagnosticRequestOnBoardMonitoringTestResults in the given context.
        """
        return self.requestOnBoardMonitoringTestResultsClassRef

    def setRequestOnBoardMonitoringTestResultsClassRef(self, value: Optional[RefType]) -> DiagnosticRequestOnBoardMonitoringTestResults:
        """
        This reference substantiates that abstract reference in the role serviceClass for this specific concrete class. Thereby, the reference represents the ability to access shared attributes among all DiagnosticRequestOnBoardMonitoringTestResults in the given context.

        A None value is a no-op and does not overwrite an existing requestOnBoardMonitoringTestResultsClassRef.
        """
        if value is not None:
            self.requestOnBoardMonitoringTestResultsClassRef = value
        return self


class DiagnosticRequestPowertrainFreezeFrameData(DiagnosticServiceInstance):
    """This meta-class represents the ability to model an instance of the OBD mode 0x02 service. Tags: atp.recommendedPackage=DiagnosticPowertrainFreezeFrames"""

    # DiagnosticRequestPowertrainFreezeFrameData method parity checklist:
    # Spec: AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf, Table 4.132, p.152
    # Columns: impl / docstring / test / reader / writer / release   ([—] = no XML element)
    # [x] __init__                                             [x] impl  [x] docstring  [x] test  [—] reader  [—] writer  R23-11
    # [x] getFreezeFrameRef                                    [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setFreezeFrameRef                                    [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getRequestPowertrainFreezeFrameDataRef               [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setRequestPowertrainFreezeFrameDataRef               [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11

    def __init__(self, parent: ARObject, short_name: str):
        super().__init__(parent, short_name)

        # This represents the associated freeze-frame.
        self.freezeFrameRef: Optional[RefType] = None

        # This reference substantiates that abstract reference in the role serviceClass for this specific concrete class. Thereby, the reference represents the ability to access shared attributes among all DiagnosticRequestPowertrainFreezeFrameData in the given context.
        self.requestPowertrainFreezeFrameDataRef: Optional[RefType] = None

    def getFreezeFrameRef(self) -> Optional[RefType]:
        """
        This represents the associated freeze-frame.
        """
        return self.freezeFrameRef

    def setFreezeFrameRef(self, value: Optional[RefType]) -> DiagnosticRequestPowertrainFreezeFrameData:
        """
        This represents the associated freeze-frame.

        A None value is a no-op and does not overwrite an existing freezeFrameRef.
        """
        if value is not None:
            self.freezeFrameRef = value
        return self

    def getRequestPowertrainFreezeFrameDataRef(self) -> Optional[RefType]:
        """
        This reference substantiates that abstract reference in the role serviceClass for this specific concrete class. Thereby, the reference represents the ability to access shared attributes among all DiagnosticRequestPowertrainFreezeFrameData in the given context.
        """
        return self.requestPowertrainFreezeFrameDataRef

    def setRequestPowertrainFreezeFrameDataRef(self, value: Optional[RefType]) -> DiagnosticRequestPowertrainFreezeFrameData:
        """
        This reference substantiates that abstract reference in the role serviceClass for this specific concrete class. Thereby, the reference represents the ability to access shared attributes among all DiagnosticRequestPowertrainFreezeFrameData in the given context.

        A None value is a no-op and does not overwrite an existing requestPowertrainFreezeFrameDataRef.
        """
        if value is not None:
            self.requestPowertrainFreezeFrameDataRef = value
        return self


class DiagnosticRequestUpload(DiagnosticMemoryAddressableRangeAccess):
    """This represents an instance of the "Request Upload" diagnostic service. Tags: atp.recommendedPackage=DiagnosticMemoryByAdresss"""

    # DiagnosticRequestUpload method parity checklist:
    # Spec: AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf, Table 4.123, p.145
    # Columns: impl / docstring / test / reader / writer / release   ([—] = no XML element)
    # [x] __init__                  [x] impl  [x] docstring  [x] test  [—] reader  [—] writer  R23-11
    # [x] getRequestUploadClassRef  [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setRequestUploadClassRef  [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11

    def __init__(self, parent: ARObject, short_name: str):
        super().__init__(parent, short_name)

        # This reference substantiates that abstract reference in the role serviceClass for this specific concrete class. Thereby, the reference represents the ability to access shared attributes among all DiagnosticRequestUpload in the given context.
        self.requestUploadClassRef: Optional[RefType] = None

    def getRequestUploadClassRef(self) -> Optional[RefType]:
        """
        This reference substantiates that abstract reference in the role serviceClass for this specific concrete class. Thereby, the reference represents the ability to access shared attributes among all DiagnosticRequestUpload in the given context.
        """
        return self.requestUploadClassRef

    def setRequestUploadClassRef(self, value: Optional[RefType]) -> DiagnosticRequestUpload:
        """
        This reference substantiates that abstract reference in the role serviceClass for this specific concrete class. Thereby, the reference represents the ability to access shared attributes among all DiagnosticRequestUpload in the given context.

        A None value is a no-op and does not overwrite an existing requestUploadClassRef.
        """
        if value is not None:
            self.requestUploadClassRef = value
        return self


class DiagnosticRequestVehicleInfo(DiagnosticServiceInstance):
    """This meta-class represents the ability to model an instance of the OBD mode 0x09 service. Tags: atp.recommendedPackage=DiagnosticRequestVehicleInfos"""

    # DiagnosticRequestVehicleInfo method parity checklist:
    # Spec: AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf, Table 4.144, p.160
    # Columns: impl / docstring / test / reader / writer / release   ([—] = no XML element)
    # [x] __init__                                      [x] impl  [x] docstring  [x] test  [—] reader  [—] writer  R23-11
    # [x] getInfoTypeRef                                [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setInfoTypeRef                                [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getRequestVehicleInformationClassRef          [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setRequestVehicleInformationClassRef          [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11

    def __init__(self, parent: ARObject, short_name: str):
        super().__init__(parent, short_name)

        # This represents the info type associated with the mode 0x09 service.
        self.infoTypeRef: Optional[RefType] = None

        # This reference substantiates that abstract reference in the role serviceClass for this specific concrete class. Thereby, the reference represents the ability to access shared attributes among all DiagnosticRequesVehicleInfo in the given context.
        self.requestVehicleInformationClassRef: Optional[RefType] = None

    def getInfoTypeRef(self) -> Optional[RefType]:
        """
        This represents the info type associated with the mode 0x09 service.
        """
        return self.infoTypeRef

    def setInfoTypeRef(self, value: Optional[RefType]) -> DiagnosticRequestVehicleInfo:
        """
        This represents the info type associated with the mode 0x09 service.

        A None value is a no-op and does not overwrite an existing infoTypeRef.
        """
        if value is not None:
            self.infoTypeRef = value
        return self

    def getRequestVehicleInformationClassRef(self) -> Optional[RefType]:
        """
        This reference substantiates that abstract reference in the role serviceClass for this specific concrete class. Thereby, the reference represents the ability to access shared attributes among all DiagnosticRequesVehicleInfo in the given context.
        """
        return self.requestVehicleInformationClassRef

    def setRequestVehicleInformationClassRef(self, value: Optional[RefType]) -> DiagnosticRequestVehicleInfo:
        """
        This reference substantiates that abstract reference in the role serviceClass for this specific concrete class. Thereby, the reference represents the ability to access shared attributes among all DiagnosticRequesVehicleInfo in the given context.

        A None value is a no-op and does not overwrite an existing requestVehicleInformationClassRef.
        """
        if value is not None:
            self.requestVehicleInformationClassRef = value
        return self


class DiagnosticResponseOnEvent(ARElement):
    """This represents an instance of the "Response on Event" diagnostic service."""

    # DiagnosticResponseOnEvent method parity checklist:
    # Spec: AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf, Table 4.101, p.132
    # Columns: impl / docstring / test / reader / writer / release   ([—] = no XML element)
    # [x] __init__                   [x] impl  [x] docstring  [x] test  [—] reader  [—] writer  R23-11
    # [x] addEventWindow             [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getEventWindows            [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] getResponseOnEventAction   [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setResponseOnEventAction   [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getResponseOnEventClass    [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setResponseOnEventClass    [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11

    def __init__(self, parent: ARObject, short_name: str):
        super().__init__(parent, short_name)

        # This represents the applicable DiagnosticEventWindows
        self.eventWindow: List[DiagnosticEventWindow] = []

        # Defines sub-functions of the service ResponseOnEvent.
        self.responseOnEventAction: Optional[DiagnosticResponseOnEventActionEnum] = None

        # This reference substantiates that abstract reference in the role serviceClass for this specific concrete class. Thereby, the reference represents the ability to access shared attributes among all DiagnosticResponseOnEvent in the given context.
        self.responseOnEventClass: Optional[RefType] = None

    def addEventWindow(self, value: Optional[DiagnosticEventWindow]) -> DiagnosticResponseOnEvent:
        """
        This represents the applicable DiagnosticEventWindows

        A None value is a no-op and does not append an eventWindow.
        """
        if value is not None:
            self.eventWindow.append(value)
        return self

    def getEventWindows(self) -> List[DiagnosticEventWindow]:
        """
        This represents the applicable DiagnosticEventWindows
        """
        return self.eventWindow

    def getResponseOnEventAction(self) -> Optional[DiagnosticResponseOnEventActionEnum]:
        """
        Defines sub-functions of the service ResponseOnEvent.
        """
        return self.responseOnEventAction

    def setResponseOnEventAction(self, value: Optional[DiagnosticResponseOnEventActionEnum]) -> DiagnosticResponseOnEvent:
        """
        Defines sub-functions of the service ResponseOnEvent.

        A None value is a no-op and does not overwrite an existing responseOnEventAction.
        """
        if value is not None:
            self.responseOnEventAction = value
        return self

    def getResponseOnEventClass(self) -> Optional[RefType]:
        """
        This reference substantiates that abstract reference in the role serviceClass for this specific concrete class. Thereby, the reference represents the ability to access shared attributes among all DiagnosticResponseOnEvent in the given context.
        """
        return self.responseOnEventClass

    def setResponseOnEventClass(self, value: Optional[RefType]) -> DiagnosticResponseOnEvent:
        """
        This reference substantiates that abstract reference in the role serviceClass for this specific concrete class. Thereby, the reference represents the ability to access shared attributes among all DiagnosticResponseOnEvent in the given context.

        A None value is a no-op and does not overwrite an existing responseOnEventClass.
        """
        if value is not None:
            self.responseOnEventClass = value
        return self


class DiagnosticRoutine(ARElement):
    """This meta-class represents the ability to define a diagnostic routine."""

    # DiagnosticRoutine method parity checklist:
    # Spec: AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf, Table 4.85, p.124
    # Columns: impl / docstring / test / reader / writer / release   ([—] = no XML element)
    # [x] __init__              [x] impl  [x] docstring  [x] test  [—] reader  [—] writer  R23-11
    # [x] getId                 [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setId                 [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] createRequestResult   [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getRequestResult      [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] getRoutineInfo        [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setRoutineInfo        [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] createStart           [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getStart              [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] createStop            [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getStop               [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11

    def __init__(self, parent: ARObject, short_name: str):
        super().__init__(parent, short_name)

        # This is the numerical identifier used to identify the DiagnosticRoutine in the scope of diagnostic workflow
        self.id: Optional[PositiveInteger] = None

        # This represents the ability to request the result of a running routine.
        self.requestResult: Optional[DiagnosticRequestRoutineResults] = None

        # This represents the routine info byte. The info byte contains a manufacturer-specific value (for the identification of record identifiers) that is reported to the tester. Other use cases for this attribute are mentioned in ISO 27145 and ISO 26021.
        self.routineInfo: Optional[PositiveInteger] = None

        # This represents the ability to start a routine
        self.start: Optional[DiagnosticStartRoutine] = None

        # This represents the ability to stop a running routine.
        self.stop: Optional[DiagnosticStopRoutine] = None

    def getId(self) -> Optional[PositiveInteger]:
        """
        This is the numerical identifier used to identify the DiagnosticRoutine in the scope of diagnostic workflow
        """
        return self.id

    def setId(self, value: Optional[PositiveInteger]) -> DiagnosticRoutine:
        """
        This is the numerical identifier used to identify the DiagnosticRoutine in the scope of diagnostic workflow

        A None value is a no-op and does not overwrite an existing id.
        """
        if value is not None:
            self.id = value
        return self

    def createRequestResult(self, short_name: str) -> DiagnosticRequestRoutineResults:
        """
        This represents the ability to request the result of a running routine.

        The existing requestResult is returned when the short name already exists (no duplicate creation).
        """
        if self.requestResult is None or self.requestResult.getShortName() != short_name:
            self.requestResult = DiagnosticRequestRoutineResults(self, short_name)
        return self.requestResult

    def getRequestResult(self) -> Optional[DiagnosticRequestRoutineResults]:
        """
        This represents the ability to request the result of a running routine.
        """
        return self.requestResult

    def getRoutineInfo(self) -> Optional[PositiveInteger]:
        """
        This represents the routine info byte. The info byte contains a manufacturer-specific value (for the identification of record identifiers) that is reported to the tester. Other use cases for this attribute are mentioned in ISO 27145 and ISO 26021.
        """
        return self.routineInfo

    def setRoutineInfo(self, value: Optional[PositiveInteger]) -> DiagnosticRoutine:
        """
        This represents the routine info byte. The info byte contains a manufacturer-specific value (for the identification of record identifiers) that is reported to the tester. Other use cases for this attribute are mentioned in ISO 27145 and ISO 26021.

        A None value is a no-op and does not overwrite an existing routineInfo.
        """
        if value is not None:
            self.routineInfo = value
        return self

    def createStart(self, short_name: str) -> DiagnosticStartRoutine:
        """
        This represents the ability to start a routine

        The existing start is returned when the short name already exists (no duplicate creation).
        """
        if self.start is None or self.start.getShortName() != short_name:
            self.start = DiagnosticStartRoutine(self, short_name)
        return self.start

    def getStart(self) -> Optional[DiagnosticStartRoutine]:
        """
        This represents the ability to start a routine
        """
        return self.start

    def createStop(self, short_name: str) -> DiagnosticStopRoutine:
        """
        This represents the ability to stop a running routine.

        The existing stop is returned when the short name already exists (no duplicate creation).
        """
        if self.stop is None or self.stop.getShortName() != short_name:
            self.stop = DiagnosticStopRoutine(self, short_name)
        return self.stop

    def getStop(self) -> Optional[DiagnosticStopRoutine]:
        """
        This represents the ability to stop a running routine.
        """
        return self.stop


class DiagnosticRoutineControl(ARElement):
    """This represents an instance of the "Routine Control" diagnostic service."""

    # DiagnosticRoutineControl method parity checklist:
    # Spec: AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf, Table 4.89, p.125
    # Columns: impl / docstring / test / reader / writer / release   ([—] = no XML element)
    # [x] __init__                [x] impl  [x] docstring  [x] test  [—] reader  [—] writer  R23-11
    # [x] getRoutine              [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setRoutine              [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getRoutineControlClass  [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setRoutineControlClass  [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11

    def __init__(self, parent: ARObject, short_name: str):
        super().__init__(parent, short_name)

        # This refers to the applicable DiagnosticRoutine.
        self.routine: Optional[RefType] = None

        # This reference substantiates that abstract reference in the role serviceClass for this specific concrete class. Thereby, the reference represents the ability to access shared attributes among all DiagnosticRoutineControl in the given context.
        self.routineControlClass: Optional[RefType] = None

    def getRoutine(self) -> Optional[RefType]:
        """
        This refers to the applicable DiagnosticRoutine.
        """
        return self.routine

    def setRoutine(self, value: Optional[RefType]) -> DiagnosticRoutineControl:
        """
        This refers to the applicable DiagnosticRoutine.

        A None value is a no-op and does not overwrite an existing routine.
        """
        if value is not None:
            self.routine = value
        return self

    def getRoutineControlClass(self) -> Optional[RefType]:
        """
        This reference substantiates that abstract reference in the role serviceClass for this specific concrete class. Thereby, the reference represents the ability to access shared attributes among all DiagnosticRoutineControl in the given context.
        """
        return self.routineControlClass

    def setRoutineControlClass(self, value: Optional[RefType]) -> DiagnosticRoutineControl:
        """
        This reference substantiates that abstract reference in the role serviceClass for this specific concrete class. Thereby, the reference represents the ability to access shared attributes among all DiagnosticRoutineControl in the given context.

        A None value is a no-op and does not overwrite an existing routineControlClass.
        """
        if value is not None:
            self.routineControlClass = value
        return self


class DiagnosticSecurityAccess(ARElement):
    """This represents an instance of the "Security Access" diagnostic service."""

    # DiagnosticSecurityAccess method parity checklist:
    # Spec: AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf, Table 4.49, p.96
    # Columns: impl / docstring / test / reader / writer / release   ([—] = no XML element)
    # [x] __init__                      [x] impl  [x] docstring  [x] test  [—] reader  [—] writer  R23-11
    # [x] getRequestSeedId              [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setRequestSeedId              [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getSecurityAccessClass        [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setSecurityAccessClass        [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getSecurityDelayTimeOnBoot    [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setSecurityDelayTimeOnBoot    [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getSecurityLevel              [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setSecurityLevel              [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11

    def __init__(self, parent: ARObject, short_name: str):
        super().__init__(parent, short_name)

        # This would be 0x01, 0x03, 0x05, ... The sendKey id can be computed by adding 1 to the requestSeedId
        self.requestSeedId: Optional[PositiveInteger] = None

        # This reference substantiates that abstract reference in the role serviceClass for this specific concrete class. Thereby, the reference represents the ability to access shared attributes among all DiagnosticSecurityAccess in the given context.
        self.securityAccessClass: Optional[RefType] = None

        # Start delay timer on power on in seconds. This delay indicates the time after ECU boot power-on where no security access request is accepted.
        self.securityDelayTimeOnBoot: Optional[TimeValue] = None

        # This reference identifies the applicable security level for the security access. Stereotypes: atpSplitable Tags: atp.Splitkey=securityLevel
        self.securityLevel: Optional[RefType] = None

    def getRequestSeedId(self) -> Optional[PositiveInteger]:
        """
        This would be 0x01, 0x03, 0x05, ... The sendKey id can be computed by adding 1 to the requestSeedId
        """
        return self.requestSeedId

    def setRequestSeedId(self, value: Optional[PositiveInteger]):
        """
        This would be 0x01, 0x03, 0x05, ... The sendKey id can be computed by adding 1 to the requestSeedId

        A None value is a no-op and does not overwrite an existing requestSeedId.
        """
        if value is not None:
            self.requestSeedId = value
        return self

    def getSecurityAccessClass(self) -> Optional[RefType]:
        """
        This reference substantiates that abstract reference in the role serviceClass for this specific concrete class. Thereby, the reference represents the ability to access shared attributes among all DiagnosticSecurityAccess in the given context.
        """
        return self.securityAccessClass

    def setSecurityAccessClass(self, value: Optional[RefType]):
        """
        This reference substantiates that abstract reference in the role serviceClass for this specific concrete class. Thereby, the reference represents the ability to access shared attributes among all DiagnosticSecurityAccess in the given context.

        A None value is a no-op and does not overwrite an existing securityAccessClass.
        """
        if value is not None:
            self.securityAccessClass = value
        return self

    def getSecurityDelayTimeOnBoot(self) -> Optional[TimeValue]:
        """
        Start delay timer on power on in seconds. This delay indicates the time after ECU boot power-on where no security access request is accepted.
        """
        return self.securityDelayTimeOnBoot

    def setSecurityDelayTimeOnBoot(self, value: Optional[TimeValue]):
        """
        Start delay timer on power on in seconds. This delay indicates the time after ECU boot power-on where no security access request is accepted.

        A None value is a no-op and does not overwrite an existing securityDelayTimeOnBoot.
        """
        if value is not None:
            self.securityDelayTimeOnBoot = value
        return self

    def getSecurityLevel(self) -> Optional[RefType]:
        """
        This reference identifies the applicable security level for the security access. Stereotypes: atpSplitable Tags: atp.Splitkey=securityLevel
        """
        return self.securityLevel

    def setSecurityLevel(self, value: Optional[RefType]):
        """
        This reference identifies the applicable security level for the security access. Stereotypes: atpSplitable Tags: atp.Splitkey=securityLevel

        A None value is a no-op and does not overwrite an existing securityLevel.
        """
        if value is not None:
            self.securityLevel = value
        return self


class DiagnosticSecurityEventReportingModeMapping(DiagnosticMapping):
    """This meta-class represents the ability to associate a location in a DID with a security event. The purpose of this mapping is that the location in the DID contains the setting of the reporting mode for the specific security event. This means that the reporting mode of the security event can be set via the diagnostic service WriteDataByIdentifier. Tags: atp.Status=candidate atp.recommendedPackage=DiagnosticMappings"""

    # DiagnosticSecurityEventReportingModeMapping method parity checklist:
    # Spec: AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf, Table 5.18, p.243
    # Columns: impl / docstring / test / reader / writer / release   ([—] = no XML element)
    # [x] __init__                           [x] impl  [x] docstring  [x] test  [—] reader  [—] writer  R23-11
    # [x] getDataElementRef                     [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setDataElementRef                     [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getSecurityEventRef                   [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setSecurityEventRef                   [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11

    def __init__(self, parent: ARObject, short_name: str):
        super().__init__(parent, short_name)

        # This reference identifies the data element that carries the information about the reporting mode. Tags: atp.Status=candidate
        self.dataElementRef: Optional[RefType] = None

        # This reference identifies the mapped security event. Tags: atp.Status=candidate
        self.securityEventRef: Optional[RefType] = None

    def getDataElementRef(self) -> Optional[RefType]:
        """
        This reference identifies the data element that carries the information about the reporting mode. Tags: atp.Status=candidate
        """
        return self.dataElementRef

    def setDataElementRef(self, value: Optional[RefType]) -> DiagnosticSecurityEventReportingModeMapping:
        """
        This reference identifies the data element that carries the information about the reporting mode. Tags: atp.Status=candidate
        A None value is a no-op and does not overwrite an existing dataElementRef.
        """
        if value is not None:
            self.dataElementRef = value
        return self

    def getSecurityEventRef(self) -> Optional[RefType]:
        """
        This reference identifies the mapped security event. Tags: atp.Status=candidate
        """
        return self.securityEventRef

    def setSecurityEventRef(self, value: Optional[RefType]) -> DiagnosticSecurityEventReportingModeMapping:
        """
        This reference identifies the mapped security event. Tags: atp.Status=candidate
        A None value is a no-op and does not overwrite an existing securityEventRef.
        """
        if value is not None:
            self.securityEventRef = value
        return self


class DiagnosticParameterElementAccess(ARObject):
    """This meta-class acts as a single point for defining structured references to a specific DiagnosticParameterElement."""

    # DiagnosticParameterElementAccess method parity checklist:
    # Spec: AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf, Table 5.5, p.229
    # Columns: impl / docstring / test / reader / writer / release   ([—] = no XML element)
    # [x] __init__              [x] impl  [x] docstring  [x] test  [—] reader  [—] writer  R23-11
    # [x] addContextElementRef  [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getContextElementRefs [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] getTargetElementRef   [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setTargetElementRef   [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11

    def __init__(self):
        super().__init__()

        # This represents the context of an applicable payload that corresponds to the referenced DataPrototype in the role mappedDataElement. Tags: xml.sequenceOffset=10
        self.contextElementRefs: List[RefType] = []

        # This represents the target reference of an applicable payload that corresponds to the referenced DataPrototype in the role mappedDataElement. Tags: xml.sequenceOffset=20
        self.targetElementRef: Optional[RefType] = None

    def addContextElementRef(self, value: Optional[RefType]) -> DiagnosticParameterElementAccess:
        """
        This represents the context of an applicable payload that corresponds to the referenced DataPrototype in the role mappedDataElement. Tags: xml.sequenceOffset=10
        A None value is a no-op and does not append a contextElementRef.
        """
        if value is not None:
            self.contextElementRefs.append(value)
        return self

    def getContextElementRefs(self) -> List[RefType]:
        """
        This represents the context of an applicable payload that corresponds to the referenced DataPrototype in the role mappedDataElement. Tags: xml.sequenceOffset=10
        """
        return self.contextElementRefs

    def getTargetElementRef(self) -> Optional[RefType]:
        """
        This represents the target reference of an applicable payload that corresponds to the referenced DataPrototype in the role mappedDataElement. Tags: xml.sequenceOffset=20
        """
        return self.targetElementRef

    def setTargetElementRef(self, value: Optional[RefType]) -> DiagnosticParameterElementAccess:
        """
        This represents the target reference of an applicable payload that corresponds to the referenced DataPrototype in the role mappedDataElement. Tags: xml.sequenceOffset=20
        A None value is a no-op and does not overwrite an existing targetElementRef.
        """
        if value is not None:
            self.targetElementRef = value
        return self


class DiagnosticServiceDataMapping(DiagnosticSwMapping):
    """This represents the ability to define a mapping of a diagnostic service to a software-component. This kind of service mapping is applicable for the usage of SenderReceiverInterfaces or event/notifier semantics in ServiceInterfaces on the adaptive platform. Tags: atp.recommendedPackage=DiagnosticServiceMappings"""

    # DiagnosticServiceDataMapping method parity checklist:
    # Spec: AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf, Table 5.4, p.228
    # Columns: impl / docstring / test / reader / writer / release   ([—] = no XML element)
    # [x] __init__                        [x] impl  [x] docstring  [x] test  [—] reader  [—] writer  R23-11
    # [x] getDiagnosticDataElementRef     [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setDiagnosticDataElementRef     [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getDiagnosticParameterRef       [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setDiagnosticParameterRef       [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getMappedDataElementIRef        [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setMappedDataElementIRef        [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getParameterElementAccess       [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setParameterElementAccess       [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11

    def __init__(self, parent: ARObject, short_name: str):
        super().__init__(parent, short_name)

        # This represents the applicable payload that corresponds to the referenced DataPrototype in the role mappedDataElement or (in case of a usage on the adaptive platform) mappedApDataElement.
        self.diagnosticDataElementRef: Optional[RefType] = None

        # This represents the applicable payload that corresponds to the referenced DataPrototype in the role mappedDataElement. Tags: xml.sequenceOffset=20
        self.diagnosticParameterRef: Optional[RefType] = None

        # This represents the dataElement in the application software that is accessed for diagnostic purpose. This role is applicable on the classic platform. InstanceRef implemented by: DataPrototypeInSystemInstanceRef
        self.mappedDataElementIRef: Optional[RefType] = None

        # This aggregation represents the single point of access to the reference to one specific DiagnosticParameterElement.
        self.parameterElementAccess: Optional[DiagnosticParameterElementAccess] = None

    def getDiagnosticDataElementRef(self) -> Optional[RefType]:
        """
        This represents the applicable payload that corresponds to the referenced DataPrototype in the role mappedDataElement or (in case of a usage on the adaptive platform) mappedApDataElement.
        """
        return self.diagnosticDataElementRef

    def setDiagnosticDataElementRef(self, value: Optional[RefType]) -> DiagnosticServiceDataMapping:
        """
        This represents the applicable payload that corresponds to the referenced DataPrototype in the role mappedDataElement or (in case of a usage on the adaptive platform) mappedApDataElement.
        A None value is a no-op and does not overwrite an existing diagnosticDataElementRef.
        """
        if value is not None:
            self.diagnosticDataElementRef = value
        return self

    def getDiagnosticParameterRef(self) -> Optional[RefType]:
        """
        This represents the applicable payload that corresponds to the referenced DataPrototype in the role mappedDataElement. Tags: xml.sequenceOffset=20
        """
        return self.diagnosticParameterRef

    def setDiagnosticParameterRef(self, value: Optional[RefType]) -> DiagnosticServiceDataMapping:
        """
        This represents the applicable payload that corresponds to the referenced DataPrototype in the role mappedDataElement. Tags: xml.sequenceOffset=20
        A None value is a no-op and does not overwrite an existing diagnosticParameterRef.
        """
        if value is not None:
            self.diagnosticParameterRef = value
        return self

    def getMappedDataElementIRef(self) -> Optional[RefType]:
        """
        This represents the dataElement in the application software that is accessed for diagnostic purpose. This role is applicable on the classic platform. InstanceRef implemented by: DataPrototypeInSystemInstanceRef
        """
        return self.mappedDataElementIRef

    def setMappedDataElementIRef(self, value: Optional[RefType]) -> DiagnosticServiceDataMapping:
        """
        This represents the dataElement in the application software that is accessed for diagnostic purpose. This role is applicable on the classic platform. InstanceRef implemented by: DataPrototypeInSystemInstanceRef
        A None value is a no-op and does not overwrite an existing mappedDataElementIRef.
        """
        if value is not None:
            self.mappedDataElementIRef = value
        return self

    def getParameterElementAccess(self) -> Optional[DiagnosticParameterElementAccess]:
        """
        This aggregation represents the single point of access to the reference to one specific DiagnosticParameterElement.
        """
        return self.parameterElementAccess

    def setParameterElementAccess(self, value: Optional[DiagnosticParameterElementAccess]) -> DiagnosticServiceDataMapping:
        """
        This aggregation represents the single point of access to the reference to one specific DiagnosticParameterElement.
        A None value is a no-op and does not overwrite an existing parameterElementAccess.
        """
        if value is not None:
            self.parameterElementAccess = value
        return self


class DiagnosticServiceMappingDiagTarget(ARObject):
    """This meta-class serves as a base class for diagnostics-related targets of subclasses of DiagnosticSwMapping."""

    # DiagnosticServiceMappingDiagTarget method parity checklist:
    # Spec: AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf, Table 5.12, p.234
    # Columns: impl / docstring / test / reader / writer / release   ([—] = no XML element)
    # [x] __init__     [x] impl  [x] docstring  [x] test  [—] reader  [—] writer  R23-11

    def __init__(self):
        if type(self) is DiagnosticServiceMappingDiagTarget:
            raise TypeError("DiagnosticServiceMappingDiagTarget is an abstract class.")

        super().__init__()


class DiagnosticServiceSwMapping(DiagnosticSwMapping):
    """This represents the ability to define a mapping of a diagnostic service to a software-component or a basic-software module. If the former is used then this kind of service mapping is applicable for the usage of ClientServerInterfaces. Tags: atp.recommendedPackage=DiagnosticServiceMappings"""

    # DiagnosticServiceSwMapping method parity checklist:
    # Spec: AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf, Table 5.15, p.239
    # Columns: impl / docstring / test / reader / writer / release   ([—] = no XML element)
    # [x] __init__                              [x] impl  [x] docstring  [x] test  [—] reader  [—] writer  R23-11
    # [x] getAccessedDataPrototypeIRef          [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setAccessedDataPrototypeIRef          [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getDiagnosticDataElementRef           [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setDiagnosticDataElementRef           [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getDiagnosticParameterRef             [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setDiagnosticParameterRef             [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getMappedBswServiceDependencyRef      [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setMappedBswServiceDependencyRef      [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getMappedFlatSwcServiceDependencyRef  [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setMappedFlatSwcServiceDependencyRef  [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getMappedSwcServiceDependencyInSystemIRef [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setMappedSwcServiceDependencyInSystemIRef [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getParameterElementAccess             [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setParameterElementAccess             [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getServiceInstanceRef                 [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setServiceInstanceRef                 [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11

    def __init__(self, parent: ARObject, short_name: str):
        super().__init__(parent, short_name)

        # Thi instanceRef identifies the DataPrototype that is supposed to be accessed in the context of the operation argument. InstanceRef implemented by: DataPrototypeInClientServerInterfaceInstanceRef
        self.accessedDataPrototypeIRef: Optional[RefType] = None

        # This represents a DiagnosticDataElement required to execute the respective diagnostic service in the context of the diagnostic service mapping,
        self.diagnosticDataElementRef: Optional[RefType] = None

        # This represents the applicable payload that corresponds to the referenced DataPrototype in the role mappedDataElement.
        self.diagnosticParameterRef: Optional[RefType] = None

        # This is supposed to represent a reference to a BswServiceDependency. the latter is not derived from Referrable and therefore this detour needs to be implemented to still let BswServiceDependency become the target of a reference.
        self.mappedBswServiceDependencyRef: Optional[RefType] = None

        # This represents the ability to refer to an AtomicSwComponentType that is available without the definition of how it will be embedded into the component hierarchy.
        self.mappedFlatSwcServiceDependencyRef: Optional[RefType] = None

        # This represents the ability to point into the component hierarchy (under possible consideration of the rootSoftwareComposition) InstanceRef implemented by: SwcServiceDependencyInSystemInstanceRef
        self.mappedSwcServiceDependencyInSystemIRef: Optional[RefType] = None

        # This aggregation represents the single point of access to the reference to one specific DiagnosticParameterElement.
        self.parameterElementAccess: Optional[DiagnosticParameterElementAccess] = None

        # This represents the service instance that needs to be considered in this diagnostics service mapping.
        self.serviceInstanceRef: Optional[RefType] = None

    def getAccessedDataPrototypeIRef(self) -> Optional[RefType]:
        """
        Thi instanceRef identifies the DataPrototype that is supposed to be accessed in the context of the operation argument. InstanceRef implemented by: DataPrototypeInClientServerInterfaceInstanceRef
        """
        return self.accessedDataPrototypeIRef

    def setAccessedDataPrototypeIRef(self, value: Optional[RefType]) -> DiagnosticServiceSwMapping:
        """
        Thi instanceRef identifies the DataPrototype that is supposed to be accessed in the context of the operation argument. InstanceRef implemented by: DataPrototypeInClientServerInterfaceInstanceRef
        A None value is a no-op and does not overwrite an existing accessedDataPrototypeIRef.
        """
        if value is not None:
            self.accessedDataPrototypeIRef = value
        return self

    def getDiagnosticDataElementRef(self) -> Optional[RefType]:
        """
        This represents a DiagnosticDataElement required to execute the respective diagnostic service in the context of the diagnostic service mapping,
        """
        return self.diagnosticDataElementRef

    def setDiagnosticDataElementRef(self, value: Optional[RefType]) -> DiagnosticServiceSwMapping:
        """
        This represents a DiagnosticDataElement required to execute the respective diagnostic service in the context of the diagnostic service mapping,
        A None value is a no-op and does not overwrite an existing diagnosticDataElementRef.
        """
        if value is not None:
            self.diagnosticDataElementRef = value
        return self

    def getDiagnosticParameterRef(self) -> Optional[RefType]:
        """
        This represents the applicable payload that corresponds to the referenced DataPrototype in the role mappedDataElement.
        """
        return self.diagnosticParameterRef

    def setDiagnosticParameterRef(self, value: Optional[RefType]) -> DiagnosticServiceSwMapping:
        """
        This represents the applicable payload that corresponds to the referenced DataPrototype in the role mappedDataElement.
        A None value is a no-op and does not overwrite an existing diagnosticParameterRef.
        """
        if value is not None:
            self.diagnosticParameterRef = value
        return self

    def getMappedBswServiceDependencyRef(self) -> Optional[RefType]:
        """
        This is supposed to represent a reference to a BswServiceDependency. the latter is not derived from Referrable and therefore this detour needs to be implemented to still let BswServiceDependency become the target of a reference.
        """
        return self.mappedBswServiceDependencyRef

    def setMappedBswServiceDependencyRef(self, value: Optional[RefType]) -> DiagnosticServiceSwMapping:
        """
        This is supposed to represent a reference to a BswServiceDependency. the latter is not derived from Referrable and therefore this detour needs to be implemented to still let BswServiceDependency become the target of a reference.
        A None value is a no-op and does not overwrite an existing mappedBswServiceDependencyRef.
        """
        if value is not None:
            self.mappedBswServiceDependencyRef = value
        return self

    def getMappedFlatSwcServiceDependencyRef(self) -> Optional[RefType]:
        """
        This represents the ability to refer to an AtomicSwComponentType that is available without the definition of how it will be embedded into the component hierarchy.
        """
        return self.mappedFlatSwcServiceDependencyRef

    def setMappedFlatSwcServiceDependencyRef(self, value: Optional[RefType]) -> DiagnosticServiceSwMapping:
        """
        This represents the ability to refer to an AtomicSwComponentType that is available without the definition of how it will be embedded into the component hierarchy.
        A None value is a no-op and does not overwrite an existing mappedFlatSwcServiceDependencyRef.
        """
        if value is not None:
            self.mappedFlatSwcServiceDependencyRef = value
        return self

    def getMappedSwcServiceDependencyInSystemIRef(self) -> Optional[RefType]:
        """
        This represents the ability to point into the component hierarchy (under possible consideration of the rootSoftwareComposition) InstanceRef implemented by: SwcServiceDependencyInSystemInstanceRef
        """
        return self.mappedSwcServiceDependencyInSystemIRef

    def setMappedSwcServiceDependencyInSystemIRef(self, value: Optional[RefType]) -> DiagnosticServiceSwMapping:
        """
        This represents the ability to point into the component hierarchy (under possible consideration of the rootSoftwareComposition) InstanceRef implemented by: SwcServiceDependencyInSystemInstanceRef
        A None value is a no-op and does not overwrite an existing mappedSwcServiceDependencyInSystemIRef.
        """
        if value is not None:
            self.mappedSwcServiceDependencyInSystemIRef = value
        return self

    def getParameterElementAccess(self) -> Optional[DiagnosticParameterElementAccess]:
        """
        This aggregation represents the single point of access to the reference to one specific DiagnosticParameterElement.
        """
        return self.parameterElementAccess

    def setParameterElementAccess(self, value: Optional[DiagnosticParameterElementAccess]) -> DiagnosticServiceSwMapping:
        """
        This aggregation represents the single point of access to the reference to one specific DiagnosticParameterElement.
        A None value is a no-op and does not overwrite an existing parameterElementAccess.
        """
        if value is not None:
            self.parameterElementAccess = value
        return self

    def getServiceInstanceRef(self) -> Optional[RefType]:
        """
        This represents the service instance that needs to be considered in this diagnostics service mapping.
        """
        return self.serviceInstanceRef

    def setServiceInstanceRef(self, value: Optional[RefType]) -> DiagnosticServiceSwMapping:
        """
        This represents the service instance that needs to be considered in this diagnostics service mapping.
        A None value is a no-op and does not overwrite an existing serviceInstanceRef.
        """
        if value is not None:
            self.serviceInstanceRef = value
        return self


class DiagnosticSessionControl(ARElement):
    """This represents an instance of the "Session Control" diagnostic service."""

    # DiagnosticSessionControl method parity checklist:
    # Spec: AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf, Table 4.47, p.93
    # Columns: impl / docstring / test / reader / writer / release   ([—] = no XML element)
    # [x] __init__                  [x] impl  [x] docstring  [x] test  [—] reader  [—] writer  R23-11
    # [x] getDiagnosticSessionRef   [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setDiagnosticSessionRef   [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getSessionControlClassRef [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setSessionControlClassRef [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11

    def __init__(self, parent: ARObject, short_name: str):
        super().__init__(parent, short_name)

        # This represents the applicable DiagnosticSessions
        self.diagnosticSessionRef: Optional[RefType] = None

        # This reference substantiates that abstract reference in the role serviceClass for this specific concrete class. Thereby, the reference represents the ability to access shared attributes among all DiagnosticSessionControl in the given context.
        self.sessionControlClassRef: Optional[RefType] = None

    def getDiagnosticSessionRef(self) -> Optional[RefType]:
        """
        This represents the applicable DiagnosticSessions
        """
        return self.diagnosticSessionRef

    def setDiagnosticSessionRef(self, value: Optional[RefType]):
        """
        This represents the applicable DiagnosticSessions

        A None value is a no-op and does not overwrite an existing diagnosticSessionRef.
        """
        if value is not None:
            self.diagnosticSessionRef = value
        return self

    def getSessionControlClassRef(self) -> Optional[RefType]:
        """
        This reference substantiates that abstract reference in the role serviceClass for this specific concrete class. Thereby, the reference represents the ability to access shared attributes among all DiagnosticSessionControl in the given context.
        """
        return self.sessionControlClassRef

    def setSessionControlClassRef(self, value: Optional[RefType]):
        """
        This reference substantiates that abstract reference in the role serviceClass for this specific concrete class. Thereby, the reference represents the ability to access shared attributes among all DiagnosticSessionControl in the given context.

        A None value is a no-op and does not overwrite an existing sessionControlClassRef.
        """
        if value is not None:
            self.sessionControlClassRef = value
        return self


class DiagnosticStorageCondition(DiagnosticCondition):
    """Specification of a storage condition. Tags: atp.recommendedPackage=DiagnosticConditions"""

    # DiagnosticStorageCondition method parity checklist:
    # Spec: AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf, Table 4.186, p.194
    # Columns: impl / docstring / test / reader / writer / release   ([—] = no XML element)
    # [x] __init__     [x] impl  [x] docstring  [x] test  [—] reader  [—] writer  R23-11

    def __init__(self, parent: ARObject, short_name: str):
        super().__init__(parent, short_name)


class DiagnosticStorageConditionGroup(DiagnosticConditionGroup):
    """
    Storage condition group which includes one or several storage conditions. Tags: atp.recommendedPackage=DiagnosticConditions

    [constr_1842] Existence of DiagnosticStorageConditionGroup.storageCondition: For each DiagnosticStorageConditionGroup, attribute storageCondition shall exist at the time when the DEXT is complete.
    """

    # DiagnosticStorageConditionGroup method parity checklist:
    # Spec: AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf, Table 4.195, p.200
    # Columns: impl / docstring / test / reader / writer / release   ([—] = no XML element)
    # [x] __init__                    [x] impl  [x] docstring  [x] test  [—] reader  [—] writer  R23-11
    # [x] addStorageConditionRef      [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getStorageConditionRefs     [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11

    def __init__(self, parent: ARObject, short_name: str):
        super().__init__(parent, short_name)

        # Reference to storageConditions that are part of the StorageConditionGroup.
        self.storageConditionRefs: List[RefType] = []

    def addStorageConditionRef(self, ref: Optional[RefType]) -> DiagnosticStorageConditionGroup:
        """
        Reference to storageConditions that are part of the StorageConditionGroup.

        A None value is a no-op and does not extend the storageConditionRefs list.
        """
        if ref is not None:
            self.storageConditionRefs.append(ref)
        return self

    def getStorageConditionRefs(self) -> List[RefType]:
        """
        Reference to storageConditions that are part of the StorageConditionGroup.
        """
        return self.storageConditionRefs


class DiagnosticStorageConditionPortMapping(DiagnosticSwMapping):
    """Defines to which SWC service ports with DiagnosticStorageConditionNeeds the DiagnosticStorageCondition is mapped. Tags: atp.recommendedPackage=DiagnosticMappings"""

    # DiagnosticStorageConditionPortMapping method parity checklist:
    # Spec: AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf, Table 5.27, p.253
    # Columns: impl / docstring / test / reader / writer / release   ([—] = no XML element)
    # [x] __init__                [x] impl  [x] docstring  [x] test  [—] reader  [—] writer  R23-11
    # [x] getDiagnosticStorageConditionRef             [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setDiagnosticStorageConditionRef             [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getSwcFlatServiceDependencyRef               [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setSwcFlatServiceDependencyRef               [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getSwcServiceDependencyInSystemIRef          [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setSwcServiceDependencyInSystemIRef          [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11

    def __init__(self, parent: ARObject, short_name: str):
        super().__init__(parent, short_name)

        # Reference to the StorageCondition which is mapped to a SWC service port with DiagnosticStorageConditionNeeds.
        self.diagnosticStorageConditionRef: Optional[RefType] = None

        # Reference to a SwcServiceDependencyType that links ServiceNeeds to SWC service ports.
        self.swcFlatServiceDependencyRef: Optional[RefType] = None

        # Instance reference to a SwcServiceDependency that links ServiceNeeds to SWC service ports. InstanceRef implemented by: SwcServiceDependencyInSystemInstanceRef
        self.swcServiceDependencyInSystemIRef: Optional[RefType] = None

    def getDiagnosticStorageConditionRef(self) -> Optional[RefType]:
        """
        Reference to the StorageCondition which is mapped to a SWC service port with DiagnosticStorageConditionNeeds.
        """
        return self.diagnosticStorageConditionRef

    def setDiagnosticStorageConditionRef(self, value: Optional[RefType]) -> DiagnosticStorageConditionPortMapping:
        """
        Reference to the StorageCondition which is mapped to a SWC service port with DiagnosticStorageConditionNeeds.
        A None value is a no-op and does not overwrite an existing diagnosticStorageConditionRef.
        """
        if value is not None:
            self.diagnosticStorageConditionRef = value
        return self

    def getSwcFlatServiceDependencyRef(self) -> Optional[RefType]:
        """
        Reference to a SwcServiceDependencyType that links ServiceNeeds to SWC service ports.
        """
        return self.swcFlatServiceDependencyRef

    def setSwcFlatServiceDependencyRef(self, value: Optional[RefType]) -> DiagnosticStorageConditionPortMapping:
        """
        Reference to a SwcServiceDependencyType that links ServiceNeeds to SWC service ports.
        A None value is a no-op and does not overwrite an existing swcFlatServiceDependencyRef.
        """
        if value is not None:
            self.swcFlatServiceDependencyRef = value
        return self

    def getSwcServiceDependencyInSystemIRef(self) -> Optional[RefType]:
        """
        Instance reference to a SwcServiceDependency that links ServiceNeeds to SWC service ports. InstanceRef implemented by: SwcServiceDependencyInSystemInstanceRef
        """
        return self.swcServiceDependencyInSystemIRef

    def setSwcServiceDependencyInSystemIRef(self, value: Optional[RefType]) -> DiagnosticStorageConditionPortMapping:
        """
        Instance reference to a SwcServiceDependency that links ServiceNeeds to SWC service ports. InstanceRef implemented by: SwcServiceDependencyInSystemInstanceRef
        A None value is a no-op and does not overwrite an existing swcServiceDependencyInSystemIRef.
        """
        if value is not None:
            self.swcServiceDependencyInSystemIRef = value
        return self


class DiagnosticTestResult(ARElement):
    """
    This meta-class represents the ability to define diagnostic test results. Tags: atp.recommendedPackage=DiagnosticTestResults

    [constr_1850] Existence of aggregation DiagnosticTestResult.testIdentifier: For each DiagnosticTestResult, the aggregation of meta-class DiagnosticTestIdentifier in the role testIdentifier shall exist at the time when the DEXT is complete.

    [constr_1851] Existence of reference DiagnosticTestResult.monitoredIdentifier: For each DiagnosticTestResult, the reference to meta-class DiagnosticTestIdentifier in the role monitoredIdentifier shall exist at the time when the DEXT is complete.
    """

    # DiagnosticTestResult method parity checklist:
    # Spec: AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf, Table 4.201, p.204
    # Columns: impl / docstring / test / reader / writer / release   ([—] = no XML element)
    # [x] __init__                     [x] impl  [x] docstring  [x] test  [—] reader  [—] writer  R23-11
    # [x] getDiagnosticEventRef        [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setDiagnosticEventRef        [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getMonitoredIdentifierRef    [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setMonitoredIdentifierRef    [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getTestIdentifier            [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setTestIdentifier            [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getUpdateKind                [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setUpdateKind                [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11

    def __init__(self, parent: ARObject, short_name: str):
        super().__init__(parent, short_name)

        # This attribute represents the diagnostic event that is related to the diagnostic test result. Stereotypes: atpSplitable; atpVariation Tags: atp.Splitkey=diagnosticEvent.diagnosticEvent, diagnosticEvent.variationPoint.shortLabel vh.latestBindingTime=preCompileTime
        self.diagnosticEventRef: Optional[RefType] = None

        # This attribute represents the related diagnostic monitored identifier.
        self.monitoredIdentifierRef: Optional[RefType] = None

        # This attribute represents the applicable test identifier.
        self.testIdentifier: Optional[DiagnosticTestIdentifier] = None

        # This attribute controls the update behavior of the enclosing DiagnosticTestResult. Stereotypes: atpVariation Tags: vh.latestBindingTime=preCompileTime
        self.updateKind: Optional[DiagnosticTestResultUpdateEnum] = None

    def getDiagnosticEventRef(self) -> Optional[RefType]:
        """
        This attribute represents the diagnostic event that is related to the diagnostic test result. Stereotypes: atpSplitable; atpVariation Tags: atp.Splitkey=diagnosticEvent.diagnosticEvent, diagnosticEvent.variationPoint.shortLabel vh.latestBindingTime=preCompileTime
        """
        return self.diagnosticEventRef

    def setDiagnosticEventRef(self, value: Optional[RefType]) -> DiagnosticTestResult:
        """
        This attribute represents the diagnostic event that is related to the diagnostic test result. Stereotypes: atpSplitable; atpVariation Tags: atp.Splitkey=diagnosticEvent.diagnosticEvent, diagnosticEvent.variationPoint.shortLabel vh.latestBindingTime=preCompileTime

        A None value is a no-op and does not overwrite an existing diagnosticEventRef.
        """
        if value is not None:
            self.diagnosticEventRef = value
        return self

    def getMonitoredIdentifierRef(self) -> Optional[RefType]:
        """
        This attribute represents the related diagnostic monitored identifier.
        """
        return self.monitoredIdentifierRef

    def setMonitoredIdentifierRef(self, value: Optional[RefType]) -> DiagnosticTestResult:
        """
        This attribute represents the related diagnostic monitored identifier.

        A None value is a no-op and does not overwrite an existing monitoredIdentifierRef.
        """
        if value is not None:
            self.monitoredIdentifierRef = value
        return self

    def getTestIdentifier(self) -> Optional[DiagnosticTestIdentifier]:
        """
        This attribute represents the applicable test identifier.
        """
        return self.testIdentifier

    def setTestIdentifier(self, value: Optional[DiagnosticTestIdentifier]) -> DiagnosticTestResult:
        """
        This attribute represents the applicable test identifier.

        A None value is a no-op and does not overwrite an existing testIdentifier.
        """
        if value is not None:
            self.testIdentifier = value
        return self

    def getUpdateKind(self) -> Optional[DiagnosticTestResultUpdateEnum]:
        """
        This attribute controls the update behavior of the enclosing DiagnosticTestResult. Stereotypes: atpVariation Tags: vh.latestBindingTime=preCompileTime
        """
        return self.updateKind

    def setUpdateKind(self, value: Optional[DiagnosticTestResultUpdateEnum]) -> DiagnosticTestResult:
        """
        This attribute controls the update behavior of the enclosing DiagnosticTestResult. Stereotypes: atpVariation Tags: vh.latestBindingTime=preCompileTime

        A None value is a no-op and does not overwrite an existing updateKind.
        """
        if value is not None:
            self.updateKind = value
        return self


class DiagnosticTestRoutineIdentifier(ARElement):
    """This represents the test id of the DiagnosticTestIdentifier. Tags: atp.recommendedPackage=DiagnosticTestRoutineIdentifier"""

    # DiagnosticTestRoutineIdentifier method parity checklist:
    # Spec: AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf, Table 4.143, p.158
    # Columns: impl / docstring / test / reader / writer / release   ([—] = no XML element)
    # [x] __init__                       [x] impl  [x] docstring  [x] test  [—] reader  [—] writer  R23-11
    # [x] getId                          [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setId                          [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getRequestDataSize             [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setRequestDataSize             [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getResponseDataSize            [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setResponseDataSize            [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11

    def __init__(self, parent: ARObject, short_name: str):
        super().__init__(parent, short_name)

        # This represents the numerical id of the DiagnosticTestIdentifier (see SAE J1979-DA).
        self.id: Optional[PositiveInteger] = None

        # This represents the specified data size for the request message. Unit: byte.
        self.requestDataSize: Optional[PositiveInteger] = None

        # This represents the specified data size for the response message. Unit:byte.
        self.responseDataSize: Optional[PositiveInteger] = None

    def getId(self) -> Optional[PositiveInteger]:
        """
        This represents the numerical id of the DiagnosticTestIdentifier (see SAE J1979-DA).
        """
        return self.id

    def setId(self, value: Optional[PositiveInteger]) -> DiagnosticTestRoutineIdentifier:
        """
        This represents the numerical id of the DiagnosticTestIdentifier (see SAE J1979-DA).

        A None value is a no-op and does not overwrite an existing id.
        """
        if value is not None:
            self.id = value
        return self

    def getRequestDataSize(self) -> Optional[PositiveInteger]:
        """
        This represents the specified data size for the request message. Unit: byte.
        """
        return self.requestDataSize

    def setRequestDataSize(self, value: Optional[PositiveInteger]) -> DiagnosticTestRoutineIdentifier:
        """
        This represents the specified data size for the request message. Unit: byte.

        A None value is a no-op and does not overwrite an existing requestDataSize.
        """
        if value is not None:
            self.requestDataSize = value
        return self

    def getResponseDataSize(self) -> Optional[PositiveInteger]:
        """
        This represents the specified data size for the response message. Unit:byte.
        """
        return self.responseDataSize

    def setResponseDataSize(self, value: Optional[PositiveInteger]) -> DiagnosticTestRoutineIdentifier:
        """
        This represents the specified data size for the response message. Unit:byte.

        A None value is a no-op and does not overwrite an existing responseDataSize.
        """
        if value is not None:
            self.responseDataSize = value
        return self


class DiagnosticTransferExit(DiagnosticMemoryByAddress):
    """This represents an instance of the "Transfer Exit" diagnostic service. Tags: atp.recommendedPackage=DiagnosticMemoryByAdresss"""

    # DiagnosticTransferExit method parity checklist:
    # Spec: AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf, Table 4.117, p.143
    # Columns: impl / docstring / test / reader / writer / release   ([—] = no XML element)
    # [x] __init__                  [x] impl  [x] docstring  [x] test  [—] reader  [—] writer  R23-11
    # [x] getTransferExitClassRef   [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setTransferExitClassRef   [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11

    def __init__(self, parent: ARObject, short_name: str):
        super().__init__(parent, short_name)

        # This reference substantiates that abstract reference in the role serviceClass for this specific concrete class. Thereby, the reference represents the ability to access shared attributes among all DiagnosticTransferExit in the given context.
        self.transferExitClassRef: Optional[RefType] = None

    def getTransferExitClassRef(self) -> Optional[RefType]:
        """
        This reference substantiates that abstract reference in the role serviceClass for this specific concrete class. Thereby, the reference represents the ability to access shared attributes among all DiagnosticTransferExit in the given context.
        """
        return self.transferExitClassRef

    def setTransferExitClassRef(self, value: Optional[RefType]) -> DiagnosticTransferExit:
        """
        This reference substantiates that abstract reference in the role serviceClass for this specific concrete class. Thereby, the reference represents the ability to access shared attributes among all DiagnosticTransferExit in the given context.

        A None value is a no-op and does not overwrite an existing transferExitClassRef.
        """
        if value is not None:
            self.transferExitClassRef = value
        return self


class DiagnosticTroubleCode(ARElement, ABC):
    """A diagnostic trouble code defines a unique identifier that is shown to the diagnostic tester."""

    # DiagnosticTroubleCode method parity checklist:
    # Spec: AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf, Table 4.161, p.176
    # Columns: impl / docstring / test / reader / writer / release   ([—] = no XML element)
    # [x] __init__     [x] impl  [x] docstring  [x] test  [—] reader  [—] writer  R23-11

    def __init__(self, parent: ARObject, short_name: str):
        super().__init__(parent, short_name)


class DiagnosticTroubleCodeGroup(ARElement):
    """
    The diagnostic trouble code group defines the DTCs belonging together and thereby forming a group. Tags: atp.recommendedPackage=DiagnosticTroubleCodes

    [constr_1830] Existence of DiagnosticTroubleCodeGroup.groupNumber: For each DiagnosticTroubleCodeGroup, attribute groupNumber shall exist at the time when the DEXT is complete.
    """

    # DiagnosticTroubleCodeGroup method parity checklist:
    # Spec: AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf, Table 4.162, p.177
    # Columns: impl / docstring / test / reader / writer / release   ([—] = no XML element)
    # [x] __init__            [x] impl  [x] docstring  [x] test  [—] reader  [—] writer  R23-11
    # [x] addDtcRef           [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getDtcRefs          [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] getGroupNumber      [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setGroupNumber      [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11

    def __init__(self, parent: ARObject, short_name: str):
        super().__init__(parent, short_name)

        # This represents the collection of DiagnosticTroubleCodes defined by this DiagnosticTroubleCodeGroup. Stereotypes: atpSplitable; atpVariation Tags: atp.Splitkey=dtc.diagnosticTroubleCode, dtc.variation Point.shortLabel vh.latestBindingTime=postBuild
        self.dtcRefs: List[RefType] = []

        # This represents the base number of the DTC group. Stereotypes: atpVariation Tags: vh.latestBindingTime=preCompileTime
        self.groupNumber: Optional[PositiveInteger] = None

    def addDtcRef(self, ref: Optional[RefType]) -> DiagnosticTroubleCodeGroup:
        """
        This represents the collection of DiagnosticTroubleCodes defined by this DiagnosticTroubleCodeGroup.

        A None value is a no-op and does not extend the dtcRefs list.
        """
        if ref is not None:
            self.dtcRefs.append(ref)
        return self

    def getDtcRefs(self) -> List[RefType]:
        """
        This represents the collection of DiagnosticTroubleCodes defined by this DiagnosticTroubleCodeGroup.
        """
        return self.dtcRefs

    def getGroupNumber(self) -> Optional[PositiveInteger]:
        """
        This represents the base number of the DTC group.
        """
        return self.groupNumber

    def setGroupNumber(self, value: Optional[PositiveInteger]) -> DiagnosticTroubleCodeGroup:
        """
        This represents the base number of the DTC group.

        A None value is a no-op and does not overwrite an existing groupNumber.
        """
        if value is not None:
            self.groupNumber = value
        return self


class DiagnosticTroubleCodeJ1939(DiagnosticTroubleCode):
    """This meta-class represents the ability to model specific trouble-code related properties for J1939. Tags: atp.recommendedPackage=DiagnosticTroubleCodes"""

    # DiagnosticTroubleCodeJ1939 method parity checklist:
    # Spec: AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf, Table 4.223, p.222
    # Columns: impl / docstring / test / reader / writer / release   ([—] = no XML element)
    # [x] __init__          [x] impl  [x] docstring  [x] test  [—] reader  [—] writer  R23-11
    # [x] getDtcPropsRef    [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setDtcPropsRef    [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getFmi            [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setFmi            [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getKind           [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setKind           [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getNodeRef        [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setNodeRef        [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getSpnRef         [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setSpnRef         [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11

    def __init__(self, parent: ARObject, short_name: str):
        super().__init__(parent, short_name)

        # Defined properties associated with the J1939 DTC.
        self.dtcPropsRef: Optional[RefType] = None

        # This attribute represents the behavior of the Failure Mode Indicator.
        self.fmi: Optional[PositiveInteger] = None

        # This attribute further specifies the DTC in terms of its semantics.
        self.kind: Optional[DiagnosticTroubleCodeJ1939DtcKindEnum] = None

        # This represents the related DiagnosticJ1939Node.
        self.nodeRef: Optional[RefType] = None

        # This represents the releated SPN.
        self.spnRef: Optional[RefType] = None

    def getDtcPropsRef(self) -> Optional[RefType]:
        """
        Defined properties associated with the J1939 DTC.
        """
        return self.dtcPropsRef

    def setDtcPropsRef(self, value: Optional[RefType]) -> DiagnosticTroubleCodeJ1939:
        """
        Defined properties associated with the J1939 DTC.
        A None value is a no-op and does not overwrite an existing dtcProps reference.
        """
        if value is not None:
            self.dtcPropsRef = value
        return self

    def getFmi(self) -> Optional[PositiveInteger]:
        """
        This attribute represents the behavior of the Failure Mode Indicator.
        """
        return self.fmi

    def setFmi(self, value: Optional[PositiveInteger]) -> DiagnosticTroubleCodeJ1939:
        """
        This attribute represents the behavior of the Failure Mode Indicator.
        A None value is a no-op and does not overwrite an existing fmi.
        """
        if value is not None:
            self.fmi = value
        return self

    def getKind(self) -> Optional[DiagnosticTroubleCodeJ1939DtcKindEnum]:
        """
        This attribute further specifies the DTC in terms of its semantics.
        """
        return self.kind

    def setKind(self, value: Optional[DiagnosticTroubleCodeJ1939DtcKindEnum]) -> DiagnosticTroubleCodeJ1939:
        """
        This attribute further specifies the DTC in terms of its semantics.
        A None value is a no-op and does not overwrite an existing kind.
        """
        if value is not None:
            self.kind = value
        return self

    def getNodeRef(self) -> Optional[RefType]:
        """
        This represents the related DiagnosticJ1939Node.
        """
        return self.nodeRef

    def setNodeRef(self, value: Optional[RefType]) -> DiagnosticTroubleCodeJ1939:
        """
        This represents the related DiagnosticJ1939Node.
        A None value is a no-op and does not overwrite an existing node reference.
        """
        if value is not None:
            self.nodeRef = value
        return self

    def getSpnRef(self) -> Optional[RefType]:
        """
        This represents the releated SPN.
        """
        return self.spnRef

    def setSpnRef(self, value: Optional[RefType]) -> DiagnosticTroubleCodeJ1939:
        """
        This represents the releated SPN.
        A None value is a no-op and does not overwrite an existing spn reference.
        """
        if value is not None:
            self.spnRef = value
        return self


class DiagnosticTroubleCodeUdsToTroubleCodeObdMapping(DiagnosticMapping):
    """This meta-class represents the ability to associate a UDS trouble code to an OBD trouble code. Tags: atp.recommendedPackage=DiagnosticMappings"""

    # DiagnosticTroubleCodeUdsToTroubleCodeObdMapping method parity checklist:
    # Spec: AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf, Table 4.180, p.188
    # Columns: impl / docstring / test / reader / writer / release   ([—] = no XML element)
    # [x] __init__              [x] impl  [x] docstring  [x] test  [—] reader  [—] writer  R23-11
    # [x] getTroubleCodeObdRef  [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setTroubleCodeObdRef  [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getTroubleCodeUdsRef  [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setTroubleCodeUdsRef  [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11

    def __init__(self, parent: ARObject, short_name: str):
        super().__init__(parent, short_name)

        # This represents the OBD DTC referenced in the mapping between UDS and OBD DTCs.
        self.troubleCodeObdRef: Optional[RefType] = None

        # This represents the UDS DTC referenced in the mapping between UDS and OBD DTCs.
        self.troubleCodeUdsRef: Optional[RefType] = None

    def getTroubleCodeObdRef(self) -> Optional[RefType]:
        """
        This represents the OBD DTC referenced in the mapping between UDS and OBD DTCs.
        """
        return self.troubleCodeObdRef

    def setTroubleCodeObdRef(self, value: Optional[RefType]) -> DiagnosticTroubleCodeUdsToTroubleCodeObdMapping:
        """
        This represents the OBD DTC referenced in the mapping between UDS and OBD DTCs.
        A None value is a no-op and does not overwrite an existing troubleCodeObdRef.
        """
        if value is not None:
            self.troubleCodeObdRef = value
        return self

    def getTroubleCodeUdsRef(self) -> Optional[RefType]:
        """
        This represents the UDS DTC referenced in the mapping between UDS and OBD DTCs.
        """
        return self.troubleCodeUdsRef

    def setTroubleCodeUdsRef(self, value: Optional[RefType]) -> DiagnosticTroubleCodeUdsToTroubleCodeObdMapping:
        """
        This represents the UDS DTC referenced in the mapping between UDS and OBD DTCs.
        A None value is a no-op and does not overwrite an existing troubleCodeUdsRef.
        """
        if value is not None:
            self.troubleCodeUdsRef = value
        return self


class DiagnosticVerifyCertificateBidirectional(DiagnosticAuthentication):
    """This meta-class represents the subfunction to do a bidirectional verification of the certificate."""

    # DiagnosticVerifyCertificateBidirectional method parity checklist:
    # Spec: AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf, Table 4.54, p.99
    # Columns: impl / docstring / test / reader / writer / release   ([—] = no XML element)
    # [x] __init__  [x] impl  [x] docstring  [x] test  [—] reader  [—] writer  R23-11

    def __init__(self, parent: ARObject, short_name: str):
        super().__init__(parent, short_name)


class DiagnosticVerifyCertificateUnidirectional(DiagnosticAuthentication):
    """This meta-class represents the subfunction to do a unidirectional verification of the certificate."""

    # DiagnosticVerifyCertificateUnidirectional method parity checklist:
    # Spec: AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf, Table 4.55, p.100
    # Columns: impl / docstring / test / reader / writer / release   ([—] = no XML element)
    # [x] __init__  [x] impl  [x] docstring  [x] test  [x] reader  [x] writer  R23-11

    def __init__(self, parent: ARObject, short_name: str):
        super().__init__(parent, short_name)


class DiagnosticWriteDataByIdentifier(DiagnosticDataByIdentifier):
    """This represents an instance of the "Write Data by Identifier" diagnostic service."""

    # DiagnosticWriteDataByIdentifier method parity checklist:
    # Spec: AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf, Table 4.71, p.113
    # Columns: impl / docstring / test / reader / writer / release   ([—] = no XML element)
    # [x] __init__           [x] impl  [x] docstring  [x] test  [—] reader  [—] writer  R23-11
    # [x] getWriteClass      [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setWriteClass      [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11

    def __init__(self, parent: ARObject, short_name: str):
        super().__init__(parent, short_name)

        # This reference substantiates that abstract reference in the role serviceClass for this specific concrete class. Thereby, the reference represents the ability to access shared attributes among all DiagnosticWriteDataByIdentifier in the given context.
        self.writeClass: Optional[RefType] = None

    def getWriteClass(self) -> Optional[RefType]:
        """
        This reference substantiates that abstract reference in the role serviceClass for this specific concrete class. Thereby, the reference represents the ability to access shared attributes among all DiagnosticWriteDataByIdentifier in the given context.
        """
        return self.writeClass

    def setWriteClass(self, value: Optional[RefType]) -> DiagnosticWriteDataByIdentifier:
        """
        This reference substantiates that abstract reference in the role serviceClass for this specific concrete class. Thereby, the reference represents the ability to access shared attributes among all DiagnosticWriteDataByIdentifier in the given context.

        A None value is a no-op and does not overwrite an existing writeClass.
        """
        if value is not None:
            self.writeClass = value
        return self


class DiagnosticReadMemoryByAddress(DiagnosticMemoryAddressableRangeAccess):
    """This represents an instance of the "Read Memory by Address" diagnostic service. Tags: atp.recommendedPackage=DiagnosticMemoryByAdresss"""

    # DiagnosticReadMemoryByAddress method parity checklist:
    # Spec: AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf, Table 4.115, p.142
    # Columns: impl / docstring / test / reader / writer / release   ([—] = no XML element)
    # [x] __init__           [x] impl  [x] docstring  [x] test  [—] reader  [—] writer  R23-11
    # [x] getReadClassRef    [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setReadClassRef    [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11

    def __init__(self, parent: ARObject, short_name: str):
        super().__init__(parent, short_name)

        # This reference substantiates that abstract reference in the role serviceClass for this specific concrete class. Thereby, the reference represents the ability to access shared attributes among all DiagnosticReadMemoryByAddresst in the given context.
        self.readClassRef: Optional[RefType] = None

    def getReadClassRef(self) -> Optional[RefType]:
        """
        This reference substantiates that abstract reference in the role serviceClass for this specific concrete class. Thereby, the reference represents the ability to access shared attributes among all DiagnosticReadMemoryByAddresst in the given context.
        """
        return self.readClassRef

    def setReadClassRef(self, value: Optional[RefType]) -> DiagnosticReadMemoryByAddress:
        """
        This reference substantiates that abstract reference in the role serviceClass for this specific concrete class. Thereby, the reference represents the ability to access shared attributes among all DiagnosticReadMemoryByAddresst in the given context.

        A None value is a no-op and does not overwrite an existing readClassRef.
        """
        if value is not None:
            self.readClassRef = value
        return self


class DiagnosticWriteMemoryByAddress(DiagnosticMemoryAddressableRangeAccess):
    """This represents an instance of the "Write Memory by Address" diagnostic service. Tags: atp.recommendedPackage=DiagnosticMemoryByAdresss"""

    # DiagnosticWriteMemoryByAddress method parity checklist:
    # Spec: AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf, Table 4.113, p.141
    # Columns: impl / docstring / test / reader / writer / release   ([—] = no XML element)
    # [x] __init__            [x] impl  [x] docstring  [x] test  [—] reader  [—] writer  R23-11
    # [x] getWriteClassRef    [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setWriteClassRef    [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11

    def __init__(self, parent: ARObject, short_name: str):
        super().__init__(parent, short_name)

        # This reference substantiates that abstract reference in the role serviceClass for this specific concrete class. Thereby, the reference represents the ability to access shared attributes among all DiagnosticWritememoryByAddress in the given context.
        self.writeClassRef: Optional[RefType] = None

    def getWriteClassRef(self) -> Optional[RefType]:
        """
        This reference substantiates that abstract reference in the role serviceClass for this specific concrete class. Thereby, the reference represents the ability to access shared attributes among all DiagnosticWritememoryByAddress in the given context.
        """
        return self.writeClassRef

    def setWriteClassRef(self, value: Optional[RefType]) -> DiagnosticWriteMemoryByAddress:
        """
        This reference substantiates that abstract reference in the role serviceClass for this specific concrete class. Thereby, the reference represents the ability to access shared attributes among all DiagnosticWritememoryByAddress in the given context.

        A None value is a no-op and does not overwrite an existing writeClassRef.
        """
        if value is not None:
            self.writeClassRef = value
        return self


class FMFeature(ARElement):
    pass


class FMFeatureMap(ARElement):
    pass


class FMFeatureModel(ARElement):
    pass


class FMFeatureSelectionSet(ARElement):
    pass


class IdsDesign(ARElement):
    pass


class LifeCycleStateDefinitionGroup(ARElement):
    """
    This meta class represents the ability to define the states and properties of one particular life cycle. Tags: atp.recommendedPackage=LifeCycleStateDefintionGroups
    """

    # LifeCycleStateDefinitionGroup method parity checklist:
    # Spec: AUTOSAR_FO_TPS_GenericStructureTemplate.pdf, Table 12.1, p.388
    # Columns: impl / docstring / test / reader / writer / release   ([—] = no XML element)
    # [x] __init__         [x] impl  [x] docstring  [x] test  [—] reader  [—] writer  R23-11
    # [x] createLcState    [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getLcStates      [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11

    def __init__(self, parent: ARObject, short_name: str):
        super().__init__(parent, short_name)

        # Describes a single life cycle state of this life cycle state definition group.
        self.lcStates: List[LifeCycleState] = []

    def createLcState(self, short_name: str) -> LifeCycleState:
        """
        Creates a LifeCycleState of this life cycle state definition group with the given short name, or returns the existing one if it already exists.

        Args:
            short_name: The short name for the new LifeCycleState

        Returns:
            The created (or existing) LifeCycleState
        """
        if not self.IsReferrableElementExists(short_name, LifeCycleState):
            state = LifeCycleState(self, short_name)
            self.addReferrableElement(state)
            self.lcStates.append(state)
        return cast(LifeCycleState, self.getReferrableElement(short_name, LifeCycleState))

    def getLcStates(self) -> List[LifeCycleState]:
        """
        Describes a single life cycle state of this life cycle state definition group.
        """
        return self.lcStates


class PhysicalDimensionMappingSet(ARElement):
    """This class represents a container for a list of mappings between PhysicalDimensions. Tags: atp.recommendedPackage=PhysicalDimensionMappingSets"""

    # PhysicalDimensionMappingSet method parity checklist:
    # Spec: AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf, Table 5.78, p.399
    # Columns: impl / docstring / test / reader / writer / release   ([—] = no XML element)
    # [x] __init__                     [x] impl  [x] docstring  [x] test  [—] reader  [—] writer  R23-11
    # [x] addPhysicalDimensionMapping  [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getPhysicalDimensionMappings [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11

    def __init__(self, parent: ARObject, short_name: str):
        super().__init__(parent, short_name)

        # This aggregation represents a concrete collections of PhysicalDimensionMappings in the context of one PhysicalDimensionMappingSet.
        self.physicalDimensionMappings: List[PhysicalDimensionMapping] = []

    def addPhysicalDimensionMapping(self, value: Optional[PhysicalDimensionMapping]) -> PhysicalDimensionMappingSet:
        """
        This aggregation represents a concrete collections of PhysicalDimensionMappings in the context of one PhysicalDimensionMappingSet.

        A None value is a no-op and does not append a physicalDimensionMapping.
        """
        if value is not None:
            self.physicalDimensionMappings.append(value)
        return self

    def getPhysicalDimensionMappings(self) -> List[PhysicalDimensionMapping]:
        """
        This aggregation represents a concrete collections of PhysicalDimensionMappings in the context of one PhysicalDimensionMappingSet.
        """
        return self.physicalDimensionMappings


class PostBuildVariantCriterionValueSet(ARElement):
    pass


class SecurityEventContextMappingApplication(ARElement):
    pass


class SecurityEventContextMappingBswModule(ARElement):
    pass


class SecurityEventContextMappingFunctionalCluster(ARElement):
    pass


class SecurityEventDefinition(ARElement):
    pass


class CpSoftwareClusterBinaryManifestDescriptor(ARElement):
    pass


class CpSoftwareClusterResourcePool(ARElement):
    pass


class CryptoServiceKey(ARElement):
    pass


class CryptoServiceQueue(ARElement):
    pass


class GeneralPurposeConnection(ARElement):
    pass


class GlobalTimeDomain(ARElement):
    pass


class LogAndTraceMessageCollectionSet(ARElement):
    pass


class TransformationPropsSet(ARElement):
    pass


class IEEE1722TpAcfConnection(IEEE1722TpConnection):
    pass


class IEEE1722TpAafConnection(IEEE1722TpAvConnection):
    pass


class IEEE1722TpIidcConnection(IEEE1722TpAvConnection):
    pass


class IEEE1722TpRvfConnection(IEEE1722TpAvConnection):
    pass
