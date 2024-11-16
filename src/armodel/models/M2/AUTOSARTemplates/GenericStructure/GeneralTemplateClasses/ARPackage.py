from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable import CollectableElement
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable import Identifiable, Referrable
from armodel.models.M2.MSR.AsamHdo.BaseTypes import SwBaseType
from armodel.models.bsw_module_template import BswModuleDescription, BswModuleEntry
from armodel.models.common_structure import ModeDeclarationGroup
from armodel.models.datatype import ApplicationArrayDataType, ApplicationDataType, ApplicationPrimitiveDataType, ApplicationRecordDataType, DataTypeMappingSet
from armodel.models.end_to_end_protection import EndToEndProtectionSet
from armodel.models.fibex.can_communication import CanFrame
from armodel.models.fibex.fibex_4_multiplatform import Gateway
from armodel.models.fibex.fibex_core.core_communication import DcmIPdu, ISignal, ISignalGroup, ISignalIPdu, ISignalIPduGroup, NPdu, NmPdu, SecuredIPdu, SystemSignal, SystemSignalGroup
from armodel.models.fibex.fibex_core.core_topology import CanCluster, EcuInstance, LinCluster
from armodel.models.fibex.lin_communication import LinUnconditionalFrame
from armodel.models.M2.AUTOSARTemplates.CommonStructure.SwcBswMapping import SwcBswMapping
from armodel.models.global_constraints import DataConstr
from armodel.models.implementation import BswImplementation, Implementation, SwcImplementation
from armodel.models.M2.AUTOSARTemplates.CommonStructure import ConstantSpecification
from armodel.models.M2.AUTOSARTemplates.CommonStructure.implementation_data_types import ImplementationDataType
from armodel.models.M2.AUTOSARTemplates.ecuc_description_template import EcucModuleConfigurationValues, EcucValueCollection
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.components import SwComponentType
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.composition import CompositionSwComponentType
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.port_interface import ClientServerInterface, ModeSwitchInterface, ParameterInterface, SenderReceiverInterface, TriggerInterface
from armodel.models.M2.AUTOSARTemplates.system_template import System
from armodel.models.M2.AUTOSARTemplates.system_template.network_management import NmConfig
from armodel.models.M2.AUTOSARTemplates.system_template.transport_protocols import CanTpConfig
from armodel.models.M2.MSR.AsamHdo.Units import PhysicalDimension, Unit
from armodel.models.M2.MSR.data_dictionary.auxillary_objects import SwAddrMethod
from armodel.models.M2.MSR.AsamHdo.ComputationMethod import CompuMethod
from armodel.models.record_layout import SwRecordLayout
from armodel.models.sw_component import ApplicationSwComponentType, AtomicSwComponentType, ComplexDeviceDriverSwComponentType, EcuAbstractionSwComponentType, SensorActuatorSwComponentType, ServiceSwComponentType
from armodel.models.timing import SwcTiming

from typing import Dict, List

class ARPackage(Identifiable, CollectableElement):
    def __init__(self, parent: ARObject, short_name: str):
        Identifiable.__init__(self, parent, short_name)
        CollectableElement.__init__(self)

        self._ar_packages = {}      # type: Dict[str, ARPackage]

    def getARPackages(self):    # type: (...) -> List[ARPackage]
        return list(sorted(self._ar_packages.values(), key= lambda a: a.short_name))
        #return list(filter(lambda e: isinstance(e, ARPackage), self.elements.values()))

    def createARPackage(self, short_name: str):
        '''
        if (short_name not in self.elements):
            ar_package = ARPackage(self, short_name)
            self.elements[short_name] = ar_package
        return self.elements[short_name]
        '''
        if short_name not in self._ar_packages:
            ar_package = ARPackage(self, short_name)
            self._ar_packages[short_name] = ar_package
        return self._ar_packages[short_name]

    def getElement(self, short_name: str) -> Referrable:
        if (short_name in self._ar_packages):
            return self._ar_packages[short_name]
        return CollectableElement.getElement(self, short_name)

    def createEcuAbstractionSwComponentType(self, short_name: str) -> EcuAbstractionSwComponentType:
        if (short_name not in self.elements):
            sw_component = EcuAbstractionSwComponentType(self, short_name)
            self.addElement(sw_component)
        return self.getElement(short_name)

    def createApplicationSwComponentType(self, short_name: str) -> ApplicationSwComponentType:
        if short_name not in self.elements:
            sw_component = ApplicationSwComponentType(self, short_name)
            self.addElement(sw_component)
        return self.getElement(short_name)

    def createComplexDeviceDriverSwComponentType(self, short_name: str) -> ComplexDeviceDriverSwComponentType:
        if short_name not in self.elements:
            sw_component = ComplexDeviceDriverSwComponentType(self, short_name)
            self.addElement(sw_component)
        return self.getElement(short_name)

    def createServiceSwComponentType(self, short_name: str) -> ServiceSwComponentType:
        if (short_name not in self.elements):
            sw_component = ServiceSwComponentType(self, short_name)
            self.addElement(sw_component)
        return self.getElement(short_name)

    def createSensorActuatorSwComponentType(self, short_name: str) -> SensorActuatorSwComponentType:
        if (short_name not in self.elements):
            sw_component = SensorActuatorSwComponentType(self, short_name)
            self.addElement(sw_component)
        return self.getElement(short_name)

    def createCompositionSwComponentType(self, short_name: str) -> CompositionSwComponentType:
        if (short_name not in self.elements):
            sw_component = CompositionSwComponentType(self, short_name)
            self.addElement(sw_component)
        return self.getElement(short_name)

    def createSenderReceiverInterface(self, short_name: str) -> SenderReceiverInterface:
        if (short_name not in self.elements):
            sr_interface = SenderReceiverInterface(self, short_name)
            self.addElement(sr_interface)
        return self.getElement(short_name)

    def createParameterInterface(self, short_name: str) -> ParameterInterface:
        if (short_name not in self.elements):
            sr_interface = ParameterInterface(self, short_name)
            self.addElement(sr_interface)
        return self.getElement(short_name)

    def createClientServerInterface(self, short_name: str) -> ClientServerInterface:
        if (short_name not in self.elements):
            cs_interface = ClientServerInterface(self, short_name)
            self.addElement(cs_interface)
        return self.getElement(short_name)

    def createApplicationPrimitiveDataType(self, short_name: str) -> ApplicationPrimitiveDataType:
        if (short_name not in self.elements):
            data_type = ApplicationPrimitiveDataType(self, short_name)
            self.addElement(data_type)
        return self.getElement(short_name)

    def createApplicationRecordDataType(self, short_name: str) -> ApplicationPrimitiveDataType:
        if (short_name not in self.elements):
            data_type = ApplicationRecordDataType(self, short_name)
            self.addElement(data_type)
        return self.getElement(short_name)

    def createImplementationDataType(self, short_name: str) -> ImplementationDataType:
        if (short_name not in self.elements):
            data_type = ImplementationDataType(self, short_name)
            self.addElement(data_type)
        return self.getElement(short_name)

    def createSwBaseType(self, short_name: str) -> SwBaseType:
        if (short_name not in self.elements):
            base_type = SwBaseType(self, short_name)
            self.addElement(base_type)
        return self.getElement(short_name)

    def createDataTypeMappingSet(self, short_name: str) -> DataTypeMappingSet:
        if (short_name not in self.elements):
            mapping_set = DataTypeMappingSet(self, short_name)
            self.addElement(mapping_set)
        return self.getElement(short_name)

    def createCompuMethod(self, short_name: str) -> CompuMethod:
        if (short_name not in self.elements):
            compu_method = CompuMethod(self, short_name)
            self.addElement(compu_method)
        return self.getElement(short_name)

    def createBswModuleDescription(self, short_name: str) -> BswModuleDescription:
        if (short_name not in self.elements):
            desc = BswModuleDescription(self, short_name)
            self.addElement(desc)
        return self.getElement(short_name)

    def createBswModuleEntry(self, short_name: str) -> BswModuleEntry:
        if (short_name not in self.elements):
            entry = BswModuleEntry(self, short_name)
            self.addElement(entry)
        return self.getElement(short_name)

    def createBswImplementation(self, short_name: str) -> BswImplementation:
        if (short_name not in self.elements):
            impl = BswImplementation(self, short_name)
            self.addElement(impl)
        return self.getElement(short_name)

    def createSwcImplementation(self, short_name: str) -> SwcImplementation:
        if (short_name not in self.elements):
            impl = SwcImplementation(self, short_name)
            self.addElement(impl)
        return self.getElement(short_name)

    def createSwcBswMapping(self, short_name: str) -> SwcBswMapping:
        if (short_name not in self.elements):
            mapping = SwcBswMapping(self, short_name)
            self.addElement(mapping)
        return self.getElement(short_name)

    def createConstantSpecification(self, short_name: str) -> ConstantSpecification:
        if (short_name not in self.elements):
            spec = ConstantSpecification(self, short_name)
            self.addElement(spec)
        return self.getElement(short_name)

    def createDataConstr(self, short_name: str) -> DataConstr:
        if (short_name not in self.elements):
            constr = DataConstr(self, short_name)
            self.addElement(constr)
        return self.getElement(short_name)

    def createUnit(self, short_name: str) -> Unit:
        if (short_name not in self.elements):
            unit = Unit(self, short_name)
            self.addElement(unit)
        return self.getElement(short_name)

    def createEndToEndProtectionSet(self, short_name: str) -> EndToEndProtectionSet:
        if (short_name not in self.elements):
            e2d_set = EndToEndProtectionSet(self, short_name)
            self.addElement(e2d_set)
        return self.getElement(short_name)

    def createApplicationArrayDataType(self, short_name: str) -> ApplicationArrayDataType:
        if (short_name not in self.elements):
            data_type = ApplicationArrayDataType(self, short_name)
            self.addElement(data_type)
        return self.getElement(short_name)

    def createSwRecordLayout(self, short_name: str) -> SwRecordLayout:
        if (short_name not in self.elements):
            layout = SwRecordLayout(self, short_name)
            self.addElement(layout)
        return self.getElement(short_name)

    def createSwAddrMethod(self, short_name: str) -> SwAddrMethod:
        if (short_name not in self.elements):
            method = SwAddrMethod(self, short_name)
            self.addElement(method)
        return self.getElement(short_name)

    def createTriggerInterface(self, short_name: str) -> TriggerInterface:
        if (short_name not in self.elements):
            trigger_interface = TriggerInterface(self, short_name)
            self.addElement(trigger_interface)
        return trigger_interface

    def createModeDeclarationGroup(self, short_name: str) -> ModeDeclarationGroup:
        if (short_name not in self.elements):
            group = ModeDeclarationGroup(self, short_name)
            self.addElement(group)
        return self.getElement(short_name)

    def createModeSwitchInterface(self, short_name: str) -> ModeSwitchInterface:
        if (short_name not in self.elements):
            switch_interface = ModeSwitchInterface(self, short_name)
            self.addElement(switch_interface)
        return self.getElement(short_name)

    def createSwcTiming(self, short_name: str) -> SwcTiming:
        if (short_name not in self.elements):
            timing = SwcTiming(self, short_name)
            self.addElement(timing)
        return self.getElement(short_name)

    def createLinCluster(self, short_name: str) -> LinCluster:
        if (short_name not in self.elements):
            cluster = LinCluster(self, short_name)
            self.addElement(cluster)
        return self.getElement(short_name)

    def createCanCluster(self, short_name: str) -> CanCluster:
        if (short_name not in self.elements):
            cluster = CanCluster(self, short_name)
            self.addElement(cluster)
        return self.getElement(short_name)

    def createLinUnconditionalFrame(self, short_name: str) -> LinUnconditionalFrame:
        if (short_name not in self.elements):
            frame = LinUnconditionalFrame(self, short_name)
            self.addElement(frame)
        return self.getElement(short_name)

    def createNmPdu(self, short_name: str) -> NmPdu:
        if (short_name not in self.elements):
            element = NmPdu(self, short_name)
            self.addElement(element)
        return self.getElement(short_name)

    def createNPdu(self, short_name: str) -> NPdu:
        if (short_name not in self.elements):
            element = NPdu(self, short_name)
            self.addElement(element)
        return self.getElement(short_name)

    def createDcmIPdu(self, short_name: str) -> DcmIPdu:
        if (short_name not in self.elements):
            element = DcmIPdu(self, short_name)
            self.addElement(element)
        return self.getElement(short_name)

    def createSecuredIPdu(self, short_name: str) -> SecuredIPdu:
        if (short_name not in self.elements):
            element = SecuredIPdu(self, short_name)
            self.addElement(element)
        return self.getElement(short_name)

    def createNmConfig(self, short_name: str) -> NmConfig:
        if (short_name not in self.elements):
            element = NmConfig(self, short_name)
            self.addElement(element)
        return self.getElement(short_name)

    def createCanTpConfig(self, short_name: str) -> CanTpConfig:
        if (short_name not in self.elements):
            element = CanTpConfig(self, short_name)
            self.addElement(element)
        return self.getElement(short_name)

    def createCanFrame(self, short_name: str) -> CanFrame:
        if (short_name not in self.elements):
            element = CanFrame(self, short_name)
            self.addElement(element)
        return self.getElement(short_name)

    def createEcuInstance(self, short_name: str) -> EcuInstance:
        if (short_name not in self.elements):
            element = EcuInstance(self, short_name)
            self.addElement(element)
        return self.getElement(short_name)

    def createGateway(self, short_name: str) -> Gateway:
        if (short_name not in self.elements):
            element = Gateway(self, short_name)
            self.addElement(element)
        return self.getElement(short_name)

    def createISignal(self, short_name: str) -> ISignal:
        if (short_name not in self.elements):
            element = ISignal(self, short_name)
            self.addElement(element)
        return self.getElement(short_name)

    def createSystemSignal(self, short_name: str) -> SystemSignal:
        if (short_name not in self.elements):
            element = SystemSignal(self, short_name)
            self.addElement(element)
        return self.getElement(short_name)

    def createSystemSignalGroup(self, short_name: str) -> SystemSignalGroup:
        if (short_name not in self.elements):
            element = SystemSignalGroup(self, short_name)
            self.addElement(element)
        return self.getElement(short_name)

    def createISignalIPdu(self, short_name: str) -> ISignalIPdu:
        if (short_name not in self.elements):
            element = ISignalIPdu(self, short_name)
            self.addElement(element)
        return self.getElement(short_name)

    def createEcucValueCollection(self, short_name: str) -> EcucValueCollection:
        if (short_name not in self.elements):
            element = EcucValueCollection(self, short_name)
            self.addElement(element)
        return self.getElement(short_name)

    def createEcucModuleConfigurationValues(self, short_name: str) -> EcucModuleConfigurationValues:
        if (short_name not in self.elements):
            element = EcucModuleConfigurationValues(self, short_name)
            self.addElement(element)
        return self.getElement(short_name)

    def createPhysicalDimension(self, short_name: str) -> PhysicalDimension:
        if (short_name not in self.elements):
            element = PhysicalDimension(self, short_name)
            self.addElement(element)
        return self.getElement(short_name)

    def createISignalGroup(self, short_name: str) -> ISignalGroup:
        if (short_name not in self.elements):
            element = ISignalGroup(self, short_name)
            self.addElement(element)
        return self.getElement(short_name)

    def createISignalIPduGroup(self, short_name: str) -> ISignalIPduGroup:
        if (short_name not in self.elements):
            element = ISignalIPduGroup(self, short_name)
            self.addElement(element)
        return self.getElement(short_name)

    def createSystem(self, short_name: str) -> System:
        if (short_name not in self.elements):
            element = System(self, short_name)
            self.addElement(element)
        return self.getElement(short_name)

    def getApplicationPrimitiveDataTypes(self) -> List[ApplicationPrimitiveDataType]:
        return list(sorted(filter(lambda a: isinstance(a, ApplicationPrimitiveDataType), self.elements.values()), key= lambda o:o.short_name))

    def getApplicationDataType(self) -> List[ApplicationDataType]:
        return list(sorted(filter(lambda a: isinstance(a, ApplicationDataType), self.elements.values()), key= lambda o:o.short_name))

    def getImplementationDataTypes(self) -> List[ImplementationDataType]:
        return list(sorted(filter(lambda a: isinstance(a, ImplementationDataType), self.elements.values()), key= lambda o:o.short_name))

    def getSwBaseTypes(self) -> List[SwBaseType]:
        return list(filter(lambda a: isinstance(a, SwBaseType), self.elements.values()))

    def getSwComponentTypes(self) -> List[SwComponentType]:
        return list(filter(lambda a : isinstance(a, SwComponentType), self.elements.values()))

    def getSensorActuatorSwComponentType(self) -> List[SensorActuatorSwComponentType]:
        return list(filter(lambda a : isinstance(a, SensorActuatorSwComponentType), self.elements.values()))

    def getAtomicSwComponentTypes(self) -> List[AtomicSwComponentType]:
        return list(filter(lambda a : isinstance(a, AtomicSwComponentType), self.elements.values()))

    def getCompositionSwComponentTypes(self) -> List[CompositionSwComponentType]:
        return list(filter(lambda a : isinstance(a, CompositionSwComponentType), self.elements.values()))

    def getComplexDeviceDriverSwComponentTypes(self) -> List[ComplexDeviceDriverSwComponentType]:
        return list(sorted(filter(lambda a : isinstance(a, ComplexDeviceDriverSwComponentType), self.elements.values()), key = lambda a: a.short_name))

    def getSenderReceiverInterfaces(self) -> List[SenderReceiverInterface]:
        return list(sorted(filter(lambda a : isinstance(a, SenderReceiverInterface), self.elements.values()), key = lambda a: a.short_name))

    def getParameterInterfaces(self) -> List[ParameterInterface]:
        return list(sorted(filter(lambda a : isinstance(a, ParameterInterface), self.elements.values()), key = lambda a: a.short_name))

    def getClientServerInterfaces(self) -> List[ClientServerInterface]:
        return list(sorted(filter(lambda a : isinstance(a, ClientServerInterface), self.elements.values()), key = lambda a: a.short_name))

    def getDataTypeMappingSets(self) -> List[DataTypeMappingSet]:
        return list(sorted(filter(lambda a : isinstance(a, DataTypeMappingSet), self.elements.values()), key = lambda a: a.short_name))

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
        return list(sorted(filter(lambda a : isinstance(a, ApplicationArrayDataType), self.elements.values()), key = lambda a: a.short_name))

    def getSwRecordLayouts(self) -> List[SwRecordLayout]:
        return list(sorted(filter(lambda a : isinstance(a, SwRecordLayout), self.elements.values()), key = lambda a: a.short_name))

    def getSwAddrMethods(self) -> List[SwAddrMethod]:
        return list(sorted(filter(lambda a : isinstance(a, SwAddrMethod), self.elements.values()), key = lambda a: a.short_name))

    def getTriggerInterfaces(self) -> List[TriggerInterface]:
        return list(sorted(filter(lambda a : isinstance(a, TriggerInterface), self.elements.values()), key = lambda a: a.short_name))

    def getModeDeclarationGroups(self) -> List[ModeDeclarationGroup]:
        return list(sorted(filter(lambda a : isinstance(a, ModeDeclarationGroup), self.elements.values()), key = lambda a: a.short_name))

    def getModeSwitchInterfaces(self) -> List[ModeSwitchInterface]:
        return list(sorted(filter(lambda a : isinstance(a, ModeSwitchInterface), self.elements.values()), key = lambda a: a.short_name))

    def getSwcTimings(self) -> List[SwcTiming]:
        return list(sorted(filter(lambda a : isinstance(a, SwcTiming), self.elements.values()), key = lambda a: a.short_name))

    def getLinClusters(self) -> List[LinCluster]:
        return list(sorted(filter(lambda a : isinstance(a, LinCluster), self.elements.values()), key = lambda a: a.short_name))

    def getCanClusters(self) -> List[CanCluster]:
        return list(sorted(filter(lambda a : isinstance(a, CanCluster), self.elements.values()), key = lambda a: a.short_name))

    def getLinUnconditionalFrames(self) -> List[LinUnconditionalFrame]:
        return list(sorted(filter(lambda a : isinstance(a, LinUnconditionalFrame), self.elements.values()), key = lambda a: a.short_name))

    def getNmPdus(self) -> List[NmPdu]:
        return list(sorted(filter(lambda a : isinstance(a, NmPdu), self.elements.values()), key = lambda a: a.short_name))

    def getNPdus(self) -> List[NPdu]:
        return list(sorted(filter(lambda a : isinstance(a, NPdu), self.elements.values()), key = lambda a: a.short_name))

    def getDcmIPdus(self) -> List[DcmIPdu]:
        return list(sorted(filter(lambda a : isinstance(a, DcmIPdu), self.elements.values()), key = lambda a: a.short_name))

    def getSecuredIPdus(self) -> List[SecuredIPdu]:
        return list(sorted(filter(lambda a : isinstance(a, SecuredIPdu), self.elements.values()), key = lambda a: a.short_name))

    def getNmConfigs(self) -> List[NmConfig]:
        return list(sorted(filter(lambda a : isinstance(a, NmConfig), self.elements.values()), key = lambda a: a.short_name))

    def getCanTpConfigs(self) -> List[CanTpConfig]:
        return list(sorted(filter(lambda a : isinstance(a, CanTpConfig), self.elements.values()), key = lambda a: a.short_name))

    def getCanFrames(self) -> List[CanFrame]:
        return list(sorted(filter(lambda a : isinstance(a, CanFrame), self.elements.values()), key = lambda a: a.short_name))

    def getEcuInstances(self) -> List[EcuInstance]:
        return list(sorted(filter(lambda a : isinstance(a, EcuInstance), self.elements.values()), key = lambda a: a.short_name))

    def getGateways(self) -> List[Gateway]:
        return list(sorted(filter(lambda a : isinstance(a, Gateway), self.elements.values()), key = lambda a: a.short_name))

    def getISignals(self) -> List[ISignal]:
        return list(sorted(filter(lambda a : isinstance(a, ISignal), self.elements.values()), key = lambda a: a.short_name))

    def getEcucValueCollections(self) -> List[EcucValueCollection]:
        return list(sorted(filter(lambda a : isinstance(a, EcucValueCollection), self.elements.values()), key = lambda a: a.short_name))

    def getEcucModuleConfigurationValues(self) -> List[EcucModuleConfigurationValues]:
        return list(sorted(filter(lambda a : isinstance(a, EcucModuleConfigurationValues), self.elements.values()), key = lambda a: a.short_name))

    def getEcucModuleConfigurationValues(self) -> List[PhysicalDimension]:
        return list(sorted(filter(lambda a : isinstance(a, PhysicalDimension), self.elements.values()), key = lambda a: a.short_name))

    def getISignalGroups(self) -> List[ISignalGroup]:
        return list(sorted(filter(lambda a : isinstance(a, ISignalGroup), self.elements.values()), key = lambda a: a.short_name))

    def getSystemSignals(self) -> List[SystemSignal]:
        return list(sorted(filter(lambda a : isinstance(a, SystemSignal), self.elements.values()), key = lambda a: a.short_name))

    def getSystemSignalGroups(self) -> List[SystemSignalGroup]:
        return list(sorted(filter(lambda a : isinstance(a, SystemSignalGroup), self.elements.values()), key = lambda a: a.short_name))

    def getISignalIPdus(self) -> List[ISignalIPdu]:
        return list(sorted(filter(lambda a : isinstance(a, ISignalIPdu), self.elements.values()), key = lambda a: a.short_name))

    def getSystems(self) -> List[System]:
        return list(sorted(filter(lambda a : isinstance(a, System), self.elements.values()), key = lambda a: a.short_name))
