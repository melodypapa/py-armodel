from typing import List
import xml.etree.ElementTree as ET
import os

from ..models.M2.AUTOSARTemplates.generic_structure.ar_package import ARPackage

from ..models.ar_ref import RefType
from ..models.M2.AUTOSARTemplates.common_structure.implementation import ImplementationProps
from ..models.M2.AUTOSARTemplates.common_structure import ApplicationValueSpecification, ArrayValueSpecification, ConstantReference, NumericalValueSpecification, RecordValueSpecification, TextValueSpecification, ValueSpecification
from ..models.M2.AUTOSARTemplates.generic_structure.abstract_structure import AnyInstanceRef
from ..models.M2.AUTOSARTemplates.common_structure.implementation_data_types import ImplementationDataTypeElement
from ..models.M2.AUTOSARTemplates.sw_component_template.composition.instance_refs import POperationInAtomicSwcInstanceRef, PPortInCompositionInstanceRef, ROperationInAtomicSwcInstanceRef, RPortInCompositionInstanceRef
from ..models.M2.AUTOSARTemplates.sw_component_template.port_interface.instance_refs import ApplicationCompositeElementInPortInterfaceInstanceRef
from ..models.M2.AUTOSARTemplates.sw_component_template.swc_internal_behavior.instance_refs_usage import AutosarParameterRef, AutosarVariableRef, VariableInAtomicSWCTypeInstanceRef
from ..models.M2.AUTOSARTemplates.system_template.instance_refs import VariableDataPrototypeInSystemInstanceRef
from ..models.M2.AUTOSARTemplates.sw_component_template.components.instance_refs import InnerPortGroupInCompositionInstanceRef, PModeGroupInAtomicSwcInstanceRef, RModeGroupInAtomicSWCInstanceRef
from ..models.M2.AUTOSARTemplates.sw_component_template.swc_internal_behavior import RunnableEntityArgument
from ..models.M2.AUTOSARTemplates.sw_component_template.components import PortGroup, SwComponentType, SymbolProps, PPortPrototype, RPortPrototype
from ..models.M2.AUTOSARTemplates.sw_component_template.composition import AssemblySwConnector, CompositionSwComponentType, DelegationSwConnector

from ..models.M2.AUTOSARTemplates.sw_component_template.swc_internal_behavior.mode_declaration_group import ModeAccessPoint
from ..models.M2.AUTOSARTemplates.sw_component_template.swc_internal_behavior.server_call import ServerCallPoint
from ..models.M2.AUTOSARTemplates.sw_component_template.communication import ClientComSpec, ModeSwitchSenderComSpec, NonqueuedReceiverComSpec, NonqueuedSenderComSpec, ParameterRequireComSpec, QueuedSenderComSpec, ReceiverComSpec, SenderComSpec, ServerComSpec
from ..models.fibex.lin_communication import LinFrameTriggering
from ..models.fibex.fibex_core.core_topology import AbstractCanCluster, CanPhysicalChannel, CommunicationCluster, LinPhysicalChannel, PhysicalChannel
from ..models.M2.MSR.data_dictionary.data_def_properties import SwDataDefProps
from ..models.M2.MSR.documentation.block_elements import DocumentationBlock
from ..models.M2.AUTOSARTemplates.system_template import System, SystemMapping
from ..models.M2.AUTOSARTemplates.system_template.data_mapping import SenderReceiverToSignalGroupMapping, SenderReceiverToSignalMapping
from ..models.M2.AUTOSARTemplates.system_template.network_management import CanNmCluster, CanNmClusterCoupling, CanNmNode, NmCluster, NmConfig, NmNode
from ..models.fibex.can_communication import CanFrameTriggering, RxIdentifierRange
from ..models.M2.AUTOSARTemplates.ecuc_description_template import EcucAbstractReferenceValue, EcucContainerValue, EcucInstanceReferenceValue, EcucModuleConfigurationValues, EcucNumericalParamValue, EcucParameterValue, EcucReferenceValue, EcucTextualParamValue, EcucValueCollection
from ..models.fibex.fibex_4_multiplatform import ISignalMapping
from ..models.fibex.fibex_core.core_communication import Frame, FrameTriggering, IPdu, ISignalIPdu, ISignalTriggering, PduTriggering
from ..models.internal_behavior import IncludedDataTypeSet
from ..models.timing import ExecutionOrderConstraint, TimingExtension
from ..models.bsw_module_template import BswModeSenderPolicy
from ..models.M2.AUTOSARTemplates.sw_component_template.port_interface import InvalidationPolicy, ModeSwitchInterface, ParameterInterface, PortInterface
from ..models.common_structure import IncludedModeDeclarationGroupSet, MemorySection, ModeDeclarationGroup, ModeDeclarationGroupPrototype, ModeRequestTypeMap
from ..models.implementation import BswImplementation, EngineeringObject
from ..models.general_structure import MultilanguageReferrable
from ..models.multilanguage_data import LOverviewParagraph, MultiLanguageOverviewParagraph, LLongName, MultiLanguageParagraph, MultilanguageLongName
from ..models.data_def_properties import ValueList
from ..models.record_layout import SwRecordLayoutGroup, SwRecordLayoutGroupContent, SwRecordLayoutV
from ..models.datatype import ApplicationArrayDataType, ApplicationCompositeDataType, ApplicationDataType, AutosarDataType, BaseTypeDirectDefinition
from ..models.calibration import SwAxisGrouped, SwAxisIndividual, SwCalprmAxis, SwCalprmAxisSet
from ..models.communication import CompositeNetworkRepresentation
from ..models.end_to_end_protection import EndToEndDescription, EndToEndProtection, EndToEndProtectionSet, EndToEndProtectionVariablePrototype
from ..models.service_mapping import RoleBasedPortAssignment
from ..models.M2.AUTOSARTemplates.autosar_top_level_structure import AUTOSAR
from ..models.ar_object import ARLiteral
from ..models.service_needs import RoleBasedDataAssignment
from ..models.sw_component import AtomicSwComponentType, PortAPIOption, PortDefinedArgumentValue, ServiceDependency,  SwcServiceDependency
from ..models.M2.AUTOSARTemplates.sw_component_template.data_type.data_prototypes import ApplicationCompositeElementDataPrototype, AutosarDataPrototype, DataPrototype, ParameterDataPrototype, VariableDataPrototype
from ..models.port_prototype import ModeSwitchReceiverComSpec, QueuedReceiverComSpec
from ..models.annotation import Annotation, GeneralAnnotation
from ..models.global_constraints import InternalConstrs, DataConstr, DataConstrRule, PhysConstrs

from ..models import SwcInternalBehavior, RunnableEntity, RTEEvent, OperationInvokedEvent, DataReceivedEvent, RVariableInAtomicSwcInstanceRef
from ..models import SwcModeSwitchEvent, RModeInAtomicSwcInstanceRef

from ..models import ImplementationDataType,  SwPointerTargetProps, DataTypeMappingSet, DataTypeMap
from ..models import SenderReceiverInterface, ClientServerInterface, ClientServerOperation, ArgumentDataPrototype
from ..models import Identifiable, AdminData, Sdg, Sd
from ..models import CompuMethod, CompuScale, CompuScales, Compu, CompuConst, CompuConstTextContent, CompuScaleConstantContents, CompuScaleRationalFormula, CompuRationalCoeffs, CompuNominatorDenominator
from ..models import InternalBehavior, ExecutableEntity
from ..models import Implementation, Code, AutosarEngineeringObject, ResourceConsumption
from ..models import TransmissionAcknowledgementRequest
from ..models import BswModuleDescription, BswInternalBehavior, BswModuleEntity, BswScheduleEvent, SwcBswMapping, SwcBswRunnableMapping
from ..models import ApplicationRecordDataType
from ..models import SwValueCont, SwValues

from .abstract_arxml_parser import AbstractARXMLParser

class ARXMLParser(AbstractARXMLParser):
    def __init__(self, options=None) -> None:
        super().__init__(options)

    def getChildElementRxIdentifierRange(self, element: ET.Element, key: str) -> RxIdentifierRange:
        child_element = self.find(element, key)
        range = None
        if child_element is not None:
            range = RxIdentifierRange()
            range.setLowerCanId(self.getChildElementOptionalNumericalValue(child_element, "LOWER-CAN-ID")) \
                 .setUpperCanId(self.getChildElementOptionalNumericalValue(child_element, "UPPER-CAN-ID"))
        return range
        
    def readSd(self, element: ET.Element, sdg: Sdg):
        for child_element in self.findall(element, "./SD"):
            sd = Sd()
            if 'GID' in child_element.attrib:
                sd.setGID(child_element.attrib['GID'])
            sd.setValue(child_element.text)
            sdg.addSd(sd)

    def getSdg(self, element: ET.Element) -> Sdg:
        sdg = Sdg()
        if 'GID' in element.attrib:
            sdg.setGID(element.attrib["GID"])
        self.readSd(element, sdg)
        for child_element in self.findall(element, "SDG"):
            sdg.addSdgContentsType(self.getSdg(child_element))
        return sdg
    
    def readSdgs(self, element: ET.Element, admin_data: AdminData):
        for child_element in self.findall(element, "./SDGS/SDG"):
            admin_data.addSdg(self.getSdg(child_element))
    
    def readAdminData(self, element: ET.Element, identifiable: Identifiable):
        child_element = self.find(element, "./ADMIN-DATA")
        if child_element is not None:
            self.logger.debug("readAdminData")
            admin_data = AdminData()
            self.readSdgs(child_element, admin_data)
            identifiable.setAdminData(admin_data)

    def readMultilanguageReferrable(self, element: ET.Element, referrable: MultilanguageReferrable):
        self.readElementAttributes(element, referrable)
        referrable.setLongName(self.getMultilanguageLongName(element, "LONG-NAME"))
    
    def readIdentifiable(self, element: ET.Element, identifiable: Identifiable):
        self.readMultilanguageReferrable(element, identifiable)

        for annotation in self.getAnnotations(element):
            identifiable.addAnnotation(annotation)

        identifiable.setCategory(self.getChildElementOptionalLiteral(element, "CATEGORY")) \
                    .setDesc(self.getMultiLanguageOverviewParagraph(element, "DESC"))
        
        self.readAdminData(element, identifiable)
    
    def readLLongName(self, element: ET.Element, long_name: MultilanguageLongName):
        for child_element in self.findall(element, "./L-4"):
            l4 = LLongName()
            self.readElementAttributes(child_element, l4)
            l4.value = child_element.text
            if 'L' in child_element.attrib:
                l4.l = child_element.attrib['L']
            long_name.addL4(l4)
    
    def getMultilanguageLongName(self, element: ET.Element, key: str) -> MultilanguageLongName:
        long_name = None
        child_element = self.find(element, "./%s" % key)
        if child_element is not None:
            long_name = MultilanguageLongName()
            self.readElementAttributes(child_element, long_name)
            self.readLLongName(child_element, long_name)
        return long_name
    
    def readLOverviewParagraph(self, element: ET.Element, paragraph: MultiLanguageOverviewParagraph):
        for child_element in self.findall(element, "./L-2"):
            l2 = LOverviewParagraph()
            self.readElementAttributes(child_element, l2)
            l2.value = child_element.text
            if 'L' in child_element.attrib:
                l2.l = child_element.attrib['L']
            paragraph.addL2(l2)
    
    def getMultiLanguageOverviewParagraph(self, element: ET.Element, key: str) -> MultiLanguageOverviewParagraph:
        paragraph = None
        child_element = element.find("./xmlns:%s" % key, self.nsmap)
        if child_element is not None:
            paragraph = MultiLanguageOverviewParagraph()
            self.readElementAttributes(child_element, paragraph)
            self.readLOverviewParagraph(child_element, paragraph)
        return paragraph
    
    def getVariableInAtomicSWCTypeInstanceRef(self, element: ET.Element) -> VariableInAtomicSWCTypeInstanceRef:
        autosar_variable_iref  = None
        if element is not None:
            autosar_variable_iref = VariableInAtomicSWCTypeInstanceRef()
            self.readElementAttributes(element, autosar_variable_iref)
            autosar_variable_iref.setPortPrototypeRef(self.getChildElementOptionalRefType(element, "PORT-PROTOTYPE-REF"))
            autosar_variable_iref.setTargetDataPrototypeRef(self.getChildElementOptionalRefType(element, "TARGET-DATA-PROTOTYPE-REF"))
        return autosar_variable_iref

    def getAutosarVariableInImplDatatype(self, element: ET.Element) ->  AutosarVariableRef:
        child_element = self.find(element, "ACCESSED-VARIABLE")
        accessed_variable_ref  = None
        if (child_element is not None):
            accessed_variable_ref = AutosarVariableRef()
            accessed_variable_ref.setAutosarVariableIRef(self.getVariableInAtomicSWCTypeInstanceRef(self.find(child_element, "AUTOSAR-VARIABLE-IREF")))
        return accessed_variable_ref

    def getLocalVariableRef(self, element: ET.Element) ->  AutosarVariableRef:
        child_element = self.find(element, "ACCESSED-VARIABLE")
        accessed_variable_ref  = None
        if (child_element is not None):
            accessed_variable_ref = AutosarVariableRef()
            accessed_variable_ref.setLocalVariableRef(self.getChildElementOptionalRefType(child_element, "LOCAL-VARIABLE-REF"))
        return accessed_variable_ref

    def _readVariableAccesses(self, element: ET.Element, parent: RunnableEntity, key: str):
        for child_element in element.findall("./xmlns:%s/xmlns:VARIABLE-ACCESS" % key, self.nsmap):
            short_name = self.getShortName(child_element)

            self.logger.debug("readVariableAccesses %s" % short_name)

            if (key == "DATA-RECEIVE-POINT-BY-ARGUMENTS"):
                variable_access = parent.createDataReceivePointByArgument(short_name)
                variable_access.setAccessedVariableRef(self.getAutosarVariableInImplDatatype(child_element))
            elif (key == "DATA-RECEIVE-POINT-BY-VALUES"):
                variable_access = parent.createDataReceivePointByValue(short_name)
                variable_access.setAccessedVariableRef(self.getAutosarVariableInImplDatatype(child_element))
            elif (key == "DATA-READ-ACCESSS"):
                variable_access = parent.createDataReadAccess(short_name)
                variable_access.setAccessedVariableRef(self.getAutosarVariableInImplDatatype(child_element))
            elif (key == "DATA-WRITE-ACCESSS"):
                variable_access = parent.createDataWriteAccess(short_name)
                variable_access.setAccessedVariableRef(self.getAutosarVariableInImplDatatype(child_element))
            elif (key == "DATA-SEND-POINTS"):
                variable_access = parent.createDataSendPoint(short_name)
                variable_access.setAccessedVariableRef(self.getAutosarVariableInImplDatatype(child_element))
            elif (key == "WRITTEN-LOCAL-VARIABLES"):
                variable_access = parent.createWrittenLocalVariable(short_name)
                variable_access.setAccessedVariableRef(self.getLocalVariableRef(child_element))
            elif (key == "READ-LOCAL-VARIABLES"):
                variable_access = parent.createReadLocalVariable(short_name)
                variable_access.setAccessedVariableRef(self.getLocalVariableRef(child_element))
            else:
                self._raiseError("Invalid key type <%s>" % key)

            self.readIdentifiable(child_element, variable_access)

    def readBswModuleDescriptionImplementedEntry(self, element: ET.Element, parent: BswModuleDescription):
        for child_element in element.findall("./xmlns:PROVIDED-ENTRYS/xmlns:BSW-MODULE-ENTRY-REF-CONDITIONAL", self.nsmap):
            ref = self.getChildElementOptionalRefType(child_element, "BSW-MODULE-ENTRY-REF") 
            if (ref is not None):
                parent.addImplementedEntry(ref)
            self.logger.debug("ImplementedEntry <%s> of BswModuleDescription <%s> has been added", ref.value, parent.getShortName())

    def readModeDeclarationGroupPrototype(self, element: ET.Element, prototype: ModeDeclarationGroupPrototype):
        self.readIdentifiable(element, prototype)
        prototype.type_tref = self.getChildElementOptionalRefType(element, "TYPE-TREF")

    def readProvidedModeGroup(self, element: ET.Element, parent: BswModuleDescription):
        for child_element in element.findall("./xmlns:PROVIDED-MODE-GROUPS/xmlns:MODE-DECLARATION-GROUP-PROTOTYPE", self.nsmap):
            short_name = self.getShortName(child_element)
            self.logger.debug("readProvidedModeGroup %s" % short_name)

            mode_group = parent.createProvidedModeGroup(short_name)
            self.readModeDeclarationGroupPrototype(child_element, mode_group)

    def readRequiredModeGroup(self, element: ET.Element, parent: BswModuleDescription):
        for child_element in element.findall("./xmlns:REQUIRED-MODE-GROUPS/xmlns:MODE-DECLARATION-GROUP-PROTOTYPE", self.nsmap):
            short_name = self.getShortName(child_element)
            self.logger.debug("readRequiredModeGroup %s" % short_name)
            mode_group = parent.createProvidedModeGroup(short_name)
            mode_group.type_tref = self.getChildElementRefType(parent.getShortName(), child_element, "TYPE-TREF")

    def readCanEnterExclusiveAreaRefs(self, element: ET.Element, entity: ExecutableEntity):
        for ref in self.getChildElementRefTypeList(element, "CAN-ENTER-EXCLUSIVE-AREA-REFS/CAN-ENTER-EXCLUSIVE-AREA-REF"):
            entity.addCanEnterExclusiveAreaRef(ref)

    def readExecutableEntity(self, element: ET.Element, entity: ExecutableEntity):
        self.logger.debug("readExecutableEntity %s" % entity.getShortName())
        self.readIdentifiable(element, entity)
        self.readCanEnterExclusiveAreaRefs(element, entity)
        entity.setMinimumStartInterval(self.getChildElementOptionalFloatValue(element, "MINIMUM-START-INTERVAL")) \
              .setSwAddrMethodRef(self.getChildElementOptionalRefType(element, "SW-ADDR-METHOD-REF"))

    def readBswModuleEntityManagedModeGroup(self, element: ET.Element, entity: BswModuleEntity):
        for child_element in self.findall(element, "./MANAGED-MODE-GROUPS/MODE-DECLARATION-GROUP-PROTOTYPE-REF-CONDITIONAL"):
            ref_type = self.getChildElementOptionalRefType(child_element, "MODE-DECLARATION-GROUP-PROTOTYPE-REF")
            if ref_type is not None:
                entity.addManagedModeGroupRef(ref_type)

    def readBswModuleEntity(self, element: ET.Element, entity: BswModuleEntity):
        self.readExecutableEntity(element, entity)
        entity.setImplementedEntryRef(self.getChildElementRefType(entity.getShortName(), element, "IMPLEMENTED-ENTRY-REF"))
        self.readBswModuleEntityManagedModeGroup(element, entity)

    def readBswCalledEntity(self, element: ET.Element, parent: BswInternalBehavior):
        for child_element in element.findall("./xmlns:ENTITYS/xmlns:BSW-CALLED-ENTITY", self.nsmap):
            short_name = self.getShortName(child_element)
            self.logger.debug("readBswCalledEntity %s" % short_name)
            entity = parent.createBswCalledEntity(short_name)

            self.readBswModuleEntity(child_element, entity)

    def readBswSchedulableEntity(self, element: ET.Element, parent: BswInternalBehavior):
        for child_element in element.findall("./xmlns:ENTITYS/xmlns:BSW-SCHEDULABLE-ENTITY", self.nsmap):
            short_name = self.getShortName(child_element)
            self.logger.debug("readBswSchedulableEntity %s" % short_name)
            entity = parent.createBswSchedulableEntity(short_name)
            self.readBswModuleEntity(child_element, entity)

    def readBswEvent(self, element: ET.Element, event: BswScheduleEvent):
        event.startsOnEventRef = self.getChildElementRefType(event.getShortName(), element, "STARTS-ON-EVENT-REF")

    def readBswScheduleEvent(self, element, event: BswScheduleEvent):
        self.readBswEvent(element, event)

    def readBswModeSwitchEvent(self, element: ET.Element, parent: BswInternalBehavior):
        for child_element in element.findall("./xmlns:EVENTS/xmlns:BSW-MODE-SWITCH-EVENT", self.nsmap):
            short_name = self.getShortName(child_element)
            self.logger.debug("readBswModeSwitchEvent %s" % short_name)
            event = parent.createBswModeSwitchEvent(short_name)
            # Read the Inherit BswScheduleEvent
            self.readBswScheduleEvent(child_element, event)

    def readBswTimingEvent(self, element: ET.Element, parent: BswInternalBehavior):
        for child_element in element.findall("./xmlns:EVENTS/xmlns:BSW-TIMING-EVENT", self.nsmap):
            short_name = self.getShortName(child_element)
            self.logger.debug("readBswTimingEvent %s" % short_name)
            event = parent.createBswTimingEvent(short_name)
            event.period = self.getChildElementOptionalFloatValue(child_element, "PERIOD")
            # Read the Inherit BswScheduleEvent
            self.readBswScheduleEvent(child_element, event)

    def readBswDataReceivedEvent(self, element: ET.Element, parent: BswInternalBehavior):
        for child_element in element.findall("./xmlns:EVENTS/xmlns:BSW-DATA-RECEIVED-EVENT", self.nsmap):
            short_name = self.getShortName(child_element)
            self.logger.debug("readBswDataReceivedEvent %s" % short_name)
            event = parent.createBswDataReceivedEvent(short_name)
            event.data_ref = self.getChildElementRefType(parent.getShortName(), child_element, "DATA-REF")
            # Read the Inherit BswScheduleEvent
            self.readBswScheduleEvent(child_element, event)

    def readBswInternalTriggerOccurredEvent(self, element: ET.Element, parent: BswInternalBehavior):
        for child_element in self.findall(element, "./EVENTS/BSW-INTERNAL-TRIGGER-OCCURRED-EVENT"):
            short_name = self.getShortName(child_element)
            self.logger.debug("readBswInternalTriggerOccurredEvent %s" % short_name)
            event = parent.createBswInternalTriggerOccurredEvent(short_name)
            event.event_source_ref = self.getChildElementRefType(parent.getShortName(), child_element, "EVENT-SOURCE-REF")
            # Read the Inherit BswScheduleEvent
            self.readBswScheduleEvent(child_element, event)

    def getBswModeSenderPolicy(self, element: ET.Element) -> BswModeSenderPolicy:
        policy = BswModeSenderPolicy()
        policy.setProvidedModeGroupRef(self.getChildElementOptionalRefType(element, "PROVIDED-MODE-GROUP-REF"))
        policy.setQueueLength(self.getChildElementOptionalNumericalValue(element, "QUEUE-LENGTH"))
        return policy

    def readBswInternalBehaviorModeSenderPolicy(self, element: ET.Element, parent: BswInternalBehavior):
        for child_element in self.findall(element, "./MODE-SENDER-POLICYS/*"):
            tag_name = self.getTagName(child_element)
            if tag_name == "BSW-MODE-SENDER-POLICY":
                parent.addModeSenderPolicy(self.getBswModeSenderPolicy(child_element))
            else:
                self._raiseError("Unsupported ModeSenderPolicy type <%s>." % tag_name)

    def readDataTypeMappingRefs(self, element: ET.Element, behavior: InternalBehavior):
        child_element = element.find("./xmlns:DATA-TYPE-MAPPING-REFS", self.nsmap)
        if child_element is not None:
            for ref in self.getChildElementRefTypeList(child_element, "./DATA-TYPE-MAPPING-REF"):
                behavior.addDataTypeMappingRef(ref)

    def readInternalBehaviorConstantMemories(self, element: ET.Element, behavior: InternalBehavior):
        for child_element in element.findall("./xmlns:CONSTANT-MEMORYS/xmlns:PARAMETER-DATA-PROTOTYPE", self.nsmap):
            short_name = self.getShortName(child_element)
            prototype = behavior.createConstantMemory(short_name)
            self.readParameterDataPrototype(child_element, prototype)

    def readInternalBehavior(self, element: ET.Element, behavior: InternalBehavior):
        self.readIdentifiable(element, behavior)
        self.readInternalBehaviorConstantMemories(element, behavior)
        for child_element in element.findall("./xmlns:EXCLUSIVE-AREAS/xmlns:EXCLUSIVE-AREA", self.nsmap):
            short_name = self.getShortName(child_element)
            behavior.createExclusiveArea(short_name)
        self.readDataTypeMappingRefs(element, behavior)

    def getRoleBasedDataAssignment(self, element: ET.Element) -> RoleBasedDataAssignment:
        assignment = RoleBasedDataAssignment()
        assignment.role = self.getChildElementOptionalLiteral(element, "ROLE")
        assignment.used_parameter_element = self.getAutosarParameterRef(element, "USED-PARAMETER-ELEMENT")
        assignment.used_pim_ref = self.getChildElementOptionalRefType(element, "USED-PIM-REF")
        return assignment
    
    def getRoleBasedPortAssignment(self, element: ET.Element) -> RoleBasedPortAssignment:
        assignment = RoleBasedPortAssignment()
        assignment.port_prototype_ref = self.getChildElementOptionalRefType(element, "PORT-PROTOTYPE-REF")
        assignment.role = self.getChildElementOptionalLiteral(element, "ROLE")
        return assignment

    def readServiceDependency(self, element: ET.Element, dependency: ServiceDependency):
        self.readIdentifiable(element, dependency)

    def readSwcServiceDependencyAssignedData(self, element: ET.Element, dependency: SwcServiceDependency):
        for child_element in element.findall("./xmlns:ASSIGNED-DATAS/*", self.nsmap):
            tag_name = self.getTagName(child_element.tag)
            if (tag_name == "ROLE-BASED-DATA-ASSIGNMENT"):
                dependency.AddAssignedData(self.getRoleBasedDataAssignment(child_element))
            else:
                self._raiseError("Unsupported assigned data <%s>" % tag_name)

    def readSwcServiceDependencyAssignedPorts(self, element: ET.Element, dependency: SwcServiceDependency):
        for child_element in element.findall("./xmlns:ASSIGNED-PORTS/*", self.nsmap):
            tag_name = self.getTagName(child_element.tag)
            if (tag_name == "ROLE-BASED-PORT-ASSIGNMENT"):
                dependency.AddAssignedPort(self.getRoleBasedPortAssignment(child_element))
            else:
                self._raiseError("Unsupported assigned ports <%s>" % tag_name)

    def readNvBlockNeeds(self, element: ET.Element, parent: SwcServiceDependency):
        short_name = self.getShortName(element)
        needs = parent.createNvBlockNeeds(short_name)
        self.logger.debug("readNvBlockNeeds %s" % short_name)
        needs.calc_ram_block_crc = self.getChildElementOptionalBooleanValue(element, "CALC-RAM-BLOCK-CRC")
        needs.check_static_block_id = self.getChildElementOptionalBooleanValue(element, "CHECK-STATIC-BLOCK-ID")
        needs.n_data_sets = self.getChildElementOptionalNumericalValue(element, "N-DATA-SETS")
        needs.n_rom_blocks = self.getChildElementOptionalNumericalValue(element, "N-ROM-BLOCKS")
        needs.readonly = self.getChildElementOptionalBooleanValue(element, "READONLY")
        needs.reliability = self.getChildElementOptionalLiteral(element, "RELIABILITY")
        needs.resistant_to_changed_sw = self.getChildElementOptionalBooleanValue(element, "RESISTANT-TO-CHANGED-SW")
        needs.restore_at_start = self.getChildElementOptionalBooleanValue(element, "RESTORE-AT-START")
        needs.store_at_shutdown = self.getChildElementOptionalBooleanValue(element, "STORE-AT-SHUTDOWN")
        needs.write_only_once = self.getChildElementOptionalBooleanValue(element, "WRITE-ONLY-ONCE")
        needs.write_verification = self.getChildElementOptionalBooleanValue(element, "WRITE-VERIFICATION")
        needs.writing_priority = self.getChildElementOptionalLiteral(element, "WRITING-PRIORITY")                          

    def readSwcServiceDependencyServiceNeeds(self, element: ET.Element, parent: SwcServiceDependency):
        for child_element in element.findall("./xmlns:SERVICE-NEEDS/*", self.nsmap):
            tag_name = self.getTagName(child_element.tag)
            if tag_name == "NV-BLOCK-NEEDS":
                self.readNvBlockNeeds(child_element, parent)    
            else:
                self._raiseError("Unsupported service needs <%s>" % tag_name)

    def readSwcServiceDependency(self, element: ET.Element, parent: SwcInternalBehavior):
        short_name = self.getShortName(element)
        dependency = parent.createSwcServiceDependency(short_name)
        self.logger.debug("readSwcServiceDependency %s" % short_name)
        self.readServiceDependency(element, dependency)
        self.readSwcServiceDependencyAssignedData(element, dependency)
        self.readSwcServiceDependencyAssignedPorts(element, dependency)
        self.readSwcServiceDependencyServiceNeeds(element, dependency)

    def readSwcInternalBehaviorServiceDependencies(self, element: ET.Element, parent: SwcInternalBehavior):
        for child_element in element.findall("./xmlns:SERVICE-DEPENDENCYS/*", self.nsmap):
            tag_name = self.getTagName(child_element.tag)
            if (tag_name == "SWC-SERVICE-DEPENDENCY"):
                self.readSwcServiceDependency(child_element, parent)
            else:
                self._raiseError("Unsupported Service Dependencies <%s>" % tag_name)

    def getIncludedDataTypeSets(self, element: ET.Element) -> List[IncludedDataTypeSet]:
        include_data_type_sets = []
        for child_element in self.findall(element, "./INCLUDED-DATA-TYPE-SETS/INCLUDED-DATA-TYPE-SET"):
            include_data_type_set = IncludedDataTypeSet()
            self.readElementAttributes(child_element, include_data_type_set)
            for ref_type in self.getChildElementRefTypeList(child_element, "./DATA-TYPE-REFS/DATA-TYPE-REF"):
                include_data_type_set.addDataTypeRef(ref_type)
            include_data_type_sets.append(include_data_type_set)
        return include_data_type_sets

    def readSwcInternalBehavior(self, element: ET.Element, parent: AtomicSwComponentType):
        for child_element in self.findall(element, "./INTERNAL-BEHAVIORS/SWC-INTERNAL-BEHAVIOR"):
            short_name = self.getShortName(child_element)
            behavior = parent.createSwcInternalBehavior(short_name)
            self.logger.debug("readSwcInternalBehavior %s" % behavior.full_name)

            # read the internal behavior
            self.readInternalBehavior(child_element, behavior)
            
            # read the extra SwcInternalBehavior
            self.readSwcInternalBehaviorRunnables(child_element, behavior)
            self.readSwcInternalBehaviorEvents(child_element, behavior)
            self.readSwcInternalBehaviorServiceDependencies(child_element, behavior)
            self.readExplicitInterRunnableVariables(child_element, behavior)
            for data_type_set  in self.getIncludedDataTypeSets(child_element):
                behavior.addIncludedDataTypeSet(data_type_set)
            behavior.handle_termination_and_restart = self.getChildElementOptionalLiteral(child_element, "HANDLE-TERMINATION-AND-RESTART")
            self.readPerInstanceMemories(child_element, behavior)
            self.readPerInstanceParameters(child_element, behavior)
            self.readPortAPIOptions(child_element, behavior)
            behavior.supports_multiple_instantiation = self.getChildElementOptionalBooleanValue(child_element, "SUPPORTS-MULTIPLE-INSTANTIATION")

    def getIncludedModeDeclarationGroupSets(self, element: ET.Element) -> List[IncludedModeDeclarationGroupSet]:
        group_sets = []
        for child_element in self.findall(element, "INCLUDED-MODE-DECLARATION-GROUP-SETS/INCLUDED-MODE-DECLARATION-GROUP-SET"):
            group_set = IncludedModeDeclarationGroupSet()
            for ref_type in self.getChildElementRefTypeList(child_element, "./MODE-DECLARATION-GROUP-REFS/MODE-DECLARATION-GROUP-REF"):
                group_set.addModeDeclarationGroupRef(ref_type)
            group_sets.append(group_set)
        return group_sets

    def readBswInternalBehavior(self, element: ET.Element, parent: BswModuleDescription):
        for child_element in element.findall("./xmlns:INTERNAL-BEHAVIORS/xmlns:BSW-INTERNAL-BEHAVIOR", self.nsmap):
            short_name = self.getShortName(child_element)
            behavior = parent.createBswInternalBehavior(short_name)
            self.logger.debug("readBswInternalBehavior %s" % behavior.full_name)

            # read the internal behavior
            self.readInternalBehavior(child_element, behavior)
            self.readBswCalledEntity(child_element, behavior)
            self.readBswSchedulableEntity(child_element, behavior)
            self.readBswModeSwitchEvent(child_element, behavior)
            self.readBswTimingEvent(child_element, behavior)
            self.readBswDataReceivedEvent(child_element, behavior)
            self.readBswInternalTriggerOccurredEvent(child_element, behavior)
            self.readBswInternalBehaviorModeSenderPolicy(child_element, behavior)
            for group_set in self.getIncludedModeDeclarationGroupSets(child_element):
                behavior.addIncludedModeDeclarationGroupSet(group_set)

    def readBswModuleDescription(self, element: ET.Element, parent: ARPackage):
        short_name = self.getShortName(element)
        bsw_module_description = parent.createBswModuleDescription(short_name)
        bsw_module_description.module_id = self.getChildElementOptionalNumericalValue(element, "MODULE-ID")

        self.logger.debug("readBswModuleDescription %s" % bsw_module_description.full_name)

        self.readBswModuleDescriptionImplementedEntry(element, bsw_module_description)
        self.readProvidedModeGroup(element, bsw_module_description)
        self.readRequiredModeGroup(element, bsw_module_description)
        self.readBswInternalBehavior(element, bsw_module_description)

    def readBswModuleEntry(self, element: ET.Element, parent: ARPackage):
        short_name = self.getShortName(element)
        entry = parent.createBswModuleEntry(short_name)
        entry.is_reentrant = self.getChildElementOptionalBooleanValue(element, "IS-REENTRANT")
        entry.is_synchronous = self.getChildElementOptionalBooleanValue(element, "IS-SYNCHRONOUS")
        entry.service_id = self.getChildElementOptionalNumericalValue(element, "SERVICE-ID")
        entry.call_type = self.getChildElementOptionalLiteral(element, "CALL-TYPE")
        entry.execution_context = self.getChildElementOptionalLiteral(element, "EXECUTION-CONTEXT")
        entry.sw_service_impl_policy = self.getChildElementOptionalLiteral(element, "SW-SERVICE-IMPL-POLICY")

        #self.logger.debug("readBswModuleEntry \n%s" % entry)
        self.logger.debug("readBswModuleEntry %s" % entry.getShortName())

    def readEngineeringObject(self, element: ET.Element, engineering_obj: EngineeringObject):
        self.readElementAttributes(element, engineering_obj)
        engineering_obj.setShortLabel(self.getChildElementOptionalLiteral(element, "SHORT-LABEL")) \
                       .setCategory(self.getChildElementOptionalLiteral(element, "CATEGORY"))
        
    def getAutosarEngineeringObject(self, element: ET.Element) -> AutosarEngineeringObject:
        obj = AutosarEngineeringObject()
        self.readEngineeringObject(element, obj)
        self.logger.debug("getAutosarEngineeringObject %s", obj.short_label)
        return obj

    def readArtifactDescriptor(self, element: ET.Element, code_desc: Code):
        for child_element in element.findall("./xmlns:ARTIFACT-DESCRIPTORS/*", self.nsmap):
            tag_name = self.getTagName(child_element.tag)
            if tag_name == "AUTOSAR-ENGINEERING-OBJECT":
                code_desc.addArtifactDescriptor(self.getAutosarEngineeringObject(child_element))
            else:
                self._raiseError("Unsupported Artifact Descriptor <%s>" % tag_name)
            
    def readCodeDescriptor(self, element: ET.Element, impl: Implementation):
        for child_element in element.findall("./xmlns:CODE-DESCRIPTORS/xmlns:CODE", self.nsmap):
            short_name = self.getShortName(child_element)
            self.logger.debug("readCodeDescriptor %s" % short_name)
            code_desc = impl.createCodeDescriptor(short_name)
            self.readIdentifiable(child_element, code_desc)
            self.readArtifactDescriptor(child_element, code_desc)

    def readMemorySectionOptions(self, element: ET.Element, section: MemorySection):
        child_element = element.find("./xmlns:OPTIONS", self.nsmap)
        if child_element is not None:
            for value in self.getChildElementLiteralValueList(child_element, "OPTION"):
                section.addOption(value)

    def readMemorySections(self, element: ET.Element, consumption: ResourceConsumption):
        for child_element in element.findall("./xmlns:MEMORY-SECTIONS/xmlns:MEMORY-SECTION", self.nsmap):
            short_name = self.getShortName(child_element)
            memory_section = consumption.createMemorySection(short_name)
            self.readIdentifiable(child_element, memory_section)
            memory_section.setAlignment(self.getChildElementOptionalLiteral(child_element, "ALIGNMENT"))
            self.readMemorySectionOptions(child_element, memory_section)
            memory_section.size = self.getChildElementOptionalNumericalValue(child_element, "SIZE")
            memory_section.swAddrMethodRef = self.getChildElementOptionalRefType(child_element, "SW-ADDRMETHOD-REF")
            memory_section.symbol = self.getChildElementOptionalLiteral(child_element, "SYMBOL")
            self.logger.debug("readMemorySections %s" % memory_section.getShortName())

    def readResourceConsumption(self, element: ET.Element, impl: Implementation):
        child_element = element.find("./xmlns:RESOURCE-CONSUMPTION", self.nsmap)
        if (child_element is not None):
            short_name = self.getShortName(child_element)
            consumption = ResourceConsumption(impl, short_name)
            self.readIdentifiable(child_element, consumption)
            self.readMemorySections(child_element, consumption)
            impl.setResourceConsumption(consumption)

    def readImplementation(self, element: ET.Element, impl: Implementation):
        self.readIdentifiable(element, impl)
        self.readCodeDescriptor(element, impl)
        impl.programming_language = self.getChildElementOptionalLiteral(element, "PROGRAMMING-LANGUAGE")
        self.readResourceConsumption(element, impl)
        impl.sw_version = self.getChildElementOptionalLiteral(element, "SW-VERSION")
        impl.swc_bsw_mapping_ref = self.getChildElementOptionalRefType(element, "SWC-BSW-MAPPING-REF")
        impl.used_code_generator = self.getChildElementOptionalLiteral(element, "USED-CODE-GENERATOR")
        impl.vendor_id = self.getChildElementOptionalNumericalValue(element, "VENDOR-ID")

    def readBswImplementationVendorSpecificModuleDefRefs(self, element: ET.Element, parent: BswImplementation):
        child_element = element.find("./xmlns:VENDOR-SPECIFIC-MODULE-DEF-REFS", self.nsmap)
        if child_element is not None:
            for ref in self.getChildElementRefTypeList(child_element, "./VENDOR-SPECIFIC-MODULE-DEF-REF"):
                parent.addVendorSpecificModuleDefRef(ref)

    def readBswImplementation(self, element: ET.Element, parent: ARPackage):
        short_name = self.getShortName(element)
        impl = parent.createBswImplementation(short_name)   
        self.logger.debug("readBswImplementation %s" % impl.getShortName())
        self.readImplementation(element, impl)
        impl.ar_release_version = self.getChildElementOptionalLiteral(element, "AR-RELEASE-VERSION")
        impl.behavior_ref = self.getChildElementOptionalRefType(element, "BEHAVIOR-REF")
        self.readBswImplementationVendorSpecificModuleDefRefs(element, impl)

    def readSwcImplementation(self, element: ET.Element, parent: ARPackage):
        short_name = self.getShortName(element)
        impl = parent.createSwcImplementation(short_name)   
        self.logger.debug("readSwcImplementation %s" % impl.getShortName())
        self.readImplementation(element, impl)
        impl.behavior_ref = self.getChildElementOptionalRefType(element, "BEHAVIOR-REF")

    def readDataReceivePointByArguments(self, element, parent: RunnableEntity):
        self._readVariableAccesses(element, parent, "DATA-RECEIVE-POINT-BY-ARGUMENTS")

    def readDataReceivePointByValues(self, element: ET.Element, parent: RunnableEntity):
        self._readVariableAccesses(element, parent, "DATA-RECEIVE-POINT-BY-VALUES")

    def readDataReadAccesses(self, element: ET.Element, parent: RunnableEntity):
        self._readVariableAccesses(element, parent, "DATA-READ-ACCESSS")

    def readDataWriteAccesses(self, element: ET.Element, parent: RunnableEntity):
        self._readVariableAccesses(element, parent, "DATA-WRITE-ACCESSS")

    def readDataSendPoints(self, element: ET.Element, parent: RunnableEntity):
        self._readVariableAccesses(element, parent, "DATA-SEND-POINTS")

    def getRunnableEntityArgument(self, element: ET.Element) -> RunnableEntityArgument:
        argument = RunnableEntityArgument()
        argument.setSymbol(self.getChildElementOptionalLiteral(element, "SYMBOL"))
        return argument

    def getAutosarParameterRef(self, element: ET.Element, key: str) -> AutosarParameterRef:
        accessed_parameter = None
        child_element = element.find("./xmlns:%s" % key, self.nsmap)
        if child_element is not None:
            accessed_parameter = AutosarParameterRef()
            accessed_parameter.local_parameter_ref = self.getChildElementOptionalRefType(child_element, "LOCAL-PARAMETER-REF")
        return accessed_parameter

    def readParameterAccesses(self, element: ET.Element, parent: RunnableEntity):
        for child_element in element.findall("./xmlns:PARAMETER-ACCESSS/xmlns:PARAMETER-ACCESS", self.nsmap):
            short_name = self.getShortName(child_element)
            self.logger.debug("readParameterAccesses %s" % short_name)
            parameter_access = parent.createParameterAccess(short_name)
            parameter_access.accessed_parameter = self.getAutosarParameterRef(child_element, "ACCESSED-PARAMETER")

    def readWrittenLocalVariables(self, element: ET.Element, parent: RunnableEntity):
        self._readVariableAccesses(element, parent, "WRITTEN-LOCAL-VARIABLES")

    def readReadLocalVariables(self, element: ET.Element, parent: RunnableEntity):
        self._readVariableAccesses(element, parent, "READ-LOCAL-VARIABLES")

    def readROperationIRef(self, element: ET.Element, key: str, parent: ServerCallPoint):
        child_element = element.find("./xmlns:%s" % key, self.nsmap)
        if (child_element is not None):
            operation_iref = ROperationInAtomicSwcInstanceRef()
            operation_iref.context_r_port_ref = self.getChildElementOptionalRefType(child_element, "CONTEXT-R-PORT-REF")
            operation_iref.target_required_operation_ref = self.getChildElementOptionalRefType(child_element, "TARGET-REQUIRED-OPERATION-REF")
            parent.setOperationIRef(operation_iref)

    def readRVariableInAtomicSwcInstanceRef(self, element: ET.Element, parent: DataReceivedEvent):
        child_element = self.find(element, "DATA-IREF")
        if (child_element is not None):
            data_iref = RVariableInAtomicSwcInstanceRef()
            data_iref.setContextRPortRef(self.getChildElementOptionalRefType(child_element, "CONTEXT-R-PORT-REF")) \
                     .setTargetDataElementRef(self.getChildElementOptionalRefType(child_element, "TARGET-DATA-ELEMENT-REF"))
            parent.setDataIRef(data_iref)

    def readRModeInAtomicSwcInstanceRef(self, element: ET.Element, parent: SwcModeSwitchEvent):
        for child_element in element.findall("./xmlns:MODE-IREFS/xmlns:MODE-IREF", self.nsmap):
            mode_iref = RModeInAtomicSwcInstanceRef()
            mode_iref.setContextPortRef(self.getChildElementOptionalRefType(child_element, "CONTEXT-PORT-REF")) \
                     .setContextModeDeclarationGroupPrototypeRef(self.getChildElementOptionalRefType(child_element, "CONTEXT-MODE-DECLARATION-GROUP-PROTOTYPE-REF")) \
                     .setTargetModeDeclarationRef(self.getChildElementOptionalRefType(child_element, "TARGET-MODE-DECLARATION-REF"))
            parent.addModeIRef(mode_iref)

    def readSynchronousServerCallPoint(self, element: ET.Element, parent: RunnableEntity):
        short_name = self.getShortName(element)
        self.logger.debug("readSynchronousServerCallPoint %s" % short_name)
        server_call_point = parent.createSynchronousServerCallPoint(short_name)
        self.readIdentifiable(element, server_call_point)
        server_call_point.setTimeout(self.getChildElementOptionalFloatValue(element, "TIMEOUT"))
        self.readROperationIRef(element, "OPERATION-IREF", server_call_point)

    def readAsynchronousServerCallPoint(self, element: ET.Element, parent: RunnableEntity):
        short_name = self.getShortName(element)
        self.logger.debug("readAsynchronousServerCallPoint %s" % short_name)
        server_call_point = parent.createAsynchronousServerCallPoint(short_name)
        self.readIdentifiable(element, server_call_point)
        server_call_point.setTimeout(self.getChildElementOptionalFloatValue(element, "TIMEOUT"))
        self.readROperationIRef(element, "OPERATION-IREF", server_call_point)

    def readInternalBehaviorServerCallPoint(self, element: ET.Element, parent: RunnableEntity):
        for child_element in self.findall(element, "SERVER-CALL-POINTS/*"):
            tag_name = self.getTagName(child_element.tag)
            if tag_name == "SYNCHRONOUS-SERVER-CALL-POINT":
                self.readSynchronousServerCallPoint(child_element, parent)
            elif tag_name == "ASYNCHRONOUS-SERVER-CALL-POINT":
                self.readAsynchronousServerCallPoint(child_element, parent)
            else:
                self._raiseError("Unsupported server call point type <%s>" % tag_name)

    def readInternalTriggeringPoints(self, element: ET.Element, parent: RunnableEntity):
        for child_element in self.findall(element, "INTERNAL-TRIGGERING-POINTS/INTERNAL-TRIGGERING-POINT"):
            short_name = self.getShortName(child_element)
            point = parent.createInternalTriggeringPoint(short_name)
            point.sw_impl_policy = self.getChildElementOptionalLiteral(child_element, "SW-IMPL-POLICY")

    def getRModeInAtomicSwcInstanceRef(self, element: ET.Element) -> RModeInAtomicSwcInstanceRef:
        iref = RModeInAtomicSwcInstanceRef()
        iref.setBaseRef(self.getChildElementOptionalRefType(element, "BASE-REF")) \
            .setContextPortRef(self.getChildElementOptionalRefType(element, "CONTEXT-PORT-REF")) \
            .setContextModeDeclarationGroupPrototypeRef(self.getChildElementOptionalRefType(element, "CONTEXT-MODE-DECLARATION-GROUP-PROTOTYPE-REF")) \
            .setTargetModeDeclarationRef(self.getChildElementOptionalRefType(element, "TARGET-MODE-DECLARATION-REF"))
        return iref
    
    def getRModeGroupInAtomicSWCInstanceRef(self, element: ET.Element) -> RModeGroupInAtomicSWCInstanceRef:
        child_element = self.find(element, "MODE-GROUP-IREF/R-MODE-GROUP-IN-ATOMIC-SWC-INSTANCE-REF")
        iref = None
        if child_element is not None:
            iref = RModeGroupInAtomicSWCInstanceRef()
            iref.setContextRPortRef(self.getChildElementOptionalRefType(child_element, "CONTEXT-R-PORT-REF")) \
                .setTargetModeGroupRef(self.getChildElementOptionalRefType(child_element, "TARGET-MODE-GROUP-REF"))
        return iref
    
    def getPModeGroupInAtomicSWCInstanceRef(self, element: ET.Element) -> PModeGroupInAtomicSwcInstanceRef:
        child_element = self.find(element, "MODE-GROUP-IREF")
        iref = None
        if child_element is not None:
            iref = PModeGroupInAtomicSwcInstanceRef()
            iref.setContextPPortRef(self.getChildElementOptionalRefType(child_element, "CONTEXT-P-PORT-REF")) \
                .setTargetModeGroupRef(self.getChildElementOptionalRefType(child_element, "TARGET-MODE-GROUP-REF"))
        return iref

    def readModeAccessPoints(self, element: ET.Element, parent: RunnableEntity):
        for child_element in self.findall(element, "MODE-ACCESS-POINTS/MODE-ACCESS-POINT"):
            point = ModeAccessPoint()
            point.setModeGroupIRef(self.getRModeGroupInAtomicSWCInstanceRef(child_element))
            parent.addModeAccessPoint(point)

    def readModeSwitchPoints(self, element: ET.Element, parent: RunnableEntity):
        for child_element in self.findall(element, "MODE-SWITCH-POINTS/MODE-SWITCH-POINT"):
            point = parent.createModeSwitchPoint(self.getShortName(child_element))
            point.setModeGroupIRef(self.getPModeGroupInAtomicSWCInstanceRef(child_element))

    def readRunnableEntityArguments(self, element: ET.Element, entity: RunnableEntity):
        for child_element in self.findall(element, "ARGUMENTS/*"):
            tag_name = self.getTagName(child_element)
            if tag_name == "RUNNABLE-ENTITY-ARGUMENT":
                entity.addArgument(self.getRunnableEntityArgument(child_element))
            else:
                raise NotImplementedError("Unsupported Arguments of runnable entity <%s>" % tag_name)

    def readRunnableEntity(self, element: ET.Element, entity: RunnableEntity):
        self.readExecutableEntity(element, entity)
        self.readRunnableEntityArguments(element, entity)

        entity.setCanBeInvokedConcurrently(self.getChildElementOptionalBooleanValue(element, "CAN-BE-INVOKED-CONCURRENTLY"))
        entity.setSymbol(self.getChildElementOptionalLiteral(element, "SYMBOL"))

        self.readDataReceivePointByArguments(element, entity)
        self.readDataReceivePointByValues(element, entity)
        self.readDataReadAccesses(element, entity)
        self.readDataWriteAccesses(element, entity)
        self.readDataSendPoints(element, entity)
        self.readInternalBehaviorServerCallPoint(element, entity)
        self.readInternalTriggeringPoints(element, entity)
        self.readModeAccessPoints(element, entity)
        self.readModeSwitchPoints(element, entity)
        self.readParameterAccesses(element, entity)
        self.readReadLocalVariables(element, entity)
        self.readWrittenLocalVariables(element, entity)

    def readSwcInternalBehaviorRunnables(self, element: ET.Element, parent: SwcInternalBehavior):
        for child_element in self.findall(element, "RUNNABLES/RUNNABLE-ENTITY"):
            short_name = self.getShortName(child_element)
            entity = parent.createRunnableEntity(short_name)
            self.logger.debug("readRunnableEntities %s" % short_name)
            
            self.readRunnableEntity(child_element, entity)

    def getRModeInAtomicSwcInstanceRef(self, element: ET.Element) -> RModeInAtomicSwcInstanceRef:
        iref = RModeInAtomicSwcInstanceRef()
        iref.setBaseRef(self.getChildElementOptionalRefType(element, "BASE-REF")) \
            .setContextPortRef(self.getChildElementOptionalRefType(element, "CONTEXT-PORT-REF")) \
            .setContextModeDeclarationGroupPrototypeRef(self.getChildElementOptionalRefType(element, "CONTEXT-MODE-DECLARATION-GROUP-PROTOTYPE-REF")) \
            .setTargetModeDeclarationRef(self.getChildElementOptionalRefType(element, "TARGET-MODE-DECLARATION-REF"))
        return iref

    def readRTEEvent(self, element: ET.Element, event: RTEEvent):
        self.readIdentifiable(element, event)
        event.start_on_event_ref = self.getChildElementOptionalRefType(element, "START-ON-EVENT-REF")
        for child_element in element.findall("./xmlns:DISABLED-MODE-IREFS/xmlns:DISABLED-MODE-IREF", self.nsmap):
            iref = self.getRModeInAtomicSwcInstanceRef(child_element)
            event.addDisabledModeIRef(iref)

    def readOperationIRef(self, element: ET.Element, parent: OperationInvokedEvent):
        child_element = element.find("./xmlns:OPERATION-IREF", self.nsmap)
        if (child_element is not None):
            parent.operation_iref = POperationInAtomicSwcInstanceRef()
            parent.operation_iref.context_p_port_ref = self.getChildElementRefType(parent.getShortName(), child_element, "CONTEXT-P-PORT-REF")
            parent.operation_iref.target_provided_operation_ref = self.getChildElementRefType(parent.getShortName(), child_element, "TARGET-PROVIDED-OPERATION-REF")

    def readOperationInvokedEvent(self, element: ET.Element, parent: SwcInternalBehavior):
        short_name = self.getShortName(element)
        event = parent.createOperationInvokedEvent(short_name)
        self.readOperationIRef(element, event)
        self.readRTEEvent(element, event)

    def readVariableDataPrototype(self, element: ET.Element, prototype: VariableDataPrototype):
        self.readAutosarDataPrototype(element, prototype)
        prototype.setInitValue(self.getInitValue(element))
        
    def readExplicitInterRunnableVariables(self, element: ET.Element, parent: SwcInternalBehavior):
        for child_element in element.findall("./xmlns:EXPLICIT-INTER-RUNNABLE-VARIABLES/xmlns:VARIABLE-DATA-PROTOTYPE", self.nsmap):
            short_name = self.getShortName(child_element)
            prototype = parent.createExplicitInterRunnableVariable(short_name)
            self.readVariableDataPrototype(child_element, prototype)

    def readPerInstanceMemories(self, element: ET.Element, behavior: SwcInternalBehavior):
        for child_element in element.findall("./xmlns:PER-INSTANCE-MEMORYS/xmlns:PER-INSTANCE-MEMORY", self.nsmap):
            short_name = self.getShortName(child_element)
            memory = behavior.createPerInstanceMemory(short_name)
            self.readIdentifiable(child_element, memory)
            memory.setInitValue(self.getChildElementOptionalLiteral(child_element, "INIT-VALUE")) \
                  .setSwDataDefProps(self.getSwDataDefProps(child_element, "SW-DATA-DEF-PROPS")) \
                  .setType(self.getChildElementOptionalLiteral(child_element, "TYPE")) \
                  .setTypeDefinition(self.getChildElementOptionalLiteral(child_element, "TYPE-DEFINITION"))

    def readAutosarDataPrototype(self, element: ET.Element, prototype: AutosarDataPrototype):
        self.readDataPrototype(element, prototype)
        prototype.setTypeTRef(self.getChildElementOptionalRefType(element, "TYPE-TREF"))

    def readParameterDataPrototype(self, element: ET.Element, prototype: ParameterDataPrototype):
        self.readIdentifiable(element, prototype)
        self.readAutosarDataPrototype(element, prototype)
        prototype.setInitValue(self.getInitValue(element))
        
    def readPerInstanceParameters(self, element: ET.Element, behavior: SwcInternalBehavior):
        for child_element in element.findall("./xmlns:PER-INSTANCE-PARAMETERS/xmlns:PARAMETER-DATA-PROTOTYPE", self.nsmap):
            short_name = self.getShortName(child_element)
            prototype = behavior.createPerInstanceParameter(short_name)
            self.readParameterDataPrototype(child_element, prototype)

    def readPortDefinedArgumentValue(self, element: ET.Element) -> PortDefinedArgumentValue:
        argument_value = PortDefinedArgumentValue()
        child_element = element.find("./xmlns:VALUE/*", self.nsmap)
        if child_element is not None:
            argument_value.value = self.getValueSpecification(child_element)
        argument_value.value_type = self.getChildElementOptionalRefType(element, "VALUE-TYPE-TREF")
        return argument_value

    def readPortAPIOptions(self, element: ET.Element, behavior: SwcInternalBehavior):
        for child_element in element.findall("./xmlns:PORT-API-OPTIONS/xmlns:PORT-API-OPTION", self.nsmap):
            option = PortAPIOption()
            option.enable_take_address = self.getChildElementOptionalBooleanValue(child_element, "ENABLE-TAKE-ADDRESS")
            option.indirect_api = self.getChildElementOptionalBooleanValue(child_element, "INDIRECT-API")
            option.port_ref = self.getChildElementOptionalRefType(child_element, "PORT-REF")
            for argument_value_tag in child_element.findall("./xmlns:PORT-ARG-VALUES/xmlns:PORT-DEFINED-ARGUMENT-VALUE", self.nsmap):
                option.addPortArgValue(self.readPortDefinedArgumentValue(argument_value_tag))
            behavior.addPortAPIOption(option)
            
    def readTimingEvent(self, element: ET.Element, parent: SwcInternalBehavior):
        short_name = self.getShortName(element)
        event = parent.createTimingEvent(short_name)
        self.readRTEEvent(element, event)
        event.offset = self.getChildElementOptionalFloatValue(element, "OFFSET")
        event.period = self.getChildElementOptionalFloatValue(element, "PERIOD")

    def readDataReceivedEvent(self, element: ET.Element, parent: SwcInternalBehavior):
        short_name = self.getShortName(element)
        event = parent.createDataReceivedEvent(short_name)
        self.readRTEEvent(element, event)
        self.readRVariableInAtomicSwcInstanceRef(element, event)

    def readSwcModeSwitchEvent(self, element: ET.Element, parent: SwcInternalBehavior):
        short_name = self.getShortName(element)
        event = parent.createSwcModeSwitchEvent(short_name)
        self.readRTEEvent(element, event)
        event.activation = self.getChildElementOptionalLiteral(element, "ACTIVATION")
        self.readRModeInAtomicSwcInstanceRef(element, event)

    def readInternalTriggerOccurredEvent(self, element: ET.Element, parent: SwcInternalBehavior):
        short_name = self.getShortName(element)
        event = parent.createInternalTriggerOccurredEvent(short_name)
        self.readRTEEvent(element, event)
        event.event_source_ref = self.getChildElementRefType(parent.getShortName(), element, "EVENT-SOURCE-REF")

    def readInitEvent(self, element, parent: SwcInternalBehavior):
        short_name = self.getShortName(element)
        event = parent.createInitEvent(short_name)
        self.readRTEEvent(element, event)

    def readSwcInternalBehaviorEvents(self, element: ET.Element, parent: SwcInternalBehavior):
        for child_element in element.findall("./xmlns:EVENTS/*", self.nsmap):
            tag_name = self.getTagName(child_element.tag)
            if tag_name == "TIMING-EVENT":
                self.readTimingEvent(child_element, parent)
            elif tag_name == "SWC-MODE-SWITCH-EVENT":
                self.readSwcModeSwitchEvent(child_element, parent)
            elif tag_name == "OPERATION-INVOKED-EVENT":
                self.readOperationInvokedEvent(child_element, parent)
            elif tag_name == "DATA-RECEIVED-EVENT":
                self.readDataReceivedEvent(child_element, parent)
            elif tag_name == "INTERNAL-TRIGGER-OCCURRED-EVENT":
                self.readInternalTriggerOccurredEvent(child_element, parent)
            elif tag_name == "INIT-EVENT":
                self.readInitEvent(child_element, parent)
            else:
                self._raiseError("Unsupported SwcInternalBehavior Event <%s>" % tag_name)

    def readSwPointerTargetProps(self, element: ET.Element, parent: SwDataDefProps):
        child_element = self.find(element, "SW-POINTER-TARGET-PROPS")
        if child_element is not None:
            sw_pointer_target_props = SwPointerTargetProps()
            sw_pointer_target_props.target_category = self.getChildElementOptionalLiteral(child_element, "TARGET-CATEGORY")
            sw_pointer_target_props.sw_data_def_props = self.getSwDataDefProps(child_element, "SW-DATA-DEF-PROPS")
            parent.swPointerTargetProps = sw_pointer_target_props

    def readLParagraph(self, element: ET.Element, paragraph: MultiLanguageParagraph):
        for child_element in self.findall(element, "./L-1"):
            l1 = LOverviewParagraph()
            self.readElementAttributes(child_element, l1)
            l1.value = child_element.text
            if 'L' in child_element.attrib:
                l1.l = child_element.attrib['L']
            paragraph.addL1(l1)
    
    def getMultiLanguageParagraphs(self, element: ET.Element, key: str) -> List[MultiLanguageParagraph]:
        paragraphs = []
        for child_element in self.findall(element, key):
            paragraph = MultiLanguageParagraph()
            self.readElementAttributes(child_element, paragraph)
            self.readLParagraph(child_element, paragraph)
            paragraphs.append(paragraph)
        return paragraphs

    def getDocumentationBlock(self, element: ET.Element, key: str) -> DocumentationBlock:
        block = None
        child_element = self.find(element, key)
        if child_element is not None:
            block = DocumentationBlock()
            self.readElementAttributes(child_element, block)
            for paragraph in self.getMultiLanguageParagraphs(child_element, "P"):
                block.addP(paragraph)
        return block

    def readGeneralAnnotation(self, element: ET.Element, annotation: GeneralAnnotation):
        annotation.setAnnotationOrigin(self.getChildElementOptionalLiteral(element, 'ANNOTATION-ORIGIN')) \
            .setAnnotationText(self.getDocumentationBlock(element, "ANNOTATION-TEXT")) \
            .setLabel(self.getMultilanguageLongName(element, "LABEL"))

    def getAnnotations(self, element: ET.Element) -> List[Annotation]:
        annotations = []
        for child_element in element.findall("./xmlns:ANNOTATIONS/xmlns:ANNOTATION", self.nsmap):
            annotation = Annotation()
            self.readGeneralAnnotation(child_element, annotation)
            annotations.append(annotation)
        return annotations

    def getSwAxisIndividual(self, element: ET.Element) -> SwAxisIndividual:
        props = SwAxisIndividual()
        self.readElementAttributes(element, props)
        props.setInputVariableTypeRef(self.getChildElementOptionalRefType(element, "INPUT-VARIABLE-TYPE-REF")) \
             .setCompuMethodRef(self.getChildElementOptionalRefType(element, "COMPU-METHOD-REF")) \
             .setSwMaxAxisPoints(self.getChildElementOptionalNumericalValue(element, "SW-MAX-AXIS-POINTS")) \
             .setSwMinAxisPoints(self.getChildElementOptionalNumericalValue(element, "SW-MIN-AXIS-POINTS")) \
             .setDataConstrRef(self.getChildElementOptionalRefType(element, "DATA-CONSTR-REF"))
        return props
    
    def getSwAxisGrouped(self, element: ET.Element) -> SwAxisGrouped:
        props = SwAxisGrouped()
        props.setSharedAxisTypeRef(self.getChildElementOptionalRefType(element, "SHARED-AXIS-TYPE-REF"))
        return props

    def getSwCalprmAxis(self, element: ET.Element) -> SwCalprmAxis:
        axis = SwCalprmAxis()
        axis.sw_axis_index = self.getChildElementOptionalNumericalValue(element, "SW-AXIS-INDEX")
        axis.category = self.getChildElementOptionalLiteral(element, "CATEGORY")
        child_element = element.find("./xmlns:SW-AXIS-INDIVIDUAL", self.nsmap)
        if child_element is not None:
            axis.sw_calprm_axis_type_props = self.getSwAxisIndividual(child_element)
        child_element = element.find("./xmlns:SW-AXIS-GROUPED", self.nsmap)
        if child_element is not None:
            axis.sw_calprm_axis_type_props = self.getSwAxisGrouped(child_element)
        
        return axis

    def getSwCalprmAxisSet(self, element: ET.Element, key: str) -> SwCalprmAxisSet:
        set = SwCalprmAxisSet()
        for child_element in element.findall("./xmlns:%s/*" % key, self.nsmap):
            tag_name = self.getTagName(child_element.tag)
            if tag_name == "SW-CALPRM-AXIS":
                set.addSwCalprmAxis(self.getSwCalprmAxis(child_element))
        return set
    
    def readSwDataDefProsInvalidValue(self, element: ET.Element, props: SwDataDefProps):
        child_element = self.find(element, "INVALID-VALUE/*")
        if child_element is not None:
            props.setInvalidValue(self.getValueSpecification(child_element))

    def getSwDataDefProps(self, element: ET.Element, key: str) -> SwDataDefProps:
        child_element = element.find("./xmlns:%s" % key, self.nsmap)
        sw_data_def_props = None
        if child_element is not None:
            conditional_tag = child_element.find("./xmlns:SW-DATA-DEF-PROPS-VARIANTS/xmlns:SW-DATA-DEF-PROPS-CONDITIONAL", self.nsmap)
            if conditional_tag is not None:
                sw_data_def_props = SwDataDefProps()
                self.readElementAttributes(child_element, sw_data_def_props)

                for annotation in self.getAnnotations(conditional_tag):
                    sw_data_def_props.addAnnotation(annotation)

                sw_data_def_props.setBaseTypeRef(self.getChildElementOptionalRefType(conditional_tag, "BASE-TYPE-REF")) \
                                 .setDataConstrRef(self.getChildElementOptionalRefType(conditional_tag, "DATA-CONSTR-REF")) \
                                 .setCompuMethodRef(self.getChildElementOptionalRefType(conditional_tag, "COMPU-METHOD-REF")) \
                                 .setSwImplPolicy(self.getChildElementOptionalLiteral(conditional_tag, "SW-IMPL-POLICY")) \
                                 .setImplementationDataTypeRef(self.getChildElementOptionalRefType(conditional_tag, "IMPLEMENTATION-DATA-TYPE-REF")) \
                                 .setSwCalibrationAccess(self.getChildElementOptionalLiteral(conditional_tag, "SW-CALIBRATION-ACCESS")) \
                                 .setSwCalprmAxisSet(self.getSwCalprmAxisSet(conditional_tag, "SW-CALPRM-AXIS-SET")) \
                                 .setSwRecordLayoutRef(self.getChildElementOptionalRefType(conditional_tag, "SW-RECORD-LAYOUT-REF")) \
                                 .setValueAxisDataTypeRef(self.getChildElementOptionalRefType(conditional_tag, "VALUE-AXIS-DATA-TYPE-REF")) \
                                 .setUnitRef(self.getChildElementOptionalRefType(conditional_tag, "UNIT-REF"))
                self.readSwDataDefProsInvalidValue(conditional_tag, sw_data_def_props)
                self.readSwPointerTargetProps(conditional_tag, sw_data_def_props)
                self.readElementAttributes(conditional_tag, sw_data_def_props.conditional)
        return sw_data_def_props
    
    def readAutosarDataType(self, element: ET.Element, data_type: AutosarDataType):
        self.readIdentifiable(element, data_type)
        data_type.setSwDataDefProps(self.getSwDataDefProps(element, "SW-DATA-DEF-PROPS"))

    def readApplicationPrimitiveDataType(self, element: ET.Element, parent: ARPackage):
        short_name = self.getShortName(element)
        data_type = parent.createApplicationPrimitiveDataType(short_name)
        self.logger.debug("readApplicationPrimitiveDataTypes %s" % short_name)
        self.readAutosarDataType(element, data_type)

    def readApplicationCompositeElementDataPrototype(self, element: ET.Element, prototype: ApplicationCompositeElementDataPrototype):
        prototype.setTypeTRef(self.getChildElementOptionalRefType(element, "TYPE-TREF"))

    def readApplicationRecordElements(self, element: ET.Element, parent: ApplicationRecordDataType):
        for child_element in element.findall("./xmlns:ELEMENTS/xmlns:APPLICATION-RECORD-ELEMENT", self.nsmap):
            short_name = self.getShortName(child_element)
            record_element = parent.createApplicationRecordElement(short_name)
            self.logger.debug("readApplicationRecordElements %s" % short_name)
            self.readIdentifiable(child_element, record_element)
            self.readApplicationCompositeElementDataPrototype(child_element, record_element)

    def readApplicationRecordDataTypes(self, element: ET.Element, parent: ARPackage):
        short_name = self.getShortName(element)
        data_type = parent.createApplicationRecordDataType(short_name)
        self.logger.debug("readApplicationRecordDataTypes %s" % short_name)
        self.readIdentifiable(element, data_type)
        data_type.setSwDataDefProps(self.getSwDataDefProps(element, "SW-DATA-DEF-PROPS"))
        self.readApplicationRecordElements(element, data_type)

    def readImplementationDataTypeElements(self, element: ET.Element, parent: ImplementationDataType):
        for child_element in self.findall(element, "SUB-ELEMENTS/IMPLEMENTATION-DATA-TYPE-ELEMENT"):
            short_name = self.getShortName(child_element)
            type_element = parent.createImplementationDataTypeElement(short_name)
            self.readIdentifiable(child_element, type_element)
            type_element.setArraySize(self.getChildElementOptionalLiteral(child_element, "ARRAY-SIZE")) \
                        .setArraySizeSemantics(self.getChildElementOptionalLiteral(child_element, "ARRAY-SIZE-SEMANTICS"))
            self.readImplementationDataTypeElements(child_element, type_element)
            type_element.setSwDataDefProps(self.getSwDataDefProps(child_element, "SW-DATA-DEF-PROPS"))

    def readImplementationDataType(self, element: ET.Element, parent: ARPackage):
        short_name = self.getShortName(element)
        data_type = parent.createImplementationDataType(short_name)
        self.readAutosarDataType(element, data_type)
        self.readImplementationDataTypeElements(element, data_type)
        data_type.setTypeEmitter(self.getChildElementOptionalLiteral(element, "TYPE-EMITTER"))
        
        
        '''
        if (data_type.getCategory().getValue() == ImplementationDataType.CATEGORY_ARRAY):
            if (len(data_type.getImplementationDataTypeElements()) < 1):
                self._raiseError("Array Sub-Element of <%s> do not defined." % data_type.getShortName())

            array_sub_element = data_type.getImplementationDataTypeElements()[0]
            if (array_sub_element.getCategory().getValue() == ImplementationDataType.CATEGORY_TYPE_REFERENCE):
                data_type.setArrayElementType(array_sub_element.swDataDefProps.implementationDataTypeRef.value)
            elif (array_sub_element.getCategory().getValue() == ImplementationDataType.CATEGORY_TYPE_VALUE):  # TODO: fix 
                return
            else:
                self._raiseError("The category <%s> of array sub-element <%s> does not support." % (
                    array_sub_element.getCategory().getValue(), data_type.getShortName()))
        elif (data_type.getCategory().getValue() == ImplementationDataType.CATEGORY_TYPE_STRUCTURE):
            if len(data_type.getImplementationDataTypeElements()) < 1:
                self._raiseError("Structure Sub-Element of <%s> do not defined." % data_type.getShortName())
            self.readImplementationDataTypeSymbolProps(element, data_type)
            struct_sub_element = data_type.getImplementationDataTypeElements()[0]
            if struct_sub_element.getCategory().getValue() == ImplementationDataType.CATEGORY_TYPE_REFERENCE:
                data_type.setStructElementType(struct_sub_element.getSwDataDefProps().getImplementationDataTypeRef().getValue())
            #elif struct_sub_element.getCategory().getValue() == ImplementationDataType.CATEGORY_TYPE_VALUE:
            #    return
            else:
                self._raiseError("The category <%s> of structure sub-element <%s> does not support." % (
                    struct_sub_element.getCategory().getValue(), data_type.getShortName()))
        '''

    def readBaseTypeDirectDefinition(self, element: ET.Element, definition: BaseTypeDirectDefinition):
        definition.base_type_size = self.getChildElementOptionalNumericalValue(element, "BASE-TYPE-SIZE")
        definition.base_type_encoding = self.getChildElementOptionalLiteral(element, "BASE-TYPE-ENCODING")
        definition.mem_alignment = self.getChildElementOptionalNumericalValue(element, "MEM-ALIGNMENT")
        definition.native_declaration = self.getChildElementOptionalLiteral(element, "NATIVE-DECLARATION")

    def readSwBaseType(self, element: ET.Element, parent: ARPackage):
        short_name = self.getShortName(element)
        data_type = parent.createSwBaseType(short_name)
        self.readIdentifiable(element, data_type)
        self.readBaseTypeDirectDefinition(element, data_type.baseTypeDefinition)

    def getApplicationCompositeElementInPortInterfaceInstanceRef(self, element: ET.Element, key:str) -> ApplicationCompositeElementInPortInterfaceInstanceRef:
        child_element = element.find("./xmlns:%s" % key, self.nsmap)
        iref = None
        if child_element is not None:
            iref = ApplicationCompositeElementInPortInterfaceInstanceRef()
            iref.setRootDataPrototypeRef(self.getChildElementOptionalRefType(child_element, "ROOT-DATA-PROTOTYPE-REF"))\
                .setTargetDataPrototypeRef(self.getChildElementOptionalRefType(child_element, "TARGET-DATA-PROTOTYPE-REF"))
        return iref

    def getCompositeNetworkRepresentation(self, element: ET.Element) -> CompositeNetworkRepresentation:
        self.logger.debug("getCompositeNetworkRepresentation")
        representation = CompositeNetworkRepresentation()
        representation.leaf_element_iref = self.getApplicationCompositeElementInPortInterfaceInstanceRef(element, "LEAF-ELEMENT-IREF")
        representation.network_representation = self.getSwDataDefProps(element, "NETWORK-REPRESENTATION")
        return representation

    def readReceiverComSpec(self, element: ET.Element, com_spec: ReceiverComSpec):
        self.readElementAttributes(element, com_spec)
        for child_element in self.findall(element, "COMPOSITE-NETWORK-REPRESENTATIONS/COMPOSITE-NETWORK-REPRESENTATION"):
            com_spec.addCompositeNetworkRepresentation(self.getCompositeNetworkRepresentation(child_element))
        com_spec.dataElementRef = self.getChildElementOptionalRefType(element, "DATA-ELEMENT-REF")
        com_spec.networkRepresentation = self.getSwDataDefProps(element, "NETWORK-REPRESENTATION")
        com_spec.handleOutOfRange = self.getChildElementOptionalLiteral(element, "HANDLE-OUT-OF-RANGE")
        com_spec.usesEndToEndProtection = self.getChildElementOptionalBooleanValue(element, "USES-END-TO-END-PROTECTION")

    def getSwValues(self, element: ET.Element, key: str) -> SwValues:
        child_element = element.find("./xmlns:%s" % key, self.nsmap) # type: ET.Element
        if child_element is None:
            return None
        sw_values = SwValues()
        self.readElementAttributes(child_element, sw_values)
        for v in self.getChildElementFloatValueList(child_element, "V"):
            sw_values.addV(v)
        sw_values.vt = self.getChildElementOptionalLiteral(child_element, "VT")
        return sw_values
    
    def getValueList(self, element: ET.Element, key: str) -> ValueList:
        value_list = None
        child_element = element.find("./xmlns:%s" % key, self.nsmap) # type: ET.Element
        if child_element is not None:
            self.logger.debug("getValueList %s" % key)
            value_list = ValueList()
            self.readElementAttributes(child_element, value_list)
            value_list.v = self.getChildElementOptionalFloatValue(child_element, "V")
        return value_list

    def getSwValueCont(self, element: ET.Element) -> SwValueCont:
        cont = None
        child_element = element.find("./xmlns:SW-VALUE-CONT", self.nsmap)
        if child_element is not None:
            self.logger.debug("getSwValueCont")
            cont = SwValueCont()
            self.readElementAttributes(child_element, cont)
            cont.unit_ref = self.getChildElementOptionalRefType(child_element, "UNIT-REF")
            cont.sw_arraysize = self.getValueList(child_element, "SW-ARRAYSIZE")
            cont.sw_values_phys = self.getSwValues(child_element, "SW-VALUES-PHYS")
        return cont
    
    def readApplicationValueSpecification(self, element: ET.Element, value_spec: ApplicationValueSpecification):
        self.readValueSpecification(element, value_spec)
        value_spec.category = self.getChildElementOptionalLiteral(element, "CATEGORY")
        value_spec.sw_value_cont = self.getSwValueCont(element)

        self.logger.debug("readApplicationValueSpecification Category %s" % value_spec.category)

    def getInitValue(self, element: ET.Element) -> ValueSpecification:
        value_spec = None
        child_element = self.find(element, "INIT-VALUE/*")
        if child_element is not None:
            self.logger.debug("getInitValue")
            value_spec = self.getValueSpecification(child_element)
        return value_spec
    
    def getClientComSpec(self, element: ET.Element) -> ClientComSpec:
        com_spec = ClientComSpec()
        self.readElementAttributes(element, com_spec)
        com_spec.operationRef = self.getChildElementOptionalRefType(element, "OPERATION-REF")
        return com_spec
    
    def getParameterRequireComSpec(self, element: ET.Element) -> ParameterRequireComSpec:
        com_spec = ParameterRequireComSpec()
        self.readElementAttributes(element, com_spec)
        com_spec.setInitValue(self.getInitValue(element)) \
                .setParameterRef(self.getChildElementOptionalRefType(element, "PARAMETER-REF"))
        return com_spec
    
    def getQueuedReceiverComSpec(self, element: ET.Element) -> QueuedReceiverComSpec:
        com_spec = QueuedReceiverComSpec()
        self.readElementAttributes(element, com_spec)
        self.readReceiverComSpec(element, com_spec)
        com_spec.queueLength = self.getChildElementOptionalNumericalValue(element, "QUEUE-LENGTH")
        return com_spec
    
    def getModeSwitchReceiverComSpec(self, element: ET.Element) -> ModeSwitchReceiverComSpec:
        com_spec = ModeSwitchReceiverComSpec()
        self.readElementAttributes(element, com_spec)
        com_spec.modeGroupRef = self.getChildElementOptionalRefType(element, "MODE-GROUP-REF")
        return com_spec

    def getNonqueuedReceiverComSpec(self, element: ET.Element) -> NonqueuedReceiverComSpec:
        com_spec = NonqueuedReceiverComSpec()
        self.readElementAttributes(element, com_spec)            
        self.readReceiverComSpec(element, com_spec)
        com_spec.aliveTimeout = self.getChildElementOptionalFloatValue(element, "ALIVE-TIMEOUT")
        com_spec.enableUpdated = self.getChildElementOptionalBooleanValue(element, "ENABLE-UPDATE")
        com_spec.handleNeverReceived = self.getChildElementOptionalBooleanValue(element, "HANDLE-NEVER-RECEIVED")
        com_spec.handleTimeoutType = self.getChildElementOptionalLiteral(element, "HANDLE-TIMEOUT-TYPE")
        com_spec.initValue = self.getInitValue(element)
        return com_spec

    def readRequiredComSpec(self, element: ET.Element, parent: RPortPrototype):
        for child_element in element.findall("./xmlns:REQUIRED-COM-SPECS/*", self.nsmap):
            tag_name = self.getTagName(child_element.tag)
            if tag_name == "NONQUEUED-RECEIVER-COM-SPEC":
                parent.addRequiredComSpec(self.getNonqueuedReceiverComSpec(child_element))
            elif tag_name == "CLIENT-COM-SPEC":
                parent.addRequiredComSpec(self.getClientComSpec(child_element))
            elif tag_name == "QUEUED-RECEIVER-COM-SPEC":
                parent.addRequiredComSpec(self.getQueuedReceiverComSpec(child_element))
            elif tag_name == "MODE-SWITCH-RECEIVER-COM-SPEC":
                parent.addRequiredComSpec(self.getModeSwitchReceiverComSpec(child_element))
            elif tag_name == "PARAMETER-REQUIRE-COM-SPEC":
                parent.addRequiredComSpec(self.getParameterRequireComSpec(child_element))
            else:
                self._raiseError("Unsupported RequiredComSpec <%s>" % tag_name)

    def readRPortPrototype(self, element: ET.Element, parent: AtomicSwComponentType):
        short_name = self.getShortName(element)
        self.logger.debug("readRPortPrototype %s" % short_name)
        prototype = parent.createRPortPrototype(short_name)
        self.readIdentifiable(element, prototype)
        prototype.setRequiredInterfaceTRef(self.getChildElementOptionalRefType(element, "REQUIRED-INTERFACE-TREF"))

        self.readRequiredComSpec(element, prototype)

    def readAtomicSwComponentTypePorts(self, element: ET.Element, sw_component: AtomicSwComponentType):
        for child_element in self.findall(element, "PORTS/*"):
            tag_name = self.getTagName(child_element)
            if tag_name == "P-PORT-PROTOTYPE":
                self.readPPortPrototype(child_element, sw_component)
            elif tag_name == "R-PORT-PROTOTYPE":
                self.readRPortPrototype(child_element, sw_component)
            else:
                self._raiseError("Unsupported Port Prototype <%s>" % tag_name)

    def readTransmissionAcknowledgementRequest(self, element: ET.Element) -> TransmissionAcknowledgementRequest:
        child_element = element.find("./xmlns:TRANSMISSION-ACKNOWLEDGE", self.nsmap)
        if (child_element is not None):
            acknowledge = TransmissionAcknowledgementRequest()
            self.readElementAttributes(child_element, acknowledge)
            acknowledge.timeout = self.getChildElementOptionalFloatValue(child_element, "TIMEOUT")
            return acknowledge
        return None

    def readSenderComSpec(self, element:ET.Element, com_spec: SenderComSpec):
        self.readElementAttributes(element, com_spec)
        for child_element in element.findall("./xmlns:COMPOSITE-NETWORK-REPRESENTATIONS/xmlns:COMPOSITE-NETWORK-REPRESENTATION", self.nsmap):
            com_spec.addCompositeNetworkRepresentation(self.getCompositeNetworkRepresentation(child_element))
        com_spec.setDataElementRef(self.getChildElementOptionalRefType(element, "DATA-ELEMENT-REF")) \
                .setNetworkRepresentation(self.getSwDataDefProps(element, "NETWORK-REPRESENTATION")) \
                .setHandleOutOfRange(self.getChildElementOptionalLiteral(element, "HANDLE-OUT-OF-RANGE")) \
                .setTransmissionAcknowledge(self.readTransmissionAcknowledgementRequest(element)) \
                .setUsesEndToEndProtection(self.getChildElementOptionalBooleanValue(element, "USES-END-TO-END-PROTECTION"))

    def getNonqueuedSenderComSpec(self, element) -> NonqueuedSenderComSpec:
        com_spec = NonqueuedSenderComSpec()
        self.readSenderComSpec(element, com_spec)
        com_spec.setInitValue(self.getInitValue(element))
        return com_spec
    
    def getServerComSpec(self, element) -> ServerComSpec:
        com_spec = ServerComSpec()
        com_spec.setOperationRef(self.getChildElementOptionalRefType(element, "OPERATION-REF")) \
                .setQueueLength(self.getChildElementOptionalNumericalValue(element, "QUEUE-LENGTH"))
        return com_spec
    
    def getQueuedSenderComSpec(self, element) -> QueuedSenderComSpec:
        com_spec = QueuedSenderComSpec()
        self.readSenderComSpec(element, com_spec)
        return com_spec
    
    def getModeSwitchSenderComSpec(self, element) -> ModeSwitchSenderComSpec:
        com_spec = ModeSwitchSenderComSpec()
        com_spec.setModeGroupRef(self.getChildElementOptionalRefType(element, "MODE-GROUP-REF")) \
                .setQueueLength(self.getChildElementOptionalNumericalValue(element, "QUEUE-LENGTH"))
        return com_spec

    def readProvidedComSpec(self, element: ET.Element, parent: PPortPrototype):
        for child_element in element.findall("./xmlns:PROVIDED-COM-SPECS/*", self.nsmap):
            tag_name = self.getTagName(child_element.tag)
            if tag_name == "NONQUEUED-SENDER-COM-SPEC":
                parent.addProvidedComSpec(self.getNonqueuedSenderComSpec(child_element))
            elif tag_name == "SERVER-COM-SPEC":
                parent.addProvidedComSpec(self.getServerComSpec(child_element))
            elif tag_name == "QUEUED-SENDER-COM-SPEC":
                parent.addProvidedComSpec(self.getQueuedSenderComSpec(child_element))
            elif tag_name == "MODE-SWITCH-SENDER-COM-SPEC":
                parent.addProvidedComSpec(self.getModeSwitchSenderComSpec(child_element))
            else:
                self._raiseError("Unsupported RequiredComSpec <%s>" % tag_name)

    def readPPortPrototype(self, element: ET.Element, parent: AtomicSwComponentType):
        short_name = self.getShortName(element)
        self.logger.debug("readPPortPrototype %s" % short_name)
        prototype = parent.createPPortPrototype(short_name)
        self.readIdentifiable(element, prototype)
        prototype.setProvidedInterfaceTRef(self.getChildElementOptionalRefType(element, "PROVIDED-INTERFACE-TREF"))

        self.readProvidedComSpec(element, prototype)

    def readPortGroupInnerGroupIRefs(self, element: ET.Element, parent: PortGroup):
        for child_element in self.findall(element, "INNER-GROUP-IREFS/INNER-GROUP-IREF"):
            inner_group_iref = InnerPortGroupInCompositionInstanceRef()
            #inner_group_iref.contextRef = self.getChildElementOptionalRefType(child_element, "CONTEXT-REF")
            inner_group_iref.setTargetRef(self.getChildElementOptionalRefType(child_element, "TARGET-REF"))
            parent.addInnerGroupIRef(inner_group_iref)

    def readPortGroupOuterPortRefs(self, element: ET.Element, parent: PortGroup):
        for child_element in self.findall(element, "OUTER-PORTS/PORT-PROTOTYPE-REF-CONDITIONAL"):
            parent.addOuterPortRef(self.getChildElementOptionalRefType(child_element, "PORT-PROTOTYPE-REF"))

    def readPortGroup(self, element: ET.Element, parent: SwComponentType):
        short_name = self.getShortName(element)
        self.logger.debug("readPortGroup %s" % short_name)
        port_group = parent.createPortGroup(short_name)
        self.readIdentifiable(element, port_group)
        self.readPortGroupInnerGroupIRefs(element, port_group)
        self.readPortGroupOuterPortRefs(element, port_group)

    def readSwComponentTypePortGroups(self, element: ET.Element, parent: SwComponentType):
        for child_element in element.findall("./xmlns:PORT-GROUPS/*", self.nsmap):
            tag_name = self.getTagName(child_element.tag)
            if tag_name == "PORT-GROUP":
                self.readPortGroup(child_element, parent)
            else:
                self._raiseError("Unsupported Port Group type: %s" % tag_name)

    def readSwComponentType(self, element: ET.Element, parent: SwComponentType):
        self.readIdentifiable(element, parent)
        self.readAtomicSwComponentTypePorts(element, parent)
        self.readSwComponentTypePortGroups(element, parent)

    def readAtomicSwComponentType(self, element, parent: AtomicSwComponentType):
        self.readSwComponentType(element, parent)
        self.readSwcInternalBehavior(element, parent)

    def readEcuAbstractionSwComponent(self, element, parent: ARPackage):
        short_name = self.getShortName(element)
        sw_component = parent.createEcuAbstractionSwComponentType(short_name)
        self.readAtomicSwComponentType(element, sw_component)

    def readApplicationSwComponentTypes(self, element: ET.Element, parent: ARPackage):
        short_name = self.getShortName(element)
        sw_component = parent.createApplicationSwComponentType(short_name)
        self.readAtomicSwComponentType(element, sw_component)

    def readComplexDeviceDriverSwComponentType(self, element: ET.Element, parent: ARPackage):
        short_name = self.getShortName(element)
        sw_component = parent.createComplexDeviceDriverSwComponentType(short_name)
        self.logger.debug("readComplexDeviceDriverSwComponentType <%s>" % short_name)
        self.readAtomicSwComponentType(element, sw_component)

    def readSensorActuatorSwComponentType(self, element: ET.Element, parent: ARPackage):
        short_name = self.getShortName(element)
        sw_component = parent.createSensorActuatorSwComponentType(short_name)
        self.logger.debug("readSensorActuatorSwComponentType <%s>" % short_name)
        self.readAtomicSwComponentType(element, sw_component)

    def readServiceSwComponentType(self, element: ET.Element, parent: ARPackage):
        short_name = self.getShortName(element)
        sw_component = parent.createServiceSwComponentType(short_name)
        self.logger.debug("readServiceSwComponentType <%s>" % short_name)
        self.readAtomicSwComponentType(element, sw_component)

    def readPPortInCompositionInstanceRef(self, element: ET.Element, p_port_in_composition_instance_ref: PPortInCompositionInstanceRef):
        p_port_in_composition_instance_ref.setContextComponentRef(self.getChildElementOptionalRefType(element, "CONTEXT-COMPONENT-REF")) \
                                          .setTargetPPortRef(self.getChildElementOptionalRefType(element, "TARGET-P-PORT-REF"))
        
        self.logger.debug("PPortInCompositionInstanceRef")
        self.logger.debug("  CONTEXT-COMPONENT-REF DEST: %s, %s"
                          % (p_port_in_composition_instance_ref.getContextComponentRef().getDest(), p_port_in_composition_instance_ref.getContextComponentRef().getValue()))
        self.logger.debug("  TARGET-P-PORT-REF DEST: %s, %s" 
                          % (p_port_in_composition_instance_ref.getTargetPPortRef().getDest(), p_port_in_composition_instance_ref.getTargetPPortRef().getValue()))

    def readRPortInCompositionInstanceRef(self, element, r_port_in_composition_instance_ref: RPortInCompositionInstanceRef):
        r_port_in_composition_instance_ref.setContextComponentRef(self.getChildElementOptionalRefType(element, "CONTEXT-COMPONENT-REF")) \
                                          .setTargetRPortRef(self.getChildElementOptionalRefType(element, "TARGET-R-PORT-REF"))

        self.logger.debug("RPortInCompositionInstanceRef")
        self.logger.debug("  CONTEXT-COMPONENT-REF DEST: %s, %s"
                          % (r_port_in_composition_instance_ref.getContextComponentRef().getDest(), r_port_in_composition_instance_ref.getContextComponentRef().getValue()))
        self.logger.debug("  TARGET-P-PORT-REF DEST: %s, %s" 
                          % (r_port_in_composition_instance_ref.getTargetRPortRef().getDest(), r_port_in_composition_instance_ref.getTargetRPortRef().getValue()))

    def readAssemblySwConnectorProviderIRef(self, element: ET.Element, parent: AssemblySwConnector):
        child_element = self.find(element, "PROVIDER-IREF")
        if (child_element is not None):
            provide_iref = PPortInCompositionInstanceRef()
            self.readElementAttributes(child_element, provide_iref)
            self.readPPortInCompositionInstanceRef(child_element, provide_iref)
            parent.setProviderIRef(provide_iref)

    def readAssemblySwConnectorRequesterIRef(self, element: ET.Element, parent: AssemblySwConnector):
        child_element = self.find(element, "REQUESTER-IREF")
        if (child_element is not None):
            requester_iref = RPortInCompositionInstanceRef()
            self.readElementAttributes(child_element, requester_iref)
            self.readRPortInCompositionInstanceRef(child_element, requester_iref)
            parent.setRequesterIRef(requester_iref)

    def readAssemblySwConnectors(self, element: ET.Element, parent: CompositionSwComponentType):
        for child_element in element.findall("./xmlns:CONNECTORS/xmlns:ASSEMBLY-SW-CONNECTOR", self.nsmap):
            short_name = self.getShortName(child_element)
            self.logger.debug("readAssemblySwConnectors %s" % short_name)

            connector = parent.createAssemblySwConnector(short_name)
            self.readIdentifiable(child_element, connector)
            self.readAssemblySwConnectorProviderIRef(child_element, connector)
            self.readAssemblySwConnectorRequesterIRef(child_element, connector)

    def readDelegationSwConnectorInnerPortIRef(self, element, parent: DelegationSwConnector):
        inner_port_iref_element = self.find(element, "INNER-PORT-IREF")
        if (inner_port_iref_element is not None):
            child_element = self.find(inner_port_iref_element, "R-PORT-IN-COMPOSITION-INSTANCE-REF")
            if (child_element is not None):
                r_port_in_composition_instance_ref = RPortInCompositionInstanceRef()
                self.readRPortInCompositionInstanceRef(child_element, r_port_in_composition_instance_ref)
                parent.setInnerPortIRref(r_port_in_composition_instance_ref)
                return
            
            child_element = self.find(inner_port_iref_element, "P-PORT-IN-COMPOSITION-INSTANCE-REF")
            if (child_element is not None):
                p_port_in_composition_instance_ref = PPortInCompositionInstanceRef()
                self.readPPortInCompositionInstanceRef(child_element, p_port_in_composition_instance_ref)
                parent.setInnerPortIRref(p_port_in_composition_instance_ref)
                return
            
            self._raiseError("Unsupported child element of INNER-PORT-IREF")

    def readDelegationSwConnectors(self, element, parent: CompositionSwComponentType):
        for child_element in self.findall(element, "CONNECTORS/DELEGATION-SW-CONNECTOR"):
            short_name = self.getShortName(child_element)
            self.logger.debug("readDelegationSwConnectors %s" % short_name)

            connector = parent.createDelegationSwConnector(short_name)
            self.readIdentifiable(child_element, connector)
            self.readDelegationSwConnectorInnerPortIRef(child_element, connector)

            if connector.getInnerPortIRref() == None and connector.getOuterPortRef() == None:
                self._raiseError("Invalid PortPrototype of DELEGATION-SW-CONNECTOR")

            connector.setOuterPortRef(self.getChildElementOptionalRefType(child_element, "OUTER-PORT-REF"))
            self.logger.debug("OUTER-PORT-REF DEST: %s, %s"
                          % (connector.getOuterPortRef().getDest(), connector.getOuterPortRef().getValue()))

    def readSwComponentPrototypes(self, element: ET.Element, parent: CompositionSwComponentType):
        for child_element in element.findall("./xmlns:COMPONENTS/xmlns:SW-COMPONENT-PROTOTYPE", self.nsmap):
            short_name = self.getShortName(child_element)
            self.logger.debug("readSwComponentPrototypes %s" % short_name)
            prototype = parent.createSwComponentPrototype(short_name)
            self.readIdentifiable(child_element, prototype)
            prototype.typeTRef = self.getChildElementOptionalRefType(child_element, "TYPE-TREF")

    def readCompositionSwComponentTypeDataTypeMappingSet(self, element: ET.Element, parent: CompositionSwComponentType):
        child_element = element.find("./xmlns:DATA-TYPE-MAPPING-REFS", self.nsmap)
        self.logger.debug("readDataTypeMappingSet")
        if child_element is not None:
            for ref in self.getChildElementRefTypeList(child_element, "./DATA-TYPE-MAPPING-REF"):
                parent.addDataTypeMapping(ref)

    def readCompositionSwComponentType(self, element: ET.Element, parent: ARPackage):
        short_name = self.getShortName(element)
        self.logger.debug("readCompositionSwComponentTypes: <%s>" % short_name)

        sw_component = parent.createCompositionSwComponentType(short_name)
        self.readIdentifiable(element, sw_component)
        self.readSwComponentType(element, sw_component)
        self.readSwComponentPrototypes(element, sw_component)
        self.readAssemblySwConnectors(element, sw_component)
        self.readDelegationSwConnectors(element, sw_component)
        self.readCompositionSwComponentTypeDataTypeMappingSet(element, sw_component)

        self.logger.debug("ReadCompositionSwComponentTypes: <%s> (Done)" % short_name)

    def readDataTypeMaps(self, element: ET.Element, parent: DataTypeMappingSet):
        for child_element in element.findall("./xmlns:DATA-TYPE-MAPS/xmlns:DATA-TYPE-MAP", self.nsmap):
            data_type_map = DataTypeMap()
            self.readElementAttributes(child_element, data_type_map)
            data_type_map.application_data_type_ref = self.getChildElementOptionalRefType(child_element, "APPLICATION-DATA-TYPE-REF")
            data_type_map.implementation_data_type_ref = self.getChildElementOptionalRefType(child_element, "IMPLEMENTATION-DATA-TYPE-REF")
            parent.addDataTypeMap(data_type_map)
            # add the data type map to global namespace
            AUTOSAR.getInstance().addDataTypeMap(data_type_map)

    def readModeRequestTypeMaps(self, element: ET.Element, parent: DataTypeMappingSet):
        for child_element in element.findall("./xmlns:MODE-REQUEST-TYPE-MAPS/xmlns:MODE-REQUEST-TYPE-MAP", self.nsmap):
            map = ModeRequestTypeMap()
            self.readElementAttributes(child_element, map)
            map.implementation_data_type_ref = self.getChildElementOptionalRefType(child_element, "IMPLEMENTATION-DATA-TYPE-REF")
            map.mode_group_ref = self.getChildElementOptionalRefType(child_element, "MODE-GROUP-REF")
            parent.addModeRequestTypeMap(map)

    def readDataTypeMappingSet(self, element: ET.Element, parent: ARPackage):
        short_name = self.getShortName(element)
        mapping_set = parent.createDataTypeMappingSet(short_name)
        self.readIdentifiable(element, mapping_set)
        self.readDataTypeMaps(element, mapping_set)
        self.readModeRequestTypeMaps(element, mapping_set)

    def readSenderReceiverInterfaceDataElements(self, element: ET.Element, sr_interface: SenderReceiverInterface):
        for child_element in element.findall("./xmlns:DATA-ELEMENTS/xmlns:VARIABLE-DATA-PROTOTYPE", self.nsmap):
            short_name = self.getShortName(child_element)
            prototype = sr_interface.createDataElement(short_name)
            self.readIdentifiable(child_element, prototype)
            prototype.swDataDefProps = self.getSwDataDefProps(child_element, "SW-DATA-DEF-PROPS")
            self.readAutosarDataPrototype(child_element, prototype)
            prototype.initValue = self.getInitValue(child_element)

    def readSenderReceiverInterfaceInvalidationPolicies(self, element: ET.Element, sr_interface: SenderReceiverInterface):
        for child_element in self.findall(element, "INVALIDATION-POLICYS/INVALIDATION-POLICY"):
            policy = InvalidationPolicy()
            policy.setDataElementRef(self.getChildElementOptionalRefType(child_element, "DATA-ELEMENT-REF")) \
                  .setHandleInvalid(self.getChildElementOptionalLiteral(child_element, "HANDLE-INVALID"))
            sr_interface.addInvalidationPolicy(policy)

    def readInvalidationPolicys(self, element: ET.Element, parent: SenderReceiverInterface):
        for child_element in element.findall("./xmlns:INVALIDATION-POLICYS/xmlns:INVALIDATION-POLICY", self.nsmap):
            # short_name = self.getShortName(child_element)
            policy = parent.createInvalidationPolicy()
            self.readIdentifiable(child_element, policy)
            policy.data_element_ref = self.getChildElementOptionalRefType(child_element, "DATA-ELEMENT-REF")
            policy.handle_invalid = self.getChildElementOptionalLiteral(child_element, "HANDLE-INVALID")

    def readSenderReceiverInterfaces(self, element, parent: ARPackage):
        short_name = self.getShortName(element)
        sr_interface = parent.createSenderReceiverInterface(short_name)
        self.readIdentifiable(element, sr_interface)
        sr_interface.isService = self.getChildElementOptionalBooleanValue(element, "IS-SERVICE")
        self.readSenderReceiverInterfaceDataElements(element, sr_interface)
        self.readSenderReceiverInterfaceInvalidationPolicies(element, sr_interface)

    def readArgumentDataPrototypes(self, element: ET.Element, parent: ClientServerOperation):
        for child_element in element.findall("./xmlns:ARGUMENTS/xmlns:ARGUMENT-DATA-PROTOTYPE", self.nsmap):
            short_name = self.getShortName(child_element)
            prototype = ArgumentDataPrototype(property, short_name)
            self.readIdentifiable(child_element, prototype)
            prototype.swDataDefProps = self.getSwDataDefProps(child_element, "SW-DATA-DEF-PROPS")
            prototype.typeTRef = self.getChildElementOptionalRefType(child_element, "TYPE-TREF")
            prototype.direction = self.getChildElementOptionalLiteral(child_element, "DIRECTION")
            prototype.server_argument_impl_policy = self.getChildElementOptionalLiteral(child_element, "SERVER-ARGUMENT-IMPL-POLICY")
            parent.addArgumentDataPrototype(prototype)

    def readPossibleErrorRefs(self, element: ET.Element, parent: ClientServerOperation):
        child_element = element.find("./xmlns:POSSIBLE-ERROR-REFS", self.nsmap)
        if child_element is not None:
            for ref in self.getChildElementRefTypeList(child_element, "./POSSIBLE-ERROR-REF"):
                parent.addPossibleErrorRef(ref)

    def readOperations(self, element: ET.Element, parent: ClientServerInterface):
        for child_element in element.findall("./xmlns:OPERATIONS/xmlns:CLIENT-SERVER-OPERATION", self.nsmap):
            short_name = self.getShortName(child_element)
            operation = parent.createOperation(short_name)
            self.readIdentifiable(child_element, operation)
            self.readArgumentDataPrototypes(child_element, operation)
            self.readPossibleErrorRefs(child_element, operation)

    def readPossibleErrors(self, element: ET.Element, parent: ClientServerInterface):
        for child_element in element.findall("./xmlns:POSSIBLE-ERRORS/xmlns:APPLICATION-ERROR", self.nsmap):
            short_name = self.getShortName(child_element)
            error = parent.createApplicationError(short_name)
            self.readIdentifiable(child_element, error) # some errors has its uuid
            error.error_code = self.getChildElementOptionalNumericalValue(child_element, "ERROR-CODE")

    def readPortInterface(self, element: ET.Element, port_interface: PortInterface):
        port_interface.isService = self.getChildElementOptionalBooleanValue(element, "IS-SERVICE")
        port_interface.serviceKind = self.getChildElementOptionalLiteral(element, "SERVICE-KIND")

    def readClientServerInterface(self, element: ET.Element, parent: ARPackage):
        short_name = self.getShortName(element)
        cs_interface = parent.createClientServerInterface(short_name)
        self.readIdentifiable(element, cs_interface)
        self.readPortInterface(element, cs_interface)
        self.readOperations(element, cs_interface)
        self.readPossibleErrors(element, cs_interface)

    def readCompuConst(self, element: ET.Element, parent: CompuScale):
        child_element = element.find("./xmlns:COMPU-CONST/xmlns:VT", self.nsmap)
        if (child_element is not None):
            self.logger.debug("readCompuConst VT: %s" % child_element.text)
            contents = CompuScaleConstantContents()
            contents.compu_const = CompuConst()
            contents.compu_const.compu_const_content_type = CompuConstTextContent()
            contents.compu_const.compu_const_content_type.vt = ARLiteral()
            contents.compu_const.compu_const_content_type.vt.setValue(child_element.text)
            parent.compuScaleContents = contents

    def readCompuNominatorDenominator(self, element: ET.Element, key: str, parent: CompuNominatorDenominator):
        for child_element in element.findall("./xmlns:%s/xmlns:V" % key, self.nsmap):
            self.logger.debug("readCompuNominatorDenominator - %s: %s" % (key, child_element.text))
            parent.add_v(child_element.text)

    def readCompuRationCoeffs(self, element: ET.Element, parent: CompuScale):
        child_element = element.find("./xmlns:COMPU-RATIONAL-COEFFS", self.nsmap)
        if (child_element is not None):
            self.logger.debug("readCompuRationCoeffs")
            contents = CompuScaleRationalFormula()
            contents.compu_rational_coeffs = CompuRationalCoeffs()
            contents.compu_rational_coeffs.compu_denominator = CompuNominatorDenominator()
            contents.compu_rational_coeffs.compu_numerator = CompuNominatorDenominator()
            self.readCompuNominatorDenominator(child_element, "COMPU-DENOMINATOR", contents.compu_rational_coeffs.compu_denominator)
            self.readCompuNominatorDenominator(child_element, "COMPU-NUMERATOR", contents.compu_rational_coeffs.compu_numerator)
            parent.compuScaleContents = contents

    def readCompuScaleContents(self, element: ET.Element, parent: CompuScale):
        self.readCompuConst(element, parent)
        self.readCompuRationCoeffs(element, parent)

    def readCompuScales(self, element: ET.Element, parent: CompuScales):
        for child_element in element.findall('./xmlns:COMPU-SCALES/xmlns:COMPU-SCALE', self.nsmap):
            compu_scale = CompuScale()
            self.readElementAttributes(child_element, compu_scale)
            compu_scale.short_label = self.getChildElementOptionalLiteral(child_element, "SHORT-LABEL")
            compu_scale.symbol = self.getChildElementOptionalLiteral(child_element, "SYMBOL")
            compu_scale.lowerLimit = self.getChildLimitElement(child_element, "LOWER-LIMIT")
            compu_scale.upperLimit = self.getChildLimitElement(child_element, "UPPER-LIMIT")
            self.readCompuScaleContents(child_element, compu_scale)
            parent.addCompuScale(compu_scale)

    def readCompuInternalToPhys(self, element: ET.Element, parent: CompuMethod):
        child_element = element.find("./xmlns:COMPU-INTERNAL-TO-PHYS", self.nsmap)
        if (child_element is not None):
            parent.compu_internal_to_phys = Compu()
            self.readElementAttributes(child_element, parent.compu_internal_to_phys)
            parent.compu_internal_to_phys.compu_content = CompuScales()
            self.readCompuScales(child_element, parent.compu_internal_to_phys.compu_content)

    def readCompuMethod(self, element: ET.Element, parent: ARPackage):
        short_name = self.getShortName(element)
        self.logger.debug("readCompuMethods %s" % short_name)
        compu_method = parent.createCompuMethod(short_name)
        self.readIdentifiable(element, compu_method)
        compu_method.unit_ref = self.getChildElementOptionalRefType(element, "UNIT-REF")
        self.readCompuInternalToPhys(element, compu_method)

    def readSwcBswRunnableMappings(self, element: ET.Element, parent: SwcBswMapping):
        for child_element in element.findall("./xmlns:RUNNABLE-MAPPINGS/xmlns:SWC-BSW-RUNNABLE-MAPPING", self.nsmap):
            mapping = SwcBswRunnableMapping()
            mapping.bswEntityRef = self.getChildElementOptionalRefType(child_element, "BSW-ENTITY-REF")
            mapping.swcRunnableRef = self.getChildElementOptionalRefType(child_element, "SWC-RUNNABLE-REF")
            parent.addRunnableMapping(mapping)

    def readSwcBswMappings(self, element: ET.Element, parent: ARPackage):
        short_name = self.getShortName(element)
        self.logger.debug("readSwcBswMappings %s" % short_name)
        swc_bsw_mapping = parent.createSwcBswMapping(short_name)
        swc_bsw_mapping.bswBehaviorRef = self.getChildElementOptionalRefType(element, "BSW-BEHAVIOR-REF")
        self.readSwcBswRunnableMappings(element, swc_bsw_mapping)
        swc_bsw_mapping.swcBehaviorRef = self.getChildElementOptionalRefType(element, "SWC-BEHAVIOR-REF")

    def readValueSpecification(self, element: ET.Element, value_spec: ValueSpecification):
        self.readElementAttributes(element, value_spec)
        value_spec.short_label = self.getChildElementOptionalLiteral(element, "SHORT-LABEL")
        self.logger.debug("readValueSpecification")

    def getApplicationValueSpecification(self, element: ET.Element) -> ApplicationValueSpecification:
        self.logger.debug("getApplicationValueSpecification")
        value_spec = ApplicationValueSpecification()
        self.readValueSpecification(element, value_spec)
        value_spec.category = self.getChildElementOptionalLiteral(element, "CATEGORY")
        value_spec.sw_value_cont = self.getSwValueCont(element)
        return value_spec
    
    def getNumericalValueSpecification(self, element: ET.Element) -> NumericalValueSpecification:
        self.logger.debug("getNumericalValueSpecification")
        value_spec = NumericalValueSpecification()
        self.readValueSpecification(element, value_spec)
        value_spec.value = self.getChildElementOptionalFloatValue(element, "VALUE")
        return value_spec
    
    def getTextValueSpecification(self, element: ET.Element) -> TextValueSpecification:
        self.logger.debug("getTextValueSpecification")
        value_spec = TextValueSpecification()
        self.readValueSpecification(element, value_spec)
        value_spec.value = self.getChildElementOptionalLiteral(element, "VALUE")
        return value_spec

    def getArrayValueSpecification(self, element: ET.Element) -> ArrayValueSpecification:
        self.logger.debug("getArrayValueSpecification")
        value_spec = ArrayValueSpecification()
        self.readValueSpecification(element, value_spec)
        child_elements = element.findall("./xmlns:ELEMENTS/*", self.nsmap)
        for child_element in child_elements:
            value_spec.addElement(self.getValueSpecification(child_element))
        return value_spec

    def getConstantReference(self, element: ET.Element) -> ConstantReference:
        self.logger.debug("getConstantReference")
        value_spec = ConstantReference()
        self.readValueSpecification(element, value_spec)
        value_spec.setConstantRef(self.getChildElementOptionalRefType(element, "CONSTANT-REF"))
        return value_spec         

    def getValueSpecification(self, element: ET.Element) -> ValueSpecification:
        tag_name = self.getTagName(element.tag)
        if tag_name == "APPLICATION-VALUE-SPECIFICATION":
            value_spec = self.getApplicationValueSpecification(element)
        elif tag_name == "RECORD-VALUE-SPECIFICATION":
            value_spec = self.getRecordValueSpecification(element)
        elif tag_name == "NUMERICAL-VALUE-SPECIFICATION":
            value_spec = self.getNumericalValueSpecification(element)
        elif tag_name == "ARRAY-VALUE-SPECIFICATION":
            value_spec = self.getArrayValueSpecification(element)
        elif tag_name == "TEXT-VALUE-SPECIFICATION":
            value_spec = self.getTextValueSpecification(element)
        elif tag_name == "CONSTANT-REFERENCE":
            value_spec = self.getConstantReference(element)
        else:
            raise NotImplementedError("Unsupported RecordValueSpecificationField %s" % tag_name)
        return value_spec

    def readRecordValueSpecificationFields(self, element: ET.Element, spec: RecordValueSpecification):
        for child_element in element.findall("./xmlns:FIELDS/*", self.nsmap):
            spec.addField(self.getValueSpecification(child_element))

    def getRecordValueSpecification(self, element: ET.Element) -> RecordValueSpecification:
        value_spec = RecordValueSpecification()
        self.readValueSpecification(element, value_spec)
        self.readRecordValueSpecificationFields(element, value_spec)
        return value_spec

    def readConstantSpecification(self, element: ET.Element, parent: ARPackage):
        short_name = self.getShortName(element)
        self.logger.debug("readConstantSpecification %s" % short_name)
        spec = parent.createConstantSpecification(short_name)
        self.readIdentifiable(element, spec)
        for value_spec_tag in self.findall(element, "VALUE-SPEC/*"):
            spec.setValueSpec(self.getValueSpecification(value_spec_tag))
                
    def readInternalConstrs(self, element: ET.Element, parent: DataConstrRule):
        child_element = element.find("./xmlns:INTERNAL-CONSTRS", self.nsmap)
        if child_element is not None:
            constrs = InternalConstrs()
            self.readElementAttributes(child_element, constrs)
            constrs.lower_limit = self.getChildLimitElement(child_element, "LOWER-LIMIT")
            constrs.upper_limit = self.getChildLimitElement(child_element, "UPPER-LIMIT")
            parent.internalConstrs = constrs

    def readPhysConstrs(self, element: ET.Element, parent: DataConstrRule):
        child_element = element.find("./xmlns:PHYS-CONSTRS", self.nsmap)
        if child_element is not None:
            constrs = PhysConstrs()
            self.readElementAttributes(child_element, constrs)
            constrs.lower_limit = self.getChildLimitElement(child_element, "LOWER-LIMIT")
            constrs.upper_limit = self.getChildLimitElement(child_element, "UPPER-LIMIT")
            constrs.unit_ref = self.getChildElementOptionalRefType(child_element, "UNIT-REF")
            parent.physConstrs = constrs
                
    def readDataConstrRule(self, element: ET.Element, parent: DataConstr):
        for child_element in element.findall("./xmlns:DATA-CONSTR-RULES/xmlns:DATA-CONSTR-RULE", self.nsmap):
            self.logger.debug("readDataConstrRule")
            rule = DataConstrRule()
            self.readElementAttributes(child_element, rule)
            rule.constrLevel = self.getChildElementOptionalNumericalValue(child_element, "CONSTR-LEVEL")
            self.readInternalConstrs(child_element, rule)
            self.readPhysConstrs(child_element, rule)
            parent.addDataConstrRule(rule)
                
    def readDataConstr(self, element: ET.Element, parent: ARPackage):
        short_name = self.getShortName(element)
        self.logger.debug("readDataConstr %s" % short_name)
        constr = parent.createDataConstr(short_name)
        self.readIdentifiable(element, constr)
        self.readDataConstrRule(element, constr)

    def readUnit(self, element: ET.Element, parent: ARPackage):
        short_name = self.getShortName(element)
        self.logger.debug("readUnit %s" % short_name)
        unit = parent.createUnit(short_name)
        self.readIdentifiable(element, unit)
        unit.setDisplayName(self.getChildElementOptionalLiteral(element, "DISPLAY-NAME")) \
            .setFactorSiToUnit(self.getChildElementOptionalFloatValue(element, "FACTOR-SI-TO-UNIT")) \
            .setOffsetSiToUnit(self.getChildElementOptionalFloatValue(element, "OFFSET-SI-TO-UNIT")) \
            .setPhysicalDimensionRef(self.getChildElementOptionalRefType(element, "PHYSICAL-DIMENSION-REF"))


    def readEndToEndDescriptionDataId(self, element: ET.Element, parent: EndToEndDescription):
        child_element = element.find("./xmlns:DATA-IDS", self.nsmap)
        if child_element is not None:
            for value in self.getChildElementNumericalValueList(child_element, "DATA-ID"):
                parent.addDataId(value)

    def getEndToEndDescription(self, element: ET.Element, key: str) -> EndToEndDescription:
        child_element = element.find("./xmlns:%s" % key, self.nsmap)
        desc = None
        if (child_element is not None):
            desc = EndToEndDescription()
            desc.category = self.getChildElementOptionalLiteral(child_element, "CATEGORY")
            self.readEndToEndDescriptionDataId(child_element, desc)
            desc.dataIdMode = self.getChildElementOptionalNumericalValue(child_element, "DATA-ID-MODE")
            desc.maxDeltaCounterInit = self.getChildElementOptionalNumericalValue(child_element, "MAX-DELTA-COUNTER-INIT")
            desc.crcOffset = self.getChildElementOptionalNumericalValue(child_element, "CRC-OFFSET")
            desc.counterOffset = self.getChildElementOptionalNumericalValue(child_element, "COUNTER-OFFSET")
        return desc
    
    def getVariableDataPrototypeInSystemInstanceRef(self, element: ET.Element) -> VariableDataPrototypeInSystemInstanceRef:
        iref = None
        if element is not None:
            iref = VariableDataPrototypeInSystemInstanceRef()
            #iref.addContextComponentRef() = self.getChildElementOptionalRefType(element, "CONTEXT-COMPONENT-REF")
            iref.setContextCompositionRef(self.getChildElementOptionalRefType(element, "CONTEXT-COMPOSITION-REF")) \
                .setContextPortRef(self.getChildElementOptionalRefType(element, "CONTEXT-PORT-REF")) \
                .setTargetDataPrototypeRef(self.getChildElementOptionalRefType(element, "TARGET-DATA-PROTOTYPE-REF"))
        return iref
    
    def getEndToEndProtectionVariablePrototype(self, element: ET.Element) -> EndToEndProtectionVariablePrototype:
        prototype = EndToEndProtectionVariablePrototype()
        for child_element in element.findall("./xmlns:RECEIVER-IREFS/xmlns:RECEIVER-IREF", self.nsmap):
            prototype.addReceiverIref(self.getVariableDataPrototypeInSystemInstanceRef(child_element))
        child_element = element.find("./xmlns:SENDER-IREF", self.nsmap)
        if child_element is not None:
            prototype.senderIRef = self.getVariableDataPrototypeInSystemInstanceRef(child_element)
        return prototype
    
    def readEndToEndProtectionVariablePrototypes(self, element: ET.Element, parent: EndToEndProtection):
        for child_element in element.findall("./xmlns:END-TO-END-PROTECTION-VARIABLE-PROTOTYPES/*", self.nsmap):
            tag_name = self.getTagName(child_element.tag)
            if tag_name == "END-TO-END-PROTECTION-VARIABLE-PROTOTYPE":
                parent.addEndToEndProtectionVariablePrototype(self.getEndToEndProtectionVariablePrototype(child_element))
            else:
                self._raiseError("Unsupported End To End Protection Variable Prototype <%s>" % tag_name)

    def readEndToEndProtection(self, element: ET.Element, parent: EndToEndProtectionSet):
        short_name = self.getShortName(element)
        self.logger.debug("readEndToEndProtection %s" % short_name)
        protection = parent.createEndToEndProtection(short_name)
        self.readIdentifiable(element, protection)
        protection.endToEndProfile = self.getEndToEndDescription(element, "END-TO-END-PROFILE")
        self.readEndToEndProtectionVariablePrototypes(element, protection)

    def readEndToEndProtections(self, element: ET.Element, parent: EndToEndProtectionSet):
        for child_element in element.findall("./xmlns:END-TO-END-PROTECTIONS/*", self.nsmap):
            tag_name = self.getTagName(child_element.tag)
            if tag_name == "END-TO-END-PROTECTION":
                self.readEndToEndProtection(child_element, parent)

    def readEndToEndProtectionSet(self, element: ET.Element, parent: ARPackage):
        short_name = self.getShortName(element)
        self.logger.debug("readEndToEndProtectionSet %s" % short_name)
        protection_set = parent.createEndToEndProtectionSet(short_name)
        self.readEndToEndProtections(element, protection_set)

    def readAutosarDataType(self, element: ET.Element, data_type: AutosarDataType):
        self.readIdentifiable(element, data_type)
        data_type.swDataDefProps = self.getSwDataDefProps(element, "SW-DATA-DEF-PROPS")

    def readImplementationProps(self, element: ET.Element, props: ImplementationProps):
        props.setSymbol(self.getChildElementOptionalLiteral(element, "SYMBOL"))

    def readSymbolProps(self, element: ET.Element, props: SymbolProps):
        self.readImplementationProps(element, props)

    def readImplementationDataTypeSymbolProps(self, element: ET.Element, data_type: ImplementationDataType):
        child_element = element.find("./xmlns:SYMBOL-PROPS", self.nsmap)
        if child_element is not None:
            short_name = self.getShortName(child_element)
            self.logger.debug("readSymbolProps %s" % short_name)
            props = data_type.createSymbolProps(short_name)
            self.readSymbolProps(child_element, props)

    def readApplicationDataType(self, element: ET.Element, data_type: ApplicationDataType):
        self.readAutosarDataType(element, data_type)

    def readApplicationCompositeDataType(self, element: ET.Element, data_type: ApplicationCompositeDataType):
        self.readApplicationDataType(element, data_type)

    def readDataPrototype(self, element: ET.Element, prototype: DataPrototype):
        self.readIdentifiable(element, prototype)

    def readApplicationCompositeElementDataPrototype(self, element: ET.Element, prototype: ApplicationCompositeElementDataPrototype):
        self.readDataPrototype(element, prototype)
        prototype.typeTRef = self.getChildElementOptionalRefType(element, "TYPE-TREF")

    def readApplicationArrayElement(self, element: ET.Element, parent: ApplicationArrayDataType):
        child_element = element.find("./xmlns:ELEMENT", self.nsmap)
        if child_element is not None:
            short_name = self.getShortName(child_element)
            self.logger.debug("readApplicationArrayElement %s" % short_name)
            array_element = parent.createApplicationArrayElement(short_name)
            self.readApplicationCompositeElementDataPrototype(child_element, array_element)
            array_element.setArraySizeSemantics(self.getChildElementOptionalLiteral(child_element, "ARRAY-SIZE-SEMANTICS"))
            array_element.setMaxNumberOfElements(self.getChildElementOptionalNumericalValue(child_element, "MAX-NUMBER-OF-ELEMENTS"))

    def readApplicationArrayDataType(self, element: ET.Element, parent: ARPackage):
        short_name = self.getShortName(element)
        self.logger.debug("readApplicationArrayDataType %s" % short_name)
        data_type = parent.createApplicationArrayDataType(short_name)
        self.readApplicationCompositeDataType(element, data_type)
        self.readApplicationArrayElement(element, data_type)

    def getSwRecordLayoutV(self, element: ET.Element, key: str) -> SwRecordLayoutV:
        child_element = element.find("./xmlns:%s" % key, self.nsmap)
        layout_v = None
        if child_element is not None:
            layout_v = SwRecordLayoutV()
            layout_v.setShortLabel(self.getChildElementOptionalLiteral(child_element, "SHORT-LABEL")) \
                    .setBaseTypeRef(self.getChildElementOptionalRefType(child_element, "BASE-TYPE-REF")) \
                    .setSwRecordLayoutVAxis(self.getChildElementOptionalNumericalValue(child_element, "SW-RECORD-LAYOUT-V-AXIS")) \
                    .setSwRecordLayoutVProp(self.getChildElementOptionalLiteral(child_element, "SW-RECORD-LAYOUT-V-PROP")) \
                    .setSwRecordLayoutVIndex(self.getChildElementOptionalLiteral(child_element, "SW-RECORD-LAYOUT-V-INDEX"))
        return layout_v

    def getSwRecordLayoutGroup(self, element: ET.Element, key: str) -> SwRecordLayoutGroup:
        child_element = element.find("./xmlns:%s" % key, self.nsmap)
        group = None
        if child_element is not None:
            group = SwRecordLayoutGroup()
            group.setShortLabel(self.getChildElementOptionalLiteral(child_element, "SHORT-LABEL")) \
                 .setCategory(self.getChildElementOptionalLiteral(child_element, "CATEGORY")) \
                 .setSwRecordLayoutGroupAxis(self.getChildElementOptionalNumericalValue(child_element, "SW-RECORD-LAYOUT-GROUP-AXIS")) \
                 .setSwRecordLayoutGroupIndex(self.getChildElementOptionalLiteral(child_element, "SW-RECORD-LAYOUT-GROUP-INDEX")) \
                 .setSwRecordLayoutGroupFrom(self.getChildElementOptionalLiteral(child_element, "SW-RECORD-LAYOUT-GROUP-FROM")) \
                 .setSwRecordLayoutGroupTo(self.getChildElementOptionalLiteral(child_element, "SW-RECORD-LAYOUT-GROUP-TO")) \
            
            group_content = SwRecordLayoutGroupContent()
            group_content.swRecordLayoutGroup = self.getSwRecordLayoutGroup(child_element, "SW-RECORD-LAYOUT-GROUP")
            group_content.swRecordLayoutV = self.getSwRecordLayoutV(child_element, "SW-RECORD-LAYOUT-V")

            if group_content.swRecordLayoutGroup is not None:
                group.setSwRecordLayoutGroupContentType(group_content)
            elif group_content.swRecordLayoutV is not None:
                group.setSwRecordLayoutGroupContentType(group_content)

        return group

    def readSwRecordLayout(self, element: ET.Element, parent: ARPackage):
        short_name = self.getShortName(element)
        self.logger.debug("readSwRecordLayout %s" % short_name)
        layout = parent.createSwRecordLayout(short_name)
        self.readIdentifiable(element, layout)
        layout.setSwRecordLayoutGroup(self.getSwRecordLayoutGroup(element, "SW-RECORD-LAYOUT-GROUP"))

    def readSwAddrMethod(self, element: ET.Element, parent: ARPackage):
        short_name = self.getShortName(element)
        self.logger.debug("readSwAddrMethod %s" % short_name)
        layout = parent.createSwAddrMethod(short_name)

    def readTriggerInterface(self, element: ET.Element, parent: ARPackage):
        short_name = self.getShortName(element)
        self.logger.debug("readTriggerInterface %s" % short_name)
        trigger_if = parent.createTriggerInterface(short_name)

    def readModeDeclarationGroupModeDeclaration(self, element: ET.Element, parent: ModeDeclarationGroup):
        for child_element in element.findall("./xmlns:MODE-DECLARATIONS/xmlns:MODE-DECLARATION", self.nsmap):
            short_name = self.getShortName(child_element)
            declaration = parent.createModeDeclaration(short_name)
            declaration.setValue(self.getChildElementOptionalNumericalValue(child_element, "VALUE"))

    def readModeDeclarationGroup(self, element: ET.Element, parent: ARPackage):
        short_name = self.getShortName(element)
        self.logger.debug("readModeDeclarationGroup %s" % short_name)
        group = parent.createModeDeclarationGroup(short_name)
        self.readIdentifiable(element, group)
        self.readModeDeclarationGroupModeDeclaration(element, group)
        group.setInitialModeRef(self.getChildElementOptionalRefType(element, "INITIAL-MODE-REF"))
        group.setOnTransitionValue(self.getChildElementOptionalNumericalValue(element, "ON-TRANSITION-VALUE"))

    def readModeSwitchInterfaceModeGroup(self, element: ET.Element, parent: ModeSwitchInterface):
        child_element = self.find(element, "MODE-GROUP")
        if child_element is not None:
            short_name = self.getShortName(child_element)
            mode_group = parent.createModeGroup(short_name)
            self.readIdentifiable(child_element, mode_group)
            mode_group.type_tref = self.getChildElementOptionalRefType(child_element, "TYPE-TREF")

    def readModeSwitchInterface(self, element: ET.Element, parent: ARPackage):
        short_name = self.getShortName(element)
        self.logger.debug("readModeSwitchInterface %s" % short_name)
        mode_interface = parent.createModeSwitchInterface(short_name)
        self.readPortInterface(element, mode_interface)
        self.readModeSwitchInterfaceModeGroup(element, mode_interface)

    def readEOCExecutableEntityRef(self, element: ET.Element, constraint: ExecutionOrderConstraint):
        short_name = self.getShortName(element)
        self.logger.debug("readEocExecutableEntityRef %s" % short_name)
        entity_ref = constraint.createEOCExecutableEntityRef(short_name)
        self.readIdentifiable(element, entity_ref)
        for ref in self.getChildElementRefTypeList(element, "SUCCESSOR-REFS/SUCCESSOR-REF"):
            entity_ref.addSuccessorRef(ref)

    def readExecutionOrderConstraintOrderedElement(self, element: ET.Element, constrain: ExecutionOrderConstraint):
        for child_element in self.findall(element, "ORDERED-ELEMENTS/*"):
            tag_name = self.getTagName(child_element)
            if tag_name == "EOC-EXECUTABLE-ENTITY-REF":
                self.readEOCExecutableEntityRef(child_element, constrain)
            else:
                self._raiseError("Unsupported order element <%s>." % tag_name)

    def readExecutionOrderConstraint(self, element: ET.Element, extension: TimingExtension):
        short_name = self.getShortName(element)
        self.logger.debug("readExecutionOrderConstraint %s" % short_name)
        constraint = extension.createExecutionOrderConstraint(short_name)
        self.readIdentifiable(element, constraint)
        self.readExecutionOrderConstraintOrderedElement(element, constraint)

    def readTimingExtension(self, element: ET.Element, extension: TimingExtension):
        for child_element in self.findall(element, "TIMING-REQUIREMENTS/*"):
            tag_name = self.getTagName(child_element)
            if tag_name == "EXECUTION-ORDER-CONSTRAINT":
                self.readExecutionOrderConstraint(child_element, extension)
            else:
                self._raiseError("Unsupported timing requirement <%s>" % tag_name)

    def readSwcTiming(self, element: ET.Element, parent: ARPackage):
        short_name = self.getShortName(element)
        self.logger.debug("readSwcTiming %s" % short_name)
        timing = parent.createSwcTiming(short_name)
        self.readIdentifiable(element, timing)
        self.readTimingExtension(element, timing)

    def readFrameTriggering(self, element: ET.Element, triggering: FrameTriggering):
        for ref in self.getChildElementRefTypeList(element, 'FRAME-PORT-REFS/FRAME-PORT-REF'):
            triggering.addFramePortRef(ref)
        triggering.setFrameRef(self.getChildElementOptionalRefType(element, "FRAME-REF"))
        for child_element in self.findall(element, 'PDU-TRIGGERINGS/PDU-TRIGGERING-REF-CONDITIONAL'):
            triggering.addPduTriggeringRef(self.getChildElementOptionalRefType(child_element, "PDU-TRIGGERING-REF"))

    def readCanFrameTriggering(self, element: ET.Element, triggering: CanFrameTriggering):
        self.logger.debug("Read CanFrameTriggering %s" % triggering.getShortName())
        self.readIdentifiable(element, triggering)
        self.readFrameTriggering(element, triggering)
        triggering.setCanAddressingMode(self.getChildElementOptionalLiteral(element, "CAN-ADDRESSING-MODE")) \
                  .setCanFdFrameSupport(self.getChildElementOptionalBooleanValue(element, "CAN-FD-FRAME-SUPPORT")) \
                  .setCanFrameRxBehavior(self.getChildElementOptionalLiteral(element, "CAN-FRAME-RX-BEHAVIOR")) \
                  .setCanFrameTxBehavior(self.getChildElementOptionalLiteral(element, "CAN-FRAME-TX-BEHAVIOR")) \
                  .setIdentifier(self.getChildElementOptionalNumericalValue(element, "IDENTIFIER")) \
                  .setRxIdentifierRange(self.getChildElementRxIdentifierRange(element, "RX-IDENTIFIER-RANGE"))


    def readLinFrameTriggering(self, element: ET.Element, triggering: LinFrameTriggering):
        self.logger.debug("Read LinFrameTriggering %s" % triggering.getShortName())
        self.readIdentifiable(element, triggering)
        self.readFrameTriggering(element, triggering)
        triggering.setIdentifier(self.getChildElementOptionalNumericalValue(element, "IDENTIFIER")) \
                  .setLinChecksum(self.getChildElementOptionalLiteral(element, "LIN-CHECKSUM"))

    def readISignalTriggering(self, element: ET.Element, triggering: ISignalTriggering):
        self.logger.debug("Read ISignalTriggering %s" % triggering.getShortName())
        self.readIdentifiable(element, triggering)
        triggering.setISignalGroupRef(self.getChildElementOptionalRefType(element, "I-SIGNAL-GROUP-REF"))
        for ref in self.getChildElementRefTypeList(element, 'I-SIGNAL-PORT-REFS/I-SIGNAL-PORT-REF'):
            triggering.addISignalPortRef(ref)
        triggering.setISignalRef(self.getChildElementOptionalRefType(element, "I-SIGNAL-REF"))

    def readPduTriggering(self, element: ET.Element, triggering: PduTriggering):
        self.logger.debug("Read PduTriggering %s" % triggering.getShortName())
        self.readIdentifiable(element, triggering)
        for ref in self.getChildElementRefTypeList(element, 'I-PDU-PORT-REFS/I-PDU-PORT-REF'):
            triggering.addIPduPortRef(ref)
        triggering.setIPduRef(self.getChildElementOptionalRefType(element, "I-PDU-REF"))
        for child_element in self.findall(element, 'I-SIGNAL-TRIGGERINGS/I-SIGNAL-TRIGGERING-REF-CONDITIONAL'):
            triggering.addISignalTriggeringRef(self.getChildElementOptionalRefType(child_element, "I-SIGNAL-TRIGGERING-REF"))

    def readPhysicalChannel(self, element: ET.Element, channel: PhysicalChannel):
        for child_element in self.findall(element, 'COMM-CONNECTORS/COMMUNICATION-CONNECTOR-REF-CONDITIONAL'):
            channel.addCommConnectorRef(self.getChildElementOptionalRefType(child_element, "COMMUNICATION-CONNECTOR-REF"))
        
        for child_element in self.findall(element, "FRAME-TRIGGERINGS/*"):
            tag_name = self.getTagName(child_element)
            if tag_name == "CAN-FRAME-TRIGGERING":
                triggering = channel.createCanFrameTriggering(self.getShortName(child_element))
                self.readCanFrameTriggering(child_element, triggering)
            elif tag_name == "LIN-FRAME-TRIGGERING":
                triggering = channel.createLinFrameTriggering(self.getShortName(child_element))
                self.readLinFrameTriggering(child_element, triggering)
            else:
                raise NotImplementedError("Unsupported Frame Triggering <%s>" % tag_name)
            
        for child_element in self.findall(element, "I-SIGNAL-TRIGGERINGS/*"):
            tag_name = self.getTagName(child_element)
            if tag_name == "I-SIGNAL-TRIGGERING":
                triggering = channel.createISignalTriggering(self.getShortName(child_element))
                self.readISignalTriggering(child_element, triggering)
            else:
                raise NotImplementedError("Unsupported Frame Triggering <%s>" % tag_name)
            
        for child_element in self.findall(element, "PDU-TRIGGERINGS/*"):
            tag_name = self.getTagName(child_element)
            if tag_name == "PDU-TRIGGERING":
                triggering = channel.createPduTriggering(self.getShortName(child_element))
                self.readPduTriggering(child_element, triggering)
            else:
                raise NotImplementedError("Unsupported Frame Triggering <%s>" % tag_name)

    def readCanPhysicalChannel(self, element: ET.Element, channel: CanPhysicalChannel):
        self.readIdentifiable(element, channel)
        self.readPhysicalChannel(element, channel)

    def readLinPhysicalChannel(self, element: ET.Element, channel: LinPhysicalChannel):
        self.readIdentifiable(element, channel)
        self.readPhysicalChannel(element, channel)

    def readCommunicationClusterPhysicalChannels(self, element: ET.Element, cluster: CommunicationCluster):
        for child_element in self.findall(element, "PHYSICAL-CHANNELS/*"):
            tag_name = self.getTagName(child_element)
            if tag_name == "CAN-PHYSICAL-CHANNEL":
                channel = cluster.createCanPhysicalChannel(self.getShortName(child_element))
                self.readCanPhysicalChannel(child_element, channel)
            elif tag_name == "LIN-PHYSICAL-CHANNEL":
                channel = cluster.createLinPhysicalChannel(self.getShortName(child_element))
                self.readLinPhysicalChannel(child_element, channel)
            else:
                raise NotImplementedError("Unsupported Physical Channel <%s>" % tag_name)


    def readCommunicationCluster(self, element: ET.Element, cluster: CommunicationCluster):
        cluster.setBaudrate(self.getChildElementOptionalNumericalValue(element, "BAUDRATE")) 
        self.readCommunicationClusterPhysicalChannels(element, cluster)
        cluster.setProtocolName(self.getChildElementOptionalLiteral(element, "PROTOCOL-NAME")) \
               .setProtocolVersion(self.getChildElementOptionalLiteral(element, "PROTOCOL-VERSION"))

    def readAbstractCanCluster(self, element: ET.Element, cluster: AbstractCanCluster):
        cluster.setCanFdBaudrate(self.getChildElementOptionalNumericalValue(element, "CAN-FD-BAUDRATE")) 

    def readLinCluster(self, element: ET.Element, parent: ARPackage):
        short_name = self.getShortName(element)
        self.logger.debug("readLinCluster %s" % short_name)
        cluster = parent.createLinCluster(short_name)
        self.readIdentifiable(element, cluster)
        child_element = self.find(element, "LIN-CLUSTER-VARIANTS/LIN-CLUSTER-CONDITIONAL")
        if child_element is not None:
            self.readCommunicationCluster(child_element, cluster)

    def readCanCluster(self, element: ET.Element, parent: ARPackage):
        short_name = self.getShortName(element)
        self.logger.debug("readCanCluster %s" % short_name)
        cluster = parent.createCanCluster(short_name)
        self.readIdentifiable(element, cluster)
        child_element = self.find(element, "CAN-CLUSTER-VARIANTS/CAN-CLUSTER-CONDITIONAL")
        if child_element is not None:
            self.readCommunicationCluster(child_element, cluster)
            self.readAbstractCanCluster(child_element, cluster)

    def readPduToFrameMappings(self, element: ET.Element, parent: Frame):
        for child_element in self.findall(element, "PDU-TO-FRAME-MAPPINGS/PDU-TO-FRAME-MAPPING"):
            short_name = self.getShortName(child_element)
            self.logger.debug("readPduToFrameMapping %s" % short_name)
            mapping = parent.createPduToFrameMapping(short_name)
            self.readIdentifiable(child_element, mapping)
            mapping.packingByteOrder = self.getChildElementOptionalLiteral(child_element, "PACKING-BYTE-ORDER")
            mapping.pduRef = self.getChildElementOptionalRefType(child_element, "PDU-REF")
            mapping.startPosition = self.getChildElementOptionalNumericalValue(child_element, "START-POSITION")

    def readFrame(self, element: ET.Element, frame: Frame):
        self.readIdentifiable(element, frame)
        frame.frameLength = self.getChildElementOptionalNumericalValue(element, "FRAME-LENGTH")
        self.readPduToFrameMappings(element, frame)

    def readLinUnconditionalFrame(self, element: ET.Element, parent: ARPackage):
        short_name = self.getShortName(element)
        self.logger.debug("LinUnconditionalFrame %s" % short_name)
        frame = parent.createLinUnconditionalFrame(short_name)
        self.readFrame(element, frame)

    def readNmPdu(self, element: ET.Element, parent: ARPackage):
        short_name = self.getShortName(element)
        self.logger.debug("readNmPdu %s" % short_name)
        pdu = parent.createNmPdu(short_name)
        self.readIdentifiable(element, pdu)
        self.readIPdu(element, pdu)

    def readNPdu(self, element: ET.Element, parent: ARPackage):
        short_name = self.getShortName(element)
        self.logger.debug("readNPdu %s" % short_name)
        pdu = parent.createNPdu(short_name)
        self.readIdentifiable(element, pdu)
        self.readIPdu(element, pdu)

    def readIPdu(self, element: ET.Element, pdu: IPdu):
        pdu.setLength(self.getChildElementOptionalNumericalValue(element, "LENGTH"))
        
    def readDcmIPdu(self, element: ET.Element, parent: ARPackage):
        short_name = self.getShortName(element)
        self.logger.debug("readDcmIPdu %s" % short_name)
        pdu = parent.createDcmIPdu(short_name)
        self.readIdentifiable(element, pdu)
        self.readIPdu(element, pdu)
        pdu.setDiagPduType(self.getChildElementOptionalLiteral(element, "DIAG-PDU-TYPE"))

    def readSecuredIPdu(self, element: ET.Element, parent: ARPackage):
        short_name = self.getShortName(element)
        self.logger.debug("readSecuredIPdu %s" % short_name)
        pdu = parent.createSecuredIPdu(short_name)
        self.readIdentifiable(element, pdu)
        self.readIPdu(element, pdu)

    def readNmNode(self, element: ET.Element, nm_node: NmNode):
        nm_node.setControllerRef(self.getChildElementOptionalRefType(element, "CONTROLLER-REF")) \
            .setNmIfEcuRef(self.getChildElementOptionalRefType(element, "NM-IF-ECU-REF")) \
            .setNmNodeId(self.getChildElementOptionalNumericalValue(element, "NM-NODE-ID"))
        for ref in self.getChildElementRefTypeList(element, "RX-NM-PDU-REFS/RX-NM-PDU-REF"):
            nm_node.addRxNmPduRef(ref)
        for ref in self.getChildElementRefTypeList(element, "TX-NM-PDU-REFS/TX-NM-PDU-REF"):
            nm_node.addTxNmPduRefs(ref)

    def readCanNmNode(self, element: ET.Element, parent: NmCluster):
        short_name = self.getShortName(element)
        self.logger.debug("readCanNmNode %s" % short_name)
        nm_node = parent.createCanNmNode(short_name)            # type: CanNmNode
        self.readIdentifiable(element, nm_node)
        self.readNmNode(element, nm_node)

        nm_node.setNmMsgCycleOffset(self.getChildElementOptionalFloatValue(element, "NM-MSG-CYCLE-OFFSET")) \
               .setNmMsgReducedTime(self.getChildElementOptionalFloatValue(element, "NM-MSG-REDUCED-TIME")) \
               .setNmRangeConfig(self.getChildElementRxIdentifierRange(element, "NM-RANGE-CONFIG"))

    def readNmClusterNmNodes(self, element: ET.Element, parent: NmCluster):
        self.logger.debug("readNmConfigNmNodes %s" % parent.getShortName())
        for child_element in self.findall(element, "NM-NODES/*"):
            tag_name = self.getTagName(child_element)
            if tag_name == "CAN-NM-NODE":
                self.readCanNmNode(child_element, parent)
            else:
                self._raiseError("Unsupported Nm Node <%s>" % tag_name)

    def getCanNmClusterCoupling(self, element: ET.Element) -> CanNmClusterCoupling:
        coupling  = CanNmClusterCoupling()
        
        for ref in self.getChildElementRefTypeList(element, "COUPLED-CLUSTER-REFS/COUPLED-CLUSTER-REF"):
            coupling.addCoupledClusterRef(ref)

        coupling.setNmBusloadReductionEnabled(self.getChildElementOptionalBooleanValue(element, "NM-BUSLOAD-REDUCTION-ENABLED")) \
                .setNmImmediateRestartEnabled(self.getChildElementOptionalBooleanValue(element, "NM-IMMEDIATE-RESTART-ENABLED"))
    
        return coupling

    def readNmConfigNmClusterCouplings(self, element: ET.Element, nm_config: NmConfig):
        self.logger.debug("readNmClusterNmClusterCouplings %s" % nm_config.getShortName())
        for child_element in self.findall(element, "NM-CLUSTER-COUPLINGS/*"):
            tag_name = self.getTagName(child_element)
            if tag_name == "CAN-NM-CLUSTER-COUPLING":
                nm_config.addNmClusterCouplings(self.getCanNmClusterCoupling(child_element))
            else:
                self._raiseError("Unsupported Nm Node <%s>" % tag_name)

    def readNmCluster(self, element: ET.Element, cluster: NmCluster):
        cluster.setCommunicationClusterRef(self.getChildElementOptionalRefType(element, "COMMUNICATION-CLUSTER-REF")) \
               .setNmChannelId(self.getChildElementOptionalNumericalValue(element, "NM-CHANNEL-ID")) \
               .setNmChannelSleepMaster(self.getChildElementOptionalBooleanValue(element, "NM-CHANNEL-SLEEP-MASTER"))
        self.readNmClusterNmNodes(element, cluster)
        cluster.setNmSynchronizingNetwork(self.getChildElementOptionalBooleanValue(element, "NM-SYNCHRONIZING-NETWORK"))

    def readCanNmCluster(self, element: ET.Element, parent: NmConfig):
        short_name = self.getShortName(element)
        self.logger.debug("readCanNmCluster %s" % short_name)
        cluster = parent.createCanNmCluster(short_name)         # type: CanNmCluster
        self.readIdentifiable(element, cluster)
        self.readNmCluster(element, cluster)

        cluster.setNmBusloadReductionActive(self.getChildElementOptionalBooleanValue(element, "NM-BUSLOAD-REDUCTION-ACTIVE")) \
               .setNmCarWakeUpRxEnabled(self.getChildElementOptionalBooleanValue(element, "NM-CAR-WAKE-UP-RX-ENABLED")) \
               .setNmCbvPosition(self.getChildElementOptionalNumericalValue(element, "NM-CBV-POSITION")) \
               .setNmChannelActive(self.getChildElementOptionalBooleanValue(element, "NM-CHANNEL-ACTIVE")) \
               .setNmImmediateNmCycleTime(self.getChildElementOptionalFloatValue(element, "NM-IMMEDIATE-NM-CYCLE-TIME")) \
               .setNmImmediateNmTransmissions(self. getChildElementOptionalNumericalValue(element, "NM-IMMEDIATE-NM-TRANSMISSIONS")) \
               .setNmMessageTimeoutTime(self.getChildElementOptionalFloatValue(element, "NM-MESSAGE-TIMEOUT-TIME")) \
               .setNmMsgCycleTime(self.getChildElementOptionalFloatValue(element, "NM-MSG-CYCLE-TIME")) \
               .setNmNetworkTimeout(self.getChildElementOptionalFloatValue(element, "NM-NETWORK-TIMEOUT")) \
               .setNmNidPosition(self. getChildElementOptionalNumericalValue(element, "NM-NID-POSITION")) \
               .setNmRemoteSleepIndicationTime(self.getChildElementOptionalFloatValue(element, "NM-REMOTE-SLEEP-INDICATION-TIME")) \
               .setNmRepeatMessageTime(self.getChildElementOptionalFloatValue(element, "NM-REPEAT-MESSAGE-TIME")) \
               .setNmUserDataLength(self. getChildElementOptionalNumericalValue(element, "NM-USER-DATA-LENGTH")) \
               .setNmWaitBusSleepTime(self.getChildElementOptionalFloatValue(element, "NM-WAIT-BUS-SLEEP-TIME"))
        
    def readNmConfigNmClusters(self, element: ET.Element, parent: NmConfig):
        for child_element in self.findall(element, "NM-CLUSTERS/*"):
            tag_name = self.getTagName(child_element)
            if tag_name == "CAN-NM-CLUSTER":
                self.readCanNmCluster(child_element, parent)
            else:
                self._raiseError("Unsupported Nm Cluster <%s>" % tag_name)
    
    def readNmConfig(self, element: ET.Element, parent: ARPackage):
        short_name = self.getShortName(element)
        self.logger.debug("NmConfig %s" % short_name)
        config = parent.createNmConfig(short_name)                  # type: NmConfig
        self.readIdentifiable(element, config)
        self.readNmConfigNmClusters(element, config)
        self.readNmConfigNmClusterCouplings(element, config)

    def readCanTpConfig(self, element: ET.Element, parent: ARPackage):
        short_name = self.getShortName(element)
        self.logger.debug("CanTpConfig %s" % short_name)
        pdu = parent.createCanTpConfig(short_name)
        self.readIdentifiable(element, pdu)

    def readCanFrame(self, element: ET.Element, parent: ARPackage):
        short_name = self.getShortName(element)
        self.logger.debug("CanFrame %s" % short_name)
        frame = parent.createCanFrame(short_name)
        self.readFrame(element, frame)

    def readEcuInstance(self, element: ET.Element, parent: ARPackage):
        short_name = self.getShortName(element)
        self.logger.debug("EcuInstance %s" % short_name)
        instance = parent.createEcuInstance(short_name)
        self.readIdentifiable(element, instance)

    '''
    def getFrameMappings(self, element: ET.Element) -> List[FrameMapping]:
        mappings = []
        for child_element in self.findall(element, 'FRAME-MAPPINGS/'):
            mapping = FrameMapping()
            mapping.sourceFrameRef = self.getChildElementOptionalRefType(child_element, "SOURCE-FRAME-REF")
            mapping.targetFrameRef = self.getChildElementOptionalRefType(child_element, "TARGET-FRAME-REF")
            mappings.append(mapping)
        return mappings
    '''

    def getISignalMappings(self, element: ET.Element) -> List[ISignalMapping]:
        mappings = []
        for child_element in self.findall(element, "SIGNAL-MAPPINGS/I-SIGNAL-MAPPING"):
            mapping = ISignalMapping()
            mapping.sourceSignalRef = self.getChildElementOptionalRefType(child_element, "SOURCE-SIGNAL-REF")
            mapping.targetSignalRef = self.getChildElementOptionalRefType(child_element, "TARGET-SIGNAL-REF")
            mappings.append(mapping)
        return mappings
    
    '''
    def getIPduMappings(self, element: ET.Element) -> List[IPduMapping]:
        mappings = []
        for child_element in self.findall(element, tag_name):
            mapping = IPduMapping()
            mapping.sourceIPduRef = self.getChildElementOptionalRefType(child_element, "SOURCE-IPDU-REF")
            mapping.targetIPduRef = self.getChildElementOptionalRefType(child_element, "TARGET-IPDU-REF")
            mappings.append(mapping)
        return mappings
    '''

    def readGateway(self, element: ET.Element, parent: ARPackage):
        short_name = self.getShortName(element)
        self.logger.debug("Gateway %s" % short_name)
        gateway = parent.createGateway(short_name)
        self.readIdentifiable(element, gateway)
        gateway.ecuRef = self.getChildElementOptionalRefType(element, "ECU-REF")
        for mapping in self.getISignalMappings(element):
            gateway.addSignalMapping(mapping)

    def readISignal(self, element: ET.Element, parent: ARPackage):
        short_name = self.getShortName(element)
        self.logger.debug("ISignal %s" % short_name)
        signal = parent.createISignal(short_name)
        self.readIdentifiable(element, signal)
        signal.dataTypePolicy = self.getChildElementOptionalLiteral(element, "DATA-TYPE-POLICY")
        signal.initValue = self.getInitValue(element)
        signal.length = self.getChildElementOptionalNumericalValue(element, "LENGTH")
        signal.networkRepresentationProps = self.getSwDataDefProps(element, "NETWORK-REPRESENTATION-PROPS")
        signal.systemSignalRef = self.getChildElementOptionalRefType(element, "SYSTEM-SIGNAL-REF")

    def readEcucValueCollectionEcucValues(self, element: ET.Element, parent: EcucValueCollection):
        for child_element in self.findall(element, "ECUC-VALUES/ECUC-MODULE-CONFIGURATION-VALUES-REF-CONDITIONAL"):
            ref = self.getChildElementOptionalRefType(child_element, "ECUC-MODULE-CONFIGURATION-VALUES-REF") 
            if (ref is not None):
                parent.addEcucValueRef(ref)
            self.logger.debug("EcucValue <%s> of EcucValueCollection <%s> has been added", ref.value, parent.getShortName())

    def readEcucValueCollection(self, element: ET.Element, parent: ARPackage):
        short_name = self.getShortName(element)
        self.logger.debug("EcucValueCollection %s" % short_name)
        collection = parent.createEcucValueCollection(short_name)
        self.readIdentifiable(element, collection)
        collection.setEcuExtractRef(self.getChildElementOptionalRefType(element, "ECU-EXTRACT-REF"))
        self.readEcucValueCollectionEcucValues(element, collection)

    def readEcucParameterValue(self, element: ET.Element, param_value: EcucParameterValue):
        param_value.setDefinitionRef(self.getChildElementOptionalRefType(element, "DEFINITION-REF"))
        for annotation in self.getAnnotations(element):
            param_value.addAnnotation(annotation)

    def getEcucTextualParamValue(self, element: ET.Element) -> EcucTextualParamValue:
        param_value = EcucTextualParamValue()
        self.readEcucParameterValue(element, param_value)
        param_value.setValue(self.getChildElementOptionalLiteral(element, "VALUE"))
        return param_value

    def getEcucNumericalParamValue(self, element: ET.Element) -> EcucNumericalParamValue:
        param_value = EcucNumericalParamValue()
        self.readEcucParameterValue(element, param_value)
        param_value.setValue(self.getChildElementOptionalNumericalValue(element, "VALUE"))
        return param_value

    def readEcucContainerValueParameterValues(self, element: ET.Element, container_value: EcucContainerValue):
        for child_element in self.findall(element, "PARAMETER-VALUES/*"):
            tag_name = self.getTagName(child_element)
            if tag_name == "ECUC-TEXTUAL-PARAM-VALUE":
                container_value.addParameterValue(self.getEcucTextualParamValue(child_element))
            elif tag_name == "ECUC-NUMERICAL-PARAM-VALUE":
                container_value.addParameterValue(self.getEcucNumericalParamValue(child_element))
            else:
                raise NotImplementedError("Unsupported EcucParameterValue <%s>" % tag_name)
            
    def readEcucAbstractReferenceValue(self, element: ET.Element, value: EcucAbstractReferenceValue):
        value.setDefinitionRef(self.getChildElementOptionalRefType(element, "DEFINITION-REF"))
        for annotation in self.getAnnotations(element):
            value.addAnnotation(annotation)

    def getEcucReferenceValue(self, element: ET.Element) -> EcucReferenceValue:
        value = EcucReferenceValue()
        self.readEcucAbstractReferenceValue(element, value)
        value.setValueRef(self.getChildElementOptionalRefType(element, "VALUE-REF"))
        return value
    
    def getAnyInstanceRef(self, element: ET.Element, key) -> AnyInstanceRef:
        instance_ref = None
        child_element = self.find(element, key)
        if child_element is not None:
            instance_ref = AnyInstanceRef()
            instance_ref.setBaseRef(self.getChildElementOptionalRefType(child_element, "BASE-REF")) \
                        .setContextElementRef(self.getChildElementOptionalRefType(child_element, "CONTEXT-ELEMENT-REF")) \
                        .setTargetRef(self.getChildElementOptionalRefType(child_element, "TARGET-REF"))
        return instance_ref
    
    def getEcucInstanceReferenceValue(self, element: ET.Element) -> EcucInstanceReferenceValue:
        value = EcucInstanceReferenceValue()
        self.readEcucAbstractReferenceValue(element, value)
        value.setValueIRef(self.getAnyInstanceRef(element, "VALUE-IREF"))
        return value
            
    def readEcucContainerValueReferenceValues(self, element: ET.Element, container_value: EcucContainerValue):
        for child_element in self.findall(element, "REFERENCE-VALUES/*"):
            tag_name = self.getTagName(child_element)
            if tag_name == "ECUC-REFERENCE-VALUE":
                container_value.addReferenceValue(self.getEcucReferenceValue(child_element))
            elif tag_name == "ECUC-INSTANCE-REFERENCE-VALUE":
                container_value.addReferenceValue(self.getEcucInstanceReferenceValue(child_element))
            else:
                raise NotImplementedError("Unsupported EcucParameterValue <%s>" % tag_name)

    def readEcucContainerValue(self, element: ET.Element, container_value: EcucContainerValue):
        self.readIdentifiable(element, container_value)
        container_value.setDefinitionRef(self.getChildElementOptionalRefType(element, "DEFINITION-REF"))
        self.readEcucContainerValueParameterValues(element, container_value)
        self.readEcucContainerValueReferenceValues(element, container_value)
        self.readEcucContainerValueSubContainers(element, container_value)

    def readEcucContainerValueEcucContainerValue(self, element: ET.Element, parent: EcucContainerValue):
        short_name = self.getShortName(element)
        self.logger.debug("EcucContainerValue %s" % short_name)
        container_value = parent.createSubContainer(short_name)
        self.readEcucContainerValue(element, container_value)

    def readEcucContainerValueSubContainers(self, element: ET.Element, parent: EcucContainerValue):
        for child_element in self.findall(element, "SUB-CONTAINERS/*"):
            tag_name = self.getTagName(child_element)
            if tag_name == "ECUC-CONTAINER-VALUE":
                self.readEcucContainerValueEcucContainerValue(child_element, parent)
            else:
                raise NotImplementedError("Unsupported Sub Container %s" % tag_name) 

    def readEcucModuleConfigurationValuesEcucContainerValue(self, element: ET.Element, parent: EcucModuleConfigurationValues):
        short_name = self.getShortName(element)
        self.logger.debug("EcucContainerValue %s" % short_name)
        container_value = parent.createContainer(short_name)
        self.readEcucContainerValue(element, container_value)

    def readEcucModuleConfigurationValuesContainers(self, element: ET.Element, values: EcucModuleConfigurationValues):
        for child_element in self.findall(element, "CONTAINERS/*"):
            tag_name = self.getTagName(child_element)
            if tag_name == "ECUC-CONTAINER-VALUE":
                self.readEcucModuleConfigurationValuesEcucContainerValue(child_element, values)
            else:
                raise NotImplementedError("Unsupported Container %s" % tag_name) 

    def readEcucModuleConfigurationValues(self, element: ET.Element, parent: ARPackage):
        short_name = self.getShortName(element)
        self.logger.debug("EcucModuleConfigurationValues %s" % short_name)
        values = parent.createEcucModuleConfigurationValues(short_name)
        self.readIdentifiable(element, values)
        values.setDefinitionRef(self.getChildElementOptionalRefType(element, "DEFINITION-REF"))
        values.setImplementationConfigVariant(self.getChildElementOptionalLiteral(element, "IMPLEMENTATION-CONFIG-VARIANT"))
        values.setModuleDescriptionRef(self.getChildElementOptionalRefType(element, "MODULE-DESCRIPTION-REF"))
        self.readEcucModuleConfigurationValuesContainers(element, values)

    def readPhysicalDimensions(self, element: ET.Element, parent: ARPackage):
        short_name = self.getShortName(element)
        self.logger.debug("readPhysicalDimensions %s" % short_name)
        dimension = parent.createPhysicalDimension(short_name)
        self.readIdentifiable(element, dimension)
        dimension.setCurrentExp(self.getChildElementOptionalNumericalValue(element, "CURRENT-EXP")) \
                 .setLengthExp(self.getChildElementOptionalNumericalValue(element, "LENGTH-EXP")) \

    '''
    def getIPduMappings(self, element: ET.Element) -> List[IPduMapping]:
        mappings = []
        for child_element in self.findall(element, tag_name):
            mapping = IPduMapping()
            mapping.sourceIPduRef = self.getChildElementOptionalRefType(child_element, "SOURCE-IPDU-REF")
            mapping.targetIPduRef = self.getChildElementOptionalRefType(child_element, "TARGET-IPDU-REF")
            mappings.append(mapping)
        return mappings
    '''

    def readISignalGroup(self, element: ET.Element, parent: ARPackage):
        short_name = self.getShortName(element)
        self.logger.debug("ISignalGroup %s" % short_name)
        group = parent.createISignalGroup(short_name)
        self.readIdentifiable(element, group)
        for ref_type in self.getChildElementRefTypeList(element, "I-SIGNAL-REFS/I-SIGNAL-REF"):
            group.addISignalRef(ref_type)
        group.systemSignalGroupRef = self.getChildElementOptionalRefType(element, "SYSTEM-SIGNAL-GROUP-REF")

    def readSystemSignal(self, element: ET.Element, parent: ARPackage):
        short_name = self.getShortName(element)
        self.logger.debug("SystemSignal %s" % short_name)
        signal = parent.createSystemSignal(short_name)
        self.readIdentifiable(element, signal)
        signal.setDynamicLength(self.getChildElementOptionalBooleanValue(element, "DYNAMIC-LENGTH"))

    def readSystemSignalGroup(self, element: ET.Element, parent: ARPackage):
        short_name = self.getShortName(element)
        self.logger.debug("SystemSignalGroup %s" % short_name)
        group = parent.createSystemSignalGroup(short_name)
        self.readIdentifiable(element, group)
        for ref_type in self.getChildElementRefTypeList(element, "SYSTEM-SIGNAL-REFS/SYSTEM-SIGNAL-REF"):
            group.addSystemSignalRefs(ref_type)

    def readISignalToPduMappings(self, element: ET.Element, parent: ISignalIPdu):
        for child_element in self.findall(element, "I-SIGNAL-TO-PDU-MAPPINGS/I-SIGNAL-TO-I-PDU-MAPPING"):
            short_name = self.getShortName(child_element)
            mapping = parent.createISignalToPduMappings(short_name)
            self.readIdentifiable(child_element, mapping)
            mapping.setISignalRef(self.getChildElementOptionalRefType(child_element, "I-SIGNAL-REF")) \
                   .setISignalGroupRef(self.getChildElementOptionalRefType(child_element, "I-SIGNAL-GROUP-REF")) \
                   .setPackingByteOrder(self.getChildElementOptionalLiteral(child_element, "PACKING-BYTE-ORDER")) \
                   .setStartPosition(self.getChildElementOptionalNumericalValue(child_element, "START-POSITION")) \
                   .setTransferProperty(self.getChildElementOptionalLiteral(child_element, "TRANSFER-PROPERTY")) \
                   .setUpdateIndicationBitPosition(self.getChildElementOptionalNumericalValue(child_element, "UPDATE-INDICATION-BIT-POSITION"))

    def readISignalIPdu(self, element: ET.Element, parent: ARPackage):
        short_name = self.getShortName(element)
        self.logger.debug("ISignalIPdu %s" % short_name)
        i_pdu = parent.createISignalIPdu(short_name)
        self.readIdentifiable(element, i_pdu)
        i_pdu.setLength(self.getChildElementOptionalNumericalValue(element, "LENGTH"))
        self.readISignalToPduMappings(element, i_pdu)
        i_pdu.setUnusedBitPattern(self.getChildElementOptionalLiteral(element, "UNUSED-BIT-PATTERN"))

    def getISignalIPduRefs(self, element: ET.Element) -> List[RefType]:
        ref_types = [] 
        for child_element in self.findall(element, "I-SIGNAL-I-PDUS/I-SIGNAL-I-PDU-REF-CONDITIONAL"):
            ref_types.append(self.getChildElementOptionalRefType(child_element, "I-SIGNAL-I-PDU-REF"))
        return ref_types

    def readISignalIPduGroup(self, element: ET.Element, parent: ARPackage):
        short_name = self.getShortName(element)
        self.logger.debug("ISignalIPduGroup %s" % short_name)
        group = parent.createISignalIPduGroup(short_name)
        self.readIdentifiable(element, group)
        group.communicationDirection = self.getChildElementOptionalLiteral(element, "COMMUNICATION-DIRECTION")
        group.communicationMode = self.getChildElementOptionalLiteral(element, "COMMUNICATION-MODE")
        for ref_type in self.getChildElementRefTypeList(element, "CONTAINED-I-SIGNAL-I-PDU-GROUP-REFS/CONTAINED-I-SIGNAL-I-PDU-GROUP-REF"):
            group.addContainedISignalIPduGroupRef(ref_type)
        for ref_type in self.getISignalIPduRefs(element):
            group.addISignalIPduRef(ref_type)

    def getSenderReceiverToSignalMapping(self, element: ET.Element) -> SenderReceiverToSignalMapping:
        mapping = SenderReceiverToSignalMapping()
        mapping.setDataElementIRef(self.getVariableDataPrototypeInSystemInstanceRef(self.find(element, "DATA-ELEMENT-IREF")))
        mapping.setSystemSignalRef(self.getChildElementOptionalRefType(element, "SYSTEM-SIGNAL-REF"))
        return mapping
    
    def getSenderReceiverToSignalGroupMapping(self, element: ET.Element) -> SenderReceiverToSignalGroupMapping:
        mapping = SenderReceiverToSignalGroupMapping()
        mapping.setDataElementIRef(self.getVariableDataPrototypeInSystemInstanceRef(self.find(element, "DATA-ELEMENT-IREF")))
        mapping.setSignalGroupRef(self.getChildElementOptionalRefType(element, "SIGNAL-GROUP-REF"))
        return mapping
    
    def readSystemMappingDataMappings(self, element: ET.Element, mapping: SystemMapping):
        for child_element in self.findall(element, "DATA-MAPPINGS/*"):
            tag_name = self.getTagName(child_element)
            if tag_name == "SENDER-RECEIVER-TO-SIGNAL-MAPPING":
                mapping.addDataMapping(self.getSenderReceiverToSignalMapping(child_element))
            elif tag_name == "SENDER-RECEIVER-TO-SIGNAL-GROUP-MAPPING":
                mapping.addDataMapping(self.getSenderReceiverToSignalGroupMapping(child_element))
            else:
                raise NotImplementedError("Unsupported Data Mapping %s" % tag_name)

    def readSystemMapping(self, element: ET.Element, parent: System):
        short_name = self.getShortName(element)
        self.logger.debug("SystemMapping %s" % short_name)
        mapping = parent.createSystemMapping(short_name)
        self.readIdentifiable(element, mapping)
        self.readSystemMappingDataMappings(element, mapping)

    def readSystemMappings(self, element: ET.Element, system: System):
        for child_element in self.findall(element, "MAPPINGS/*"):
            tag_name = self.getTagName(child_element)
            if tag_name == "SYSTEM-MAPPING":
                self.readSystemMapping(child_element, system)
            else:
                raise NotImplementedError("Unsupported Mapping %s" % tag_name)

    def readSystem(self, element: ET.Element, parent: ARPackage):
        short_name = self.getShortName(element)
        self.logger.debug("System %s" % short_name)
        system = parent.createSystem(short_name)
        self.readIdentifiable(element, system)

        system.setEcuExtractVersion(self.getChildElementOptionalLiteral(element, "ECU-EXTRACT-VERSION"))
        for child_element in self.findall(element, "FIBEX-ELEMENTS/FIBEX-ELEMENT-REF-CONDITIONAL"):
            system.addFibexElementRef(self.getChildElementOptionalRefType(child_element, "FIBEX-ELEMENT-REF"))
        self.readSystemMappings(element, system)

    def readParameterInterfaceParameters(self, element: ET.Element, parent: ParameterInterface):
        for child_element in element.findall("./xmlns:PARAMETERS/xmlns:PARAMETER-DATA-PROTOTYPE", self.nsmap):
            short_name = self.getShortName(child_element)
            prototype = parent.createParameter(short_name)
            self.readParameterDataPrototype(child_element, prototype)
    
    def readParameterInterface(self, element: ET.Element, parent: ARPackage):
        short_name = self.getShortName(element)
        self.logger.debug("ParameterInterface %s" % short_name)
        pi_interface = parent.createParameterInterface(short_name)
        self.readIdentifiable(element, pi_interface)
        self.readParameterInterfaceParameters(element, pi_interface)


    def readARPackageElements(self, element: ET.Element, parent: ARPackage):
        for child_element in self.findall(element, "./ELEMENTS/*"):
            tag_name = self.getTagName(child_element.tag)
            if tag_name == "COMPOSITION-SW-COMPONENT-TYPE":
                self.readCompositionSwComponentType(child_element, parent)
            elif tag_name == "COMPLEX-DEVICE-DRIVER-SW-COMPONENT-TYPE":
                self.readComplexDeviceDriverSwComponentType(child_element, parent)
            elif tag_name == "SWC-IMPLEMENTATION":
                self.readSwcImplementation(child_element, parent)
            elif tag_name == "APPLICATION-PRIMITIVE-DATA-TYPE":
                self.readApplicationPrimitiveDataType(child_element, parent)
            elif tag_name == "APPLICATION-RECORD-DATA-TYPE":
                self.readApplicationRecordDataTypes(child_element, parent)
            elif tag_name == "SW-BASE-TYPE":
                self.readSwBaseType(child_element, parent)
            elif tag_name == "COMPU-METHOD":
                self.readCompuMethod(child_element, parent)
            elif tag_name == "CONSTANT-SPECIFICATION":
                self.readConstantSpecification(child_element, parent)
            elif tag_name == "DATA-CONSTR":
                self.readDataConstr(child_element, parent)
            elif tag_name == "END-TO-END-PROTECTION-SET":
                self.readEndToEndProtectionSet(child_element, parent)
            elif tag_name == "SENDER-RECEIVER-INTERFACE":
                self.readSenderReceiverInterfaces(child_element, parent)
            elif tag_name == "UNIT":
                self.readUnit(child_element, parent)
            elif tag_name == "BSW-MODULE-DESCRIPTION":
                self.readBswModuleDescription(child_element, parent)
            elif tag_name == "BSW-MODULE-ENTRY":
                self.readBswModuleEntry(child_element, parent)
            elif tag_name == "SWC-BSW-MAPPING":
                self.readSwcBswMappings(child_element, parent)
            elif tag_name == "BSW-IMPLEMENTATION":
                self.readBswImplementation(child_element, parent)
            elif tag_name == "IMPLEMENTATION-DATA-TYPE":
                self.readImplementationDataType(child_element, parent)
            elif tag_name == "CLIENT-SERVER-INTERFACE":
                self.readClientServerInterface(child_element, parent)
            elif tag_name == "APPLICATION-SW-COMPONENT-TYPE":
                self.readApplicationSwComponentTypes(child_element, parent)
            elif tag_name == "ECU-ABSTRACTION-SW-COMPONENT-TYPE":
                self.readEcuAbstractionSwComponent(child_element, parent)
            elif tag_name == "APPLICATION-ARRAY-DATA-TYPE":
                self.readApplicationArrayDataType(child_element, parent)
            elif tag_name == "SW-RECORD-LAYOUT":
                self.readSwRecordLayout(child_element, parent)
            elif tag_name == "SW-ADDR-METHOD":
                self.readSwAddrMethod(child_element, parent)
            elif tag_name == "TRIGGER-INTERFACE":
                self.readTriggerInterface(child_element, parent)
            elif tag_name == "SERVICE-SW-COMPONENT-TYPE":
                self.readServiceSwComponentType(child_element, parent)
            elif tag_name == "SENSOR-ACTUATOR-SW-COMPONENT-TYPE":
                self.readSensorActuatorSwComponentType(child_element, parent)
            elif tag_name == "DATA-TYPE-MAPPING-SET":
                self.readDataTypeMappingSet(child_element, parent)
            elif tag_name == "MODE-DECLARATION-GROUP":
                self.readModeDeclarationGroup(child_element, parent)
            elif tag_name == "MODE-SWITCH-INTERFACE":
                self.readModeSwitchInterface(child_element, parent)
            elif tag_name == "SWC-TIMING":
                self.readSwcTiming(child_element, parent)
            elif tag_name == "LIN-CLUSTER":
                self.readLinCluster(child_element, parent)
            elif tag_name == "LIN-UNCONDITIONAL-FRAME":
                self.readLinUnconditionalFrame(child_element, parent)
            elif tag_name == "NM-PDU":
                self.readNmPdu(child_element, parent)
            elif tag_name == "N-PDU":
                self.readNPdu(child_element, parent)
            elif tag_name == "DCM-I-PDU":
                self.readDcmIPdu(child_element, parent)
            elif tag_name == "SECURED-I-PDU":
                self.readSecuredIPdu(child_element, parent)
            elif tag_name == "NM-CONFIG":
                self.readNmConfig(child_element, parent)
            elif tag_name == "CAN-TP-CONFIG":
                self.readCanTpConfig(child_element, parent)
            elif tag_name == "LIN-TP-CONFIG":
                pass
            elif tag_name == "SYSTEM":
                self.readSystem(child_element, parent)
            elif tag_name == "ECU-INSTANCE":
                self.readEcuInstance(child_element, parent)
            elif tag_name == "GATEWAY":
                self.readGateway(child_element, parent)
            elif tag_name == "I-SIGNAL-I-PDU-GROUP":
                self.readISignalIPduGroup(child_element, parent)
            elif tag_name == "CAN-CLUSTER":
                self.readCanCluster(child_element, parent)
            elif tag_name == "CAN-FRAME":
                self.readCanFrame(child_element, parent)
            elif tag_name == "I-SIGNAL":
                self.readISignal(child_element, parent)
            elif tag_name == "I-SIGNAL-GROUP":
                self.readISignalGroup(child_element, parent)
            elif tag_name == "I-SIGNAL-I-PDU":
                self.readISignalIPdu(child_element, parent)
            elif tag_name == "SYSTEM-SIGNAL":
                self.readSystemSignal(child_element, parent)
            elif tag_name == "SYSTEM-SIGNAL-GROUP":
                self.readSystemSignalGroup(child_element, parent)
            elif tag_name == "ECUC-VALUE-COLLECTION":
                self.readEcucValueCollection(child_element, parent)
            elif tag_name == "ECUC-MODULE-CONFIGURATION-VALUES":
                self.readEcucModuleConfigurationValues(child_element, parent)
            elif tag_name == "PHYSICAL-DIMENSION":
                self.readPhysicalDimensions(child_element, parent)
            elif tag_name == "PARAMETER-INTERFACE":
                self.readParameterInterface(child_element, parent)
            else:
                self._raiseError("Unsupported element type of ARPackage <%s>" % tag_name)

    def readARPackages(self, element: ET.Element, parent: ARPackage):
        for child_element in element.findall("./xmlns:AR-PACKAGES/xmlns:AR-PACKAGE", self.nsmap):
            short_name = self.getShortName(child_element)
            ar_package = parent.createARPackage(short_name)

            self.logger.debug("readARPackages %s" % ar_package.full_name)

            self.readIdentifiable(child_element, ar_package)
            self.readARPackageElements(child_element, ar_package)
            self.readARPackages(child_element, ar_package)


    def load(self, filename, document: AUTOSAR):
        self.logger.info("Load %s ..." % os.path.realpath(filename))

        tree = ET.parse(filename)
        root = tree.getroot()
        if (self.getPureTagName(root.tag) != "AUTOSAR"):
            self._raiseError("Invalid ARXML file <%s>" % filename)

        self.getAUTOSARInfo(root, document)
        self.readARPackages(root, document)

        document.reload()
