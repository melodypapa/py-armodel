"""
This module contains the ARPackage class and related classes for AUTOSAR models
in the GenericStructure module. ARPackage represents a hierarchical container for
organizing AUTOSAR elements according to the AUTOSAR standard. It serves as the
primary organizational unit for grouping related AUTOSAR model elements such as
components, interfaces, data types, and other packages.
"""

from __future__ import annotations
from typing import Dict, List, Optional
from typing import TYPE_CHECKING

from abc import ABC

if TYPE_CHECKING:
    from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ElementCollection import (
        Collection,
    )
    from armodel.models.M2.MSR.AsamHdo.BaseTypes import SwBaseType

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable import Referrable
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ElementCollection import CollectableElement


class PackageableElement(CollectableElement, ABC):
    """
    This meta-class specifies the ability to be a member of an AUTOSAR package.
    """

    # PackageableElement method parity checklist:
    # Spec: AUTOSAR_FO_TPS_GenericStructureTemplate.pdf, Table 4.2, p.54
    # Spec verified: R23-11
    # Columns: impl / docstring / test / reader / writer   ([—] = no XML element)
    # [x] __init__                     [x] impl  [x] docstring  [x] test  [—] reader  [—] writer
    #
    # Heritage fix (Rule 0001.2): Table 4.2 Base closure names CollectableElement as the
    # most-derived direct base, so PackageableElement re-parents from Identifiable to
    # CollectableElement. __init__ still forwards (parent, short_name) up the chain.

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
    "AdminData",
    "Annotation",
    "ApplicationArrayDataType",
    "ApplicationDataType",
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
    "DataConstr",
    "DataPrototypeGroup",
    "DataTransformationSet",
    "DataTypeMappingSet",
    "DcmIPdu",
    "DiagnosticConnection",
    "DiagnosticServiceTable",
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
    "TriggerInterface",
    "Unit",
    "UserDefinedIPdu",
    "UserDefinedPdu",
    "ARElement",
    "ARPackage",
    "PackageableElement",
    "ReferenceBase",
]


from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import CategoryString  # noqa: E402,F401


from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import Boolean, Identifier, RefType, ReferrableSubtypesEnum  # noqa: E402


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

    def addGlobalElement(self, value: ReferrableSubtypesEnum) -> "ReferenceBase":
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

    def addGlobalInPackageRef(self, value: RefType) -> "ReferenceBase":
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

    def setIsDefault(self, value: Optional[Boolean]) -> "ReferenceBase":
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

    def setPackageRef(self, value: Optional[RefType]) -> "ReferenceBase":
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

    def setShortLabel(self, value: Optional[Identifier]) -> "ReferenceBase":
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

    def setIsGlobal(self, value: Optional[Boolean]) -> "ReferenceBase":
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

    def setBaseIsThisPackage(self, value: Optional[Boolean]) -> "ReferenceBase":
        """
        This indicates that this base is established by the current package. In this case the association "package" can be derived as the qualified shortName of the enclosing package. If the value of baseIsThisPackage is set to true then one of the following must be true: • target of the association "package" must be the enclosing package. • association "package" is omitted. A None value is a no-op and does not overwrite an existing baseIsThisPackage.
        """
        if value is not None:
            self.baseIsThisPackage = value
        return self


class ARPackage(CollectableElement):
    """
    AUTOSAR package, allowing to create top level packages to structure the contained ARElements. ARPackages are open sets. This means that in a file based description system multiple files can be used to partially describe the contents of a package. This is an extended version of MSR's SW-SYSTEM.
    """

    # ARPackage method parity checklist:
    # Spec: AUTOSAR_FO_TPS_GenericStructureTemplate.pdf, Table 4.1, p.53
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
    # adminData, category, introduction, desc) are carried directly because the
    # Python base is CollectableElement; they belong to the Identifiable/Referrable
    # checklists.
    # Convenience factory accessors (createXxx/getXxxs) are pre-existing API for the
    # element aggregation; each concrete element class carries its own spec table
    # and checklist.

    def __init__(self, parent: ARObject, short_name: str):
        # Referrable/Identifiable members (parent, short_name, longName, annotations,
        # adminData, category, introduction, desc, uuid, variationPoint) and the
        # element-collection registry are inherited from CollectableElement -> Identifiable.
        super().__init__(parent, short_name)

        # This represents a sub package within an ARPackage, thus allowing for an unlimited package hierarchy.
        self.arPackages: Dict[str, "ARPackage"] = {}
        # This denotes the reference bases for the package. This is the basis for all relative references within the package. The base needs to be selected according to the base attribute within the references.
        self.referenceBases: List[ReferenceBase] = []

    def getARPackages(self) -> List["ARPackage"]:
        """
        This represents a sub package within an ARPackage, thus allowing for an unlimited package hierarchy.

        Returns:
            List of ARPackage instances sorted by short name
        """
        return list(sorted(self.arPackages.values(), key=lambda a: a.short_name))
        # return list(filter(lambda e: isinstance(e, ARPackage), self.elements))

    def createARPackage(self, short_name: str) -> "ARPackage":
        """
        This represents a sub package within an ARPackage, thus allowing for an unlimited package hierarchy. Creates a new sub-package with the given short name, or returns an existing package if one with the same name already exists.

        Args:
            short_name: The short name for the new sub-package

        Returns:
            The newly created or existing ARPackage instance
        """
        if short_name not in self.arPackages:
            ar_package = ARPackage(self, short_name)
            self.arPackages[short_name] = ar_package
        return self.arPackages[short_name]

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
            if short_name in self.arPackages:
                return self.arPackages[short_name]
        return CollectableElement.getElement(self, short_name, type)

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

    def createApplicationRecordDataType(self, short_name: str) -> ApplicationPrimitiveDataType:

        if not self.IsElementExists(short_name, ApplicationRecordDataType):
            data_type = ApplicationRecordDataType(self, short_name)
            self.addElement(data_type)
        return self.getElement(short_name, ApplicationRecordDataType)

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

    def createDiagnosticConnection(self, short_name: str) -> DiagnosticConnection:

        if not self.IsElementExists(short_name, DiagnosticConnection):
            connection = DiagnosticConnection(self, short_name)
            self.addElement(connection)
        return self.getElement(short_name, DiagnosticConnection)

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

    def createCollection(self, short_name: str) -> "Collection":
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

    def getCollections(self) -> List["Collection"]:
        from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ElementCollection import Collection

        return list(sorted(filter(lambda a: isinstance(a, Collection), self.elements), key=lambda a: a.short_name))

    def getKeywordSets(self) -> List[KeywordSet]:

        return list(sorted(filter(lambda a: isinstance(a, KeywordSet), self.elements), key=lambda a: a.short_name))

    def getPortPrototypeBlueprints(self) -> List[PortPrototypeBlueprint]:

        return list(sorted(filter(lambda a: isinstance(a, PortPrototypeBlueprint), self.elements), key=lambda a: a.short_name))

    def getModeDeclarationMappingSets(self) -> List[ModeDeclarationMappingSet]:

        return list(sorted(filter(lambda a: isinstance(a, ModeDeclarationMappingSet), self.elements), key=lambda a: a.short_name))

    def getReferenceBases(self) -> List[ReferenceBase]:
        """
        This denotes the reference bases for the package. This is the basis for all relative references within the package. The base needs to be selected according to the base attribute within the references.
        """
        return self.referenceBases

    def addReferenceBase(self, value: Optional[ReferenceBase]) -> "ARPackage":
        """
        This denotes the reference bases for the package. This is the basis for all relative references within the package. The base needs to be selected according to the base attribute within the references. A None value is a no-op and does not append to referenceBases.
        """
        if value is not None:
            self.referenceBases.append(value)
        return self


# Element-class names are re-exported eagerly. Every models/ module that imports
# from this module only needs ARElement/PackageableElement, which are defined above,
# so partial-module initialization resolves the cycle without lazy machinery.
from armodel.models.M2.AUTOSARTemplates.AdaptivePlatform.PlatformModuleDeployment.Firewall import FirewallRule, StateDependentFirewall  # noqa: E402
from armodel.models.M2.AUTOSARTemplates.BswModuleTemplate.BswImplementation import BswImplementation  # noqa: E402
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
from armodel.models.M2.AUTOSARTemplates.DiagnosticExtract.DiagnosticContribution import DiagnosticServiceTable  # noqa: E402
from armodel.models.M2.AUTOSARTemplates.ECUCDescriptionTemplate import (  # noqa: E402
    EcucModuleConfigurationValues,
    EcucValueCollection,
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
from armodel.models.M2.AUTOSARTemplates.GenericStructure.VariantHandling import (  # noqa: E402
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
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.SwcImplementation import SwcImplementation  # noqa: E402
from armodel.models.M2.AUTOSARTemplates.SystemTemplate import System  # noqa: E402
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.DiagnosticConnection import DiagnosticConnection  # noqa: E402
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Can.CanCommunication import CanFrame  # noqa: E402
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Can.CanTopology import CanXlProps  # noqa: E402
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Ethernet.EthernetFrame import GenericEthernetFrame  # noqa: E402
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Ethernet.EthernetTopology import EthernetCluster  # noqa: E402
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Ethernet.ObsoleteModel import SoAdRoutingGroup  # noqa: E402
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Ethernet.ServiceInstances import (  # noqa: E402
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
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Transformer import (  # noqa: E402
    DataTransformationSet,
    E2EProfileCompatibilityProps,
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

# Bind Collection's real base (ARElement) now that this module is fully defined. Collection is
# declared in ElementCollection with a placeholder base to avoid an import cycle: ElementCollection
# is imported for CollectableElement at class-definition time (PackageableElement re-parents to
# CollectableElement), and Collection's spec base ARElement lives here, so binding it here keeps
# both modules importable. After this, isinstance(coll, ARElement) holds.
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ElementCollection import Collection  # noqa: E402

Collection.__bases__ = (ARElement,)
