"""
This module contains the ARPackage class and related classes for AUTOSAR models
in the GenericStructure module. ARPackage represents a hierarchical container for
organizing AUTOSAR elements according to the AUTOSAR standard. It serves as the
primary organizational unit for grouping related AUTOSAR model elements such as
components, interfaces, data types, and other packages.
"""

from typing import (
    Any,
    Dict,
    List,
    Optional,
)

from armodel.v2.models.M2.AUTOSARTemplates.BswModuleTemplate.BswImplementation import (
    BswImplementation,
)
from armodel.v2.models.M2.AUTOSARTemplates.BswModuleTemplate.BswInterfaces import (
    BswModuleEntry,
)
from armodel.v2.models.M2.AUTOSARTemplates.BswModuleTemplate.BswOverview import (
    BswModuleDescription,
)
from armodel.v2.models.M2.AUTOSARTemplates.CommonStructure import (
    ConstantSpecification,
)
from armodel.v2.models.M2.AUTOSARTemplates.CommonStructure.FlatMap import (
    FlatMap,
)
from armodel.v2.models.M2.AUTOSARTemplates.CommonStructure.Implementation import (
    Implementation,
)
from armodel.v2.models.M2.AUTOSARTemplates.CommonStructure.ImplementationDataTypes import (
    ImplementationDataType,
)
from armodel.v2.models.M2.AUTOSARTemplates.CommonStructure.ModeDeclaration import (
    ModeDeclarationGroup,
)
from armodel.v2.models.M2.AUTOSARTemplates.CommonStructure.StandardizationTemplate.BlueprintDedicated.PortPrototypeBlueprint import (
    PortPrototypeBlueprint,
)
from armodel.v2.models.M2.AUTOSARTemplates.CommonStructure.StandardizationTemplate.Keyword import (
    KeywordSet,
)
from armodel.v2.models.M2.AUTOSARTemplates.CommonStructure.SwcBswMapping import (
    SwcBswMapping,
)
from armodel.v2.models.M2.AUTOSARTemplates.CommonStructure.Timing.TimingExtensions import (
    SwcTiming,
)
from armodel.v2.models.M2.AUTOSARTemplates.DiagnosticExtract.DiagnosticContribution import (
    DiagnosticServiceTable,
)
from armodel.v2.models.M2.AUTOSARTemplates.ECUCDescriptionTemplate import (
    EcucModuleConfigurationValues,
    EcucValueCollection,
)
from armodel.v2.models.M2.AUTOSARTemplates.ECUCParameterDefTemplate import (
    EcucModuleDef,
)
from armodel.v2.models.M2.AUTOSARTemplates.EcuResourceTemplate import HwElement
from armodel.v2.models.M2.AUTOSARTemplates.EcuResourceTemplate.HwElementCategory import (
    HwCategory,
    HwType,
)
from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import (
    ARObject,
)
from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ElementCollection import (
    CollectableElement,
    Collection,
)
from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable import (
    Referrable,
)
from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Boolean,
    CategoryString,
    Identifier,
    ReferrableSubtypesEnum,
    RefType,
)
from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.LifeCycles import (
    LifeCycleInfoSet,
)
from armodel.v2.models.M2.AUTOSARTemplates.SWComponentTemplate.Components import (
    ApplicationSwComponentType,
    AtomicSwComponentType,
    ComplexDeviceDriverSwComponentType,
    EcuAbstractionSwComponentType,
    SensorActuatorSwComponentType,
    ServiceSwComponentType,
    SwComponentType,
)
from armodel.v2.models.M2.AUTOSARTemplates.SWComponentTemplate.Composition import (
    CompositionSwComponentType,
)
from armodel.v2.models.M2.AUTOSARTemplates.SWComponentTemplate.Datatype.Datatypes import (
    ApplicationArrayDataType,
    ApplicationDataType,
    ApplicationPrimitiveDataType,
    ApplicationRecordDataType,
    DataTypeMappingSet,
)
from armodel.v2.models.M2.AUTOSARTemplates.SWComponentTemplate.EndToEndProtection import (
    EndToEndProtectionSet,
)
from armodel.v2.models.M2.AUTOSARTemplates.SWComponentTemplate.PortInterface import (
    ClientServerInterface,
    ModeDeclarationMappingSet,
    ModeSwitchInterface,
    ParameterInterface,
    PortInterfaceMappingSet,
    SenderReceiverInterface,
    TriggerInterface,
)
from armodel.v2.models.M2.AUTOSARTemplates.SWComponentTemplate.SwcImplementation import (
    SwcImplementation,
)
from armodel.v2.models.M2.AUTOSARTemplates.SystemTemplate import System
from armodel.v2.models.M2.AUTOSARTemplates.SystemTemplate.DiagnosticConnection import (
    DiagnosticConnection,
)
from armodel.v2.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Can.CanCommunication import (
    CanFrame,
)
from armodel.v2.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Ethernet.EthernetCommunication import (
    SoAdRoutingGroup,
)
from armodel.v2.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Ethernet.EthernetFrame import (
    GenericEthernetFrame,
)
from armodel.v2.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Ethernet.EthernetTopology import (
    EthernetCluster,
)
from armodel.v2.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Flexray.FlexrayCommunication import (
    FlexrayFrame,
)
from armodel.v2.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Flexray.FlexrayTopology import (
    FlexrayCluster,
)
from armodel.v2.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Lin.LinCommunication import (
    LinUnconditionalFrame,
)
from armodel.v2.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Multiplatform import (
    Gateway,
)
from armodel.v2.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore.CoreCommunication import (
    DcmIPdu,
    GeneralPurposeIPdu,
    GeneralPurposePdu,
    ISignal,
    ISignalGroup,
    ISignalIPdu,
    ISignalIPduGroup,
    MultiplexedIPdu,
    NmPdu,
    NPdu,
    SecureCommunicationPropsSet,
    SecuredIPdu,
    SystemSignal,
    SystemSignalGroup,
    UserDefinedIPdu,
    UserDefinedPdu,
)
from armodel.v2.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore.CoreTopology import (
    CanCluster,
    EcuInstance,
    LinCluster,
)
from armodel.v2.models.M2.AUTOSARTemplates.SystemTemplate.NetworkManagement import (
    NmConfig,
)
from armodel.v2.models.M2.AUTOSARTemplates.SystemTemplate.Transformer import (
    DataTransformationSet,
)
from armodel.v2.models.M2.AUTOSARTemplates.SystemTemplate.TransportProtocols import (
    CanTpConfig,
    DoIpTpConfig,
    LinTpConfig,
)
from armodel.v2.models.M2.MSR.AsamHdo.AdminData import AdminData
from armodel.v2.models.M2.MSR.AsamHdo.BaseTypes import SwBaseType
from armodel.v2.models.M2.MSR.AsamHdo.ComputationMethod import CompuMethod
from armodel.v2.models.M2.MSR.AsamHdo.Constraints.GlobalConstraints import (
    DataConstr,
)
from armodel.v2.models.M2.MSR.AsamHdo.Units import (
    PhysicalDimension,
    Unit,
)
from armodel.v2.models.M2.MSR.DataDictionary.AuxillaryObjects import (
    SwAddrMethod,
)
from armodel.v2.models.M2.MSR.DataDictionary.RecordLayout import SwRecordLayout
from armodel.v2.models.M2.MSR.Documentation.Annotation import Annotation
from armodel.v2.models.M2.MSR.Documentation.TextModel.BlockElements import (
    DocumentationBlock,
)
from armodel.v2.models.M2.MSR.Documentation.TextModel.MultilanguageData import (
    MultilanguageLongName,
    MultiLanguageOverviewParagraph,
)


class ReferenceBase(ARObject):
    """
    Represents a reference base in AUTOSAR models. Reference bases define
    how elements in one package can reference elements in other packages.
    They are used to establish relationships between different AUTOSAR packages.
    """


    def _validate_abstract(self) -> None:
        """Validate this is a concrete class."""
        pass

    def __init__(self) -> None:
        """
        Initializes a ReferenceBase instance with default values for
        package reference properties.
        """
        super().__init__()

        # List of global elements that can be referenced
        self.globalElements: List[ReferrableSubtypesEnum] = []
        # List of global references within the package
        self.globalInPackageRefs: List[RefType] = []
        # Flag indicating if this reference base is the default
        self.isDefault: Union[Optional[Boolean] , None] = None
        # Flag indicating if this reference base is global
        self.isGlobal: Union[Optional[Boolean] , None] = None
        # Flag indicating if this reference base belongs to the current package
        self.BaseIsThisPackage: Union[Optional[Boolean] , None] = None
        # List of package references
        self.packageRef: Union[Optional[List[RefType]] , None] = None
        # Short label for this reference base
        self.shortLabel: Union[Optional[Identifier] , None] = None

    def getGlobalElements(self) -> List[ReferrableSubtypesEnum]:
        """
        Returns the list of global elements that can be referenced.

        Returns:
            List of global elements that can be referenced
        """
        return self.globalElements

    def addGlobalElement(self, value: ReferrableSubtypesEnum) -> 'ReferenceBase':
        """
        Adds a global element to the list of referenceable elements.

        Args:
            value: The element to add to the list of global elements

        Returns:
            Reference to this ReferenceBase instance (for method chaining)
        """
        self.globalElements.append(value)
        return self

    def getGlobalInPackageRefs(self) -> List[RefType]:
        """
        Returns the list of global references within the package.

        Returns:
            List of global references within the package
        """
        return self.globalInPackageRefs

    def addGlobalInPackageRef(self, value: RefType) -> 'ReferenceBase':
        """
        Adds a global reference to the package.

        Args:
            value: The reference to add to the list of global in-package references

        Returns:
            Reference to this ReferenceBase instance (for method chaining)
        """
        self.globalInPackageRefs.append(value)
        return self

    def getIsDefault(self) -> Optional[Boolean]:
        """
        Returns whether this reference base is the default.

        Returns:
            Boolean indicating if this is the default reference base (or None)
        """
        return self.isDefault

    def setIsDefault(self, value: Boolean) -> 'ReferenceBase':
        """
        Sets whether this reference base is the default.

        Args:
            value: Boolean indicating if this should be the default reference base

        Returns:
            Reference to this ReferenceBase instance (for method chaining)
        """
        self.isDefault = value
        return self

    def getIsGlobal(self) -> Optional[Boolean]:
        """
        Returns whether this reference base is global.

        Returns:
            Boolean indicating if this is a global reference base (or None)
        """
        return self.isGlobal

    def setIsGlobal(self, value: Boolean) -> 'ReferenceBase':
        """
        Sets whether this reference base is global.

        Args:
            value: Boolean indicating if this should be a global reference base

        Returns:
            Reference to this ReferenceBase instance (for method chaining)
        """
        self.isGlobal = value
        return self

    def getBaseIsThisPackage(self) -> Optional[Boolean]:
        """
        Returns whether this reference base belongs to the current package.

        Returns:
            Boolean indicating if this reference base belongs to the current package (or None)
        """
        return self.BaseIsThisPackage

    def setBaseIsThisPackage(self, value: Boolean) -> 'ReferenceBase':
        """
        Sets whether this reference base belongs to the current package.

        Args:
            value: Boolean indicating if this reference base belongs to the current package

        Returns:
            Reference to this ReferenceBase instance (for method chaining)
        """
        self.BaseIsThisPackage = value
        return self

    def getPackageRef(self) -> Optional[List[RefType]]:
        """
        Returns the list of package references.

        Returns:
            List of package references (or None)
        """
        return self.packageRef

    def setPackageRef(self, value: List[RefType]) -> 'ReferenceBase':
        """
        Sets the list of package references.

        Args:
            value: List of package references to set

        Returns:
            Reference to this ReferenceBase instance (for method chaining)
        """
        self.packageRef = value
        return self

    def getShortLabel(self) -> Optional[Identifier]:
        """
        Returns the short label for this reference base.

        Returns:
            Short label identifier (or None)
        """
        return self.shortLabel

    def setShortLabel(self, value: Identifier) -> 'ReferenceBase':
        """
        Sets the short label for this reference base.

        Args:
            value: The identifier to use as the short label

        Returns:
            Reference to this ReferenceBase instance (for method chaining)
        """
        self.shortLabel = value
        return self


class ARPackage(CollectableElement):
    """
    Represents an AUTOSAR package, which is a container for organizing
    AUTOSAR model elements hierarchically. ARPackage serves as the primary
    organizational unit in AUTOSAR models, allowing for grouping of related
    elements such as software components, interfaces, data types, and other packages.

    ARPackages form a tree-like structure where each package can contain
    sub-packages as well as various AUTOSAR elements.
    """

    def __init__(self, parent: ARObject, short_name: str) -> None:
        """
        Initializes an ARPackage instance with the specified parent and short name.

        Args:
            parent: The parent ARObject that contains this package
            short_name: The unique identifier for this package within its parent
        """
        # Initialize CollectableElement (which inherits from ARObject)
        CollectableElement.__init__(self)
        # Explicitly initialize ARObject attributes since CollectableElement doesn't call super().__init__()
        ARObject.__init__(self)

        # Referrable attributes (added directly since ARPackage doesn't inherit from Referrable)
        self.parent = parent
        self.short_name = short_name

        # Identifiable attributes (added directly since ARPackage doesn't inherit from Identifiable)
        self.longName: Union[Optional[MultilanguageLongName] , None] = None
        self.annotations: List[Annotation] = []
        self.adminData: Union[Optional[AdminData] , None] = None
        self.category: Union[Optional[CategoryString] , None] = None
        self.introduction: Union[Optional[DocumentationBlock] , None] = None
        self.desc: Union[Optional[MultiLanguageOverviewParagraph] , None] = None

        # Dictionary mapping short names to sub-packages
        self.arPackages: Dict[str, 'ARPackage'] = {}
        # List of reference bases for this package
        self.referenceBases: List[ReferenceBase] = []

    @property
    def shortName(self) -> str:
        """str: The short name of this ARPackage."""
        return self.short_name

    @shortName.setter
    def shortName(self, value: str):
        self.short_name = value

    def getShortName(self) -> str:
        """
        Gets the short name of this ARPackage.

        Returns:
            The short name of this ARPackage
        """
        return self.short_name

    def getParent(self) -> ARObject:
        """
        Gets the parent of this ARPackage.

        Returns:
            The parent ARObject
        """
        return self.parent

    @property
    def full_name(self) -> str:
        """
        str: The full name of this ARPackage, including the parent's full name.
        """
        return self.parent.full_name + "/" + self.short_name

    def getFullName(self) -> str:
        """
        Gets the full name of this ARPackage, including the parent's full name.

        Returns:
            The full name of this ARPackage
        """
        return self.full_name

    def getLongName(self) -> Optional[MultilanguageLongName]:
        """
        Gets the long name of this ARPackage.

        Returns:
            MultilanguageLongName representing the long name, or None if not set
        """
        return self.longName

    def setLongName(self, value: MultilanguageLongName) -> 'ARPackage':
        """
        Sets the long name of this ARPackage.

        Args:
            value: The long name to set

        Returns:
            self for method chaining
        """
        self.longName = value
        return self

    def getAdminData(self) -> Optional[AdminData]:
        """
        Gets the administrative data for this ARPackage.

        Returns:
            AdminData instance, or None if not set
        """
        return self.adminData

    def setAdminData(self, value: AdminData) -> 'ARPackage':
        """
        Sets the administrative data for this ARPackage.
        Only sets the value if it is not None.

        Args:
            value: The administrative data to set

        Returns:
            self for method chaining
        """
        if value is not None:
            self.adminData = value
        return self

    def removeAdminData(self) -> None:
        """
        Removes the administrative data for this ARPackage.
        """
        self.adminData = None

    def getDesc(self) -> Optional[MultiLanguageOverviewParagraph]:
        """
        Gets the description for this ARPackage.

        Returns:
            MultiLanguageOverviewParagraph instance, or None if not set
        """
        return self.desc

    def setDesc(self, value: MultiLanguageOverviewParagraph) -> 'ARPackage':
        """
        Sets the description for this ARPackage.

        Args:
            value: The description to set

        Returns:
            self for method chaining
        """
        self.desc = value
        return self

    def getCategory(self) -> Optional[CategoryString]:
        """
        Gets the category for this ARPackage.

        Returns:
            CategoryString instance, or None if not set
        """
        return self.category

    def setCategory(self, value: Any) -> 'ARPackage':
        """
        Sets the category for this ARPackage.
        If the value is a string, it will be converted to a CategoryString.

        Args:
            value: The category to set

        Returns:
            self for method chaining
        """
        if isinstance(value, str):
            self.category = CategoryString().setValue(value)
        else:
            self.category = value
        return self

    def getIntroduction(self) -> Optional[DocumentationBlock]:
        """
        Gets the introduction documentation for this ARPackage.

        Returns:
            DocumentationBlock instance, or None if not set
        """
        return self.introduction

    def setIntroduction(self, value: DocumentationBlock) -> 'ARPackage':
        """
        Sets the introduction documentation for this ARPackage.

        Args:
            value: The introduction documentation to set

        Returns:
            self for method chaining
        """
        self.introduction = value
        return self

    def addAnnotation(self, annotation: Annotation) -> 'ARPackage':
        """
        Adds an annotation to this ARPackage.

        Args:
            annotation: The annotation to add

        Returns:
            self for method chaining
        """
        self.annotations.append(annotation)
        return self

    def getAnnotations(self) -> List[Annotation]:
        """
        Gets the list of annotations for this ARPackage.

        Returns:
            List of Annotation instances
        """
        return self.annotations

    def getARPackages(self) -> List['ARPackage']:
        """
        Returns a list of all sub-packages contained in this ARPackage,
        sorted by their short names.

        Returns:
            List of ARPackage instances sorted by short name
        """
        return sorted(self.arPackages.values(), key=lambda a: a.short_name)
        # return list(filter(lambda e: isinstance(e, ARPackage), self.elements))

    def createARPackage(self, short_name: str) -> 'ARPackage':
        """
        Creates a new sub-package with the given short name, or returns
        an existing package if one with the same name already exists.

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
        Retrieves an element by its short name, optionally filtered by type.
        This method searches for both sub-packages and other elements in this package.

        Args:
            short_name: The short name of the element to retrieve
            type: Optional type filter for the element to retrieve

        Returns:
            The element with the specified name and type, or None if not found
        """
        if (type is ARPackage or type is None) and short_name in self.arPackages:
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
        if (not self.IsElementExists(short_name, CompuMethod)):
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

    def createCollection(self, short_name: str) -> Collection:
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
        return sorted(filter(lambda a: isinstance(a, ApplicationPrimitiveDataType), self.elements), key=lambda o: o.short_name)

    def getApplicationDataType(self) -> List[ApplicationDataType]:
        return sorted(filter(lambda a: isinstance(a, ApplicationDataType), self.elements), key=lambda o: o.short_name)

    def getImplementationDataTypes(self) -> List[ImplementationDataType]:
        return sorted(filter(lambda a: isinstance(a, ImplementationDataType), self.elements), key=lambda o: o.short_name)

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
        return sorted(filter(lambda a: isinstance(a, ComplexDeviceDriverSwComponentType), self.elements), key=lambda a: a.short_name)

    def getSenderReceiverInterfaces(self) -> List[SenderReceiverInterface]:
        return sorted(filter(lambda a: isinstance(a, SenderReceiverInterface), self.elements), key=lambda a: a.short_name)

    def getParameterInterfaces(self) -> List[ParameterInterface]:
        return sorted(filter(lambda a: isinstance(a, ParameterInterface), self.elements), key=lambda a: a.short_name)

    def getClientServerInterfaces(self) -> List[ClientServerInterface]:
        return sorted(filter(lambda a: isinstance(a, ClientServerInterface), self.elements), key=lambda a: a.short_name)

    def getDataTypeMappingSets(self) -> List[DataTypeMappingSet]:
        return sorted(filter(lambda a: isinstance(a, DataTypeMappingSet), self.elements), key=lambda a: a.short_name)

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

    def getConstantSpecifications(self) -> List[ConstantSpecification]:
        return list(filter(lambda a: isinstance(a, ConstantSpecification), self.elements))

    def getDataConstrs(self) -> List[DataConstr]:
        return list(filter(lambda a: isinstance(a, DataConstr), self.elements))

    def getUnits(self) -> List[Unit]:
        return list(filter(lambda a: isinstance(a, Unit), self.elements))

    def getApplicationArrayDataTypes(self) -> List[ApplicationArrayDataType]:
        return sorted(filter(lambda a: isinstance(a, ApplicationArrayDataType), self.elements), key=lambda a: a.short_name)

    def getSwRecordLayouts(self) -> List[SwRecordLayout]:
        return sorted(filter(lambda a: isinstance(a, SwRecordLayout), self.elements), key=lambda a: a.short_name)

    def getSwAddrMethods(self) -> List[SwAddrMethod]:
        return sorted(filter(lambda a: isinstance(a, SwAddrMethod), self.elements), key=lambda a: a.short_name)

    def getTriggerInterfaces(self) -> List[TriggerInterface]:
        return sorted(filter(lambda a: isinstance(a, TriggerInterface), self.elements), key=lambda a: a.short_name)

    def getModeDeclarationGroups(self) -> List[ModeDeclarationGroup]:
        return sorted(filter(lambda a: isinstance(a, ModeDeclarationGroup), self.elements), key=lambda a: a.short_name)

    def getModeSwitchInterfaces(self) -> List[ModeSwitchInterface]:
        return sorted(filter(lambda a: isinstance(a, ModeSwitchInterface), self.elements), key=lambda a: a.short_name)

    def getSwcTimings(self) -> List[SwcTiming]:
        return sorted(filter(lambda a: isinstance(a, SwcTiming), self.elements), key=lambda a: a.short_name)

    def getLinClusters(self) -> List[LinCluster]:
        return sorted(filter(lambda a: isinstance(a, LinCluster), self.elements), key=lambda a: a.short_name)

    def getCanClusters(self) -> List[CanCluster]:
        return sorted(filter(lambda a: isinstance(a, CanCluster), self.elements), key=lambda a: a.short_name)

    def getLinUnconditionalFrames(self) -> List[LinUnconditionalFrame]:
        return sorted(filter(lambda a: isinstance(a, LinUnconditionalFrame), self.elements), key=lambda a: a.short_name)

    def getNmPdus(self) -> List[NmPdu]:
        return sorted(filter(lambda a: isinstance(a, NmPdu), self.elements), key=lambda a: a.short_name)

    def getNPdus(self) -> List[NPdu]:
        return sorted(filter(lambda a: isinstance(a, NPdu), self.elements), key=lambda a: a.short_name)

    def getDcmIPdus(self) -> List[DcmIPdu]:
        return sorted(filter(lambda a: isinstance(a, DcmIPdu), self.elements), key=lambda a: a.short_name)

    def getSecuredIPdus(self) -> List[SecuredIPdu]:
        return sorted(filter(lambda a: isinstance(a, SecuredIPdu), self.elements), key=lambda a: a.short_name)

    def getNmConfigs(self) -> List[NmConfig]:
        return sorted(filter(lambda a: isinstance(a, NmConfig), self.elements), key=lambda a: a.short_name)

    def getCanTpConfigs(self) -> List[CanTpConfig]:
        return sorted(filter(lambda a: isinstance(a, CanTpConfig), self.elements), key=lambda a: a.short_name)

    def getCanFrames(self) -> List[CanFrame]:
        return sorted(filter(lambda a: isinstance(a, CanFrame), self.elements), key=lambda a: a.short_name)

    def getEcuInstances(self) -> List[EcuInstance]:
        return sorted(filter(lambda a: isinstance(a, EcuInstance), self.elements), key=lambda a: a.short_name)

    def getGateways(self) -> List[Gateway]:
        return sorted(filter(lambda a: isinstance(a, Gateway), self.elements), key=lambda a: a.short_name)

    def getISignals(self) -> List[ISignal]:
        return sorted(filter(lambda a: isinstance(a, ISignal), self.elements), key=lambda a: a.short_name)

    def getEcucValueCollections(self) -> List[EcucValueCollection]:
        return sorted(filter(lambda a: isinstance(a, EcucValueCollection), self.elements), key=lambda a: a.short_name)

    def getEcucModuleConfigurationValues(self) -> List[EcucModuleConfigurationValues]:
        return sorted(filter(lambda a: isinstance(a, EcucModuleConfigurationValues), self.elements), key=lambda a: a.short_name)

    def getEcucModuleDefs(self) -> List[EcucModuleDef]:
        return sorted(filter(lambda a: isinstance(a, EcucModuleDef), self.elements), key=lambda a: a.short_name)

    def getEcucPhysicalDimensions(self) -> List[PhysicalDimension]:
        return sorted(filter(lambda a: isinstance(a, PhysicalDimension), self.elements), key=lambda a: a.short_name)

    def getISignalGroups(self) -> List[ISignalGroup]:
        return sorted(filter(lambda a: isinstance(a, ISignalGroup), self.elements), key=lambda a: a.short_name)

    def getSystemSignals(self) -> List[SystemSignal]:
        return sorted(filter(lambda a: isinstance(a, SystemSignal), self.elements), key=lambda a: a.short_name)

    def getSystemSignalGroups(self) -> List[SystemSignalGroup]:
        return sorted(filter(lambda a: isinstance(a, SystemSignalGroup), self.elements), key=lambda a: a.short_name)

    def getISignalIPdus(self) -> List[ISignalIPdu]:
        return sorted(filter(lambda a: isinstance(a, ISignalIPdu), self.elements), key=lambda a: a.short_name)

    def getSystems(self) -> List[System]:
        return sorted(filter(lambda a: isinstance(a, System), self.elements), key=lambda a: a.short_name)

    def getHwElements(self) -> List[HwElement]:
        return sorted(filter(lambda a: isinstance(a, HwElement), self.elements), key=lambda a: a.short_name)

    def getHwCategories(self) -> List[HwCategory]:
        return sorted(filter(lambda a: isinstance(a, HwCategory), self.elements), key=lambda a: a.short_name)

    def getFlexrayFrames(self) -> List[FlexrayFrame]:
        return sorted(filter(lambda a: isinstance(a, FlexrayFrame), self.elements), key=lambda a: a.short_name)

    def getDataTransformationSets(self) -> List[DataTransformationSet]:
        return sorted(filter(lambda a: isinstance(a, DataTransformationSet), self.elements), key=lambda a: a.short_name)

    def getCollections(self) -> List[Collection]:
        return sorted(filter(lambda a: isinstance(a, Collection), self.elements), key=lambda a: a.short_name)

    def getKeywordSets(self) -> List[KeywordSet]:
        return sorted(filter(lambda a: isinstance(a, KeywordSet), self.elements), key=lambda a: a.short_name)

    def getPortPrototypeBlueprints(self) -> List[PortPrototypeBlueprint]:
        return sorted(filter(lambda a: isinstance(a, PortPrototypeBlueprint), self.elements), key=lambda a: a.short_name)

    def getModeDeclarationMappingSets(self) -> List[ModeDeclarationMappingSet]:
        return sorted(filter(lambda a: isinstance(a, ModeDeclarationMappingSet), self.elements), key=lambda a: a.short_name)

    def getReferenceBases(self):
        return self.referenceBases

    def addReferenceBase(self, value):
        self.referenceBases.append(value)
        return self
