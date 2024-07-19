from ..models.communication import CompositeNetworkRepresentation
from ..models.end_to_end_protection import EndToEndDescription, EndToEndProtectionSet
from ..models.service_mapping import RoleBasedPortAssignment
from ..models.ar_package import AUTOSAR, ARPackage
from ..models.ar_object import ARObject
from ..models.service_needs import RoleBasedDataAssignment
from ..models.ar_ref import ApplicationCompositeElementInPortInterfaceInstanceRef, InnerPortGroupInCompositionInstanceRef, VariableInAtomicSWCTypeInstanceRef, AutosarParameterRef
from ..models.sw_component import AtomicSwComponentType, CompositionSwComponentType, ParameterAccess, PortAPIOption, PortDefinedArgumentValue, PortGroup, ServiceDependency, SwComponentType, SwcServiceDependency
from ..models.data_prototype import AutosarDataPrototype
from ..models.port_prototype import QueuedReceiverComSpec
from ..models.annotation import Annotation, GeneralAnnotation
from ..models.global_constraints import InternalConstrs, DataConstr, DataConstrRule, PhysConstrs

from ..models import SwcInternalBehavior, RunnableEntity, RTEEvent, ServerCallPoint, OperationInvokedEvent, DataReceivedEvent, RVariableInAtomicSwcInstanceRef
from ..models import SwcModeSwitchEvent, RModeInAtomicSwcInstanceRef
from ..models import RefType, AutosarVariableRef, ArVariableInImplementationDataInstanceRef, POperationInAtomicSwcInstanceRef, ROperationInAtomicSwcInstanceRef
from ..models import ImplementationDataType, SwDataDefProps, SwPointerTargetProps, DataTypeMappingSet, DataTypeMap, ImplementationDataTypeElement
from ..models import RPortPrototype, PPortPrototype
from ..models import ReceiverComSpec, ClientComSpec, NonqueuedReceiverComSpec
from ..models import SenderComSpec, NonqueuedSenderComSpec, ServerComSpec
from ..models import SenderReceiverInterface, ClientServerInterface, ClientServerOperation, ArgumentDataPrototype
from ..models import ARElement, Identifiable, AdminData, Sdg, Sd, MultilanguageReferrable, Referrable, LLongName, MultilanguageLongName
from ..models import AssemblySwConnector, PPortInCompositionInstanceRef, RPortInCompositionInstanceRef
from ..models import DelegationSwConnector
from ..models import CompuMethod, CompuScale, Limit, CompuScales, Compu, CompuConst, CompuConstTextContent, CompuScaleConstantContents, CompuScaleRationalFormula, CompuRationalCoeffs, CompuNominatorDenominator
from ..models import InternalBehavior, ExecutableEntity
from ..models import Implementation, Code, AutosarEngineeringObject, ResourceConsumption
from ..models import TransmissionAcknowledgementRequest
from ..models import BswModuleDescription, BswInternalBehavior, BswCalledEntity, BswModuleEntity, BswScheduleEvent, SwcBswMapping, SwcBswRunnableMapping
from ..models import ValueSpecification, ApplicationValueSpecification, TextValueSpecification, NumericalValueSpecification, ArrayValueSpecification, ConstantReference
from ..models import RecordValueSpecification
from ..models import ApplicationRecordDataType
from ..models import SwValueCont, SwValues
from ..models import ARBoolean, ARLiteral
from ..models import BaseType

from typing import List
from colorama import Fore
import xml.etree.ElementTree as ET
import re
import logging

class ARXMLParser:
    def __init__(self, options = None):
        self.nsmap = {"xmlns": "http://autosar.org/schema/r4.0"}
        self.options = {}
        self.options['warning'] = False
        self.logger = logging.getLogger()
        
        self._processOptions(options=options)

    def getTagName(self, tag: str) -> str:
        return tag.replace("{%s}" % self.nsmap["xmlns"], "")

    def _processOptions(self, options):
        if options:
            if 'warning' in options:
                self.options['warning'] = options['warning']

    def _raiseError(self, error_msg):
        if (self.options['warning'] == True):
            self.logger.error(Fore.RED + error_msg + Fore.WHITE)
        else:
            raise ValueError(error_msg)

    def getPureTagName(self, tag):
        return re.sub(r'\{[\w:\/.]+\}(\w+)', r'\1', tag)

    def getChildElement(self, short_name: str, element: ET.Element, key: str) -> str:
        child_element = element.find("./xmlns:%s" % key, self.nsmap)
        if (child_element is not None):
            return child_element.text
        self._raiseError("The attribute %s of <%s> has not been defined" % (key, short_name))

    def getChildElementOptionalValue(self, element: ET.Element, key: str) -> str:
        child_element = element.find("./xmlns:%s" % key, self.nsmap)
        if (child_element is not None):
            if child_element.text is None:
                return ""
            return child_element.text
        return None
    
    def getChildElementLiteral(self, short_name: str, element: ET.Element, key: str) -> ARLiteral:
        child_element = element.find("./xmlns:%s" % key, self.nsmap)
        if (child_element != None):
            literal = ARLiteral()
            self.readElementAttributes(child_element, literal)
            literal.value = child_element.text
            return literal
        self._raiseError("The attribute %s of <%s> has not been defined" % (key, short_name))

    def getChildElementOptionalLiteral(self, element: ET.Element, key: str) -> ARLiteral:
        child_element = element.find("./xmlns:%s" % key, self.nsmap)
        if (child_element != None):
            self.logger.debug("readChildOptionalElementLiteral : %s" % child_element.text)
            literal = ARLiteral()
            self.readElementAttributes(child_element, literal)
            literal.value = child_element.text
            return literal
        return None

    def _convertStringToBooleanValue(self, value: str) -> bool:
        if (value == "true"):
            return True
        return False
    
    def getChildElementOptionalFloatValue(self, element: ET.Element, key: str) -> float:
        value = self.getChildElementOptionalValue(element, key)
        if (value == None):
            return None
        return float(value)

    def getChildElementBooleanValue(self, short_name: str, element: ET.Element, key: str) -> ARBoolean:
        literal = self.getChildElementLiteral(short_name, element, key)
        bool_value = ARBoolean()
        bool_value.timestamp = literal.timestamp
        bool_value.value = self._convertStringToBooleanValue(literal.value)
        return bool_value

    def getChildElementOptionalBooleanValue(self, element: ET.Element, key: str) -> ARBoolean:
        literal = self.getChildElementOptionalLiteral(element, key)
        if (literal == None):
            return None
        bool_value = ARBoolean()
        bool_value.timestamp = literal.timestamp
        bool_value.value = self._convertStringToBooleanValue(literal.value)
        return bool_value

    def _convertStringToNumberValue(self, value) -> int:
        m = re.match(r"0x([0-9a-f]+)", value, re.I)
        if (m):
            return int(m.group(1), 16)
        return int(value)

    def getChildElementNumberValue(self, short_name: str, element: ET.Element, key: str) -> int:
        value = self.getChildElement(short_name, element, key)
        return self._convertStringToNumberValue(value)

    def getChildElementOptionalNumberValue(self, element: ET.Element, key: str) -> int:
        value = self.getChildElementOptionalValue(element, key)
        if (value == None):
            return None
        return self._convertStringToNumberValue(value)
    
    def getChildLimitElement(self, element: ET.Element, key: str) -> Limit:
        child_element = element.find("./xmlns:%s" % key, self.nsmap)
        if (child_element != None):
            limit = Limit()
            self.readElementAttributes(child_element, limit)
            if ('INTERVAL-TYPE' in child_element.attrib):
                limit.interval_type = child_element.attrib['INTERVAL-TYPE']
            else:
                limit.interval_type = "CLOSED"
            limit.value = child_element.text
            return limit
        return None
    
    def getShortName(self, element: ET.Element) -> str:
        return self.getChildElement("", element, "SHORT-NAME")
    
    def readSd(self, element: ET.Element, sdg: Sdg):
        for child_element in element.findall("./xmlns:SD", self.nsmap):
            sd = Sd()
            sd.gid = child_element.attrib['GID']
            sd.value = child_element.text

            sdg.addSd(sd)
    
    def readSdg(self, element: ET.Element, admin_data: AdminData):
        for child_element in element.findall("./xmlns:SDGS/xmlns:SDG", self.nsmap):
            sdg = Sdg()
            sdg.gid = child_element.attrib["GID"]
            self.readSd(child_element, sdg)
            admin_data.addSdg(sdg)
    
    def readAdminData(self, element: ET.Element, identifiable: Identifiable):
        child_element = element.find("./xmlns:ADMIN-DATA", self.nsmap)
        if child_element is not None:
            self.logger.debug("readAdminData")
            admin_data = AdminData()
            self.readSdg(child_element, admin_data)
            identifiable.admin_data = admin_data
    
    def readIdentifiable(self, element: ET.Element, identifiable: Identifiable):
        self.readElementAttributes(element, identifiable)
        identifiable.long_name = self.getMultilanguageLongName(element, "LONG-NAME")
        identifiable.category = self.getChildElementOptionalValue(element, "CATEGORY")
        self.readAdminData(element, identifiable)

    def _getChildElementRefTypeDestAndValue(self, element) -> RefType:
        ref = RefType()
        ref.dest = element.attrib['DEST']
        ref.value = element.text
        return ref

    def getChildElementRefType(self, short_name: str, element: ET.Element, key: str) -> RefType:
        child_element = element.find("./xmlns:%s" % key, self.nsmap)
        if (child_element != None):
            return self._getChildElementRefTypeDestAndValue(child_element)
        self._raiseError("The attribute %s of <%s> has not been defined" % (key, short_name))

    def getChildElementOptionalRefType(self, element:ET.Element, key: str) -> RefType:
        child_element = element.find("./xmlns:%s" % key, self.nsmap)
        if (child_element != None):
            return self._getChildElementRefTypeDestAndValue(child_element)
        return None

    def getChildElementRefTypeList(self, element: ET.Element, key: str) -> List[RefType]:
        child_elements = element.findall("./xmlns:%s" % key, self.nsmap)
        results = []
        for child_element in child_elements:
            ref = RefType()
            ref.dest = child_element.attrib['DEST']
            ref.value = child_element.text
            results.append(ref)
        return results
    
    def readElementOptionalAttrib(self, element: ET.Element, key: str) -> str:
        if key in element.attrib:
            return element.attrib[key]
        return None
    
    def readLLongName(self, element: ET.Element, long_name: MultilanguageLongName):
        for child_element in element.findall("./xmlns:L-4", self.nsmap):
            l4 = LLongName()
            self.readElementAttributes(child_element, l4)
            l4.value = child_element.text
            if 'L' in child_element.attrib:
                l4.l = child_element.attrib['L']
            long_name.add_l4(l4)
    
    def getMultilanguageLongName(self, element: ET.Element, key: str) -> MultilanguageLongName:
        long_name = None
        child_element = element.find("./xmlns:%s" % key, self.nsmap)
        if child_element is not None:
            long_name = MultilanguageLongName()
            self.readElementAttributes(child_element, long_name)
            self.readLLongName(child_element, long_name)
        return long_name

    def readElementAttributes(self, element: ET.Element, ar_object: ARObject):
        ar_object.timestamp = self.readElementOptionalAttrib(element, "T")             # read the timestamp
        ar_object.uuid      = self.readElementOptionalAttrib(element, "UUID")          # read the uuid

        if ar_object.timestamp is not None:
            self.logger.debug("Timestamp: %s" % ar_object.timestamp)
        if ar_object.uuid is not None:
            self.logger.debug("UUID: %s" % ar_object.uuid)

    def readAutosarVariableInImplDatatype(self, element: ET.Element, accessed_variable_ref: AutosarVariableRef):
        child_element = element.find("./xmlns:ACCESSED-VARIABLE/xmlns:AUTOSAR-VARIABLE-IREF", self.nsmap)
        if (child_element != None):
            autosar_variable_iref = VariableInAtomicSWCTypeInstanceRef()
            autosar_variable_iref.port_prototype_ref = self.getChildElementOptionalRefType(child_element, "PORT-PROTOTYPE-REF")
            if autosar_variable_iref.port_prototype_ref is None:
                self._raiseError("PORT-PROTOTYPE-REF of <%s> is empty." % accessed_variable_ref.parent.short_name)
            autosar_variable_iref.target_data_prototype_ref = self.getChildElementOptionalRefType(child_element, "TARGET-DATA-PROTOTYPE-REF")
            if autosar_variable_iref.target_data_prototype_ref is None:
                self._raiseError("TARGET-DATA-PROTOTYPE-REF of <%s> is empty." % accessed_variable_ref.parent.short_name)
            accessed_variable_ref.autosar_variable_iref = autosar_variable_iref

    def readLocalVariableRef(self, element, accessed_variable_ref: AutosarVariableRef):
        child_element = element.find("./xmlns:ACCESSED-VARIABLE", self.nsmap)
        if (child_element != None):
            accessed_variable_ref.local_variable_ref = self.getChildElementOptionalRefType(child_element, "LOCAL-VARIABLE-REF")

    def _readVariableAccesses(self, element: ET.Element, parent: RunnableEntity, key: str):
        for child_element in element.findall("./xmlns:%s/xmlns:VARIABLE-ACCESS" % key, self.nsmap):
            short_name = self.getShortName(child_element)

            self.logger.debug("readVariableAccesses %s" % short_name)

            if (key == "DATA-RECEIVE-POINT-BY-ARGUMENTS"):
                variable_access = parent.createDataReceivePointByArgument(short_name)
                self.readAutosarVariableInImplDatatype(child_element, variable_access.accessed_variable_ref)
            elif (key == "DATA-RECEIVE-POINT-BY-VALUES"):
                variable_access = parent.createDataReceivePointByValue(short_name)
                self.readAutosarVariableInImplDatatype(child_element, variable_access.accessed_variable_ref)
            elif (key == "DATA-READ-ACCESSS"):
                variable_access = parent.createDataReadAccess(short_name)
                self.readAutosarVariableInImplDatatype(child_element, variable_access.accessed_variable_ref)
            elif (key == "DATA-WRITE-ACCESSS"):
                variable_access = parent.createDataWriteAccess(short_name)
                self.readAutosarVariableInImplDatatype(child_element, variable_access.accessed_variable_ref)
            elif (key == "DATA-SEND-POINTS"):
                variable_access = parent.createDataSendPoint(short_name)
                self.readAutosarVariableInImplDatatype(child_element, variable_access.accessed_variable_ref)
            elif (key == "WRITTEN-LOCAL-VARIABLES"):
                variable_access = parent.createWrittenLocalVariable(short_name)
                self.readLocalVariableRef(child_element, variable_access.accessed_variable_ref)
            elif (key == "READ-LOCAL-VARIABLES"):
                variable_access = parent.createReadLocalVariable(short_name)
                self.readLocalVariableRef(child_element, variable_access.accessed_variable_ref)
            else:
                self._raiseError("Invalid key type <%s>" % key)

            # self.readIdentifiable(child_element, variable_access)

    def readBswModuleDescriptionImplementedEntry(self, element: ET.Element, parent: BswModuleDescription):
        for child_element in element.findall("./xmlns:PROVIDED-ENTRYS/xmlns:BSW-MODULE-ENTRY-REF-CONDITIONAL", self.nsmap):
            ref = self.getChildElementOptionalRefType(child_element, "BSW-MODULE-ENTRY-REF") 
            if (ref != None):
                parent.addImplementedEntry(ref)
            self.logger.debug("ImplementedEntry <%s> of BswModuleDescription <%s> has been added", ref.value, parent.short_name)

    def readProvidedModeGroup(self, element: ET.Element, parent: BswModuleDescription):
        for child_element in element.findall("./xmlns:PROVIDED-MODE-GROUPS/xmlns:MODE-DECLARATION-GROUP-PROTOTYPE", self.nsmap):
            short_name = self.getShortName(child_element)
            self.logger.debug("readProvidedModeGroup %s" % short_name)

            mode_group = parent.createProvidedModeGroup(short_name)
            mode_group.type_tref = self.getChildElementRefType(parent.short_name, child_element, "TYPE-TREF")

    def readRequiredModeGroup(self, element: ET.Element, parent: BswModuleDescription):
        for child_element in element.findall("./xmlns:REQUIRED-MODE-GROUPS/xmlns:MODE-DECLARATION-GROUP-PROTOTYPE", self.nsmap):
            short_name = self.getShortName(child_element)
            self.logger.debug("readRequiredModeGroup %s" % short_name)
            mode_group = parent.createProvidedModeGroup(short_name)
            mode_group.type_tref = self.getChildElementRefType(parent.short_name, child_element, "TYPE-TREF")

    def readCanEnterExclusiveAreaRefs(self, element: ET.Element, entity: ExecutableEntity):
        child_element = element.find("./xmlns:CAN-ENTER-EXCLUSIVE-AREA-REFS", self.nsmap)
        if child_element != None:
            for ref in self.getChildElementRefTypeList(child_element, "CAN-ENTER-EXCLUSIVE-AREA-REF"):
                entity.addCanEnterExclusiveAreaRef(ref)

    def readExecutableEntity(self, element: ET.Element, entity: ExecutableEntity):
        self.logger.debug("readExecutableEntity %s" % entity.short_name)
        self.readIdentifiable(element, entity)
        entity.minimum_start_interval = self.getChildElementOptionalFloatValue(element, "MINIMUM-START-INTERVAL")
        self.readCanEnterExclusiveAreaRefs(element, entity)

    def readBswModuleEntity(self, element, entity: BswModuleEntity):
        self.readExecutableEntity(element, entity)
        entity.implemented_entry_ref = self.getChildElementRefType(entity.short_name, element, "IMPLEMENTED-ENTRY-REF")

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
        event.starts_on_event_ref = self.getChildElementRefType(event.short_name, element, "STARTS-ON-EVENT-REF")

    def readBswScheduleEvent(self, element, event: BswScheduleEvent):
        self.readBswEvent(element, event)

    def readBswModeSwitchEvent(self, element: ET.Element, parent: BswInternalBehavior):
        for child_element in element.findall("./xmlns:EVENTS/xmlns:BSW-MODE-SWITCH-EVENT", self.nsmap):
            short_name = self.getShortName(child_element)
            self.logger.debug("readBswModeSwitchEvent %s" % short_name)
            event = parent.createBswModeSwitchEvent(short_name)

            self.readBswScheduleEvent(child_element, event)

    def readBswTimingEvent(self, element: ET.Element, parent: BswInternalBehavior):
        for child_element in element.findall("./xmlns:EVENTS/xmlns:BSW-TIMING-EVENT", self.nsmap):
            short_name = self.getShortName(child_element)
            self.logger.debug("readBswTimingEvent %s" % short_name)
            event = parent.createBswTimingEvent(short_name)
            event.period = self.getChildElementOptionalFloatValue(child_element, "PERIOD")

            self.readBswScheduleEvent(child_element, event)

    def readBswDataReceivedEvent(self, element: ET.Element, parent: BswInternalBehavior):
        for child_element in element.findall("./xmlns:EVENTS/xmlns:BSW-DATA-RECEIVED-EVENT", self.nsmap):
            short_name = self.getShortName(child_element)
            self.logger.debug("readBswDataReceivedEvent %s" % short_name)
            event = parent.createBswDataReceivedEvent(short_name)
            event.data_ref = self.getChildElementRefType(parent.short_name, child_element, "DATA-REF")

            self.readBswScheduleEvent(child_element, event)

    def readBswInternalTriggerOccurredEvent(self, element: ET.Element, parent: BswInternalBehavior):
        for child_element in element.findall("./xmlns:EVENTS/xmlns:BSW-INTERNAL-TRIGGER-OCCURRED-EVENT", self.nsmap):
            short_name = self.getShortName(child_element)
            self.logger.debug("readBswInternalTriggerOccurredEvent %s" % short_name)
            event = parent.createBswInternalTriggerOccurredEvent(short_name)
            event.event_source_ref = self.getChildElementRefType(parent.short_name, child_element, "EVENT-SOURCE-REF")

            self.readBswScheduleEvent(child_element, event)

    def readDataTypeMappingRefs(self, element: ET.Element, behavior: InternalBehavior):
        child_element = element.find("./xmlns:DATA-TYPE-MAPPING-REFS", self.nsmap)
        if child_element != None:
            for ref in self.getChildElementRefTypeList(child_element, "DATA-TYPE-MAPPING-REF"):
                behavior.addDataTypeMappingRef(ref)

    def readInternalBehavior(self, element: ET.Element, behavior: InternalBehavior):
        self.readIdentifiable(element,  behavior)
        for child_element in element.findall("./xmlns:EXCLUSIVE-AREAS/xmlns:EXCLUSIVE-AREA", self.nsmap):
            short_name = self.getShortName(child_element)
            behavior.createExclusiveArea(short_name)
        self.readDataTypeMappingRefs(element, behavior)

    def getRoleBasedDataAssignment(self, element: ET.Element) -> RoleBasedDataAssignment:
        assignment = RoleBasedDataAssignment()
        assignment.role = self.getChildElementOptionalValue(element, "ROLE")
        assignment.used_parameter_element = self.getAutosarParameterRef(element, "USED-PARAMETER-ELEMENT")
        assignment.used_pim_ref = self.getChildElementOptionalRefType(element, "USED-PIM-REF")
        return assignment
    
    def getRoleBasedPortAssignment(self, element: ET.Element) -> RoleBasedPortAssignment:
        assignment = RoleBasedPortAssignment()
        assignment.port_prototype_ref = self.getChildElementOptionalRefType(element, "PORT-PROTOTYPE-REF")
        assignment.role = self.getChildElementOptionalValue(element, "ROLE")
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
        needs.n_data_sets = self.getChildElementOptionalNumberValue(element, "N-DATA-SETS")
        needs.n_rom_blocks = self.getChildElementOptionalNumberValue(element, "N-ROM-BLOCKS")
        needs.readonly = self.getChildElementOptionalBooleanValue(element, "READONLY")
        needs.reliability = self.getChildElementOptionalValue(element, "RELIABILITY")
        needs.resistant_to_changed_sw = self.getChildElementOptionalBooleanValue(element, "RESISTANT-TO-CHANGED-SW")
        needs.restore_at_start = self.getChildElementOptionalBooleanValue(element, "RESTORE-AT-START")
        needs.store_at_shutdown = self.getChildElementOptionalBooleanValue(element, "STORE-AT-SHUTDOWN")
        needs.write_only_once = self.getChildElementOptionalBooleanValue(element, "WRITE-ONLY-ONCE")
        needs.write_verification = self.getChildElementOptionalBooleanValue(element, "WRITE-VERIFICATION")
        needs.writing_priority = self.getChildElementOptionalValue(element, "WRITING-PRIORITY")                          

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

    def readSwcInternalBehavior(self, element: ET.Element, parent: AtomicSwComponentType):
        for child_element in element.findall("./xmlns:INTERNAL-BEHAVIORS/xmlns:SWC-INTERNAL-BEHAVIOR", self.nsmap):
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
            behavior.handle_termination_and_restart = self.getChildElementOptionalValue(child_element, "HANDLE-TERMINATION-AND-RESTART")
            self.readPerInstanceMemories(child_element, behavior)
            self.readPerInstanceParameter(child_element, behavior)
            self.readPortAPIOptions(child_element, behavior)
            behavior.supports_multiple_instantiation = self.getChildElementOptionalBooleanValue(child_element, "SUPPORTS-MULTIPLE-INSTANTIATION")

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

    def readBswModuleDescription(self, element: ET.Element, parent: ARPackage):
        short_name = self.getShortName(element)
        bsw_module_description = parent.createBswModuleDescription(short_name)
        bsw_module_description.module_id = self.getChildElementNumberValue(short_name, element, "MODULE-ID")

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
        entry.service_id = self.getChildElementOptionalNumberValue(element, "SERVICE-ID")
        entry.call_type = self.getChildElementOptionalValue(element, "CALL-TYPE")
        entry.execution_context = self.getChildElementOptionalValue(element, "EXECUTION-CONTEXT")
        entry.sw_service_impl_policy = self.getChildElementOptionalValue(element, "SW-SERVICE-IMPL-POLICY")

        #self.logger.debug("readBswModuleEntry \n%s" % entry)
        self.logger.debug("readBswModuleEntry %s" % entry.short_name)

    def readArtifactDescriptor(self, element: ET.Element, code_desc: Code):
        for child_element in element.findall("./xmlns:ARTIFACT-DESCRIPTORS/xmlns:AUTOSAR-ENGINEERING-OBJECT", self.nsmap):
            artifact_desc = AutosarEngineeringObject()
            artifact_desc.short_label = self.getChildElement(code_desc.short_name, child_element, "SHORT-LABEL")
            self.readIdentifiable(child_element, artifact_desc)
            code_desc.addArtifactDescriptor(artifact_desc)
            
            self.logger.debug("readArtifactDescriptor %s", artifact_desc.short_label)

    def readCodeDescriptor(self, element: ET.Element, impl: Implementation):
        for child_element in element.findall("./xmlns:CODE-DESCRIPTORS/xmlns:CODE", self.nsmap):
            short_name = self.getShortName(child_element)
            self.logger.debug("readCodeDescriptor %s" % short_name)
            code_desc = impl.createCodeDescriptor(short_name)
            self.readIdentifiable(child_element, code_desc)
            self.readArtifactDescriptor(child_element, code_desc)

    def readMemorySections(self, element: ET.Element, consumption: ResourceConsumption):
        for child_element in element.findall("./xmlns:MEMORY-SECTIONS/xmlns:MEMORY-SECTION", self.nsmap):
            short_name = self.getShortName(child_element)
            memory_section = consumption.createMemorySection(short_name)
            self.readIdentifiable(child_element, memory_section)
            memory_section.alignment = self.getChildElementOptionalValue(child_element, "ALIGNMENT")
            memory_section.size = self.getChildElementOptionalNumberValue(child_element, "SIZE")
            memory_section.sw_addr_method_ref = self.getChildElementRefType(consumption.short_name, child_element, "SW-ADDRMETHOD-REF")
            self.logger.debug("readMemorySections %s" % memory_section.short_name)

    def readResourceConsumption(self, element: ET.Element, impl: Implementation):
        child_element = element.find("./xmlns:RESOURCE-CONSUMPTION", self.nsmap)
        if (child_element == None):
            self._raiseError("Invalid ResourceConsumption of Implementation <%s>" % impl.short_name)
            return
        short_name = self.getShortName(child_element)
        impl.resource_consumption = ResourceConsumption(impl, short_name)
        self.readIdentifiable(child_element, impl.resource_consumption)
        self.readMemorySections(child_element, impl.resource_consumption)

    def readImplementation(self, element: ET.Element, impl: Implementation):
        self.readIdentifiable(element, impl)
        self.readCodeDescriptor(element, impl)
        impl.programming_language = self.getChildElementOptionalValue(element, "PROGRAMMING-LANGUAGE")
        self.readResourceConsumption(element, impl)
        impl.sw_version = self.getChildElementOptionalValue(element, "SW-VERSION")
        impl.swc_bsw_mapping_ref = self.getChildElementOptionalRefType(element, "SWC-BSW-MAPPING-REF")
        impl.used_code_generator = self.getChildElementOptionalValue(element, "USED-CODE-GENERATOR")
        impl.vendor_id = self.getChildElementOptionalNumberValue(element, "VENDOR-ID")

    def readBswImplementation(self, element: ET.Element, parent: ARPackage):
        short_name = self.getShortName(element)
        impl = parent.createBswImplementation(short_name)   
        self.logger.debug("readBswImplementation %s" % impl.short_name)

        self.readImplementation(element, impl)

        impl.ar_release_version = self.getChildElement(parent.short_name, element, "AR-RELEASE-VERSION")
        impl.behavior_ref = self.getChildElementRefType(parent.short_name, element, "BEHAVIOR-REF")

    def readSwcImplementation(self, element: ET.Element, parent: ARPackage):
        short_name = self.getShortName(element)
        impl = parent.createSwcImplementation(short_name)   
        self.logger.debug("readSwcImplementation %s" % impl.short_name)
        self.readImplementation(element, impl)
        impl.behavior_ref = self.getChildElementRefType(parent.short_name, element, "BEHAVIOR-REF")

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
            parent.operation_iref = operation_iref

    def readRVariableInAtomicSwcInstanceRef(self, element: ET.Element, parent: DataReceivedEvent):
        child_element = element.find("./xmlns:DATA-IREF", self.nsmap)
        if (child_element is not None):
            data_iref = RVariableInAtomicSwcInstanceRef()
            data_iref.context_r_port_ref = self.getChildElementOptionalRefType(child_element, "CONTEXT-R-PORT-REF")
            data_iref.target_data_element_ref = self.getChildElementOptionalRefType(child_element, "TARGET-DATA-ELEMENT-REF")
            parent.data_iref = data_iref

    def readRModeInAtomicSwcInstanceRef(self, element: ET.Element, parent: SwcModeSwitchEvent):
        for child_element in element.findall("./xmlns:MODE-IREFS/xmlns:MODE-IREF", self.nsmap):
            mode_iref = RModeInAtomicSwcInstanceRef()
            mode_iref.context_port_ref = self.getChildElementOptionalRefType(child_element, "CONTEXT-PORT-REF")
            mode_iref.context_mode_declaration_group_prototype_ref = self.getChildElementRefType("", child_element, "CONTEXT-MODE-DECLARATION-GROUP-PROTOTYPE-REF")
            mode_iref.target_mode_declaration_ref = self.getChildElementRefType("", child_element, "TARGET-MODE-DECLARATION-REF")
            parent.addModeIRef(mode_iref)

    def readSynchronousServerCallPoint(self, element: ET.Element, parent: RunnableEntity):
        short_name = self.getShortName(element)
        self.logger.debug("readSynchronousServerCallPoint %s" % short_name)
        serverCallPoint = parent.createSynchronousServerCallPoint(short_name)
        serverCallPoint.timeout = self.getChildElementOptionalFloatValue(element, "TIMEOUT")
        self.readROperationIRef(element, "OPERATION-IREF", serverCallPoint)

    def readAsynchronousServerCallPoint(self, element: ET.Element, parent: RunnableEntity):
        short_name = self.getShortName(element)
        self.logger.debug("readAsynchronousServerCallPoint %s" % short_name)
        serverCallPoint = parent.createAsynchronousServerCallPoint(short_name)
        serverCallPoint.timeout = self.getChildElementOptionalFloatValue(element, "TIMEOUT")
        self.readROperationIRef(element, "OPERATION-IREF", serverCallPoint)

    def readInternalBehaviorServerCallPoint(self, element: ET.Element, parent: RunnableEntity):
        for child_element in element.findall("./xmlns:SERVER-CALL-POINTS/*", self.nsmap):
            tag_name = self.getTagName(child_element.tag)
            if tag_name == "SYNCHRONOUS-SERVER-CALL-POINT":
                self.readSynchronousServerCallPoint(child_element, parent)
            elif tag_name == "ASYNCHRONOUS-SERVER-CALL-POINT":
                self.readAsynchronousServerCallPoint(child_element, parent)
            else:
                self._raiseError("Unsupported server call point type <%s>" % tag_name)

    def readInternalTriggeringPoint(self, element: ET.Element, parent: RunnableEntity):
        for child_element in element.findall("./xmlns:INTERNAL-TRIGGERING-POINTS/xmlns:INTERNAL-TRIGGERING-POINT", self.nsmap):
            short_name = self.getShortName(child_element)
            point = parent.createInternalTriggeringPoint(short_name)
            point.sw_impl_policy = self.getChildElementOptionalValue(child_element, "SW-IMPL-POLICY")

    def readSwcInternalBehaviorRunnables(self, element: ET.Element, parent: SwcInternalBehavior):
        for child_element in element.findall("./xmlns:RUNNABLES/xmlns:RUNNABLE-ENTITY", self.nsmap):
            short_name = self.getShortName(child_element)
            entity = parent.createRunnableEntity(short_name)
            self.logger.debug("readRunnableEntities %s" % short_name)
            
            self.readExecutableEntity(child_element, entity)
            entity.can_be_invoked_concurrently = self.getChildElementOptionalBooleanValue(child_element, "CAN-BE-INVOKED-CONCURRENTLY")
            entity.symbol = self.getChildElement(short_name, child_element, "SYMBOL")

            self.readDataReceivePointByArguments(child_element, entity)
            self.readDataReceivePointByValues(child_element, entity)
            self.readDataReadAccesses(child_element, entity)
            self.readDataWriteAccesses(child_element, entity)
            self.readDataSendPoints(child_element, entity)
            self.readParameterAccesses(child_element, entity)
            self.readWrittenLocalVariables(child_element, entity)
            self.readReadLocalVariables(child_element, entity)
            self.readInternalBehaviorServerCallPoint(child_element, entity)
            self.readInternalTriggeringPoint(child_element, entity)

    def getRModeInAtomicSwcInstanceRef(self, element: ET.Element) -> RModeInAtomicSwcInstanceRef:
        iref = RModeInAtomicSwcInstanceRef()
        iref.base_ref = self.getChildElementOptionalRefType(element, "BASE")
        iref.context_port_ref = self.getChildElementOptionalRefType(element, "CONTEXT-PORT-REF")
        iref.context_mode_declaration_group_prototype_ref = self.getChildElementOptionalRefType(element, "CONTEXT-MODE-DECLARATION-GROUP-PROTOTYPE-REF")
        iref.target_mode_declaration_ref = self.getChildElementOptionalRefType(element, "TARGET-MODE-DECLARATION-REF")
        return iref

    def readRTEEvent(self, element: ET.Element, event: RTEEvent):
        self.readIdentifiable(element, event)
        event.start_on_event_ref = self.getChildElementOptionalRefType(element, "START-ON-EVENT-REF")
        for child_element in element.findall("./xmlns:DISABLED-MODE-IREFS/xmlns:DISABLED-MODE-IREF", self.nsmap):
            iref = self.getRModeInAtomicSwcInstanceRef(child_element)
            event.addDisabledModeIRef(iref)

    def readOperationIRef(self, element: ET.Element, parent: OperationInvokedEvent):
        child_element = element.find("./xmlns:OPERATION-IREF", self.nsmap)
        if (child_element != None):
            parent.operation_iref = POperationInAtomicSwcInstanceRef()
            parent.operation_iref.context_p_port_ref = self.getChildElementRefType(parent.short_name, child_element, "CONTEXT-P-PORT-REF")
            parent.operation_iref.target_provided_operation_ref = self.getChildElementRefType(parent.short_name, child_element, "TARGET-PROVIDED-OPERATION-REF")

    def readOperationInvokedEvent(self, element: ET.Element, parent: SwcInternalBehavior):
        short_name = self.getShortName(element)
        event = parent.createOperationInvokedEvent(short_name)
        self.readOperationIRef(element, event)
        self.readRTEEvent(element, event)
    
    def readExplicitInterRunnableVariables(self, element: ET.Element, parent: SwcInternalBehavior):
        for child_element in element.findall("./xmlns:EXPLICIT-INTER-RUNNABLE-VARIABLES/xmlns:VARIABLE-DATA-PROTOTYPE", self.nsmap):
            short_name = self.getShortName(child_element)
            prototype = parent.createExplicitInterRunnableVariable(short_name)
            prototype.sw_data_def_props = self.getSwDataDefProps(child_element, "SW-DATA-DEF-PROPS")
            prototype.type_tref = self.getChildElementOptionalRefType(child_element, "TYPE-TREF")
            prototype.init_value = self.getInitValue(child_element)

    def readPerInstanceMemories(self, element: ET.Element, behavior: SwcInternalBehavior):
        for child_element in element.findall("./xmlns:PER-INSTANCE-MEMORYS/xmlns:PER-INSTANCE-MEMORY", self.nsmap):
            short_name = self.getShortName(child_element)
            memory = behavior.createPerInstanceMemory(short_name)
            self.readIdentifiable(child_element, memory)
            memory.init_value = self.getChildElementOptionalValue(child_element, "INIT-VALUE")
            memory.sw_data_def_props = self.getSwDataDefProps(child_element, "SW-DATA-DEF-PROPS")
            memory.type = self.getChildElementOptionalValue(child_element, "TYPE")
            memory.type_definition = self.getChildElementOptionalValue(child_element, "TYPE-DEFINITION")

    def readAutosarDataPrototype(self, element: ET.Element, prototype: AutosarDataPrototype):
        prototype.type_tref = self.getChildElementOptionalRefType(element, "TYPE-TREF")

    def readParameterDataPrototype(self, element: ET.Element, behavior: SwcInternalBehavior):
        short_name = self.getShortName(element)
        prototype = behavior.createParameterDataPrototype(short_name)
        self.readIdentifiable(element, prototype)
        self.readAutosarDataPrototype(element, prototype)
        prototype.init_value = self.getInitValue(element)
        
    def readPerInstanceParameter(self, element: ET.Element, behavior: SwcInternalBehavior):
        for child_element in element.findall("./xmlns:PER-INSTANCE-PARAMETERS/xmlns:PARAMETER-DATA-PROTOTYPE", self.nsmap):
            self.readParameterDataPrototype(child_element, behavior)

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
            option.indirect_API = self.getChildElementOptionalBooleanValue(child_element, "INDIRECT-API")
            option.port_ref = self.getChildElementOptionalRefType(child_element, "PORT-REF")
            for argument_value_tag in child_element.findall("./xmlns:PORT-ARG-VALUES/xmlns:PORT-DEFINED-ARGUMENT-VALUE", self.nsmap):
                option.addPortArgValue(self.readPortDefinedArgumentValue(argument_value_tag))
            behavior.addPortAPIOption(option)
            
    def readInitEvents(self, element, parent: SwcInternalBehavior):
        for child_element in element.findall("./xmlns:EVENTS/xmlns:INIT-EVENT", self.nsmap):
            short_name = self.getShortName(child_element)
            event = parent.createInitEvent(short_name)
            self.readRTEEvent(child_element, event)

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
        event.activation = self.getChildElementOptionalValue(element, "ACTIVATION")
        self.readRModeInAtomicSwcInstanceRef(element, event)

    def readInternalTriggerOccurredEvent(self, element: ET.Element, parent: SwcInternalBehavior):
        short_name = self.getShortName(element)
        event = parent.createInternalTriggerOccurredEvent(short_name)
        self.readRTEEvent(element, event)
        event.event_source_ref = self.getChildElementRefType(parent.short_name, element, "EVENT-SOURCE-REF")

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
            else:
                self._raiseError("Unsupported SwcInternalBehavior Event <%s>" % tag_name)

    def readSwPointerTargetProps(self, element: ET.Element, parent: SwDataDefProps):
        child_element = element.find("./xmlns:SW-POINTER-TARGET-PROPS", self.nsmap)
        if (child_element != None):
            sw_pointer_target_props = SwPointerTargetProps()
            sw_pointer_target_props.target_category = self.getChildElement("", child_element, "TARGET-CATEGORY")
            sw_pointer_target_props.sw_data_def_props = self.getSwDataDefProps(child_element, "SW-DATA-DEF-PROPS")
            parent.sw_pointer_target_props = sw_pointer_target_props

    def readGeneralAnnotation(self, element: ET.Element, annotation: GeneralAnnotation):
        annotation.label = self.getMultilanguageLongName(element, "LABEL")

    def readAnnotations(self, element: ET.Element, props: SwDataDefProps) :
        for child_element in element.findall("./xmlns:ANNOTATIONS/xmlns:ANNOTATION", self.nsmap):
            annotation = Annotation()
            self.readGeneralAnnotation(child_element, annotation)
            props.addAnnotation(annotation)

    def getSwDataDefProps(self, element: ET.Element, key: str) -> SwDataDefProps:
        child_element = element.find("./xmlns:%s/xmlns:SW-DATA-DEF-PROPS-VARIANTS/xmlns:SW-DATA-DEF-PROPS-CONDITIONAL" % key, self.nsmap)

        if (child_element is not None):
            sw_data_def_props = SwDataDefProps()
            self.readElementAttributes(child_element, sw_data_def_props)
            self.readAnnotations(child_element, sw_data_def_props)
            sw_data_def_props.base_type_ref = self.getChildElementOptionalRefType(child_element, "BASE-TYPE-REF")
            sw_data_def_props.data_constr_ref = self.getChildElementOptionalRefType(child_element, "DATA-CONSTR-REF")
            sw_data_def_props.compu_method_ref = self.getChildElementOptionalRefType(child_element, "COMPU-METHOD-REF")
            sw_data_def_props.sw_impl_policy = self.getChildElementOptionalValue(child_element, "SW-IMPL-POLICY")
            sw_data_def_props.implementation_data_type_ref = self.getChildElementOptionalRefType(child_element, "IMPLEMENTATION-DATA-TYPE-REF")
            sw_data_def_props.sw_calibration_access = self.getChildElementOptionalValue(child_element, "SW-CALIBRATION-ACCESS")
            self.readSwPointerTargetProps(child_element, sw_data_def_props)
            return sw_data_def_props

    def readApplicationPrimitiveDataType(self, element: ET.Element, parent: ARPackage):
        short_name = self.getShortName(element)
        data_type = parent.createApplicationPrimitiveDataType(short_name)
        self.logger.debug("readApplicationPrimitiveDataTypes %s" % short_name)
        self.readIdentifiable(element, data_type)
        data_type.sw_data_def_props = self.getSwDataDefProps(element, "SW-DATA-DEF-PROPS")

    def readApplicationRecordElements(self, element: ET.Element, parent: ApplicationRecordDataType):
        for child_element in element.findall("./xmlns:ELEMENTS/xmlns:APPLICATION-RECORD-ELEMENT", self.nsmap):
            short_name = self.getShortName(child_element)
            record_element = parent.createApplicationRecordElement(short_name)
            self.logger.debug("readApplicationRecordElements %s" % short_name)
            self.readIdentifiable(child_element, record_element)
            record_element.type_tref = self.getChildElementOptionalRefType(child_element, "TYPE-TREF")

    def readApplicationRecordDataTypes(self, element: ET.Element, parent: ARPackage):
        short_name = self.getShortName(element)
        data_type = parent.createApplicationRecordDataType(short_name)
        self.logger.debug("readApplicationRecordDataTypes %s" % short_name)
        self.readIdentifiable(element, data_type)
        data_type.sw_data_def_props = self.getSwDataDefProps(element, "SW-DATA-DEF-PROPS")
        self.readApplicationRecordElements(element, data_type)

    def readImplementationDataTypeElements(self, element: ET.Element, parent: ARElement):
        for child_element in element.findall("./xmlns:SUB-ELEMENTS/xmlns:IMPLEMENTATION-DATA-TYPE-ELEMENT", self.nsmap):
            short_name = self.getShortName(child_element)
            type_element = parent.createImplementationDataTypeElement(short_name)   # type: ImplementationDataTypeElement
            self.readIdentifiable(child_element, type_element)
            type_element.array_size = self.getChildElementOptionalValue(child_element, "ARRAY-SIZE")
            type_element.array_size_semantics = self.getChildElementOptionalValue(child_element, "ARRAY-SIZE-SEMANTICS")
            self.readImplementationDataTypeElements(child_element, type_element)
            type_element.sw_data_def_props = self.getSwDataDefProps(child_element, "SW-DATA-DEF-PROPS")

    def readImplementationDataType(self, element: ET.Element, parent: ARPackage):
        short_name = self.getShortName(element)
        data_type = parent.createImplementationDataType(short_name)
        self.readIdentifiable(element, data_type)
        self.readImplementationDataTypeElements(element, data_type)
        data_type.sw_data_def_props = self.getSwDataDefProps(element, "SW-DATA-DEF-PROPS")
        if (data_type.category == ImplementationDataType.CATEGORY_ARRAY):
            if (len(data_type.getImplementationDataTypeElements()) < 1):
                self._raiseError("Array Sub-Element of <%s> do not defined." % data_type.short_name)
            array_sub_element = data_type.getImplementationDataTypeElements()[0]
            if (array_sub_element.category == ImplementationDataType.CATEGORY_TYPE_REFERENCE):
                data_type.setArrayElementType(array_sub_element.sw_data_def_props.implementation_data_type_ref.value)
            elif (array_sub_element.category == ImplementationDataType.CATEGORY_TYPE_VALUE):  # TODO: fix 
                return
            else:
                self._raiseError("The category <%s> of array sub-element <%s> does not support." % (array_sub_element.category, data_type.short_name))

    def readBaseTypeDirectDefinition(self, element: ET.Element, parent: BaseType):
        parent.base_type_definition.base_type_size = int(self.getChildElementOptionalValue(element, "BASE-TYPE-SIZE"))
        parent.base_type_definition.base_type_encoding = self.getChildElementOptionalLiteral(element, "BASE-TYPE-ENCODING")
        parent.base_type_definition.native_declaration = self.getChildElementOptionalLiteral(element, "NATIVE-DECLARATION")

    def readSwBaseType(self, element: ET.Element, parent: ARPackage):
        short_name = self.getShortName(element)
        data_type = parent.createSwBaseType(short_name)
        self.readIdentifiable(element, data_type)
        self.readBaseTypeDirectDefinition(element, data_type)

    def getApplicationCompositeElementInPortInterfaceInstanceRef(self, element: ET.Element, key:str) -> ApplicationCompositeElementInPortInterfaceInstanceRef:
        child_element = element.find("./xmlns:%s" % key, self.nsmap)
        iref = None
        if child_element is not None:
            iref = ApplicationCompositeElementInPortInterfaceInstanceRef()
            iref.root_data_prototype_ref = self.getChildElementOptionalRefType(child_element, "ROOT-DATA-PROTOTYPE-REF")
            iref.target_data_prototype_ref = self.getChildElementOptionalRefType(child_element, "TARGET-DATA-PROTOTYPE-REF")
        return iref

    def getCompositeNetworkRepresentation(self, element: ET.Element) -> CompositeNetworkRepresentation:
        self.logger.debug("getCompositeNetworkRepresentation")
        representation = CompositeNetworkRepresentation()
        representation.leaf_element_iref = self.getApplicationCompositeElementInPortInterfaceInstanceRef(element, "LEAF-ELEMENT-IREF")
        representation.network_representation = self.getSwDataDefProps(element, "NETWORK-REPRESENTATION")
        return representation

    def readReceiverComSpec(self, element, com_spec: ReceiverComSpec):
        self.readElementAttributes(element, com_spec)
        for child_element in element.findall("./xmlns:COMPOSITE-NETWORK-REPRESENTATIONS/xmlns:COMPOSITE-NETWORK-REPRESENTATION", self.nsmap):
            com_spec.addCompositeNetworkRepresentation(self.getCompositeNetworkRepresentation(child_element))
        com_spec.data_element_ref = self.getChildElementOptionalRefType(element, "DATA-ELEMENT-REF")
        com_spec.network_representation = self.getSwDataDefProps(element, "NETWORK-REPRESENTATION")
        com_spec.handle_out_of_range = self.getChildElementOptionalValue(element, "HANDLE-OUT-OF-RANGE")
        com_spec.uses_end_to_end_protection = self.getChildElementOptionalBooleanValue(element, "USES-END-TO-END-PROTECTION")

    def readSwValues(self, element: ET.Element, key: str) -> SwValues:
        child_element = element.find("./xmlns:%s" % key, self.nsmap) # type: ET.Element
        if child_element is None:
            return None
        values = SwValues()
        v_element = child_element.find("./xmlns:V", self.nsmap)
        if v_element is not None:
            values.v = v_element.text
            self.logger.debug("readSwValues - V: %s" % values.v)
        return values

    def getSwValueCont(self, element: ET.Element) -> SwValueCont:
        cont = None
        child_element = element.find("./xmlns:SW-VALUE-CONT", self.nsmap)
        if child_element is not None:
            cont = SwValueCont()
            cont.unit_ref = self.getChildElementOptionalRefType(child_element, "UNIT-REF")
            cont.sw_values_phys = self.readSwValues(child_element, "SW-VALUES-PHYS")

            self.logger.debug("getSwValueCont - Unit: %s" % cont.unit_ref.value)
        return cont
    
    def readValueSpecification(self, element: ET.Element, value_spec: ValueSpecification):
        value_spec.short_label = self.getChildElementOptionalValue(element, "SHORT-LABEL")
        self.readElementAttributes(element, value_spec)
        self.logger.debug("readValueSpecification")

    def readApplicationValueSpecification(self, element: ET.Element, value_spec: ApplicationValueSpecification):
        self.readValueSpecification(element, value_spec)
        value_spec.category = self.getChildElementOptionalValue(element, "CATEGORY")
        value_spec.sw_value_cont = self.getSwValueCont(element)

        self.logger.debug("readApplicationValueSpecification Category %s" % value_spec.category)

    def getInitValue(self, element: ET.Element) -> ValueSpecification:
        value_spec = None
        child_element = element.find("./xmlns:INIT-VALUE/*", self.nsmap)
        if child_element is not None:
            self.logger.debug("getInitValue")
            value_spec = self.getValueSpecification(child_element)
        return value_spec
    
    def getClientComSpec(self, element: ET.Element) -> ClientComSpec:
        com_spec = ClientComSpec()
        self.readElementAttributes(element, com_spec)
        com_spec.operation_ref = self.getChildElementOptionalRefType(element, "OPERATION-REF")
        return com_spec
    
    def getQueuedReceiverComSpec(self, element: ET.Element) -> QueuedReceiverComSpec:
        com_spec = QueuedReceiverComSpec()
        self.readElementAttributes(element, com_spec)
        self.readReceiverComSpec(element, com_spec)
        com_spec.queue_length = self.getChildElementOptionalNumberValue(element, "QUEUE-LENGTH")
        return com_spec

    def getNonqueuedReceiverComSpec(self, element: ET.Element) -> NonqueuedReceiverComSpec:
        com_spec = NonqueuedReceiverComSpec()
        self.readElementAttributes(element, com_spec)            
        self.readReceiverComSpec(element, com_spec)
        com_spec.alive_timeout = self.getChildElementOptionalFloatValue(element, "ALIVE-TIMEOUT")
        com_spec.enable_updated = self.getChildElementOptionalBooleanValue(element, "ENABLE-UPDATE")
        com_spec.handle_never_received = self.getChildElementOptionalBooleanValue(element, "HANDLE-NEVER-RECEIVED")
        com_spec.handel_timeout_type = self.getChildElementOptionalValue(element, "HANDLE-TIMEOUT-TYPE")
        com_spec.init_value = self.getInitValue(element)
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
            else:
                raise NotImplementedError("Unsupported RequiredComSpec <%s>" % tag_name)

    def readRPortPrototype(self, element: ET.Element, parent: AtomicSwComponentType):
        for child_element in element.findall("./xmlns:PORTS/xmlns:R-PORT-PROTOTYPE", self.nsmap):
            short_name = self.getShortName(child_element)
            self.logger.debug("readRPortPrototype %s" % short_name)

            prototype = parent.createRPortPrototype(short_name)
            self.readElementAttributes(child_element, prototype)
            prototype.required_interface_tref = self.getChildElementOptionalRefType(child_element, "REQUIRED-INTERFACE-TREF")

            self.readRequiredComSpec(child_element, prototype)

    def readTransmissionAcknowledgementRequest(self, element: ET.Element) -> TransmissionAcknowledgementRequest:
        child_element = element.find("./xmlns:TRANSMISSION-ACKNOWLEDGE", self.nsmap)
        if (child_element != None):
            acknowledge = TransmissionAcknowledgementRequest()
            self.readElementAttributes(child_element, acknowledge)
            acknowledge.timeout = self.getChildElementOptionalFloatValue(child_element, "TIMEOUT")
            return acknowledge
        return None

    def readSenderComSpec(self, element:ET.Element, com_spec: SenderComSpec):
        self.readElementAttributes(element, com_spec)
        for child_element in element.findall("./xmlns:COMPOSITE-NETWORK-REPRESENTATIONS/xmlns:COMPOSITE-NETWORK-REPRESENTATION", self.nsmap):
            com_spec.addCompositeNetworkRepresentation(self.getCompositeNetworkRepresentation(child_element))
        com_spec.data_element_ref = self.getChildElementOptionalRefType(element, "DATA-ELEMENT-REF")
        com_spec.network_representation = self.getSwDataDefProps(element, "NETWORK-REPRESENTATION")
        com_spec.handle_out_of_range = self.getChildElementOptionalValue(element, "HANDLE-OUT-OF-RANGE")
        com_spec.transmission_acknowledge = self.readTransmissionAcknowledgementRequest(element)
        com_spec.uses_end_to_end_protection = self.getChildElementOptionalBooleanValue(element, "USES-END-TO-END-PROTECTION")

    def getNonqueuedSenderComSpec(self, element) -> NonqueuedSenderComSpec:
        com_spec = NonqueuedSenderComSpec()
        self.readSenderComSpec(element, com_spec)
        com_spec.init_value = self.getInitValue(element)
        return com_spec
    
    def getServerComSpec(self, element) -> ServerComSpec:
        com_spec = ServerComSpec()
        self.readSenderComSpec(element, com_spec)
        com_spec.operation_ref = self.getChildElementOptionalRefType(element, "OPERATION-REF")
        com_spec.queue_length = self.getChildElementOptionalNumberValue(element, "QUEUE-LENGTH")
        return com_spec

    def readProvidedComSpec(self, element: ET.Element, parent: PPortPrototype):
        for child_element in element.findall("./xmlns:PROVIDED-COM-SPECS/*", self.nsmap):
            tag_name = self.getTagName(child_element.tag)
            if tag_name == "NONQUEUED-SENDER-COM-SPEC":
                parent.addProvidedComSpec(self.getNonqueuedSenderComSpec(child_element))
            elif tag_name == "SERVER-COM-SPEC":
                parent.addProvidedComSpec(self.getServerComSpec(child_element))
            else:
                raise NotImplementedError("Unsupported RequiredComSpec <%s>" % tag_name)

    def readPPortPrototype(self, element: ET.Element, parent: AtomicSwComponentType):
        for child_element in element.findall("./xmlns:PORTS/xmlns:P-PORT-PROTOTYPE", self.nsmap):
            short_name = self.getShortName(child_element)
            self.logger.debug("readPPortPrototype %s" % short_name)
            prototype = parent.createPPortPrototype(short_name)
            self.readIdentifiable(child_element, prototype)
            prototype.provided_interface_tref = self.getChildElementOptionalRefType(child_element, "PROVIDED-INTERFACE-TREF")

            self.readProvidedComSpec(child_element, prototype)

    def readPortGroupInnerGroupIRefs(self, element: ET.Element, parent: PortGroup):
        for child_element in element.findall("./xmlns:INNER-GROUP-IREFS/xmlns:INNER-GROUP-IREF", self.nsmap):
            inner_group_iref = InnerPortGroupInCompositionInstanceRef()
            inner_group_iref.contextRef = self.getChildElementOptionalRefType(child_element, "CONTEXT-REF")
            inner_group_iref.targetRef = self.getChildElementOptionalRefType(child_element, "TARGET-REF")
            parent.addInnerGroupIRef(inner_group_iref)

    def readPortGroup(self, element: ET.Element, parent: SwComponentType):
        short_name = self.getShortName(element)
        self.logger.debug("readPortGroup %s" % short_name)
        port_group = parent.createPortGroup(short_name)
        self.readIdentifiable(element, port_group)
        self.readPortGroupInnerGroupIRefs(element, port_group)

    def readSwComponentTypePortGroups(self, element: ET.Element, parent: SwComponentType):
        for child_element in element.findall("./xmlns:PORT-GROUPS/*", self.nsmap):
            tag_name = self.getTagName(child_element.tag)
            if tag_name == "PORT-GROUP":
                self.readPortGroup(child_element, parent)
            else:
                self._raiseError("Unsupported Port Group type: %s" % tag_name)

    def readSwComponentType(self, element: ET.Element, parent: SwComponentType):
        self.readIdentifiable(element, parent)
        self.readRPortPrototype(element, parent)
        self.readPPortPrototype(element, parent)
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
        for child_element in element.findall("./xmlns:ELEMENTS/xmlns:SENSOR-ACTUATOR-SW-COMPONENT-TYPE", self.nsmap):
            short_name = self.getShortName(child_element)
            sw_component = parent.createSensorActuatorSwComponentType(short_name)
            self.readAtomicSwComponentType(child_element, sw_component)

    def readServiceSwComponentTypes(self, element: ET.Element, parent: ARPackage):
        for child_element in element.findall("./xmlns:ELEMENTS/xmlns:SERVICE-SW-COMPONENT-TYPE", self.nsmap):
            short_name = self.getShortName(child_element)
            sw_component = parent.createServiceSwComponentType(short_name)
            self.readAtomicSwComponentType(child_element, sw_component)

    def readPPortInCompositionInstanceRef(self, element: ET.Element, p_port_in_composition_instance_ref: PPortInCompositionInstanceRef):
        p_port_in_composition_instance_ref.context_component_ref = self.getChildElementOptionalRefType(element, "CONTEXT-COMPONENT-REF")
        p_port_in_composition_instance_ref.target_p_port_ref = self.getChildElementOptionalRefType(element, "TARGET-P-PORT-REF")
        
        self.logger.debug("PPortInCompositionInstanceRef")
        self.logger.debug("  CONTEXT-COMPONENT-REF DEST: %s, %s"
                          % (p_port_in_composition_instance_ref.context_component_ref.dest, p_port_in_composition_instance_ref.context_component_ref.value))
        self.logger.debug("  TARGET-P-PORT-REF DEST: %s, %s" 
                          % (p_port_in_composition_instance_ref.target_p_port_ref.dest, p_port_in_composition_instance_ref.target_p_port_ref.value))

    def readRPortInCompositionInstanceRef(self, element, r_port_in_composition_instance_ref: RPortInCompositionInstanceRef):
        r_port_in_composition_instance_ref.context_component_ref = self.getChildElementOptionalRefType(element, "CONTEXT-COMPONENT-REF")
        r_port_in_composition_instance_ref.target_r_port_ref = self.getChildElementOptionalRefType(element, "TARGET-R-PORT-REF")

        self.logger.debug("RPortInCompositionInstanceRef")
        self.logger.debug("  CONTEXT-COMPONENT-REF DEST: %s, %s"
                          % (r_port_in_composition_instance_ref.context_component_ref.dest, r_port_in_composition_instance_ref.context_component_ref.value))
        self.logger.debug("  TARGET-P-PORT-REF DEST: %s, %s" 
                          % (r_port_in_composition_instance_ref.target_r_port_ref.dest, r_port_in_composition_instance_ref.target_r_port_ref.value))

    def readAssemblySwConnectorProviderIRef(self, element: ET.Element, parent: AssemblySwConnector):
        child_element = element.find("./xmlns:PROVIDER-IREF", self.nsmap)
        if (child_element != None):
            provide_iref = PPortInCompositionInstanceRef()
            self.readElementAttributes(child_element, provide_iref)
            self.readPPortInCompositionInstanceRef(child_element, provide_iref)
            parent.provider_iref = provide_iref

    def readAssemblySwConnectorRequesterIRef(self, element: ET.Element, parent: AssemblySwConnector):
        child_element = element.find("./xmlns:REQUESTER-IREF", self.nsmap)
        if (child_element != None):
            requester_iref = RPortInCompositionInstanceRef()
            self.readElementAttributes(child_element, requester_iref)
            self.readRPortInCompositionInstanceRef(child_element, requester_iref)
            parent.requester_iref = requester_iref

    def readAssemblySwConnectors(self, element: ET.Element, parent: CompositionSwComponentType):
        for child_element in element.findall("./xmlns:CONNECTORS/xmlns:ASSEMBLY-SW-CONNECTOR", self.nsmap):
            short_name = self.getShortName(child_element)
            self.logger.debug("readAssemblySwConnectors %s" % short_name)

            connector = parent.createAssemblySwConnector(short_name)
            self.readIdentifiable(child_element, connector)
            self.readAssemblySwConnectorProviderIRef(child_element, connector)
            self.readAssemblySwConnectorRequesterIRef(child_element, connector)

    def readDelegationSwConnectorInnerPortIRef(self, element, parent: DelegationSwConnector):
        inner_port_iref_element = element.find("./xmlns:INNER-PORT-IREF", self.nsmap)
        if (inner_port_iref_element != None):
            child_element = inner_port_iref_element.find("./xmlns:R-PORT-IN-COMPOSITION-INSTANCE-REF", self.nsmap)
            if (child_element != None):
                r_port_in_composition_instance_ref = RPortInCompositionInstanceRef()
                self.readRPortInCompositionInstanceRef(child_element, r_port_in_composition_instance_ref)
                parent.inner_port_iref = r_port_in_composition_instance_ref
                return
            
            child_element = inner_port_iref_element.find("./xmlns:P-PORT-IN-COMPOSITION-INSTANCE-REF", self.nsmap)
            if (child_element != None):
                p_port_in_composition_instance_ref = PPortInCompositionInstanceRef()
                self.readPPortInCompositionInstanceRef(child_element, p_port_in_composition_instance_ref)
                parent.inner_port_iref = p_port_in_composition_instance_ref
                return
            
            self._raiseError("Unsupported child element of INNER-PORT-IREF")

    def readDelegationSwConnectors(self, element, parent: CompositionSwComponentType):
        for child_element in element.findall("./xmlns:CONNECTORS/xmlns:DELEGATION-SW-CONNECTOR", self.nsmap):
            short_name = self.getShortName(child_element)
            self.logger.debug("readDelegationSwConnectors %s" % short_name)

            connector = parent.createDelegationSwConnector(short_name)
            self.readIdentifiable(child_element, connector)
            self.readDelegationSwConnectorInnerPortIRef(child_element, connector)

            if connector.inner_port_iref == None and connector.outer_port_iref == None:
                self._raiseError("Invalid PortPrototype of DELEGATION-SW-CONNECTOR")

            connector.outer_port_ref = self.getChildElementOptionalRefType(child_element, "OUTER-PORT-REF")
            self.logger.debug("OUTER-PORT-REF DEST: %s, %s"
                          % (connector.outer_port_ref.dest, connector.outer_port_ref.value))

    def readSwComponentPrototypes(self, element: ET.Element, parent: CompositionSwComponentType):
        for child_element in element.findall("./xmlns:COMPONENTS/xmlns:SW-COMPONENT-PROTOTYPE", self.nsmap):
            short_name = self.getShortName(child_element)
            self.logger.debug("readSwComponentPrototypes %s" % short_name)
            prototype = parent.createSwComponentPrototype(short_name)
            self.readIdentifiable(child_element, prototype)
            prototype.type_tref = self.getChildElementOptionalRefType(child_element, "TYPE-TREF")

    def readDataTypeMappingSet(self, element: ET.Element, parent: CompositionSwComponentType):
        child_element = element.find("./xmlns:DATA-TYPE-MAPPING-REFS", self.nsmap)
        self.logger.debug("readDataTypeMappingSet")
        if child_element != None:
            for ref in self.getChildElementRefTypeList(child_element, "DATA-TYPE-MAPPING-REF"):
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
        self.readDataTypeMappingSet(element, sw_component)

        self.logger.debug("ReadCompositionSwComponentTypes: <%s> (Done)" % short_name)

    def readDataTypeMap(self, element: ET.Element, parent: DataTypeMappingSet):
        for child_element in element.findall("./xmlns:DATA-TYPE-MAPS/xmlns:DATA-TYPE-MAP", self.nsmap):
            data_type_map = DataTypeMap()
            data_type_map.application_data_type_ref = self.getChildElementOptionalRefType(child_element, "APPLICATION-DATA-TYPE-REF")
            data_type_map.implementation_data_type_ref = self.getChildElementOptionalRefType(child_element, "IMPLEMENTATION-DATA-TYPE-REF")
            parent.addDataTypeMap(data_type_map)
            # add the data type map to global namespace
            AUTOSAR.getInstance().addDataTypeMap(data_type_map)

    def readDataTypeMappingSets(self, element: ET.Element, parent: ARPackage):
        for child_element in element.findall("./xmlns:ELEMENTS/xmlns:DATA-TYPE-MAPPING-SET", self.nsmap):
            short_name = self.getShortName(child_element)
            mapping_set = parent.createDataTypeMappingSet(short_name)
            self.readDataTypeMap(child_element, mapping_set)

    def readDataElements(self, element: ET.Element, parent: SenderReceiverInterface):
        for child_element in element.findall("./xmlns:DATA-ELEMENTS/xmlns:VARIABLE-DATA-PROTOTYPE", self.nsmap):
            short_name = self.getShortName(child_element)
            prototype = parent.createDataElement(short_name)
            prototype.sw_data_def_props = self.getSwDataDefProps(child_element, "SW-DATA-DEF-PROPS")
            self.readAutosarDataPrototype(child_element, prototype)
            prototype.init_value = self.getInitValue(child_element)

    def readSenderReceiverInterfaces(self, element, parent: ARPackage):
        short_name = self.getShortName(element)
        sr_interface = parent.createSenderReceiverInterface(short_name)
        self.readIdentifiable(element, sr_interface)
        sr_interface.is_service = self.getChildElementOptionalBooleanValue(element, "IS-SERVICE")
        self.readDataElements(element, sr_interface)

    def readArgumentDataPrototypes(self, element: ET.Element, parent: ClientServerOperation):
        for child_element in element.findall("./xmlns:ARGUMENTS/xmlns:ARGUMENT-DATA-PROTOTYPE", self.nsmap):
            short_name = self.getShortName(child_element)
            prototype = ArgumentDataPrototype(property, short_name)
            prototype.type_tref = self.getChildElementOptionalRefType(child_element, "TYPE-TREF")
            prototype.direction = self.getChildElement(short_name, child_element, "DIRECTION")
            parent.addArgumentDataPrototype(prototype)

    def readPossibleErrorRefs(self, element: ET.Element, parent: ClientServerOperation):
        child_element = element.find("./xmlns:POSSIBLE-ERROR-REFS", self.nsmap)
        if child_element != None:
            for ref in self.getChildElementRefTypeList(child_element, "POSSIBLE-ERROR-REF"):
                parent.addPossibleErrorRef(ref)

    def readOperations(self, element: ET.Element, parent: ClientServerInterface):
        for child_element in element.findall("./xmlns:OPERATIONS/xmlns:CLIENT-SERVER-OPERATION", self.nsmap):
            short_name = self.getShortName(child_element)
            operation = parent.createOperation(short_name)
            self.readArgumentDataPrototypes(child_element, operation)
            self.readPossibleErrorRefs(child_element, operation)

    def readPossibleErrors(self, element: ET.Element, parent: ClientServerInterface):
        for child_element in element.findall("./xmlns:POSSIBLE-ERRORS/xmlns:APPLICATION-ERROR", self.nsmap):
            short_name = self.getShortName(child_element)
            error = parent.createApplicationError(short_name)
            error.error_code = self.getChildElementNumberValue(short_name, child_element, "ERROR-CODE")

    def readClientServerInterface(self, element: ET.Element, parent: ARPackage):
        short_name = self.getShortName(element)
        cs_interface = parent.createClientServerInterface(short_name)
        cs_interface.is_service = self.getChildElementOptionalBooleanValue(element, "IS-SERVICE")
        self.readOperations(element, cs_interface)
        self.readPossibleErrors(element, cs_interface)

    def readCompuConst(self, element: ET.Element, parent: CompuScale):
        child_element = element.find("./xmlns:COMPU-CONST/xmlns:VT", self.nsmap)
        if (child_element is not None):
            self.logger.debug("readCompuConst VT: %s" % child_element.text)
            contents = CompuScaleConstantContents()
            contents.compu_const = CompuConst()
            contents.compu_const.compu_const_content_type = CompuConstTextContent()
            contents.compu_const.compu_const_content_type.vt = child_element.text
            parent.compu_scale_contents = contents

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
            parent.compu_scale_contents = contents

    def readCompuScaleContents(self, element: ET.Element, parent: CompuScale):
        self.readCompuConst(element, parent)
        self.readCompuRationCoeffs(element, parent)

    def readCompuScales(self, element: ET.Element, parent: CompuScales):
        for child_element in element.findall('./xmlns:COMPU-SCALES/xmlns:COMPU-SCALE', self.nsmap):
            compu_scale = CompuScale()
            compu_scale.lower_limit = self.getChildLimitElement(child_element, "LOWER-LIMIT")
            compu_scale.upper_limit = self.getChildLimitElement(child_element, "UPPER-LIMIT")
            self.readCompuScaleContents(child_element, compu_scale)
            parent.addCompuScale(compu_scale)

    def readCompuInternalToPhys(self, element: ET.Element, parent: CompuMethod):
        child_element = element.find("./xmlns:COMPU-INTERNAL-TO-PHYS", self.nsmap)
        if (child_element != None):
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
            mapping.bsw_entity_ref = self.getChildElementOptionalRefType(child_element, "BSW-ENTITY-REF")
            mapping.swc_runnable_ref = self.getChildElementOptionalRefType(child_element, "SWC-RUNNABLE-REF")
            parent.addRunnableMapping(mapping)

    def readSwcBswMappings(self, element: ET.Element, parent: ARPackage):
        short_name = self.getShortName(element)
        self.logger.debug("readSwcBswMappings %s" % short_name)
        swc_bsw_mapping = parent.createSwcBswMapping(short_name)
        swc_bsw_mapping.bsw_behavior_ref = self.getChildElementOptionalRefType(element, "BSW-BEHAVIOR-REF")
        self.readSwcBswRunnableMappings(element, swc_bsw_mapping)
        swc_bsw_mapping.swc_behavior_ref = self.getChildElementOptionalRefType(element, "SWC-BEHAVIOR-REF")

    def readValueSpecification(self, element: ET.Element, value_spec: ValueSpecification):
        value_spec.short_label = self.getChildElementOptionalValue(element, "SHORT-LABEL")

    def readSwValueCont(self, element: ET.Element, spec: ApplicationValueSpecification):
        child_element = element.find("./xmlns:SW-VALUE-CONT", self.nsmap)
        if child_element is not None:
            sw_value_cont = SwValueCont()
            sw_value_cont.unit_ref = self.getChildElementOptionalRefType(child_element, "UNIT-REF")
            sw_value_cont.sw_values_phys = self.readSwValues(child_element, "SW-VALUES-PHYS")
            spec.sw_value_cont = sw_value_cont

    def getApplicationValueSpecification(self, element: ET.Element) -> ApplicationValueSpecification:
        value_spec = ApplicationValueSpecification()
        self.readValueSpecification(element, value_spec)
        value_spec.category = self.getChildElementOptionalValue(element, "CATEGORY")
        self.readSwValueCont(element, value_spec)
        return value_spec
    
    def getNumericalValueSpecification(self, element: ET.Element) -> NumericalValueSpecification:
        value_spec = NumericalValueSpecification()
        self.readValueSpecification(element, value_spec)
        value_spec.value = self.getChildElementOptionalNumberValue(element, "VALUE")
        return value_spec
    
    def getTextValueSpecification(self, element: ET.Element) -> TextValueSpecification:
        value_spec = TextValueSpecification()
        self.readValueSpecification(element, value_spec)
        value_spec.value = self.getChildElementOptionalValue(element, "VALUE")
        self.logger.debug("readTextValueSpecification Value: %s" % value_spec.value)
        return value_spec

    def getArrayValueSpecification(self, element: ET.Element) -> ArrayValueSpecification:
        value_spec = ArrayValueSpecification()
        self.readValueSpecification(element, value_spec)
        child_elements = element.findall("./xmlns:ELEMENTS/*", self.nsmap)
        for child_element in child_elements:
            value_spec.add_element(self.getValueSpecification(child_element))
        return value_spec

    def getConstantReference(self, element: ET.Element) -> ConstantReference:
        value_spec = ConstantReference()
        self.readValueSpecification(element, value_spec)
        value_spec.constant_ref = self.getChildElementOptionalRefType(element, "CONSTANT-REF")
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
            spec.add_field(self.getValueSpecification(child_element))

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
        for value_spec_tag in element.findall("./xmlns:VALUE-SPEC/*", self.nsmap):
            spec.value_spec = self.getValueSpecification(value_spec_tag)
                
    def readInternalConstrs(self, element: ET.Element, parent: DataConstrRule):
        child_element = element.find("./xmlns:INTERNAL-CONSTRS", self.nsmap)
        if child_element is not None:
            constrs = InternalConstrs()
            self.readElementAttributes(child_element, constrs)
            constrs.lower_limit = self.getChildLimitElement(child_element, "LOWER-LIMIT")
            constrs.upper_limit = self.getChildLimitElement(child_element, "UPPER-LIMIT")
            parent.internal_constrs = constrs

    def readPhysConstrs(self, element: ET.Element, parent: DataConstrRule):
        child_element = element.find("./xmlns:PHYS-CONSTRS", self.nsmap)
        if child_element is not None:
            constrs = PhysConstrs()
            self.readElementAttributes(child_element, constrs)
            constrs.lower_limit = self.getChildLimitElement(child_element, "LOWER-LIMIT")
            constrs.upper_limit = self.getChildLimitElement(child_element, "UPPER-LIMIT")
            constrs.unit_ref = self.getChildElementOptionalRefType(child_element, "UNIT-REF")
            parent.phys_constrs = constrs
                
    def readDataConstrRule(self, element: ET.Element, parent: DataConstr):
        for child_element in element.findall("./xmlns:DATA-CONSTR-RULES/xmlns:DATA-CONSTR-RULE", self.nsmap):
            self.logger.debug("readDataConstrRule")
            rule = DataConstrRule()
            self.readElementAttributes(child_element, rule)
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
        unit.display_name = self.getChildElementOptionalLiteral(element, "DISPLAY-NAME")

    def readEndToEndDescriptionDataId(self, element: ET.Element, parent: EndToEndDescription):
        for child_element in element.findall("./xmlns:DATA-IDS:", self.nsmap):
            parent.addDataId(self.getChildElementOptionalNumberValue(child_element, "DATA-ID"))

    def getEndToEndDescription(self, element: ET.Element, key: str) -> EndToEndDescription:
        child_element = element.find("./xmlns:%s" % key, self.nsmap)
        desc = None
        if (child_element is not None):
            desc = EndToEndDescription()
            desc.category = self.getChildElementOptionalValue(child_element, "CATEGORY")
            self.readEndToEndDescriptionDataId(child_element, desc)
        return desc

    def readEndToEndProtection(self, element: ET.Element, parent: EndToEndProtectionSet):
        short_name = self.getShortName(element)
        self.logger.debug("readEndToEndProtection %s" % short_name)
        protection = parent.createEndToEndProtection(short_name)
        self.readIdentifiable(element, protection)
        protection.endToEndProfile = self.getEndToEndDescription(element, "END-TO-END-PROFILE")

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

    def readARPackageElements(self, element: ET.Element, parent: ARPackage):
        for child_element in element.findall("./xmlns:ELEMENTS/*", self.nsmap):
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
            else:
                raise NotImplementedError("Unsupported element type of ARPackage <%s>" % tag_name)
                #pass

    def getAUTOSARInfo(self, element: ET.Element, document: AUTOSAR):
        key = "{http://www.w3.org/2001/XMLSchema-instance}schemaLocation"
        if key in element.attrib:
            document.schema_location = element.attrib[key]
        
        self.logger.debug("schemaLocation %s" % document.schema_location)

    def readARPackages(self, element: ET.Element, parent: ARPackage):
        for child_element in element.findall("./xmlns:AR-PACKAGES/xmlns:AR-PACKAGE", self.nsmap):
            short_name = self.getShortName(child_element)
            ar_package = parent.createARPackage(short_name)

            self.logger.debug("readARPackages %s" % ar_package.full_name)

            self.readElementAttributes(child_element, ar_package)
            self.readARPackageElements(child_element, ar_package)
            self.readARPackages(child_element, ar_package)


    def load(self, filename, document: AUTOSAR):
        self.logger.info("Load %s ..." % filename)

        tree = ET.parse(filename)
        root = tree.getroot()
        if (self.getPureTagName(root.tag) != "AUTOSAR"):
            self._raiseError("Invalid ARXML file <%s>" % filename)

        self.getAUTOSARInfo(root, document)
        self.readARPackages(root, document)
