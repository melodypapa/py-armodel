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
        # return list(filter(lambda e: isinstance(e, ARPackage), self.elements.values()))

    def createARPackage(self, short_name: str):
        '''
        if (not self.IsElementExists(short_name)):
            ar_package = ARPackage(self, short_name)
            self.elements[short_name] = ar_package
        return self.elements[short_name]
        '''
        if short_name not in self.arPackages:
            ar_package = ARPackage(self, short_name)
            self.arPackages[short_name] = ar_package
        return self.arPackages[short_name]

    def getElement(self, short_name: str) -> Referrable:
        if (short_name in self.arPackages):
            return self.arPackages[short_name]
        return CollectableElement.getElement(self, short_name)

    def createEcuAbstractionSwComponentType(self, short_name: str) -> EcuAbstractionSwComponentType:
        if (not self.IsElementExists(short_name)):
            sw_component = EcuAbstractionSwComponentType(self, short_name)
            self.addElement(sw_component)
        return self.getElement(short_name)

    def createApplicationSwComponentType(self, short_name: str) -> ApplicationSwComponentType:
        if not self.IsElementExists(short_name):
            sw_component = ApplicationSwComponentType(self, short_name)
            self.addElement(sw_component)
        return self.getElement(short_name)

    def createComplexDeviceDriverSwComponentType(self, short_name: str) -> ComplexDeviceDriverSwComponentType:
        if not self.IsElementExists(short_name):
            sw_component = ComplexDeviceDriverSwComponentType(self, short_name)
            self.addElement(sw_component)
        return self.getElement(short_name)

    def createServiceSwComponentType(self, short_name: str) -> ServiceSwComponentType:
        if (not self.IsElementExists(short_name)):
            sw_component = ServiceSwComponentType(self, short_name)
            self.addElement(sw_component)
        return self.getElement(short_name)

    def createSensorActuatorSwComponentType(self, short_name: str) -> SensorActuatorSwComponentType:
        if (not self.IsElementExists(short_name)):
            sw_component = SensorActuatorSwComponentType(self, short_name)
            self.addElement(sw_component)
        return self.getElement(short_name)

    def createCompositionSwComponentType(self, short_name: str) -> CompositionSwComponentType:
        if (not self.IsElementExists(short_name)):
            sw_component = CompositionSwComponentType(self, short_name)
            self.addElement(sw_component)
        return self.getElement(short_name)

    def createSenderReceiverInterface(self, short_name: str) -> SenderReceiverInterface:
        if (not self.IsElementExists(short_name)):
            sr_interface = SenderReceiverInterface(self, short_name)
            self.addElement(sr_interface)
        return self.getElement(short_name)

    def createParameterInterface(self, short_name: str) -> ParameterInterface:
        if (not self.IsElementExists(short_name)):
            sr_interface = ParameterInterface(self, short_name)
            self.addElement(sr_interface)
        return self.getElement(short_name)
    
    def createGenericEthernetFrame(self, short_name: str) -> GenericEthernetFrame:
        if (not self.IsElementExists(short_name)):
            frame = GenericEthernetFrame(self, short_name)
            self.addElement(frame)
        return self.getElement(short_name)
    
    def createLifeCycleInfoSet(self, short_name: str) -> LifeCycleInfoSet:
        if (not self.IsElementExists(short_name)):
            set = LifeCycleInfoSet(self, short_name)
            self.addElement(set)
        return self.getElement(short_name)
    
    def createClientServerInterface(self, short_name: str) -> ClientServerInterface:
        if (not self.IsElementExists(short_name)):
            cs_interface = ClientServerInterface(self, short_name)
            self.addElement(cs_interface)
        return self.getElement(short_name)

    def createApplicationPrimitiveDataType(self, short_name: str) -> ApplicationPrimitiveDataType:
        if (not self.IsElementExists(short_name)):
            data_type = ApplicationPrimitiveDataType(self, short_name)
            self.addElement(data_type)
        return self.getElement(short_name)

    def createApplicationRecordDataType(self, short_name: str) -> ApplicationPrimitiveDataType:
        if (not self.IsElementExists(short_name)):
            data_type = ApplicationRecordDataType(self, short_name)
            self.addElement(data_type)
        return self.getElement(short_name)

    def createImplementationDataType(self, short_name: str) -> ImplementationDataType:
        if (not self.IsElementExists(short_name)):
            data_type = ImplementationDataType(self, short_name)
            self.addElement(data_type)
        return self.getElement(short_name)

    def createSwBaseType(self, short_name: str) -> SwBaseType:
        if (not self.IsElementExists(short_name)):
            base_type = SwBaseType(self, short_name)
            self.addElement(base_type)
        return self.getElement(short_name)

    def createDataTypeMappingSet(self, short_name: str) -> DataTypeMappingSet:
        if (not self.IsElementExists(short_name)):
            mapping_set = DataTypeMappingSet(self, short_name)
            self.addElement(mapping_set)
        return self.getElement(short_name)

    def createCompuMethod(self, short_name: str) -> CompuMethod:
        if (not self.IsElementExists(short_name)):
            compu_method = CompuMethod(self, short_name)
            self.addElement(compu_method)
        return self.getElement(short_name)

    def createBswModuleDescription(self, short_name: str) -> BswModuleDescription:
        if (not self.IsElementExists(short_name)):
            desc = BswModuleDescription(self, short_name)
            self.addElement(desc)
        return self.getElement(short_name)

    def createBswModuleEntry(self, short_name: str) -> BswModuleEntry:
        if (not self.IsElementExists(short_name)):
            entry = BswModuleEntry(self, short_name)
            self.addElement(entry)
        return self.getElement(short_name)

    def createBswImplementation(self, short_name: str) -> BswImplementation:
        if (not self.IsElementExists(short_name)):
            impl = BswImplementation(self, short_name)
            self.addElement(impl)
        return self.getElement(short_name)

    def createSwcImplementation(self, short_name: str) -> SwcImplementation:
        if (not self.IsElementExists(short_name)):
            impl = SwcImplementation(self, short_name)
            self.addElement(impl)
        return self.getElement(short_name)

    def createSwcBswMapping(self, short_name: str) -> SwcBswMapping:
        if (not self.IsElementExists(short_name)):
            mapping = SwcBswMapping(self, short_name)
            self.addElement(mapping)
        return self.getElement(short_name)

    def createConstantSpecification(self, short_name: str) -> ConstantSpecification:
        if (not self.IsElementExists(short_name)):
            spec = ConstantSpecification(self, short_name)
            self.addElement(spec)
        return self.getElement(short_name)

    def createDataConstr(self, short_name: str) -> DataConstr:
        if (not self.IsElementExists(short_name)):
            constr = DataConstr(self, short_name)
            self.addElement(constr)
        return self.getElement(short_name)

    def createUnit(self, short_name: str) -> Unit:
        if (not self.IsElementExists(short_name)):
            unit = Unit(self, short_name)
            self.addElement(unit)
        return self.getElement(short_name)

    def createEndToEndProtectionSet(self, short_name: str) -> EndToEndProtectionSet:
        if (not self.IsElementExists(short_name)):
            e2d_set = EndToEndProtectionSet(self, short_name)
            self.addElement(e2d_set)
        return self.getElement(short_name)

    def createApplicationArrayDataType(self, short_name: str) -> ApplicationArrayDataType:
        if (not self.IsElementExists(short_name)):
            data_type = ApplicationArrayDataType(self, short_name)
            self.addElement(data_type)
        return self.getElement(short_name)

    def createSwRecordLayout(self, short_name: str) -> SwRecordLayout:
        if (not self.IsElementExists(short_name)):
            layout = SwRecordLayout(self, short_name)
            self.addElement(layout)
        return self.getElement(short_name)

    def createSwAddrMethod(self, short_name: str) -> SwAddrMethod:
        if (not self.IsElementExists(short_name)):
            method = SwAddrMethod(self, short_name)
            self.addElement(method)
        return self.getElement(short_name)

    def createTriggerInterface(self, short_name: str) -> TriggerInterface:
        if (not self.IsElementExists(short_name)):
            trigger_interface = TriggerInterface(self, short_name)
            self.addElement(trigger_interface)
        return trigger_interface

    def createModeDeclarationGroup(self, short_name: str) -> ModeDeclarationGroup:
        if (not self.IsElementExists(short_name)):
            group = ModeDeclarationGroup(self, short_name)
            self.addElement(group)
        return self.getElement(short_name)

    def createModeSwitchInterface(self, short_name: str) -> ModeSwitchInterface:
        if (not self.IsElementExists(short_name)):
            switch_interface = ModeSwitchInterface(self, short_name)
            self.addElement(switch_interface)
        return self.getElement(short_name)

    def createSwcTiming(self, short_name: str) -> SwcTiming:
        if (not self.IsElementExists(short_name)):
            timing = SwcTiming(self, short_name)
            self.addElement(timing)
        return self.getElement(short_name)

    def createLinCluster(self, short_name: str) -> LinCluster:
        if (not self.IsElementExists(short_name)):
            cluster = LinCluster(self, short_name)
            self.addElement(cluster)
        return self.getElement(short_name)

    def createCanCluster(self, short_name: str) -> CanCluster:
        if (not self.IsElementExists(short_name)):
            cluster = CanCluster(self, short_name)
            self.addElement(cluster)
        return self.getElement(short_name)

    def createLinUnconditionalFrame(self, short_name: str) -> LinUnconditionalFrame:
        if (not self.IsElementExists(short_name)):
            frame = LinUnconditionalFrame(self, short_name)
            self.addElement(frame)
        return self.getElement(short_name)

    def createNmPdu(self, short_name: str) -> NmPdu:
        if (not self.IsElementExists(short_name)):
            element = NmPdu(self, short_name)
            self.addElement(element)
        return self.getElement(short_name)

    def createNPdu(self, short_name: str) -> NPdu:
        if (not self.IsElementExists(short_name)):
            element = NPdu(self, short_name)
            self.addElement(element)
        return self.getElement(short_name)

    def createDcmIPdu(self, short_name: str) -> DcmIPdu:
        if (not self.IsElementExists(short_name)):
            element = DcmIPdu(self, short_name)
            self.addElement(element)
        return self.getElement(short_name)

    def createSecuredIPdu(self, short_name: str) -> SecuredIPdu:
        if (not self.IsElementExists(short_name)):
            element = SecuredIPdu(self, short_name)
            self.addElement(element)
        return self.getElement(short_name)

    def createNmConfig(self, short_name: str) -> NmConfig:
        if (not self.IsElementExists(short_name)):
            element = NmConfig(self, short_name)
            self.addElement(element)
        return self.getElement(short_name)

    def createCanTpConfig(self, short_name: str) -> CanTpConfig:
        if (not self.IsElementExists(short_name)):
            element = CanTpConfig(self, short_name)
            self.addElement(element)
        return self.getElement(short_name)
    
    def createLinTpConfig(self, short_name: str) -> LinTpConfig:
        if (not self.IsElementExists(short_name)):
            element = LinTpConfig(self, short_name)
            self.addElement(element)
        return self.getElement(short_name)

    def createCanFrame(self, short_name: str) -> CanFrame:
        if (not self.IsElementExists(short_name)):
            element = CanFrame(self, short_name)
            self.addElement(element)
        return self.getElement(short_name)

    def createEcuInstance(self, short_name: str) -> EcuInstance:
        if (not self.IsElementExists(short_name)):
            element = EcuInstance(self, short_name)
            self.addElement(element)
        return self.getElement(short_name)

    def createGateway(self, short_name: str) -> Gateway:
        if (not self.IsElementExists(short_name)):
            element = Gateway(self, short_name)
            self.addElement(element)
        return self.getElement(short_name)

    def createISignal(self, short_name: str) -> ISignal:
        if (not self.IsElementExists(short_name)):
            element = ISignal(self, short_name)
            self.addElement(element)
        return self.getElement(short_name)

    def createSystemSignal(self, short_name: str) -> SystemSignal:
        if (not self.IsElementExists(short_name)):
            element = SystemSignal(self, short_name)
            self.addElement(element)
        return self.getElement(short_name)

    def createSystemSignalGroup(self, short_name: str) -> SystemSignalGroup:
        if (not self.IsElementExists(short_name)):
            element = SystemSignalGroup(self, short_name)
            self.addElement(element)
        return self.getElement(short_name)

    def createISignalIPdu(self, short_name: str) -> ISignalIPdu:
        if (not self.IsElementExists(short_name)):
            element = ISignalIPdu(self, short_name)
            self.addElement(element)
        return self.getElement(short_name)

    def createEcucValueCollection(self, short_name: str) -> EcucValueCollection:
        if (not self.IsElementExists(short_name)):
            element = EcucValueCollection(self, short_name)
            self.addElement(element)
        return self.getElement(short_name)

    def createEcucModuleConfigurationValues(self, short_name: str) -> EcucModuleConfigurationValues:
        if (not self.IsElementExists(short_name)):
            element = EcucModuleConfigurationValues(self, short_name)
            self.addElement(element)
        return self.getElement(short_name)
    
    def createEcucModuleDef(self, short_name: str) -> EcucModuleDef:
        if (not self.IsElementExists(short_name)):
            element = EcucModuleDef(self, short_name)
            self.addElement(element)
        return self.getElement(short_name)

    def createPhysicalDimension(self, short_name: str) -> PhysicalDimension:
        if (not self.IsElementExists(short_name)):
            element = PhysicalDimension(self, short_name)
            self.addElement(element)
        return self.getElement(short_name)

    def createISignalGroup(self, short_name: str) -> ISignalGroup:
        if (not self.IsElementExists(short_name)):
            element = ISignalGroup(self, short_name)
            self.addElement(element)
        return self.getElement(short_name)

    def createISignalIPduGroup(self, short_name: str) -> ISignalIPduGroup:
        if (not self.IsElementExists(short_name)):
            element = ISignalIPduGroup(self, short_name)
            self.addElement(element)
        return self.getElement(short_name)

    def createSystem(self, short_name: str) -> System:
        if (not self.IsElementExists(short_name)):
            element = System(self, short_name)
            self.addElement(element)
        return self.getElement(short_name)
    
    def createFlatMap(self, short_name: str) -> FlatMap:
        if (not self.IsElementExists(short_name)):
            map = FlatMap(self, short_name)
            self.addElement(map)
        return self.getElement(short_name)
    
    def createPortInterfaceMappingSet(self, short_name: str) -> PortInterfaceMappingSet:
        if (not self.IsElementExists(short_name)):
            map_set = PortInterfaceMappingSet(self, short_name)
            self.addElement(map_set)
        return self.getElement(short_name)
    
    def createEthernetCluster(self, short_name: str) -> EthernetCluster:
        if (not self.IsElementExists(short_name)):
            cluster = EthernetCluster(self, short_name)
            self.addElement(cluster)
        return self.getElement(short_name)
    
    def createDiagnosticConnection(self, short_name: str) -> DiagnosticConnection:
        if (not self.IsElementExists(short_name)):
            connection = DiagnosticConnection(self, short_name)
            self.addElement(connection)
        return self.getElement(short_name)
    
    def createDiagnosticServiceTable(self, short_name: str) -> DiagnosticServiceTable:
        if (not self.IsElementExists(short_name)):
            table = DiagnosticServiceTable(self, short_name)
            self.addElement(table)
        return self.getElement(short_name)
    
    def createMultiplexedIPdu(self, short_name: str) -> MultiplexedIPdu:
        if (not self.IsElementExists(short_name)):
            ipdu = MultiplexedIPdu(self, short_name)
            self.addElement(ipdu)
        return self.getElement(short_name)
    
    def createUserDefinedIPdu(self, short_name: str) -> UserDefinedIPdu:
        if (not self.IsElementExists(short_name)):
            ipdu = UserDefinedIPdu(self, short_name)
            self.addElement(ipdu)
        return self.getElement(short_name)
    
    def createUserDefinedPdu(self, short_name: str) -> UserDefinedPdu:
        if (not self.IsElementExists(short_name)):
            pdu = UserDefinedPdu(self, short_name)
            self.addElement(pdu)
        return self.getElement(short_name)
    
    def createGeneralPurposeIPdu(self, short_name: str) -> GeneralPurposeIPdu:
        if (not self.IsElementExists(short_name)):
            i_pdu = GeneralPurposeIPdu(self, short_name)
            self.addElement(i_pdu)
        return self.getElement(short_name)
    
    def createGeneralPurposePdu(self, short_name: str) -> GeneralPurposePdu:
        if (not self.IsElementExists(short_name)):
            pdu = GeneralPurposePdu(self, short_name)
            self.addElement(pdu)
        return self.getElement(short_name)
    
    def createSecureCommunicationPropsSet(self, short_name: str) -> SecureCommunicationPropsSet:
        if (not self.IsElementExists(short_name)):
            props_set = SecureCommunicationPropsSet(self, short_name)
            self.addElement(props_set)
        return self.getElement(short_name)
    
    def createSoAdRoutingGroup(self, short_name: str) -> SoAdRoutingGroup:
        if (not self.IsElementExists(short_name)):
            group = SoAdRoutingGroup(self, short_name)
            self.addElement(group)
        return self.getElement(short_name)
    
    def createDoIpTpConfig(self, short_name: str) -> DoIpTpConfig:
        if (not self.IsElementExists(short_name)):
            tp_config = DoIpTpConfig(self, short_name)
            self.addElement(tp_config)
        return self.getElement(short_name)
    
    def createHwElement(self, short_name: str) -> HwElement:
        if (not self.IsElementExists(short_name)):
            hw_element = HwElement(self, short_name)
            self.addElement(hw_element)
        return self.getElement(short_name)
    
    def createHwCategory(self, short_name: str) -> HwCategory:
        if (not self.IsElementExists(short_name)):
            hw_category = HwCategory(self, short_name)
            self.addElement(hw_category)
        return self.getElement(short_name)
    
    def createHwType(self, short_name: str) -> HwType:
        if (not self.IsElementExists(short_name)):
            hw_category = HwType(self, short_name)
            self.addElement(hw_category)
        return self.getElement(short_name)
    
    def createFlexrayFrame(self, short_name: str) -> FlexrayFrame:
        if (not self.IsElementExists(short_name)):
            frame = FlexrayFrame(self, short_name)
            self.addElement(frame)
        return self.getElement(short_name)
    
    def createFlexrayCluster(self, short_name: str) -> FlexrayCluster:
        if (not self.IsElementExists(short_name)):
            frame = FlexrayCluster(self, short_name)
            self.addElement(frame)
        return self.getElement(short_name)
    
    def createDataTransformationSet(self, short_name: str) -> DataTransformationSet:
        if (not self.IsElementExists(short_name)):
            transform_set = DataTransformationSet(self, short_name)
            self.addElement(transform_set)
        return self.getElement(short_name)
    
    def createCollection(self, short_name: str) -> Collection:
        if (not self.IsElementExists(short_name)):
            collection = Collection(self, short_name)
            self.addElement(collection)
        return self.getElement(short_name)
    
    def createKeywordSet(self, short_name: str) -> KeywordSet:
        if (not self.IsElementExists(short_name)):
            keyword_set = KeywordSet(self, short_name)
            self.addElement(keyword_set)
        return self.getElement(short_name)
    
    def createPortPrototypeBlueprint(self, short_name: str) -> PortPrototypeBlueprint:
        if (not self.IsElementExists(short_name)):
            keyword_set = PortPrototypeBlueprint(self, short_name)
            self.addElement(keyword_set)
        return self.getElement(short_name)
    
    def createModeDeclarationMappingSet(self, short_name: str) -> ModeDeclarationMappingSet:
        if (not self.IsElementExists(short_name)):
            mapping_set = ModeDeclarationMappingSet(self, short_name)
            self.addElement(mapping_set)
        return self.getElement(short_name)

    def getApplicationPrimitiveDataTypes(self) -> List[ApplicationPrimitiveDataType]:
        return list(sorted(filter(lambda a: isinstance(a, ApplicationPrimitiveDataType), self.elements.values()), key=lambda o: o.short_name))

    def getApplicationDataType(self) -> List[ApplicationDataType]:
        return list(sorted(filter(lambda a: isinstance(a, ApplicationDataType), self.elements.values()), key=lambda o: o.short_name))

    def getImplementationDataTypes(self) -> List[ImplementationDataType]:
        return list(sorted(filter(lambda a: isinstance(a, ImplementationDataType), self.elements.values()), key=lambda o: o.short_name))

    def getSwBaseTypes(self) -> List[SwBaseType]:
        return list(filter(lambda a: isinstance(a, SwBaseType), self.elements.values()))

    def getSwComponentTypes(self) -> List[SwComponentType]:
        return list(filter(lambda a: isinstance(a, SwComponentType), self.elements.values()))

    def getSensorActuatorSwComponentType(self) -> List[SensorActuatorSwComponentType]:
        return list(filter(lambda a: isinstance(a, SensorActuatorSwComponentType), self.elements.values()))

    def getAtomicSwComponentTypes(self) -> List[AtomicSwComponentType]:
        return list(filter(lambda a: isinstance(a, AtomicSwComponentType), self.elements.values()))

    def getCompositionSwComponentTypes(self) -> List[CompositionSwComponentType]:
        return list(filter(lambda a: isinstance(a, CompositionSwComponentType), self.elements.values()))

    def getComplexDeviceDriverSwComponentTypes(self) -> List[ComplexDeviceDriverSwComponentType]:
        return list(sorted(filter(lambda a: isinstance(a, ComplexDeviceDriverSwComponentType), self.elements.values()), key=lambda a: a.short_name))

    def getSenderReceiverInterfaces(self) -> List[SenderReceiverInterface]:
        return list(sorted(filter(lambda a: isinstance(a, SenderReceiverInterface), self.elements.values()), key=lambda a: a.short_name))

    def getParameterInterfaces(self) -> List[ParameterInterface]:
        return list(sorted(filter(lambda a: isinstance(a, ParameterInterface), self.elements.values()), key=lambda a: a.short_name))

    def getClientServerInterfaces(self) -> List[ClientServerInterface]:
        return list(sorted(filter(lambda a: isinstance(a, ClientServerInterface), self.elements.values()), key=lambda a: a.short_name))

    def getDataTypeMappingSets(self) -> List[DataTypeMappingSet]:
        return list(sorted(filter(lambda a: isinstance(a, DataTypeMappingSet), self.elements.values()), key=lambda a: a.short_name))

    def getCompuMethods(self) -> List[CompuMethod]:
        return list(filter(lambda a: isinstance(a, CompuMethod), self.elements.values()))

    def getBswModuleDescriptions(self) -> List[BswModuleDescription]:
        return list(filter(lambda a: isinstance(a, BswModuleDescription), self.elements.values()))

    def getBswModuleEntries(self) -> List[BswModuleEntry]:
        return list(filter(lambda a: isinstance(a, BswModuleEntry), self.elements.values()))

    def getBswImplementations(self) -> List[BswImplementation]:
        return list(filter(lambda a: isinstance(a, BswImplementation), self.elements.values()))

    def getSwcImplementations(self) -> List[SwcImplementation]:
        return list(filter(lambda a: isinstance(a, SwcImplementation), self.elements.values()))

    def getImplementations(self) -> List[Implementation]:
        return list(filter(lambda a: isinstance(a, Implementation), self.elements.values()))

    def getSwcBswMappings(self) -> List[SwcBswMapping]:
        return list(filter(lambda a: isinstance(a, SwcBswMapping), self.elements.values()))

    def getConstantSpecifications(self) -> List[ConstantSpecification]:
        return list(filter(lambda a: isinstance(a, ConstantSpecification), self.elements.values()))

    def getDataConstrs(self) -> List[DataConstr]:
        return list(filter(lambda a: isinstance(a, DataConstr), self.elements.values()))

    def getUnits(self) -> List[Unit]:
        return list(filter(lambda a: isinstance(a, Unit), self.elements.values()))

    def getApplicationArrayDataTypes(self) -> List[ApplicationArrayDataType]:
        return list(sorted(filter(lambda a: isinstance(a, ApplicationArrayDataType), self.elements.values()), key=lambda a: a.short_name))

    def getSwRecordLayouts(self) -> List[SwRecordLayout]:
        return list(sorted(filter(lambda a: isinstance(a, SwRecordLayout), self.elements.values()), key=lambda a: a.short_name))

    def getSwAddrMethods(self) -> List[SwAddrMethod]:
        return list(sorted(filter(lambda a: isinstance(a, SwAddrMethod), self.elements.values()), key=lambda a: a.short_name))

    def getTriggerInterfaces(self) -> List[TriggerInterface]:
        return list(sorted(filter(lambda a: isinstance(a, TriggerInterface), self.elements.values()), key=lambda a: a.short_name))

    def getModeDeclarationGroups(self) -> List[ModeDeclarationGroup]:
        return list(sorted(filter(lambda a: isinstance(a, ModeDeclarationGroup), self.elements.values()), key=lambda a: a.short_name))

    def getModeSwitchInterfaces(self) -> List[ModeSwitchInterface]:
        return list(sorted(filter(lambda a: isinstance(a, ModeSwitchInterface), self.elements.values()), key=lambda a: a.short_name))

    def getSwcTimings(self) -> List[SwcTiming]:
        return list(sorted(filter(lambda a: isinstance(a, SwcTiming), self.elements.values()), key=lambda a: a.short_name))

    def getLinClusters(self) -> List[LinCluster]:
        return list(sorted(filter(lambda a: isinstance(a, LinCluster), self.elements.values()), key=lambda a: a.short_name))

    def getCanClusters(self) -> List[CanCluster]:
        return list(sorted(filter(lambda a: isinstance(a, CanCluster), self.elements.values()), key=lambda a: a.short_name))

    def getLinUnconditionalFrames(self) -> List[LinUnconditionalFrame]:
        return list(sorted(filter(lambda a: isinstance(a, LinUnconditionalFrame), self.elements.values()), key=lambda a: a.short_name))

    def getNmPdus(self) -> List[NmPdu]:
        return list(sorted(filter(lambda a: isinstance(a, NmPdu), self.elements.values()), key=lambda a: a.short_name))

    def getNPdus(self) -> List[NPdu]:
        return list(sorted(filter(lambda a: isinstance(a, NPdu), self.elements.values()), key=lambda a: a.short_name))

    def getDcmIPdus(self) -> List[DcmIPdu]:
        return list(sorted(filter(lambda a: isinstance(a, DcmIPdu), self.elements.values()), key=lambda a: a.short_name))

    def getSecuredIPdus(self) -> List[SecuredIPdu]:
        return list(sorted(filter(lambda a: isinstance(a, SecuredIPdu), self.elements.values()), key=lambda a: a.short_name))

    def getNmConfigs(self) -> List[NmConfig]:
        return list(sorted(filter(lambda a: isinstance(a, NmConfig), self.elements.values()), key=lambda a: a.short_name))

    def getCanTpConfigs(self) -> List[CanTpConfig]:
        return list(sorted(filter(lambda a: isinstance(a, CanTpConfig), self.elements.values()), key=lambda a: a.short_name))

    def getCanFrames(self) -> List[CanFrame]:
        return list(sorted(filter(lambda a: isinstance(a, CanFrame), self.elements.values()), key=lambda a: a.short_name))

    def getEcuInstances(self) -> List[EcuInstance]:
        return list(sorted(filter(lambda a: isinstance(a, EcuInstance), self.elements.values()), key=lambda a: a.short_name))

    def getGateways(self) -> List[Gateway]:
        return list(sorted(filter(lambda a: isinstance(a, Gateway), self.elements.values()), key=lambda a: a.short_name))

    def getISignals(self) -> List[ISignal]:
        return list(sorted(filter(lambda a: isinstance(a, ISignal), self.elements.values()), key=lambda a: a.short_name))

    def getEcucValueCollections(self) -> List[EcucValueCollection]:
        return list(sorted(filter(lambda a: isinstance(a, EcucValueCollection), self.elements.values()), key=lambda a: a.short_name))

    def getEcucModuleConfigurationValues(self) -> List[EcucModuleConfigurationValues]:
        return list(sorted(filter(lambda a: isinstance(a, EcucModuleConfigurationValues), self.elements.values()), key=lambda a: a.short_name))
    
    def getEcucModuleDefs(self) -> List[EcucModuleDef]:
        return list(sorted(filter(lambda a: isinstance(a, EcucModuleDef), self.elements.values()), key=lambda a: a.short_name))

    def getEcucPhysicalDimensions(self) -> List[PhysicalDimension]:
        return list(sorted(filter(lambda a: isinstance(a, PhysicalDimension), self.elements.values()), key=lambda a: a.short_name))

    def getISignalGroups(self) -> List[ISignalGroup]:
        return list(sorted(filter(lambda a: isinstance(a, ISignalGroup), self.elements.values()), key=lambda a: a.short_name))

    def getSystemSignals(self) -> List[SystemSignal]:
        return list(sorted(filter(lambda a: isinstance(a, SystemSignal), self.elements.values()), key=lambda a: a.short_name))

    def getSystemSignalGroups(self) -> List[SystemSignalGroup]:
        return list(sorted(filter(lambda a: isinstance(a, SystemSignalGroup), self.elements.values()), key=lambda a: a.short_name))

    def getISignalIPdus(self) -> List[ISignalIPdu]:
        return list(sorted(filter(lambda a: isinstance(a, ISignalIPdu), self.elements.values()), key=lambda a: a.short_name))

    def getSystems(self) -> List[System]:
        return list(sorted(filter(lambda a: isinstance(a, System), self.elements.values()), key=lambda a: a.short_name))
    
    def getHwElements(self) -> List[HwElement]:
        return list(sorted(filter(lambda a: isinstance(a, HwElement), self.elements.values()), key=lambda a: a.short_name))
    
    def getHwCategories(self) -> List[HwCategory]:
        return list(sorted(filter(lambda a: isinstance(a, HwCategory), self.elements.values()), key=lambda a: a.short_name))
    
    def getFlexrayFrames(self) -> List[FlexrayFrame]:
        return list(sorted(filter(lambda a: isinstance(a, FlexrayFrame), self.elements.values()), key=lambda a: a.short_name))
    
    def getDataTransformationSets(self) -> List[DataTransformationSet]:
        return list(sorted(filter(lambda a: isinstance(a, DataTransformationSet), self.elements.values()), key=lambda a: a.short_name))
    
    def getCollections(self) -> List[Collection]:
        return list(sorted(filter(lambda a: isinstance(a, Collection), self.elements.values()), key=lambda a: a.short_name))
    
    def getKeywordSets(self) -> List[KeywordSet]:
        return list(sorted(filter(lambda a: isinstance(a, KeywordSet), self.elements.values()), key=lambda a: a.short_name))
    
    def getPortPrototypeBlueprints(self) -> List[PortPrototypeBlueprint]:
        return list(sorted(filter(lambda a: isinstance(a, PortPrototypeBlueprint), self.elements.values()), key=lambda a: a.short_name))
    
    def getModeDeclarationMappingSets(self) -> List[ModeDeclarationMappingSet]:
        return list(sorted(filter(lambda a: isinstance(a, ModeDeclarationMappingSet), self.elements.values()), key=lambda a: a.short_name))
    
    def getReferenceBases(self):
        return self.referenceBases

    def addReferenceBase(self, value):
        self.referenceBases.append(value)
        return self
