from ..models import AUTOSAR, ARPackage, ARObject, EcuAbstractionSwComponentType, AtomicSwComponentType, SwComponentType, CompositionSwComponentType
from ..models import SwcInternalBehavior, RunnableEntity, RTEEvent, VariableAccess, ServerCallPoint, OperationInvokedEvent
from ..models import RefType, AutosarVariableRef, ArVariableInImplementationDataInstanceRef, POperationInAtomicSwcInstanceRef, ROperationInAtomicSwcInstanceRef
from ..models import ImplementationDataType, SwDataDefProps, SwPointerTargetProps, DataTypeMappingSet, DataTypeMap, ImplementationDataTypeElement
from ..models import DataPrototype, RPortPrototype, PPortPrototype
from ..models import ReceiverComSpec, ClientComSpec, NonqueuedReceiverComSpec, QueuedReceiverComSpec
from ..models import SenderComSpec, NonqueuedSenderComSpec
from ..models import SenderReceiverInterface, ClientServerInterface, ClientServerOperation, ArgumentDataPrototype
from ..models import AutosarDataType, ARElement
from ..models import AssemblySwConnector, ProvidedPortPrototypeInstanceRef, RequiredPortPrototypeInstanceRef
from ..models import CompuMethod, CompuScale, Limit, CompuScales, Compu, CompuConst, CompuConstTextContent

from typing import List
import xml.etree.ElementTree as ET
import re


class ARXMLParser:
    def __init__(self):
        self.nsmap = {"xmlns": "http://autosar.org/schema/r4.0"}

    def getPureTagName(self, tag):
        return re.sub(r'\{[\w:\/.]+\}(\w+)', r'\1', tag)

    def readChildElement(self, short_name: str, element, key: str) -> str:
        child_element = element.find("./xmlns:%s" % key, self.nsmap)
        if (child_element != None):
            return child_element.text
        raise ValueError("The attribute %s of <%s> has not been defined" % (key, short_name))

    def readChildElementBooleanValue(self, short_name, element, key) -> bool:
        value = self.readChildElement(short_name, element, key)
        if (value == "true"):
            return True
        return False

    def readChildOptionalElement(self, element, key) -> str:
        child_element = element.find("./xmlns:%s" % key, self.nsmap)
        if (child_element != None):
            return child_element.text
        return None

    def readChildOptionElementBooleanValue(self, element, key) -> bool:
        value = self.readChildElement("", element, key)
        if (value == None):
            return None
        elif (value == "True"):
            return True
        else:
            return False

    def readChildLimitElement(self, element, key) -> Limit:
        child_element = element.find("./xmlns:%s" % key, self.nsmap)
        if (child_element != None):
            limit = Limit()
            limit.interval_type = child_element.attrib['INTERVAL-TYPE']
            limit.value = child_element.text
            return limit
        return None

    def readShortName(self, element) -> str:
        return self.readChildElement("", element, "SHORT-NAME")

    def readChildRefElement(self, element, key) -> RefType:
        child_element = element.find("./xmlns:%s" % key, self.nsmap)
        if (child_element != None):
            ref = RefType()
            ref.dest = child_element.attrib['DEST']
            ref.value = child_element.text
            return ref
        return None

    def readChildRefElementList(self, element, key) -> List[RefType]:
        child_elements = element.findall("./xmlns:%s" % key, self.nsmap)
        results = []
        for child_element in child_elements:
            ref = RefType()
            ref.dest = child_element.attrib['DEST']
            ref.value = child_element.text
            results.append(ref)
        return results

    def readSwInternalBehavior(self, element, parent: AtomicSwComponentType):
        for child_element in element.findall("./xmlns:INTERNAL-BEHAVIORS/xmlns:SWC-INTERNAL-BEHAVIOR", self.nsmap):
            short_name = self.readShortName(child_element)
            behavior = parent.createSwcInternalBehavior(short_name)

            self.readRunnableEntities(child_element, behavior)
            self.readOperationInvokedEvents(child_element, behavior)
            self.readTimingEvents(child_element, behavior)
            self.readInternalTriggerOccurredEvent(child_element, behavior)
            self.readExplicitInterRunnableVariables(child_element, behavior)

    def readAutosarVariableInImplDatatype(self, element, accessed_variable_ref: AutosarVariableRef):
        child_element = element.find("./xmlns:ACCESSED-VARIABLE/xmlns:AUTOSAR-VARIABLE-IREF", self.nsmap)
        if (child_element != None):
            autosar_variable_in_impl_datatype = ArVariableInImplementationDataInstanceRef()
            autosar_variable_in_impl_datatype.port_prototype_ref = self.readChildRefElement(child_element, "PORT-PROTOTYPE-REF")
            autosar_variable_in_impl_datatype.target_data_prototype_ref = self.readChildRefElement(child_element, "TARGET-DATA-PROTOTYPE-REF")
            accessed_variable_ref.autosar_variable_in_impl_datatype = autosar_variable_in_impl_datatype

    def readLocalVariableRef(self, element, accessed_variable_ref: AutosarVariableRef):
        child_element = element.find("./xmlns:ACCESSED-VARIABLE", self.nsmap)
        if (child_element != None):
            accessed_variable_ref.local_variable_ref = self.readChildRefElement(child_element, "LOCAL-VARIABLE-REF")

    def _readVariableAccesses(self, element, parent: RunnableEntity, key: str):
        for child_element in element.findall("./xmlns:%s/xmlns:VARIABLE-ACCESS" % key, self.nsmap):
            short_name = self.readShortName(child_element)
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
                raise ValueError("Invalid key type <%s>" % key)

    def readDataReceivePointByArguments(self, element, parent: RunnableEntity):
        self._readVariableAccesses(element, parent, "DATA-RECEIVE-POINT-BY-ARGUMENTS")

    def readDataReceivePointByValues(self, element, parent: RunnableEntity):
        self._readVariableAccesses(element, parent, "DATA-RECEIVE-POINT-BY-VALUES")

    def readDataReadAccesses(self, element, parent: RunnableEntity):
        self._readVariableAccesses(element, parent, "DATA-READ-ACCESSS")

    def readDataSendPoints(self, element, parent: RunnableEntity):
        self._readVariableAccesses(element, parent, "DATA-SEND-POINTS")

    def readWrittenLocalVariables(self, element, parent: RunnableEntity):
        self._readVariableAccesses(element, parent, "WRITTEN-LOCAL-VARIABLES")

    def readReadLocalVariables(self, element, parent: RunnableEntity):
        self._readVariableAccesses(element, parent, "READ-LOCAL-VARIABLES")

    def readROperationIRef(self, element, serverCallPoint: ServerCallPoint):
        child_element = element.find("./xmlns:OPERATION-IREF", self.nsmap)
        if (child_element != None):
            operation_iref = ROperationInAtomicSwcInstanceRef()
            operation_iref.context_r_port_ref = self.readChildRefElement(child_element, "CONTEXT-R-PORT-REF")
            operation_iref.target_required_operation_ref = self.readChildRefElement(child_element, "TARGET-REQUIRED-OPERATION-REF")
            serverCallPoint.operation_iref = operation_iref

    def readSynchronousServerCallPoint(self, element, parent: RunnableEntity):
        for child_element in element.findall("./xmlns:SERVER-CALL-POINTS/xmlns:SYNCHRONOUS-SERVER-CALL-POINT", self.nsmap):
            short_name = self.readShortName(child_element)
            serverCallPoint = parent.createSynchronousServerCallPoint(short_name)
            serverCallPoint.timeout = self.readChildElement(short_name, child_element, "TIMEOUT")
            self.readROperationIRef(child_element, serverCallPoint)

    def readInternalTriggeringPoint(self, element, parent: RunnableEntity):
        for child_element in element.findall("./xmlns:INTERNAL-TRIGGERING-POINTS/xmlns:INTERNAL-TRIGGERING-POINT", self.nsmap):
            short_name = self.readShortName(child_element)
            point = parent.createInternalTriggeringPoint(short_name)
            point.sw_impl_policy = self.readChildOptionalElement(child_element, "SW-IMPL-POLICY")

    def readRunnableEntities(self, element, parent: SwcInternalBehavior):
        for child_element in element.findall("./xmlns:RUNNABLES/xmlns:RUNNABLE-ENTITY", self.nsmap):
            short_name = self.readShortName(child_element)
            runnable = parent.createRunnableEntity(short_name)
            runnable.can_be_invoked_concurrently = self.readChildElement(short_name, child_element, "CAN-BE-INVOKED-CONCURRENTLY")
            runnable.symbol = self.readChildElement(short_name, child_element, "SYMBOL")

            self.readDataReceivePointByArguments(child_element, runnable)
            self.readDataReceivePointByValues(child_element, runnable)
            self.readDataReadAccesses(child_element, runnable)
            self.readDataSendPoints(child_element, runnable)
            self.readWrittenLocalVariables(child_element, runnable)
            self.readReadLocalVariables(child_element, runnable)
            self.readSynchronousServerCallPoint(child_element, runnable)
            self.readInternalTriggeringPoint(child_element, runnable)

    def readRTEEvent(self, element, event: RTEEvent):
        event.start_on_event_ref = self.readChildRefElement(element, "START-ON-EVENT-REF")

    def readOperationIRef(self, element, parent: OperationInvokedEvent):
        child_element = element.find("./xmlns:OPERATION-IREF", self.nsmap)
        if (child_element != None):
            parent.operation_iref = POperationInAtomicSwcInstanceRef()
            parent.operation_iref.context_p_port_ref = self.readChildRefElement(child_element, "CONTEXT-P-PORT-REF")
            parent.operation_iref.target_provided_operation_ref = self.readChildRefElement(child_element, "TARGET-PROVIDED-OPERATION-REF")

    def readOperationInvokedEvents(self, element, parent: SwcInternalBehavior):
        for child_element in element.findall("./xmlns:EVENTS/xmlns:OPERATION-INVOKED-EVENT", self.nsmap):
            short_name = self.readShortName(child_element)
            event = parent.createOperationInvokedEvent(short_name)
            self.readOperationIRef(child_element, event)
            self.readRTEEvent(child_element, event)

    def readExplicitInterRunnableVariables(self, element, parent: SwcInternalBehavior):
        for child_element in element.findall("./xmlns:EXPLICIT-INTER-RUNNABLE-VARIABLES/xmlns:VARIABLE-DATA-PROTOTYPE", self.nsmap):
            short_name = self.readShortName(child_element)
            prototype = parent.createExplicitInterRunnableVariable(short_name)
            self.readSwDataDefProps(child_element, prototype)
            prototype.type_tref = self.readChildRefElement(child_element, "TYPE-TREF")

    def readTimingEvents(self, element, parent: SwcInternalBehavior):
        for child_element in element.findall("./xmlns:EVENTS/xmlns:TIMING-EVENT", self.nsmap):
            short_name = self.readShortName(child_element)
            event = parent.createTimingEvent(short_name)

            self.readRTEEvent(child_element, event)

            offset = self.readChildOptionalElement(child_element, "OFFSET")
            if (offset != None):
                event.offset = (float)(offset)
            event.period = (float)(self.readChildElement(short_name, child_element, "PERIOD"))

    def readInternalTriggerOccurredEvent(self, element, parent: SwcInternalBehavior):
        for child_element in element.findall("./xmlns:EVENTS/xmlns:INTERNAL-TRIGGER-OCCURRED-EVENT", self.nsmap):
            short_name = self.readShortName(child_element)
            event = parent.createInternalTriggerOccurredEvent(short_name)

            self.readRTEEvent(child_element, event)
            event.event_source_ref = self.readChildRefElement(child_element, "EVENT-SOURCE-REF")

    def readSwPointerTargetProps(self, element, parent: ARElement):
        child_element = element.find(
            "./xmlns:SW-POINTER-TARGET-PROPS", self.nsmap)

        if (child_element != None):
            sw_pointer_target_props = SwPointerTargetProps()
            sw_pointer_target_props.target_category = self.readChildElement("", child_element, "TARGET-CATEGORY")
            self.readSwDataDefProps(child_element, sw_pointer_target_props)
            parent.sw_pointer_target_props = sw_pointer_target_props

    def readSwDataDefProps(self, element, parent: ARElement):
        child_element = element.find(
            "./xmlns:SW-DATA-DEF-PROPS/xmlns:SW-DATA-DEF-PROPS-VARIANTS/xmlns:SW-DATA-DEF-PROPS-CONDITIONAL", self.nsmap)

        if (child_element != None):
            sw_data_def_props = SwDataDefProps()
            sw_data_def_props.base_type_ref = self.readChildRefElement(child_element, "BASE-TYPE-REF")
            sw_data_def_props.data_constr_ref = self.readChildRefElement(child_element, "DATA-CONSTR-REF")
            sw_data_def_props.compu_method_ref = self.readChildRefElement(child_element, "COMPU-METHOD-REF")
            sw_data_def_props.implementation_data_type_ref = self.readChildRefElement(child_element, "IMPLEMENTATION-DATA-TYPE-REF")
            sw_data_def_props.sw_calibration_access = self.readChildOptionalElement(child_element, "SW-CALIBRATION-ACCESS")
            self.readSwPointerTargetProps(child_element, sw_data_def_props)
            parent.sw_data_def_props = sw_data_def_props

    def readApplicationPrimitiveDataTypes(self, element, parent: ARPackage):
        for child_element in element.findall("./xmlns:ELEMENTS/xmlns:APPLICATION-PRIMITIVE-DATA-TYPE", self.nsmap):
            short_name = self.readShortName(child_element)
            data_type = parent.createApplicationPrimitiveDataType(short_name)
            data_type.category = self.readChildElement(short_name, child_element, "CATEGORY")
            self.readSwDataDefProps(child_element, data_type)

    def readApplicationRecordDataTypes(self, element, parent: ARPackage):
        for child_element in element.findall("./xmlns:ELEMENTS/xmlns:APPLICATION-RECORD-DATA-TYPE", self.nsmap):
            short_name = self.readShortName(child_element)
            data_type = parent.createApplicationRecordDataType(short_name)
            data_type.category = self.readChildElement(short_name, child_element, "CATEGORY")
            self.readSwDataDefProps(child_element, data_type)

            # TODO: add read APPLICATION-RECORD-ELEMENT

    def readImplementationDataTypeElements(self, element, parent: ARElement):
        for child_element in element.findall("./xmlns:SUB-ELEMENTS/xmlns:IMPLEMENTATION-DATA-TYPE-ELEMENT", self.nsmap):
            short_name = self.readShortName(child_element)
            type_element = parent.createImplementationDataTypeElement(short_name)   # type: ImplementationDataTypeElement
            type_element.category = self.readChildElement(short_name, child_element, "CATEGORY")
            type_element.array_size = self.readChildOptionalElement(child_element, "ARRAY-SIZE")
            type_element.array_size_semantics = self.readChildOptionalElement(child_element, "ARRAY-SIZE-SEMANTICS")
            self.readImplementationDataTypeElements(child_element, type_element)
            self.readSwDataDefProps(child_element, type_element)

    def readImplementationDataTypes(self, element, parent: ARPackage):
        for child_element in element.findall("./xmlns:ELEMENTS/xmlns:IMPLEMENTATION-DATA-TYPE", self.nsmap):
            short_name = self.readShortName(child_element)
            data_type = parent.createImplementationDataType(short_name)
            data_type.category = self.readChildElement(short_name, child_element, "CATEGORY")
            self.readImplementationDataTypeElements(child_element, data_type)
            self.readSwDataDefProps(child_element, data_type)
            if (data_type.category == ImplementationDataType.CATEGORY_ARRAY):
                if (len(data_type.getImplementationDataTypeElements()) < 1):
                    raise ValueError("Array Sub-Element of <%s> do not defined." % data_type.short_name)
                array_sub_element = data_type.getImplementationDataTypeElements()[0]
                if (array_sub_element.category == ImplementationDataType.CATEGORY_TYPE_REFERENCE):
                    data_type.setArrayElementType(array_sub_element.sw_data_def_props.implementation_data_type_ref.value)
                else:
                    raise ValueError("The catetory <%s> of array sub-element does not support." % array_sub_element.category)

    def readSwDataTypes(self, element, parent: ARPackage):
        for child_element in element.findall("./xmlns:ELEMENTS/xmlns:SW-BASE-TYPE", self.nsmap):
            short_name = self.readShortName(child_element)
            data_type = parent.createSwBaseType(short_name)

    def readClientComSpec(self, element, parent: RPortPrototype):
        for child_element in element.findall("./xmlns:REQUIRED-COM-SPECS/xmlns:CLIENT-COM-SPEC", self.nsmap):
            try:
                com_spec = ClientComSpec()
                com_spec.operation_ref = self.readChildRefElement(child_element, "OPERATION-REF")
                parent.addRequiredComSpec(com_spec)
            except ValueError as err:
                print(parent.short_name + ": " + str(err))

    def readReceiverComSpec(self, element, com_spec: ReceiverComSpec):
        #FIXME: readchildElement
        com_spec.data_element_ref = self.readChildRefElement(element, "DATA-ELEMENT-REF")
        com_spec.handle_out_of_range = self.readChildElement("", element, "HANDLE-OUT-OF-RANGE")
        com_spec.uses_end_to_end_protection = self.readChildOptionElementBooleanValue(element, "USES-END-TO-END-PROTECTION")

    def readNonqueuedReceiverComSpec(self, element, parent: RPortPrototype):
        for child_element in element.findall("./xmlns:REQUIRED-COM-SPECS/xmlns:NONQUEUED-RECEIVER-COM-SPEC", self.nsmap):

            com_spec = NonqueuedReceiverComSpec()
            self.readReceiverComSpec(child_element, com_spec)
            try:
                # FIXME:
                com_spec.alive_timeout = float(self.readChildElement("", child_element, "ALIVE-TIMEOUT"))
                com_spec.enable_updated = self.readChildElementBooleanValue("", child_element, "ENABLE-UPDATE")
                com_spec.handle_never_received = self.readChildElementBooleanValue("", child_element, "HANDLE-NEVER-RECEIVED")
                com_spec.handel_timeout_type = self.readChildElement("", child_element, "HANDLE-TIMEOUT-TYPE")
            except ValueError as err:
                print(parent.short_name + ": " + str(err))

            parent.addRequiredComSpec(com_spec)

    def readRPortPrototype(self, element, parent: AtomicSwComponentType):
        for child_element in element.findall("./xmlns:PORTS/xmlns:R-PORT-PROTOTYPE", self.nsmap):
            short_name = self.readShortName(child_element)
            prototype = parent.createRPortPrototype(short_name)
            prototype.required_interface_tref = self.readChildRefElement(
                child_element, "REQUIRED-INTERFACE-TREF")

            self.readClientComSpec(child_element, prototype)
            self.readNonqueuedReceiverComSpec(child_element, prototype)

    def readSenderComSpec(self, element, com_spec: SenderComSpec):
        # FIXME:
        com_spec.data_element_ref = self.readChildRefElement(element, "DATA-ELEMENT-REF")
        com_spec.handle_out_of_range = self.readChildElement("", element, "HANDLE-OUT-OF-RANGE")
        com_spec.uses_end_to_end_protection = self.readChildOptionElementBooleanValue(element, "USES-END-TO-END-PROTECTION")

    def readNonqueuedSenderComSpec(self, element, parent: PPortPrototype):
        for child_element in element.findall("./xmlns:PROVIDED-COM-SPECS/xmlns:NONQUEUED-SENDER-COM-SPEC", self.nsmap):
            com_spec = NonqueuedSenderComSpec()
            self.readSenderComSpec(child_element, com_spec)
            parent.addProvidedComSpec(com_spec)

    def readPPortPrototype(self, element, parent: AtomicSwComponentType):
        for child_element in element.findall("./xmlns:PORTS/xmlns:P-PORT-PROTOTYPE", self.nsmap):
            short_name = self.readShortName(child_element)
            prototype = parent.createPPortPrototype(short_name)
            prototype.provided_interface_tref = self.readChildRefElement(
                child_element, "PROVIDED-INTERFACE-TREF")
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

    def readServiceSwComponentTypes(self, element, parent: ARPackage):
        for child_element in element.findall("./xmlns:ELEMENTS/xmlns:SERVICE-SW-COMPONENT-TYPE", self.nsmap):
            short_name = self.readShortName(child_element)
            sw_component = parent.createServiceSwComponentType(short_name)
            self.readAtomicSwComponentType(child_element, sw_component)

    def readAssemblySwConnectorProviderIRef(self, element, parent: AssemblySwConnector):
        child_element = element.find("./xmlns:PROVIDER-IREF", self.nsmap)
        if (child_element != None):
            provider_iref = ProvidedPortPrototypeInstanceRef()
            provider_iref.context_component_ref = self.readChildRefElement(
                child_element, "CONTEXT-COMPONENT-REF")
            provider_iref.target_p_port_ref = self.readChildRefElement(
                child_element, "TARGET-P-PORT-REF")
            parent.provider_iref = provider_iref

    def readAssemblySwConnectorRequesterIRef(self, element, parent: AssemblySwConnector):
        child_element = element.find("./xmlns:REQUESTER-IREF", self.nsmap)
        if (child_element != None):
            requester_iref = RequiredPortPrototypeInstanceRef()
            requester_iref.context_component_ref = self.readChildRefElement(
                child_element, "CONTEXT-COMPONENT-REF")
            requester_iref.target_r_port_ref = self.readChildRefElement(
                child_element, "TARGET-R-PORT-REF")
            parent.requester_iref = requester_iref

    def readAssemblySwConnectors(self, element, parent: CompositionSwComponentType):
        for child_element in element.findall("./xmlns:CONNECTORS/xmlns:ASSEMBLY-SW-CONNECTOR", self.nsmap):
            short_name = self.readShortName(child_element)
            connector = parent.createAssemblySwConnector(short_name)
            self.readAssemblySwConnectorProviderIRef(child_element, connector)
            self.readAssemblySwConnectorRequesterIRef(child_element, connector)

    def readSwComponentPrototypes(self, element, parent: CompositionSwComponentType):
        for child_element in element.findall("./xmlns:COMPONENTS/xmlns:SW-COMPONENT-PROTOTYPE", self.nsmap):
            short_name = self.readShortName(child_element)
            prototype = parent.createSwComponentPrototype(short_name)
            prototype.type_tref = self.readChildRefElement(
                child_element, "TYPE-TREF")

    def readCompositionSwComponentTypes(self, element, parent: ARPackage):
        for child_element in element.findall("./xmlns:ELEMENTS/xmlns:COMPOSITION-SW-COMPONENT-TYPE", self.nsmap):
            short_name = self.readShortName(child_element)
            sw_component = parent.createCompositionSwComponentType(short_name)
            self.readSwComponentType(child_element, sw_component)
            self.readSwComponentPrototypes(child_element, sw_component)
            self.readAssemblySwConnectors(child_element, sw_component)

    def readDataTypeMap(self, element, parent: DataTypeMappingSet):
        for child_element in element.findall("./xmlns:DATA-TYPE-MAPS/xmlns:DATA-TYPE-MAP", self.nsmap):
            data_type_map = DataTypeMap()
            data_type_map.application_data_type_ref = self.readChildRefElement(
                child_element, "APPLICATION-DATA-TYPE-REF")
            data_type_map.implementation_data_type_ref = self.readChildRefElement(
                child_element, "IMPLEMENTATION-DATA-TYPE-REF")
            parent.addDataTypeMap(data_type_map)
            # add the data type map to global namespace
            AUTOSAR.getInstance().addDataTypeMap(data_type_map)

    def readDataTypeMappingSets(self, element, parent: ARPackage):
        for child_element in element.findall("./xmlns:ELEMENTS/xmlns:DATA-TYPE-MAPPING-SET", self.nsmap):
            short_name = self.readShortName(child_element)
            mapping_set = parent.createDataTypeMappingSet(short_name)
            self.readDataTypeMap(child_element, mapping_set)

    def readVariableDataPrototype(self, element, parent: SenderReceiverInterface):
        for child_element in element.findall("./xmlns:DATA-ELEMENTS/xmlns:VARIABLE-DATA-PROTOTYPE", self.nsmap):
            short_name = self.readShortName(child_element)
            prototype = parent.createDataElement(short_name)
            self.readSwDataDefProps(child_element, prototype)
            prototype.type_tref = self.readChildRefElement(
                child_element, "TYPE-TREF")

    def readSenderReceiverInterfaces(self, element, parent: ARPackage):
        for child_element in element.findall("./xmlns:ELEMENTS/xmlns:SENDER-RECEIVER-INTERFACE", self.nsmap):
            short_name = self.readShortName(child_element)
            sr_interface = parent.createSenderReceiverInterface(short_name)
            self.readVariableDataPrototype(child_element, sr_interface)

    def readArgumentDataPrototypes(self, element, parent: ClientServerOperation):
        for child_element in element.findall("./xmlns:ARGUMENTS/xmlns:ARGUMENT-DATA-PROTOTYPE", self.nsmap):
            short_name = self.readShortName(child_element)
            prototype = ArgumentDataPrototype(property, short_name)
            prototype.type_tref = self.readChildRefElement(
                child_element, "TYPE-TREF")
            prototype.direction = self.readChildElement(
                short_name, child_element, "DIRECTION")
            parent.addArgumentDataPrototype(prototype)

    def readPossibleErrorRefs(self, element, parent: ClientServerOperation):
        child_element = element.find("./xmlns:POSSIBLE-ERROR-REFS", self.nsmap)
        if child_element != None:
            for ref in self.readChildRefElementList(child_element, "POSSIBLE-ERROR-REF"):
                parent.addPossibleErrorRef(ref)

    def readOperations(self, element, parent: ClientServerInterface):
        for child_element in element.findall("./xmlns:OPERATIONS/xmlns:CLIENT-SERVER-OPERATION", self.nsmap):
            short_name = self.readShortName(child_element)
            operation = parent.createOperation(short_name)
            self.readArgumentDataPrototypes(child_element, operation)
            self.readPossibleErrorRefs(child_element, operation)

    def readPossibleErrors(self, element, parent: ClientServerInterface):
        for child_element in element.findall("./xmlns:POSSIBLE-ERRORS/xmlns:APPLICATION-ERROR", self.nsmap):
            short_name = self.readShortName(child_element)
            error = parent.createApplicationError(short_name)
            error.error_code = int(self.readChildElement(
                short_name, child_element, "ERROR-CODE"))

    def readClientServerInterfaces(self, element, parent: ARPackage):
        for child_element in element.findall("./xmlns:ELEMENTS/xmlns:CLIENT-SERVER-INTERFACE", self.nsmap):
            short_name = self.readShortName(child_element)
            cs_interface = parent.createClientServerInterface(short_name)
            cs_interface.is_service = self.readChildElement(
                short_name, child_element, "IS-SERVICE")
            self.readOperations(child_element, cs_interface)
            self.readPossibleErrors(child_element, cs_interface)

    def readCompuConstTextContent(self, element, parent: CompuConstTextContent):
        child_element = element.find(
            "./xmlns:COMPU-CONST/xmlns:VT", self.nsmap)
        if (child_element != None):
            parent.vt = child_element.text

    def readCompuScales(self, element, parent: CompuScales):
        for child_element in element.findall('./xmlns:COMPU-SCALES/xmlns:COMPU-SCALE', self.nsmap):
            compu_scale = CompuScale()
            compu_scale.lower_limit = self.readChildLimitElement(
                child_element, "LOWER-LIMIT")
            compu_scale.upper_limit = self.readChildLimitElement(
                child_element, "UPPER-LIMIT")
            compu_scale.compu_inverse_value = CompuConstTextContent()
            self.readCompuConstTextContent(
                child_element, compu_scale.compu_inverse_value)
            parent.addCompuScale(compu_scale)

    def readCompuInternalToPhys(self, element, parent: CompuMethod):
        child_element = element.find(
            "./xmlns:COMPU-INTERNAL-TO-PHYS", self.nsmap)
        if (child_element != None):
            parent.compu_internal_to_phys = Compu()
            parent.compu_internal_to_phys.compu_content = CompuScales()
            self.readCompuScales(
                child_element, parent.compu_internal_to_phys.compu_content)

    def readCompuMethods(self, element, parent: ARPackage):
        for child_element in element.findall("./xmlns:ELEMENTS/xmlns:COMPU-METHOD", self.nsmap):
            short_name = self.readShortName(child_element)
            compu_method = parent.createCompuMethod(short_name)
            compu_method.category = self.readChildElement(
                short_name, child_element, "CATEGORY")
            self.readCompuInternalToPhys(child_element, compu_method)

    def readARPackages(self, element, parent):
        for child_element in element.findall("./xmlns:AR-PACKAGES/xmlns:AR-PACKAGE", self.nsmap):
            short_name = self.readShortName(child_element)
            ar_package = parent.createARPackage(short_name)

            self.readSenderReceiverInterfaces(child_element, ar_package)
            self.readClientServerInterfaces(child_element, ar_package)
            self.readDataTypeMappingSets(child_element, ar_package)
            self.readARPackages(child_element, ar_package)
            self.readApplicationPrimitiveDataTypes(child_element, ar_package)
            self.readApplicationRecordDataTypes(child_element, ar_package)
            self.readImplementationDataTypes(child_element, ar_package)
            self.readSwDataTypes(child_element, ar_package)
            self.readCompuMethods(child_element, ar_package)
            self.readEcuAbstractionSwComponents(child_element, ar_package)
            self.readApplicationSwComponentTypes(child_element, ar_package)
            self.readComplexDeviceDriverSwComponentTypes(
                child_element, ar_package)
            self.readServiceSwComponentTypes(child_element, ar_package)
            self.readCompositionSwComponentTypes(child_element, ar_package)

    def load(self, filename, document: AUTOSAR):
        tree = ET.parse(filename)
        root = tree.getroot()
        if (self.getPureTagName(root.tag) != "AUTOSAR"):
            raise ValueError("Invalid ARXML file <%s>" % filename)

        print("Load %s ..." % filename)

        self.readARPackages(root, document)
