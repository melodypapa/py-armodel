import logging
import xml.etree.cElementTree as ET

from xml.dom import minidom
from typing import List

from ..models.ar_object import ARLiteral
from ..models import AUTOSAR, ARPackage, ARObject, Identifiable, MultilanguageReferrable, Referrable, AdminData, Sdg, ARElement, SwDataDefProps, MultilanguageLongName
from ..models import CompositionSwComponentType, SwComponentType, SwComponentPrototype
from ..models import PortPrototype, PPortPrototype, RPortPrototype
from ..models import NonqueuedReceiverComSpec, NonqueuedSenderComSpec, ClientComSpec
from ..models import TRefType
from ..models import PPortComSpec, RPortComSpec, SenderComSpec, ReceiverComSpec
from ..models import TransmissionAcknowledgementRequest
from ..models import ValueSpecification, ApplicationValueSpecification, TextValueSpecification, NumericalValueSpecification, ArrayValueSpecification
from ..models import ConstantSpecification, RecordValueSpecification, ConstantReference
from ..models import SwValueCont, SwValues
from ..models import SwConnector, AssemblySwConnector, DelegationSwConnector, PPortInCompositionInstanceRef, RPortInCompositionInstanceRef
from ..models import ARBoolean
from ..models import ApplicationPrimitiveDataType, AutosarDataType, ApplicationDataType, ApplicationRecordDataType, BaseType
from ..models import CompuMethod, CompuScales, CompuScale, Limit, CompuScaleConstantContents, CompuConstTextContent, CompuScaleRationalFormula, CompuNominatorDenominator

from ..models.global_constraints import DataConstr, DataConstrRule, InternalConstrs, PhysConstrs

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

    def writeChildOptionalElement(self, element: ET.Element, key: str, value: str):
        if value is not None:
            child_element = ET.SubElement(element, key)
            child_element.text = value

    def writeChildOptionalRefElement(self, parent: ET.Element, child_tag_name: str, ref: TRefType):
        if ref is not None:
            child_tag = ET.SubElement(parent, child_tag_name)
            if ref.dest is not None:
                child_tag.attrib['DEST'] = ref.dest
            if ref.value is not None:
                child_tag.text = ref.value

    def writeChildOptionalElementFloatValue(self, element: ET.Element, key: str, value: float):
        if value is not None:
            child_element = ET.SubElement(element, key)
            literal = "%g" % value
            if literal == '0':
                literal = "0.0"
            child_element.text = literal

    def writeChildOptionalElementBooleanValue(self, element: ET.Element, key: str, value: ARBoolean) -> ET.Element:
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
        
    def writeShortName(self, parent: ET.Element, name: str) -> ET.Element:
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
        self.writeShortName(element, referrable.short_name)

    def writeMultiLongName(self, element: ET.Element, long_name: MultilanguageLongName):
        self.writeElementAttributes(element, long_name)
        for l4 in long_name.get_l4s():
            l4_tag = ET.SubElement(element, "L-4")
            self.writeElementAttributes(l4_tag, l4)
            if l4.l is not None:
                l4_tag.attrib['L'] = l4.l
            l4_tag.text = l4.value

    def writeMultilanguageReferrable(self, element: ET.Element, referrable: MultilanguageReferrable):
        self.writeReferable(element, referrable)
        if referrable.long_name is not None:
            long_name_tag = ET.SubElement(element, "LONG-NAME")
            self.writeMultiLongName(long_name_tag, referrable.long_name)

    def writeAdminData(self, element: ET.Element, admin_data: AdminData):
        element = ET.SubElement(element, "ADMIN-DATA")
        self.writeSdg(element, admin_data)

    def writeIdentifiable(self, element: ET.Element, identifiable: Identifiable):
        self.writeMultilanguageReferrable(element, identifiable)
        self.writeChildOptionalElement(element, "CATEGORY", identifiable.category)
        if identifiable.admin_data is not None:
            self.writeAdminData(element, identifiable.admin_data)

    def writeARElement(self, parent: ET.Element, ar_element: ARElement):
        self.writeIdentifiable(parent, ar_element)
    
    def writeTransmissionAcknowledgementRequest(self, element: ET.Element, acknowledge: TransmissionAcknowledgementRequest):
        if (acknowledge != None):
            child_element = ET.SubElement(element, "TRANSMISSION-ACKNOWLEDGE")
            self.writeElementAttributes(child_element, acknowledge)
            if acknowledge.timeout != None:
                self.writeChildOptionalElementFloatValue(child_element, "TIMEOUT", acknowledge.timeout)

    def writeSenderComSpec(self, com_spec_tag: ET.Element, com_spec: SenderComSpec):
        self.writeChildOptionalRefElement(com_spec_tag, "DATA-ELEMENT-REF", com_spec.data_element_ref)
        if com_spec.network_representation is not None:
            network_representation_tag = ET.SubElement(com_spec_tag, "NETWORK-REPRESENTATION")
            self.writeSwDataDefProps(network_representation_tag, com_spec.network_representation)
        self.writeChildOptionalElement(com_spec_tag, "HANDLE-OUT-OF-RANGE", com_spec.handle_out_of_range)
        self.writeTransmissionAcknowledgementRequest(com_spec_tag, com_spec.transmission_acknowledge)
        self.writeChildOptionalElementBooleanValue(com_spec_tag, "USES-END-TO-END-PROTECTION", com_spec.uses_end_to_end_protection)
    
    def writeNonqueuedSenderComSpec(self, com_specs_tag: ET.Element, com_spec: NonqueuedSenderComSpec):
        com_spec_tag = ET.SubElement(com_specs_tag, "NONQUEUED-SENDER-COM-SPEC")
        self.writeElementAttributes(com_spec_tag, com_spec)
        self.writeSenderComSpec(com_spec_tag, com_spec)

        if com_spec.init_value is not None:
            init_value_tag = ET.SubElement(com_spec_tag, "INIT-VALUE")
            if isinstance(com_spec.init_value, NumericalValueSpecification):
                self.writeNumberValueSpecification(init_value_tag, com_spec.init_value)
            elif isinstance(com_spec.init_value, ArrayValueSpecification):
                self.writeArrayValueSpecification(init_value_tag, com_spec.init_value)
            elif isinstance(com_spec.init_value, ConstantReference):
                self.writeConstantReference(init_value_tag, com_spec.init_value)
            else:
                raise NotImplementedError("Unsupported ValueSpecification %s" % type(com_spec.init_value))
    
    def writePPortComSpec(self, com_specs_tag: ET.Element, com_spec: PPortComSpec):
        if isinstance(com_spec, NonqueuedSenderComSpec):
            self.writeNonqueuedSenderComSpec(com_specs_tag, com_spec)
        else:
            raise NotImplementedError("Unsupported PPortComSpec")
        
    def writeReceiverComSpec(self, com_spec_tag: ET.Element, com_spec: ReceiverComSpec):
        self.writeChildOptionalRefElement(com_spec_tag, "DATA-ELEMENT-REF", com_spec.data_element_ref)
        self.writeChildOptionalElement(com_spec_tag, "HANDLE-OUT-OF-RANGE", com_spec.handle_out_of_range)
        self.writeChildOptionalElementBooleanValue(com_spec_tag, "USES-END-TO-END-PROTECTION", com_spec.uses_end_to_end_protection)

    def writeSwValues(self, element: ET.Element, values: SwValues):
        if values.v is not None:
            self.writeChildOptionalElement(element, "V", values.v)

    def writeSwValueCont(self, element: ET.Element, cont: SwValueCont):
        child_element = ET.SubElement(element, "SW-VALUE-CONT")
        self.writeChildOptionalRefElement(child_element, "UNIT-REF", cont.unit_ref)
        if cont.sw_values_phys is not None:
            sw_values_phys_tag = ET.SubElement(child_element, "SW-VALUES-PHYS")
            self.writeSwValues(sw_values_phys_tag, cont.sw_values_phys)

    def writeValueSpecification(self, element: ET.Element, value_spec: ValueSpecification):
        self.writeElementAttributes(element, value_spec)
        if value_spec.short_label is not None:
            self.writeChildOptionalElement(element, "SHORT-LABEL", value_spec.short_label)                                

    def writeApplicationValueSpecification(self, element: ET.Element, value_spec: ApplicationValueSpecification):
        value_spec_tag = ET.SubElement(element, "APPLICATION-VALUE-SPECIFICATION")
        self.writeValueSpecification(value_spec_tag, value_spec)
        self.writeChildOptionalElement(value_spec_tag, "CATEGORY", value_spec.category)
        self.writeSwValueCont(value_spec_tag, value_spec.sw_value_cont)

    def writeTextValueSpecification(self, element: ET.Element, value_spec: TextValueSpecification):
        value_spec_tag = ET.SubElement(element, "TEXT-VALUE-SPECIFICATION")
        self.writeValueSpecification(value_spec_tag, value_spec)
        self.writeChildOptionalElement(value_spec_tag, "VALUE", value_spec.value)

    def writeNumberValueSpecification(self, element: ET.Element, value_spec: NumericalValueSpecification):
        value_spec_tag = ET.SubElement(element, "NUMERICAL-VALUE-SPECIFICATION")
        self.writeValueSpecification(value_spec_tag, value_spec)
        self.writeChildOptionalElement(value_spec_tag, "VALUE", value_spec.value)

    def writeArrayValueSpecification(self, element: ET.Element, value_spec: ArrayValueSpecification):
        value_spec_tag = ET.SubElement(element, "ARRAY-VALUE-SPECIFICATION")
        self.writeValueSpecification(value_spec_tag, value_spec)
        sub_elements = value_spec.get_elements()
        if len(sub_elements) > 0:
            elements_tag = ET.SubElement(value_spec_tag, "ELEMENTS")
            for sub_element in sub_elements:
                if isinstance(sub_element, NumericalValueSpecification):
                    self.writeNumberValueSpecification(elements_tag, sub_element)
                else:
                    raise NotImplementedError("Unsupported element type of <%s> of ArrayValueSpecification" % type(sub_element))
                
    def writeConstantReference(self, element: ET.Element, value_spec: ConstantReference):
        value_spec_tag = ET.SubElement(element, "CONSTANT-REFERENCE")
        self.writeValueSpecification(value_spec_tag, value_spec)
        self.writeChildOptionalRefElement(value_spec_tag, "CONSTANT-REF", value_spec.constant_ref)

    def writeNonqueuedReceiverComSpec(self, com_specs_tag: ET.Element, com_spec: NonqueuedReceiverComSpec):
        com_spec_tag = ET.SubElement(com_specs_tag, "NONQUEUED-RECEIVER-COM-SPEC")
        self.writeElementAttributes(com_spec_tag, com_spec)
        self.writeReceiverComSpec(com_spec_tag, com_spec)
        self.writeChildOptionalElementFloatValue(com_spec_tag, "ALIVE-TIMEOUT", com_spec.alive_timeout)
        self.writeChildOptionalElementBooleanValue(com_spec_tag, "ENABLE-UPDATE", com_spec.enable_updated)
        self.writeChildOptionalElementBooleanValue(com_spec_tag, "HANDLE-NEVER-RECEIVED", com_spec.handle_never_received)
        self.writeChildOptionalElement(com_spec_tag, "HANDLE-TIMEOUT-TYPE", com_spec.handel_timeout_type)
        if com_spec.init_value is not None:
            init_value_tag = ET.SubElement(com_spec_tag, "INIT-VALUE")
            if isinstance(com_spec.init_value, ApplicationValueSpecification):
                self.writeApplicationValueSpecification(init_value_tag, com_spec.init_value)
            elif isinstance(com_spec.init_value, TextValueSpecification):
                self.writeTextValueSpecification(init_value_tag, com_spec.init_value)
            elif isinstance(com_spec.init_value, ConstantReference):
                self.writeConstantReference(init_value_tag, com_spec.init_value)
            else:
                raise NotImplementedError("Unsupported ValueSpecification %s" % type(com_spec.init_value))
    
    def writeClientComSpec(self, com_specs_tag: ET.Element, com_spec: ClientComSpec):
        self.logger.debug("writeClientComSpec")

        com_spec_tag = ET.SubElement(com_specs_tag, "CLIENT-COM-SPEC")
        self.writeElementAttributes(com_spec_tag, com_spec)
        self.writeChildOptionalRefElement(com_spec_tag, "OPERATION-REF", com_spec.operation_ref)
    
    def writeRPortComSpec(self, com_specs_tag: ET.Element, com_spec: RPortComSpec):
        if isinstance(com_spec, NonqueuedReceiverComSpec):
            self.writeNonqueuedReceiverComSpec(com_specs_tag, com_spec)
        elif isinstance(com_spec, ClientComSpec):
            self.writeClientComSpec(com_specs_tag, com_spec)
        else:
            raise ValueError("Unsupported RPortComSpec %s" % type(com_spec))
    
    def writePPortPrototype(self, ports_tag: ET.Element, prototype: PPortPrototype):
        prototype_tag = ET.SubElement(ports_tag, "P-PORT-PROTOTYPE")

        self.writeElementAttributes(prototype_tag, prototype)
        self.writeShortName(prototype_tag, prototype.short_name)

        self.logger.debug("writePPortPrototype %s" % prototype.short_name)

        com_specs = prototype.getProvidedComSpecs()
        if len(com_specs):
            com_specs_tag = ET.SubElement(prototype_tag, "PROVIDED-COM-SPECS")
            for com_spec in com_specs:
                self.writePPortComSpec(com_specs_tag, com_spec)

        self.writeChildOptionalRefElement(prototype_tag, "PROVIDED-INTERFACE-TREF", prototype.provided_interface_tref)

    def writeRPortPrototype(self, ports_tag: ET.Element, prototype: RPortPrototype):
        prototype_tag = ET.SubElement(ports_tag, "R-PORT-PROTOTYPE")
        
        self.writeElementAttributes(prototype_tag, prototype)
        self.writeShortName(prototype_tag, prototype.short_name)

        self.logger.debug("writeRPortPrototype %s" % prototype.short_name)
        
        com_specs = prototype.getRequiredComSpecs()
        if len(com_specs) > 0:
            com_specs_tag = ET.SubElement(prototype_tag, "REQUIRED-COM-SPECS")
            for com_spec in com_specs:
                self.writeRPortComSpec(com_specs_tag, com_spec)

        self.writeChildOptionalRefElement(prototype_tag, "REQUIRED-INTERFACE-TREF", prototype.required_interface_tref)
    
    def writePortPrototypes(self, ports_tag: ET.Element, port_prototypes: List[PortPrototype]):
        for port_prototype in port_prototypes:
            if isinstance(port_prototype, PPortPrototype):
                self.writePPortPrototype(ports_tag, port_prototype)
            elif isinstance(port_prototype, RPortPrototype):
                self.writeRPortPrototype(ports_tag, port_prototype)
            else:
                self._raiseError("Invalid PortPrototype")
    
    def writeSwComponentType(self, element: ET.Element, sw_component: SwComponentType):
        ports_tag = ET.SubElement(element, "PORTS")
        self.writePortPrototypes(ports_tag, sw_component.getPortPrototype())

    def writeSwComponentPrototype(self, element: ET.Element, prototype: SwComponentPrototype):
        prototype_tag = ET.SubElement(element, "SW-COMPONENT-PROTOTYPE")
        self.writeElementAttributes(prototype_tag, prototype)
        self.writeShortName(prototype_tag, prototype.short_name)
        self.writeChildOptionalRefElement(prototype_tag, "TYPE-TREF", prototype.type_tref)

    def writeSwComponentPrototypes(self, element: ET.Element, sw_component: CompositionSwComponentType):
        components_tag = ET.SubElement(element, "COMPONENTS")
        for prototype in sw_component.getSwComponentPrototypes():
            self.writeSwComponentPrototype(components_tag, prototype)

    def writeAssemblySwConnector(self, element: ET.Element, sw_connector: AssemblySwConnector):
        connector_tag = ET.SubElement(element, "ASSEMBLY-SW-CONNECTOR")
        self.writeElementAttributes(connector_tag, sw_connector)
        self.writeShortName(connector_tag, sw_connector.short_name)

        if sw_connector.provider_iref is not None:
            provider_iref_tag = ET.SubElement(connector_tag, "PROVIDER-IREF")
            self.writeElementAttributes(provider_iref_tag, sw_connector.provider_iref)
            self.writeChildOptionalRefElement(provider_iref_tag, "CONTEXT-COMPONENT-REF", sw_connector.provider_iref.context_component_ref)
            self.writeChildOptionalRefElement(provider_iref_tag, "TARGET-P-PORT-REF", sw_connector.provider_iref.target_p_port_ref)

        if sw_connector.requester_iref is not None:
            requester_iref_tag = ET.SubElement(connector_tag, "REQUESTER-IREF")
            self.writeElementAttributes(requester_iref_tag, sw_connector.requester_iref)
            self.writeChildOptionalRefElement(requester_iref_tag, "CONTEXT-COMPONENT-REF", sw_connector.requester_iref.context_component_ref)
            self.writeChildOptionalRefElement(requester_iref_tag, "TARGET-R-PORT-REF", sw_connector.requester_iref.target_r_port_ref)

    def writeDelegationSwConnector(self, element: ET.Element, sw_connector: DelegationSwConnector):
        connector_tag = ET.SubElement(element, "DELEGATION-SW-CONNECTOR")
        self.writeElementAttributes(connector_tag, sw_connector)
        self.writeShortName(connector_tag, sw_connector.short_name)

        if sw_connector.inner_port_iref is not None:
            inner_port_iref_tag = ET.SubElement(connector_tag, "INNER-PORT-IREF")
            if isinstance(sw_connector.inner_port_iref, PPortInCompositionInstanceRef):
                instance_ref_tag = ET.SubElement(inner_port_iref_tag, "P-PORT-IN-COMPOSITION-INSTANCE-REF")
                self.writeChildOptionalRefElement(instance_ref_tag, "CONTEXT-COMPONENT-REF", sw_connector.inner_port_iref.context_component_ref)
                self.writeChildOptionalRefElement(instance_ref_tag, "TARGET-P-PORT-REF", sw_connector.inner_port_iref.target_p_port_ref)
            elif isinstance(sw_connector.inner_port_iref, RPortInCompositionInstanceRef):
                instance_ref_tag = ET.SubElement(inner_port_iref_tag, "R-PORT-IN-COMPOSITION-INSTANCE-REF")
                self.writeChildOptionalRefElement(instance_ref_tag, "CONTEXT-COMPONENT-REF", sw_connector.inner_port_iref.context_component_ref)
                self.writeChildOptionalRefElement(instance_ref_tag, "TARGET-R-PORT-REF", sw_connector.inner_port_iref.target_r_port_ref)
            else:
                self._raiseError("Invalid inner port of DelegationSwConnector <%s>" % sw_connector.short_name)

        if sw_connector.outer_port_ref is not None:
            self.writeChildOptionalRefElement(connector_tag, "OUTER-PORT-REF", sw_connector.outer_port_ref)
            #self.writeChildOptionalRefElement(requester_iref_tag, "TARGET-R-PORT-REF", sw_connector.requester_iref.target_r_port_ref)
        
    def writeSwConnector(self, element: ET.Element, sw_connector: SwConnector):
        if isinstance(sw_connector, AssemblySwConnector):
            self.writeAssemblySwConnector(element, sw_connector)
        elif isinstance(sw_connector, DelegationSwConnector):
            self.writeDelegationSwConnector(element, sw_connector)
        else:
            raise NotImplementedError("Unsupported Sw Connector %s")

    def writeSwConnectors(self, element: ET.Element, sw_component: CompositionSwComponentType):
        connectors_tag = ET.SubElement(element, "CONNECTORS")
        for sw_connector in sw_component.getSwConnectors():
            self.writeSwConnector(connectors_tag, sw_connector)

    def writeDataTypeMappingSet(self, element: ET.Element, parent: CompositionSwComponentType):
        data_type_mappings = parent.getDataTypeMappings()
        if len(data_type_mappings) > 0:
            child_element = ET.SubElement(element, "DATA-TYPE-MAPPING-REFS")
            self.logger.debug("writeDataTypeMappingSet")
            for data_type_mapping in data_type_mappings:
                self.writeChildOptionalRefElement(child_element, "DATA-TYPE-MAPPING-REF", data_type_mapping)
    
    def writeCompositionSwComponentType(self, parent: ET.Element, sw_component: CompositionSwComponentType):
        child_element = ET.SubElement(parent, "COMPOSITION-SW-COMPONENT-TYPE")

        self.writeIdentifiable(child_element, sw_component)
        self.writeSwComponentType(child_element, sw_component)
        self.writeSwComponentPrototypes(child_element, sw_component)
        self.writeSwConnectors(child_element, sw_component)
        self.writeDataTypeMappingSet(child_element, sw_component)

    def writeCompositionSwComponentTypes(self, element: ET.Element, ar_package: ARPackage):
        for sw_component in ar_package.getCompositionSwComponentTypes():
            self.writeCompositionSwComponentType(element, sw_component)

    def writeSwDataDefProps(self, element: ET.Element, sw_data_def_props: SwDataDefProps):
        sw_data_def_props_tag = ET.SubElement(element, "SW-DATA-DEF-PROPS")
        sw_data_def_props_variants_tag = ET.SubElement(sw_data_def_props_tag, "SW-DATA-DEF-PROPS-VARIANTS")
        sw_data_def_props_conditional_tag = ET.SubElement(sw_data_def_props_variants_tag, "SW-DATA-DEF-PROPS-CONDITIONAL")
        if sw_data_def_props.sw_calibration_access is not None:
            self.writeChildOptionalElement(sw_data_def_props_conditional_tag, "SW-CALIBRATION-ACCESS", sw_data_def_props.sw_calibration_access)
        if sw_data_def_props.compu_method_ref is not None:
            self.writeChildOptionalRefElement(sw_data_def_props_conditional_tag, "COMPU-METHOD-REF", sw_data_def_props.compu_method_ref)
        if sw_data_def_props.data_constr_ref is not None:
            self.writeChildOptionalRefElement(sw_data_def_props_conditional_tag, "DATA-CONSTR-REF", sw_data_def_props.data_constr_ref)

    def writeAutosarDataType(self, parent: ET.Element, data_type: AutosarDataType):
        self.writeARElement(parent, data_type)
        if data_type.sw_data_def_props is not None:
            self.writeSwDataDefProps(parent, data_type.sw_data_def_props)

    def writeApplicationDataType(self, parent: ET.Element, data_type: ApplicationDataType):
        self.writeAutosarDataType(parent, data_type)

    def writeApplicationPrimitiveDataType(self, element: ET.Element, data_type: ApplicationPrimitiveDataType):
        data_type_tag = ET.SubElement(element, "APPLICATION-PRIMITIVE-DATA-TYPE")
        self.writeApplicationDataType(data_type_tag, data_type)

    def writeApplicationRecordElements(self, element: ET.Element, data_type: ApplicationRecordDataType):
        record_elements = data_type.getApplicationRecordElements()
        if len(record_elements) > 0:
            elements_tag = ET.SubElement(element, "ELEMENTS")
            for record_element in record_elements:
                record_element_tag = ET.SubElement(elements_tag, "APPLICATION-RECORD-ELEMENT")
                self.writeIdentifiable(record_element_tag, record_element)
                self.writeChildOptionalRefElement(record_element_tag, "TYPE-TREF", record_element.type_tref)

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
        self.writeChildOptionalElement(element, "BASE-TYPE-SIZE", str(base_type.base_type_definition.base_type_size))
        self.writeChildOptionalElementLiteral(element, "BASE-TYPE-ENCODING", base_type.base_type_definition.base_type_encoding)
        self.writeChildOptionalElementLiteral(element, "NATIVE-DECLARATION", base_type.base_type_definition.native_declaration)

    def writeSwBaseTypes(self, element: ET.Element, ar_package: ARPackage):
        for base_type in ar_package.getSwBaseTypes():
            data_type_tag = ET.SubElement(element, "SW-BASE-TYPE")
            self.writeIdentifiable(data_type_tag, base_type)
            self.writeBaseTypeDirectDefinition(data_type_tag, base_type)

    def writeCompuScaleConstantContents(self, element: ET.Element, contents: CompuScaleConstantContents):
        compu_const_tag = ET.SubElement(element, "COMPU-CONST")
        if isinstance(contents.compu_const.compu_const_content_type, CompuConstTextContent):
            self.writeChildOptionalElement(compu_const_tag, "VT", contents.compu_const.compu_const_content_type.vt)

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

    def writeCompuMethods(self, element: ET.Element, parent: ARPackage):
        for compu_method in parent.getCompuMethods():
            compu_method_tag = ET.SubElement(element, "COMPU-METHOD")
            self.logger.debug("writeCompuMethods %s" % compu_method.short_name)
            self.writeIdentifiable(compu_method_tag, compu_method)
            self.writeChildOptionalRefElement(compu_method_tag, "UNIT-REF", compu_method.unit_ref)
            self.writeCompuInternalToPhys(compu_method_tag, compu_method)

    def writeApplicationValueSpecification(self, element: ET.Element, spec: ApplicationValueSpecification):
        spec_tag = ET.SubElement(element, "APPLICATION-VALUE-SPECIFICATION")
        self.writeChildOptionalElement(spec_tag, "SHORT-LABEL", spec.short_label)
        self.writeChildOptionalElement(spec_tag, "CATEGORY", spec.category)
        self.writeSwValueCont(spec_tag, spec.sw_value_cont)

    def writeRecordValueSpecification(self, element: ET.Element, spec: RecordValueSpecification):
        spec_tag = ET.SubElement(element, "RECORD-VALUE-SPECIFICATION")
        fields = spec.get_fields()
        if len(fields) > 0:
            fields_tag = ET.SubElement(spec_tag, "FIELDS")
            for field in fields:
                if isinstance(field, ApplicationValueSpecification):
                    self.writeApplicationValueSpecification(fields_tag, field)
                else:
                    raise NotImplementedError("Unsupported Field <%s>" % type(field))

    def writeConstantSpecifications(self, element: ET.Element, parent: ARPackage):
        for spec in parent.getConstantSpecifications():
            spec_tag = ET.SubElement(element, "CONSTANT-SPECIFICATION")
            self.writeIdentifiable(spec_tag, spec)

            if spec.value_spec is not None:
                value_spec_tag = ET.SubElement(spec_tag, "VALUE-SPEC")
                if isinstance(spec.value_spec, ApplicationValueSpecification):
                    self.writeApplicationValueSpecification(value_spec_tag, spec.value_spec)
                elif isinstance(spec.value_spec, RecordValueSpecification):
                    self.writeRecordValueSpecification(value_spec_tag, spec.value_spec)
                else:
                    raise NotImplementedError("Unsupported ConstantSpecification %s" % type(spec.value_spec))
                
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
        self.writeChildOptionalRefElement(constrs_tag, "UNIT-REF", parent.unit_ref)
                
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

    def writeDataConstr(self, element: ET.Element, parent: ARPackage):
        for constr in parent.getDataConstrs():
            child_element = ET.SubElement(element, "DATA-CONSTR")
            self.writeIdentifiable(child_element, constr)
            self.writeDataConstrRules(child_element, constr) 

    def writeUnit(self, element: ET.Element, parent: ARPackage):
        for unit in parent.getUnits():
            self.logger.debug("writeUnit %s" % unit.short_name)
            child_element = ET.SubElement(element, "UNIT")
            self.writeIdentifiable(child_element, unit)
            self.writeChildOptionalElementLiteral(child_element, "DISPLAY-NAME", unit.display_name)
        
    def writeARPackages(self, element: ET.Element, pkgs: List[ARPackage]):
        if len(pkgs) > 0:
            pkgs_tag = ET.SubElement(element, "AR-PACKAGES")

            for pkg in pkgs:
                pkg_tag  = ET.SubElement(pkgs_tag, "AR-PACKAGE")
            
                self.writeElementAttributes(pkg_tag, pkg)
                self.writeShortName(pkg_tag, pkg.short_name)
                self.logger.debug("writeARPackage %s" % pkg.full_name)

                if pkg.getTotalElement() > 0:
                    elements_tag = ET.SubElement(pkg_tag, "ELEMENTS")
                    
                    self.writeApplicationDataTypes(elements_tag, pkg)
                    self.writeCompositionSwComponentTypes(elements_tag, pkg)
                    self.writeSwBaseTypes(elements_tag, pkg)
                    self.writeCompuMethods(elements_tag, pkg)
                    self.writeConstantSpecifications(elements_tag, pkg)
                    self.writeDataConstr(elements_tag, pkg)
                    self.writeUnit(elements_tag, pkg)

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
        root.attrib["xsi:schemaLocation"] = "http://autosar.org/schema/r4.0 AUTOSAR_4-2-2.xsd"
        
        self.writeARPackages(root, document.getARPackages())

        self.saveToFile(filename, root)
        