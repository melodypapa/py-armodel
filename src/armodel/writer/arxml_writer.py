import logging
import xml.etree.cElementTree as ET

from xml.dom import minidom
from typing import List

from ..models.data_prototype import AutosarDataPrototype, ParameterDataPrototype, VariableDataPrototype
from ..models.bsw_module_template import BswModuleDescription, BswModuleEntry
from ..models.ar_package import AUTOSAR
from ..models.sw_component import ApplicationSwComponentType, AtomicSwComponentType, ComplexDeviceDriverSwComponentType, DataReceivedEvent, EcuAbstractionSwComponentType, OperationInvokedEvent, RTEEvent, SwcModeSwitchEvent, VariableAccess
from ..models.ar_object import ARBoolean
from ..models.ar_package import ARPackage
from ..models.ar_ref import AutosarVariableRef, POperationInAtomicSwcInstanceRef, PPortInCompositionInstanceRef, RModeInAtomicSwcInstanceRef, RPortInCompositionInstanceRef, TRefType
from ..models.calibration import SwValueCont, SwValues
from ..models.common_structure import ApplicationValueSpecification, ArrayValueSpecification, ConstantReference, NumericalValueSpecification, RecordValueSpecification, TextValueSpecification, ValueSpecification
from ..models.communication import TransmissionAcknowledgementRequest
from ..models.data_dictionary import SwDataDefProps
from ..models.datatype import ApplicationDataType, ApplicationPrimitiveDataType, ApplicationRecordDataType, AutosarDataType, BaseType, ImplementationDataType, SwBaseType
from ..models.general_structure import ARElement, AdminData, Identifiable, Limit, MultilanguageReferrable, Referrable, Sdg, SwcBswMapping
from ..models.m2_msr import CompuConstTextContent, CompuMethod, CompuNominatorDenominator, CompuScale, CompuScaleConstantContents, CompuScaleRationalFormula, CompuScales
from ..models.port_prototype import ClientComSpec, NonqueuedReceiverComSpec, NonqueuedSenderComSpec, PPortComSpec, PPortPrototype, PortPrototype, QueuedReceiverComSpec, RPortComSpec, RPortPrototype, ReceiverComSpec, SenderComSpec, ServerComSpec
from ..models.sw_component import AssemblySwConnector, CompositionSwComponentType, DelegationSwConnector, SwComponentPrototype, SwComponentType, SwConnector
from ..models.annotation import Annotation
from ..models.end_to_end_protection import EndToEndProtectionSet
from ..models.port_interface import ApplicationError, ClientServerInterface, ClientServerOperation, SenderReceiverInterface
from ..models.unit import Unit
from ..models.implementation import BswImplementation, Code, Implementation, SwcImplementation
from ..models.common_structure import ConstantSpecification, ExecutableEntity, InternalBehavior, ResourceConsumption
from ..models.sw_component import RunnableEntity, SwcInternalBehavior, TimingEvent
from ..models.ar_object import ARLiteral, ARObject, MultilanguageLongName
from ..models.global_constraints import DataConstr, InternalConstrs, PhysConstrs

from colorama import Fore

class ARXMLWriter:
    def __init__(self, options = None) -> None:
        self.options = {}
        self.options['warning'] = False
        self.options['version'] = "4.2.2"
        self.logger = logging.getLogger()
        
        self._processOptions(options=options)

        self.nsmap = {
            "xmlns": "http://autosar.org/schema/r4.0", 
        }

    def _processOptions(self, options):
        if options:
            if 'warning' in options:
                self.options['warning'] = options['warning']

    def _raiseError(self, error_msg):
        if (self.options['warning'] == True):
            self.logger.error(Fore.RED + error_msg + Fore.WHITE)
        else:
            raise ValueError(error_msg)
        
    def writeElementAttributes(self, element: ET.Element, ar_obj: ARObject):
        if ar_obj.timestamp is not None:
            self.logger.debug("Timestamp: %s" % ar_obj.timestamp)
            element.attrib['T'] = ar_obj.timestamp
        if ar_obj.uuid is not None:
            self.logger.debug("UUID: %s" % ar_obj.uuid)
            element.attrib['UUID'] = ar_obj.uuid

    def setChildOptionalElement(self, element: ET.Element, key: str, value: str):
        if value is not None:
            child_element = ET.SubElement(element, key)
            child_element.text = value

    def setChildOptionalElementNumberValue(self, element: ET.Element, key: str, value: str):
        if value is not None:
            child_element = ET.SubElement(element, key)
            child_element.text = str(value)

    def setChildOptionalRefElement(self, parent: ET.Element, child_tag_name: str, ref: TRefType):
        if ref is not None:
            child_tag = ET.SubElement(parent, child_tag_name)
            if ref.dest is not None:
                child_tag.attrib['DEST'] = ref.dest
            if ref.value is not None:
                child_tag.text = ref.value

    def setChildOptionalElementFloatValue(self, element: ET.Element, key: str, value: float):
        if value is not None:
            child_element = ET.SubElement(element, key)
            literal = "%g" % value
            if literal == '0':
                literal = "0.0"
            child_element.text = literal

    def setChildOptionalElementBooleanValue(self, element: ET.Element, key: str, value: ARBoolean) -> ET.Element:
        child_element = None
        if value is not None:
            child_element = ET.SubElement(element, key)
            self.writeElementAttributes(child_element, value)
            if value.value:
                child_element.text = "true"
            else:
                child_element.text = "false"
        return child_element

    def writeChildOptionalElementLiteral(self, element: ET.Element, key: str, value: ARLiteral) -> ET.Element:
        child_element = None
        if value is not None:
            child_element = ET.SubElement(element, key)
            self.writeElementAttributes(child_element, value)
            child_element.text = value.value
        return child_element      
        
    def setShortName(self, parent: ET.Element, name: str) -> ET.Element:
        sub_element = ET.SubElement(parent, "SHORT-NAME")
        sub_element.text = name

        return sub_element
    
    def writeSd(self, parent: ET.Element, sdg: Sdg):
        for sd in sdg.getSds():
            sd_tag = ET.SubElement(parent, "SD")
            sd_tag.attrib['GID'] = sd.gid
            sd_tag.text = sd.value
    
    def writeSdg(self, parent: ET.Element, admin_data: AdminData):
        sdgs = admin_data.getSdgs()
        if len(sdgs) > 0:
            sdgs_tag = ET.SubElement(parent, "SDGS")
            for sdg in sdgs:
                sdg_tag = ET.SubElement(sdgs_tag, "SDG")
                sdg_tag.attrib['GID'] = sdg.gid
                self.writeSd(sdg_tag, sdg)
    
    def writeChildLimitElement(self, element: ET.Element, key: str, limit: Limit):
        if limit is not None:
            limit_tag = ET.SubElement(element, key)
            limit_tag.attrib['INTERVAL-TYPE'] = limit.interval_type
            limit_tag.text = limit.value
    
    def writeReferable(self, element: ET.Element, referrable: Referrable):
        self.writeElementAttributes(element, referrable)
        self.setShortName(element, referrable.short_name)

    def setMultiLongName(self, element: ET.Element, key: str, long_name: MultilanguageLongName):
        if long_name is not None:
            long_name_tag = ET.SubElement(element, key)
            self.writeElementAttributes(long_name_tag, long_name)
            for l4 in long_name.get_l4s():
                l4_tag = ET.SubElement(long_name_tag, "L-4")
                self.writeElementAttributes(l4_tag, l4)
                if l4.l is not None:
                    l4_tag.attrib['L'] = l4.l
                l4_tag.text = l4.value

    def writeMultilanguageReferrable(self, element: ET.Element, referrable: MultilanguageReferrable):
        self.writeReferable(element, referrable)
        if referrable.long_name is not None:
            self.setMultiLongName(element, "LONG-NAME", referrable.long_name)

    def writeAdminData(self, element: ET.Element, admin_data: AdminData):
        element = ET.SubElement(element, "ADMIN-DATA")
        self.writeSdg(element, admin_data)

    def writeIdentifiable(self, element: ET.Element, identifiable: Identifiable):
        self.writeMultilanguageReferrable(element, identifiable)
        self.setChildOptionalElement(element, "CATEGORY", identifiable.category)
        if identifiable.admin_data is not None:
            self.writeAdminData(element, identifiable.admin_data)

    def writeARElement(self, parent: ET.Element, ar_element: ARElement):
        self.writeIdentifiable(parent, ar_element)
    
    def writeTransmissionAcknowledgementRequest(self, element: ET.Element, acknowledge: TransmissionAcknowledgementRequest):
        if (acknowledge != None):
            child_element = ET.SubElement(element, "TRANSMISSION-ACKNOWLEDGE")
            self.writeElementAttributes(child_element, acknowledge)
            if acknowledge.timeout != None:
                self.setChildOptionalElementFloatValue(child_element, "TIMEOUT", acknowledge.timeout)

    def writeSenderComSpec(self, com_spec_tag: ET.Element, com_spec: SenderComSpec):
        self.setChildOptionalRefElement(com_spec_tag, "DATA-ELEMENT-REF", com_spec.data_element_ref)
        self.setSwDataDefProps(com_spec_tag, "NETWORK-REPRESENTATION", com_spec.network_representation)
        self.setChildOptionalElement(com_spec_tag, "HANDLE-OUT-OF-RANGE", com_spec.handle_out_of_range)
        self.writeTransmissionAcknowledgementRequest(com_spec_tag, com_spec.transmission_acknowledge)
        self.setChildOptionalElementBooleanValue(com_spec_tag, "USES-END-TO-END-PROTECTION", com_spec.uses_end_to_end_protection)
    
    def writeNonqueuedSenderComSpec(self, com_specs_tag: ET.Element, com_spec: NonqueuedSenderComSpec):
        com_spec_tag = ET.SubElement(com_specs_tag, "NONQUEUED-SENDER-COM-SPEC")
        self.writeElementAttributes(com_spec_tag, com_spec)
        self.writeSenderComSpec(com_spec_tag, com_spec)
        self.setInitValue(com_spec_tag, com_spec.init_value)
            
    def writeServerComSpec(self, com_specs_tag: ET.Element, com_spec: ServerComSpec):
        com_spec_tag = ET.SubElement(com_specs_tag, "SERVER-COM-SPEC")
        self.writeElementAttributes(com_spec_tag, com_spec)
        self.writeSenderComSpec(com_spec_tag, com_spec)

        self.setChildOptionalRefElement(com_spec_tag, "OPERATION-REF", com_spec.operation_ref)
        self.setChildOptionalElementNumberValue(com_spec_tag, "QUEUE-LENGTH",    com_spec.queue_length)
    
    def writePPortComSpec(self, com_specs_tag: ET.Element, com_spec: PPortComSpec):
        if isinstance(com_spec, NonqueuedSenderComSpec):
            self.writeNonqueuedSenderComSpec(com_specs_tag, com_spec)
        elif isinstance(com_spec, ServerComSpec):
            self.writeServerComSpec(com_specs_tag, com_spec)
        else:
            raise NotImplementedError("Unsupported PPortComSpec %s" % type(com_spec))
        
    def writeReceiverComSpec(self, com_spec_tag: ET.Element, com_spec: ReceiverComSpec):
        self.setChildOptionalRefElement(com_spec_tag, "DATA-ELEMENT-REF", com_spec.data_element_ref)
        self.setSwDataDefProps(com_spec_tag, "NETWORK-REPRESENTATION", com_spec.network_representation)
        self.setChildOptionalElement(com_spec_tag, "HANDLE-OUT-OF-RANGE", com_spec.handle_out_of_range)
        self.setChildOptionalElementBooleanValue(com_spec_tag, "USES-END-TO-END-PROTECTION", com_spec.uses_end_to_end_protection)

    def writeSwValues(self, element: ET.Element, values: SwValues):
        if values.v is not None:
            self.setChildOptionalElement(element, "V", values.v)

    def writeSwValueCont(self, element: ET.Element, cont: SwValueCont):
        child_element = ET.SubElement(element, "SW-VALUE-CONT")
        self.setChildOptionalRefElement(child_element, "UNIT-REF", cont.unit_ref)
        if cont.sw_values_phys is not None:
            sw_values_phys_tag = ET.SubElement(child_element, "SW-VALUES-PHYS")
            self.writeSwValues(sw_values_phys_tag, cont.sw_values_phys)

    def writeValueSpecification(self, element: ET.Element, value_spec: ValueSpecification):
        self.writeElementAttributes(element, value_spec)
        if value_spec.short_label is not None:
            self.setChildOptionalElement(element, "SHORT-LABEL", value_spec.short_label)                                

    def setApplicationValueSpecification(self, element: ET.Element, value_spec: ApplicationValueSpecification):
        value_spec_tag = ET.SubElement(element, "APPLICATION-VALUE-SPECIFICATION")
        self.writeValueSpecification(value_spec_tag, value_spec)
        self.setChildOptionalElement(value_spec_tag, "CATEGORY", value_spec.category)
        self.writeSwValueCont(value_spec_tag, value_spec.sw_value_cont)

    def setTextValueSpecification(self, element: ET.Element, value_spec: TextValueSpecification):
        value_spec_tag = ET.SubElement(element, "TEXT-VALUE-SPECIFICATION")
        self.writeValueSpecification(value_spec_tag, value_spec)
        self.setChildOptionalElement(value_spec_tag, "VALUE", value_spec.value)

    def setNumericalValueSpecification(self, element: ET.Element, value_spec: NumericalValueSpecification):
        value_spec_tag = ET.SubElement(element, "NUMERICAL-VALUE-SPECIFICATION")
        self.writeValueSpecification(value_spec_tag, value_spec)
        self.setChildOptionalElementNumberValue(value_spec_tag, "VALUE", value_spec.value)

    def setArrayValueSpecification(self, element: ET.Element, value_spec: ArrayValueSpecification):
        value_spec_tag = ET.SubElement(element, "ARRAY-VALUE-SPECIFICATION")
        self.writeValueSpecification(value_spec_tag, value_spec)
        sub_elements = value_spec.get_elements()
        if len(sub_elements) > 0:
            elements_tag = ET.SubElement(value_spec_tag, "ELEMENTS")
            for sub_element in sub_elements:
                if isinstance(sub_element, NumericalValueSpecification):
                    self.setNumericalValueSpecification(elements_tag, sub_element)
                else:
                    raise NotImplementedError("Unsupported element type of <%s> of ArrayValueSpecification" % type(sub_element))
                
    def setConstantReference(self, element: ET.Element, value_spec: ConstantReference):
        value_spec_tag = ET.SubElement(element, "CONSTANT-REFERENCE")
        self.writeValueSpecification(value_spec_tag, value_spec)
        self.setChildOptionalRefElement(value_spec_tag, "CONSTANT-REF", value_spec.constant_ref)

    def setValueSpecification(self, element: ET.Element, value_spec: ValueSpecification):
        if isinstance(value_spec, ApplicationValueSpecification):
            self.setApplicationValueSpecification(element, value_spec)
        elif isinstance(value_spec, TextValueSpecification):
            self.setTextValueSpecification(element, value_spec)
        elif isinstance(value_spec, ConstantReference):
            self.setConstantReference(element, value_spec)
        elif isinstance(value_spec, NumericalValueSpecification):
            self.setNumericalValueSpecification(element, value_spec)
        elif isinstance(value_spec, ArrayValueSpecification):
            self.setArrayValueSpecification(element, value_spec)
        else:
            raise NotImplementedError("Unsupported ValueSpecification %s" % type(value_spec))

    def setInitValue(self, element: ET.Element, init_value: ValueSpecification):
        if init_value is not None:
            child_element = ET.SubElement(element, "INIT-VALUE")
            self.setValueSpecification(child_element, init_value)

    def writeNonqueuedReceiverComSpec(self, element: ET.Element, com_spec: NonqueuedReceiverComSpec):
        child_element = ET.SubElement(element, "NONQUEUED-RECEIVER-COM-SPEC")
        self.writeElementAttributes(child_element, com_spec)
        self.writeReceiverComSpec(child_element, com_spec)
        self.setChildOptionalElementFloatValue(child_element, "ALIVE-TIMEOUT", com_spec.alive_timeout)
        self.setChildOptionalElementBooleanValue(child_element, "ENABLE-UPDATE", com_spec.enable_updated)
        self.setChildOptionalElementBooleanValue(child_element, "HANDLE-NEVER-RECEIVED", com_spec.handle_never_received)
        self.setChildOptionalElement(child_element, "HANDLE-TIMEOUT-TYPE", com_spec.handel_timeout_type)
        self.setInitValue(child_element, com_spec.init_value)

    def writeQueuedReceiverComSpec(self, element: ET.Element, com_spec: QueuedReceiverComSpec):
        child_element = ET.SubElement(element, "QUEUED-RECEIVER-COM-SPEC")
        self.writeElementAttributes(child_element, com_spec)
        self.writeReceiverComSpec(child_element, com_spec)
        self.setChildOptionalElementNumberValue(child_element, "QUEUE-LENGTH", com_spec.queue_length)
    
    def writeClientComSpec(self, element: ET.Element, com_spec: ClientComSpec):
        self.logger.debug("writeClientComSpec")
        child_element = ET.SubElement(element, "CLIENT-COM-SPEC")
        self.writeElementAttributes(child_element, com_spec)
        self.setChildOptionalRefElement(child_element, "OPERATION-REF", com_spec.operation_ref)

    def writeRPortComSpec(self, element: ET.Element, com_spec: RPortComSpec):
        if isinstance(com_spec, NonqueuedReceiverComSpec):
            self.writeNonqueuedReceiverComSpec(element, com_spec)
        elif isinstance(com_spec, QueuedReceiverComSpec):
            self.writeQueuedReceiverComSpec(element, com_spec)
        elif isinstance(com_spec, ClientComSpec):
            self.writeClientComSpec(element, com_spec)
        else:
            raise ValueError("Unsupported RPortComSpec %s" % type(com_spec))
    
    def writePPortPrototype(self, ports_tag: ET.Element, prototype: PPortPrototype):
        prototype_tag = ET.SubElement(ports_tag, "P-PORT-PROTOTYPE")

        self.writeIdentifiable(prototype_tag, prototype)
        self.logger.debug("writePPortPrototype %s" % prototype.short_name)

        com_specs = prototype.getProvidedComSpecs()
        if len(com_specs):
            com_specs_tag = ET.SubElement(prototype_tag, "PROVIDED-COM-SPECS")
            for com_spec in com_specs:
                self.writePPortComSpec(com_specs_tag, com_spec)

        self.setChildOptionalRefElement(prototype_tag, "PROVIDED-INTERFACE-TREF", prototype.provided_interface_tref)

    def writeRPortPrototype(self, ports_tag: ET.Element, prototype: RPortPrototype):
        prototype_tag = ET.SubElement(ports_tag, "R-PORT-PROTOTYPE")
        
        self.writeElementAttributes(prototype_tag, prototype)
        self.setShortName(prototype_tag, prototype.short_name)

        self.logger.debug("writeRPortPrototype %s" % prototype.short_name)
        
        com_specs = prototype.getRequiredComSpecs()
        if len(com_specs) > 0:
            com_specs_tag = ET.SubElement(prototype_tag, "REQUIRED-COM-SPECS")
            for com_spec in com_specs:
                self.writeRPortComSpec(com_specs_tag, com_spec)

        self.setChildOptionalRefElement(prototype_tag, "REQUIRED-INTERFACE-TREF", prototype.required_interface_tref)
    
    def writePortPrototypes(self, ports_tag: ET.Element, port_prototypes: List[PortPrototype]):
        for port_prototype in port_prototypes:
            if isinstance(port_prototype, PPortPrototype):
                self.writePPortPrototype(ports_tag, port_prototype)
            elif isinstance(port_prototype, RPortPrototype):
                self.writeRPortPrototype(ports_tag, port_prototype)
            else:
                self._raiseError("Invalid PortPrototype")
    
    def writeSwComponentType(self, element: ET.Element, sw_component: SwComponentType):
        self.writeIdentifiable(element, sw_component)
        port_prototypes = sw_component.getPortPrototype()
        if len(port_prototypes) > 0:
            ports_tag = ET.SubElement(element, "PORTS")
            self.writePortPrototypes(ports_tag, port_prototypes)

    def writeSwComponentPrototype(self, element: ET.Element, prototype: SwComponentPrototype):
        prototype_tag = ET.SubElement(element, "SW-COMPONENT-PROTOTYPE")
        self.writeElementAttributes(prototype_tag, prototype)
        self.setShortName(prototype_tag, prototype.short_name)
        self.setChildOptionalRefElement(prototype_tag, "TYPE-TREF", prototype.type_tref)

    def writeSwComponentPrototypes(self, element: ET.Element, sw_component: CompositionSwComponentType):
        components_tag = ET.SubElement(element, "COMPONENTS")
        for prototype in sw_component.getSwComponentPrototypes():
            self.writeSwComponentPrototype(components_tag, prototype)

    def writeAssemblySwConnector(self, element: ET.Element, sw_connector: AssemblySwConnector):
        connector_tag = ET.SubElement(element, "ASSEMBLY-SW-CONNECTOR")
        self.writeIdentifiable(connector_tag, sw_connector)

        if sw_connector.provider_iref is not None:
            provider_iref_tag = ET.SubElement(connector_tag, "PROVIDER-IREF")
            self.writeElementAttributes(provider_iref_tag, sw_connector.provider_iref)
            self.setChildOptionalRefElement(provider_iref_tag, "CONTEXT-COMPONENT-REF", sw_connector.provider_iref.context_component_ref)
            self.setChildOptionalRefElement(provider_iref_tag, "TARGET-P-PORT-REF", sw_connector.provider_iref.target_p_port_ref)

        if sw_connector.requester_iref is not None:
            requester_iref_tag = ET.SubElement(connector_tag, "REQUESTER-IREF")
            self.writeElementAttributes(requester_iref_tag, sw_connector.requester_iref)
            self.setChildOptionalRefElement(requester_iref_tag, "CONTEXT-COMPONENT-REF", sw_connector.requester_iref.context_component_ref)
            self.setChildOptionalRefElement(requester_iref_tag, "TARGET-R-PORT-REF", sw_connector.requester_iref.target_r_port_ref)

    def writeDelegationSwConnector(self, element: ET.Element, sw_connector: DelegationSwConnector):
        connector_tag = ET.SubElement(element, "DELEGATION-SW-CONNECTOR")
        self.writeIdentifiable(connector_tag, sw_connector)

        if sw_connector.inner_port_iref is not None:
            inner_port_iref_tag = ET.SubElement(connector_tag, "INNER-PORT-IREF")
            if isinstance(sw_connector.inner_port_iref, PPortInCompositionInstanceRef):
                instance_ref_tag = ET.SubElement(inner_port_iref_tag, "P-PORT-IN-COMPOSITION-INSTANCE-REF")
                self.setChildOptionalRefElement(instance_ref_tag, "CONTEXT-COMPONENT-REF", sw_connector.inner_port_iref.context_component_ref)
                self.setChildOptionalRefElement(instance_ref_tag, "TARGET-P-PORT-REF", sw_connector.inner_port_iref.target_p_port_ref)
            elif isinstance(sw_connector.inner_port_iref, RPortInCompositionInstanceRef):
                instance_ref_tag = ET.SubElement(inner_port_iref_tag, "R-PORT-IN-COMPOSITION-INSTANCE-REF")
                self.setChildOptionalRefElement(instance_ref_tag, "CONTEXT-COMPONENT-REF", sw_connector.inner_port_iref.context_component_ref)
                self.setChildOptionalRefElement(instance_ref_tag, "TARGET-R-PORT-REF", sw_connector.inner_port_iref.target_r_port_ref)
            else:
                self._raiseError("Invalid inner port of DelegationSwConnector <%s>" % sw_connector.short_name)

        if sw_connector.outer_port_ref is not None:
            self.setChildOptionalRefElement(connector_tag, "OUTER-PORT-REF", sw_connector.outer_port_ref)
            #self.writeChildOptionalRefElement(requester_iref_tag, "TARGET-R-PORT-REF", sw_connector.requester_iref.target_r_port_ref)
        
    def writeSwConnector(self, element: ET.Element, sw_connector: SwConnector):
        if isinstance(sw_connector, AssemblySwConnector):
            self.writeAssemblySwConnector(element, sw_connector)
        elif isinstance(sw_connector, DelegationSwConnector):
            self.writeDelegationSwConnector(element, sw_connector)
        else:
            raise NotImplementedError("Unsupported Sw Connector %s")

    def writeSwConnectors(self, element: ET.Element, sw_component: CompositionSwComponentType):
        sw_connectors = sw_component.getSwConnectors()
        if len(sw_connectors) > 0:
            connectors_tag = ET.SubElement(element, "CONNECTORS")
            for sw_connector in sw_connectors:
                self.writeSwConnector(connectors_tag, sw_connector)

    def writeDataTypeMappingSet(self, element: ET.Element, parent: CompositionSwComponentType):
        data_type_mappings = parent.getDataTypeMappings()
        if len(data_type_mappings) > 0:
            child_element = ET.SubElement(element, "DATA-TYPE-MAPPING-REFS")
            self.logger.debug("writeDataTypeMappingSet")
            for data_type_mapping in data_type_mappings:
                self.setChildOptionalRefElement(child_element, "DATA-TYPE-MAPPING-REF", data_type_mapping)
    
    def writeCompositionSwComponentType(self, parent: ET.Element, sw_component: CompositionSwComponentType):
        child_element = ET.SubElement(parent, "COMPOSITION-SW-COMPONENT-TYPE")

        self.writeSwComponentType(child_element, sw_component)
        self.writeSwComponentPrototypes(child_element, sw_component)
        self.writeSwConnectors(child_element, sw_component)
        self.writeDataTypeMappingSet(child_element, sw_component)

    def writeCompositionSwComponentTypes(self, element: ET.Element, ar_package: ARPackage):
        for sw_component in ar_package.getCompositionSwComponentTypes():
            self.writeCompositionSwComponentType(element, sw_component)

    def writeGeneralAnnotation(self, element: ET.Element, annotation: Annotation):
        self.setMultiLongName(element, "LABEL", annotation.label)

    def writeAnnotations(self, element: ET.Element, props: SwDataDefProps) :
        annotations = props.getAnnotations()
        if len(annotations) > 0:
            annotations_tag = ET.SubElement(element, "ANNOTATIONS")
            for annotation in annotations:
                annotation_tag = ET.SubElement(annotations_tag, "ANNOTATION")
                self.writeGeneralAnnotation(annotation_tag, annotation)

    def setSwDataDefProps(self, element: ET.Element, key: str, sw_data_def_props: SwDataDefProps):
        if sw_data_def_props is not None:
            child_element = ET.SubElement(element, key)
            sw_data_def_props_variants_tag = ET.SubElement(child_element, "SW-DATA-DEF-PROPS-VARIANTS")
            sw_data_def_props_conditional_tag = ET.SubElement(sw_data_def_props_variants_tag, "SW-DATA-DEF-PROPS-CONDITIONAL")
            self.writeElementAttributes(sw_data_def_props_conditional_tag, sw_data_def_props)
            self.writeAnnotations(sw_data_def_props_conditional_tag, sw_data_def_props)
            self.setChildOptionalRefElement(sw_data_def_props_conditional_tag, "BASE-TYPE-REF", sw_data_def_props.base_type_ref)
            self.setChildOptionalElement(sw_data_def_props_conditional_tag, "SW-CALIBRATION-ACCESS", sw_data_def_props.sw_calibration_access)
            self.setChildOptionalRefElement(sw_data_def_props_conditional_tag, "COMPU-METHOD-REF", sw_data_def_props.compu_method_ref)
            self.setChildOptionalElement(sw_data_def_props_conditional_tag, "SW-IMPL-POLICY", sw_data_def_props.sw_impl_policy)
            self.setChildOptionalRefElement(sw_data_def_props_conditional_tag, "IMPLEMENTATION-DATA-TYPE-REF", sw_data_def_props.implementation_data_type_ref)
            self.setChildOptionalRefElement(sw_data_def_props_conditional_tag, "DATA-CONSTR-REF", sw_data_def_props.data_constr_ref)

    def writeAutosarDataType(self, parent: ET.Element, data_type: AutosarDataType):
        self.writeARElement(parent, data_type)
        self.setSwDataDefProps(parent, "SW-DATA-DEF-PROPS", data_type.sw_data_def_props)

    def writeApplicationDataType(self, parent: ET.Element, data_type: ApplicationDataType):
        self.writeAutosarDataType(parent, data_type)

    def writeApplicationPrimitiveDataType(self, element: ET.Element, data_type: ApplicationPrimitiveDataType):
        self.logger.debug("writeApplicationPrimitiveDataType %s" % data_type.short_name)
        data_type_tag = ET.SubElement(element, "APPLICATION-PRIMITIVE-DATA-TYPE")
        self.writeApplicationDataType(data_type_tag, data_type)

    def writeApplicationRecordElements(self, element: ET.Element, data_type: ApplicationRecordDataType):
        record_elements = data_type.getApplicationRecordElements()
        if len(record_elements) > 0:
            elements_tag = ET.SubElement(element, "ELEMENTS")
            for record_element in record_elements:
                record_element_tag = ET.SubElement(elements_tag, "APPLICATION-RECORD-ELEMENT")
                self.writeIdentifiable(record_element_tag, record_element)
                self.setChildOptionalRefElement(record_element_tag, "TYPE-TREF", record_element.type_tref)

    def writeApplicationRecordDataType(self, element: ET.Element, data_type: ApplicationRecordDataType):
        data_type_tag = ET.SubElement(element, "APPLICATION-RECORD-DATA-TYPE")
        self.writeApplicationDataType(data_type_tag, data_type)
        self.writeApplicationRecordElements(data_type_tag, data_type)

    def writeApplicationDataTypes(self, parent: ET.Element, ar_package: ARPackage):
        for data_type in ar_package.getApplicationDataType():
            if isinstance(data_type, ApplicationPrimitiveDataType):
                self.writeApplicationPrimitiveDataType(parent, data_type)
            elif isinstance(data_type, ApplicationRecordDataType):
                self.writeApplicationRecordDataType(parent, data_type)
            else:
                raise NotImplementedError("Unsupported ApplicationDataType <%s>" % type(data_type))

    def writeBaseTypeDirectDefinition(self, element: ET.Element, base_type: BaseType):
        self.setChildOptionalElement(element, "BASE-TYPE-SIZE", str(base_type.base_type_definition.base_type_size))
        self.writeChildOptionalElementLiteral(element, "BASE-TYPE-ENCODING", base_type.base_type_definition.base_type_encoding)
        self.writeChildOptionalElementLiteral(element, "NATIVE-DECLARATION", base_type.base_type_definition.native_declaration)

    def writeSwBaseType(self, element: ET.Element, base_type: SwBaseType):
        data_type_tag = ET.SubElement(element, "SW-BASE-TYPE")
        self.writeIdentifiable(data_type_tag, base_type)
        self.writeBaseTypeDirectDefinition(data_type_tag, base_type)

    def writeCompuScaleConstantContents(self, element: ET.Element, contents: CompuScaleConstantContents):
        compu_const_tag = ET.SubElement(element, "COMPU-CONST")
        if isinstance(contents.compu_const.compu_const_content_type, CompuConstTextContent):
            self.setChildOptionalElement(compu_const_tag, "VT", contents.compu_const.compu_const_content_type.vt)

    def writeCompuNominatorDenominator(self, element: ET.Element, key: str, parent: CompuNominatorDenominator):
        child_element = ET.SubElement(element, key)
        for v in parent.get_vs():
            v_tag = ET.SubElement(child_element, "V")
            v_tag.text = v

    def writeCompuScaleRationalFormula(self, element: ET.Element, contents: CompuScaleRationalFormula):
        if contents.compu_rational_coeffs is not None:
            coeffs_tag = ET.SubElement(element, "COMPU-RATIONAL-COEFFS")
            if contents.compu_rational_coeffs.compu_numerator:
                self.writeCompuNominatorDenominator(coeffs_tag, "COMPU-NUMERATOR", contents.compu_rational_coeffs.compu_numerator)
            if contents.compu_rational_coeffs.compu_denominator:
                self.writeCompuNominatorDenominator(coeffs_tag, "COMPU-DENOMINATOR", contents.compu_rational_coeffs.compu_denominator)

    def writeCompuScaleContents(self, element: ET.Element, compu_scale: CompuScale):
        if isinstance(compu_scale.compu_scale_contents, CompuScaleConstantContents):
            self.writeCompuScaleConstantContents(element, compu_scale.compu_scale_contents)
        elif isinstance(compu_scale.compu_scale_contents, CompuScaleRationalFormula):
            self.writeCompuScaleRationalFormula(element, compu_scale.compu_scale_contents)
        else:
            raise NotImplementedError("Unsupported CompuScaleContents %s" % type(compu_scale.compu_scale_contents))

    def writeCompuScales(self, element: ET.Element, compu_scales: CompuScales):
        compu_scales_tag = ET.SubElement(element, "COMPU-SCALES")
        for compu_scale in compu_scales.getCompuScales():
            compu_scale_tag = ET.SubElement(compu_scales_tag, "COMPU-SCALE")
            self.writeChildLimitElement(compu_scale_tag, "LOWER-LIMIT", compu_scale.lower_limit)
            self.writeChildLimitElement(compu_scale_tag, "UPPER-LIMIT", compu_scale.upper_limit)
            self.writeCompuScaleContents(compu_scale_tag, compu_scale)

    def writeCompuInternalToPhys(self, element: ET.Element, compu_method: CompuMethod):
        if compu_method.compu_internal_to_phys is not None:
            compu_internal_to_phys_tag = ET.SubElement(element, "COMPU-INTERNAL-TO-PHYS")
            self.writeElementAttributes(compu_internal_to_phys_tag, compu_method.compu_internal_to_phys)
            if isinstance(compu_method.compu_internal_to_phys.compu_content, CompuScales):
                self.writeCompuScales(compu_internal_to_phys_tag, compu_method.compu_internal_to_phys.compu_content)

    def writeCompuMethod(self, element: ET.Element, compu_method: CompuMethod):
        compu_method_tag = ET.SubElement(element, "COMPU-METHOD")
        self.logger.debug("writeCompuMethods %s" % compu_method.short_name)
        self.writeIdentifiable(compu_method_tag, compu_method)
        self.setChildOptionalRefElement(compu_method_tag, "UNIT-REF", compu_method.unit_ref)
        self.writeCompuInternalToPhys(compu_method_tag, compu_method)

    def setApplicationValueSpecification(self, element: ET.Element, spec: ApplicationValueSpecification):
        spec_tag = ET.SubElement(element, "APPLICATION-VALUE-SPECIFICATION")
        self.setChildOptionalElement(spec_tag, "SHORT-LABEL", spec.short_label)
        self.setChildOptionalElement(spec_tag, "CATEGORY", spec.category)
        self.writeSwValueCont(spec_tag, spec.sw_value_cont)

    def writeRecordValueSpecification(self, element: ET.Element, spec: RecordValueSpecification):
        spec_tag = ET.SubElement(element, "RECORD-VALUE-SPECIFICATION")
        fields = spec.get_fields()
        if len(fields) > 0:
            fields_tag = ET.SubElement(spec_tag, "FIELDS")
            for field in fields:
                if isinstance(field, ApplicationValueSpecification):
                    self.setApplicationValueSpecification(fields_tag, field)
                else:
                    raise NotImplementedError("Unsupported Field <%s>" % type(field))

    def writeConstantSpecification(self, element: ET.Element, spec: ConstantSpecification):
        spec_tag = ET.SubElement(element, "CONSTANT-SPECIFICATION")
        self.writeIdentifiable(spec_tag, spec)

        if spec.value_spec is not None:
            value_spec_tag = ET.SubElement(spec_tag, "VALUE-SPEC")
            self.setValueSpecification(value_spec_tag, spec.value_spec)
                
    def writeInternalConstrs(self, element: ET.Element, parent: InternalConstrs):
        constrs_tag = ET.SubElement(element, "INTERNAL-CONSTRS")
        if parent.lower_limit is not None:
            self.writeChildLimitElement(constrs_tag, "LOWER-LIMIT", parent.lower_limit)
        if parent.upper_limit is not None:
            self.writeChildLimitElement(constrs_tag, "UPPER-LIMIT", parent.upper_limit)

    def writePhysConstrs(self, element: ET.Element, parent: PhysConstrs):
        constrs_tag = ET.SubElement(element, "PHYS-CONSTRS")
        if parent.lower_limit is not None:
            self.writeChildLimitElement(constrs_tag, "LOWER-LIMIT", parent.lower_limit)
        if parent.upper_limit is not None:
            self.writeChildLimitElement(constrs_tag, "UPPER-LIMIT", parent.upper_limit)
        self.setChildOptionalRefElement(constrs_tag, "UNIT-REF", parent.unit_ref)
                
    def writeDataConstrRules(self, element: ET.Element, parent: DataConstr):
        rules = parent.getDataConstrRules()
        if len(rules) > 0:
            rules_tag = ET.SubElement(element, "DATA-CONSTR-RULES")
            for rule in rules:
                rule_tag = ET.SubElement(rules_tag, "DATA-CONSTR-RULE")
                if rule.internal_constrs is not None:
                    self.writeInternalConstrs(rule_tag, rule.internal_constrs)
                if rule.phys_constrs is not None:
                    self.writePhysConstrs(rule_tag, rule.phys_constrs)

    def writeDataConstr(self, element: ET.Element, constr: DataConstr):
        child_element = ET.SubElement(element, "DATA-CONSTR")
        self.writeIdentifiable(child_element, constr)
        self.writeDataConstrRules(child_element, constr) 

    def writeUnit(self, element: ET.Element, unit: Unit):
        self.logger.debug("writeUnit %s" % unit.short_name)
        child_element = ET.SubElement(element, "UNIT")
        self.writeIdentifiable(child_element, unit)
        self.writeChildOptionalElementLiteral(child_element, "DISPLAY-NAME", unit.display_name)

    def setRModeInAtomicSwcInstanceRef(self, element: ET.Element, key: str, iref: RModeInAtomicSwcInstanceRef):
        child_element = ET.SubElement(element, key)
        self.setChildOptionalRefElement(child_element, "BASE", iref.base_ref)
        self.setChildOptionalRefElement(child_element, "CONTEXT-PORT-REF", iref.context_port_ref)
        self.setChildOptionalRefElement(child_element, "CONTEXT-MODE-DECLARATION-GROUP-PROTOTYPE-REF", iref.context_mode_declaration_group_prototype_ref)
        self.setChildOptionalRefElement(child_element, "TARGET-MODE-DECLARATION-REF", iref.target_mode_declaration_ref)

    def setPOperationInAtomicSwcInstanceRef(self, element: ET.Element, key: str, iref: POperationInAtomicSwcInstanceRef):
        child_element = ET.SubElement(element, key)
        self.setChildOptionalRefElement(child_element, "CONTEXT-P-PORT-REF", iref.context_p_port_ref)
        self.setChildOptionalRefElement(child_element, "TARGET-PROVIDED-OPERATION-REF", iref.target_provided_operation_ref)

    def setRTEEvent(self, element: ET.Element, event: RTEEvent):
        self.writeIdentifiable(element, event)
        irefs = event.getDisabledModeIRefs()
        if len(irefs) > 0:
            child_element = ET.SubElement(element, "DISABLED-MODE-IREFS")
            for iref in irefs:
                self.setRModeInAtomicSwcInstanceRef(child_element, "DISABLED-MODE-IREF", iref)
        self.setChildOptionalRefElement(element, "START-ON-EVENT-REF", event.start_on_event_ref)

    def setTimingEvent(self, element: ET.Element, event: TimingEvent):
        if event is not None:
            child_element = ET.SubElement(element, "TIMING-EVENT")
            self.setRTEEvent(child_element, event)
            self.setChildOptionalElementNumberValue(child_element, "PERIOD", event.period)

    def setOperationInvokedEvent(self, element: ET.Element, event: OperationInvokedEvent):
        if event is not None:
            child_element = ET.SubElement(element, "OPERATION-INVOKED-EVENT")
            self.setRTEEvent(child_element, event)
            self.setPOperationInAtomicSwcInstanceRef(child_element, "OPERATION-IREF", event.operation_iref)

    def setSwcModeSwitchEvent(self, element: ET.Element, event: SwcModeSwitchEvent):
        if event is not None:
            child_element = ET.SubElement(element, "SWC-MODE-SWITCH-EVENT")
            self.setRTEEvent(child_element, event)
            self.setChildOptionalElement(child_element, "ACTIVATION", event.activation)
            irefs = event.getModeIRefs()
            if len(irefs) > 0:
                mode_irefs_tag = ET.SubElement(child_element, "MODE-IREFS")
                for iref in irefs:
                    self.setRModeInAtomicSwcInstanceRef(mode_irefs_tag, "MODE-IREF", iref)

    def setDataReceivedEvent(self, element: ET.Element, event: DataReceivedEvent):
        if event is not None:
            child_element = ET.SubElement(element, "DATA-RECEIVED-EVENT")
            self.setRTEEvent(child_element, event)

    def writeRTEEvents(self, element: ET.Element, parent: SwcInternalBehavior):
        events = parent.getRteEvents()
        if len(events) > 0:
            child_element = ET.SubElement(element, "EVENTS")
            
            for event in events:
                if isinstance(event, TimingEvent):
                    self.setTimingEvent(child_element, event)
                elif isinstance(event, OperationInvokedEvent):
                    self.setOperationInvokedEvent(child_element, event)
                elif isinstance(event, SwcModeSwitchEvent):
                    self.setSwcModeSwitchEvent(child_element, event)
                elif isinstance(event, DataReceivedEvent):
                    self.setDataReceivedEvent(child_element, event)
                else:
                    raise NotImplementedError("Unsupported Event <%s>" % type(event))
                
    def writeExclusiveAreas(self, element: ET.Element, behavior: InternalBehavior):
        #areas = behavior.getExclusiveAreas():
        #if 
        #for area in behavior.getExclusiveAreas():
        #    self.writeExclusiveArea(element, )
        pass

    def writeDataTypeMappingRefs(self, element: ET.Element, behavior: InternalBehavior):
        refs = behavior.getDataTypeMappingRefs()
        if len(refs) > 0:
            refs_tag = ET.SubElement(element, "DATA-TYPE-MAPPING-REFS")
            for ref in refs:
                self.setChildOptionalRefElement(refs_tag, "DATA-TYPE-MAPPING-REF", ref)
           
    def writeInternalBehavior(self, element: ET.Element, behavior: InternalBehavior):
        self.writeExclusiveAreas(element, behavior)
        self.writeDataTypeMappingRefs(element, behavior)

    def writeExecutableEntity(self, element: ET.Element, entity: ExecutableEntity):
        if entity is not None:
            self.setChildOptionalElementFloatValue(element, "MINIMUM-START-INTERVAL", entity.minimum_start_interval)

    def setAutosarVariableRef(self, element: ET.Element, ref: AutosarVariableRef):
        if ref is not None:
            child_element = ET.SubElement(element, "ACCESSED-VARIABLE")
            if ref.autosar_variable_iref is not None:
                child_element = ET.SubElement(child_element, "AUTOSAR-VARIABLE-IREF")
                self.setChildOptionalRefElement(child_element, "PORT-PROTOTYPE-REF", ref.autosar_variable_iref.port_prototype_ref)
                self.setChildOptionalRefElement(child_element, "TARGET-DATA-PROTOTYPE-REF", ref.autosar_variable_iref.target_data_prototype_ref)
            if ref.local_variable_ref is not None:
                self.setChildOptionalRefElement(child_element, "LOCAL-VARIABLE-REF", ref.local_variable_ref)

    def setVariableAccess(self, element: ET.Element, access: VariableAccess):
        child_element = ET.SubElement(element, "VARIABLE-ACCESS")
        self.writeIdentifiable(child_element, access)
        self.setAutosarVariableRef(child_element, access.accessed_variable_ref)

    def writeDataReadAccesses(self, element: ET.Element, entity: RunnableEntity):
        #accesses = entity.getDataReadAccesses():
        pass
        
    def writeDataReceivePointByArguments(self, element: ET.Element, entity: RunnableEntity):
        accesses = entity.getDataReceivePointByArguments()
        if len(accesses) > 0:
            child_element = ET.SubElement(element, "DATA-RECEIVE-POINT-BY-ARGUMENTS")
            for access in accesses:
                self.setVariableAccess(child_element, access)

    def writeDataSendPoints(self, element: ET.Element, entity: RunnableEntity):
        points = entity.getDataSendPoints()
        if len(points) > 0:
            child_element = ET.SubElement(element, "DATA-SEND-POINTS")
            for point in points:
                self.setVariableAccess(child_element, point)

    def writeReadLocalVariables(self, element: ET.Element, entity: RunnableEntity):
        variables = entity.getReadLocalVariables()
        if len(variables) > 0:
            child_element = ET.SubElement(element, "READ-LOCAL-VARIABLES")
            for access in variables:
                self.setVariableAccess(child_element, access)

    def writeServerCallPoints(self, element: ET.Element, entity: RunnableEntity):
        points = entity.getServerCallPoints()
        if len(points) > 0:
            child_element = ET.SubElement(element, "SERVER-CALL-POINTS")
            for point in points:
                self.writeOperations

    def writeRunnableEntity(self, element: ET.Element, entity: RunnableEntity):
        if entity is not None:
            child_element = ET.SubElement(element, "RUNNABLE-ENTITY")
            self.writeIdentifiable(child_element, entity)
            self.writeExecutableEntity(child_element, entity)
            self.setChildOptionalElementBooleanValue(child_element, "CAN-BE-INVOKED-CONCURRENTLY", entity.can_be_invoked_concurrently)
            self.writeDataReceivePointByArguments(child_element, entity)
            self.writeDataSendPoints(child_element, entity)
            self.writeReadLocalVariables(child_element, entity)
            self.writeServerCallPoints(child_element, entity)
            self.setChildOptionalElement(child_element, "SYMBOL", entity.symbol)

    def writeRunnableEntities(self, element: ET.Element, behavior: SwcInternalBehavior):
        entities = behavior.getRunnableEntities()
        if len(entities) > 0:
            runnables_tag = ET.SubElement(element, "RUNNABLES")
            for entity in entities:
                if isinstance(entity, RunnableEntity):
                    self.writeRunnableEntity(runnables_tag, entity)
                else:
                    raise NotImplementedError("Unsupported RunnableEntity <%s>" % type(entity))
                
    def writeExplicitInterRunnableVariables(self, element: ET.Element, behavior: SwcInternalBehavior):
        prototypes = behavior.getExplicitInterRunnableVariables()
        if len(prototypes) > 0:
            child_element = ET.SubElement(element, "EXPLICIT-INTER-RUNNABLE-VARIABLES")
            for prototype in prototypes:
                if isinstance(prototype, VariableDataPrototype):
                    self.writeVariableDataPrototype(child_element, prototype)
                else:
                    self._raiseError("Unsupported ExplicitInterRunnableVariables <%s>" % type(prototype))

    def writePerInstanceMemories(self, element: ET.Element, behavior: SwcInternalBehavior):
        memories = behavior.getPerInstanceMemories()
        if len(memories) > 0:
            memories_tag = ET.SubElement(element, "PER-INSTANCE-MEMORYS")
            for memory in memories:
                child_element = ET.SubElement(memories_tag, "PER-INSTANCE-MEMORY")
                self.writeIdentifiable(child_element, memory)
                self.setChildOptionalElement(child_element, "INIT-VALUE", memory.init_value)
                self.setSwDataDefProps(child_element, "SW-DATA-DEF-PROPS", memory.sw_data_def_props)
                self.setChildOptionalElement(child_element, "TYPE", memory.type)
                self.setChildOptionalElement(child_element, "TYPE-DEFINITION", memory.type_definition)

    def writeParameterDataPrototype(self, element: ET.Element, prototype: ParameterDataPrototype):
        child_element = ET.SubElement(element, "PARAMETER-DATA-PROTOTYPE")
        self.writeIdentifiable(child_element, prototype)
        self.writeAutosarDataPrototype(child_element, prototype)
        self.setInitValue(child_element, prototype.init_value)

    def writeParameterDataPrototypes(self, element: ET.Element, behavior: SwcInternalBehavior):
        prototypes = behavior.getParameterDataPrototypes()
        if len(prototypes) > 0:
            child_element = ET.SubElement(element, "PER-INSTANCE-PARAMETERS")
            for prototype in prototypes:
                self.writeParameterDataPrototype(child_element, prototype)

    def writePortAPIOptions(self, element: ET.Element, behavior: SwcInternalBehavior):
        options = behavior.getPortAPIOptions()
        if len(options) > 0:
            port_api_options_tag = ET.SubElement(element, "PORT-API-OPTIONS")
            for option in options:
                child_element = ET.SubElement(port_api_options_tag, "PORT-API-OPTION")
                self.setChildOptionalElementBooleanValue(child_element, "ENABLE-TAKE-ADDRESS", option.enable_take_address)
                self.setChildOptionalElementBooleanValue(child_element, "INDIRECT-API", option.indirect_API)
                self.setChildOptionalRefElement(child_element, "PORT-REF", option.port_ref)

    def writeSwcInternalBehavior(self, element: ET.Element, behavior: SwcInternalBehavior):
        self.logger.debug("writeSwInternalBehavior %s" % behavior.short_name)

        child_element = ET.SubElement(element, "SWC-INTERNAL-BEHAVIOR")
        self.writeIdentifiable(child_element, behavior)
        self.writeInternalBehavior(child_element, behavior)
        self.writeRTEEvents(child_element, behavior)
        self.writeExplicitInterRunnableVariables(child_element, behavior)
        self.setChildOptionalElement(child_element, "HANDLE-TERMINATION-AND-RESTART", behavior.handle_termination_and_restart)
        self.writePerInstanceMemories(child_element, behavior)
        self.writeParameterDataPrototypes(child_element, behavior)
        self.writePortAPIOptions(child_element, behavior)
        self.writeRunnableEntities(child_element, behavior)
        self.setChildOptionalElementBooleanValue(child_element, "SUPPORTS-MULTIPLE-INSTANTIATION", behavior.supports_multiple_instantiation)

    def writeAtomicSwComponentTypeInternalBehaviors(self, element: ET.Element, behavior: InternalBehavior):
        if behavior is not None:
            behaviors_tag = ET.SubElement(element, "INTERNAL-BEHAVIORS")
            if isinstance(behavior, SwcInternalBehavior):
                self.writeSwcInternalBehavior(behaviors_tag, behavior)
            else:
                self._raiseError("Unsupported Internal Behaviors <%s>" % type(behavior))

    def writeAtomicSwComponentType(self, element: ET.Element, sw_component: AtomicSwComponentType):
        self.writeSwComponentType(element, sw_component)
        self.writeAtomicSwComponentTypeInternalBehaviors(element, sw_component.internal_behavior)

    def writeComplexDeviceDriverSwComponentType(self, element: ET.Element, sw_component: ComplexDeviceDriverSwComponentType):
        self.logger.debug("writeComplexDeviceDriverSwComponentType %s" % sw_component.short_name)
        child_element = ET.SubElement(element, "COMPLEX-DEVICE-DRIVER-SW-COMPONENT-TYPE")
        self.writeAtomicSwComponentType(child_element, sw_component)

    def writeArtifactDescriptors(self, element: ET.Element, code_desc: Code):
        artifact_descriptors = code_desc.getArtifactDescriptors()
        if len(artifact_descriptors) > 0:
            artifact_descs_tag = ET.SubElement(element, "ARTIFACT-DESCRIPTORS")
            for artifact_desc in artifact_descriptors:
                artifact_desc_tag = ET.SubElement(artifact_descs_tag, "AUTOSAR-ENGINEERING-OBJECT")
                self.logger.debug("writeArtifactDescriptor %s", artifact_desc.short_label)
                self.writeElementAttributes(artifact_desc_tag, artifact_desc)
                self.setChildOptionalElement(artifact_desc_tag, "SHORT-LABEL", artifact_desc.short_label)
                self.setChildOptionalElement(artifact_desc_tag, "CATEGORY", artifact_desc.category)
            
    def writeCodeDescriptors(self, element: ET.Element, impl: Implementation):
        codes = impl.getCodeDescriptors()
        if len(codes) > 0:
            code_descriptors_tag = ET.SubElement(element, "CODE-DESCRIPTORS")
            for code in codes:
                child_element = ET.SubElement(code_descriptors_tag, "CODE")
                self.writeIdentifiable(child_element, code)
                self.logger.debug("writeCodeDescriptor %s" % code.short_name)
                self.writeArtifactDescriptors(child_element, code)

    def writeMemorySections(self, element: ET.Element, consumption: ResourceConsumption):
        memory_sections = consumption.getMemorySections()
        if len(memory_sections) > 0:
            sections_tag = ET.SubElement(element, "MEMORY-SECTIONS")
            for memory_section in memory_sections:
                child_element = ET.SubElement(sections_tag, "MEMORY-SECTION")
                self.writeIdentifiable(child_element, memory_section)
                self.setChildOptionalElement(child_element, "ALIGNMENT", memory_section.alignment)
                self.setChildOptionalElementNumberValue(child_element, "SIZE", memory_section.size)
                self.setChildOptionalRefElement(child_element, "SW-ADDRMETHOD-REF", memory_section.sw_addr_method_ref)
                self.logger.debug("writeMemorySections %s" % memory_section.short_name)

    def writeResourceConsumption(self, element: ET.Element, consumption: ResourceConsumption):
        if consumption is not None:
            child_element = ET.SubElement(element, "RESOURCE-CONSUMPTION")
            self.writeIdentifiable(child_element, consumption)
            self.writeMemorySections(child_element, consumption)

    def writeImplementation(self, element: ET.Element, impl: Implementation):
        self.writeIdentifiable(element, impl)
        self.writeCodeDescriptors(element, impl)
        self.setChildOptionalElement(element, "PROGRAMMING-LANGUAGE", impl.programming_language)
        self.writeResourceConsumption(element, impl.resource_consumption)
        self.setChildOptionalElement(element, "SW-VERSION", impl.sw_version)
        self.setChildOptionalRefElement(element, "SWC-BSW-MAPPING-REF", impl.swc_bsw_mapping_ref)
        self.setChildOptionalElementNumberValue(element, "VENDOR-ID", impl.vendor_id)

    def writeSwcImplementation(self, element: ET.Element, impl: SwcImplementation):
        self.logger.debug("writeSwcImplementation %s" % impl.short_name)
        child_element = ET.SubElement(element, "SWC-IMPLEMENTATION")
        self.writeImplementation(child_element, impl)
        self.setChildOptionalRefElement(child_element, "BEHAVIOR-REF", impl.behavior_ref)

    def writeEndToEndProtectionSet(self, element: ET.Element, protection_set: EndToEndProtectionSet):
        self.logger.debug("writeEndToEndProtectionSet %s" % protection_set.short_name)
        child_element = ET.SubElement(element, "END-TO-END-PROTECTION-SET")
        self.writeIdentifiable(child_element, protection_set)

    def writeAutosarDataPrototype(self, element: ET.Element, prototype: AutosarDataPrototype):
        self.setChildOptionalRefElement(element, "TYPE-TREF", prototype.type_tref)

    def writeVariableDataPrototype(self, element: ET.Element, prototype: VariableDataPrototype):
        self.logger.debug("writeVariableDataPrototype %s" % prototype.short_name)
        child_element = ET.SubElement(element, "VARIABLE-DATA-PROTOTYPE")
        self.writeIdentifiable(child_element, prototype)
        self.setSwDataDefProps(child_element, "SW-DATA-DEF-PROPS", prototype.sw_data_def_props)
        self.writeAutosarDataPrototype(child_element, prototype)
        self.setInitValue(child_element, prototype.init_value)

    def writeDataElements(self, element: ET.Element, sr_interface: SenderReceiverInterface):
        data_elements = sr_interface.getDataElements()
        if len(data_elements) > 0:
            data_elements_tag = ET.SubElement(element, "DATA-ELEMENTS")
            for data_element in data_elements:
                if isinstance(data_element, VariableDataPrototype):
                    self.writeVariableDataPrototype(data_elements_tag, data_element)
                else:
                    self._raiseError("Unsupported Data Element <%s>" % type(data_element))

    def writeSenderReceiverInterface(self, element: ET.Element, sr_interface: SenderReceiverInterface):
        self.logger.debug("writeSenderReceiverInterface %s" % sr_interface.short_name)
        child_element = ET.SubElement(element, "SENDER-RECEIVER-INTERFACE")
        self.writeIdentifiable(child_element, sr_interface)
        self.setChildOptionalElementBooleanValue(child_element, "IS-SERVICE", sr_interface.is_service)
        self.writeDataElements(child_element, sr_interface)

    def writerBswModuleDescriptionImplementedEntry(self, element: ET.Element, desc: BswModuleDescription):
        entries = desc.getImplementedEntries()
        if len(entries) > 0:
            entries_tag = ET.SubElement(element, "PROVIDED-ENTRYS")
            for entry in entries:
                entry_tag = ET.SubElement(entries_tag, "BSW-MODULE-ENTRY-REF-CONDITIONAL")
                self.setChildOptionalRefElement(entry_tag, "BSW-MODULE-ENTRY-REF", entry)

    def writeBswModuleDescription(self, element: ET.Element, desc: BswModuleDescription):
        self.logger.debug("writeBswModuleDescription %s" % desc.short_name)
        child_element = ET.SubElement(element, "BSW-MODULE-DESCRIPTION")
        self.writeIdentifiable(child_element, desc)

        self.setChildOptionalElementNumberValue(child_element, "MODULE-ID", desc.module_id)
        self.writerBswModuleDescriptionImplementedEntry(child_element, desc)
        #self.readProvidedModeGroup(element, bsw_module_description)
        #self.readRequiredModeGroup(element, bsw_module_description)
        #self.readBswInternalBehavior(element, bsw_module_description)

    def writeBswModuleEntry(self, element: ET.Element, entry: BswModuleEntry):
        self.logger.debug("writeBswModuleDescription %s" % entry.short_name)
        child_element = ET.SubElement(element, "BSW-MODULE-ENTRY")
        self.writeIdentifiable(child_element, entry)

    def writeSwcBswMapping(self, element: ET.Element, mapping: SwcBswMapping):
        self.logger.debug("writeBswModuleDescription %s" % mapping.short_name)
        child_element = ET.SubElement(element, "BSW-MODULE-ENTRY")
        self.writeIdentifiable(child_element, mapping)

    def writeBswImplementation(self, element: ET.Element, impl: BswImplementation):
        self.logger.debug("writeBswModuleDescription %s" % impl.short_name)
        child_element = ET.SubElement(element, "BSW-MODULE-ENTRY")
        self.writeIdentifiable(child_element, impl)

    def writeImplementationDataType(self, element: ET.Element, data_type: ImplementationDataType):
        self.logger.debug("writeImplementationDataType %s" % data_type.short_name)
        child_element = ET.SubElement(element, "IMPLEMENTATION-DATA-TYPE")
        self.writeIdentifiable(child_element, data_type)
        self.setSwDataDefProps(child_element, "SW-DATA-DEF-PROPS", data_type.sw_data_def_props)

    def writeArgumentDataPrototypes(self, element: ET.Element, parent: ClientServerOperation):
        arguments = parent.getArgumentDataPrototypes()
        if len(arguments) > 0:
            arguments_tag = ET.SubElement(element, "ARGUMENTS")
            for prototype in arguments:
                child_element = ET.SubElement(arguments_tag, "ARGUMENT-DATA-PROTOTYPE")
                self.writeIdentifiable(child_element, prototype)
                self.setChildOptionalRefElement(child_element, "TYPE-TREF", prototype.type_tref)
                self.setChildOptionalElement(child_element, "DIRECTION", prototype.direction)

    def writePossibleErrorRefs(self, element: ET.Element, parent: ClientServerOperation):
        error_refs = parent.getPossbileErrorRefs()
        if len(error_refs) > 0:
            error_refs_tag = ET.SubElement(element, "POSSIBLE-ERROR-REFS")
            for error_ref in error_refs:
                self.setChildOptionalRefElement(error_refs_tag, "POSSIBLE-ERROR-REF", error_ref)

    def writeClientServerOperation(self, element: ET.Element, operation: ClientServerOperation):
        self.logger.debug("writeClientServerOperation %s" % operation.short_name)
        child_element = ET.SubElement(element, "CLIENT-SERVER-OPERATION")
        self.writeIdentifiable(child_element, operation)
        self.writeArgumentDataPrototypes(child_element, operation)
        self.writePossibleErrorRefs(child_element, operation)

    def writeOperations(self, element: ET.Element, parent: ClientServerInterface):
        operations = parent.getOperations()
        if len(operations) > 0:
            operations_tag = ET.SubElement(element, "OPERATIONS")
            for operation in operations:
                if isinstance(operation, ClientServerOperation):
                    self.writeClientServerOperation(operations_tag, operation)
                else:
                    self._raiseError("Unsupported Operation <%s>" % type(operation))

    def writeApplicationError(self, element: ET.Element, error: ApplicationError):
        self.logger.debug("writeApplicationError %s" % error.short_name)
        child_element = ET.SubElement(element, "APPLICATION-ERROR")
        self.writeIdentifiable(child_element, error)
        self.setChildOptionalElementNumberValue(child_element, "ERROR-CODE", error.error_code)

    def writePossibleErrors(self, element: ET.Element, parent: ClientServerInterface):
        errors = parent.getPossibleErrors()
        if len(errors) > 0:
            errors_tag = ET.SubElement(element, "POSSIBLE-ERRORS")
            for error in errors:
                if isinstance(error, ApplicationError):
                    self.writeApplicationError(errors_tag, error)
                else:
                    self._raiseError("Unsupported PossibleError %s" % type(error))

    def writeClientServerInterface(self, element: ET.Element, cs_interface: ClientServerInterface):
        self.logger.debug("writeClientServerInterface %s" % cs_interface.short_name)
        child_element = ET.SubElement(element, "CLIENT-SERVER-INTERFACE")
        self.writeIdentifiable(child_element, cs_interface)
        self.setChildOptionalElementBooleanValue(child_element, "IS-SERVICE", cs_interface.is_service)
        self.writeOperations(child_element, cs_interface)
        self.writePossibleErrors(child_element, cs_interface)

    def writeApplicationSwComponentType(self, element: ET.Element, sw_component: ApplicationSwComponentType):
        self.logger.debug("writeApplicationSwComponentType %s" % sw_component.short_name)
        child_element = ET.SubElement(element, "APPLICATION-SW-COMPONENT-TYPE")
        self.writeAtomicSwComponentType(child_element, sw_component)

    def writeEcuAbstractionSwComponentType(self, element: ET.Element, sw_component: EcuAbstractionSwComponentType):
        self.logger.debug("writeEcuAbstractionSwComponentType %s" % sw_component.short_name)
        child_element = ET.SubElement(element, "ECU-ABSTRACTION-SW-COMPONENT-TYPE")
        self.writeAtomicSwComponentType(child_element, sw_component)

    def writeARPackageElement(self, element: ET.Element, ar_element: ARElement):
        if isinstance(ar_element, ComplexDeviceDriverSwComponentType):
            self.writeComplexDeviceDriverSwComponentType(element, ar_element)
        elif isinstance(ar_element, SwcImplementation):
            self.writeSwcImplementation(element, ar_element)
        elif isinstance(ar_element, CompositionSwComponentType):
            self.writeCompositionSwComponentType(element, ar_element)
        elif isinstance(ar_element, ApplicationPrimitiveDataType):
            self.writeApplicationPrimitiveDataType(element, ar_element)
        elif isinstance(ar_element, ApplicationRecordDataType):
            self.writeApplicationRecordDataType(element, ar_element)
        elif isinstance(ar_element, SwBaseType):
            self.writeSwBaseType(element, ar_element)
        elif isinstance(ar_element, CompuMethod):
            self.writeCompuMethod(element, ar_element)
        elif isinstance(ar_element, ConstantSpecification):
            self.writeConstantSpecification(element, ar_element)
        elif isinstance(ar_element, DataConstr):
            self.writeDataConstr(element, ar_element)
        elif isinstance(ar_element, EndToEndProtectionSet):
            self.writeEndToEndProtectionSet(element, ar_element)
        elif isinstance(ar_element, SenderReceiverInterface):
            self.writeSenderReceiverInterface(element, ar_element)
        elif isinstance(ar_element, Unit):
            self.writeUnit(element, ar_element)
        elif isinstance(ar_element, BswModuleDescription):
            self.writeBswModuleDescription(element, ar_element)
        elif isinstance(ar_element, BswModuleEntry):
            self.writeBswModuleEntry(element, ar_element)
        elif isinstance(ar_element, SwcBswMapping):
            self.writeSwcBswMapping(element, ar_element)
        elif isinstance(ar_element, BswImplementation):
            self.writeBswImplementation(element, ar_element)
        elif isinstance(ar_element, ImplementationDataType):
            self.writeImplementationDataType(element, ar_element)
        elif isinstance(ar_element, ClientServerInterface):
            self.writeClientServerInterface(element, ar_element)
        elif isinstance(ar_element, ApplicationSwComponentType):
            self.writeApplicationSwComponentType(element, ar_element)
        elif isinstance(ar_element, EcuAbstractionSwComponentType):
            self.writeEcuAbstractionSwComponentType(element, ar_element)
        else:
            raise NotImplementedError("Unsupported Elements of ARPackage <%s>" % type(ar_element))
        
    def writeARPackages(self, element: ET.Element, pkgs: List[ARPackage]):
        if len(pkgs) > 0:
            pkgs_tag = ET.SubElement(element, "AR-PACKAGES")

            for pkg in pkgs:
                pkg_tag  = ET.SubElement(pkgs_tag, "AR-PACKAGE")
            
                self.writeIdentifiable(pkg_tag, pkg)
                self.logger.debug("writeARPackage %s" % pkg.full_name)

                if pkg.getTotalElement() > 0:
                    elements_tag = ET.SubElement(pkg_tag, "ELEMENTS")

                    for ar_element in pkg.getElements():
                        if not isinstance(ar_element, ARPackage):
                            self.writeARPackageElement(elements_tag, ar_element)

                self.writeARPackages(pkg_tag, pkg.getARPackages())

    def patch_xml(self, xml: str) -> str:
        xml = xml.replace("<SW-DATA-DEF-PROPS-CONDITIONAL/>","<SW-DATA-DEF-PROPS-CONDITIONAL></SW-DATA-DEF-PROPS-CONDITIONAL>")
        xml = xml.replace("<ELEMENTS/>","")
        return xml

    def saveToFile(self, filename, root: ET.Element):
        xml = ET.tostring(root, encoding = "UTF-8", xml_declaration = True, short_empty_elements = False)
        
        dom = minidom.parseString(xml.decode())
        xml = dom.toprettyxml(indent = "  ", encoding = "UTF-8")

        text = self.patch_xml(xml.decode())
    
        with open(filename, "w") as f_out:
            #f_out.write(xml.decode())
            f_out.write(text)

    def save(self, filename, document: AUTOSAR):
        self.logger.info("Save %s ..." % filename)

        root = ET.Element("AUTOSAR", self.nsmap)
        root.attrib["xmlns:xsi"] = "http://www.w3.org/2001/XMLSchema-instance"
        root.attrib["xsi:schemaLocation"] = document.schema_location
        
        self.writeARPackages(root, document.getARPackages())

        self.saveToFile(filename, root)
        