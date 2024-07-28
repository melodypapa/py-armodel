import logging
import xml.etree.cElementTree as ET
import re

from xml.dom import minidom
from typing import List

from armodel.models.data_def_properties import ValueList
from armodel.models.multilanguage_data import MultiLanguageOverviewParagraph, MultilanguageLongName

from ..models.record_layout import SwRecordLayout, SwRecordLayoutGroup, SwRecordLayoutV
from ..models.service_mapping import RoleBasedPortAssignment
from ..models.service_needs import NvBlockNeeds, RoleBasedDataAssignment
from ..models.data_prototype import ApplicationArrayElement, ApplicationCompositeElementDataPrototype, ApplicationRecordElement, AutosarDataPrototype, DataPrototype, ParameterDataPrototype, VariableDataPrototype
from ..models.bsw_module_template import BswInternalBehavior, BswModuleDescription, BswModuleEntity, BswModuleEntry
from ..models.ar_package import AUTOSAR
from ..models.sw_component import ApplicationSwComponentType, AtomicSwComponentType, ComplexDeviceDriverSwComponentType, DataReceivedEvent, EcuAbstractionSwComponentType, InternalTriggerOccurredEvent, OperationInvokedEvent, ParameterAccess, PortAPIOption, PortGroup, RTEEvent, ServerCallPoint, ServiceDependency, SwcModeSwitchEvent, SwcServiceDependency, SynchronousServerCallPoint, VariableAccess
from ..models.ar_object import ARBoolean, ARFloat, ARNumerical
from ..models.ar_package import ARPackage
from ..models.ar_ref import ApplicationCompositeElementInPortInterfaceInstanceRef, AutosarParameterRef, AutosarVariableRef, InnerPortGroupInCompositionInstanceRef, POperationInAtomicSwcInstanceRef, PPortInCompositionInstanceRef, RModeInAtomicSwcInstanceRef, ROperationInAtomicSwcInstanceRef, RPortInCompositionInstanceRef, RVariableInAtomicSwcInstanceRef, TRefType, VariableDataPrototypeInSystemInstanceRef
from ..models.calibration import SwAxisGrouped, SwAxisIndividual, SwCalprmAxis, SwCalprmAxisSet, SwValueCont, SwValues
from ..models.common_structure import ApplicationValueSpecification, ArrayValueSpecification, ConstantReference, ModeDeclarationGroupPrototype, NumericalValueSpecification, RecordValueSpecification, TextValueSpecification, ValueSpecification
from ..models.communication import CompositeNetworkRepresentation, TransmissionAcknowledgementRequest
from ..models.data_dictionary import SwAddrMethod, SwDataDefProps
from ..models.datatype import ApplicationArrayDataType, ApplicationCompositeDataType, ApplicationDataType, ApplicationPrimitiveDataType, ApplicationRecordDataType, AutosarDataType, BaseType, BaseTypeDirectDefinition, ImplementationDataType, SwBaseType
from ..models.general_structure import ARElement, AdminData, Identifiable, Limit, MultilanguageReferrable, Referrable, Sdg, SwcBswMapping
from ..models.m2_msr import CompuConstTextContent, CompuMethod, CompuNominatorDenominator, CompuScale, CompuScaleConstantContents, CompuScaleRationalFormula, CompuScales
from ..models.port_prototype import ClientComSpec, NonqueuedReceiverComSpec, NonqueuedSenderComSpec, PPortComSpec, PPortPrototype, PortPrototype, QueuedReceiverComSpec, RPortComSpec, RPortPrototype, ReceiverComSpec, SenderComSpec, ServerComSpec
from ..models.sw_component import AssemblySwConnector, CompositionSwComponentType, DelegationSwConnector, SwComponentPrototype, SwComponentType, SwConnector
from ..models.annotation import Annotation
from ..models.end_to_end_protection import EndToEndDescription, EndToEndProtection, EndToEndProtectionSet, EndToEndProtectionVariablePrototype
from ..models.port_interface import ApplicationError, ClientServerInterface, ClientServerOperation, SenderReceiverInterface, TriggerInterface
from ..models.unit import Unit
from ..models.implementation import BswImplementation, Code, Implementation, SwcImplementation
from ..models.common_structure import ConstantSpecification, ExecutableEntity, InternalBehavior, ResourceConsumption
from ..models.sw_component import RunnableEntity, SwcInternalBehavior, TimingEvent
from ..models.ar_object import ARLiteral, ARObject
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

    def setChildElementOptionalValue(self, element: ET.Element, key: str, value: str):
        if value is not None:
            child_element = ET.SubElement(element, key)
            child_element.text = value

    def setChildElementOptionalNumberValue(self, element: ET.Element, key: str, value: str):
        if value is not None:
            child_element = ET.SubElement(element, key)
            child_element.text = str(value)

    def setChildElementOptionalNumericalValue(self, element: ET.Element, key: str, numerical: ARNumerical):
        if numerical is not None:
            child_element = ET.SubElement(element, key)
            self.writeElementAttributes(child_element, numerical)
            child_element.text = numerical.text

    def setChildElementOptionalLiteral(self, element: ET.Element, key: str, literal: ARLiteral):
        if literal is not None:
            child_element = ET.SubElement(element, key)
            self.writeElementAttributes(child_element, literal)
            if literal.value is not None:
                child_element.text = str(literal.value)

    def setChildElementOptionalRefType(self, parent: ET.Element, child_tag_name: str, ref: TRefType):
        if ref is not None:
            child_tag = ET.SubElement(parent, child_tag_name)
            if ref.dest is not None:
                child_tag.attrib['DEST'] = ref.dest
            if ref.value is not None:
                child_tag.text = ref.value

    def setChildElementOptionalFloatValue(self, element: ET.Element, key: str, value: ARFloat):
        if value is not None:
            child_element = ET.SubElement(element, key)
            child_element.text = value.text

    def setChildElementOptionalBooleanValue(self, element: ET.Element, key: str, value: ARBoolean) -> ET.Element:
        child_element = None
        if value is not None:
            child_element = ET.SubElement(element, key)
            self.writeElementAttributes(child_element, value)
            if value.value:
                child_element.text = "true"
            else:
                child_element.text = "false"
        return child_element

    def writeChildElementOptionalLiteral(self, element: ET.Element, key: str, value: ARLiteral) -> ET.Element:
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
            self.writeElementAttributes(limit_tag, limit)
            if limit.intervalType is not None:
                limit_tag.attrib['INTERVAL-TYPE'] = limit.intervalType
            limit_tag.text = limit.value
    
    def writeReferable(self, element: ET.Element, referrable: Referrable):
        self.writeElementAttributes(element, referrable)
        self.setShortName(element, referrable.short_name)

    def setMultiLongName(self, element: ET.Element, key: str, long_name: MultilanguageLongName):
        if long_name is not None:
            long_name_tag = ET.SubElement(element, key)
            self.writeElementAttributes(long_name_tag, long_name)
            for l4 in long_name.getL4s():
                l4_tag = ET.SubElement(long_name_tag, "L-4")
                self.writeElementAttributes(l4_tag, l4)
                if l4.l is not None:
                    l4_tag.attrib['L'] = l4.l
                l4_tag.text = l4.value

    def setMultiLanguageOverviewParagraph(self, element: ET.Element, key: str, paragraph: MultiLanguageOverviewParagraph):
        if paragraph is not None:
            long_name_tag = ET.SubElement(element, key)
            self.writeElementAttributes(long_name_tag, paragraph)
            for l2 in paragraph.getL2s():
                l2_tag = ET.SubElement(long_name_tag, "L-2")
                self.writeElementAttributes(l2_tag, l2)
                if l2.l is not None:
                    l2_tag.attrib['L'] = l2.l
                l2_tag.text = l2.value

    def writeMultilanguageReferrable(self, element: ET.Element, referrable: MultilanguageReferrable):
        self.writeReferable(element, referrable)
        if referrable.longName is not None:
            self.setMultiLongName(element, "LONG-NAME", referrable.longName)

    def writeAdminData(self, element: ET.Element, admin_data: AdminData):
        element = ET.SubElement(element, "ADMIN-DATA")
        self.writeSdg(element, admin_data)

    def writeIdentifiable(self, element: ET.Element, identifiable: Identifiable):
        self.writeMultilanguageReferrable(element, identifiable)
        self.setMultiLanguageOverviewParagraph(element, "DESC", identifiable.desc)
        self.setChildElementOptionalValue(element, "CATEGORY", identifiable.category)
        if identifiable.admin_data is not None:
            self.writeAdminData(element, identifiable.admin_data)

    def writeARElement(self, parent: ET.Element, ar_element: ARElement):
        self.writeIdentifiable(parent, ar_element)
    
    def writeTransmissionAcknowledgementRequest(self, element: ET.Element, acknowledge: TransmissionAcknowledgementRequest):
        if (acknowledge != None):
            child_element = ET.SubElement(element, "TRANSMISSION-ACKNOWLEDGE")
            self.writeElementAttributes(child_element, acknowledge)
            if acknowledge.timeout != None:
                self.setChildElementOptionalFloatValue(child_element, "TIMEOUT", acknowledge.timeout)

    def writeSenderComSpec(self, element: ET.Element, com_spec: SenderComSpec):
        representations = com_spec.getCompositeNetworkRepresentations()
        if len(representations) > 0:
            child_element = ET.SubElement(element, "COMPOSITE-NETWORK-REPRESENTATIONS")
            for representation in representations:
                self.setCompositeNetworkRepresentation(child_element, representation)
        self.setChildElementOptionalRefType(element, "DATA-ELEMENT-REF", com_spec.data_element_ref)
        self.setSwDataDefProps(element, "NETWORK-REPRESENTATION", com_spec.network_representation)
        self.setChildElementOptionalValue(element, "HANDLE-OUT-OF-RANGE", com_spec.handle_out_of_range)
        self.writeTransmissionAcknowledgementRequest(element, com_spec.transmission_acknowledge)
        self.setChildElementOptionalBooleanValue(element, "USES-END-TO-END-PROTECTION", com_spec.uses_end_to_end_protection)
    
    def writeNonqueuedSenderComSpec(self, com_specs_tag: ET.Element, com_spec: NonqueuedSenderComSpec):
        com_spec_tag = ET.SubElement(com_specs_tag, "NONQUEUED-SENDER-COM-SPEC")
        self.writeElementAttributes(com_spec_tag, com_spec)
        self.writeSenderComSpec(com_spec_tag, com_spec)
        self.setInitValue(com_spec_tag, com_spec.init_value)
            
    def writeServerComSpec(self, com_specs_tag: ET.Element, com_spec: ServerComSpec):
        com_spec_tag = ET.SubElement(com_specs_tag, "SERVER-COM-SPEC")
        self.writeElementAttributes(com_spec_tag, com_spec)
        self.setChildElementOptionalRefType(com_spec_tag, "OPERATION-REF", com_spec.operation_ref)
        self.setChildElementOptionalNumberValue(com_spec_tag, "QUEUE-LENGTH",    com_spec.queue_length)
    
    def writePPortComSpec(self, com_specs_tag: ET.Element, com_spec: PPortComSpec):
        if isinstance(com_spec, NonqueuedSenderComSpec):
            self.writeNonqueuedSenderComSpec(com_specs_tag, com_spec)
        elif isinstance(com_spec, ServerComSpec):
            self.writeServerComSpec(com_specs_tag, com_spec)
        else:
            raise NotImplementedError("Unsupported PPortComSpec %s" % type(com_spec))
        
    def setApplicationCompositeElementInPortInterfaceInstanceRef(self, element: ET.Element, key:str, iref: ApplicationCompositeElementInPortInterfaceInstanceRef):
        if iref is not None:
            child_element = ET.SubElement(element, key)
            self.setChildElementOptionalRefType(child_element, "ROOT-DATA-PROTOTYPE-REF", iref.root_data_prototype_ref)
            self.setChildElementOptionalRefType(child_element, "TARGET-DATA-PROTOTYPE-REF", iref.target_data_prototype_ref)
        return iref
        
    def setCompositeNetworkRepresentation(self, element: ET.Element, representation: CompositeNetworkRepresentation):
        if representation is not None:
            self.logger.debug("setCompositeNetworkRepresentation")
            child_element = ET.SubElement(element, "COMPOSITE-NETWORK-REPRESENTATION")
            self.setApplicationCompositeElementInPortInterfaceInstanceRef(child_element, "LEAF-ELEMENT-IREF", representation.leaf_element_iref)
            self.setSwDataDefProps(child_element, "NETWORK-REPRESENTATION", representation.network_representation)
        
    def writeReceiverComSpec(self, element: ET.Element, com_spec: ReceiverComSpec):
        representations = com_spec.getCompositeNetworkRepresentations()
        if len(representations) > 0:
            child_element = ET.SubElement(element, "COMPOSITE-NETWORK-REPRESENTATIONS")
            for representation in representations:
                self.setCompositeNetworkRepresentation(child_element, representation)
        self.setChildElementOptionalRefType(element, "DATA-ELEMENT-REF", com_spec.data_element_ref)
        self.setSwDataDefProps(element, "NETWORK-REPRESENTATION", com_spec.network_representation)
        self.setChildElementOptionalValue(element, "HANDLE-OUT-OF-RANGE", com_spec.handle_out_of_range)
        self.setChildElementOptionalBooleanValue(element, "USES-END-TO-END-PROTECTION", com_spec.uses_end_to_end_protection)

    def setSwValues(self, element: ET.Element, key: str, sw_values: SwValues):
        if sw_values is not None:
            child_element = ET.SubElement(element, key)
            self.writeElementAttributes(child_element, sw_values)
            for v in sw_values.getVs():
                self.setChildElementOptionalFloatValue(child_element, "V", v)
            self.setChildElementOptionalValue(child_element, "VT", sw_values.vt)

    def setValueList(self, element: ET.Element, key: str, value_list: ValueList):
        if value_list is not None:
            child_element = ET.SubElement(element, key)
            self.writeElementAttributes(child_element, value_list)
            self.setChildElementOptionalFloatValue(child_element, "V", value_list.v)

    def writeSwValueCont(self, element: ET.Element, cont: SwValueCont):
        child_element = ET.SubElement(element, "SW-VALUE-CONT")
        self.writeElementAttributes(child_element, cont)
        self.setChildElementOptionalRefType(child_element, "UNIT-REF", cont.unitRef)
        self.setValueList(child_element, "SW-ARRAYSIZE", cont.swArraysize)
        self.setSwValues(child_element, "SW-VALUES-PHYS", cont.swValuesPhys)

    def writeValueSpecification(self, element: ET.Element, value_spec: ValueSpecification):
        self.writeElementAttributes(element, value_spec)
        if value_spec.short_label is not None:
            self.setChildElementOptionalValue(element, "SHORT-LABEL", value_spec.short_label)                                

    def setApplicationValueSpecification(self, element: ET.Element, value_spec: ApplicationValueSpecification):
        value_spec_tag = ET.SubElement(element, "APPLICATION-VALUE-SPECIFICATION")
        self.writeValueSpecification(value_spec_tag, value_spec)
        self.setChildElementOptionalValue(value_spec_tag, "CATEGORY", value_spec.category)
        self.writeSwValueCont(value_spec_tag, value_spec.sw_value_cont)

    def setTextValueSpecification(self, element: ET.Element, value_spec: TextValueSpecification):
        value_spec_tag = ET.SubElement(element, "TEXT-VALUE-SPECIFICATION")
        self.writeValueSpecification(value_spec_tag, value_spec)
        self.setChildElementOptionalValue(value_spec_tag, "VALUE", value_spec.value)

    def setNumericalValueSpecification(self, element: ET.Element, value_spec: NumericalValueSpecification):
        value_spec_tag = ET.SubElement(element, "NUMERICAL-VALUE-SPECIFICATION")
        self.writeValueSpecification(value_spec_tag, value_spec)
        self.setChildElementOptionalFloatValue(value_spec_tag, "VALUE", value_spec.value)

    def setArrayValueSpecification(self, element: ET.Element, value_spec: ArrayValueSpecification):
        value_spec_tag = ET.SubElement(element, "ARRAY-VALUE-SPECIFICATION")
        self.writeValueSpecification(value_spec_tag, value_spec)
        sub_elements = value_spec.get_elements()
        if len(sub_elements) > 0:
            elements_tag = ET.SubElement(value_spec_tag, "ELEMENTS")
            for sub_element in sub_elements:
                if isinstance(sub_element, NumericalValueSpecification):
                    self.setNumericalValueSpecification(elements_tag, sub_element)
                elif isinstance(sub_element, ApplicationValueSpecification):
                    self.setApplicationValueSpecification(elements_tag, sub_element)
                else:
                    raise NotImplementedError("Unsupported element type of <%s> of ArrayValueSpecification" % type(sub_element))
                
    def setConstantReference(self, element: ET.Element, value_spec: ConstantReference):
        value_spec_tag = ET.SubElement(element, "CONSTANT-REFERENCE")
        self.writeValueSpecification(value_spec_tag, value_spec)
        self.setChildElementOptionalRefType(value_spec_tag, "CONSTANT-REF", value_spec.constant_ref)

    def setValueSpecification(self, element: ET.Element, value_spec: ValueSpecification):
        if value_spec is not None:
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
            elif isinstance(value_spec, RecordValueSpecification):
                self.setRecordValueSpecification(element, value_spec)
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
        self.setChildElementOptionalFloatValue(child_element, "ALIVE-TIMEOUT", com_spec.alive_timeout)
        self.setChildElementOptionalBooleanValue(child_element, "ENABLE-UPDATE", com_spec.enable_updated)
        self.setChildElementOptionalBooleanValue(child_element, "HANDLE-NEVER-RECEIVED", com_spec.handle_never_received)
        self.setChildElementOptionalValue(child_element, "HANDLE-TIMEOUT-TYPE", com_spec.handel_timeout_type)
        self.setInitValue(child_element, com_spec.init_value)

    def writeQueuedReceiverComSpec(self, element: ET.Element, com_spec: QueuedReceiverComSpec):
        child_element = ET.SubElement(element, "QUEUED-RECEIVER-COM-SPEC")
        self.writeElementAttributes(child_element, com_spec)
        self.writeReceiverComSpec(child_element, com_spec)
        self.setChildElementOptionalNumberValue(child_element, "QUEUE-LENGTH", com_spec.queue_length)
    
    def writeClientComSpec(self, element: ET.Element, com_spec: ClientComSpec):
        self.logger.debug("writeClientComSpec")
        child_element = ET.SubElement(element, "CLIENT-COM-SPEC")
        self.writeElementAttributes(child_element, com_spec)
        self.setChildElementOptionalRefType(child_element, "OPERATION-REF", com_spec.operation_ref)

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

        self.setChildElementOptionalRefType(prototype_tag, "PROVIDED-INTERFACE-TREF", prototype.provided_interface_tref)

    def writeRPortPrototype(self, ports_tag: ET.Element, prototype: RPortPrototype):
        self.logger.debug("writeRPortPrototype %s" % prototype.short_name)
        prototype_tag = ET.SubElement(ports_tag, "R-PORT-PROTOTYPE")
        self.writeIdentifiable(prototype_tag, prototype)
        com_specs = prototype.getRequiredComSpecs()
        if len(com_specs) > 0:
            com_specs_tag = ET.SubElement(prototype_tag, "REQUIRED-COM-SPECS")
            for com_spec in com_specs:
                self.writeRPortComSpec(com_specs_tag, com_spec)
        self.setChildElementOptionalRefType(prototype_tag, "REQUIRED-INTERFACE-TREF", prototype.required_interface_tref)
    
    def writePortPrototypes(self, ports_tag: ET.Element, port_prototypes: List[PortPrototype]):
        for port_prototype in port_prototypes:
            if isinstance(port_prototype, PPortPrototype):
                self.writePPortPrototype(ports_tag, port_prototype)
            elif isinstance(port_prototype, RPortPrototype):
                self.writeRPortPrototype(ports_tag, port_prototype)
            else:
                self._raiseError("Invalid PortPrototype")

    def writeInnerGroupIRef(self, element: ET.Element, inner_group_iref: InnerPortGroupInCompositionInstanceRef):
        child_element = ET.SubElement(element, "INNER-GROUP-IREF")
        self.setChildElementOptionalRefType(child_element, "CONTEXT-REF", inner_group_iref.contextRef)
        self.setChildElementOptionalRefType(child_element, "TARGET-REF", inner_group_iref.targetRef)

    def writePortGroupInnerGroupIRefs(self, element: ET.Element, parent: PortGroup):
        irefs = parent.getInnerGroupIRefs()
        if len(irefs) > 0:
            child_element = ET.SubElement(element, "INNER-GROUP-IREFS")
            for iref in irefs:
                self.writeInnerGroupIRef(child_element, iref)

    def writePortGroupOuterPortRefs(self, element: ET.Element, parent: PortGroup):
        refs = parent.getOuterPortRefs()
        if len(refs) > 0:
            outer_ports_element = ET.SubElement(element, "OUTER-PORTS")
            for ref in refs:
                child_element = ET.SubElement(outer_ports_element, "PORT-PROTOTYPE-REF-CONDITIONAL")
                self.setChildElementOptionalRefType(child_element, "PORT-PROTOTYPE-REF", ref)

    def writePortGroup(self, element: ET.Element, port_group: PortGroup):
        self.logger.debug("writePortGroup %s" % port_group.short_name)
        child_element = ET.SubElement(element, "PORT-GROUP")
        self.writeIdentifiable(child_element, port_group)
        self.writePortGroupInnerGroupIRefs(child_element, port_group)
        self.writePortGroupOuterPortRefs(child_element, port_group)

    def writeSwComponentTypePortGroups(self, element: ET.Element, parent: SwComponentType):
        port_groups = parent.getPortGroups()
        if len(port_groups) > 0:
            child_element = ET.SubElement(element, "PORT-GROUPS")
            for port_group in port_groups:
                self.writePortGroup(child_element, port_group)
    
    def writeSwComponentType(self, element: ET.Element, sw_component: SwComponentType):
        self.writeIdentifiable(element, sw_component)
        port_prototypes = sw_component.getPortPrototype()
        if len(port_prototypes) > 0:
            ports_tag = ET.SubElement(element, "PORTS")
            self.writePortPrototypes(ports_tag, port_prototypes)
        self.writeSwComponentTypePortGroups(element, sw_component)

    def writeSwComponentPrototype(self, element: ET.Element, prototype: SwComponentPrototype):
        prototype_tag = ET.SubElement(element, "SW-COMPONENT-PROTOTYPE")
        self.writeIdentifiable(prototype_tag, prototype)
        self.setChildElementOptionalRefType(prototype_tag, "TYPE-TREF", prototype.type_tref)

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
            self.setChildElementOptionalRefType(provider_iref_tag, "CONTEXT-COMPONENT-REF", sw_connector.provider_iref.context_component_ref)
            self.setChildElementOptionalRefType(provider_iref_tag, "TARGET-P-PORT-REF", sw_connector.provider_iref.target_p_port_ref)

        if sw_connector.requester_iref is not None:
            requester_iref_tag = ET.SubElement(connector_tag, "REQUESTER-IREF")
            self.writeElementAttributes(requester_iref_tag, sw_connector.requester_iref)
            self.setChildElementOptionalRefType(requester_iref_tag, "CONTEXT-COMPONENT-REF", sw_connector.requester_iref.context_component_ref)
            self.setChildElementOptionalRefType(requester_iref_tag, "TARGET-R-PORT-REF", sw_connector.requester_iref.target_r_port_ref)

    def writeDelegationSwConnector(self, element: ET.Element, sw_connector: DelegationSwConnector):
        connector_tag = ET.SubElement(element, "DELEGATION-SW-CONNECTOR")
        self.writeIdentifiable(connector_tag, sw_connector)

        if sw_connector.inner_port_iref is not None:
            inner_port_iref_tag = ET.SubElement(connector_tag, "INNER-PORT-IREF")
            if isinstance(sw_connector.inner_port_iref, PPortInCompositionInstanceRef):
                instance_ref_tag = ET.SubElement(inner_port_iref_tag, "P-PORT-IN-COMPOSITION-INSTANCE-REF")
                self.setChildElementOptionalRefType(instance_ref_tag, "CONTEXT-COMPONENT-REF", sw_connector.inner_port_iref.context_component_ref)
                self.setChildElementOptionalRefType(instance_ref_tag, "TARGET-P-PORT-REF", sw_connector.inner_port_iref.target_p_port_ref)
            elif isinstance(sw_connector.inner_port_iref, RPortInCompositionInstanceRef):
                instance_ref_tag = ET.SubElement(inner_port_iref_tag, "R-PORT-IN-COMPOSITION-INSTANCE-REF")
                self.setChildElementOptionalRefType(instance_ref_tag, "CONTEXT-COMPONENT-REF", sw_connector.inner_port_iref.context_component_ref)
                self.setChildElementOptionalRefType(instance_ref_tag, "TARGET-R-PORT-REF", sw_connector.inner_port_iref.target_r_port_ref)
            else:
                self._raiseError("Invalid inner port of DelegationSwConnector <%s>" % sw_connector.short_name)

        if sw_connector.outer_port_ref is not None:
            self.setChildElementOptionalRefType(connector_tag, "OUTER-PORT-REF", sw_connector.outer_port_ref)
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
                self.setChildElementOptionalRefType(child_element, "DATA-TYPE-MAPPING-REF", data_type_mapping)
    
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

    def setSwAxisIndividual(self, element: ET.Element, props: SwAxisIndividual):
        child_element = ET.SubElement(element, "SW-AXIS-INDIVIDUAL")
        self.writeElementAttributes(child_element, props)
        self.setChildElementOptionalRefType(child_element, "INPUT-VARIABLE-TYPE-REF", props.inputVariableTypeRef)
        self.setChildElementOptionalRefType(child_element, "COMPU-METHOD-REF", props.compuMethodRef)
        self.setChildElementOptionalNumericalValue(child_element, "SW-MAX-AXIS-POINTS", props.swMaxAxisPoints) 
        self.setChildElementOptionalNumericalValue(child_element, "SW-MIN-AXIS-POINTS", props.swMinAxisPoints)
        self.setChildElementOptionalRefType(child_element, "DATA-CONSTR-REF", props.dataConstrRef)

    def setSwAxisGrouped(self, element: ET.Element, props: SwAxisGrouped):
        child_element = ET.SubElement(element, "SW-AXIS-GROUPED")
        self.writeElementAttributes(child_element, props)
        self.setChildElementOptionalRefType(child_element, "SHARED-AXIS-TYPE-REF", props.sharedAxisTypeRef)

    def setSwCalprmAxis(self, element: ET.Element, axis: SwCalprmAxis):
        if axis is not None:
            child_element = ET.SubElement(element, "SW-CALPRM-AXIS")
            self.setChildElementOptionalNumericalValue(child_element, "SW-AXIS-INDEX", axis.swAxisIndex)
            self.setChildElementOptionalLiteral(child_element, "CATEGORY", axis.category)
            if axis.swCalprmAxisTypeProps is not None:
                if isinstance(axis.swCalprmAxisTypeProps, SwAxisIndividual):
                    self.setSwAxisIndividual(child_element, axis.swCalprmAxisTypeProps)
                elif isinstance(axis.swCalprmAxisTypeProps, SwAxisGrouped):
                    self.setSwAxisGrouped(child_element, axis.swCalprmAxisTypeProps)
                else:
                    self._raiseError("Unsupported SwCalprmAxisTypeProps %s" % type(axis.swCalprmAxisTypeProps))

    def setSwCalprmAxisSet(self, element: ET.Element, key: str, set: SwCalprmAxisSet):
        axises = set.getSwCalprmAxises()
        if len(axises) > 0:
            child_element = ET.SubElement(element, key)
            for axis in axises:
                self.setSwCalprmAxis(child_element, axis)

    def setSwDataDefProps(self, element: ET.Element, key: str, sw_data_def_props: SwDataDefProps):
        if sw_data_def_props is not None:
            child_element = ET.SubElement(element, key)
            self.writeElementAttributes(child_element, sw_data_def_props)
            sw_data_def_props_variants_tag = ET.SubElement(child_element, "SW-DATA-DEF-PROPS-VARIANTS")
            sw_data_def_props_conditional_tag = ET.SubElement(sw_data_def_props_variants_tag, "SW-DATA-DEF-PROPS-CONDITIONAL")
            self.writeElementAttributes(sw_data_def_props_conditional_tag, sw_data_def_props.conditional)
            self.writeAnnotations(sw_data_def_props_conditional_tag, sw_data_def_props)
            self.setChildElementOptionalRefType(sw_data_def_props_conditional_tag, "BASE-TYPE-REF", sw_data_def_props.baseTypeRef)
            self.setChildElementOptionalValue(sw_data_def_props_conditional_tag, "SW-CALIBRATION-ACCESS", sw_data_def_props.swCalibrationAccess)
            self.setSwCalprmAxisSet(sw_data_def_props_conditional_tag, "SW-CALPRM-AXIS-SET", sw_data_def_props.swCalprmAxisSet)
            self.setChildElementOptionalRefType(sw_data_def_props_conditional_tag, "COMPU-METHOD-REF", sw_data_def_props.compuMethodRef)
            self.setChildElementOptionalValue(sw_data_def_props_conditional_tag, "SW-IMPL-POLICY", sw_data_def_props.swImplPolicy)
            self.setChildElementOptionalRefType(sw_data_def_props_conditional_tag, "IMPLEMENTATION-DATA-TYPE-REF", sw_data_def_props.implementationDataTypeRef)
            self.setChildElementOptionalRefType(sw_data_def_props_conditional_tag, "DATA-CONSTR-REF", sw_data_def_props.dataConstrRef)
            self.setChildElementOptionalRefType(sw_data_def_props_conditional_tag, "SW-RECORD-LAYOUT-REF", sw_data_def_props.swRecordLayoutRef)
            self.setChildElementOptionalRefType(sw_data_def_props_conditional_tag, "VALUE-AXIS-DATA-TYPE-REF", sw_data_def_props.valueAxisDataTypeRef)
            self.setChildElementOptionalRefType(sw_data_def_props_conditional_tag, "UNIT-REF", sw_data_def_props.unitRef)
            

    def writeApplicationDataType(self, element: ET.Element, data_type: ApplicationDataType):
        self.writeAutosarDataType(element, data_type)

    def writeApplicationCompositeDataType(self, element: ET.Element, data_type: ApplicationCompositeDataType):
        self.writeApplicationDataType(element, data_type)

    def writeAutosarDataType(self, element: ET.Element, data_type: AutosarDataType):
        self.writeARElement(element, data_type)
        self.setSwDataDefProps(element, "SW-DATA-DEF-PROPS", data_type.sw_data_def_props)

    def writeApplicationPrimitiveDataType(self, element: ET.Element, data_type: ApplicationPrimitiveDataType):
        self.logger.debug("writeApplicationPrimitiveDataType %s" % data_type.short_name)
        data_type_tag = ET.SubElement(element, "APPLICATION-PRIMITIVE-DATA-TYPE")
        self.writeApplicationDataType(data_type_tag, data_type)

    def setDataPrototype(self, element: ET.Element, prototype: DataPrototype):
        self.writeIdentifiable(element, prototype)

    def setApplicationCompositeElementDataPrototype(self, element: ET.Element, prototype: ApplicationCompositeElementDataPrototype):
        self.setDataPrototype(element, prototype)
        self.setChildElementOptionalRefType(element, "TYPE-TREF", prototype.typeTRef)

    def setApplicationRecordElement(self, element: ET.Element, prototype: ApplicationRecordElement):
        self.setApplicationCompositeElementDataPrototype(element, prototype)

    def writeApplicationRecordElements(self, element: ET.Element, data_type: ApplicationRecordDataType):
        records = data_type.getApplicationRecordElements()
        if len(records) > 0:
            elements_tag = ET.SubElement(element, "ELEMENTS")
            for record in records:
                child_element = ET.SubElement(elements_tag, "APPLICATION-RECORD-ELEMENT")
                self.setApplicationRecordElement(child_element, record)

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

    def writeBaseTypeDirectDefinition(self, element: ET.Element, base_type_definition: BaseTypeDirectDefinition):
        self.setChildElementOptionalNumericalValue(element, "BASE-TYPE-SIZE", base_type_definition.baseTypeSize)
        self.writeChildElementOptionalLiteral(element, "BASE-TYPE-ENCODING", base_type_definition.baseTypeEncoding)
        self.setChildElementOptionalNumericalValue(element, "MEM-ALIGNMENT", base_type_definition.memAlignment)
        self.writeChildElementOptionalLiteral(element, "NATIVE-DECLARATION", base_type_definition.nativeDeclaration)

    def writeSwBaseType(self, element: ET.Element, base_type: SwBaseType):
        data_type_tag = ET.SubElement(element, "SW-BASE-TYPE")
        self.writeIdentifiable(data_type_tag, base_type)
        self.writeBaseTypeDirectDefinition(data_type_tag, base_type.baseTypeDefinition)

    def writeCompuScaleConstantContents(self, element: ET.Element, contents: CompuScaleConstantContents):
        compu_const_tag = ET.SubElement(element, "COMPU-CONST")
        if isinstance(contents.compu_const.compu_const_content_type, CompuConstTextContent):
            self.setChildElementOptionalValue(compu_const_tag, "VT", contents.compu_const.compu_const_content_type.vt)

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
        if isinstance(compu_scale.compuScaleContents, CompuScaleConstantContents):
            self.writeCompuScaleConstantContents(element, compu_scale.compuScaleContents)
        elif isinstance(compu_scale.compuScaleContents, CompuScaleRationalFormula):
            self.writeCompuScaleRationalFormula(element, compu_scale.compuScaleContents)
        else:
            raise NotImplementedError("Unsupported CompuScaleContents %s" % type(compu_scale.compuScaleContents))

    def writeCompuScales(self, element: ET.Element, compu_scales: CompuScales):
        compu_scales_tag = ET.SubElement(element, "COMPU-SCALES")
        for compu_scale in compu_scales.getCompuScales():
            child_element = ET.SubElement(compu_scales_tag, "COMPU-SCALE")
            self.writeElementAttributes(child_element, compu_scale)
            self.setChildElementOptionalLiteral(child_element, "SYMBOL", compu_scale.symbol)
            self.writeChildLimitElement(child_element, "LOWER-LIMIT", compu_scale.lowerLimit)
            self.writeChildLimitElement(child_element, "UPPER-LIMIT", compu_scale.upperLimit)
            self.writeCompuScaleContents(child_element, compu_scale)

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
        self.setChildElementOptionalRefType(compu_method_tag, "UNIT-REF", compu_method.unit_ref)
        self.writeCompuInternalToPhys(compu_method_tag, compu_method)

    def setApplicationValueSpecification(self, element: ET.Element, spec: ApplicationValueSpecification):
        spec_tag = ET.SubElement(element, "APPLICATION-VALUE-SPECIFICATION")
        self.setChildElementOptionalValue(spec_tag, "SHORT-LABEL", spec.short_label)
        self.setChildElementOptionalValue(spec_tag, "CATEGORY", spec.category)
        self.writeSwValueCont(spec_tag, spec.sw_value_cont)

    def setRecordValueSpecification(self, element: ET.Element, spec: RecordValueSpecification):
        child_element = ET.SubElement(element, "RECORD-VALUE-SPECIFICATION")
        self.writeElementAttributes(child_element, spec)
        self.setChildElementOptionalValue(child_element, "SHORT-LABEL", spec.short_label)
        fields = spec.get_fields()
        if len(fields) > 0:
            fields_tag = ET.SubElement(child_element, "FIELDS")
            for field in fields:
                if isinstance(field, ApplicationValueSpecification):
                    self.setApplicationValueSpecification(fields_tag, field)
                elif isinstance(field, NumericalValueSpecification):
                    self.setNumericalValueSpecification(fields_tag, field)
                elif isinstance(field, TextValueSpecification):
                    self.setTextValueSpecification(fields_tag, field)
                elif isinstance(field, ArrayValueSpecification):
                    self.setArrayValueSpecification(fields_tag, field)
                else:
                    raise NotImplementedError("Unsupported Field <%s>" % type(field))

    def writeConstantSpecification(self, element: ET.Element, spec: ConstantSpecification):
        spec_tag = ET.SubElement(element, "CONSTANT-SPECIFICATION")
        self.writeIdentifiable(spec_tag, spec)

        if spec.value_spec is not None:
            value_spec_tag = ET.SubElement(spec_tag, "VALUE-SPEC")
            self.setValueSpecification(value_spec_tag, spec.value_spec)
                
    def setInternalConstrs(self, element: ET.Element, constrs: InternalConstrs):
        if constrs is not None:
            constrs_tag = ET.SubElement(element, "INTERNAL-CONSTRS")
            self.writeElementAttributes(constrs_tag, constrs)
            if constrs.lower_limit is not None:
                self.writeChildLimitElement(constrs_tag, "LOWER-LIMIT", constrs.lower_limit)
            if constrs.upper_limit is not None:
                self.writeChildLimitElement(constrs_tag, "UPPER-LIMIT", constrs.upper_limit)

    def setPhysConstrs(self, element: ET.Element, constrs: PhysConstrs):
        if constrs is not None:
            child_element = ET.SubElement(element, "PHYS-CONSTRS")
            self.writeElementAttributes(child_element, constrs)
            if constrs.lower_limit is not None:
                self.writeChildLimitElement(child_element, "LOWER-LIMIT", constrs.lower_limit)
            if constrs.upper_limit is not None:
                self.writeChildLimitElement(child_element, "UPPER-LIMIT", constrs.upper_limit)
            self.setChildElementOptionalRefType(child_element, "UNIT-REF", constrs.unit_ref)
                
    def writeDataConstrRules(self, element: ET.Element, parent: DataConstr):
        rules = parent.getDataConstrRules()
        if len(rules) > 0:
            rules_tag = ET.SubElement(element, "DATA-CONSTR-RULES")
            for rule in rules:
                child_element = ET.SubElement(rules_tag, "DATA-CONSTR-RULE")
                self.writeElementAttributes(child_element, rule)
                self.setChildElementOptionalNumericalValue(child_element, "CONSTR-LEVEL", rule.constrLevel)
                self.setPhysConstrs(child_element, rule.physConstrs)
                self.setInternalConstrs(child_element, rule.internalConstrs)

    def writeDataConstr(self, element: ET.Element, constr: DataConstr):
        child_element = ET.SubElement(element, "DATA-CONSTR")
        self.writeIdentifiable(child_element, constr)
        self.writeDataConstrRules(child_element, constr) 

    def writeUnit(self, element: ET.Element, unit: Unit):
        self.logger.debug("writeUnit %s" % unit.short_name)
        child_element = ET.SubElement(element, "UNIT")
        self.writeIdentifiable(child_element, unit)
        self.writeChildElementOptionalLiteral(child_element, "DISPLAY-NAME", unit.display_name)

    def setRModeInAtomicSwcInstanceRef(self, element: ET.Element, key: str, iref: RModeInAtomicSwcInstanceRef):
        child_element = ET.SubElement(element, key)
        self.setChildElementOptionalRefType(child_element, "BASE", iref.base_ref)
        self.setChildElementOptionalRefType(child_element, "CONTEXT-PORT-REF", iref.context_port_ref)
        self.setChildElementOptionalRefType(child_element, "CONTEXT-MODE-DECLARATION-GROUP-PROTOTYPE-REF", iref.context_mode_declaration_group_prototype_ref)
        self.setChildElementOptionalRefType(child_element, "TARGET-MODE-DECLARATION-REF", iref.target_mode_declaration_ref)

    def setPOperationInAtomicSwcInstanceRef(self, element: ET.Element, key: str, iref: POperationInAtomicSwcInstanceRef):
        child_element = ET.SubElement(element, key)
        self.setChildElementOptionalRefType(child_element, "CONTEXT-P-PORT-REF", iref.context_p_port_ref)
        self.setChildElementOptionalRefType(child_element, "TARGET-PROVIDED-OPERATION-REF", iref.target_provided_operation_ref)

    def setRTEEvent(self, element: ET.Element, event: RTEEvent):
        self.writeIdentifiable(element, event)
        irefs = event.getDisabledModeIRefs()
        if len(irefs) > 0:
            child_element = ET.SubElement(element, "DISABLED-MODE-IREFS")
            for iref in irefs:
                self.setRModeInAtomicSwcInstanceRef(child_element, "DISABLED-MODE-IREF", iref)
        self.setChildElementOptionalRefType(element, "START-ON-EVENT-REF", event.start_on_event_ref)

    def setTimingEvent(self, element: ET.Element, event: TimingEvent):
        if event is not None:
            child_element = ET.SubElement(element, "TIMING-EVENT")
            self.setRTEEvent(child_element, event)
            self.setChildElementOptionalNumberValue(child_element, "PERIOD", event.period)

    def setOperationInvokedEvent(self, element: ET.Element, event: OperationInvokedEvent):
        if event is not None:
            child_element = ET.SubElement(element, "OPERATION-INVOKED-EVENT")
            self.setRTEEvent(child_element, event)
            self.setPOperationInAtomicSwcInstanceRef(child_element, "OPERATION-IREF", event.operation_iref)

    def setSwcModeSwitchEvent(self, element: ET.Element, event: SwcModeSwitchEvent):
        if event is not None:
            child_element = ET.SubElement(element, "SWC-MODE-SWITCH-EVENT")
            self.setRTEEvent(child_element, event)
            self.setChildElementOptionalValue(child_element, "ACTIVATION", event.activation)
            irefs = event.getModeIRefs()
            if len(irefs) > 0:
                mode_irefs_tag = ET.SubElement(child_element, "MODE-IREFS")
                for iref in irefs:
                    self.setRModeInAtomicSwcInstanceRef(mode_irefs_tag, "MODE-IREF", iref)

    def setRVariableInAtomicSwcInstanceRef(self, element: ET.Element, iref: RVariableInAtomicSwcInstanceRef):
        if iref is not None:
            child_element = ET.SubElement(element, "DATA-IREF")
            self.setChildElementOptionalRefType(child_element, "CONTEXT-R-PORT-REF", iref.context_r_port_ref)
            self.setChildElementOptionalRefType(child_element, "TARGET-DATA-ELEMENT-REF", iref.target_data_element_ref)

    def setDataReceivedEvent(self, element: ET.Element, event: DataReceivedEvent):
        if event is not None:
            child_element = ET.SubElement(element, "DATA-RECEIVED-EVENT")
            self.setRTEEvent(child_element, event)
            self.setRVariableInAtomicSwcInstanceRef(child_element, event.data_iref)

    def setInternalTriggerOccurredEvent(self, element: ET.Element, event: DataReceivedEvent):
        pass

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
                elif isinstance(event, InternalTriggerOccurredEvent):
                    self.setInternalTriggerOccurredEvent(child_element, event)
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
                self.setChildElementOptionalRefType(refs_tag, "DATA-TYPE-MAPPING-REF", ref)
           
    def writeInternalBehavior(self, element: ET.Element, behavior: InternalBehavior):
        self.writeIdentifiable(element, behavior)
        self.writeExclusiveAreas(element, behavior)
        self.writeDataTypeMappingRefs(element, behavior)

    def writeExecutableEntity(self, element: ET.Element, entity: ExecutableEntity):
        if entity is not None:
            self.setChildElementOptionalFloatValue(element, "MINIMUM-START-INTERVAL", entity.minimumStartInterval)

    def setAutosarVariableRef(self, element: ET.Element, ref: AutosarVariableRef):
        if ref is not None:
            child_element = ET.SubElement(element, "ACCESSED-VARIABLE")
            if ref.autosar_variable_iref is not None:
                child_element = ET.SubElement(child_element, "AUTOSAR-VARIABLE-IREF")
                self.setChildElementOptionalRefType(child_element, "PORT-PROTOTYPE-REF", ref.autosar_variable_iref.port_prototype_ref)
                self.setChildElementOptionalRefType(child_element, "TARGET-DATA-PROTOTYPE-REF", ref.autosar_variable_iref.target_data_prototype_ref)
            if ref.local_variable_ref is not None:
                self.setChildElementOptionalRefType(child_element, "LOCAL-VARIABLE-REF", ref.local_variable_ref)

    def setVariableAccess(self, element: ET.Element, access: VariableAccess):
        child_element = ET.SubElement(element, "VARIABLE-ACCESS")
        self.writeIdentifiable(child_element, access)
        self.setAutosarVariableRef(child_element, access.accessed_variable_ref)

    def writeDataReadAccesses(self, element: ET.Element, entity: RunnableEntity):
        #accesses = entity.getDataReadAccesses():
        pass

    def setAutosarParameterRef(self, element: ET.Element, key: str, parameter_ref: AutosarParameterRef):
        if parameter_ref is not None:
            child_element = ET.SubElement(element, key)
            self.setChildElementOptionalRefType(child_element, "LOCAL-PARAMETER-REF", parameter_ref.local_parameter_ref)

    def writeParameterAccess(self, element: ET.Element, parameter_access: ParameterAccess):
        child_element = ET.SubElement(element, "PARAMETER-ACCESS")
        self.writeIdentifiable(child_element, parameter_access)
        self.setAutosarParameterRef(child_element, "ACCESSED-PARAMETER", parameter_access.accessed_parameter)

    def writeParameterAccesses(self, element: ET.Element, entity: RunnableEntity):
        parameter_accesses = entity.getParameterAccesses()
        if len(parameter_accesses) > 0:
            child_element = ET.SubElement(element, "PARAMETER-ACCESSS")
            for parameter_access in parameter_accesses:
                self.writeParameterAccess(child_element, parameter_access)
        
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

    def writeDataWriteAccesses(self, element: ET.Element, entity: RunnableEntity):
        points = entity.getDataWriteAccesses()
        if len(points) > 0:
            child_element = ET.SubElement(element, "DATA-WRITE-ACCESSS")
            for point in points:
                self.setVariableAccess(child_element, point)

    def writeReadLocalVariables(self, element: ET.Element, entity: RunnableEntity):
        variables = entity.getReadLocalVariables()
        if len(variables) > 0:
            child_element = ET.SubElement(element, "READ-LOCAL-VARIABLES")
            for access in variables:
                self.setVariableAccess(child_element, access)

    def writeROperationInAtomicSwcInstanceRef(self, element: ET.Element, key: str, iref: ROperationInAtomicSwcInstanceRef):
        if iref is not None:
            child_element = ET.SubElement(element, key)
            self.setChildElementOptionalRefType(child_element, "CONTEXT-R-PORT-REF", iref.context_r_port_ref)
            self.setChildElementOptionalRefType(child_element, "TARGET-REQUIRED-OPERATION-REF", iref.target_required_operation_ref)
        
    def writeServerCallPoint(self, element: ET.Element, call_point: ServerCallPoint):
        self.writeROperationInAtomicSwcInstanceRef(element, "OPERATION-IREF", call_point.operation_iref)
        self.setChildElementOptionalFloatValue(element, "TIMEOUT", call_point.timeout)

    def writeSynchronousServerCallPoint(self, element: ET.Element, call_point: SynchronousServerCallPoint):
        child_element = ET.SubElement(element, "SYNCHRONOUS-SERVER-CALL-POINT")
        self.writeIdentifiable(child_element, call_point)
        self.writeServerCallPoint(child_element, call_point)

    def writeServerCallPoints(self, element: ET.Element, entity: RunnableEntity):
        call_points = entity.getServerCallPoints()
        if len(call_points) > 0:
            child_element = ET.SubElement(element, "SERVER-CALL-POINTS")
            for call_point in call_points:
                if isinstance(call_point, SynchronousServerCallPoint):
                    self.writeSynchronousServerCallPoint(child_element, call_point)
                else:
                    self._raiseError("Unsupported ServerCallPoint type <%s>" % type(call_point))

    def writeWrittenLocalVariable(self, element: ET.Element, entity: RunnableEntity):
        variables = entity.getWrittenLocalVariables()
        if len(variables) > 0:
            child_element = ET.SubElement(element, "WRITTEN-LOCAL-VARIABLES")
            for access in variables:
                self.setVariableAccess(child_element, access)

    def writeRunnableEntity(self, element: ET.Element, entity: RunnableEntity):
        if entity is not None:
            child_element = ET.SubElement(element, "RUNNABLE-ENTITY")
            self.writeIdentifiable(child_element, entity)
            self.writeExecutableEntity(child_element, entity)
            self.setChildElementOptionalBooleanValue(child_element, "CAN-BE-INVOKED-CONCURRENTLY", entity.can_be_invoked_concurrently)
            self.writeParameterAccesses(child_element, entity)
            self.writeDataReceivePointByArguments(child_element, entity)
            self.writeDataSendPoints(child_element, entity)
            self.writeDataWriteAccesses(child_element, entity)
            self.writeReadLocalVariables(child_element, entity)
            self.writeServerCallPoints(child_element, entity)
            self.setChildElementOptionalValue(child_element, "SYMBOL", entity.symbol)
            self.writeWrittenLocalVariable(child_element, entity)

    def writeSwcInternalBehaviorRunnableEntities(self, element: ET.Element, behavior: SwcInternalBehavior):
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
                self.setChildElementOptionalValue(child_element, "INIT-VALUE", memory.init_value)
                self.setSwDataDefProps(child_element, "SW-DATA-DEF-PROPS", memory.sw_data_def_props)
                self.setChildElementOptionalValue(child_element, "TYPE", memory.type)
                self.setChildElementOptionalValue(child_element, "TYPE-DEFINITION", memory.type_definition)

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

    def writePortDefinedArgumentValues(self, element: ET.Element, option: PortAPIOption) :
        argument_values = option.getPortArgValues()
        if len(argument_values) > 0:
            child_element = ET.SubElement(element, "PORT-ARG-VALUES")
            for argument_value in argument_values:
                child_element = ET.SubElement(child_element, "PORT-DEFINED-ARGUMENT-VALUE")
                if argument_value.value is not None:
                    value_tag = ET.SubElement(child_element, "VALUE")
                    self.setValueSpecification(value_tag, argument_value.value)
                self.setChildElementOptionalRefType(child_element, "VALUE-TYPE-TREF", argument_value.value_type)

    def writePortAPIOptions(self, element: ET.Element, behavior: SwcInternalBehavior):
        options = behavior.getPortAPIOptions()
        if len(options) > 0:
            port_api_options_tag = ET.SubElement(element, "PORT-API-OPTIONS")
            for option in options:
                child_element = ET.SubElement(port_api_options_tag, "PORT-API-OPTION")
                self.setChildElementOptionalBooleanValue(child_element, "ENABLE-TAKE-ADDRESS", option.enable_take_address)
                self.setChildElementOptionalBooleanValue(child_element, "INDIRECT-API", option.indirect_API)
                self.writePortDefinedArgumentValues(child_element, option)
                self.setChildElementOptionalRefType(child_element, "PORT-REF", option.port_ref)

    def writeServiceDependency(self, element: ET.Element, dependency: ServiceDependency):
        self.writeIdentifiable(element, dependency)

    def writeRoleBasedDataAssignment(self, element: ET.Element, assignment: RoleBasedDataAssignment):
        child_element = ET.SubElement(element, "ROLE-BASED-DATA-ASSIGNMENT")
        self.setChildElementOptionalValue(child_element, "ROLE", assignment.role)
        self.setAutosarParameterRef(child_element, "USED-PARAMETER-ELEMENT", assignment.used_parameter_element)
        self.setChildElementOptionalRefType(child_element, "USED-PIM-REF", assignment.used_pim_ref)

    def writeRoleBasedPortAssignment(self, element: ET.Element, assignment: RoleBasedPortAssignment):
        child_element = ET.SubElement(element, "ROLE-BASED-PORT-ASSIGNMENT")
        self.setChildElementOptionalRefType(child_element, "PORT-PROTOTYPE-REF", assignment.port_prototype_ref)
        self.setChildElementOptionalValue(child_element, "ROLE", assignment.role)

    def writeSwcServiceDependencyAssignedData(self, element: ET.Element, dependency: SwcServiceDependency):
        assigned_data = dependency.getAssignedData()
        if len(assigned_data) > 0:
            child_element = ET.SubElement(element, "ASSIGNED-DATAS")
            for data in assigned_data:
                if isinstance(data, RoleBasedDataAssignment):
                    self.writeRoleBasedDataAssignment(child_element, data)
                else:
                    self._raiseError("Unsupported Assigned Data <%s>" % type(data))

    def writeSwcServiceDependencyAssignedPorts(self, element: ET.Element, dependency: SwcServiceDependency):
        assigned_data = dependency.getAssignedPorts()
        if len(assigned_data) > 0:
            child_element = ET.SubElement(element, "ASSIGNED-PORTS")
            for data in assigned_data:
                if isinstance(data, RoleBasedPortAssignment):
                    self.writeRoleBasedPortAssignment(child_element, data)
                else:
                    self._raiseError("Unsupported Assigned Data <%s>" % type(data)) 

    def writeNvBlockNeeds(self, element: ET.Element, needs: NvBlockNeeds):
        child_element = ET.SubElement(element, "NV-BLOCK-NEEDS")
        self.logger.debug("writeNvBlockNeeds %s" % needs.short_name)
        self.writeIdentifiable(child_element, needs)
        self.setChildElementOptionalBooleanValue(child_element, "CALC-RAM-BLOCK-CRC", needs.calc_ram_block_crc)
        self.setChildElementOptionalBooleanValue(child_element, "CHECK-STATIC-BLOCK-ID", needs.check_static_block_id)
        self.setChildElementOptionalNumberValue(child_element, "N-DATA-SETS", needs.n_data_sets)
        self.setChildElementOptionalNumberValue(child_element, "N-ROM-BLOCKS", needs.n_rom_blocks)
        self.setChildElementOptionalBooleanValue(child_element, "READONLY", needs.readonly)
        self.setChildElementOptionalValue(child_element, "RELIABILITY", needs.reliability)
        self.setChildElementOptionalBooleanValue(child_element, "RESISTANT-TO-CHANGED-SW", needs.resistant_to_changed_sw)
        self.setChildElementOptionalBooleanValue(child_element, "RESTORE-AT-START", needs.restore_at_start)
        self.setChildElementOptionalBooleanValue(child_element, "STORE-AT-SHUTDOWN", needs.store_at_shutdown)
        self.setChildElementOptionalBooleanValue(child_element, "WRITE-ONLY-ONCE", needs.write_only_once)
        self.setChildElementOptionalBooleanValue(child_element, "WRITE-VERIFICATION", needs.write_verification)
        self.setChildElementOptionalValue(child_element, "WRITING-PRIORITY", needs.writing_priority)      

    def writeSwcServiceDependencyServiceNeeds(self, element: ET.Element, parent: SwcServiceDependency):
        needs = parent.getServiceNeeds()
        if len(needs) > 0:
            child_element = ET.SubElement(element, "SERVICE-NEEDS")
            for need in needs:
                if isinstance(need, NvBlockNeeds):
                    self.writeNvBlockNeeds(child_element, need)    
                else:
                    self._raiseError("Unsupported service needs <%s>" % type(need))                  

    def writeSwcServiceDependency(self, element: ET.Element, dependency: SwcServiceDependency):
        child_element = ET.SubElement(element, "SWC-SERVICE-DEPENDENCY")
        self.writeServiceDependency(child_element, dependency)
        self.writeSwcServiceDependencyAssignedData(child_element, dependency)
        self.writeSwcServiceDependencyAssignedPorts(child_element, dependency)
        self.writeSwcServiceDependencyServiceNeeds(child_element, dependency)

    def writeSwcInternalBehaviorServiceDependencies(self, element: ET.Element, behavior: SwcInternalBehavior):
        dependencies = behavior.getSwcServiceDependencies()
        if len(dependencies) > 0:
            child_element = ET.SubElement(element, "SERVICE-DEPENDENCYS")
            for dependency in dependencies:
                if isinstance(dependency, SwcServiceDependency):
                    self.writeSwcServiceDependency(child_element, dependency)
                else:
                    self._raiseError("Unsupported ServiceDependency <%s>" % type(dependency))

    def writeSwcInternalBehavior(self, element: ET.Element, behavior: SwcInternalBehavior):
        self.logger.debug("writeSwInternalBehavior %s" % behavior.short_name)

        child_element = ET.SubElement(element, "SWC-INTERNAL-BEHAVIOR")
        self.writeInternalBehavior(child_element, behavior)
        self.writeRTEEvents(child_element, behavior)
        self.writeExplicitInterRunnableVariables(child_element, behavior)
        self.setChildElementOptionalValue(child_element, "HANDLE-TERMINATION-AND-RESTART", behavior.handle_termination_and_restart)
        self.writePerInstanceMemories(child_element, behavior)
        self.writeParameterDataPrototypes(child_element, behavior)
        self.writePortAPIOptions(child_element, behavior)
        self.writeSwcInternalBehaviorRunnableEntities(child_element, behavior)
        self.writeSwcInternalBehaviorServiceDependencies(child_element, behavior)
        self.setChildElementOptionalBooleanValue(child_element, "SUPPORTS-MULTIPLE-INSTANTIATION", behavior.supports_multiple_instantiation)

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
                self.setChildElementOptionalValue(artifact_desc_tag, "SHORT-LABEL", artifact_desc.short_label)
                self.setChildElementOptionalValue(artifact_desc_tag, "CATEGORY", artifact_desc.category)
            
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
                self.setChildElementOptionalValue(child_element, "ALIGNMENT", memory_section.alignment)
                self.setChildElementOptionalNumberValue(child_element, "SIZE", memory_section.size)
                self.setChildElementOptionalRefType(child_element, "SW-ADDRMETHOD-REF", memory_section.sw_addr_method_ref)
                self.logger.debug("writeMemorySections %s" % memory_section.short_name)

    def writeResourceConsumption(self, element: ET.Element, consumption: ResourceConsumption):
        if consumption is not None:
            child_element = ET.SubElement(element, "RESOURCE-CONSUMPTION")
            self.writeIdentifiable(child_element, consumption)
            self.writeMemorySections(child_element, consumption)

    def writeImplementation(self, element: ET.Element, impl: Implementation):
        self.writeIdentifiable(element, impl)
        self.writeCodeDescriptors(element, impl)
        self.setChildElementOptionalValue(element, "PROGRAMMING-LANGUAGE", impl.programming_language)
        self.writeResourceConsumption(element, impl.resource_consumption)
        self.setChildElementOptionalValue(element, "SW-VERSION", impl.sw_version)
        self.setChildElementOptionalRefType(element, "SWC-BSW-MAPPING-REF", impl.swc_bsw_mapping_ref)
        self.setChildElementOptionalValue(element, "USED-CODE-GENERATOR", impl.used_code_generator)
        self.setChildElementOptionalNumberValue(element, "VENDOR-ID", impl.vendor_id)

    def writeSwcImplementation(self, element: ET.Element, impl: SwcImplementation):
        self.logger.debug("writeSwcImplementation %s" % impl.short_name)
        child_element = ET.SubElement(element, "SWC-IMPLEMENTATION")
        self.writeImplementation(child_element, impl)
        self.setChildElementOptionalRefType(child_element, "BEHAVIOR-REF", impl.behavior_ref)

    def writeEndToEndDescriptionDataId(self, element: ET.Element, parent: EndToEndDescription):
        data_ids = parent.getDataIds()
        if len(data_ids) > 0:
            child_element = ET.SubElement(element, "DATA-IDS")
            for data_id in data_ids:
                self.setChildElementOptionalNumberValue(child_element, "DATA-ID", data_id)
    
    def setEndToEndDescription(self, element: ET.Element, key: str, desc: EndToEndDescription):
        if desc is not None:
            child_element = ET.SubElement(element, key)
            self.setChildElementOptionalValue(child_element, "CATEGORY", desc.category)
            self.writeEndToEndDescriptionDataId(child_element, desc)
            self.setChildElementOptionalNumberValue(child_element, "DATA-ID-MODE", desc.dataIdMode)
            self.setChildElementOptionalNumberValue(child_element, "MAX-DELTA-COUNTER-INIT", desc.maxDeltaCounterInit)
            self.setChildElementOptionalNumberValue(child_element, "CRC-OFFSET", desc.crcOffset)
            self.setChildElementOptionalNumberValue(child_element, "COUNTER-OFFSET", desc.counterOffset)

    def setVariableDataPrototypeInSystemInstanceRef(self, element: ET.Element, key: str, iref: VariableDataPrototypeInSystemInstanceRef):
        if iref is not None:
            child_element = ET.SubElement(element, key)
            self.setChildElementOptionalRefType(child_element, "CONTEXT-COMPONENT-REF", iref.contextComponentRef)
            self.setChildElementOptionalRefType(child_element, "CONTEXT-COMPOSITION-REF", iref.contextCompositionRef)
            self.setChildElementOptionalRefType(child_element, "CONTEXT-PORT-REF", iref.contextPortRef)
            self.setChildElementOptionalRefType(child_element, "TARGET-DATA-PROTOTYPE-REF", iref.targetDataPrototypeRef)

    def setEndToEndProtectionVariablePrototype(self, element: ET.Element, key: str, prototype: EndToEndProtectionVariablePrototype):
        if prototype is not None:
            child_element = ET.SubElement(element, key)
            irefs = prototype.getReceiverIrefs()
            if len(irefs) > 0:
                child_element = ET.SubElement(child_element, "RECEIVER-IREFS")
                for iref in irefs:
                    self.setVariableDataPrototypeInSystemInstanceRef(child_element, "RECEIVER-IREF", iref)
            self.setVariableDataPrototypeInSystemInstanceRef(child_element, "SENDER-IREF", prototype.senderIRef)

    def writeEndToEndProtectionVariablePrototypes(self, element: ET.Element, parent: EndToEndProtection):
        prototypes = parent.getEndToEndProtectionVariablePrototypes()
        if len(prototypes) > 0:
            child_element = ET.SubElement(element, "END-TO-END-PROTECTION-VARIABLE-PROTOTYPES")
            for prototype in prototypes:
                if isinstance(prototype, EndToEndProtectionVariablePrototype):
                    self.setEndToEndProtectionVariablePrototype(child_element, "END-TO-END-PROTECTION-VARIABLE-PROTOTYPE", prototype)
                else:
                    self._raiseError("Unsupported End To End Protection Variable Prototype <%s>" % type(prototype))
            

    def setEndToEndProtection(self, element: ET.Element, protection: EndToEndProtection):
        if protection is not None:
            child_element = ET.SubElement(element, "END-TO-END-PROTECTION")
            self.writeIdentifiable(child_element, protection)
            self.setEndToEndDescription(child_element, "END-TO-END-PROFILE", protection.endToEndProfile)
            self.writeEndToEndProtectionVariablePrototypes(child_element, protection)

    def writeEndToEndProtections(self, element: ET.Element, protection_set: EndToEndProtectionSet):
        protections = protection_set.getEndToEndProtections()
        if len(protections) > 0:
            child_element = ET.SubElement(element, "END-TO-END-PROTECTIONS")
            for protection in protections:
                if isinstance(protection, EndToEndProtection):
                    self.setEndToEndProtection(child_element, protection)

    def writeEndToEndProtectionSet(self, element: ET.Element, protection_set: EndToEndProtectionSet):
        self.logger.debug("writeEndToEndProtectionSet %s" % protection_set.short_name)
        child_element = ET.SubElement(element, "END-TO-END-PROTECTION-SET")
        self.writeIdentifiable(child_element, protection_set)
        self.writeEndToEndProtections(child_element, protection_set)

    def writeAutosarDataPrototype(self, element: ET.Element, prototype: AutosarDataPrototype):
        self.setChildElementOptionalRefType(element, "TYPE-TREF", prototype.type_tref)

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
        self.setChildElementOptionalBooleanValue(child_element, "IS-SERVICE", sr_interface.is_service)
        self.writeDataElements(child_element, sr_interface)

    def writerBswModuleDescriptionImplementedEntry(self, element: ET.Element, desc: BswModuleDescription):
        entries = desc.getImplementedEntries()
        if len(entries) > 0:
            entries_tag = ET.SubElement(element, "PROVIDED-ENTRYS")
            for entry in entries:
                entry_tag = ET.SubElement(entries_tag, "BSW-MODULE-ENTRY-REF-CONDITIONAL")
                self.setChildElementOptionalRefType(entry_tag, "BSW-MODULE-ENTRY-REF", entry)

    def setModeDeclarationGroupPrototype(self, element: ET.Element, prototype: ModeDeclarationGroupPrototype):
        self.writeIdentifiable(element, property)
        self.setChildElementOptionalRefType(element, "TYPE-TREF", prototype.type_tref)

    def writeProvidedModeGroup(self, element: ET.Element, parent: BswModuleDescription):
        mode_groups = parent.getProvidedModeGroups()
        if len(mode_groups) > 0:
            mode_groups_tag = ET.SubElement(element, "PROVIDED-MODE-GROUPS")
            for mode_group in mode_group:
                child_element = ET.SubElement(mode_groups_tag, "MODE-DECLARATION-GROUP-PROTOTYPE") 
                self.setModeDeclarationGroupPrototype(child_element, mode_group)

    def writeBswModuleEntity(self, element, entity: BswModuleEntity):
        self.setExecutableEntity(element, entity)
        self.setChildElementOptionalRefType(element, "IMPLEMENTED-ENTRY-REF", entity.implementedEntryRef)

    def writeBswInternalBehaviorBswModuleEntities(self, element: ET.Element, parent: BswInternalBehavior):
        if parent.getTotalBswModuleEntities() > 0:
            entities_tag = ET.SubElement(element, "ENTITYS")
            for entity in parent.getBswCalledEntities():
                if isinstance(entity, BswModuleEntity):
                    child_element = ET.SubElement(entities_tag, "BSW-CALLED-ENTITY")
                    self.writeIdentifiable(child_element, entity)
                    self.logger.debug("writeBswCalledEntity %s" % entity.short_name)

            self.readBswModuleEntity(child_element, entity)

    def setBswInternalBehavior(self, element: ET.Element, behavior: BswInternalBehavior):
        child_element = ET.SubElement(element, "BSW-INTERNAL-BEHAVIOR")
        self.writeInternalBehavior(child_element, behavior)
        self.writeBswInternalBehaviorBswModuleEntities(child_element, behavior)
        #self.readBswSchedulableEntity(child_element, behavior)
        #self.readBswModeSwitchEvent(child_element, behavior)
        #self.readBswTimingEvent(element, behavior)
        #self.readBswDataReceivedEvent(element, behavior)
        #self.readBswInternalTriggerOccurredEvent(element, behavior)

    def writeBswModuleDescriptionInternalBehaviors(self, element: ET.Element, behaviors: List[InternalBehavior]):
        if len(behaviors) > 0:
            child_element = ET.SubElement(element, "INTERNAL-BEHAVIORS")
            for behavior in behaviors:
                if isinstance(behavior, BswInternalBehavior):
                    self.setBswInternalBehavior(child_element, behavior)
                else:
                    self._raiseError("Unsupport BswInternalBehavior <%s>" % type(behavior))

    def writeBswModuleDescription(self, element: ET.Element, desc: BswModuleDescription):
        self.logger.debug("writeBswModuleDescription %s" % desc.short_name)
        child_element = ET.SubElement(element, "BSW-MODULE-DESCRIPTION")
        self.writeIdentifiable(child_element, desc)
        self.setChildElementOptionalNumericalValue(child_element, "MODULE-ID", desc.moduleId)
        self.writerBswModuleDescriptionImplementedEntry(child_element, desc)
        self.writeProvidedModeGroup(child_element, desc)
        #self.readRequiredModeGroup(element, bsw_module_description)
        self.writeBswModuleDescriptionInternalBehaviors(child_element, desc.getBswInternalBehaviors())

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

    def writeImplementationDataTypeElements(self, element: ET.Element, parent: ImplementationDataType):
        sub_elements = parent.getImplementationDataTypeElements()
        if len(sub_elements) > 0:
            sub_elements_tag = ET.SubElement(element, "SUB-ELEMENTS")
            for type_element in sub_elements:
                child_element = ET.SubElement(sub_elements_tag, "IMPLEMENTATION-DATA-TYPE-ELEMENT")
                self.writeIdentifiable(child_element, type_element)
                self.setSwDataDefProps(child_element, "SW-DATA-DEF-PROPS", type_element.swDataDefProps)

    def writeImplementationDataType(self, element: ET.Element, data_type: ImplementationDataType):
        self.logger.debug("writeImplementationDataType %s" % data_type.short_name)
        child_element = ET.SubElement(element, "IMPLEMENTATION-DATA-TYPE")
        self.writeAutosarDataType(child_element, data_type)
        #self.setSwDataDefProps(child_element, "SW-DATA-DEF-PROPS", data_type.sw_data_def_props)
        self.writeImplementationDataTypeElements(child_element, data_type)

    def writeArgumentDataPrototypes(self, element: ET.Element, parent: ClientServerOperation):
        arguments = parent.getArgumentDataPrototypes()
        if len(arguments) > 0:
            arguments_tag = ET.SubElement(element, "ARGUMENTS")
            for prototype in arguments:
                child_element = ET.SubElement(arguments_tag, "ARGUMENT-DATA-PROTOTYPE")
                self.writeIdentifiable(child_element, prototype)
                self.setChildElementOptionalRefType(child_element, "TYPE-TREF", prototype.type_tref)
                self.setChildElementOptionalValue(child_element, "DIRECTION", prototype.direction)

    def writePossibleErrorRefs(self, element: ET.Element, parent: ClientServerOperation):
        error_refs = parent.getPossbileErrorRefs()
        if len(error_refs) > 0:
            error_refs_tag = ET.SubElement(element, "POSSIBLE-ERROR-REFS")
            for error_ref in error_refs:
                self.setChildElementOptionalRefType(error_refs_tag, "POSSIBLE-ERROR-REF", error_ref)

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
        self.setChildElementOptionalNumberValue(child_element, "ERROR-CODE", error.error_code)

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
        self.setChildElementOptionalBooleanValue(child_element, "IS-SERVICE", cs_interface.is_service)
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

    def setApplicationArrayElement(self, element: ET.Element, prototype: ApplicationArrayElement):
        if prototype is not None:
            child_element = ET.SubElement(element, "ELEMENT")
            self.setApplicationCompositeElementDataPrototype(child_element, prototype)
            self.setChildElementOptionalLiteral(child_element, "ARRAY-SIZE-SEMANTICS", prototype.arraySizeSemantics)
            self.setChildElementOptionalNumericalValue(child_element, "MAX-NUMBER-OF-ELEMENTS", prototype.maxNumberOfElements)

    def writeApplicationArrayDataType(self, element: ET.Element, data_type: ApplicationArrayDataType):
        self.logger.debug("writeApplicationArrayDataType %s" % data_type.short_name)
        child_element = ET.SubElement(element, "APPLICATION-ARRAY-DATA-TYPE")
        self.writeApplicationCompositeDataType(child_element, data_type)
        self.setApplicationArrayElement(child_element, data_type.element)

    def setSwRecordLayoutV(self, element: ET.Element, key: str, layout_v: SwRecordLayoutV):
        if layout_v is not None:
            child_element = ET.SubElement(element, key)
            self.setChildElementOptionalLiteral(child_element, "SHORT-LABEL", layout_v.shortLabel)
            self.setChildElementOptionalRefType(child_element, "BASE-TYPE-REF", layout_v.baseTypeRef)
            self.setChildElementOptionalNumericalValue(child_element, "SW-RECORD-LAYOUT-V-AXIS", layout_v.swRecordLayoutVAxis)
            self.setChildElementOptionalLiteral(child_element, "SW-RECORD-LAYOUT-V-PROP", layout_v.swRecordLayoutVProp)
            self.setChildElementOptionalLiteral(child_element, "SW-RECORD-LAYOUT-V-INDEX", layout_v.swRecordLayoutVIndex)

    def setSwRecordLayoutGroup(self, element: ET.Element, key: str, group: SwRecordLayoutGroup):
        if group is not None:
            child_element = ET.SubElement(element, key)
            self.setChildElementOptionalLiteral(child_element, "SHORT-LABEL", group.shortLabel)
            self.setChildElementOptionalLiteral(child_element, "CATEGORY", group.category)
            self.setChildElementOptionalNumericalValue(child_element, "SW-RECORD-LAYOUT-GROUP-AXIS", group.swRecordLayoutGroupAxis)
            self.setChildElementOptionalLiteral(child_element, "SW-RECORD-LAYOUT-GROUP-INDEX", group.swRecordLayoutGroupIndex)
            self.setChildElementOptionalLiteral(child_element, "SW-RECORD-LAYOUT-GROUP-FROM", group.swRecordLayoutGroupFrom)
            self.setChildElementOptionalLiteral(child_element, "SW-RECORD-LAYOUT-GROUP-TO", group.swRecordLayoutGroupTo)
            self.setSwRecordLayoutV(child_element, "SW-RECORD-LAYOUT-V", group.swRecordLayoutGroupContentType.swRecordLayoutV)
            self.setSwRecordLayoutGroup(child_element, "SW-RECORD-LAYOUT-GROUP", group.swRecordLayoutGroupContentType.swRecordLayoutGroup)
        return group

    def writeSwRecordLayout(self, element: ET.Element, layout: SwRecordLayout):
        self.logger.debug("writeSwRecordLayout %s" % layout.short_name)
        child_element = ET.SubElement(element, "SW-RECORD-LAYOUT")
        self.writeIdentifiable(child_element, layout)
        self.setSwRecordLayoutGroup(child_element, "SW-RECORD-LAYOUT-GROUP", layout.swRecordLayoutGroup)

    def writeSwAddrMethod(self, element: ET.Element, method: SwAddrMethod):
        self.logger.debug("writeSwAddrMethod %s" % method.short_name)
        child_element = ET.SubElement(element, "SW-RECORD-LAYOUT")

    def writeTriggerInterface(self, element: ET.Element, trigger_if: TriggerInterface):
        self.logger.debug("writeTriggerInterface %s" % trigger_if.short_name)
        child_element = ET.SubElement(element, "SW-RECORD-LAYOUT")

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
        elif isinstance(ar_element, ApplicationArrayDataType):
            self.writeApplicationArrayDataType(element, ar_element)
        elif isinstance(ar_element, SwRecordLayout):
            self.writeSwRecordLayout(element, ar_element)
        elif isinstance(ar_element, SwAddrMethod):
            self.writeSwAddrMethod(element, ar_element)
        elif isinstance(ar_element, TriggerInterface):
            self.writeTriggerInterface(element, ar_element)
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
        #xml = xml.replace("<SW-DATA-DEF-PROPS-CONDITIONAL/>","<SW-DATA-DEF-PROPS-CONDITIONAL></SW-DATA-DEF-PROPS-CONDITIONAL>")
        xml = re.sub(r"\<([\w-]+)\/\>",r"<\1></\1>", xml)
        xml = re.sub(r"<((\w+)\s+\w+=\"\w+\")\/>", r"<\1></\2>", xml)
        xml = xml.replace("<USES-END-TO-END-PROTECTION>false</USES-END-TO-END-PROTECTION>", "<USES-END-TO-END-PROTECTION>0</USES-END-TO-END-PROTECTION>")
        return xml

    def saveToFile(self, filename, root: ET.Element):
        xml = ET.tostring(root, encoding = "UTF-8", xml_declaration = True, short_empty_elements = False)
        
        dom = minidom.parseString(xml.decode())
        xml = dom.toprettyxml(indent = "  ", encoding = "UTF-8")

        text = self.patch_xml(xml.decode())
    
        with open(filename, "w", encoding="utf-8") as f_out:
            #f_out.write(xml.decode())
            f_out.write(text)

    def save(self, filename, document: AUTOSAR):
        self.logger.info("Save %s ..." % filename)

        root = ET.Element("AUTOSAR", self.nsmap)
        root.attrib["xmlns:xsi"] = "http://www.w3.org/2001/XMLSchema-instance"
        root.attrib["xsi:schemaLocation"] = document.schema_location
        
        self.writeARPackages(root, document.getARPackages())

        self.saveToFile(filename, root)
        