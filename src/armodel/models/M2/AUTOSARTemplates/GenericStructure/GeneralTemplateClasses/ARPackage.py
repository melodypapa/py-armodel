from typing import Dict, List

from .....M2.AUTOSARTemplates.SWComponentTemplate.Components import SensorActuatorSwComponentType
from .....M2.MSR.AsamHdo.BaseTypes import SwBaseType
from .....M2.MSR.AsamHdo.Units import PhysicalDimension, Unit
from .....M2.MSR.AsamHdo.Constraints.GlobalConstraints import DataConstr
from .....M2.MSR.AsamHdo.ComputationMethod import CompuMethod
from .....M2.MSR.DataDictionary.AuxillaryObjects import SwAddrMethod
from .....M2.MSR.DataDictionary.RecordLayout import SwRecordLayout

from .....M2.AUTOSARTemplates.BswModuleTemplate.BswImplementation import BswImplementation
from .....M2.AUTOSARTemplates.BswModuleTemplate.BswOverview import BswModuleDescription
from .....M2.AUTOSARTemplates.BswModuleTemplate.BswInterfaces import BswModuleEntry
from .....M2.AUTOSARTemplates.CommonStructure import ConstantSpecification
from .....M2.AUTOSARTemplates.CommonStructure.ImplementationDataTypes import ImplementationDataType
from .....M2.AUTOSARTemplates.CommonStructure.Implementation import Implementation
from .....M2.AUTOSARTemplates.CommonStructure.FlatMap import FlatMap
from .....M2.AUTOSARTemplates.CommonStructure.ModeDeclaration import ModeDeclarationGroup
from .....M2.AUTOSARTemplates.CommonStructure.SwcBswMapping import SwcBswMapping
from .....M2.AUTOSARTemplates.CommonStructure.StandardizationTemplate.BlueprintDedicated.PortPrototypeBlueprint import PortPrototypeBlueprint
from .....M2.AUTOSARTemplates.CommonStructure.StandardizationTemplate.Keyword import KeywordSet
from .....M2.AUTOSARTemplates.CommonStructure.Timing.TimingConstraint.TimingExtensions import SwcTiming
from .....M2.AUTOSARTemplates.DiagnosticExtract.DiagnosticContribution import DiagnosticServiceTable
from .....M2.AUTOSARTemplates.ECUCDescriptionTemplate import EcucModuleConfigurationValues, EcucModuleDef, EcucValueCollection
from .....M2.AUTOSARTemplates.EcuResourceTemplate import HwElement
from .....M2.AUTOSARTemplates.EcuResourceTemplate.HwElementCategory import HwCategory, HwType
from .....M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import ARObject
from .....M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ElementCollection import Collection
from .....M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable import CollectableElement, Identifiable, Referrable
from .....M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import Boolean, Identifier, RefType, ReferrableSubtypesEnum
from .....M2.AUTOSARTemplates.GenericStructure.LifeCycles import LifeCycleInfoSet
from .....M2.AUTOSARTemplates.SWComponentTemplate.Components import CompositionSwComponentType, ServiceSwComponentType, SwComponentType
from .....M2.AUTOSARTemplates.SWComponentTemplate.Components import ApplicationSwComponentType, AtomicSwComponentType
from .....M2.AUTOSARTemplates.SWComponentTemplate.Components import ComplexDeviceDriverSwComponentType, EcuAbstractionSwComponentType
from .....M2.AUTOSARTemplates.SWComponentTemplate.Datatype.Datatypes import ApplicationArrayDataType, ApplicationDataType
from .....M2.AUTOSARTemplates.SWComponentTemplate.Datatype.Datatypes import ApplicationPrimitiveDataType, ApplicationRecordDataType
from .....M2.AUTOSARTemplates.SWComponentTemplate.Datatype.Datatypes import DataTypeMappingSet
from .....M2.AUTOSARTemplates.SWComponentTemplate.EndToEndProtection import EndToEndProtectionSet
from .....M2.AUTOSARTemplates.SWComponentTemplate.PortInterface import ClientServerInterface, ModeDeclarationMappingSet, ModeSwitchInterface
from .....M2.AUTOSARTemplates.SWComponentTemplate.PortInterface import PortInterfaceMappingSet, SenderReceiverInterface, TriggerInterface
from .....M2.AUTOSARTemplates.SWComponentTemplate.PortInterface import ParameterInterface
from .....M2.AUTOSARTemplates.SWComponentTemplate.SwcImplementation import SwcImplementation

from .....M2.AUTOSARTemplates.SystemTemplate import System
from .....M2.AUTOSARTemplates.SystemTemplate.DiagnosticConnection import DiagnosticConnection
from .....M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Can.CanCommunication import CanFrame
from .....M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Multiplatform import Gateway
from .....M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore.CoreCommunication import DcmIPdu, GeneralPurposeIPdu, GeneralPurposePdu, ISignal
from .....M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore.CoreCommunication import ISignalGroup, ISignalIPdu, ISignalIPduGroup, MultiplexedIPdu
from .....M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore.CoreCommunication import NPdu, NmPdu, SecureCommunicationPropsSet, SecuredIPdu
from .....M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore.CoreCommunication import SystemSignal, SystemSignalGroup, UserDefinedIPdu, UserDefinedPdu
from .....M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore.CoreTopology import CanCluster, LinCluster
from .....M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore.EcuInstance import EcuInstance
from .....M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Lin.LinCommunication import LinUnconditionalFrame
from .....M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Ethernet.EthernetFrame import GenericEthernetFrame
from .....M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Ethernet.EthernetTopology import EthernetCluster
from .....M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Ethernet.EthernetCommunication import SoAdRoutingGroup
from .....M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Flexray.FlexrayCommunication import FlexrayFrame
from .....M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Flexray.FlexrayTopology import FlexrayCluster
from .....M2.AUTOSARTemplates.SystemTemplate.NetworkManagement import NmConfig
from .....M2.AUTOSARTemplates.SystemTemplate.Transformer import DataTransformationSet
from .....M2.AUTOSARTemplates.SystemTemplate.TransportProtocols import CanTpConfig, DoIpTpConfig, LinTpConfig


class ReferenceBase(ARObject):
    def __init__(self):
        super().__init__()

        self.globalElements = []                                    # type: List[ReferrableSubtypesEnum]
        self.globalInPackageRefs = []                               # type: List[RefType]
        self.isDefault = None                                       # type: Boolean
        self.isGlobal = None                                        # type: Boolean
        self.BaseIsThisPackage = None                               # type: Boolean
        self.packageRef = None                                      # type: List[RefType]
        self.shortLabel = None                                      # type: Identifier

    def getGlobalElements(self):
        return self.globalElements

    def addGlobalElement(self, value):
        self.globalElements.append(value)
        return self

    def getGlobalInPackageRefs(self):
        return self.globalInPackageRefs

    def addGlobalInPackageRef(self, value):
        self.globalInPackageRefs.append(value)
        return self

    def getIsDefault(self):
        return self.isDefault

    def setIsDefault(self, value):
        self.isDefault = value
        return self
    
    def getIsGlobal(self):
        return self.isGlobal

    def setIsGlobal(self, value):
        self.isGlobal = value
        return self
    
    def getBaseIsThisPackage(self):
        return self.BaseIsThisPackage

    def setBaseIsThisPackage(self, value):
        self.BaseIsThisPackage = value
        return self

    def getPackageRef(self):
        return self.packageRef

    def setPackageRef(self, value):
        self.packageRef = value
        return self

    def getShortLabel(self):
        return self.shortLabel

    def setShortLabel(self, value):
        self.shortLabel = value
        return self


class ARPackage(Identifiable, CollectableElement):
    def __init__(self, parent: ARObject, short_name: str):
        Identifiable.__init__(self, parent, short_name)
        CollectableElement.__init__(self)

        self.arPackages = {}                                        # type: Dict[str, ARPackage]
        self.referenceBases = []                                     # type: List[ReferenceBase]

    def getARPackages(self):    # type: (...) -> List[ARPackage]
        return list(sorted(self.arPackages.values(), key=lambda a: a.short_name))
        # return list(filter(lambda e: isinstance(e, ARPackage), self.elements))

    def createARPackage(self, short_name: str):
        if short_name not in self.arPackages:
            ar_package = ARPackage(self, short_name)
            self.arPackages[short_name] = ar_package
        return self.arPackages[short_name]

    def getElement(self, short_name: str, type=None) -> Referrable:
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
        if not self.IsElementExists(short_name, CanFrame):
            element = CanFrame(self, short_name)
            self.addElement(element)
        return self.getElement(short_name, CanFrame)

    def createEcuInstance(self, short_name: str) -> EcuInstance:
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
        return list(sorted(filter(lambda a: isinstance(a, Collection), self.elements), key=lambda a: a.short_name))
    
    def getKeywordSets(self) -> List[KeywordSet]:
        return list(sorted(filter(lambda a: isinstance(a, KeywordSet), self.elements), key=lambda a: a.short_name))
    
    def getPortPrototypeBlueprints(self) -> List[PortPrototypeBlueprint]:
        return list(sorted(filter(lambda a: isinstance(a, PortPrototypeBlueprint), self.elements), key=lambda a: a.short_name))
    
    def getModeDeclarationMappingSets(self) -> List[ModeDeclarationMappingSet]:
        return list(sorted(filter(lambda a: isinstance(a, ModeDeclarationMappingSet), self.elements), key=lambda a: a.short_name))
    
    def getReferenceBases(self):
        return self.referenceBases

    def addReferenceBase(self, value):
        self.referenceBases.append(value)
        return self
