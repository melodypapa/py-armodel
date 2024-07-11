from ..models.unit import Unit
from ..models.global_constraints import InternalConstrs, DataConstr, DataConstrRule, PhysConstrs

from ..models import AUTOSAR, ARPackage, ARObject, EcuAbstractionSwComponentType, AtomicSwComponentType, SwComponentType, CompositionSwComponentType
from ..models import SwcInternalBehavior, RunnableEntity, RTEEvent, VariableAccess, ServerCallPoint, OperationInvokedEvent, DataReceivedEvent, RVariableInAtomicSwcInstanceRef
from ..models import SwcModeSwitchEvent, RModeInAtomicSwcInstanceRef
from ..models import RefType, AutosarVariableRef, ArVariableInImplementationDataInstanceRef, POperationInAtomicSwcInstanceRef, ROperationInAtomicSwcInstanceRef
from ..models import ImplementationDataType, SwDataDefProps, SwPointerTargetProps, DataTypeMappingSet, DataTypeMap, ImplementationDataTypeElement
from ..models import DataPrototype, RPortPrototype, PPortPrototype
from ..models import ReceiverComSpec, ClientComSpec, NonqueuedReceiverComSpec, QueuedReceiverComSpec
from ..models import SenderComSpec, NonqueuedSenderComSpec
from ..models import SenderReceiverInterface, ClientServerInterface, ClientServerOperation, ArgumentDataPrototype
from ..models import AutosarDataType, ARElement, Identifiable, AdminData, Sdg, Sd, MultilanguageReferrable, Referrable, LLongName, MultilanguageLongName
from ..models import AssemblySwConnector, PPortInCompositionInstanceRef, RPortInCompositionInstanceRef
from ..models import DelegationSwConnector
from ..models import CompuMethod, CompuScale, Limit, CompuScales, Compu, CompuConst, CompuConstTextContent, CompuScaleConstantContents, CompuScaleRationalFormula, CompuRationalCoeffs, CompuNominatorDenominator
from ..models import InternalBehavior, ExecutableEntity
from ..models import Implementation, Code, AutosarEngineeringObject, ResourceConsumption
from ..models import TransmissionAcknowledgementRequest
from ..models import BswImplementation, BswModuleDescription, BswInternalBehavior, BswCalledEntity, BswModuleEntity, BswScheduleEvent, SwcBswMapping, SwcBswRunnableMapping
from ..models import ValueSpecification, ApplicationValueSpecification, TextValueSpecification, NumericalValueSpecification, ArrayValueSpecification, ConstantReference
from ..models import ConstantSpecification, RecordValueSpecification
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

    def readChildElement(self, short_name: str, element: ET.Element, key: str) -> str:
        child_element = element.find("./xmlns:%s" % key, self.nsmap)
        if (child_element != None):
            return child_element.text
        self._raiseError("The attribute %s of <%s> has not been defined" % (key, short_name))

    def readChildOptionalElement(self, element: ET.Element, key: str) -> str:
        child_element = element.find("./xmlns:%s" % key, self.nsmap)
        if (child_element != None):
            return child_element.text
        return None
    
    def readChildElementLiteral(self, short_name: str, element: ET.Element, key: str) -> ARLiteral:
        child_element = element.find("./xmlns:%s" % key, self.nsmap)
        if (child_element != None):
            literal = ARLiteral()
            self.readElementAttributes(child_element, literal)
            literal.value = child_element.text
            return literal
        self._raiseError("The attribute %s of <%s> has not been defined" % (key, short_name))

    def readChildOptionalElementLiteral(self, element: ET.Element, key: str) -> ARLiteral:
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
    
    def readChildElementFloatValue(self, short_name: str, element: ET.Element, key: str) -> float:
        value = self.readChildElement(short_name, element, key)
        if (value == None):
            return None
        return float(value)

    def readChildElementBooleanValue(self, short_name: str, element: ET.Element, key: str) -> ARBoolean:
        literal = self.readChildElementLiteral(short_name, element, key)
        bool_value = ARBoolean()
        bool_value.timestamp = literal.timestamp
        bool_value.value = self._convertStringToBooleanValue(literal.value)
        return bool_value

    def readChildOptionalElementBooleanValue(self, element: ET.Element, key: str) -> ARBoolean:
        literal = self.readChildOptionalElementLiteral(element, key)
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

    def readChildElementNumberValue(self, short_name: str, element: ET.Element, key: str) -> int:
        value = self.readChildElement(short_name, element, key)
        return self._convertStringToNumberValue(value)

    def readChildOptionalElementNumberValue(self, element: ET.Element, key: str) -> int:
        value = self.readChildOptionalElement(element, key)
        if (value == None):
            return None
        return self._convertStringToNumberValue(value)
    
    def readChildLimitElement(self, element: ET.Element, key: str) -> Limit:
        child_element = element.find("./xmlns:%s" % key, self.nsmap)
        if (child_element != None):
            limit = Limit()
            if ('INTERVAL-TYPE' in child_element.attrib):
                limit.interval_type = child_element.attrib['INTERVAL-TYPE']
            else:
                limit.interval_type = "CLOSED"
            limit.value = child_element.text
            return limit
        return None
    
    def readShortName(self, element: ET.Element) -> str:
        return self.readChildElement("", element, "SHORT-NAME")
    
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
        self.readMultilanguageReferrable(element, identifiable)
        identifiable.category = self.readChildOptionalElement(element, "CATEGORY")
        self.readAdminData(element, identifiable)

    def _readChildRefElementDestAndValue(self, element) -> RefType:
        ref = RefType()
        ref.dest = element.attrib['DEST']
        ref.value = element.text
        return ref

    def readChildRefElement(self, short_name: str, element: ET.Element, key: str) -> RefType:
        child_element = element.find("./xmlns:%s" % key, self.nsmap)
        if (child_element != None):
            return self._readChildRefElementDestAndValue(child_element)
        self._raiseError("The attribute %s of <%s> has not been defined" % (key, short_name))

    def readChildOptionalRefElement(self, element:ET.Element, key: str) -> RefType:
        child_element = element.find("./xmlns:%s" % key, self.nsmap)
        if (child_element != None):
            return self._readChildRefElementDestAndValue(child_element)
        return None

    def readChildRefElementList(self, element: ET.Element, key: str) -> List[RefType]:
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
    
    def readMultilanguageLongName(self, element: ET.Element, long_name: MultilanguageLongName):
        for child_element in element.findall("./xmlns:L-4", self.nsmap):
            l4 = LLongName()
            self.readElementAttributes(child_element, l4)
            l4.value = child_element.text
            if 'L' in child_element.attrib:
                l4.l = child_element.attrib['L']
            long_name.add_l4(l4)
    
    def readMultilanguageReferrable(self, element: ET.Element, referrable: MultilanguageReferrable):
        child_element = element.find("./xmlns:LONG-NAME", self.nsmap)
        if child_element is not None:
            referrable.long_name = MultilanguageLongName()
            self.readElementAttributes(child_element, referrable.long_name)
            self.readMultilanguageLongName(child_element, referrable.long_name)

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
            autosar_variable_in_impl_datatype = ArVariableInImplementationDataInstanceRef()
            autosar_variable_in_impl_datatype.port_prototype_ref = self.readChildOptionalRefElement(child_element, "PORT-PROTOTYPE-REF")
            if autosar_variable_in_impl_datatype.port_prototype_ref is None:
                self._raiseError("PORT-PROTOTYPE-REF of <%s> is empty." % accessed_variable_ref.parent.short_name)
            autosar_variable_in_impl_datatype.target_data_prototype_ref = self.readChildOptionalRefElement(child_element, "TARGET-DATA-PROTOTYPE-REF")
            if autosar_variable_in_impl_datatype.target_data_prototype_ref is None:
                self._raiseError("TARGET-DATA-PROTOTYPE-REF of <%s> is empty." % accessed_variable_ref.parent.short_name)
            accessed_variable_ref.autosar_variable_in_impl_datatype = autosar_variable_in_impl_datatype

    def readLocalVariableRef(self, element, accessed_variable_ref: AutosarVariableRef):
        child_element = element.find("./xmlns:ACCESSED-VARIABLE", self.nsmap)
        if (child_element != None):
            accessed_variable_ref.local_variable_ref = self.readChildOptionalRefElement(child_element, "LOCAL-VARIABLE-REF")

    def _readVariableAccesses(self, element: ET.Element, parent: RunnableEntity, key: str):
        for child_element in element.findall("./xmlns:%s/xmlns:VARIABLE-ACCESS" % key, self.nsmap):
            short_name = self.readShortName(child_element)

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
            ref = self.readChildOptionalRefElement(child_element, "BSW-MODULE-ENTRY-REF") 
            if (ref != None):
                parent.implemented_entry_refs.append(ref)
            self.logger.debug("ImplementedEntry <%s> of BswModuleDescription <%s> has been added", ref.value, parent.short_name)

    def readProvidedModeGroup(self, element: ET.Element, parent: BswModuleDescription):
        for child_element in element.findall("./xmlns:PROVIDED-MODE-GROUPS/xmlns:MODE-DECLARATION-GROUP-PROTOTYPE", self.nsmap):
            short_name = self.readShortName(child_element)
            self.logger.debug("readProvidedModeGroup %s" % short_name)

            mode_group = parent.createProvidedModeGroup(short_name)
            mode_group.type_tref = self.readChildRefElement(parent.short_name, child_element, "TYPE-TREF")

    def readRequiredModeGroup(self, element: ET.Element, parent: BswModuleDescription):
        for child_element in element.findall("./xmlns:REQUIRED-MODE-GROUPS/xmlns:MODE-DECLARATION-GROUP-PROTOTYPE", self.nsmap):
            short_name = self.readShortName(child_element)
            self.logger.debug("readRequiredModeGroup %s" % short_name)
            mode_group = parent.createProvidedModeGroup(short_name)
            mode_group.type_tref = self.readChildRefElement(parent.short_name, child_element, "TYPE-TREF")

    def readCanEnterExclusiveAreaRefs(self, element: ET.Element, entity: ExecutableEntity):
        child_element = element.find("./xmlns:CAN-ENTER-EXCLUSIVE-AREA-REFS", self.nsmap)
        if child_element != None:
            for ref in self.readChildRefElementList(child_element, "CAN-ENTER-EXCLUSIVE-AREA-REF"):
                entity.addCanEnterExclusiveAreaRef(ref)

    def readExecutableEntity(self, element: ET.Element, entity: ExecutableEntity):
        self.readCanEnterExclusiveAreaRefs(element, entity)

    def readBswModuleEntity(self, element, entity: BswModuleEntity):
        self.readExecutableEntity(element, entity)
        
        entity.implemented_entry_ref = self.readChildRefElement(entity.short_name, element, "IMPLEMENTED-ENTRY-REF")

    def readBswCalledEntity(self, element: ET.Element, parent: BswInternalBehavior):
        for child_element in element.findall("./xmlns:ENTITYS/xmlns:BSW-CALLED-ENTITY", self.nsmap):
            short_name = self.readShortName(child_element)
            self.logger.debug("readBswCalledEntity %s" % short_name)
            entity = parent.createBswCalledEntity(short_name)

            self.readBswModuleEntity(child_element, entity)

    def readBswSchedulableEntity(self, element: ET.Element, parent: BswInternalBehavior):
        for child_element in element.findall("./xmlns:ENTITYS/xmlns:BSW-SCHEDULABLE-ENTITY", self.nsmap):
            short_name = self.readShortName(child_element)
            self.logger.debug("readBswSchedulableEntity %s" % short_name)
            entity = parent.createBswSchedulableEntity(short_name)

            self.readBswModuleEntity(child_element, entity)

    def readBswEvent(self, element: ET.Element, event: BswScheduleEvent):
        event.starts_on_event_ref = self.readChildRefElement(event.short_name, element, "STARTS-ON-EVENT-REF")

    def readBswScheduleEvent(self, element, event: BswScheduleEvent):
        self.readBswEvent(element, event)

    def readBswModeSwitchEvent(self, element: ET.Element, parent: BswInternalBehavior):
        for child_element in element.findall("./xmlns:EVENTS/xmlns:BSW-MODE-SWITCH-EVENT", self.nsmap):
            short_name = self.readShortName(child_element)
            self.logger.debug("readBswModeSwitchEvent %s" % short_name)
            event = parent.createBswModeSwitchEvent(short_name)

            self.readBswScheduleEvent(child_element, event)

    def readBswTimingEvent(self, element: ET.Element, parent: BswInternalBehavior):
        for child_element in element.findall("./xmlns:EVENTS/xmlns:BSW-TIMING-EVENT", self.nsmap):
            short_name = self.readShortName(child_element)
            self.logger.debug("readBswTimingEvent %s" % short_name)
            event = parent.createBswTimingEvent(short_name)
            event.period = self.readChildElementFloatValue(short_name, child_element, "PERIOD")

            self.readBswScheduleEvent(child_element, event)

    def readBswDataReceivedEvent(self, element: ET.Element, parent: BswInternalBehavior):
        for child_element in element.findall("./xmlns:EVENTS/xmlns:BSW-DATA-RECEIVED-EVENT", self.nsmap):
            short_name = self.readShortName(child_element)
            self.logger.debug("readBswDataReceivedEvent %s" % short_name)
            event = parent.createBswDataReceivedEvent(short_name)
            event.data_ref = self.readChildRefElement(parent.short_name, child_element, "DATA-REF")

            self.readBswScheduleEvent(child_element, event)

    def readBswInternalTriggerOccurredEvent(self, element: ET.Element, parent: BswInternalBehavior):
        for child_element in element.findall("./xmlns:EVENTS/xmlns:BSW-INTERNAL-TRIGGER-OCCURRED-EVENT", self.nsmap):
            short_name = self.readShortName(child_element)
            self.logger.debug("readBswInternalTriggerOccurredEvent %s" % short_name)
            event = parent.createBswInternalTriggerOccurredEvent(short_name)
            event.event_source_ref = self.readChildRefElement(parent.short_name, child_element, "EVENT-SOURCE-REF")

            self.readBswScheduleEvent(child_element, event)

    def readDataTypeMappingRefs(self, element: ET.Element, behavior: InternalBehavior):
        child_element = element.find("./xmlns:DATA-TYPE-MAPPING-REFS", self.nsmap)
        if child_element != None:
            for ref in self.readChildRefElementList(child_element, "DATA-TYPE-MAPPING-REF"):
                behavior.addDataTypeMappingRef(ref)

    def readInternalBehavior(self, element: ET.Element, behavior: InternalBehavior):
        for child_element in element.findall("./xmlns:EXCLUSIVE-AREAS/xmlns:EXCLUSIVE-AREA", self.nsmap):
            short_name = self.readShortName(child_element)
            behavior.createExclusiveArea(short_name)

        self.readDataTypeMappingRefs(element, behavior)

    def readSwInternalBehavior(self, element: ET.Element, parent: AtomicSwComponentType):
        for child_element in element.findall("./xmlns:INTERNAL-BEHAVIORS/xmlns:SWC-INTERNAL-BEHAVIOR", self.nsmap):
            short_name = self.readShortName(child_element)
            behavior = parent.createSwcInternalBehavior(short_name)
            self.logger.debug("readSwInternalBehavior %s" % behavior.full_name)

            # read the internal behavior
            self.readInternalBehavior(child_element, behavior)

            self.readRunnableEntities(child_element, behavior)
            self.readOperationInvokedEvents(child_element, behavior)
            self.readTimingEvents(child_element, behavior)
            self.readInternalTriggerOccurredEvent(child_element, behavior)
            self.readExplicitInterRunnableVariables(child_element, behavior)

    def readBswInternalBehavior(self, element: ET.Element, parent: BswModuleDescription):
        for child_element in element.findall("./xmlns:INTERNAL-BEHAVIORS/xmlns:BSW-INTERNAL-BEHAVIOR", self.nsmap):
            short_name = self.readShortName(child_element)
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
        for child_element in element.findall("./xmlns:ELEMENTS/xmlns:BSW-MODULE-DESCRIPTION", self.nsmap):
            short_name = self.readShortName(child_element)
            bsw_module_description = parent.createBswModuleDescription(short_name)
            bsw_module_description.module_id = self.readChildElementNumberValue(short_name, child_element, "MODULE-ID")

            self.logger.debug("readBswModuleDescription %s" % bsw_module_description.full_name)

            self.readBswModuleDescriptionImplementedEntry(child_element, bsw_module_description)
            self.readProvidedModeGroup(child_element, bsw_module_description)
            self.readRequiredModeGroup(child_element, bsw_module_description)
            self.readBswInternalBehavior(child_element, bsw_module_description)

    def readBswModuleEntry(self, element: ET.Element, parent: ARPackage):
        for child_element in element.findall("./xmlns:ELEMENTS/xmlns:BSW-MODULE-ENTRY", self.nsmap):
            short_name = self.readShortName(child_element)
            entry = parent.createBswModuleEntry(short_name)
            entry.is_reentrant = self.readChildOptionalElementBooleanValue(child_element, "IS-REENTRANT")
            entry.is_synchronous = self.readChildOptionalElementBooleanValue(child_element, "IS-SYNCHRONOUS")
            entry.service_id = self.readChildOptionalElementNumberValue(child_element, "SERVICE-ID")
            entry.call_type = self.readChildOptionalElement(child_element, "CALL-TYPE")
            entry.execution_context = self.readChildOptionalElement(child_element, "EXECUTION-CONTEXT")
            entry.sw_service_impl_policy = self.readChildOptionalElement(child_element, "SW-SERVICE-IMPL-POLICY")

            #self.logger.debug("readBswModuleEntry \n%s" % entry)
            self.logger.debug("readBswModuleEntry %s" % entry.short_name)

    def readArtifactDescriptor(self, element: ET.Element, code_desc: Code):
        for child_element in element.findall("./xmlns:ARTIFACT-DESCRIPTORS/xmlns:AUTOSAR-ENGINEERING-OBJECT", self.nsmap):
            artifact_desc = AutosarEngineeringObject()
            artifact_desc.short_label = self.readChildElement(code_desc.short_name, child_element, "SHORT-LABEL")
            self.readIdentifiable(child_element, artifact_desc)
            code_desc.addArtifactDescriptor(artifact_desc)
            
            self.logger.debug("readArtifactDescriptor %s", artifact_desc.short_label)

    def readCodeDescriptor(self, element: ET.Element, impl: Implementation):
        for child_element in element.findall("./xmlns:CODE-DESCRIPTORS/xmlns:CODE", self.nsmap):
            short_name = self.readShortName(child_element)
            self.logger.debug("readCodeDescriptor %s" % short_name)
            code_desc = impl.createCodeDescriptor(short_name)
            self.readArtifactDescriptor(child_element, code_desc)

    def readMemorySections(self, element: ET.Element, consumption: ResourceConsumption):
        for child_element in element.findall("./xmlns:MEMORY-SECTIONS/xmlns:MEMORY-SECTION", self.nsmap):
            short_name = self.readShortName(child_element)
            memory_section = consumption.createMemorySection(short_name)
            alignment = self.readChildOptionalElement(child_element, "ALIGNMENT")
            if (alignment != None):
                memory_section.alignment = alignment
            memory_section.sw_addr_method_ref = self.readChildRefElement(consumption.short_name, child_element, "SW-ADDRMETHOD-REF")
            self.logger.debug("readMemorySections %s" % memory_section.short_name)

    def readResourceConsumption(self, element: ET.Element, impl: Implementation):
        child_element = element.find("./xmlns:RESOURCE-CONSUMPTION", self.nsmap)
        if (child_element == None):
            self._raiseError("Invalid ResourceConsumption of Implementation <%s>" % impl.short_name)
            return
        short_name = self.readShortName(child_element)
        impl.resource_consumption = ResourceConsumption(impl, short_name)
        self.readMemorySections(child_element, impl.resource_consumption)

    def readImplementation(self, element: ET.Element, impl: Implementation):
        self.readCodeDescriptor(element, impl)
        impl.programming_language = self.readChildOptionalElement(element, "PROGRAMMING-LANGUAGE")
        self.readResourceConsumption(element, impl)
        impl.sw_version = self.readChildOptionalElement(element, "SW-VERSION")
        impl.swc_bsw_mapping_ref = self.readChildOptionalRefElement(element, "SWC-BSW-MAPPING-REF")
        impl.vendor_id = self.readChildOptionalElementNumberValue(element, "VENDOR-ID")

    def readBswImplementation(self, element: ET.Element, parent: ARPackage):
        for child_element in element.findall("./xmlns:ELEMENTS/xmlns:BSW-IMPLEMENTATION", self.nsmap):
            short_name = self.readShortName(child_element)
            impl = parent.createBswImplementation(short_name)   
            self.logger.debug("readBswImplementation %s" % impl.short_name)

            self.readImplementation(child_element, impl)

            impl.ar_release_version = self.readChildElement(parent.short_name, child_element, "AR-RELEASE-VERSION")
            impl.behavior_ref = self.readChildRefElement(parent.short_name, child_element, "BEHAVIOR-REF")

    def readSwcImplementation(self, element: ET.Element, parent: ARPackage):
        for child_element in element.findall("./xmlns:ELEMENTS/xmlns:SWC-IMPLEMENTATION", self.nsmap):
            short_name = self.readShortName(child_element)
            impl = parent.createSwcImplementation(short_name)   
            self.logger.debug("readSwcImplementation %s" % impl.short_name)

            self.readImplementation(child_element, impl)

            impl.behavior_ref = self.readChildRefElement(parent.short_name, child_element, "BEHAVIOR-REF")

    def readDataReceivePointByArguments(self, element, parent: RunnableEntity):
        self._readVariableAccesses(element, parent, "DATA-RECEIVE-POINT-BY-ARGUMENTS")

    def readDataReceivePointByValues(self, element: ET.Element, parent: RunnableEntity):
        self._readVariableAccesses(element, parent, "DATA-RECEIVE-POINT-BY-VALUES")

    def readDataReadAccesses(self, element: ET.Element, parent: RunnableEntity):
        self._readVariableAccesses(element, parent, "DATA-READ-ACCESSS")

    def readDataSendPoints(self, element: ET.Element, parent: RunnableEntity):
        self._readVariableAccesses(element, parent, "DATA-SEND-POINTS")

    def readWrittenLocalVariables(self, element: ET.Element, parent: RunnableEntity):
        self._readVariableAccesses(element, parent, "WRITTEN-LOCAL-VARIABLES")

    def readReadLocalVariables(self, element: ET.Element, parent: RunnableEntity):
        self._readVariableAccesses(element, parent, "READ-LOCAL-VARIABLES")

    def readROperationIRef(self, element: ET.Element, parent: ServerCallPoint):
        child_element = element.find("./xmlns:OPERATION-IREF", self.nsmap)
        if (child_element != None):
            operation_iref = ROperationInAtomicSwcInstanceRef()
            operation_iref.context_r_port_ref = self.readChildOptionalRefElement(child_element, "CONTEXT-R-PORT-REF")
            operation_iref.target_required_operation_ref = self.readChildRefElement("", child_element, "TARGET-REQUIRED-OPERATION-REF")
            parent.operation_iref = operation_iref

    def readRVariableInAtomicSwcInstanceRef(self, element: ET.Element, parent: DataReceivedEvent):
        child_element = element.find("./xmlns:DATA-IRE", self.nsmap)
        if (child_element != None):
            data_iref = RVariableInAtomicSwcInstanceRef()
            data_iref.context_r_port_ref = self.readChildOptionalRefElement(child_element, "CONTEXT-R-PORT-REF")
            data_iref.target_required_operation_ref = self.readChildRefElement("", child_element, "TARGET-DATA-ELEMENT-REF")
            parent.data_iref = data_iref

    def readRModeInAtomicSwcInstanceRef(self, element: ET.Element, parent: SwcModeSwitchEvent):
        for child_element in element.findall("./xmlns:MODE-IREFS/xmlns:MODE-IREF", self.nsmap):
            mode_iref = RModeInAtomicSwcInstanceRef()
            mode_iref.context_port = self.readChildOptionalRefElement(child_element, "CONTEXT-PORT-REF")
            mode_iref.context_mode_declaration_group_prototype = self.readChildRefElement("", child_element, "CONTEXT-MODE-DECLARATION-GROUP-PROTOTYPE-REF")
            mode_iref.target_mode_declaration = self.readChildRefElement("", child_element, "TARGET-MODE-DECLARATION-REF")
            parent.addModeIRef(mode_iref)

    def readSynchronousServerCallPoint(self, element: ET.Element, parent: RunnableEntity):
        for child_element in element.findall("./xmlns:SERVER-CALL-POINTS/xmlns:SYNCHRONOUS-SERVER-CALL-POINT", self.nsmap):
            short_name = self.readShortName(child_element)
            serverCallPoint = parent.createSynchronousServerCallPoint(short_name)
            serverCallPoint.timeout = self.readChildElement(short_name, child_element, "TIMEOUT")
            self.readROperationIRef(child_element, serverCallPoint)

    def readAsynchronousServerCallPoint(self, element: ET.Element, parent: RunnableEntity):
        for child_element in element.findall("./xmlns:SERVER-CALL-POINTS/xmlns:ASYNCHRONOUS-SERVER-CALL-POINT", self.nsmap):
            short_name = self.readShortName(child_element)
            serverCallPoint = parent.createAsynchronousServerCallPoint(short_name)
            serverCallPoint.timeout = self.readChildElement(short_name, child_element, "TIMEOUT")
            self.readROperationIRef(child_element, serverCallPoint)

    def readInternalTriggeringPoint(self, element: ET.Element, parent: RunnableEntity):
        for child_element in element.findall("./xmlns:INTERNAL-TRIGGERING-POINTS/xmlns:INTERNAL-TRIGGERING-POINT", self.nsmap):
            short_name = self.readShortName(child_element)
            point = parent.createInternalTriggeringPoint(short_name)
            point.sw_impl_policy = self.readChildOptionalElement(child_element, "SW-IMPL-POLICY")

    def readRunnableEntities(self, element: ET.Element, parent: SwcInternalBehavior):
        for child_element in element.findall("./xmlns:RUNNABLES/xmlns:RUNNABLE-ENTITY", self.nsmap):
            short_name = self.readShortName(child_element)
            runnable = parent.createRunnableEntity(short_name)
            runnable.can_be_invoked_concurrently = self.readChildOptionalElement(child_element, "CAN-BE-INVOKED-CONCURRENTLY")
            runnable.symbol = self.readChildElement(short_name, child_element, "SYMBOL")

            self.logger.debug("readRunnableEntities %s" % short_name)

            self.readDataReceivePointByArguments(child_element, runnable)
            self.readDataReceivePointByValues(child_element, runnable)
            self.readDataReadAccesses(child_element, runnable)
            self.readDataSendPoints(child_element, runnable)
            self.readWrittenLocalVariables(child_element, runnable)
            self.readReadLocalVariables(child_element, runnable)
            self.readSynchronousServerCallPoint(child_element, runnable)
            self.readAsynchronousServerCallPoint(child_element, runnable)
            self.readInternalTriggeringPoint(child_element, runnable)

    def readRTEEvent(self, element: ET.Element, event: RTEEvent):
        event.start_on_event_ref = self.readChildOptionalRefElement(element, "START-ON-EVENT-REF")

    def readOperationIRef(self, element: ET.Element, parent: OperationInvokedEvent):
        child_element = element.find("./xmlns:OPERATION-IREF", self.nsmap)
        if (child_element != None):
            parent.operation_iref = POperationInAtomicSwcInstanceRef()
            parent.operation_iref.context_p_port_ref = self.readChildRefElement(parent.short_name, child_element, "CONTEXT-P-PORT-REF")
            parent.operation_iref.target_provided_operation_ref = self.readChildRefElement(parent.short_name, child_element, "TARGET-PROVIDED-OPERATION-REF")

    def readOperationInvokedEvents(self, element: ET.Element, parent: SwcInternalBehavior):
        for child_element in element.findall("./xmlns:EVENTS/xmlns:OPERATION-INVOKED-EVENT", self.nsmap):
            short_name = self.readShortName(child_element)
            event = parent.createOperationInvokedEvent(short_name)
            self.readOperationIRef(child_element, event)
            self.readRTEEvent(child_element, event)

    def readExplicitInterRunnableVariables(self, element: ET.Element, parent: SwcInternalBehavior):
        for child_element in element.findall("./xmlns:EXPLICIT-INTER-RUNNABLE-VARIABLES/xmlns:VARIABLE-DATA-PROTOTYPE", self.nsmap):
            short_name = self.readShortName(child_element)
            prototype = parent.createExplicitInterRunnableVariable(short_name)
            self.readSwDataDefProps(child_element, prototype)
            prototype.type_tref = self.readChildRefElement(parent.short_name, child_element, "TYPE-TREF")

    def readInitEvents(self, element, parent: SwcInternalBehavior):
        for child_element in element.findall("./xmlns:EVENTS/xmlns:INIT-EVENT", self.nsmap):
            short_name = self.readShortName(child_element)
            event = parent.createInitEvent(short_name)

            self.readRTEEvent(child_element, event)

    def readTimingEvents(self, element: ET.Element, parent: SwcInternalBehavior):
        for child_element in element.findall("./xmlns:EVENTS/xmlns:TIMING-EVENT", self.nsmap):
            short_name = self.readShortName(child_element)
            event = parent.createTimingEvent(short_name)

            self.readRTEEvent(child_element, event)

            offset = self.readChildOptionalElement(child_element, "OFFSET")
            if (offset != None):
                event.offset = (float)(offset)
            event.period = (float)(self.readChildElement(short_name, child_element, "PERIOD"))

    def readDataReceivedEvent(self, element: ET.Element, parent: SwcInternalBehavior):
        for child_element in element.findall("./xmlns:EVENTS/xmlns:DATA-RECEIVED-EVENT", self.nsmap):
            short_name = self.readShortName(child_element)
            event = parent.createDataReceivedEvent(short_name)

            self.readRTEEvent(child_element, event)
            self.readRVariableInAtomicSwcInstanceRef(child_element, event)

    def readSwcModeSwitchEvent(self, element: ET.Element, parent: SwcInternalBehavior):
        for child_element in element.findall("./xmlns:EVENTS/xmlns:SWC-MODE-SWITCH-EVENT", self.nsmap):
            short_name = self.readShortName(child_element)
            event = parent.createSwcModeSwitchEvent(short_name)

            self.readRTEEvent(child_element, event)
            self.readRModeInAtomicSwcInstanceRef(child_element, event)

    def readInternalTriggerOccurredEvent(self, element: ET.Element, parent: SwcInternalBehavior):
        for child_element in element.findall("./xmlns:EVENTS/xmlns:INTERNAL-TRIGGER-OCCURRED-EVENT", self.nsmap):
            short_name = self.readShortName(child_element)
            event = parent.createInternalTriggerOccurredEvent(short_name)

            self.readRTEEvent(child_element, event)
            event.event_source_ref = self.readChildRefElement(parent.short_name, child_element, "EVENT-SOURCE-REF")

    def readSwPointerTargetProps(self, element: ET.Element, parent: ARElement):
        child_element = element.find(
            "./xmlns:SW-POINTER-TARGET-PROPS", self.nsmap)

        if (child_element != None):
            sw_pointer_target_props = SwPointerTargetProps()
            sw_pointer_target_props.target_category = self.readChildElement("", child_element, "TARGET-CATEGORY")
            self.readSwDataDefProps(child_element, sw_pointer_target_props)
            parent.sw_pointer_target_props = sw_pointer_target_props

    def parseSwDataDefProps(self, element: ET.Element) -> SwDataDefProps:
        child_element = element.find("./xmlns:SW-DATA-DEF-PROPS/xmlns:SW-DATA-DEF-PROPS-VARIANTS/xmlns:SW-DATA-DEF-PROPS-CONDITIONAL", self.nsmap)

        if (child_element != None):
            sw_data_def_props = SwDataDefProps()
            sw_data_def_props.base_type_ref = self.readChildOptionalRefElement(child_element, "BASE-TYPE-REF")
            sw_data_def_props.data_constr_ref = self.readChildOptionalRefElement(child_element, "DATA-CONSTR-REF")
            sw_data_def_props.compu_method_ref = self.readChildOptionalRefElement(child_element, "COMPU-METHOD-REF")
            sw_data_def_props.implementation_data_type_ref = self.readChildOptionalRefElement(child_element, "IMPLEMENTATION-DATA-TYPE-REF")
            sw_data_def_props.sw_calibration_access = self.readChildOptionalElement(child_element, "SW-CALIBRATION-ACCESS")
            self.readSwPointerTargetProps(child_element, sw_data_def_props)
            return sw_data_def_props

    def readSwDataDefProps(self, element: ET.Element, parent: AutosarDataType):
        child_element = element.find("./xmlns:SW-DATA-DEF-PROPS/xmlns:SW-DATA-DEF-PROPS-VARIANTS/xmlns:SW-DATA-DEF-PROPS-CONDITIONAL", self.nsmap)

        if (child_element != None):
            sw_data_def_props = SwDataDefProps()
            sw_data_def_props.base_type_ref = self.readChildOptionalRefElement(child_element, "BASE-TYPE-REF")
            sw_data_def_props.data_constr_ref = self.readChildOptionalRefElement(child_element, "DATA-CONSTR-REF")
            sw_data_def_props.compu_method_ref = self.readChildOptionalRefElement(child_element, "COMPU-METHOD-REF")
            sw_data_def_props.implementation_data_type_ref = self.readChildOptionalRefElement(child_element, "IMPLEMENTATION-DATA-TYPE-REF")
            sw_data_def_props.sw_calibration_access = self.readChildOptionalElement(child_element, "SW-CALIBRATION-ACCESS")
            self.readSwPointerTargetProps(child_element, sw_data_def_props)
            parent.sw_data_def_props = sw_data_def_props

    def readApplicationPrimitiveDataTypes(self, element: ET.Element, parent: ARPackage):
        for child_element in element.findall("./xmlns:ELEMENTS/xmlns:APPLICATION-PRIMITIVE-DATA-TYPE", self.nsmap):
            short_name = self.readShortName(child_element)
            data_type = parent.createApplicationPrimitiveDataType(short_name)
            self.logger.debug("readApplicationPrimitiveDataTypes %s" % short_name)
            self.readIdentifiable(child_element, data_type)
            self.readSwDataDefProps(child_element, data_type)

    def readApplicationRecordElements(self, element: ET.Element, parent: ApplicationRecordDataType):
        for child_element in element.findall("./xmlns:ELEMENTS/xmlns:APPLICATION-RECORD-ELEMENT", self.nsmap):
            short_name = self.readShortName(child_element)
            record_element = parent.createApplicationRecordElement(short_name)
            self.logger.debug("readApplicationRecordElements %s" % short_name)
            self.readIdentifiable(child_element, record_element)
            record_element.type_tref = self.readChildOptionalRefElement(child_element, "TYPE-TREF")

    def readApplicationRecordDataTypes(self, element: ET.Element, parent: ARPackage):
        for child_element in element.findall("./xmlns:ELEMENTS/xmlns:APPLICATION-RECORD-DATA-TYPE", self.nsmap):
            short_name = self.readShortName(child_element)
            data_type = parent.createApplicationRecordDataType(short_name)
            self.logger.debug("readApplicationRecordDataTypes %s" % short_name)
            self.readIdentifiable(child_element, data_type)
            self.readSwDataDefProps(child_element, data_type)
            self.readApplicationRecordElements(child_element, data_type)

    def readImplementationDataTypeElements(self, element: ET.Element, parent: ARElement):
        for child_element in element.findall("./xmlns:SUB-ELEMENTS/xmlns:IMPLEMENTATION-DATA-TYPE-ELEMENT", self.nsmap):
            short_name = self.readShortName(child_element)
            type_element = parent.createImplementationDataTypeElement(short_name)   # type: ImplementationDataTypeElement
            self.readIdentifiable(child_element, type_element)
            type_element.array_size = self.readChildOptionalElement(child_element, "ARRAY-SIZE")
            type_element.array_size_semantics = self.readChildOptionalElement(child_element, "ARRAY-SIZE-SEMANTICS")
            self.readImplementationDataTypeElements(child_element, type_element)
            self.readSwDataDefProps(child_element, type_element)

    def readImplementationDataTypes(self, element: ET.Element, parent: ARPackage):
        for child_element in element.findall("./xmlns:ELEMENTS/xmlns:IMPLEMENTATION-DATA-TYPE", self.nsmap):
            short_name = self.readShortName(child_element)
            data_type = parent.createImplementationDataType(short_name)
            self.readIdentifiable(child_element, data_type)
            self.readImplementationDataTypeElements(child_element, data_type)
            self.readSwDataDefProps(child_element, data_type)
            if (data_type.category == ImplementationDataType.CATEGORY_ARRAY):
                if (len(data_type.getImplementationDataTypeElements()) < 1):
                    self._raiseError("Array Sub-Element of <%s> do not defined." % data_type.short_name)
                array_sub_element = data_type.getImplementationDataTypeElements()[0]
                if (array_sub_element.category == ImplementationDataType.CATEGORY_TYPE_REFERENCE):
                    data_type.setArrayElementType(array_sub_element.sw_data_def_props.implementation_data_type_ref.value)
                elif (array_sub_element.category == ImplementationDataType.CATEGORY_TYPE_VALUE):  # TODO: fix 
                    continue
                else:
                    self._raiseError("The category <%s> of array sub-element <%s> does not support." % (array_sub_element.category, data_type.short_name))

    def readBaseTypeDirectDefinition(self, element: ET.Element, parent: BaseType):
        parent.base_type_definition.base_type_size = int(self.readChildOptionalElement(element, "BASE-TYPE-SIZE"))
        parent.base_type_definition.base_type_encoding = self.readChildOptionalElementLiteral(element, "BASE-TYPE-ENCODING")
        parent.base_type_definition.native_declaration = self.readChildOptionalElementLiteral(element, "NATIVE-DECLARATION")

    def readSwBaseTypes(self, element: ET.Element, parent: ARPackage):
        for child_element in element.findall("./xmlns:ELEMENTS/xmlns:SW-BASE-TYPE", self.nsmap):
            short_name = self.readShortName(child_element)
            data_type = parent.createSwBaseType(short_name)
            self.readIdentifiable(child_element, data_type)
            self.readBaseTypeDirectDefinition(child_element, data_type)

    def readClientComSpec(self, element: ET.Element, parent: RPortPrototype):
        for child_element in element.findall("./xmlns:REQUIRED-COM-SPECS/xmlns:CLIENT-COM-SPEC", self.nsmap):
            try:
                com_spec = ClientComSpec()
                self.readElementAttributes(child_element, com_spec)
                com_spec.operation_ref = self.readChildRefElement(parent.short_name, child_element, "OPERATION-REF")
                parent.addRequiredComSpec(com_spec)
            except ValueError as err:
                self.logger.error(parent.short_name + ": " + str(err))

    def readReceiverComSpec(self, element, com_spec: ReceiverComSpec):
        #FIXME: readchildElement
        com_spec.data_element_ref = self.readChildOptionalRefElement(element, "DATA-ELEMENT-REF")
        self.readSwDataDefProps(element, com_spec)
        com_spec.handle_out_of_range = self.readChildOptionalElement(element, "HANDLE-OUT-OF-RANGE")
        com_spec.uses_end_to_end_protection = self.readChildOptionalElementBooleanValue(element, "USES-END-TO-END-PROTECTION")

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

    def readSwValueCont(self, element: ET.Element) -> SwValueCont:
        cont = None
        child_element = element.find("./xmlns:SW-VALUE-CONT", self.nsmap)
        if child_element is not None:
            cont = SwValueCont()
            cont.unit_ref = self.readChildOptionalRefElement(child_element, "UNIT-REF")
            cont.sw_values_phys = self.readSwValues(child_element, "SW-VALUES-PHYS")

            self.logger.debug("readSwValueCont - Unit: %s" % cont.unit_ref.value)
        return cont
    
    def readValueSpecification(self, element: ET.Element, value_spec: ValueSpecification):
        value_spec.short_label = self.readChildOptionalElement(element, "SHORT-LABEL")
        self.readElementAttributes(element, value_spec)
        
        self.logger.debug("readValueSpecification")

    def readApplicationValueSpecification(self, element: ET.Element, value_spec: ApplicationValueSpecification):
        self.readValueSpecification(element, value_spec)
        value_spec.category = self.readChildOptionalElement(element, "CATEGORY")
        value_spec.sw_value_cont = self.readSwValueCont(element)

        self.logger.debug("readApplicationValueSpecification Category %s" % value_spec.category)

    def readTextValueSpecification(self, element: ET.Element, value_spec: TextValueSpecification):
        self.readValueSpecification(element, value_spec)
        value_spec.value = self.readChildOptionalElement(element, "VALUE")

        self.logger.debug("readTextValueSpecification Value: %s" % value_spec.value)

    def readNumericalValueSpecification(self, element: ET.Element, value_spec: NumericalValueSpecification):
        self.readValueSpecification(element, value_spec)
        value_spec.value = self.readChildOptionalElement(element, "VALUE")

        self.logger.debug("readNumericalValueSpecification Value: %s" % value_spec.value)

    def readArrayValueSpecification(self, element: ET.Element, value_spec: ArrayValueSpecification):
        self.readValueSpecification(element, value_spec)
        
        child_elements = element.findall("./xmlns:ELEMENTS/xmlns:NUMERICAL-VALUE-SPECIFICATION", self.nsmap)
        for child_element in child_elements:
            sub_element = NumericalValueSpecification()
            self.readNumericalValueSpecification(child_element, sub_element)
            value_spec.add_element(sub_element)

        self.logger.debug("readArrayValueSpecification")

    def readConstantReference(self, element: ET.Element, value_spec: ConstantReference):
        self.readValueSpecification(element, value_spec)

        value_spec.constant_ref = self.readChildOptionalRefElement(element, "CONSTANT-REF")

    def readInitValue(self, element: ET.Element) -> ValueSpecification:
        value_spec = None
        child_element = element.find("./xmlns:INIT-VALUE", self.nsmap)
        if child_element is not None:
            self.logger.debug("readInitValue")
            value_spec_tag = child_element.find("./xmlns:APPLICATION-VALUE-SPECIFICATION", self.nsmap)
            if value_spec_tag is not None:
                value_spec = ApplicationValueSpecification()
                self.readApplicationValueSpecification(value_spec_tag, value_spec)
                return value_spec
            value_spec_tag = child_element.find("./xmlns:TEXT-VALUE-SPECIFICATION", self.nsmap)
            if value_spec_tag is not None:
                value_spec = TextValueSpecification()
                self.readTextValueSpecification(value_spec_tag, value_spec)
                return value_spec
            value_spec_tag = child_element.find("./xmlns:NUMERICAL-VALUE-SPECIFICATION", self.nsmap)
            if value_spec_tag is not None:
                value_spec = NumericalValueSpecification()
                self.readNumericalValueSpecification(value_spec_tag, value_spec)
                return value_spec
            value_spec_tag = child_element.find("./xmlns:ARRAY-VALUE-SPECIFICATION", self.nsmap)
            if value_spec_tag is not None:
                value_spec = ArrayValueSpecification()
                self.readArrayValueSpecification(value_spec_tag, value_spec)
                return value_spec
            value_spec_tag = child_element.find("./xmlns:CONSTANT-REFERENCE", self.nsmap)
            if value_spec_tag is not None:
                value_spec = ConstantReference()
                self.readConstantReference(value_spec_tag, value_spec)
                return value_spec

        return value_spec

    def readNonqueuedReceiverComSpec(self, element, parent: RPortPrototype):
        for child_element in element.findall("./xmlns:REQUIRED-COM-SPECS/xmlns:NONQUEUED-RECEIVER-COM-SPEC", self.nsmap):
            com_spec = NonqueuedReceiverComSpec()

            self.readElementAttributes(child_element, com_spec)            
            self.readReceiverComSpec(child_element, com_spec)
            try:
                # FIXME:
                com_spec.alive_timeout = self.readChildElementFloatValue("", child_element, "ALIVE-TIMEOUT")
                com_spec.enable_updated = self.readChildElementBooleanValue("", child_element, "ENABLE-UPDATE")
                com_spec.handle_never_received = self.readChildElementBooleanValue("", child_element, "HANDLE-NEVER-RECEIVED")
                com_spec.handel_timeout_type = self.readChildElement("", child_element, "HANDLE-TIMEOUT-TYPE")
            except ValueError as err:
                self.logger.error(parent.short_name + ": " + str(err))

            com_spec.init_value = self.readInitValue(child_element)

            parent.addRequiredComSpec(com_spec)

    def readRPortPrototype(self, element, parent: AtomicSwComponentType):
        for child_element in element.findall("./xmlns:PORTS/xmlns:R-PORT-PROTOTYPE", self.nsmap):
            short_name = self.readShortName(child_element)
            self.logger.debug("readRPortPrototype %s" % short_name)

            prototype = parent.createRPortPrototype(short_name)
            self.readElementAttributes(child_element, prototype)
            prototype.required_interface_tref = self.readChildOptionalRefElement(child_element, "REQUIRED-INTERFACE-TREF")

            self.readClientComSpec(child_element, prototype)
            self.readNonqueuedReceiverComSpec(child_element, prototype)

    def readTransmissionAcknowledgementRequest(self, element: ET.Element) -> TransmissionAcknowledgementRequest:
        child_element = element.find("./xmlns:TRANSMISSION-ACKNOWLEDGE", self.nsmap)
        if (child_element != None):
            acknowledge = TransmissionAcknowledgementRequest()
            self.readElementAttributes(child_element, acknowledge)
            acknowledge.timeout = self.readChildElementFloatValue ("", child_element, "TIMEOUT")
            return acknowledge
        return None

    def readSenderComSpec(self, element, com_spec: SenderComSpec):
        # FIXME:
        self.readElementAttributes(element, com_spec)
        com_spec.data_element_ref = self.readChildOptionalRefElement(element, "DATA-ELEMENT-REF")
        com_spec.network_representation = self.parseSwDataDefProps(element)
        self.logger.debug("network_representation %s" % com_spec.network_representation)
        com_spec.handle_out_of_range = self.readChildOptionalElement(element, "HANDLE-OUT-OF-RANGE")
        com_spec.transmission_acknowledge = self.readTransmissionAcknowledgementRequest(element)
        com_spec.uses_end_to_end_protection = self.readChildOptionalElementBooleanValue(element, "USES-END-TO-END-PROTECTION")

    def readNonqueuedSenderComSpec(self, element, parent: PPortPrototype):
        for child_element in element.findall("./xmlns:PROVIDED-COM-SPECS/xmlns:NONQUEUED-SENDER-COM-SPEC", self.nsmap):
            com_spec = NonqueuedSenderComSpec()
            self.readSenderComSpec(child_element, com_spec)
            
            com_spec.init_value = self.readInitValue(child_element)

            parent.addProvidedComSpec(com_spec)

    def readPPortPrototype(self, element, parent: AtomicSwComponentType):
        for child_element in element.findall("./xmlns:PORTS/xmlns:P-PORT-PROTOTYPE", self.nsmap):
            short_name = self.readShortName(child_element)
            self.logger.debug("readPPortPrototype %s" % short_name)

            prototype = parent.createPPortPrototype(short_name)
            self.readElementAttributes(child_element, prototype)
            prototype.provided_interface_tref = self.readChildOptionalRefElement(child_element, "PROVIDED-INTERFACE-TREF")
            self.readNonqueuedSenderComSpec(child_element, prototype)

    def readSwComponentType(self, element, parent: SwComponentType):
        self.readRPortPrototype(element, parent)
        self.readPPortPrototype(element, parent)

    def readAtomicSwComponentType(self, element, parent: AtomicSwComponentType):
        self.readSwComponentType(element, parent)
        self.readSwInternalBehavior(element, parent)

    def readEcuAbstractionSwComponents(self, element, parent: ARPackage):
        for child_element in element.findall("./xmlns:ELEMENTS/xmlns:ECU-ABSTRACTION-SW-COMPONENT-TYPE", self.nsmap):
            short_name = self.readShortName(child_element)
            sw_component = parent.createEcuAbstractionSwComponentType(
                short_name)
            self.readAtomicSwComponentType(child_element, sw_component)

    def readApplicationSwComponentTypes(self, element, parent: ARPackage):
        for child_element in element.findall("./xmlns:ELEMENTS/xmlns:APPLICATION-SW-COMPONENT-TYPE", self.nsmap):
            short_name = self.readShortName(child_element)
            sw_component = parent.createApplicationSwComponentType(short_name)
            self.readAtomicSwComponentType(child_element, sw_component)

    def readComplexDeviceDriverSwComponentTypes(self, element, parent: ARPackage):
        for child_element in element.findall("./xmlns:ELEMENTS/xmlns:COMPLEX-DEVICE-DRIVER-SW-COMPONENT-TYPE", self.nsmap):
            short_name = self.readShortName(child_element)
            sw_component = parent.createApplicationSwComponentType(short_name)
            self.readAtomicSwComponentType(child_element, sw_component)

    def readSensorActuatorSwComponentType(self, element, parent: ARPackage):
        for child_element in element.findall("./xmlns:ELEMENTS/xmlns:SENSOR-ACTUATOR-SW-COMPONENT-TYPE", self.nsmap):
            short_name = self.readShortName(child_element)
            sw_component = parent.createSensorActuatorSwComponentType(short_name)
            self.readAtomicSwComponentType(child_element, sw_component)

    def readServiceSwComponentTypes(self, element, parent: ARPackage):
        for child_element in element.findall("./xmlns:ELEMENTS/xmlns:SERVICE-SW-COMPONENT-TYPE", self.nsmap):
            short_name = self.readShortName(child_element)
            sw_component = parent.createServiceSwComponentType(short_name)
            self.readAtomicSwComponentType(child_element, sw_component)

    def readPPortInCompositionInstanceRef(self, element, p_port_in_composition_instance_ref: PPortInCompositionInstanceRef):
        p_port_in_composition_instance_ref.context_component_ref = self.readChildOptionalRefElement(element, "CONTEXT-COMPONENT-REF")
        p_port_in_composition_instance_ref.target_p_port_ref = self.readChildOptionalRefElement(element, "TARGET-P-PORT-REF")
        
        self.logger.debug("PPortInCompositionInstanceRef")
        self.logger.debug("  CONTEXT-COMPONENT-REF DEST: %s, %s"
                          % (p_port_in_composition_instance_ref.context_component_ref.dest, p_port_in_composition_instance_ref.context_component_ref.value))
        self.logger.debug("  TARGET-P-PORT-REF DEST: %s, %s" 
                          % (p_port_in_composition_instance_ref.target_p_port_ref.dest, p_port_in_composition_instance_ref.target_p_port_ref.value))

    def readRPortInCompositionInstanceRef(self, element, r_port_in_composition_instance_ref: RPortInCompositionInstanceRef):
        r_port_in_composition_instance_ref.context_component_ref = self.readChildOptionalRefElement(element, "CONTEXT-COMPONENT-REF")
        r_port_in_composition_instance_ref.target_r_port_ref = self.readChildOptionalRefElement(element, "TARGET-R-PORT-REF")

        self.logger.debug("RPortInCompositionInstanceRef")
        self.logger.debug("  CONTEXT-COMPONENT-REF DEST: %s, %s"
                          % (r_port_in_composition_instance_ref.context_component_ref.dest, r_port_in_composition_instance_ref.context_component_ref.value))
        self.logger.debug("  TARGET-P-PORT-REF DEST: %s, %s" 
                          % (r_port_in_composition_instance_ref.target_r_port_ref.dest, r_port_in_composition_instance_ref.target_r_port_ref.value))

    def readAssemblySwConnectorProviderIRef(self, element, parent: AssemblySwConnector):
        child_element = element.find("./xmlns:PROVIDER-IREF", self.nsmap)
        if (child_element != None):
            provide_iref = PPortInCompositionInstanceRef()
            self.readElementAttributes(child_element, provide_iref)
            self.readPPortInCompositionInstanceRef(child_element, provide_iref)
            parent.provider_iref = provide_iref

    def readAssemblySwConnectorRequesterIRef(self, element, parent: AssemblySwConnector):
        child_element = element.find("./xmlns:REQUESTER-IREF", self.nsmap)
        if (child_element != None):
            requester_iref = RPortInCompositionInstanceRef()
            self.readElementAttributes(child_element, requester_iref)
            self.readRPortInCompositionInstanceRef(child_element, requester_iref)
            parent.requester_iref = requester_iref

    def readAssemblySwConnectors(self, element, parent: CompositionSwComponentType):
        for child_element in element.findall("./xmlns:CONNECTORS/xmlns:ASSEMBLY-SW-CONNECTOR", self.nsmap):
            short_name = self.readShortName(child_element)
            self.logger.debug("readAssemblySwConnectors %s" % short_name)

            connector = parent.createAssemblySwConnector(short_name)
            self.readElementAttributes(child_element, connector)
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
            short_name = self.readShortName(child_element)
            self.logger.debug("readDelegationSwConnectors %s" % short_name)

            connector = parent.createDelegationSwConnector(short_name)
            self.readElementAttributes(child_element, connector)
            self.readDelegationSwConnectorInnerPortIRef(child_element, connector)

            if connector.inner_port_iref == None and connector.outer_port_iref == None:
                self._raiseError("Invalid PortPrototype of DELEGATION-SW-CONNECTOR")

            connector.outer_port_ref = self.readChildOptionalRefElement(child_element, "OUTER-PORT-REF")
            self.logger.debug("OUTER-PORT-REF DEST: %s, %s"
                          % (connector.outer_port_ref.dest, connector.outer_port_ref.value))

    def readSwComponentPrototypes(self, element: ET.Element, parent: CompositionSwComponentType):
        for child_element in element.findall("./xmlns:COMPONENTS/xmlns:SW-COMPONENT-PROTOTYPE", self.nsmap):
            short_name = self.readShortName(child_element)
            self.logger.debug("readSwComponentPrototypes %s" % short_name)

            prototype = parent.createSwComponentPrototype(short_name)
            self.readElementAttributes(child_element, prototype)
            prototype.type_tref = self.readChildOptionalRefElement(child_element, "TYPE-TREF")

    def readDataTypeMappingSet(self, element: ET.Element, parent: CompositionSwComponentType):
        child_element = element.find("./xmlns:DATA-TYPE-MAPPING-REFS", self.nsmap)
        self.logger.debug("readDataTypeMappingSet")
        if child_element != None:
            for ref in self.readChildRefElementList(child_element, "DATA-TYPE-MAPPING-REF"):
                parent.addDataTypeMapping(ref)

    def readCompositionSwComponentTypes(self, element: ET.Element, parent: ARPackage):
        for child_element in element.findall("./xmlns:ELEMENTS/xmlns:COMPOSITION-SW-COMPONENT-TYPE", self.nsmap):
            short_name = self.readShortName(child_element)
            self.logger.debug("readCompositionSwComponentTypes: <%s>" % short_name)

            sw_component = parent.createCompositionSwComponentType(short_name)
            self.readIdentifiable(child_element, sw_component)
            self.readSwComponentType(child_element, sw_component)
            self.readSwComponentPrototypes(child_element, sw_component)
            self.readAssemblySwConnectors(child_element, sw_component)
            self.readDelegationSwConnectors(child_element, sw_component)
            self.readDataTypeMappingSet(child_element, sw_component)

    def readDataTypeMap(self, element: ET.Element, parent: DataTypeMappingSet):
        for child_element in element.findall("./xmlns:DATA-TYPE-MAPS/xmlns:DATA-TYPE-MAP", self.nsmap):
            data_type_map = DataTypeMap()
            data_type_map.application_data_type_ref = self.readChildOptionalRefElement(child_element, "APPLICATION-DATA-TYPE-REF")
            data_type_map.implementation_data_type_ref = self.readChildOptionalRefElement(child_element, "IMPLEMENTATION-DATA-TYPE-REF")
            parent.addDataTypeMap(data_type_map)
            # add the data type map to global namespace
            AUTOSAR.getInstance().addDataTypeMap(data_type_map)

    def readDataTypeMappingSets(self, element: ET.Element, parent: ARPackage):
        for child_element in element.findall("./xmlns:ELEMENTS/xmlns:DATA-TYPE-MAPPING-SET", self.nsmap):
            short_name = self.readShortName(child_element)
            mapping_set = parent.createDataTypeMappingSet(short_name)
            self.readDataTypeMap(child_element, mapping_set)

    def readVariableDataPrototype(self, element: ET.Element, parent: SenderReceiverInterface):
        for child_element in element.findall("./xmlns:DATA-ELEMENTS/xmlns:VARIABLE-DATA-PROTOTYPE", self.nsmap):
            short_name = self.readShortName(child_element)
            prototype = parent.createDataElement(short_name)
            self.readSwDataDefProps(child_element, prototype)
            prototype.type_tref = self.readChildOptionalRefElement(child_element, "TYPE-TREF")

    def readSenderReceiverInterfaces(self, element, parent: ARPackage):
        for child_element in element.findall("./xmlns:ELEMENTS/xmlns:SENDER-RECEIVER-INTERFACE", self.nsmap):
            short_name = self.readShortName(child_element)
            sr_interface = parent.createSenderReceiverInterface(short_name)
            self.readVariableDataPrototype(child_element, sr_interface)

    def readArgumentDataPrototypes(self, element: ET.Element, parent: ClientServerOperation):
        for child_element in element.findall("./xmlns:ARGUMENTS/xmlns:ARGUMENT-DATA-PROTOTYPE", self.nsmap):
            short_name = self.readShortName(child_element)
            prototype = ArgumentDataPrototype(property, short_name)
            prototype.type_tref = self.readChildOptionalRefElement(child_element, "TYPE-TREF")
            prototype.direction = self.readChildElement(short_name, child_element, "DIRECTION")
            parent.addArgumentDataPrototype(prototype)

    def readPossibleErrorRefs(self, element: ET.Element, parent: ClientServerOperation):
        child_element = element.find("./xmlns:POSSIBLE-ERROR-REFS", self.nsmap)
        if child_element != None:
            for ref in self.readChildRefElementList(child_element, "POSSIBLE-ERROR-REF"):
                parent.addPossibleErrorRef(ref)

    def readOperations(self, element: ET.Element, parent: ClientServerInterface):
        for child_element in element.findall("./xmlns:OPERATIONS/xmlns:CLIENT-SERVER-OPERATION", self.nsmap):
            short_name = self.readShortName(child_element)
            operation = parent.createOperation(short_name)
            self.readArgumentDataPrototypes(child_element, operation)
            self.readPossibleErrorRefs(child_element, operation)

    def readPossibleErrors(self, element: ET.Element, parent: ClientServerInterface):
        for child_element in element.findall("./xmlns:POSSIBLE-ERRORS/xmlns:APPLICATION-ERROR", self.nsmap):
            short_name = self.readShortName(child_element)
            error = parent.createApplicationError(short_name)
            error.error_code = self.readChildElementNumberValue(short_name, child_element, "ERROR-CODE")

    def readClientServerInterfaces(self, element: ET.Element, parent: ARPackage):
        for child_element in element.findall("./xmlns:ELEMENTS/xmlns:CLIENT-SERVER-INTERFACE", self.nsmap):
            short_name = self.readShortName(child_element)
            cs_interface = parent.createClientServerInterface(short_name)
            cs_interface.is_service = self.readChildElement(short_name, child_element, "IS-SERVICE")
            self.readOperations(child_element, cs_interface)
            self.readPossibleErrors(child_element, cs_interface)

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
            compu_scale.lower_limit = self.readChildLimitElement(child_element, "LOWER-LIMIT")
            compu_scale.upper_limit = self.readChildLimitElement(child_element, "UPPER-LIMIT")
            self.readCompuScaleContents(child_element, compu_scale)
            parent.addCompuScale(compu_scale)

    def readCompuInternalToPhys(self, element: ET.Element, parent: CompuMethod):
        child_element = element.find("./xmlns:COMPU-INTERNAL-TO-PHYS", self.nsmap)
        if (child_element != None):
            parent.compu_internal_to_phys = Compu()
            self.readElementAttributes(child_element, parent.compu_internal_to_phys)
            parent.compu_internal_to_phys.compu_content = CompuScales()
            self.readCompuScales(child_element, parent.compu_internal_to_phys.compu_content)

    def readCompuMethods(self, element: ET.Element, parent: ARPackage):
        for child_element in element.findall("./xmlns:ELEMENTS/xmlns:COMPU-METHOD", self.nsmap):
            short_name = self.readShortName(child_element)
            self.logger.debug("readCompuMethods %s" % short_name)
            compu_method = parent.createCompuMethod(short_name)
            self.readIdentifiable(child_element, compu_method)
            compu_method.unit_ref = self.readChildOptionalRefElement(child_element, "UNIT-REF")
            self.readCompuInternalToPhys(child_element, compu_method)

    def readSwcBswRunnableMappings(self, element: ET.Element, parent: SwcBswMapping):
        for child_element in element.findall("./xmlns:RUNNABLE-MAPPINGS/xmlns:SWC-BSW-RUNNABLE-MAPPING", self.nsmap):
            mapping = SwcBswRunnableMapping()
            mapping.bsw_entity_ref = self.readChildOptionalRefElement(child_element, "BSW-ENTITY-REF")
            mapping.swc_runnable_ref = self.readChildOptionalRefElement(child_element, "SWC-RUNNABLE-REF")
            parent.addRunnableMapping(mapping)

    def readSwcBswMappings(self, element: ET.Element, parent: ARPackage):
        for child_element in element.findall("./xmlns:ELEMENTS/xmlns:SWC-BSW-MAPPING", self.nsmap):
            short_name = self.readShortName(child_element)
            self.logger.debug("readSwcBswMappings %s" % short_name)
            swc_bsw_mapping = parent.createSwcBswMapping(short_name)
            swc_bsw_mapping.bsw_behavior_ref = self.readChildOptionalRefElement(child_element, "BSW-BEHAVIOR-REF")
            self.readSwcBswRunnableMappings(child_element, swc_bsw_mapping)
            swc_bsw_mapping.swc_behavior_ref = self.readChildOptionalRefElement(child_element, "SWC-BEHAVIOR-REF")

    def readValueSpecification(self, element: ET.Element, value_spec: ValueSpecification):
        value_spec.short_label = self.readChildOptionalElement(element, "SHORT-LABEL")

    def readSwValueCont(self, element: ET.Element, spec: ApplicationValueSpecification):
        child_element = element.find("./xmlns:SW-VALUE-CONT", self.nsmap)
        if child_element is not None:
            sw_value_cont = SwValueCont()
            sw_value_cont.unit_ref = self.readChildOptionalRefElement(child_element, "UNIT-REF")
            sw_value_cont.sw_values_phys = self.readSwValues(child_element, "SW-VALUES-PHYS")
            spec.sw_value_cont = sw_value_cont

    def readApplicationValueSpecification(self, element: ET.Element) -> ApplicationValueSpecification:
        value_spec = ApplicationValueSpecification()
        self.readValueSpecification(element, value_spec)
        value_spec.category = self.readChildOptionalElement(element, "CATEGORY")
        self.readSwValueCont(element, value_spec)
        return value_spec

    def readRecordValueSpecificationFields(self, element: ET.Element, spec: RecordValueSpecification):
        for child_element in element.findall("./xmlns:FIELDS/*", self.nsmap):
            if child_element.tag == "{http://autosar.org/schema/r4.0}APPLICATION-VALUE-SPECIFICATION":
                value_spec = self.readApplicationValueSpecification(child_element)
            elif child_element.tag == "{http://autosar.org/schema/r4.0}RECORD-VALUE-SPECIFICATION":
                value_spec = self.readRecordValueSpecification(child_element)
            else:
                raise NotImplementedError("Unsupported VALUE-SPEC %s" % child_element.tag)
            spec.add_field(value_spec)

    def readRecordValueSpecification(self, element: ET.Element) -> RecordValueSpecification:
        value_spec = RecordValueSpecification()
        self.readValueSpecification(element, value_spec)
        self.readRecordValueSpecificationFields(element, value_spec)
        return value_spec

    def readConstantSpecification(self, element: ET.Element, parent: ARPackage):
        for child_element in element.findall("./xmlns:ELEMENTS/xmlns:CONSTANT-SPECIFICATION", self.nsmap):
            short_name = self.readShortName(child_element)
            self.logger.debug("readConstantSpecification %s" % short_name)
            spec = parent.createConstantSpecification(short_name)
            self.readIdentifiable(child_element, spec)
            for value_spec_tag in child_element.findall("./xmlns:VALUE-SPEC/*", self.nsmap):
                if value_spec_tag.tag == "{http://autosar.org/schema/r4.0}APPLICATION-VALUE-SPECIFICATION":
                    spec.value_spec = self.readApplicationValueSpecification(value_spec_tag)
                elif value_spec_tag.tag == "{http://autosar.org/schema/r4.0}RECORD-VALUE-SPECIFICATION":
                    spec.value_spec = self.readRecordValueSpecification(value_spec_tag)
                else:
                    raise NotImplementedError("Unsupported VALUE-SPEC %s" % value_spec_tag.tag)
                
    def readInternalConstrs(self, element: ET.Element, parent: DataConstrRule):
        child_element = element.find("./xmlns:INTERNAL-CONSTRS", self.nsmap)
        if child_element is not None:
            constrs = InternalConstrs()
            constrs.lower_limit = self.readChildLimitElement(child_element, "LOWER-LIMIT")
            constrs.upper_limit = self.readChildLimitElement(child_element, "UPPER-LIMIT")
            parent.internal_constrs = constrs

    def readPhysConstrs(self, element: ET.Element, parent: DataConstrRule):
        child_element = element.find("./xmlns:PHYS-CONSTRS", self.nsmap)
        if child_element is not None:
            constrs = PhysConstrs()
            constrs.lower_limit = self.readChildLimitElement(child_element, "LOWER-LIMIT")
            constrs.upper_limit = self.readChildLimitElement(child_element, "UPPER-LIMIT")
            constrs.unit_ref = self.readChildOptionalRefElement(child_element, "UNIT-REF")
            parent.phys_constrs = constrs
                
    def readDataConstrRule(self, element: ET.Element, parent: DataConstr):
        for child_element in element.findall("./xmlns:DATA-CONSTR-RULES/xmlns:DATA-CONSTR-RULE", self.nsmap):
            self.logger.debug("readDataConstrRule")
            rule = DataConstrRule()
            self.readInternalConstrs(child_element, rule)
            self.readPhysConstrs(child_element, rule)
            parent.addDataConstrRule(rule)
                
    def readDataConstr(self, element: ET.Element, parent: ARPackage):
        for child_element in element.findall("./xmlns:ELEMENTS/xmlns:DATA-CONSTR", self.nsmap):
            short_name = self.readShortName(child_element)
            self.logger.debug("readDataConstr %s" % short_name)
            constr = parent.createDataConstr(short_name)
            self.readIdentifiable(child_element, constr)
            self.readDataConstrRule(child_element, constr)

    def readUnit(self, element: ET.Element, parent: ARPackage):
        for child_element in element.findall("./xmlns:ELEMENTS/xmlns:UNIT", self.nsmap):
            short_name = self.readShortName(child_element)
            self.logger.debug("readUnit %s" % short_name)
            unit = parent.createUnit(short_name)
            self.readIdentifiable(child_element, unit)
            unit.display_name = self.readChildOptionalElementLiteral(child_element, "DISPLAY-NAME")

    def readARPackages(self, element: ET.Element, parent: ARPackage):
        for child_element in element.findall("./xmlns:AR-PACKAGES/xmlns:AR-PACKAGE", self.nsmap):
            short_name = self.readShortName(child_element)
            ar_package = parent.createARPackage(short_name)

            self.logger.debug("readARPackages %s" % ar_package.full_name)

            self.readElementAttributes(child_element, ar_package)

            self.readSenderReceiverInterfaces(child_element, ar_package)
            self.readClientServerInterfaces(child_element, ar_package)
            self.readDataTypeMappingSets(child_element, ar_package)
            self.readARPackages(child_element, ar_package)
            self.readApplicationPrimitiveDataTypes(child_element, ar_package)
            self.readApplicationRecordDataTypes(child_element, ar_package)
            self.readImplementationDataTypes(child_element, ar_package)
            self.readSwBaseTypes(child_element, ar_package)
            self.readCompuMethods(child_element, ar_package)
            self.readEcuAbstractionSwComponents(child_element, ar_package)
            self.readApplicationSwComponentTypes(child_element, ar_package)
            self.readComplexDeviceDriverSwComponentTypes(child_element, ar_package)
            self.readSensorActuatorSwComponentType(child_element, ar_package)
            self.readServiceSwComponentTypes(child_element, ar_package)
            self.readCompositionSwComponentTypes(child_element, ar_package)
            self.readBswModuleDescription(child_element, ar_package)
            self.readBswModuleEntry(child_element, ar_package)
            self.readSwcBswMappings(child_element, ar_package)
            self.readBswImplementation(child_element, ar_package)
            self.readSwcImplementation(child_element, ar_package)
            self.readConstantSpecification(child_element, ar_package)
            self.readDataConstr(child_element, ar_package)
            self.readUnit(child_element, ar_package)

    def load(self, filename, document: AUTOSAR):
        self.logger.info("Load %s ..." % filename)

        tree = ET.parse(filename)
        root = tree.getroot()
        if (self.getPureTagName(root.tag) != "AUTOSAR"):
            self._raiseError("Invalid ARXML file <%s>" % filename)

        self.readARPackages(root, document)
