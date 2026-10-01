"""
This module contains the ARPackage class and related classes for AUTOSAR models
in the GenericStructure module. ARPackage represents a hierarchical container for
organizing AUTOSAR elements according to the AUTOSAR standard. It serves as the
primary organizational unit for grouping related AUTOSAR model elements such as
components, interfaces, data types, and other packages.
"""

from __future__ import annotations
from typing import List, Optional
from typing import TYPE_CHECKING

from abc import ABC

if TYPE_CHECKING:
    # ApplicationDeferredDataType is bound at runtime by the PEP 562 __getattr__ below
    # (AbstractPlatform closes an import cycle), so it is imported here for typing only.
    from armodel.models.M2.AUTOSARTemplates.AbstractPlatform import ApplicationDeferredDataType
    from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ElementCollection import (
        Collection,
    )
    from armodel.models.M2.MSR.AsamHdo.BaseTypes import SwBaseType

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import ARObject, DiagnosticCommonProps, DiagnosticParameter, DiagnosticSupportInfoByte
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable import DiagnosticAuthTransmitCertificateEvaluation, Identifiable, Referrable
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
    "RapidPrototypingScenario",
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
    "DiagnosticVerifyCertificateUnidirectional",
    "DiagnosticVerifyCertificateBidirectional",
    "DiagnosticTroubleCodeUdsToTroubleCodeObdMapping",
    "DiagnosticTroubleCodeGroup",
    "DiagnosticTroubleCode",
    "DiagnosticTransferExit",
    "DiagnosticTestRoutineIdentifier",
    "DiagnosticTestResult",
    "DiagnosticStorageConditionPortMapping",
    "DiagnosticStorageConditionGroup",
    "DiagnosticStorageCondition",
    "DiagnosticSessionControl",
    "DiagnosticServiceDataMapping",
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
    "DiagnosticRequestControlOfOnBoardDevice",
    "DiagnosticReadScalingDataByIdentifier",
    "DiagnosticReadDataByPeriodicID",
    "DiagnosticReadDataByIdentifier",
    "DiagnosticReadDTCInformation",
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
    "ServiceProxySwComponentType",
    "ServiceSwComponentType",
    "SignalServiceTranslationPropsSet",
    "SoAdRoutingGroup",
    "SomeipSdClientEventGroupTimingConfig",
    "SomeipSdClientServiceInstanceConfig",
    "SomeipSdServerEventGroupTimingConfig",
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
    "TriggerInterface",
    "Unit",
    "UserDefinedIPdu",
    "UserDefinedPdu",
    "ARElement",
    "ARPackage",
    "PackageableElement",
    "ReferenceBase",
    "ApplicationPartition",
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
    "J1939ControllerApplication",
    "LogAndTraceMessageCollectionSet",
    "MacSecParticipantSet",
    "SocketConnectionIpduIdentifierSet",
    "TransformationPropsSet",
    "VfbTiming",
]


from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import CategoryString  # noqa: E402,F401


from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import Boolean, Identifier, NameToken, PositiveInteger, RefType, ReferrableSubtypesEnum  # noqa: E402
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
    # [x] getElement        [x] impl  [x] docstring  [x] test  [—] reader  [—] writer  R23-11
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
        # return list(filter(lambda e: isinstance(e, ARPackage), self.elements))

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

    def getElement(self, short_name: str, type=None) -> Referrable:
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
        return Identifiable.getElement(self, short_name, type)

    def createEcuAbstractionSwComponentType(self, short_name: str) -> EcuAbstractionSwComponentType:

        if not self.IsElementExists(short_name, EcuAbstractionSwComponentType):
            sw_component = EcuAbstractionSwComponentType(self, short_name)
            self.addElement(sw_component)
        return self.getElement(short_name, EcuAbstractionSwComponentType)

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

        if not self.IsElementExists(short_name, ApplicationSwComponentType):
            sw_component = ApplicationSwComponentType(self, short_name)
            self.addElement(sw_component)
        return self.getElement(short_name, ApplicationSwComponentType)

    def createComplexDeviceDriverSwComponentType(self, short_name: str) -> ComplexDeviceDriverSwComponentType:

        if not self.IsElementExists(short_name, ComplexDeviceDriverSwComponentType):
            sw_component = ComplexDeviceDriverSwComponentType(self, short_name)
            self.addElement(sw_component)
        return self.getElement(short_name, ComplexDeviceDriverSwComponentType)

    def createServiceSwComponentType(self, short_name: str) -> ServiceSwComponentType:

        if not self.IsElementExists(short_name, ServiceSwComponentType):
            sw_component = ServiceSwComponentType(self, short_name)
            self.addElement(sw_component)
        return self.getElement(short_name, ServiceSwComponentType)

    def createSensorActuatorSwComponentType(self, short_name: str) -> SensorActuatorSwComponentType:

        if not self.IsElementExists(short_name, SensorActuatorSwComponentType):
            sw_component = SensorActuatorSwComponentType(self, short_name)
            self.addElement(sw_component)
        return self.getElement(short_name, SensorActuatorSwComponentType)

    def createNvBlockSwComponentType(self, short_name: str) -> NvBlockSwComponentType:

        if not self.IsElementExists(short_name, NvBlockSwComponentType):
            sw_component = NvBlockSwComponentType(self, short_name)
            self.addElement(sw_component)
        return self.getElement(short_name, NvBlockSwComponentType)

    def createServiceProxySwComponentType(self, short_name: str) -> ServiceProxySwComponentType:

        if not self.IsElementExists(short_name, ServiceProxySwComponentType):
            sw_component = ServiceProxySwComponentType(self, short_name)
            self.addElement(sw_component)
        return self.getElement(short_name, ServiceProxySwComponentType)

    def createCompositionSwComponentType(self, short_name: str) -> CompositionSwComponentType:

        if not self.IsElementExists(short_name, CompositionSwComponentType):
            sw_component = CompositionSwComponentType(self, short_name)
            self.addElement(sw_component)
        return self.getElement(short_name, CompositionSwComponentType)

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

        if not self.IsElementExists(short_name, SenderReceiverInterface):
            sr_interface = SenderReceiverInterface(self, short_name)
            self.addElement(sr_interface)
        return self.getElement(short_name, SenderReceiverInterface)

    def createParameterInterface(self, short_name: str) -> ParameterInterface:

        if not self.IsElementExists(short_name, ParameterInterface):
            sr_interface = ParameterInterface(self, short_name)
            self.addElement(sr_interface)
        return self.getElement(short_name, ParameterInterface)

    def createNvDataInterface(self, short_name: str) -> NvDataInterface:

        if not self.IsElementExists(short_name, NvDataInterface):
            nv_interface = NvDataInterface(self, short_name)
            self.addElement(nv_interface)
        return self.getElement(short_name, NvDataInterface)

    def createGenericEthernetFrame(self, short_name: str) -> GenericEthernetFrame:

        if not self.IsElementExists(short_name, GenericEthernetFrame):
            frame = GenericEthernetFrame(self, short_name)
            self.addElement(frame)
        return self.getElement(short_name, GenericEthernetFrame)

    def createLifeCycleInfoSet(self, short_name: str) -> LifeCycleInfoSet:

        if not self.IsElementExists(short_name, LifeCycleInfoSet):
            set = LifeCycleInfoSet(self, short_name)
            self.addElement(set)
        return self.getElement(short_name, LifeCycleInfoSet)

    def createDocumentation(self, short_name: str) -> Documentation:

        if not self.IsElementExists(short_name, Documentation):
            documentation = Documentation(self, short_name)
            self.addElement(documentation)
        return self.getElement(short_name, Documentation)

    def createClientServerInterface(self, short_name: str) -> ClientServerInterface:

        if not self.IsElementExists(short_name, ClientServerInterface):
            cs_interface = ClientServerInterface(self, short_name)
            self.addElement(cs_interface)
        return self.getElement(short_name, ClientServerInterface)

    def createApplicationPrimitiveDataType(self, short_name: str) -> ApplicationPrimitiveDataType:

        if not self.IsElementExists(short_name, ApplicationPrimitiveDataType):
            data_type = ApplicationPrimitiveDataType(self, short_name)
            self.addElement(data_type)
        return self.getElement(short_name, ApplicationPrimitiveDataType)

    def createApplicationRecordDataType(self, short_name: str) -> ApplicationRecordDataType:

        if not self.IsElementExists(short_name, ApplicationRecordDataType):
            data_type = ApplicationRecordDataType(self, short_name)
            self.addElement(data_type)
        return self.getElement(short_name, ApplicationRecordDataType)

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

        if not self.IsElementExists(short_name, ApplicationDeferredDataType):
            data_type = ApplicationDeferredDataType(self, short_name)
            self.addElement(data_type)
        return self.getElement(short_name, ApplicationDeferredDataType)

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

        if not self.IsElementExists(short_name, ImplementationDataType):
            data_type = ImplementationDataType(self, short_name)
            self.addElement(data_type)
        return self.getElement(short_name, ImplementationDataType)

    def createSwBaseType(self, short_name: str) -> SwBaseType:

        if not self.IsElementExists(short_name, SwBaseType):
            base_type = SwBaseType(self, short_name)
            self.addElement(base_type)
        return self.getElement(short_name, SwBaseType)

    def createDataTypeMappingSet(self, short_name: str) -> DataTypeMappingSet:

        if not self.IsElementExists(short_name, DataTypeMappingSet):
            mapping_set = DataTypeMappingSet(self, short_name)
            self.addElement(mapping_set)
        return self.getElement(short_name, DataTypeMappingSet)

    def createCompuMethod(self, short_name: str) -> CompuMethod:

        if not self.IsElementExists(short_name, CompuMethod):
            compu_method = CompuMethod(self, short_name)
            self.addElement(compu_method)
        return self.getElement(short_name, CompuMethod)

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

        if not self.IsElementExists(short_name, BswModuleDescription):
            desc = BswModuleDescription(self, short_name)
            self.addElement(desc)
        return self.getElement(short_name, BswModuleDescription)

    def createBswModuleEntry(self, short_name: str) -> BswModuleEntry:

        if not self.IsElementExists(short_name, BswModuleEntry):
            entry = BswModuleEntry(self, short_name)
            self.addElement(entry)
        return self.getElement(short_name, BswModuleEntry)

    def createBswImplementation(self, short_name: str) -> BswImplementation:

        if not self.IsElementExists(short_name, BswImplementation):
            impl = BswImplementation(self, short_name)
            self.addElement(impl)
        return self.getElement(short_name, BswImplementation)

    def createSwcImplementation(self, short_name: str) -> SwcImplementation:

        if not self.IsElementExists(short_name, SwcImplementation):
            impl = SwcImplementation(self, short_name)
            self.addElement(impl)
        return self.getElement(short_name, SwcImplementation)

    def createSwcBswMapping(self, short_name: str) -> SwcBswMapping:

        if not self.IsElementExists(short_name, SwcBswMapping):
            mapping = SwcBswMapping(self, short_name)
            self.addElement(mapping)
        return self.getElement(short_name, SwcBswMapping)

    def createBswEntryRelationshipSet(self, short_name: str) -> BswEntryRelationshipSet:

        if not self.IsElementExists(short_name, BswEntryRelationshipSet):
            entry_set = BswEntryRelationshipSet(self, short_name)
            self.addElement(entry_set)
        return self.getElement(short_name, BswEntryRelationshipSet)

    def createFirewallRule(self, short_name: str) -> FirewallRule:
        """
        Creates a FirewallRule element in this package.
        If a rule with the given short name already exists, it is returned instead.

        Args:
            short_name: The unique short name of the rule

        Returns:
            The created (or existing) FirewallRule
        """

        if not self.IsElementExists(short_name, FirewallRule):
            rule = FirewallRule(self, short_name)
            self.addElement(rule)
        return self.getElement(short_name, FirewallRule)

    def createBlueprintMappingSet(self, short_name: str) -> BlueprintMappingSet:
        """
        Creates a BlueprintMappingSet element in this package.
        If a set with the given short name already exists, it is returned instead.

        Args:
            short_name: The unique short name of the set

        Returns:
            The created (or existing) BlueprintMappingSet
        """

        if not self.IsElementExists(short_name, BlueprintMappingSet):
            blueprint_mapping_set = BlueprintMappingSet(self, short_name)
            self.addElement(blueprint_mapping_set)
        return self.getElement(short_name, BlueprintMappingSet)

    def getBlueprintMappingSets(self) -> List[BlueprintMappingSet]:
        """
        This represents a container of mappings between "actual" model elements and the "blueprint" that has been taken for their creation.
        """
        return list(filter(lambda a: isinstance(a, BlueprintMappingSet), self.elements))

    def createConstantSpecificationMappingSet(self, short_name: str) -> ConstantSpecificationMappingSet:
        """
        Creates a ConstantSpecificationMappingSet element in this package.
        If a set with the given short name already exists, it is returned instead.

        Args:
            short_name: The unique short name of the set

        Returns:
            The created (or existing) ConstantSpecificationMappingSet
        """

        if not self.IsElementExists(short_name, ConstantSpecificationMappingSet):
            constant_specification_mapping_set = ConstantSpecificationMappingSet(self, short_name)
            self.addElement(constant_specification_mapping_set)
        return self.getElement(short_name, ConstantSpecificationMappingSet)

    def getConstantSpecificationMappingSets(self) -> List[ConstantSpecificationMappingSet]:
        """
        This meta-class represents the ability to map two ConstantSpecifications to each others. One Constant Specification is supposed to be described in the application domain and the other should be described in the implementation domain.
        """
        return list(filter(lambda a: isinstance(a, ConstantSpecificationMappingSet), self.elements))

    def createStateDependentFirewall(self, short_name: str) -> StateDependentFirewall:
        """
        Creates a StateDependentFirewall element in this package.
        If a firewall with the given short name already exists, it is returned instead.

        Args:
            short_name: The unique short name of the firewall

        Returns:
            The created (or existing) StateDependentFirewall
        """

        if not self.IsElementExists(short_name, StateDependentFirewall):
            firewall = StateDependentFirewall(self, short_name)
            self.addElement(firewall)
        return self.getElement(short_name, StateDependentFirewall)

    def createPlatformModuleEthernetEndpointConfiguration(self, short_name: str) -> PlatformModuleEthernetEndpointConfiguration:
        """
        Creates a PlatformModuleEthernetEndpointConfiguration element in this package.
        If a configuration with the given short name already exists, it is returned instead.

        Args:
            short_name: The unique short name of the configuration

        Returns:
            The created (or existing) PlatformModuleEthernetEndpointConfiguration
        """

        if not self.IsElementExists(short_name, PlatformModuleEthernetEndpointConfiguration):
            configuration = PlatformModuleEthernetEndpointConfiguration(self, short_name)
            self.addElement(configuration)
        return self.getElement(short_name, PlatformModuleEthernetEndpointConfiguration)

    def createMcFunction(self, short_name: str) -> McFunction:
        """
        Creates an McFunction element in this package.
        If a function with the given short name already exists, it is returned instead.

        Args:
            short_name: The unique short name of the function

        Returns:
            The created (or existing) McFunction
        """

        if not self.IsElementExists(short_name, McFunction):
            func = McFunction(self, short_name)
            self.addElement(func)
        return self.getElement(short_name, McFunction)

    def createMcGroup(self, short_name: str) -> McGroup:
        """
        Creates an McGroup element in this package.
        If a group with the given short name already exists, it is returned instead.

        Args:
            short_name: The unique short name of the group

        Returns:
            The created (or existing) McGroup
        """

        if not self.IsElementExists(short_name, McGroup):
            group = McGroup(self, short_name)
            self.addElement(group)
        return self.getElement(short_name, McGroup)

    def createConstantSpecification(self, short_name: str) -> ConstantSpecification:

        if not self.IsElementExists(short_name, ConstantSpecification):
            spec = ConstantSpecification(self, short_name)
            self.addElement(spec)
        return self.getElement(short_name, ConstantSpecification)

    def createCryptoEllipticCurveProps(self, short_name: str) -> CryptoEllipticCurveProps:

        if not self.IsElementExists(short_name, CryptoEllipticCurveProps):
            props = CryptoEllipticCurveProps(self, short_name)
            self.addElement(props)
        return self.getElement(short_name, CryptoEllipticCurveProps)

    def createCryptoSignatureScheme(self, short_name: str) -> CryptoSignatureScheme:

        if not self.IsElementExists(short_name, CryptoSignatureScheme):
            scheme = CryptoSignatureScheme(self, short_name)
            self.addElement(scheme)
        return self.getElement(short_name, CryptoSignatureScheme)

    def createCryptoServiceCertificate(self, short_name: str) -> CryptoServiceCertificate:

        if not self.IsElementExists(short_name, CryptoServiceCertificate):
            certificate = CryptoServiceCertificate(self, short_name)
            self.addElement(certificate)
        return self.getElement(short_name, CryptoServiceCertificate)

    def createIPSecConfigProps(self, short_name: str) -> IPSecConfigProps:

        if not self.IsElementExists(short_name, IPSecConfigProps):
            props = IPSecConfigProps(self, short_name)
            self.addElement(props)
        return self.getElement(short_name, IPSecConfigProps)

    def createCryptoServicePrimitive(self, short_name: str) -> CryptoServicePrimitive:

        if not self.IsElementExists(short_name, CryptoServicePrimitive):
            primitive = CryptoServicePrimitive(self, short_name)
            self.addElement(primitive)
        return self.getElement(short_name, CryptoServicePrimitive)

    def createDataConstr(self, short_name: str) -> DataConstr:

        if not self.IsElementExists(short_name, DataConstr):
            constr = DataConstr(self, short_name)
            self.addElement(constr)
        return self.getElement(short_name, DataConstr)

    def createUnit(self, short_name: str) -> Unit:

        if not self.IsElementExists(short_name, Unit):
            unit = Unit(self, short_name)
            self.addElement(unit)
        return self.getElement(short_name, Unit)

    def createUnitGroup(self, short_name: str) -> UnitGroup:

        if not self.IsElementExists(short_name, UnitGroup):
            unit_group = UnitGroup(self, short_name)
            self.addElement(unit_group)
        return self.getElement(short_name, UnitGroup)

    def createEndToEndProtectionSet(self, short_name: str) -> EndToEndProtectionSet:

        if not self.IsElementExists(short_name, EndToEndProtectionSet):
            e2d_set = EndToEndProtectionSet(self, short_name)
            self.addElement(e2d_set)
        return self.getElement(short_name, EndToEndProtectionSet)

    def createApplicationArrayDataType(self, short_name: str) -> ApplicationArrayDataType:

        if not self.IsElementExists(short_name, ApplicationArrayDataType):
            data_type = ApplicationArrayDataType(self, short_name)
            self.addElement(data_type)
        return self.getElement(short_name, ApplicationArrayDataType)

    def createSwRecordLayout(self, short_name: str) -> SwRecordLayout:

        if not self.IsElementExists(short_name, SwRecordLayout):
            layout = SwRecordLayout(self, short_name)
            self.addElement(layout)
        return self.getElement(short_name, SwRecordLayout)

    def createSwAddrMethod(self, short_name: str) -> SwAddrMethod:

        if not self.IsElementExists(short_name, SwAddrMethod):
            method = SwAddrMethod(self, short_name)
            self.addElement(method)
        return self.getElement(short_name, SwAddrMethod)

    def createTriggerInterface(self, short_name: str) -> TriggerInterface:

        if not self.IsElementExists(short_name, TriggerInterface):
            trigger_interface = TriggerInterface(self, short_name)
            self.addElement(trigger_interface)
        return self.getElement(short_name, TriggerInterface)

    def createDataPrototypeGroup(self, short_name: str) -> DataPrototypeGroup:

        if not self.IsElementExists(short_name, DataPrototypeGroup):
            data_group = DataPrototypeGroup(self, short_name)
            self.addElement(data_group)
        return self.getElement(short_name, DataPrototypeGroup)

    def createRunnableEntityGroup(self, short_name: str) -> RunnableEntityGroup:

        if not self.IsElementExists(short_name, RunnableEntityGroup):
            runnable_group = RunnableEntityGroup(self, short_name)
            self.addElement(runnable_group)
        return self.getElement(short_name, RunnableEntityGroup)

    def createConsistencyNeeds(self, short_name: str) -> ConsistencyNeeds:

        if not self.IsElementExists(short_name, ConsistencyNeeds):
            consistency_needs = ConsistencyNeeds(self, short_name)
            self.addElement(consistency_needs)
        return self.getElement(short_name, ConsistencyNeeds)

    def createModeDeclarationGroup(self, short_name: str) -> ModeDeclarationGroup:

        if not self.IsElementExists(short_name, ModeDeclarationGroup):
            group = ModeDeclarationGroup(self, short_name)
            self.addElement(group)
        return self.getElement(short_name, ModeDeclarationGroup)

    def createModeSwitchInterface(self, short_name: str) -> ModeSwitchInterface:

        if not self.IsElementExists(short_name, ModeSwitchInterface):
            switch_interface = ModeSwitchInterface(self, short_name)
            self.addElement(switch_interface)
        return self.getElement(short_name, ModeSwitchInterface)

    def createSwcTiming(self, short_name: str) -> SwcTiming:

        if not self.IsElementExists(short_name, SwcTiming):
            timing = SwcTiming(self, short_name)
            self.addElement(timing)
        return self.getElement(short_name, SwcTiming)

    def createLinCluster(self, short_name: str) -> LinCluster:

        if not self.IsElementExists(short_name, LinCluster):
            cluster = LinCluster(self, short_name)
            self.addElement(cluster)
        return self.getElement(short_name, LinCluster)

    def createCanCluster(self, short_name: str) -> CanCluster:

        if not self.IsElementExists(short_name, CanCluster):
            cluster = CanCluster(self, short_name)
            self.addElement(cluster)
        return self.getElement(short_name, CanCluster)

    def createJ1939Cluster(self, short_name: str) -> J1939Cluster:

        if not self.IsElementExists(short_name, J1939Cluster):
            cluster = J1939Cluster(self, short_name)
            self.addElement(cluster)
        return self.getElement(short_name, J1939Cluster)

    def createLinUnconditionalFrame(self, short_name: str) -> LinUnconditionalFrame:

        if not self.IsElementExists(short_name, LinUnconditionalFrame):
            frame = LinUnconditionalFrame(self, short_name)
            self.addElement(frame)
        return self.getElement(short_name, LinUnconditionalFrame)

    def createNmPdu(self, short_name: str) -> NmPdu:

        if not self.IsElementExists(short_name, NmPdu):
            element = NmPdu(self, short_name)
            self.addElement(element)
        return self.getElement(short_name, NmPdu)

    def createNPdu(self, short_name: str) -> NPdu:

        if not self.IsElementExists(short_name, NPdu):
            element = NPdu(self, short_name)
            self.addElement(element)
        return self.getElement(short_name, NPdu)

    def createDcmIPdu(self, short_name: str) -> DcmIPdu:

        if not self.IsElementExists(short_name, DcmIPdu):
            element = DcmIPdu(self, short_name)
            self.addElement(element)
        return self.getElement(short_name, DcmIPdu)

    def createSecuredIPdu(self, short_name: str) -> SecuredIPdu:

        if not self.IsElementExists(short_name, SecuredIPdu):
            element = SecuredIPdu(self, short_name)
            self.addElement(element)
        return self.getElement(short_name, SecuredIPdu)

    def createNmConfig(self, short_name: str) -> NmConfig:

        if not self.IsElementExists(short_name, NmConfig):
            element = NmConfig(self, short_name)
            self.addElement(element)
        return self.getElement(short_name, NmConfig)

    def createCanTpConfig(self, short_name: str) -> CanTpConfig:

        if not self.IsElementExists(short_name, CanTpConfig):
            element = CanTpConfig(self, short_name)
            self.addElement(element)
        return self.getElement(short_name, CanTpConfig)

    def createLinTpConfig(self, short_name: str) -> LinTpConfig:

        if not self.IsElementExists(short_name, LinTpConfig):
            element = LinTpConfig(self, short_name)
            self.addElement(element)
        return self.getElement(short_name, LinTpConfig)

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

        if not self.IsElementExists(short_name, CanFrame):
            element = CanFrame(self, short_name)
            self.addElement(element)
        return self.getElement(short_name, CanFrame)

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

        if not self.IsElementExists(short_name, EcuInstance):
            element = EcuInstance(self, short_name)
            self.addElement(element)
        return self.getElement(short_name, EcuInstance)

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

        if not self.IsElementExists(short_name, ConsumedProvidedServiceInstanceGroup):
            element = ConsumedProvidedServiceInstanceGroup(self, short_name)
            self.addElement(element)
        return self.getElement(short_name, ConsumedProvidedServiceInstanceGroup)

    def createGateway(self, short_name: str) -> Gateway:

        if not self.IsElementExists(short_name, Gateway):
            element = Gateway(self, short_name)
            self.addElement(element)
        return self.getElement(short_name, Gateway)

    def createISignal(self, short_name: str) -> ISignal:

        if not self.IsElementExists(short_name, ISignal):
            element = ISignal(self, short_name)
            self.addElement(element)
        return self.getElement(short_name, ISignal)

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

        if not self.IsElementExists(short_name, SystemSignal):
            element = SystemSignal(self, short_name)
            self.addElement(element)
        return self.getElement(short_name, SystemSignal)

    def createSystemSignalGroup(self, short_name: str) -> SystemSignalGroup:

        if not self.IsElementExists(short_name, SystemSignalGroup):
            element = SystemSignalGroup(self, short_name)
            self.addElement(element)
        return self.getElement(short_name, SystemSignalGroup)

    def createSignalServiceTranslationPropsSet(self, short_name: str) -> SignalServiceTranslationPropsSet:

        if not self.IsElementExists(short_name, SignalServiceTranslationPropsSet):
            element = SignalServiceTranslationPropsSet(self, short_name)
            self.addElement(element)
        return self.getElement(short_name, SignalServiceTranslationPropsSet)

    def createISignalIPdu(self, short_name: str) -> ISignalIPdu:

        if not self.IsElementExists(short_name, ISignalIPdu):
            element = ISignalIPdu(self, short_name)
            self.addElement(element)
        return self.getElement(short_name, ISignalIPdu)

    def createEcucValueCollection(self, short_name: str) -> EcucValueCollection:

        if not self.IsElementExists(short_name, EcucValueCollection):
            element = EcucValueCollection(self, short_name)
            self.addElement(element)
        return self.getElement(short_name, EcucValueCollection)

    def createEthTcpIpProps(self, short_name: str) -> EthTcpIpProps:

        if not self.IsElementExists(short_name, EthTcpIpProps):
            props = EthTcpIpProps(self, short_name)
            self.addElement(props)
        return self.getElement(short_name, EthTcpIpProps)

    def createEthTcpIpIcmpProps(self, short_name: str) -> EthTcpIpIcmpProps:

        if not self.IsElementExists(short_name, EthTcpIpIcmpProps):
            props = EthTcpIpIcmpProps(self, short_name)
            self.addElement(props)
        return self.getElement(short_name, EthTcpIpIcmpProps)

    def createOsTaskProxy(self, short_name: str) -> OsTaskProxy:

        if not self.IsElementExists(short_name, OsTaskProxy):
            proxy = OsTaskProxy(self, short_name)
            self.addElement(proxy)
        return self.getElement(short_name, OsTaskProxy)

    def createModuleConfiguration(self, short_name: str) -> ModuleConfiguration:

        if not self.IsElementExists(short_name, ModuleConfiguration):
            module_configuration = ModuleConfiguration(self, short_name)
            self.addElement(module_configuration)
        return self.getElement(short_name, ModuleConfiguration)

    def createEcucModuleConfigurationValues(self, short_name: str) -> EcucModuleConfigurationValues:

        if not self.IsElementExists(short_name, EcucModuleConfigurationValues):
            element = EcucModuleConfigurationValues(self, short_name)
            self.addElement(element)
        return self.getElement(short_name, EcucModuleConfigurationValues)

    def createEcucModuleDef(self, short_name: str) -> EcucModuleDef:

        if not self.IsElementExists(short_name, EcucModuleDef):
            element = EcucModuleDef(self, short_name)
            self.addElement(element)
        return self.getElement(short_name, EcucModuleDef)

    def createEcucDefinitionCollection(self, short_name: str) -> EcucDefinitionCollection:

        if not self.IsElementExists(short_name, EcucDefinitionCollection):
            element = EcucDefinitionCollection(self, short_name)
            self.addElement(element)
        return self.getElement(short_name, EcucDefinitionCollection)

    def createEcucDestinationUriDefSet(self, short_name: str) -> EcucDestinationUriDefSet:

        if not self.IsElementExists(short_name, EcucDestinationUriDefSet):
            element = EcucDestinationUriDefSet(self, short_name)
            self.addElement(element)
        return self.getElement(short_name, EcucDestinationUriDefSet)

    def createSwSystemConst(self, short_name: str) -> SwSystemconst:

        if not self.IsElementExists(short_name, SwSystemconst):
            element = SwSystemconst(self, short_name)
            self.addElement(element)
        return self.getElement(short_name, SwSystemconst)

    def createSwSystemconstantValueSet(self, short_name: str) -> SwSystemconstantValueSet:

        if not self.IsElementExists(short_name, SwSystemconstantValueSet):
            element = SwSystemconstantValueSet(self, short_name)
            self.addElement(element)
        return self.getElement(short_name, SwSystemconstantValueSet)

    def createEvaluatedVariantSet(self, short_name: str) -> EvaluatedVariantSet:

        if not self.IsElementExists(short_name, EvaluatedVariantSet):
            element = EvaluatedVariantSet(self, short_name)
            self.addElement(element)
        return self.getElement(short_name, EvaluatedVariantSet)

    def createSdgDef(self, short_name: str) -> SdgDef:

        if not self.IsElementExists(short_name, SdgDef):
            element = SdgDef(self, short_name)
            self.addElement(element)
        return self.getElement(short_name, SdgDef)

    def createPredefinedVariant(self, short_name: str) -> PredefinedVariant:

        if not self.IsElementExists(short_name, PredefinedVariant):
            element = PredefinedVariant(self, short_name)
            self.addElement(element)
        return self.getElement(short_name, PredefinedVariant)

    def createPostBuildVariantCriterion(self, short_name: str) -> PostBuildVariantCriterion:

        if not self.IsElementExists(short_name, PostBuildVariantCriterion):
            element = PostBuildVariantCriterion(self, short_name)
            self.addElement(element)
        return self.getElement(short_name, PostBuildVariantCriterion)

    def createPhysicalDimension(self, short_name: str) -> PhysicalDimension:

        if not self.IsElementExists(short_name, PhysicalDimension):
            element = PhysicalDimension(self, short_name)
            self.addElement(element)
        return self.getElement(short_name, PhysicalDimension)

    def createISignalGroup(self, short_name: str) -> ISignalGroup:

        if not self.IsElementExists(short_name, ISignalGroup):
            element = ISignalGroup(self, short_name)
            self.addElement(element)
        return self.getElement(short_name, ISignalGroup)

    def createISignalIPduGroup(self, short_name: str) -> ISignalIPduGroup:

        if not self.IsElementExists(short_name, ISignalIPduGroup):
            element = ISignalIPduGroup(self, short_name)
            self.addElement(element)
        return self.getElement(short_name, ISignalIPduGroup)

    def createPdurIPduGroup(self, short_name: str) -> PdurIPduGroup:

        if not self.IsElementExists(short_name, PdurIPduGroup):
            element = PdurIPduGroup(self, short_name)
            self.addElement(element)
        return self.getElement(short_name, PdurIPduGroup)

    def createClientIdDefinitionSet(self, short_name: str) -> ClientIdDefinitionSet:

        if not self.IsElementExists(short_name, ClientIdDefinitionSet):
            element = ClientIdDefinitionSet(self, short_name)
            self.addElement(element)
        return self.getElement(short_name, ClientIdDefinitionSet)

    def createInterpolationRoutineMappingSet(self, short_name: str) -> InterpolationRoutineMappingSet:

        if not self.IsElementExists(short_name, InterpolationRoutineMappingSet):
            element = InterpolationRoutineMappingSet(self, short_name)
            self.addElement(element)
        return self.getElement(short_name, InterpolationRoutineMappingSet)

    def createCpSoftwareCluster(self, short_name: str) -> CpSoftwareCluster:

        if not self.IsElementExists(short_name, CpSoftwareCluster):
            element = CpSoftwareCluster(self, short_name)
            self.addElement(element)
        return self.getElement(short_name, CpSoftwareCluster)

    def createSystem(self, short_name: str) -> System:

        if not self.IsElementExists(short_name, System):
            element = System(self, short_name)
            self.addElement(element)
        return self.getElement(short_name, System)

    def createFlatMap(self, short_name: str) -> FlatMap:

        if not self.IsElementExists(short_name, FlatMap):
            map = FlatMap(self, short_name)
            self.addElement(map)
        return self.getElement(short_name, FlatMap)

    def createBuildActionManifest(self, short_name: str) -> BuildActionManifest:
        if not self.IsElementExists(short_name, BuildActionManifest):
            manifest = BuildActionManifest(self, short_name)
            self.addElement(manifest)
        return self.getElement(short_name, BuildActionManifest)

    def createPortInterfaceMappingSet(self, short_name: str) -> PortInterfaceMappingSet:

        if not self.IsElementExists(short_name, PortInterfaceMappingSet):
            map_set = PortInterfaceMappingSet(self, short_name)
            self.addElement(map_set)
        return self.getElement(short_name, PortInterfaceMappingSet)

    def createEthernetCluster(self, short_name: str) -> EthernetCluster:

        if not self.IsElementExists(short_name, EthernetCluster):
            cluster = EthernetCluster(self, short_name)
            self.addElement(cluster)
        return self.getElement(short_name, EthernetCluster)

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
        if not self.IsElementExists(short_name, DiagnosticAuthRole):
            auth_role = DiagnosticAuthRole(self, short_name)
            self.addElement(auth_role)
        return self.getElement(short_name, DiagnosticAuthRole)

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
        if not self.IsElementExists(short_name, DiagnosticAuthenticationClass):
            authentication_class = DiagnosticAuthenticationClass(self, short_name)
            self.addElement(authentication_class)
        return self.getElement(short_name, DiagnosticAuthenticationClass)

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
        if not self.IsElementExists(short_name, DiagnosticAuthenticationConfiguration):
            configuration = DiagnosticAuthenticationConfiguration(self, short_name)
            self.addElement(configuration)
        return self.getElement(short_name, DiagnosticAuthenticationConfiguration)

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
        if not self.IsElementExists(short_name, DiagnosticAuthTransmitCertificate):
            certificate = DiagnosticAuthTransmitCertificate(self, short_name)
            self.addElement(certificate)
        return self.getElement(short_name, DiagnosticAuthTransmitCertificate)

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
        if not self.IsElementExists(short_name, DiagnosticDeAuthentication):
            de_authentication = DiagnosticDeAuthentication(self, short_name)
            self.addElement(de_authentication)
        return self.getElement(short_name, DiagnosticDeAuthentication)

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
        if not self.IsElementExists(short_name, DiagnosticProofOfOwnership):
            proof_of_ownership = DiagnosticProofOfOwnership(self, short_name)
            self.addElement(proof_of_ownership)
        return self.getElement(short_name, DiagnosticProofOfOwnership)

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
        if not self.IsElementExists(short_name, DiagnosticVerifyCertificateBidirectional):
            verification = DiagnosticVerifyCertificateBidirectional(self, short_name)
            self.addElement(verification)
        return self.getElement(short_name, DiagnosticVerifyCertificateBidirectional)

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
        if not self.IsElementExists(short_name, DiagnosticVerifyCertificateUnidirectional):
            verification = DiagnosticVerifyCertificateUnidirectional(self, short_name)
            self.addElement(verification)
        return self.getElement(short_name, DiagnosticVerifyCertificateUnidirectional)

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
        if not self.IsElementExists(short_name, DiagnosticComControl):
            com_control = DiagnosticComControl(self, short_name)
            self.addElement(com_control)
        return self.getElement(short_name, DiagnosticComControl)

    def createDiagnosticConnection(self, short_name: str) -> DiagnosticConnection:

        if not self.IsElementExists(short_name, DiagnosticConnection):
            connection = DiagnosticConnection(self, short_name)
            self.addElement(connection)
        return self.getElement(short_name, DiagnosticConnection)

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
        if not self.IsElementExists(short_name, DiagnosticContributionSet):
            contribution_set = DiagnosticContributionSet(self, short_name)
            self.addElement(contribution_set)
        return self.getElement(short_name, DiagnosticContributionSet)

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
        if not self.IsElementExists(short_name, DiagnosticCustomServiceClass):
            custom_service_class = DiagnosticCustomServiceClass(self, short_name)
            self.addElement(custom_service_class)
        return self.getElement(short_name, DiagnosticCustomServiceClass)

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
        if not self.IsElementExists(short_name, DiagnosticCustomServiceInstance):
            custom_service_instance = DiagnosticCustomServiceInstance(self, short_name)
            self.addElement(custom_service_instance)
        return self.getElement(short_name, DiagnosticCustomServiceInstance)

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
        if not self.IsElementExists(short_name, DiagnosticProtocol):
            protocol = DiagnosticProtocol(self, short_name)
            self.addElement(protocol)
        return self.getElement(short_name, DiagnosticProtocol)

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

        if not self.IsElementExists(short_name, DiagnosticServiceTable):
            table = DiagnosticServiceTable(self, short_name)
            self.addElement(table)
        return self.getElement(short_name, DiagnosticServiceTable)

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
        if not self.IsElementExists(short_name, DiagnosticSession):
            session = DiagnosticSession(self, short_name)
            self.addElement(session)
        return self.getElement(short_name, DiagnosticSession)

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
        if not self.IsElementExists(short_name, DiagnosticSessionControl):
            session_control = DiagnosticSessionControl(self, short_name)
            self.addElement(session_control)
        return self.getElement(short_name, DiagnosticSessionControl)

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
        if not self.IsElementExists(short_name, DiagnosticSessionControlClass):
            session_control_class = DiagnosticSessionControlClass(self, short_name)
            self.addElement(session_control_class)
        return self.getElement(short_name, DiagnosticSessionControlClass)

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
        if not self.IsElementExists(short_name, DiagnosticSecurityAccess):
            security_access = DiagnosticSecurityAccess(self, short_name)
            self.addElement(security_access)
        return self.getElement(short_name, DiagnosticSecurityAccess)

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
        if not self.IsElementExists(short_name, DiagnosticSecurityAccessClass):
            security_access_class = DiagnosticSecurityAccessClass(self, short_name)
            self.addElement(security_access_class)
        return self.getElement(short_name, DiagnosticSecurityAccessClass)

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
        if not self.IsElementExists(short_name, DiagnosticSecurityLevel):
            security_level = DiagnosticSecurityLevel(self, short_name)
            self.addElement(security_level)
        return self.getElement(short_name, DiagnosticSecurityLevel)

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
        if not self.IsElementExists(short_name, DiagnosticDataIdentifier):
            did = DiagnosticDataIdentifier(self, short_name)
            self.addElement(did)
        return self.getElement(short_name, DiagnosticDataIdentifier)

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
        if not self.IsElementExists(short_name, DiagnosticDynamicDataIdentifier):
            did = DiagnosticDynamicDataIdentifier(self, short_name)
            self.addElement(did)
        return self.getElement(short_name, DiagnosticDynamicDataIdentifier)

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
        if not self.IsElementExists(short_name, DiagnosticEcuReset):
            ecu_reset = DiagnosticEcuReset(self, short_name)
            self.addElement(ecu_reset)
        return self.getElement(short_name, DiagnosticEcuReset)

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
        if not self.IsElementExists(short_name, DiagnosticEcuResetClass):
            ecu_reset_class = DiagnosticEcuResetClass(self, short_name)
            self.addElement(ecu_reset_class)
        return self.getElement(short_name, DiagnosticEcuResetClass)

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
        if not self.IsElementExists(short_name, DiagnosticEnvironmentalCondition):
            condition = DiagnosticEnvironmentalCondition(self, short_name)
            self.addElement(condition)
        return self.getElement(short_name, DiagnosticEnvironmentalCondition)

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
        if not self.IsElementExists(short_name, DiagnosticFimEventGroup):
            fim_event_group = DiagnosticFimEventGroup(self, short_name)
            self.addElement(fim_event_group)
        return self.getElement(short_name, DiagnosticFimEventGroup)

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
        if not self.IsElementExists(short_name, DiagnosticJ1939Spn):
            j1939_spn = DiagnosticJ1939Spn(self, short_name)
            self.addElement(j1939_spn)
        return self.getElement(short_name, DiagnosticJ1939Spn)

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
        if not self.IsElementExists(short_name, DiagnosticAccessPermission):
            permission = DiagnosticAccessPermission(self, short_name)
            self.addElement(permission)
        return self.getElement(short_name, DiagnosticAccessPermission)

    def createDltContext(self, short_name: str) -> DltContext:

        if not self.IsElementExists(short_name, DltContext):
            context = DltContext(self, short_name)
            self.addElement(context)
        return self.getElement(short_name, DltContext)

    def createDltEcu(self, short_name: str) -> DltEcu:

        if not self.IsElementExists(short_name, DltEcu):
            ecu = DltEcu(self, short_name)
            self.addElement(ecu)
        return self.getElement(short_name, DltEcu)

    def createMultiplexedIPdu(self, short_name: str) -> MultiplexedIPdu:

        if not self.IsElementExists(short_name, MultiplexedIPdu):
            ipdu = MultiplexedIPdu(self, short_name)
            self.addElement(ipdu)
        return self.getElement(short_name, MultiplexedIPdu)

    def createUserDefinedIPdu(self, short_name: str) -> UserDefinedIPdu:

        if not self.IsElementExists(short_name, UserDefinedIPdu):
            ipdu = UserDefinedIPdu(self, short_name)
            self.addElement(ipdu)
        return self.getElement(short_name, UserDefinedIPdu)

    def createUserDefinedPdu(self, short_name: str) -> UserDefinedPdu:

        if not self.IsElementExists(short_name, UserDefinedPdu):
            pdu = UserDefinedPdu(self, short_name)
            self.addElement(pdu)
        return self.getElement(short_name, UserDefinedPdu)

    def createGeneralPurposeIPdu(self, short_name: str) -> GeneralPurposeIPdu:

        if not self.IsElementExists(short_name, GeneralPurposeIPdu):
            i_pdu = GeneralPurposeIPdu(self, short_name)
            self.addElement(i_pdu)
        return self.getElement(short_name, GeneralPurposeIPdu)

    def createGeneralPurposePdu(self, short_name: str) -> GeneralPurposePdu:

        if not self.IsElementExists(short_name, GeneralPurposePdu):
            pdu = GeneralPurposePdu(self, short_name)
            self.addElement(pdu)
        return self.getElement(short_name, GeneralPurposePdu)

    def createSecureCommunicationPropsSet(self, short_name: str) -> SecureCommunicationPropsSet:

        if not self.IsElementExists(short_name, SecureCommunicationPropsSet):
            props_set = SecureCommunicationPropsSet(self, short_name)
            self.addElement(props_set)
        return self.getElement(short_name, SecureCommunicationPropsSet)

    def createSoAdRoutingGroup(self, short_name: str) -> SoAdRoutingGroup:

        if not self.IsElementExists(short_name, SoAdRoutingGroup):
            group = SoAdRoutingGroup(self, short_name)
            self.addElement(group)
        return self.getElement(short_name, SoAdRoutingGroup)

    def createTcpOptionFilterSet(self, short_name: str) -> TcpOptionFilterSet:

        if not self.IsElementExists(short_name, TcpOptionFilterSet):
            tcp_option_filter_set = TcpOptionFilterSet(self, short_name)
            self.addElement(tcp_option_filter_set)
        return self.getElement(short_name, TcpOptionFilterSet)

    def createCanXlProps(self, short_name: str) -> CanXlProps:

        if not self.IsElementExists(short_name, CanXlProps):
            can_xl_props = CanXlProps(self, short_name)
            self.addElement(can_xl_props)
        return self.getElement(short_name, CanXlProps)

    def createSomeipSdClientServiceInstanceConfig(self, short_name: str) -> SomeipSdClientServiceInstanceConfig:

        if not self.IsElementExists(short_name, SomeipSdClientServiceInstanceConfig):
            config = SomeipSdClientServiceInstanceConfig(self, short_name)
            self.addElement(config)
        return self.getElement(short_name, SomeipSdClientServiceInstanceConfig)

    def createSomeipSdClientEventGroupTimingConfig(self, short_name: str) -> SomeipSdClientEventGroupTimingConfig:

        if not self.IsElementExists(short_name, SomeipSdClientEventGroupTimingConfig):
            config = SomeipSdClientEventGroupTimingConfig(self, short_name)
            self.addElement(config)
        return self.getElement(short_name, SomeipSdClientEventGroupTimingConfig)

    def createSomeipSdServerEventGroupTimingConfig(self, short_name: str) -> SomeipSdServerEventGroupTimingConfig:

        if not self.IsElementExists(short_name, SomeipSdServerEventGroupTimingConfig):
            config = SomeipSdServerEventGroupTimingConfig(self, short_name)
            self.addElement(config)
        return self.getElement(short_name, SomeipSdServerEventGroupTimingConfig)

    def createDoIpTpConfig(self, short_name: str) -> DoIpTpConfig:

        if not self.IsElementExists(short_name, DoIpTpConfig):
            tp_config = DoIpTpConfig(self, short_name)
            self.addElement(tp_config)
        return self.getElement(short_name, DoIpTpConfig)

    def createHwElement(self, short_name: str) -> HwElement:

        if not self.IsElementExists(short_name, HwElement):
            hw_element = HwElement(self, short_name)
            self.addElement(hw_element)
        return self.getElement(short_name, HwElement)

    def createHwCategory(self, short_name: str) -> HwCategory:

        if not self.IsElementExists(short_name, HwCategory):
            hw_category = HwCategory(self, short_name)
            self.addElement(hw_category)
        return self.getElement(short_name, HwCategory)

    def createHwType(self, short_name: str) -> HwType:

        if not self.IsElementExists(short_name, HwType):
            hw_category = HwType(self, short_name)
            self.addElement(hw_category)
        return self.getElement(short_name, HwType)

    def createFlexrayFrame(self, short_name: str) -> FlexrayFrame:

        if not self.IsElementExists(short_name, FlexrayFrame):
            frame = FlexrayFrame(self, short_name)
            self.addElement(frame)
        return self.getElement(short_name, FlexrayFrame)

    def createFlexrayCluster(self, short_name: str) -> FlexrayCluster:

        if not self.IsElementExists(short_name, FlexrayCluster):
            frame = FlexrayCluster(self, short_name)
            self.addElement(frame)
        return self.getElement(short_name, FlexrayCluster)

    def createDataTransformationSet(self, short_name: str) -> DataTransformationSet:

        if not self.IsElementExists(short_name, DataTransformationSet):
            transform_set = DataTransformationSet(self, short_name)
            self.addElement(transform_set)
        return self.getElement(short_name, DataTransformationSet)

    def createE2EProfileCompatibilityProps(self, short_name: str) -> E2EProfileCompatibilityProps:

        if not self.IsElementExists(short_name, E2EProfileCompatibilityProps):
            props = E2EProfileCompatibilityProps(self, short_name)
            self.addElement(props)
        return self.getElement(short_name, E2EProfileCompatibilityProps)

    def createTlvDataIdDefinitionSet(self, short_name: str) -> TlvDataIdDefinitionSet:

        if not self.IsElementExists(short_name, TlvDataIdDefinitionSet):
            tlv_data_id_definition_set = TlvDataIdDefinitionSet(self, short_name)
            self.addElement(tlv_data_id_definition_set)
        return self.getElement(short_name, TlvDataIdDefinitionSet)

    def createCollection(self, short_name: str) -> Collection:
        from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ElementCollection import Collection

        if not self.IsElementExists(short_name, Collection):
            collection = Collection(self, short_name)
            self.addElement(collection)
        return self.getElement(short_name, Collection)

    def createKeywordSet(self, short_name: str) -> KeywordSet:

        if not self.IsElementExists(short_name, KeywordSet):
            keyword_set = KeywordSet(self, short_name)
            self.addElement(keyword_set)
        return self.getElement(short_name, KeywordSet)

    def createPortPrototypeBlueprint(self, short_name: str) -> PortPrototypeBlueprint:

        if not self.IsElementExists(short_name, PortPrototypeBlueprint):
            keyword_set = PortPrototypeBlueprint(self, short_name)
            self.addElement(keyword_set)
        return self.getElement(short_name, PortPrototypeBlueprint)

    def createModeDeclarationMappingSet(self, short_name: str) -> ModeDeclarationMappingSet:

        if not self.IsElementExists(short_name, ModeDeclarationMappingSet):
            mapping_set = ModeDeclarationMappingSet(self, short_name)
            self.addElement(mapping_set)
        return self.getElement(short_name, ModeDeclarationMappingSet)

    def createAclPermission(self, short_name: str) -> AclPermission:

        if not self.IsElementExists(short_name, AclPermission):
            acl_permission = AclPermission(self, short_name)
            self.addElement(acl_permission)
        return self.getElement(short_name, AclPermission)

    def createAclObjectSet(self, short_name: str) -> AclObjectSet:

        if not self.IsElementExists(short_name, AclObjectSet):
            acl_object_set = AclObjectSet(self, short_name)
            self.addElement(acl_object_set)
        return self.getElement(short_name, AclObjectSet)

    def createAclOperation(self, short_name: str) -> AclOperation:

        if not self.IsElementExists(short_name, AclOperation):
            acl_operation = AclOperation(self, short_name)
            self.addElement(acl_operation)
        return self.getElement(short_name, AclOperation)

    def createAclRole(self, short_name: str) -> AclRole:

        if not self.IsElementExists(short_name, AclRole):
            acl_role = AclRole(self, short_name)
            self.addElement(acl_role)
        return self.getElement(short_name, AclRole)

    def createLifeCycleStateDefinitionGroup(self, short_name: str) -> LifeCycleStateDefinitionGroup:

        if not self.IsElementExists(short_name, LifeCycleStateDefinitionGroup):
            group = LifeCycleStateDefinitionGroup(self, short_name)
            self.addElement(group)
        return self.getElement(short_name, LifeCycleStateDefinitionGroup)

    def createViewMapSet(self, short_name: str) -> ViewMapSet:

        if not self.IsElementExists(short_name, ViewMapSet):
            view_map_set = ViewMapSet(self, short_name)
            self.addElement(view_map_set)
        return self.getElement(short_name, ViewMapSet)

    def getApplicationPrimitiveDataTypes(self) -> List[ApplicationPrimitiveDataType]:

        return list(sorted(filter(lambda a: isinstance(a, ApplicationPrimitiveDataType), self.elements), key=lambda o: o.short_name))

    def getApplicationDataType(self) -> List[ApplicationDataType]:

        return list(sorted(filter(lambda a: isinstance(a, ApplicationDataType), self.elements), key=lambda o: o.short_name))

    def getImplementationDataTypes(self) -> List[ImplementationDataType]:

        return list(sorted(filter(lambda a: isinstance(a, ImplementationDataType), self.elements), key=lambda o: o.short_name))

    def getSwBaseTypes(self) -> List[SwBaseType]:

        return list(filter(lambda a: isinstance(a, SwBaseType), self.elements))

    def getSwComponentTypes(self) -> List[SwComponentType]:

        return list(filter(lambda a: isinstance(a, SwComponentType), self.elements))

    def getSensorActuatorSwComponentType(self) -> List[SensorActuatorSwComponentType]:

        return list(filter(lambda a: isinstance(a, SensorActuatorSwComponentType), self.elements))

    def getAtomicSwComponentTypes(self) -> List[AtomicSwComponentType]:

        return list(filter(lambda a: isinstance(a, AtomicSwComponentType), self.elements))

    def getCompositionSwComponentTypes(self) -> List[CompositionSwComponentType]:

        return list(filter(lambda a: isinstance(a, CompositionSwComponentType), self.elements))

    def getComplexDeviceDriverSwComponentTypes(self) -> List[ComplexDeviceDriverSwComponentType]:

        return list(sorted(filter(lambda a: isinstance(a, ComplexDeviceDriverSwComponentType), self.elements), key=lambda a: a.short_name))

    def getSenderReceiverInterfaces(self) -> List[SenderReceiverInterface]:

        return list(sorted(filter(lambda a: isinstance(a, SenderReceiverInterface), self.elements), key=lambda a: a.short_name))

    def getParameterInterfaces(self) -> List[ParameterInterface]:

        return list(sorted(filter(lambda a: isinstance(a, ParameterInterface), self.elements), key=lambda a: a.short_name))

    def getClientServerInterfaces(self) -> List[ClientServerInterface]:

        return list(sorted(filter(lambda a: isinstance(a, ClientServerInterface), self.elements), key=lambda a: a.short_name))

    def getDataTypeMappingSets(self) -> List[DataTypeMappingSet]:

        return list(sorted(filter(lambda a: isinstance(a, DataTypeMappingSet), self.elements), key=lambda a: a.short_name))

    def getCompuMethods(self) -> List[CompuMethod]:

        return list(filter(lambda a: isinstance(a, CompuMethod), self.elements))

    def getBswModuleDescriptions(self) -> List[BswModuleDescription]:

        return list(filter(lambda a: isinstance(a, BswModuleDescription), self.elements))

    def getBswModuleEntries(self) -> List[BswModuleEntry]:

        return list(filter(lambda a: isinstance(a, BswModuleEntry), self.elements))

    def getBswImplementations(self) -> List[BswImplementation]:

        return list(filter(lambda a: isinstance(a, BswImplementation), self.elements))

    def getSwcImplementations(self) -> List[SwcImplementation]:

        return list(filter(lambda a: isinstance(a, SwcImplementation), self.elements))

    def getImplementations(self) -> List[Implementation]:

        return list(filter(lambda a: isinstance(a, Implementation), self.elements))

    def getSwcBswMappings(self) -> List[SwcBswMapping]:

        return list(filter(lambda a: isinstance(a, SwcBswMapping), self.elements))

    def getBswEntryRelationshipSets(self) -> List[BswEntryRelationshipSet]:

        return list(filter(lambda a: isinstance(a, BswEntryRelationshipSet), self.elements))

    def getMcFunctions(self) -> List[McFunction]:
        """
        Gets the McFunction elements contained in this package.

        Returns:
            List of McFunction instances
        """

        return list(filter(lambda a: isinstance(a, McFunction), self.elements))

    def getMcGroups(self) -> List[McGroup]:
        """
        Gets the McGroup elements contained in this package.

        Returns:
            List of McGroup instances
        """

        return list(filter(lambda a: isinstance(a, McGroup), self.elements))

    def getConstantSpecifications(self) -> List[ConstantSpecification]:

        return list(filter(lambda a: isinstance(a, ConstantSpecification), self.elements))

    def getDataConstrs(self) -> List[DataConstr]:

        return list(filter(lambda a: isinstance(a, DataConstr), self.elements))

    def getUnits(self) -> List[Unit]:

        return list(filter(lambda a: isinstance(a, Unit), self.elements))

    def getUnitGroups(self) -> List[UnitGroup]:

        return list(filter(lambda a: isinstance(a, UnitGroup), self.elements))

    def getApplicationArrayDataTypes(self) -> List[ApplicationArrayDataType]:

        return list(sorted(filter(lambda a: isinstance(a, ApplicationArrayDataType), self.elements), key=lambda a: a.short_name))

    def getSwRecordLayouts(self) -> List[SwRecordLayout]:

        return list(sorted(filter(lambda a: isinstance(a, SwRecordLayout), self.elements), key=lambda a: a.short_name))

    def getSwAddrMethods(self) -> List[SwAddrMethod]:

        return list(sorted(filter(lambda a: isinstance(a, SwAddrMethod), self.elements), key=lambda a: a.short_name))

    def getTriggerInterfaces(self) -> List[TriggerInterface]:

        return list(sorted(filter(lambda a: isinstance(a, TriggerInterface), self.elements), key=lambda a: a.short_name))

    def getModeDeclarationGroups(self) -> List[ModeDeclarationGroup]:

        return list(sorted(filter(lambda a: isinstance(a, ModeDeclarationGroup), self.elements), key=lambda a: a.short_name))

    def getModeSwitchInterfaces(self) -> List[ModeSwitchInterface]:

        return list(sorted(filter(lambda a: isinstance(a, ModeSwitchInterface), self.elements), key=lambda a: a.short_name))

    def getSwcTimings(self) -> List[SwcTiming]:

        return list(sorted(filter(lambda a: isinstance(a, SwcTiming), self.elements), key=lambda a: a.short_name))

    def getLinClusters(self) -> List[LinCluster]:

        return list(sorted(filter(lambda a: isinstance(a, LinCluster), self.elements), key=lambda a: a.short_name))

    def getCanClusters(self) -> List[CanCluster]:

        return list(sorted(filter(lambda a: isinstance(a, CanCluster), self.elements), key=lambda a: a.short_name))

    def getLinUnconditionalFrames(self) -> List[LinUnconditionalFrame]:

        return list(sorted(filter(lambda a: isinstance(a, LinUnconditionalFrame), self.elements), key=lambda a: a.short_name))

    def getNmPdus(self) -> List[NmPdu]:

        return list(sorted(filter(lambda a: isinstance(a, NmPdu), self.elements), key=lambda a: a.short_name))

    def getNPdus(self) -> List[NPdu]:

        return list(sorted(filter(lambda a: isinstance(a, NPdu), self.elements), key=lambda a: a.short_name))

    def getDcmIPdus(self) -> List[DcmIPdu]:

        return list(sorted(filter(lambda a: isinstance(a, DcmIPdu), self.elements), key=lambda a: a.short_name))

    def getSecuredIPdus(self) -> List[SecuredIPdu]:

        return list(sorted(filter(lambda a: isinstance(a, SecuredIPdu), self.elements), key=lambda a: a.short_name))

    def getNmConfigs(self) -> List[NmConfig]:

        return list(sorted(filter(lambda a: isinstance(a, NmConfig), self.elements), key=lambda a: a.short_name))

    def getCanTpConfigs(self) -> List[CanTpConfig]:

        return list(sorted(filter(lambda a: isinstance(a, CanTpConfig), self.elements), key=lambda a: a.short_name))

    def getCanFrames(self) -> List[CanFrame]:

        return list(sorted(filter(lambda a: isinstance(a, CanFrame), self.elements), key=lambda a: a.short_name))

    def getEcuInstances(self) -> List[EcuInstance]:

        return list(sorted(filter(lambda a: isinstance(a, EcuInstance), self.elements), key=lambda a: a.short_name))

    def getGateways(self) -> List[Gateway]:

        return list(sorted(filter(lambda a: isinstance(a, Gateway), self.elements), key=lambda a: a.short_name))

    def getISignals(self) -> List[ISignal]:

        return list(sorted(filter(lambda a: isinstance(a, ISignal), self.elements), key=lambda a: a.short_name))

    def getEcucValueCollections(self) -> List[EcucValueCollection]:

        return list(sorted(filter(lambda a: isinstance(a, EcucValueCollection), self.elements), key=lambda a: a.short_name))

    def getEcucModuleConfigurationValues(self) -> List[EcucModuleConfigurationValues]:

        return list(sorted(filter(lambda a: isinstance(a, EcucModuleConfigurationValues), self.elements), key=lambda a: a.short_name))

    def getEcucModuleDefs(self) -> List[EcucModuleDef]:

        return list(sorted(filter(lambda a: isinstance(a, EcucModuleDef), self.elements), key=lambda a: a.short_name))

    def getEcucDefinitionCollections(self) -> List[EcucDefinitionCollection]:

        return list(sorted(filter(lambda a: isinstance(a, EcucDefinitionCollection), self.elements), key=lambda a: a.short_name))

    def getSwSystemConsts(self) -> List[SwSystemconst]:

        return list(sorted(filter(lambda a: isinstance(a, SwSystemconst), self.elements), key=lambda a: a.short_name))

    def getSwSystemconstantValueSets(self) -> List[SwSystemconstantValueSet]:

        return list(sorted(filter(lambda a: isinstance(a, SwSystemconstantValueSet), self.elements), key=lambda a: a.short_name))

    def getPredefinedVariants(self) -> List[PredefinedVariant]:

        return list(
            sorted(
                filter(lambda a: isinstance(a, PredefinedVariant), self.elements),
                key=lambda a: a.short_name,
            )
        )

    def getPostBuildVariantCriterions(self) -> List[PostBuildVariantCriterion]:

        return list(
            sorted(
                filter(lambda a: isinstance(a, PostBuildVariantCriterion), self.elements),
                key=lambda a: a.short_name,
            )
        )

    def getEcucPhysicalDimensions(self) -> List[PhysicalDimension]:

        return list(sorted(filter(lambda a: isinstance(a, PhysicalDimension), self.elements), key=lambda a: a.short_name))

    def getISignalGroups(self) -> List[ISignalGroup]:

        return list(sorted(filter(lambda a: isinstance(a, ISignalGroup), self.elements), key=lambda a: a.short_name))

    def getSystemSignals(self) -> List[SystemSignal]:

        return list(sorted(filter(lambda a: isinstance(a, SystemSignal), self.elements), key=lambda a: a.short_name))

    def getSystemSignalGroups(self) -> List[SystemSignalGroup]:

        return list(sorted(filter(lambda a: isinstance(a, SystemSignalGroup), self.elements), key=lambda a: a.short_name))

    def getISignalIPdus(self) -> List[ISignalIPdu]:

        return list(sorted(filter(lambda a: isinstance(a, ISignalIPdu), self.elements), key=lambda a: a.short_name))

    def getSystems(self) -> List[System]:

        return list(sorted(filter(lambda a: isinstance(a, System), self.elements), key=lambda a: a.short_name))

    def getHwElements(self) -> List[HwElement]:

        return list(sorted(filter(lambda a: isinstance(a, HwElement), self.elements), key=lambda a: a.short_name))

    def getHwCategories(self) -> List[HwCategory]:

        return list(sorted(filter(lambda a: isinstance(a, HwCategory), self.elements), key=lambda a: a.short_name))

    def getFlexrayFrames(self) -> List[FlexrayFrame]:

        return list(sorted(filter(lambda a: isinstance(a, FlexrayFrame), self.elements), key=lambda a: a.short_name))

    def getDataTransformationSets(self) -> List[DataTransformationSet]:

        return list(sorted(filter(lambda a: isinstance(a, DataTransformationSet), self.elements), key=lambda a: a.short_name))

    def getCollections(self) -> List[Collection]:
        from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ElementCollection import Collection

        return list(sorted(filter(lambda a: isinstance(a, Collection), self.elements), key=lambda a: a.short_name))

    def getKeywordSets(self) -> List[KeywordSet]:

        return list(sorted(filter(lambda a: isinstance(a, KeywordSet), self.elements), key=lambda a: a.short_name))

    def getPortPrototypeBlueprints(self) -> List[PortPrototypeBlueprint]:

        return list(sorted(filter(lambda a: isinstance(a, PortPrototypeBlueprint), self.elements), key=lambda a: a.short_name))

    def getModeDeclarationMappingSets(self) -> List[ModeDeclarationMappingSet]:

        return list(sorted(filter(lambda a: isinstance(a, ModeDeclarationMappingSet), self.elements), key=lambda a: a.short_name))

    def getAclPermissions(self) -> List[AclPermission]:

        return list(sorted(filter(lambda a: isinstance(a, AclPermission), self.elements), key=lambda a: a.short_name))

    def getAclObjectSets(self) -> List[AclObjectSet]:

        return list(sorted(filter(lambda a: isinstance(a, AclObjectSet), self.elements), key=lambda a: a.short_name))

    def getAclOperations(self) -> List[AclOperation]:

        return list(sorted(filter(lambda a: isinstance(a, AclOperation), self.elements), key=lambda a: a.short_name))

    def getAclRoles(self) -> List[AclRole]:

        return list(sorted(filter(lambda a: isinstance(a, AclRole), self.elements), key=lambda a: a.short_name))

    def getLifeCycleStateDefinitionGroups(self) -> List[LifeCycleStateDefinitionGroup]:

        return list(sorted(filter(lambda a: isinstance(a, LifeCycleStateDefinitionGroup), self.elements), key=lambda a: a.short_name))

    def getViewMapSets(self) -> List[ViewMapSet]:

        return list(sorted(filter(lambda a: isinstance(a, ViewMapSet), self.elements), key=lambda a: a.short_name))

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
from armodel.models.M2.AUTOSARTemplates.CommonStructure.SignalServiceTranslation import SignalServiceTranslationPropsSet  # noqa: E402
from armodel.models.M2.AUTOSARTemplates.CommonStructure.StandardizationTemplate.BlueprintDedicated.PortPrototypeBlueprint import PortPrototypeBlueprint  # noqa: E402
from armodel.models.M2.AUTOSARTemplates.CommonStructure.StandardizationTemplate.Keyword import KeywordSet  # noqa: E402
from armodel.models.M2.AUTOSARTemplates.CommonStructure.SwcBswMapping import SwcBswMapping  # noqa: E402
from armodel.models.M2.AUTOSARTemplates.CommonStructure.Timing.TimingExtensions import SwcTiming  # noqa: E402
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
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.MeasurementAndCalibration import InterpolationRoutineMappingSet  # noqa: E402
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.SwcImplementation import SwcImplementation  # noqa: E402
from armodel.models.M2.AUTOSARTemplates.SystemTemplate import ClientIdDefinitionSet, CpSoftwareCluster, System  # noqa: E402
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.DiagnosticConnection import DiagnosticConnection  # noqa: E402
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.RteEventToOsTaskMapping import OsTaskProxy  # noqa: E402
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Can.CanCommunication import CanFrame  # noqa: E402
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Can.CanTopology import CanXlProps, J1939Cluster  # noqa: E402
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Ethernet.EthernetFrame import GenericEthernetFrame  # noqa: E402
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Ethernet.EthernetTopology import EthTcpIpIcmpProps, EthernetCluster, EthTcpIpProps  # noqa: E402
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Ethernet.ObsoleteModel import SoAdRoutingGroup  # noqa: E402
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Ethernet.ServiceInstances import (  # noqa: E402
    ConsumedProvidedServiceInstanceGroup,
    SomeipSdClientEventGroupTimingConfig,
    SomeipSdClientServiceInstanceConfig,
    SomeipSdServerEventGroupTimingConfig,
)
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
    MultiplexedIPdu,
    NPdu,
    NmPdu,
    PdurIPduGroup,
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
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.NetworkManagement import NmConfig  # noqa: E402
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.SecureCommunication import (  # noqa: E402
    CryptoEllipticCurveProps,
    CryptoServiceCertificate,
    CryptoServicePrimitive,
    CryptoSignatureScheme,
    IPSecConfigProps,
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
from armodel.models.M2.AUTOSARTemplates.CommonStructure.StandardizationTemplate.AbstractBlueprintStructure import LifeCycleState  # noqa: E402
from armodel.models.M2.AUTOSARTemplates.GenericStructure.BuildActionManifest import BuildActionManifest  # noqa: E402

BuildActionManifest.__bases__ = (ARElement,)


class CalibrationParameterValueSet(ARElement):
    pass


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
    pass


class CpSwClusterResourceToDiagFunctionIdMapping(DiagnosticMapping):
    pass


class CpSwClusterToDiagEventMapping(DiagnosticMapping):
    pass


class CpSwClusterToDiagRoutineSubfunctionMapping(DiagnosticMapping):
    pass


class DataExchangePoint(ARElement):
    pass


class DiagnosticAbstractAliasEvent(ARElement, ABC):
    pass


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
    pass


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
        if not self.IsElementExists(short_name, DiagnosticAuthTransmitCertificateEvaluation):
            evaluation = DiagnosticAuthTransmitCertificateEvaluation(self, short_name)
            self.addElement(evaluation)
            self.certificateEvaluations.append(evaluation)
        return self.getElement(short_name, DiagnosticAuthTransmitCertificateEvaluation)


class DiagnosticAuthTransmitCertificateMapping(DiagnosticMapping):
    pass


class DiagnosticAuthenticationConfiguration(DiagnosticAuthentication):
    """This meta-class represents the subfunction to configure the authentication."""

    # DiagnosticAuthenticationConfiguration method parity checklist:
    # Spec: AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf, Table 4.53, p.99
    # Columns: impl / docstring / test / reader / writer / release   ([—] = no XML element)
    # [x] __init__  [x] impl  [x] docstring  [x] test  [—] reader  [—] writer  R23-11

    def __init__(self, parent: ARObject, short_name: str):
        super().__init__(parent, short_name)


class DiagnosticClearDiagnosticInformation(ARElement):
    pass


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


class DiagnosticCondition(ARElement, ABC):
    pass


class DiagnosticConditionGroup(ARElement, ABC):
    pass


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
    # [x] getElementRefs       [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
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


class DiagnosticDataByIdentifier(ARElement, ABC):
    pass


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


class DiagnosticDataIdentifierSet(ARElement):
    pass


class DiagnosticMemoryByAddress(ARElement, ABC):
    pass


class DiagnosticDataTransfer(DiagnosticMemoryByAddress):
    pass


class DiagnosticDeAuthentication(DiagnosticAuthentication):
    """This meta-class represents the subfunction to remove the authentication"""

    # DiagnosticDeAuthentication method parity checklist:
    # Spec: AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf, Table 4.56, p.100
    # Columns: impl / docstring / test / reader / writer / release   ([—] = no XML element)
    # [x] __init__  [x] impl  [x] docstring  [x] test  [x] reader  [x] writer  R23-11

    def __init__(self, parent: ARObject, short_name: str):
        super().__init__(parent, short_name)


class DiagnosticDemProvidedDataMapping(DiagnosticMapping):
    pass


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
    pass


class DiagnosticEcuInstanceProps(ARElement):
    pass


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
    pass


class DiagnosticEnableConditionGroup(DiagnosticConditionGroup):
    pass


class DiagnosticEvent(ARElement):
    pass


class DiagnosticSwMapping(DiagnosticMapping, ABC):
    pass


class DiagnosticEventPortMapping(DiagnosticSwMapping):
    pass


class DiagnosticEventToDebounceAlgorithmMapping(DiagnosticMapping):
    pass


class DiagnosticEventToEnableConditionGroupMapping(DiagnosticMapping):
    pass


class DiagnosticEventToOperationCycleMapping(DiagnosticMapping):
    pass


class DiagnosticEventToSecurityEventMapping(DiagnosticMapping):
    pass


class DiagnosticEventToStorageConditionGroupMapping(DiagnosticMapping):
    pass


class DiagnosticEventToTroubleCodeJ1939Mapping(DiagnosticMapping):
    pass


class DiagnosticEventToTroubleCodeUdsMapping(DiagnosticMapping):
    pass


class DiagnosticExtendedDataRecord(ARElement):
    pass


class DiagnosticFimAliasEvent(DiagnosticAbstractAliasEvent):
    pass


class DiagnosticFimAliasEventGroup(DiagnosticAbstractAliasEvent):
    pass


class DiagnosticFimAliasEventGroupMapping(DiagnosticMapping):
    pass


class DiagnosticFimAliasEventMapping(DiagnosticMapping):
    pass


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
    pass


class DiagnosticFunctionIdentifier(ARElement):
    pass


class DiagnosticIOControl(ARElement):
    pass


class DiagnosticIndicator(ARElement):
    pass


class DiagnosticInfoType(ARElement):
    pass


class DiagnosticIumpr(ARElement):
    pass


class DiagnosticIumprDenominatorGroup(ARElement):
    pass


class DiagnosticIumprGroup(ARElement):
    pass


class DiagnosticIumprToFunctionIdentifierMapping(DiagnosticMapping):
    pass


class DiagnosticJ1939ExpandedFreezeFrame(ARElement):
    pass


class DiagnosticJ1939FreezeFrame(ARElement):
    pass


class DiagnosticJ1939Node(ARElement):
    pass


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
    pass


class DiagnosticJ1939SwMapping(DiagnosticSwMapping):
    pass


class DiagnosticMasterToSlaveEventMapping(DiagnosticMapping):
    pass


class DiagnosticMeasurementIdentifier(ARElement):
    pass


class DiagnosticMemoryAddressableRangeAccess(DiagnosticMemoryByAddress, ABC):
    pass


class DiagnosticMemoryDestinationPrimary(ARElement):
    pass


class DiagnosticMemoryIdentifier(ARElement):
    pass


class DiagnosticOperationCycle(ARElement):
    pass


class DiagnosticOperationCyclePortMapping(DiagnosticSwMapping):
    pass


class DiagnosticParameterIdentifier(ARElement):
    pass


class DiagnosticPowertrainFreezeFrame(ARElement):
    pass


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
    pass


class DiagnosticReadDataByIdentifier(DiagnosticDataByIdentifier):
    pass


class DiagnosticReadDataByPeriodicID(ARElement):
    pass


class DiagnosticReadScalingDataByIdentifier(DiagnosticDataByIdentifier):
    pass


class DiagnosticRequestControlOfOnBoardDevice(ARElement):
    pass


class DiagnosticRequestDownload(DiagnosticMemoryAddressableRangeAccess):
    pass


class DiagnosticRequestEmissionRelatedDTCPermanentStatus(ARElement):
    pass


class DiagnosticRequestFileTransfer(ARElement):
    pass


class DiagnosticRequestOnBoardMonitoringTestResults(ARElement):
    pass


class DiagnosticRequestPowertrainFreezeFrameData(ARElement):
    pass


class DiagnosticRequestUpload(DiagnosticMemoryAddressableRangeAccess):
    pass


class DiagnosticRequestVehicleInfo(ARElement):
    pass


class DiagnosticResponseOnEvent(ARElement):
    pass


class DiagnosticRoutine(ARElement):
    pass


class DiagnosticRoutineControl(ARElement):
    pass


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
    pass


class DiagnosticServiceDataMapping(DiagnosticSwMapping):
    pass


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
    pass


class DiagnosticStorageConditionGroup(DiagnosticConditionGroup):
    pass


class DiagnosticStorageConditionPortMapping(DiagnosticSwMapping):
    pass


class DiagnosticTestResult(ARElement):
    pass


class DiagnosticTestRoutineIdentifier(ARElement):
    pass


class DiagnosticTransferExit(DiagnosticMemoryByAddress):
    pass


class DiagnosticTroubleCode(ARElement, ABC):
    pass


class DiagnosticTroubleCodeGroup(ARElement):
    pass


class DiagnosticTroubleCodeUdsToTroubleCodeObdMapping(DiagnosticMapping):
    pass


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
    pass


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
        if not self.IsElementExists(short_name, LifeCycleState):
            state = LifeCycleState(self, short_name)
            self.addElement(state)
            self.lcStates.append(state)
        return self.getElement(short_name, LifeCycleState)

    def getLcStates(self) -> List[LifeCycleState]:
        """
        Describes a single life cycle state of this life cycle state definition group.
        """
        return self.lcStates


class PhysicalDimensionMappingSet(ARElement):
    pass


class PostBuildVariantCriterionValueSet(ARElement):
    pass


class RapidPrototypingScenario(ARElement):
    pass



class SecurityEventContextMappingApplication(ARElement):
    pass


class SecurityEventContextMappingBswModule(ARElement):
    pass


class SecurityEventContextMappingFunctionalCluster(ARElement):
    pass


class SecurityEventDefinition(ARElement):
    pass


class SwAxisType(ARElement):
    pass


class ApplicationPartition(ARElement):
    pass


class BswCompositionTiming(ARElement):
    pass


class BswModuleTiming(ARElement):
    pass


class CpSoftwareClusterBinaryManifestDescriptor(ARElement):
    pass


class CpSoftwareClusterMappingSet(ARElement):
    pass


class CpSoftwareClusterResourcePool(ARElement):
    pass


class CryptoServiceKey(ARElement):
    pass


class CryptoServiceQueue(ARElement):
    pass


class DdsCpConfig(ARElement):
    pass


class EcuTiming(ARElement):
    pass


class EthIpProps(ARElement):
    pass


class GeneralPurposeConnection(ARElement):
    pass


class GlobalTimeDomain(ARElement):
    pass


class IEEE1722TpConnection(ARElement, ABC):
    pass


class IPv6ExtHeaderFilterSet(ARElement):
    pass


class J1939ControllerApplication(ARElement):
    pass


class LogAndTraceMessageCollectionSet(ARElement):
    pass


class MacSecParticipantSet(ARElement):
    pass


class SocketConnectionIpduIdentifierSet(ARElement):
    pass


class TransformationPropsSet(ARElement):
    pass


class VfbTiming(ARElement):
    pass


class IEEE1722TpAcfConnection(IEEE1722TpConnection):
    pass


class IEEE1722TpAvConnection(IEEE1722TpConnection, ABC):
    pass


class IEEE1722TpAafConnection(IEEE1722TpAvConnection):
    pass


class IEEE1722TpCrfConnection(IEEE1722TpAvConnection):
    pass


class IEEE1722TpIidcConnection(IEEE1722TpAvConnection):
    pass


class IEEE1722TpRvfConnection(IEEE1722TpAvConnection):
    pass
