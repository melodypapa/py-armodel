import xml.etree.cElementTree as ET

from typing import List

from armodel.models.m2.autosar_templates.common_structure.implementation_data_types import ImplementationDataType



from ..models.m2.msr.data_dictionary.auxillary_objects import SwAddrMethod
from ..models.m2.msr.data_dictionary.data_def_properties import SwDataDefProps
from ..models.m2.msr.asam_hdo.units import PhysicalDimension
from ..models.m2.msr.documentation.block_elements import DocumentationBlock
from ..models.m2_msr import CompuConstTextContent, CompuMethod, CompuNominatorDenominator, CompuScale, CompuScaleConstantContents, CompuScaleRationalFormula, CompuScales

from ..models.m2.autosar_templates.common_structure import ApplicationValueSpecification, ArrayValueSpecification, ConstantReference, ConstantSpecification, NumericalValueSpecification, RecordValueSpecification, TextValueSpecification, ValueSpecification
from ..models.m2.autosar_templates.ecuc_description_template import EcucAbstractReferenceValue, EcucContainerValue, EcucInstanceReferenceValue, EcucModuleConfigurationValues, EcucNumericalParamValue, EcucParameterValue, EcucReferenceValue, EcucTextualParamValue, EcucValueCollection
from ..models.m2.autosar_templates.generic_structure.abstract_structure import AnyInstanceRef
from ..models.m2.autosar_templates.sw_component_template.components import PortGroup, SwComponentType, PPortPrototype, PortPrototype, RPortPrototype
from ..models.m2.autosar_templates.sw_component_template.components.instance_refs import InnerPortGroupInCompositionInstanceRef, PModeGroupInAtomicSwcInstanceRef, RModeGroupInAtomicSWCInstanceRef, RModeInAtomicSwcInstanceRef, RVariableInAtomicSwcInstanceRef
from ..models.m2.autosar_templates.sw_component_template.swc_internal_behavior import RunnableEntityArgument, SynchronousServerCallPoint
from ..models.m2.autosar_templates.sw_component_template.swc_internal_behavior.server_call import ServerCallPoint
from ..models.m2.autosar_templates.sw_component_template.swc_internal_behavior.data_elements import ParameterAccess, VariableAccess
from ..models.m2.autosar_templates.sw_component_template.composition import AssemblySwConnector, CompositionSwComponentType, DelegationSwConnector, SwComponentPrototype, SwConnector
from ..models.m2.autosar_templates.sw_component_template.composition.instance_refs import POperationInAtomicSwcInstanceRef, PPortInCompositionInstanceRef, ROperationInAtomicSwcInstanceRef, RPortInCompositionInstanceRef
from ..models.m2.autosar_templates.sw_component_template.port_interface.instance_refs import ApplicationCompositeElementInPortInterfaceInstanceRef
from ..models.m2.autosar_templates.sw_component_template.swc_internal_behavior.instance_refs_usage import AutosarParameterRef, AutosarVariableRef, VariableInAtomicSWCTypeInstanceRef
from ..models.m2.autosar_templates.system_template.instance_refs import VariableDataPrototypeInSystemInstanceRef
from ..models.m2.autosar_templates.sw_component_template.components.instance_refs import PModeGroupInAtomicSwcInstanceRef, RModeGroupInAtomicSWCInstanceRef
from ..models.m2.autosar_templates.system_template.data_mapping import SenderReceiverToSignalGroupMapping, SenderReceiverToSignalMapping
from ..models.m2.autosar_templates.system_template import System, SystemMapping
from ..models.m2.autosar_templates.system_template.network_management import CanNmCluster, CanNmClusterCoupling, CanNmNode, NmCluster, NmConfig, NmNode
from ..models.m2.autosar_templates.system_template.transport_protocols import CanTpConfig
from ..models.m2.autosar_templates.sw_component_template.communication import ClientComSpec, ModeSwitchReceiverComSpec, ModeSwitchSenderComSpec, NonqueuedReceiverComSpec, NonqueuedSenderComSpec, PPortComSpec, ParameterRequireComSpec,  QueuedReceiverComSpec, QueuedSenderComSpec, RPortComSpec, ReceiverComSpec, SenderComSpec, ServerComSpec

from ..models.fibex.fibex_4_multiplatform import Gateway, ISignalMapping
from ..models.fibex.can_communication import CanFrame, CanFrameTriggering, RxIdentifierRange
from ..models.fibex.fibex_core.core_communication import FrameTriggering, IPdu, ISignalGroup, ISignalIPdu, ISignalIPduGroup, ISignalTriggering, PduTriggering, SecuredIPdu, SystemSignal, DcmIPdu, Frame, ISignal, NPdu, NmPdu, SystemSignalGroup
from ..models.fibex.lin_communication import LinFrameTriggering, LinUnconditionalFrame
from ..models.fibex.fibex_core.core_topology import AbstractCanCluster, CanCluster, EcuInstance, CanPhysicalChannel, CommunicationCluster, LinCluster, LinPhysicalChannel, PhysicalChannel

from ..models.internal_behavior import IncludedDataTypeSet, InternalBehavior
from ..models.timing import EOCExecutableEntityRef, ExecutionOrderConstraint, SwcTiming, TimingExtension
from ..models.data_def_properties import ValueList
from ..models.multilanguage_data import MultiLanguageOverviewParagraph, MultiLanguageParagraph, MultilanguageLongName
from ..models.record_layout import SwRecordLayout, SwRecordLayoutGroup, SwRecordLayoutV
from ..models.service_mapping import RoleBasedPortAssignment
from ..models.service_needs import NvBlockNeeds, RoleBasedDataAssignment
from ..models.m2.autosar_templates.sw_component_template.data_type.data_prototypes import ApplicationArrayElement, ApplicationCompositeElementDataPrototype, ApplicationRecordElement, AutosarDataPrototype, DataPrototype, ParameterDataPrototype, VariableDataPrototype
from ..models.bsw_module_template import BswCalledEntity, BswEvent, BswInternalBehavior, BswModeSenderPolicy, BswModuleDescription, BswModuleEntity, BswModuleEntry, BswSchedulableEntity, BswScheduleEvent, BswTimingEvent
from ..models.ar_package import AUTOSAR
from ..models.sw_component import ApplicationSwComponentType, AtomicSwComponentType, ComplexDeviceDriverSwComponentType, DataReceivedEvent, EcuAbstractionSwComponentType, InitEvent, InternalTriggerOccurredEvent, OperationInvokedEvent, PortAPIOption, RTEEvent, ServiceDependency, ServiceSwComponentType, SwcModeSwitchEvent, SwcServiceDependency
from ..models.ar_package import ARPackage
from ..models.ar_ref import RefType
from ..models.calibration import SwAxisGrouped, SwAxisIndividual, SwCalprmAxis, SwCalprmAxisSet, SwValueCont, SwValues
from ..models.common_structure import IncludedModeDeclarationGroupSet, ModeDeclaration, ModeDeclarationGroup, ModeDeclarationGroupPrototype
from ..models.communication import CompositeNetworkRepresentation, TransmissionAcknowledgementRequest
from ..models.datatype import ApplicationArrayDataType, ApplicationCompositeDataType, ApplicationDataType, ApplicationPrimitiveDataType, ApplicationRecordDataType, AutosarDataType, BaseTypeDirectDefinition, DataTypeMappingSet, SwBaseType
from ..models.general_structure import ARElement, AdminData, Identifiable, Limit, MultilanguageReferrable, Referrable, Sdg, SwcBswMapping, SwcBswRunnableMapping

from ..models.annotation import Annotation
from ..models.end_to_end_protection import EndToEndDescription, EndToEndProtection, EndToEndProtectionSet, EndToEndProtectionVariablePrototype
from ..models.m2.autosar_templates.sw_component_template.port_interface import ApplicationError, ClientServerInterface, ClientServerOperation, ModeSwitchInterface, PortInterface, SenderReceiverInterface, TriggerInterface
from ..models.m2.msr.asam_hdo.units import Unit
from ..models.implementation import AutosarEngineeringObject, BswImplementation, Code, EngineeringObject, Implementation, SwcImplementation
from ..models.common_structure import ExecutableEntity, ResourceConsumption
from ..models.sw_component import RunnableEntity, SwcInternalBehavior, TimingEvent
from ..models.ar_object import ARLiteral
from ..models.global_constraints import DataConstr, InternalConstrs, PhysConstrs

from .abstract_arxml_writer import AbstractARXMLWriter
class ARXMLWriter(AbstractARXMLWriter):
    def __init__(self, options=None) -> None:
        super().__init__(options)

    def setShortName(self, parent: ET.Element, name: str) -> ET.Element:
        sub_element = ET.SubElement(parent, "SHORT-NAME")
        sub_element.text = name

        return sub_element
    
    def setChildElementRxIdentifierRange(self, element: ET.Element, key: str, range: RxIdentifierRange):
        if range is not None:
            child_element = ET.SubElement(element, key)
            self.setChildElementOptionalNumericalValue(child_element, "LOWER-CAN-ID", range.getLowerCanId()) 
            self.setChildElementOptionalNumericalValue(child_element, "UPPER-CAN-ID", range.getUpperCanId())
    
    def writeSds(self, parent: ET.Element, sdg: Sdg):
        for sd in sdg.getSds():
            sd_tag = ET.SubElement(parent, "SD")
            sd_tag.attrib['GID'] = sd.gid
            sd_tag.text = sd.value

    def setSdg(self, parent: ET.Element, sdg: Sdg):
        if sdg is not None:
            sdg_tag = ET.SubElement(parent, "SDG")
            sdg_tag.attrib['GID'] = sdg.gid
            self.writeSds(sdg_tag, sdg)
            for sdg_item in sdg.getSdgContentsTypes():
                self.setSdg(sdg_tag, sdg_item)
            
    def writeSdgs(self, parent: ET.Element, admin_data: AdminData):
        sdgs = admin_data.getSdgs()
        if len(sdgs) > 0:
            sdgs_tag = ET.SubElement(parent, "SDGS")
            for sdg in sdgs:
                self.setSdg(sdgs_tag, sdg)
    
    def writeChildLimitElement(self, element: ET.Element, key: str, limit: Limit):
        if limit is not None:
            limit_tag = ET.SubElement(element, key)
            self.setARObjectAttributes(limit_tag, limit)
            if limit.intervalType is not None:
                limit_tag.attrib['INTERVAL-TYPE'] = limit.intervalType
            limit_tag.text = limit.value
    
    def setReferable(self, element: ET.Element, referrable: Referrable):
        self.setARObjectAttributes(element, referrable)
        self.setShortName(element, referrable.short_name)

    def setMultiLongName(self, element: ET.Element, key: str, long_name: MultilanguageLongName):
        if long_name is not None:
            long_name_tag = ET.SubElement(element, key)
            self.setARObjectAttributes(long_name_tag, long_name)
            for l4 in long_name.getL4s():
                l4_tag = ET.SubElement(long_name_tag, "L-4")
                self.setARObjectAttributes(l4_tag, l4)
                if l4.l is not None:
                    l4_tag.attrib['L'] = l4.l
                l4_tag.text = l4.value

    def setMultiLanguageOverviewParagraph(self, element: ET.Element, key: str, paragraph: MultiLanguageOverviewParagraph):
        if paragraph is not None:
            long_name_tag = ET.SubElement(element, key)
            self.setARObjectAttributes(long_name_tag, paragraph)
            for l2 in paragraph.getL2s():
                l2_tag = ET.SubElement(long_name_tag, "L-2")
                self.setARObjectAttributes(l2_tag, l2)
                if l2.l is not None:
                    l2_tag.attrib['L'] = l2.l
                l2_tag.text = l2.value

    def setMultilanguageReferrable(self, element: ET.Element, referrable: MultilanguageReferrable):
        self.setReferable(element, referrable)
        if referrable.longName is not None:
            self.setMultiLongName(element, "LONG-NAME", referrable.longName)

    def setAdminData(self, element: ET.Element, admin_data: AdminData):
        element = ET.SubElement(element, "ADMIN-DATA")
        self.writeSdgs(element, admin_data)

    def setIdentifiable(self, element: ET.Element, identifiable: Identifiable):
        self.setMultilanguageReferrable(element, identifiable)
        self.setAnnotations(element, identifiable.getAnnotations())
        self.setMultiLanguageOverviewParagraph(element, "DESC", identifiable.getDesc())
        self.setChildElementOptionalLiteral(element, "CATEGORY", identifiable.getCategory())
        if identifiable.getAdminData() is not None:
            self.setAdminData(element, identifiable.getAdminData())

    def setARElement(self, parent: ET.Element, ar_element: ARElement):
        self.setIdentifiable(parent, ar_element)
    
    def setTransmissionAcknowledgementRequest(self, element: ET.Element, acknowledge: TransmissionAcknowledgementRequest):
        if (acknowledge != None):
            child_element = ET.SubElement(element, "TRANSMISSION-ACKNOWLEDGE")
            self.setARObjectAttributes(child_element, acknowledge)
            if acknowledge.timeout != None:
                self.setChildElementOptionalFloatValue(child_element, "TIMEOUT", acknowledge.timeout)

    def setSenderComSpec(self, element: ET.Element, com_spec: SenderComSpec):
        representations = com_spec.getCompositeNetworkRepresentations()
        if len(representations) > 0:
            child_element = ET.SubElement(element, "COMPOSITE-NETWORK-REPRESENTATIONS")
            for representation in representations:
                self.setCompositeNetworkRepresentation(child_element, representation)
        self.setChildElementOptionalRefType(element, "DATA-ELEMENT-REF", com_spec.getDataElementRef())
        self.setSwDataDefProps(element, "NETWORK-REPRESENTATION", com_spec.getNetworkRepresentation())
        self.setChildElementOptionalLiteral(element, "HANDLE-OUT-OF-RANGE", com_spec.getHandleOutOfRange())
        self.setTransmissionAcknowledgementRequest(element, com_spec.getTransmissionAcknowledge())
        self.setChildElementOptionalBooleanValue(element, "USES-END-TO-END-PROTECTION", com_spec.getUsesEndToEndProtection())
    
    def setNonqueuedSenderComSpec(self, element: ET.Element, com_spec: NonqueuedSenderComSpec):
        child_element = ET.SubElement(element, "NONQUEUED-SENDER-COM-SPEC")
        self.setARObjectAttributes(child_element, com_spec)
        self.setSenderComSpec(child_element, com_spec)
        self.setInitValue(child_element, com_spec.initValue)
            
    def setServerComSpec(self, element: ET.Element, com_spec: ServerComSpec):
        child_element = ET.SubElement(element, "SERVER-COM-SPEC")
        self.setARObjectAttributes(child_element, com_spec)
        self.setChildElementOptionalRefType(child_element, "OPERATION-REF", com_spec.getOperationRef())
        self.setChildElementOptionalNumericalValue(child_element, "QUEUE-LENGTH",    com_spec.getQueueLength())

    def setQueuedSenderComSpec(self, element: ET.Element, com_spec: QueuedSenderComSpec):
        child_element = ET.SubElement(element, "QUEUED-SENDER-COM-SPEC")
        self.setARObjectAttributes(child_element, com_spec)
        self.setSenderComSpec(child_element, com_spec)

    def setModeSwitchSenderComSpec(self, element: ET.Element, com_spec: ModeSwitchSenderComSpec):
        child_element = ET.SubElement(element, "MODE-SWITCH-SENDER-COM-SPEC")
        self.setARObjectAttributes(child_element, com_spec)
        self.setChildElementOptionalRefType(child_element, "MODE-GROUP-REF", com_spec.getModeGroupRef())
        self.setChildElementOptionalNumericalValue(child_element, "QUEUE-LENGTH", com_spec.getQueueLength())
    
    def writePPortComSpec(self, com_specs_tag: ET.Element, com_spec: PPortComSpec):
        if isinstance(com_spec, NonqueuedSenderComSpec):
            self.setNonqueuedSenderComSpec(com_specs_tag, com_spec)
        elif isinstance(com_spec, ServerComSpec):
            self.setServerComSpec(com_specs_tag, com_spec)
        elif isinstance(com_spec, QueuedSenderComSpec):
            self.setQueuedSenderComSpec(com_specs_tag, com_spec)
        elif isinstance(com_spec, ModeSwitchSenderComSpec):
            self.setModeSwitchSenderComSpec(com_specs_tag, com_spec)
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
        self.setChildElementOptionalRefType(element, "DATA-ELEMENT-REF", com_spec.dataElementRef)
        self.setSwDataDefProps(element, "NETWORK-REPRESENTATION", com_spec.networkRepresentation)
        self.setChildElementOptionalLiteral(element, "HANDLE-OUT-OF-RANGE", com_spec.handleOutOfRange)
        self.setChildElementOptionalBooleanValue(element, "USES-END-TO-END-PROTECTION", com_spec.usesEndToEndProtection)

    def setSwValues(self, element: ET.Element, key: str, sw_values: SwValues):
        if sw_values is not None:
            child_element = ET.SubElement(element, key)
            self.setARObjectAttributes(child_element, sw_values)
            for v in sw_values.getVs():
                self.setChildElementOptionalFloatValue(child_element, "V", v)
            self.setChildElementOptionalLiteral(child_element, "VT", sw_values.vt)

    def setValueList(self, element: ET.Element, key: str, value_list: ValueList):
        if value_list is not None:
            child_element = ET.SubElement(element, key)
            self.setARObjectAttributes(child_element, value_list)
            self.setChildElementOptionalFloatValue(child_element, "V", value_list.v)

    def writeSwValueCont(self, element: ET.Element, cont: SwValueCont):
        child_element = ET.SubElement(element, "SW-VALUE-CONT")
        self.setARObjectAttributes(child_element, cont)
        self.setChildElementOptionalRefType(child_element, "UNIT-REF", cont.unit_ref)
        self.setValueList(child_element, "SW-ARRAYSIZE", cont.sw_arraysize)
        self.setSwValues(child_element, "SW-VALUES-PHYS", cont.sw_values_phys)

    def writeValueSpecification(self, element: ET.Element, value_spec: ValueSpecification):
        self.setARObjectAttributes(element, value_spec)
        if value_spec.short_label is not None:
            self.setChildElementOptionalLiteral(element, "SHORT-LABEL", value_spec.short_label)                                

    def setApplicationValueSpecification(self, element: ET.Element, value_spec: ApplicationValueSpecification):
        value_spec_tag = ET.SubElement(element, "APPLICATION-VALUE-SPECIFICATION")
        self.writeValueSpecification(value_spec_tag, value_spec)
        self.setChildElementOptionalLiteral(value_spec_tag, "CATEGORY", value_spec.category)
        self.writeSwValueCont(value_spec_tag, value_spec.sw_value_cont)

    def setTextValueSpecification(self, element: ET.Element, value_spec: TextValueSpecification):
        value_spec_tag = ET.SubElement(element, "TEXT-VALUE-SPECIFICATION")
        self.writeValueSpecification(value_spec_tag, value_spec)
        self.setChildElementOptionalLiteral(value_spec_tag, "VALUE", value_spec.value)

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
        self.setChildElementOptionalRefType(value_spec_tag, "CONSTANT-REF", value_spec.getConstantRef())

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
        self.setARObjectAttributes(child_element, com_spec)
        self.writeReceiverComSpec(child_element, com_spec)
        self.setChildElementOptionalFloatValue(child_element, "ALIVE-TIMEOUT", com_spec.aliveTimeout)
        self.setChildElementOptionalBooleanValue(child_element, "ENABLE-UPDATE", com_spec.enableUpdated)
        self.setChildElementOptionalBooleanValue(child_element, "HANDLE-NEVER-RECEIVED", com_spec.handleNeverReceived)
        self.setChildElementOptionalLiteral(child_element, "HANDLE-TIMEOUT-TYPE", com_spec.handleTimeoutType)
        self.setInitValue(child_element, com_spec.initValue)

    def writeQueuedReceiverComSpec(self, element: ET.Element, com_spec: QueuedReceiverComSpec):
        child_element = ET.SubElement(element, "QUEUED-RECEIVER-COM-SPEC")
        self.setARObjectAttributes(child_element, com_spec)
        self.writeReceiverComSpec(child_element, com_spec)
        self.setChildElementOptionalNumericalValue(child_element, "QUEUE-LENGTH", com_spec.queueLength)
    
    def writeClientComSpec(self, element: ET.Element, com_spec: ClientComSpec):
        self.logger.debug("writeClientComSpec")
        child_element = ET.SubElement(element, "CLIENT-COM-SPEC")
        self.setARObjectAttributes(child_element, com_spec)
        self.setChildElementOptionalRefType(child_element, "OPERATION-REF", com_spec.getOperationRef())

    def writeParameterRequireComSpec(self, element: ET.Element, com_spec: ParameterRequireComSpec):
        self.logger.debug("writeParameterRequireComSpec")
        child_element = ET.SubElement(element, "PARAMETER-REQUIRE-COM-SPEC")
        self.setARObjectAttributes(child_element, com_spec)
        self.setChildElementOptionalRefType(child_element, "PARAMETER-REF", com_spec.parameter_ref)
        self.setInitValue(child_element, com_spec.init_value)

    def writeModeSwitchReceiverComSpec(self, element: ET.Element, com_spec: ModeSwitchReceiverComSpec):
        self.logger.debug("writeModeSwitchReceiverComSpec")
        child_element = ET.SubElement(element, "MODE-SWITCH-RECEIVER-COM-SPEC")
        self.setARObjectAttributes(child_element, com_spec)
        self.setChildElementOptionalRefType(child_element, "MODE-GROUP-REF", com_spec.modeGroupRef)

    def writeRPortComSpec(self, element: ET.Element, com_spec: RPortComSpec):
        if isinstance(com_spec, NonqueuedReceiverComSpec):
            self.writeNonqueuedReceiverComSpec(element, com_spec)
        elif isinstance(com_spec, QueuedReceiverComSpec):
            self.writeQueuedReceiverComSpec(element, com_spec)
        elif isinstance(com_spec, ClientComSpec):
            self.writeClientComSpec(element, com_spec)
        elif isinstance(com_spec, ModeSwitchReceiverComSpec):
            self.writeModeSwitchReceiverComSpec(element, com_spec)
        elif isinstance(com_spec, ParameterRequireComSpec):
            self.writeParameterRequireComSpec(element, com_spec)
        else:
            raise ValueError("Unsupported RPortComSpec %s" % type(com_spec))
    
    def writePPortPrototype(self, ports_tag: ET.Element, prototype: PPortPrototype):
        prototype_tag = ET.SubElement(ports_tag, "P-PORT-PROTOTYPE")

        self.setIdentifiable(prototype_tag, prototype)
        self.logger.debug("writePPortPrototype %s" % prototype.short_name)

        com_specs = prototype.getProvidedComSpecs()
        if len(com_specs):
            com_specs_tag = ET.SubElement(prototype_tag, "PROVIDED-COM-SPECS")
            for com_spec in com_specs:
                self.writePPortComSpec(com_specs_tag, com_spec)

        self.setChildElementOptionalRefType(prototype_tag, "PROVIDED-INTERFACE-TREF", prototype.getProvidedInterfaceTRef())

    def writeRPortPrototype(self, ports_tag: ET.Element, prototype: RPortPrototype):
        self.logger.debug("writeRPortPrototype %s" % prototype.short_name)
        prototype_tag = ET.SubElement(ports_tag, "R-PORT-PROTOTYPE")
        self.setIdentifiable(prototype_tag, prototype)
        com_specs = prototype.getRequiredComSpecs()
        if len(com_specs) > 0:
            com_specs_tag = ET.SubElement(prototype_tag, "REQUIRED-COM-SPECS")
            for com_spec in com_specs:
                self.writeRPortComSpec(com_specs_tag, com_spec)
        self.setChildElementOptionalRefType(prototype_tag, "REQUIRED-INTERFACE-TREF", prototype.getRequiredInterfaceTRef())
    
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
        #self.setChildElementOptionalRefType(child_element, "CONTEXT-REF", inner_group_iref.contextRef)
        self.setChildElementOptionalRefType(child_element, "TARGET-REF", inner_group_iref.getTargetRef())

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
        self.setIdentifiable(child_element, port_group)
        self.writePortGroupInnerGroupIRefs(child_element, port_group)
        self.writePortGroupOuterPortRefs(child_element, port_group)

    def writeSwComponentTypePortGroups(self, element: ET.Element, parent: SwComponentType):
        port_groups = parent.getPortGroups()
        if len(port_groups) > 0:
            child_element = ET.SubElement(element, "PORT-GROUPS")
            for port_group in port_groups:
                self.writePortGroup(child_element, port_group)
    
    def writeSwComponentType(self, element: ET.Element, sw_component: SwComponentType):
        self.setIdentifiable(element, sw_component)
        port_prototypes = sw_component.getPortPrototypes()
        if len(port_prototypes) > 0:
            ports_tag = ET.SubElement(element, "PORTS")
            self.writePortPrototypes(ports_tag, port_prototypes)
        self.writeSwComponentTypePortGroups(element, sw_component)

    def writeSwComponentPrototype(self, element: ET.Element, prototype: SwComponentPrototype):
        prototype_tag = ET.SubElement(element, "SW-COMPONENT-PROTOTYPE")
        self.setIdentifiable(prototype_tag, prototype)
        self.setChildElementOptionalRefType(prototype_tag, "TYPE-TREF", prototype.getTypeTRef())

    def writeSwComponentPrototypes(self, element: ET.Element, sw_component: CompositionSwComponentType):
        prototypes = sw_component.getSwComponentPrototypes()
        if len(prototypes) > 0:
            components_tag = ET.SubElement(element, "COMPONENTS")
        for prototype in prototypes:
            self.writeSwComponentPrototype(components_tag, prototype)

    def writeAssemblySwConnector(self, element: ET.Element, sw_connector: AssemblySwConnector):
        connector_tag = ET.SubElement(element, "ASSEMBLY-SW-CONNECTOR")
        self.setIdentifiable(connector_tag, sw_connector)

        if sw_connector.getProviderIRef() is not None:
            provider_iref_tag = ET.SubElement(connector_tag, "PROVIDER-IREF")
            provider_iref = sw_connector.getProviderIRef()
            self.setARObjectAttributes(provider_iref_tag, provider_iref)
            self.setChildElementOptionalRefType(provider_iref_tag, "CONTEXT-COMPONENT-REF", provider_iref.getContextComponentRef())
            self.setChildElementOptionalRefType(provider_iref_tag, "TARGET-P-PORT-REF", provider_iref.getTargetPPortRef())

        if sw_connector.getRequesterIRef() is not None:
            requester_iref_tag = ET.SubElement(connector_tag, "REQUESTER-IREF")
            requester_iref = sw_connector.getRequesterIRef()
            self.setARObjectAttributes(requester_iref_tag, requester_iref)
            self.setChildElementOptionalRefType(requester_iref_tag, "CONTEXT-COMPONENT-REF", requester_iref.getContextComponentRef())
            self.setChildElementOptionalRefType(requester_iref_tag, "TARGET-R-PORT-REF", requester_iref.getTargetRPortRef())

    def writeDelegationSwConnector(self, element: ET.Element, sw_connector: DelegationSwConnector):
        connector_tag = ET.SubElement(element, "DELEGATION-SW-CONNECTOR")
        self.setIdentifiable(connector_tag, sw_connector)

        if sw_connector.getInnerPortIRref() is not None:
            inner_port_iref_tag = ET.SubElement(connector_tag, "INNER-PORT-IREF")
            inner_port_iref = sw_connector.getInnerPortIRref()
            if isinstance(inner_port_iref, PPortInCompositionInstanceRef):
                instance_ref_tag = ET.SubElement(inner_port_iref_tag, "P-PORT-IN-COMPOSITION-INSTANCE-REF")
                self.setChildElementOptionalRefType(instance_ref_tag, "CONTEXT-COMPONENT-REF", inner_port_iref.getContextComponentRef())
                self.setChildElementOptionalRefType(instance_ref_tag, "TARGET-P-PORT-REF", inner_port_iref.getTargetPPortRef())
            elif isinstance(inner_port_iref, RPortInCompositionInstanceRef):
                instance_ref_tag = ET.SubElement(inner_port_iref_tag, "R-PORT-IN-COMPOSITION-INSTANCE-REF")
                self.setChildElementOptionalRefType(instance_ref_tag, "CONTEXT-COMPONENT-REF", inner_port_iref.getContextComponentRef())
                self.setChildElementOptionalRefType(instance_ref_tag, "TARGET-R-PORT-REF", inner_port_iref.getTargetRPortRef())
            else:
                self._raiseError("Invalid inner port of DelegationSwConnector <%s>" % sw_connector.getShortName())

        if sw_connector.getOuterPortRef() is not None:
            self.setChildElementOptionalRefType(connector_tag, "OUTER-PORT-REF", sw_connector.getOuterPortRef())
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
            # Change the implementation to compatible with AUTOSAR builder
            for sw_connector in sw_connectors:
                self.writeSwConnector(connectors_tag, sw_connector)
            #for sw_connector in sw_component.getAssemblySwConnectors():
            #    self.writeSwConnector(connectors_tag, sw_connector)
            #for sw_connector in sw_component.getDelegationSwConnectors():
            #    self.writeSwConnector(connectors_tag, sw_connector)

    def writeCompositionSwComponentTypeDataTypeMappingSet(self, element: ET.Element, parent: CompositionSwComponentType):
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
        self.writeCompositionSwComponentTypeDataTypeMappingSet(child_element, sw_component)

    def writeCompositionSwComponentTypes(self, element: ET.Element, ar_package: ARPackage):
        for sw_component in ar_package.getCompositionSwComponentTypes():
            self.writeCompositionSwComponentType(element, sw_component)

    def writeLParagraphs(self, element: ET.Element, paragraph: MultiLanguageParagraph):
        for l1 in paragraph.getL1s():
            l1_tag = ET.SubElement(element, "L-1")
            self.setARObjectAttributes(l1_tag, l1)
            if l1.l is not None:
                l1_tag.attrib['L'] = l1.l
                l1_tag.text = l1.value
    
    def setMultiLanguageParagraphs(self, element: ET.Element, key: str, paragraphs: List[MultiLanguageParagraph]):
        for paragraph in paragraphs:
            child_element = ET.SubElement(element, key)
            self.setARObjectAttributes(child_element, paragraph)
            self.writeLParagraphs(child_element, paragraph)
        return paragraphs

    def setDocumentationBlock(self, element: ET.Element, key: str, block: DocumentationBlock):
        if block is not None:
            child_element = ET.SubElement(element, key)
            self.setARObjectAttributes(child_element, block)
            self.setMultiLanguageParagraphs(child_element, "P", block.getPs())

    def writeGeneralAnnotation(self, element: ET.Element, annotation: Annotation):
        self.setMultiLongName(element, "LABEL", annotation.getLabel())
        self.setChildElementOptionalLiteral(element, "ANNOTATION-ORIGIN", annotation.getAnnotationOrigin())
        self.setDocumentationBlock(element, "ANNOTATION-TEXT", annotation.getAnnotationText())

    def setAnnotations(self, element: ET.Element, annotations: List[Annotation]) :
        if len(annotations) > 0:
            annotations_tag = ET.SubElement(element, "ANNOTATIONS")
            for annotation in annotations:
                annotation_tag = ET.SubElement(annotations_tag, "ANNOTATION")
                self.writeGeneralAnnotation(annotation_tag, annotation)

    def setSwAxisIndividual(self, element: ET.Element, props: SwAxisIndividual):
        child_element = ET.SubElement(element, "SW-AXIS-INDIVIDUAL")
        self.setARObjectAttributes(child_element, props)
        self.setChildElementOptionalRefType(child_element, "INPUT-VARIABLE-TYPE-REF", props.inputVariableTypeRef)
        self.setChildElementOptionalRefType(child_element, "COMPU-METHOD-REF", props.compuMethodRef)
        self.setChildElementOptionalNumericalValue(child_element, "SW-MAX-AXIS-POINTS", props.swMaxAxisPoints) 
        self.setChildElementOptionalNumericalValue(child_element, "SW-MIN-AXIS-POINTS", props.swMinAxisPoints)
        self.setChildElementOptionalRefType(child_element, "DATA-CONSTR-REF", props.dataConstrRef)

    def setSwAxisGrouped(self, element: ET.Element, props: SwAxisGrouped):
        child_element = ET.SubElement(element, "SW-AXIS-GROUPED")
        self.setARObjectAttributes(child_element, props)
        self.setChildElementOptionalRefType(child_element, "SHARED-AXIS-TYPE-REF", props.sharedAxisTypeRef)

    def setSwCalprmAxis(self, element: ET.Element, axis: SwCalprmAxis):
        if axis is not None:
            child_element = ET.SubElement(element, "SW-CALPRM-AXIS")
            self.setChildElementOptionalNumericalValue(child_element, "SW-AXIS-INDEX", axis.sw_axis_index)
            self.setChildElementOptionalLiteral(child_element, "CATEGORY", axis.category)
            if axis.sw_calprm_axis_type_props is not None:
                if isinstance(axis.sw_calprm_axis_type_props, SwAxisIndividual):
                    self.setSwAxisIndividual(child_element, axis.sw_calprm_axis_type_props)
                elif isinstance(axis.sw_calprm_axis_type_props, SwAxisGrouped):
                    self.setSwAxisGrouped(child_element, axis.sw_calprm_axis_type_props)
                else:
                    self._raiseError("Unsupported SwCalprmAxisTypeProps %s" % type(axis.sw_calprm_axis_type_props))

    def setSwCalprmAxisSet(self, element: ET.Element, key: str, set: SwCalprmAxisSet):
        axises = set.getSwCalprmAxises()
        if len(axises) > 0:
            child_element = ET.SubElement(element, key)
            for axis in axises:
                self.setSwCalprmAxis(child_element, axis)

    def writeSwDataDefProsInvalidValue(self, element: ET.Element, props: SwDataDefProps):
        if props.getInvalidValue() is not None:
            child_element = ET.SubElement(element, "INVALID-VALUE")
            self.setValueSpecification(child_element, props.getInvalidValue()) 

    def setSwDataDefProps(self, element: ET.Element, key: str, sw_data_def_props: SwDataDefProps):
        if sw_data_def_props is not None:
            child_element = ET.SubElement(element, key)
            self.setARObjectAttributes(child_element, sw_data_def_props)
            sw_data_def_props_variants_tag = ET.SubElement(child_element, "SW-DATA-DEF-PROPS-VARIANTS")
            sw_data_def_props_conditional_tag = ET.SubElement(sw_data_def_props_variants_tag, "SW-DATA-DEF-PROPS-CONDITIONAL")
            self.setARObjectAttributes(sw_data_def_props_conditional_tag, sw_data_def_props.conditional)
            self.setAnnotations(sw_data_def_props_conditional_tag, sw_data_def_props.getAnnotations())
            self.setChildElementOptionalRefType(sw_data_def_props_conditional_tag, "BASE-TYPE-REF", sw_data_def_props.getBaseTypeRef())
            self.writeSwDataDefProsInvalidValue(sw_data_def_props_conditional_tag, sw_data_def_props)
            self.setChildElementOptionalLiteral(sw_data_def_props_conditional_tag, "SW-CALIBRATION-ACCESS", sw_data_def_props.getSwCalibrationAccess())
            self.setSwCalprmAxisSet(sw_data_def_props_conditional_tag, "SW-CALPRM-AXIS-SET", sw_data_def_props.getSwCalprmAxisSet())
            self.setChildElementOptionalRefType(sw_data_def_props_conditional_tag, "COMPU-METHOD-REF", sw_data_def_props.getCompuMethodRef())
            self.setChildElementOptionalLiteral(sw_data_def_props_conditional_tag, "SW-IMPL-POLICY", sw_data_def_props.getSwImplPolicy())
            self.setChildElementOptionalRefType(sw_data_def_props_conditional_tag, "IMPLEMENTATION-DATA-TYPE-REF", sw_data_def_props.getImplementationDataTypeRef())
            self.setChildElementOptionalRefType(sw_data_def_props_conditional_tag, "DATA-CONSTR-REF", sw_data_def_props.getDataConstrRef())
            self.setChildElementOptionalRefType(sw_data_def_props_conditional_tag, "SW-RECORD-LAYOUT-REF", sw_data_def_props.getSwRecordLayoutRef())
            self.setChildElementOptionalRefType(sw_data_def_props_conditional_tag, "VALUE-AXIS-DATA-TYPE-REF", sw_data_def_props.getValueAxisDataTypeRef())
            self.setChildElementOptionalRefType(sw_data_def_props_conditional_tag, "UNIT-REF", sw_data_def_props.getUnitRef())

    def writeApplicationDataType(self, element: ET.Element, data_type: ApplicationDataType):
        self.writeAutosarDataType(element, data_type)

    def writeApplicationCompositeDataType(self, element: ET.Element, data_type: ApplicationCompositeDataType):
        self.writeApplicationDataType(element, data_type)

    def writeAutosarDataType(self, element: ET.Element, data_type: AutosarDataType):
        self.setARElement(element, data_type)
        self.setSwDataDefProps(element, "SW-DATA-DEF-PROPS", data_type.swDataDefProps)

    def writeApplicationPrimitiveDataType(self, element: ET.Element, data_type: ApplicationPrimitiveDataType):
        self.logger.debug("writeApplicationPrimitiveDataType %s" % data_type.short_name)
        data_type_tag = ET.SubElement(element, "APPLICATION-PRIMITIVE-DATA-TYPE")
        self.writeApplicationDataType(data_type_tag, data_type)

    def setDataPrototype(self, element: ET.Element, prototype: DataPrototype):
        self.setIdentifiable(element, prototype)

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
        self.setChildElementOptionalNumericalValue(element, "BASE-TYPE-SIZE", base_type_definition.base_type_size)
        self.setChildElementOptionalLiteral(element, "BASE-TYPE-ENCODING", base_type_definition.base_type_encoding)
        self.setChildElementOptionalNumericalValue(element, "MEM-ALIGNMENT", base_type_definition.mem_alignment)
        self.setChildElementOptionalLiteral(element, "NATIVE-DECLARATION", base_type_definition.native_declaration)

    def writeSwBaseType(self, element: ET.Element, base_type: SwBaseType):
        data_type_tag = ET.SubElement(element, "SW-BASE-TYPE")
        self.setIdentifiable(data_type_tag, base_type)
        self.writeBaseTypeDirectDefinition(data_type_tag, base_type.baseTypeDefinition)

    def writeCompuScaleConstantContents(self, element: ET.Element, contents: CompuScaleConstantContents):
        compu_const_tag = ET.SubElement(element, "COMPU-CONST")
        if isinstance(contents.compu_const.compu_const_content_type, CompuConstTextContent):
            self.setChildElementOptionalLiteral(compu_const_tag, "VT", contents.compu_const.compu_const_content_type.vt)

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
            self.setARObjectAttributes(child_element, compu_scale)
            self.setChildElementOptionalLiteral(child_element, "SHORT-LABEL", compu_scale.short_label)
            self.setChildElementOptionalLiteral(child_element, "SYMBOL", compu_scale.symbol)
            self.writeChildLimitElement(child_element, "LOWER-LIMIT", compu_scale.lowerLimit)
            self.writeChildLimitElement(child_element, "UPPER-LIMIT", compu_scale.upperLimit)
            self.writeCompuScaleContents(child_element, compu_scale)

    def writeCompuInternalToPhys(self, element: ET.Element, compu_method: CompuMethod):
        if compu_method.compu_internal_to_phys is not None:
            compu_internal_to_phys_tag = ET.SubElement(element, "COMPU-INTERNAL-TO-PHYS")
            self.setARObjectAttributes(compu_internal_to_phys_tag, compu_method.compu_internal_to_phys)
            if isinstance(compu_method.compu_internal_to_phys.compu_content, CompuScales):
                self.writeCompuScales(compu_internal_to_phys_tag, compu_method.compu_internal_to_phys.compu_content)

    def writeCompuMethod(self, element: ET.Element, compu_method: CompuMethod):
        compu_method_tag = ET.SubElement(element, "COMPU-METHOD")
        self.logger.debug("writeCompuMethods %s" % compu_method.short_name)
        self.setIdentifiable(compu_method_tag, compu_method)
        self.setChildElementOptionalRefType(compu_method_tag, "UNIT-REF", compu_method.unit_ref)
        self.writeCompuInternalToPhys(compu_method_tag, compu_method)

    def setApplicationValueSpecification(self, element: ET.Element, spec: ApplicationValueSpecification):
        spec_tag = ET.SubElement(element, "APPLICATION-VALUE-SPECIFICATION")
        self.setChildElementOptionalLiteral(spec_tag, "SHORT-LABEL", spec.short_label)
        self.setChildElementOptionalLiteral(spec_tag, "CATEGORY", spec.category)
        self.writeSwValueCont(spec_tag, spec.sw_value_cont)

    def setRecordValueSpecification(self, element: ET.Element, spec: RecordValueSpecification):
        child_element = ET.SubElement(element, "RECORD-VALUE-SPECIFICATION")
        self.setARObjectAttributes(child_element, spec)
        self.setChildElementOptionalLiteral(child_element, "SHORT-LABEL", spec.short_label)
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
        self.setIdentifiable(spec_tag, spec)

        if spec.getValueSpec() is not None:
            value_spec_tag = ET.SubElement(spec_tag, "VALUE-SPEC")
            self.setValueSpecification(value_spec_tag, spec.getValueSpec())
                
    def setInternalConstrs(self, element: ET.Element, constrs: InternalConstrs):
        if constrs is not None:
            constrs_tag = ET.SubElement(element, "INTERNAL-CONSTRS")
            self.setARObjectAttributes(constrs_tag, constrs)
            if constrs.lower_limit is not None:
                self.writeChildLimitElement(constrs_tag, "LOWER-LIMIT", constrs.lower_limit)
            if constrs.upper_limit is not None:
                self.writeChildLimitElement(constrs_tag, "UPPER-LIMIT", constrs.upper_limit)

    def setPhysConstrs(self, element: ET.Element, constrs: PhysConstrs):
        if constrs is not None:
            child_element = ET.SubElement(element, "PHYS-CONSTRS")
            self.setARObjectAttributes(child_element, constrs)
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
                self.setARObjectAttributes(child_element, rule)
                self.setChildElementOptionalNumericalValue(child_element, "CONSTR-LEVEL", rule.constrLevel)
                self.setPhysConstrs(child_element, rule.physConstrs)
                self.setInternalConstrs(child_element, rule.internalConstrs)

    def writeDataConstr(self, element: ET.Element, constr: DataConstr):
        child_element = ET.SubElement(element, "DATA-CONSTR")
        self.setIdentifiable(child_element, constr)
        self.writeDataConstrRules(child_element, constr) 

    def writeUnit(self, element: ET.Element, unit: Unit):
        self.logger.debug("writeUnit %s" % unit.short_name)
        child_element = ET.SubElement(element, "UNIT")
        self.setIdentifiable(child_element, unit)
        self.setChildElementOptionalLiteral(child_element, "DISPLAY-NAME", unit.getDisplayName())
        self.setChildElementOptionalFloatValue(child_element, "FACTOR-SI-TO-UNIT", unit.getFactorSiToUnit())
        self.setChildElementOptionalFloatValue(child_element, "OFFSET-SI-TO-UNIT", unit.getOffsetSiToUnit())
        self.setChildElementOptionalRefType(child_element, "PHYSICAL-DIMENSION-REF", unit.getPhysicalDimensionRef())

    def setRModeInAtomicSwcInstanceRef(self, element: ET.Element, key: str, iref: RModeInAtomicSwcInstanceRef):
        child_element = ET.SubElement(element, key)
        self.setChildElementOptionalRefType(child_element, "BASE", iref.getBaseRef())
        self.setChildElementOptionalRefType(child_element, "CONTEXT-PORT-REF", iref.getContextPortRef())
        self.setChildElementOptionalRefType(child_element, "CONTEXT-MODE-DECLARATION-GROUP-PROTOTYPE-REF", iref.getContextModeDeclarationGroupPrototypeRef())
        self.setChildElementOptionalRefType(child_element, "TARGET-MODE-DECLARATION-REF", iref.getTargetModeDeclarationRef())

    def setPOperationInAtomicSwcInstanceRef(self, element: ET.Element, key: str, iref: POperationInAtomicSwcInstanceRef):
        child_element = ET.SubElement(element, key)
        self.setChildElementOptionalRefType(child_element, "CONTEXT-P-PORT-REF", iref.context_p_port_ref)
        self.setChildElementOptionalRefType(child_element, "TARGET-PROVIDED-OPERATION-REF", iref.target_provided_operation_ref)

    def setRTEEvent(self, element: ET.Element, event: RTEEvent):
        self.setIdentifiable(element, event)
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
            self.setChildElementOptionalFloatValue(child_element, "PERIOD", event.period)

    def setOperationInvokedEvent(self, element: ET.Element, event: OperationInvokedEvent):
        if event is not None:
            child_element = ET.SubElement(element, "OPERATION-INVOKED-EVENT")
            self.setRTEEvent(child_element, event)
            self.setPOperationInAtomicSwcInstanceRef(child_element, "OPERATION-IREF", event.operation_iref)

    def setSwcModeSwitchEvent(self, element: ET.Element, event: SwcModeSwitchEvent):
        if event is not None:
            child_element = ET.SubElement(element, "SWC-MODE-SWITCH-EVENT")
            self.setRTEEvent(child_element, event)
            self.setChildElementOptionalLiteral(child_element, "ACTIVATION", event.activation)
            irefs = event.getModeIRefs()
            if len(irefs) > 0:
                mode_irefs_tag = ET.SubElement(child_element, "MODE-IREFS")
                for iref in irefs:
                    self.setRModeInAtomicSwcInstanceRef(mode_irefs_tag, "MODE-IREF", iref)

    def setRVariableInAtomicSwcInstanceRef(self, element: ET.Element, iref: RVariableInAtomicSwcInstanceRef):
        if iref is not None:
            child_element = ET.SubElement(element, "DATA-IREF")
            self.setChildElementOptionalRefType(child_element, "CONTEXT-R-PORT-REF", iref.getContextRPortRef())
            self.setChildElementOptionalRefType(child_element, "TARGET-DATA-ELEMENT-REF", iref.getTargetDataElementRef())

    def setDataReceivedEvent(self, element: ET.Element, event: DataReceivedEvent):
        if event is not None:
            child_element = ET.SubElement(element, "DATA-RECEIVED-EVENT")
            self.setRTEEvent(child_element, event)
            self.setRVariableInAtomicSwcInstanceRef(child_element, event.dataIRef)

    def setInternalTriggerOccurredEvent(self, element: ET.Element, event: DataReceivedEvent):
        pass

    def setInitEvent(self, element: ET.Element, event: InitEvent):
        if event is not None:
            child_element = ET.SubElement(element, "INIT-EVENT")
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
                elif isinstance(event, InternalTriggerOccurredEvent):
                    self.setInternalTriggerOccurredEvent(child_element, event)
                elif isinstance(event, InitEvent):
                    self.setInitEvent(child_element, event)
                else:
                    raise NotImplementedError("Unsupported Event <%s>" % type(event))
                
    def writeExclusiveAreas(self, element: ET.Element, behavior: InternalBehavior):
        areas = behavior.getExclusiveAreas()
        if len(areas) > 0:
            areas_tag = ET.SubElement(element, "EXCLUSIVE-AREAS")
            for area in areas:
                child_element = ET.SubElement(areas_tag, "EXCLUSIVE-AREA")
                self.setIdentifiable(child_element, area)

    def writeDataTypeMappingRefs(self, element: ET.Element, behavior: InternalBehavior):
        refs = behavior.getDataTypeMappingRefs()
        if len(refs) > 0:
            refs_tag = ET.SubElement(element, "DATA-TYPE-MAPPING-REFS")
            for ref in refs:
                self.setChildElementOptionalRefType(refs_tag, "DATA-TYPE-MAPPING-REF", ref)

    def writeInternalBehaviorConstantMemories(self, element: ET.Element, behavior: InternalBehavior):
        memories = behavior.getConstantMemorys()
        if len(memories) > 0:
            child_element = ET.SubElement(element, "CONSTANT-MEMORYS")
            for memory in memories:
                self.writeParameterDataPrototype(child_element, memory)
           
    def writeInternalBehavior(self, element: ET.Element, behavior: InternalBehavior):
        self.setIdentifiable(element, behavior)
        self.writeInternalBehaviorConstantMemories(element, behavior)
        self.writeDataTypeMappingRefs(element, behavior)
        self.writeExclusiveAreas(element, behavior)

    def setAutosarVariableRef(self, element: ET.Element, ref: AutosarVariableRef):
        if ref is not None:
            child_element = ET.SubElement(element, "ACCESSED-VARIABLE")
            self.setARObjectAttributes(child_element, ref)
            if ref.getAutosarVariableIRef() is not None:
                child_element = ET.SubElement(child_element, "AUTOSAR-VARIABLE-IREF")
                self.setChildElementOptionalRefType(child_element, "PORT-PROTOTYPE-REF", ref.getAutosarVariableIRef().getPortPrototypeRef())
                self.setChildElementOptionalRefType(child_element, "TARGET-DATA-PROTOTYPE-REF", ref.getAutosarVariableIRef().getTargetDataPrototypeRef())
            self.setChildElementOptionalRefType(child_element, "LOCAL-VARIABLE-REF", ref.getLocalVariableRef())

    def setVariableAccess(self, element: ET.Element, access: VariableAccess):
        child_element = ET.SubElement(element, "VARIABLE-ACCESS")
        self.setIdentifiable(child_element, access)
        self.setAutosarVariableRef(child_element, access.getAccessedVariableRef())

    def writeDataReadAccesses(self, element: ET.Element, entity: RunnableEntity):
        #accesses = entity.getDataReadAccesses():
        pass

    def setAutosarParameterRef(self, element: ET.Element, key: str, parameter_ref: AutosarParameterRef):
        if parameter_ref is not None:
            child_element = ET.SubElement(element, key)
            self.setChildElementOptionalRefType(child_element, "LOCAL-PARAMETER-REF", parameter_ref.local_parameter_ref)

    def writeParameterAccess(self, element: ET.Element, parameter_access: ParameterAccess):
        child_element = ET.SubElement(element, "PARAMETER-ACCESS")
        self.setIdentifiable(child_element, parameter_access)
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

    def setROperationInAtomicSwcInstanceRef(self, element: ET.Element, key: str, iref: ROperationInAtomicSwcInstanceRef):
        if iref is not None:
            child_element = ET.SubElement(element, key)
            self.setChildElementOptionalRefType(child_element, "CONTEXT-R-PORT-REF", iref.context_r_port_ref)
            self.setChildElementOptionalRefType(child_element, "TARGET-REQUIRED-OPERATION-REF", iref.target_required_operation_ref)
        
    def setServerCallPoint(self, element: ET.Element, call_point: ServerCallPoint):
        self.setROperationInAtomicSwcInstanceRef(element, "OPERATION-IREF", call_point.getOperationIRef())
        self.setChildElementOptionalFloatValue(element, "TIMEOUT", call_point.timeout)

    def setSynchronousServerCallPoint(self, element: ET.Element, call_point: SynchronousServerCallPoint):
        child_element = ET.SubElement(element, "SYNCHRONOUS-SERVER-CALL-POINT")
        self.setIdentifiable(child_element, call_point)
        self.setServerCallPoint(child_element, call_point)

    def writeServerCallPoints(self, element: ET.Element, entity: RunnableEntity):
        call_points = entity.getServerCallPoints()
        if len(call_points) > 0:
            child_element = ET.SubElement(element, "SERVER-CALL-POINTS")
            for call_point in call_points:
                if isinstance(call_point, SynchronousServerCallPoint):
                    self.setSynchronousServerCallPoint(child_element, call_point)
                else:
                    self._raiseError("Unsupported ServerCallPoint type <%s>" % type(call_point))

    def writeWrittenLocalVariable(self, element: ET.Element, entity: RunnableEntity):
        variables = entity.getWrittenLocalVariables()
        if len(variables) > 0:
            child_element = ET.SubElement(element, "WRITTEN-LOCAL-VARIABLES")
            for access in variables:
                self.setVariableAccess(child_element, access)

    def setRModeGroupInAtomicSWCInstanceRef(self, element: ET.Element, tag: str, iref: RModeGroupInAtomicSWCInstanceRef):
        if iref is not None:
            child_element = ET.SubElement(element, tag)
            instance_ref_tag = ET.SubElement(child_element, "R-MODE-GROUP-IN-ATOMIC-SWC-INSTANCE-REF")
            self.setChildElementOptionalRefType(instance_ref_tag, "CONTEXT-R-PORT-REF", iref.getContextRPortRef())
            self.setChildElementOptionalRefType(instance_ref_tag, "TARGET-MODE-GROUP-REF", iref.getTargetModeGroupRef())

    def setPModeGroupInAtomicSWCInstanceRef(self, element: ET.Element, tag: str, iref: PModeGroupInAtomicSwcInstanceRef):
        if iref is not None:
            child_element = ET.SubElement(element, tag)
            self.setChildElementOptionalRefType(child_element, "CONTEXT-P-PORT-REF", iref.getContextPPortRef())
            self.setChildElementOptionalRefType(child_element, "TARGET-MODE-GROUP-REF", iref.getTargetModeGroupRef())

    def writeModeAccessPoints(self, element: ET.Element, entity: RunnableEntity):
        points = entity.getModeAccessPoints()
        if len(points) > 0:
            mode_access_points_tag = ET.SubElement(element, "MODE-ACCESS-POINTS")
            for point in points:
                child_element = ET.SubElement(mode_access_points_tag, "MODE-ACCESS-POINT")
                self.setRModeGroupInAtomicSWCInstanceRef(child_element, "MODE-GROUP-IREF", point.getModeGroupIRef())

    def writeModeSwitchPoints(self, element: ET.Element, entity: RunnableEntity):
        points = entity.getModeSwitchPoints()
        if len(points) > 0:
            mode_access_points_tag = ET.SubElement(element, "MODE-SWITCH-POINTS")
            for point in points:
                child_element = ET.SubElement(mode_access_points_tag, "MODE-SWITCH-POINT")
                self.setIdentifiable(child_element, point)
                self.setPModeGroupInAtomicSWCInstanceRef(child_element, "MODE-GROUP-IREF", point.getModeGroupIRef())

    def setRunnableEntityArgument(self, element: ET.Element, argument: RunnableEntityArgument):
        child_element = ET.SubElement(element, "RUNNABLE-ENTITY-ARGUMENT")
        self.setChildElementOptionalLiteral(child_element, "SYMBOL", argument.getSymbol())

    def writeRunnableEntityArguments(self, element: ET.Element, entity: RunnableEntity):
        arguments = entity.getArguments()
        if len(arguments) > 0:
            child_element = ET.SubElement(element, "ARGUMENTS")
            for argument in arguments:
                if isinstance(argument, RunnableEntityArgument):
                    self.setRunnableEntityArgument(child_element, argument)
                else:
                    raise NotImplementedError("Unsupported argument of Runnable Entity <%s>" % type(argument))

    def writeRunnableEntity(self, element: ET.Element, entity: RunnableEntity):
        if entity is not None:
            child_element = ET.SubElement(element, "RUNNABLE-ENTITY")
            self.setExecutableEntity(child_element, entity)
            self.writeRunnableEntityArguments(child_element, entity)
            self.setChildElementOptionalBooleanValue(child_element, "CAN-BE-INVOKED-CONCURRENTLY", entity.getCanBeInvokedConcurrently())
            self.writeParameterAccesses(child_element, entity)
            self.writeDataReceivePointByArguments(child_element, entity)
            self.writeDataSendPoints(child_element, entity)
            self.writeDataWriteAccesses(child_element, entity)
            self.writeModeAccessPoints(child_element, entity)
            self.writeModeSwitchPoints(child_element, entity)
            self.writeReadLocalVariables(child_element, entity)
            self.writeServerCallPoints(child_element, entity)
            self.setChildElementOptionalLiteral(child_element, "SYMBOL", entity.symbol)
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
                self.setIdentifiable(child_element, memory)
                self.setChildElementOptionalLiteral(child_element, "INIT-VALUE", memory.initValue)
                self.setSwDataDefProps(child_element, "SW-DATA-DEF-PROPS", memory.swDataDefProps)
                self.setChildElementOptionalLiteral(child_element, "TYPE", memory.type)
                self.setChildElementOptionalLiteral (child_element, "TYPE-DEFINITION", memory.typeDefinition)

    def writeParameterDataPrototype(self, element: ET.Element, prototype: ParameterDataPrototype):
        child_element = ET.SubElement(element, "PARAMETER-DATA-PROTOTYPE")
        self.setIdentifiable(child_element, prototype)
        self.writeAutosarDataPrototype(child_element, prototype)
        self.setInitValue(child_element, prototype.initValue)

    def writeParameterDataPrototypes(self, element: ET.Element, behavior: SwcInternalBehavior):
        prototypes = behavior.getPerInstanceParameters()
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
                self.setChildElementOptionalBooleanValue(child_element, "INDIRECT-API", option.indirect_api)
                self.writePortDefinedArgumentValues(child_element, option)
                self.setChildElementOptionalRefType(child_element, "PORT-REF", option.port_ref)

    def writeServiceDependency(self, element: ET.Element, dependency: ServiceDependency):
        self.setIdentifiable(element, dependency)

    def writeRoleBasedDataAssignment(self, element: ET.Element, assignment: RoleBasedDataAssignment):
        child_element = ET.SubElement(element, "ROLE-BASED-DATA-ASSIGNMENT")
        self.setChildElementOptionalLiteral(child_element, "ROLE", assignment.role)
        self.setAutosarParameterRef(child_element, "USED-PARAMETER-ELEMENT", assignment.used_parameter_element)
        self.setChildElementOptionalRefType(child_element, "USED-PIM-REF", assignment.used_pim_ref)

    def writeRoleBasedPortAssignment(self, element: ET.Element, assignment: RoleBasedPortAssignment):
        child_element = ET.SubElement(element, "ROLE-BASED-PORT-ASSIGNMENT")
        self.setChildElementOptionalRefType(child_element, "PORT-PROTOTYPE-REF", assignment.port_prototype_ref)
        self.setChildElementOptionalLiteral(child_element, "ROLE", assignment.role)

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
        self.setIdentifiable(child_element, needs)
        self.setChildElementOptionalBooleanValue(child_element, "CALC-RAM-BLOCK-CRC", needs.calc_ram_block_crc)
        self.setChildElementOptionalBooleanValue(child_element, "CHECK-STATIC-BLOCK-ID", needs.check_static_block_id)
        self.setChildElementOptionalNumericalValue(child_element, "N-DATA-SETS", needs.n_data_sets)
        self.setChildElementOptionalNumericalValue(child_element, "N-ROM-BLOCKS", needs.n_rom_blocks)
        self.setChildElementOptionalBooleanValue(child_element, "READONLY", needs.readonly)
        self.setChildElementOptionalLiteral(child_element, "RELIABILITY", needs.reliability)
        self.setChildElementOptionalBooleanValue(child_element, "RESISTANT-TO-CHANGED-SW", needs.resistant_to_changed_sw)
        self.setChildElementOptionalBooleanValue(child_element, "RESTORE-AT-START", needs.restore_at_start)
        self.setChildElementOptionalBooleanValue(child_element, "STORE-AT-SHUTDOWN", needs.store_at_shutdown)
        self.setChildElementOptionalBooleanValue(child_element, "WRITE-ONLY-ONCE", needs.write_only_once)
        self.setChildElementOptionalBooleanValue(child_element, "WRITE-VERIFICATION", needs.write_verification)
        self.setChildElementOptionalLiteral(child_element, "WRITING-PRIORITY", needs.writing_priority)      

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

    def setIncludedDataTypeSets(self, element: ET.Element, sets: List[IncludedDataTypeSet]):
        if len(sets) > 0:
            include_data_type_sets_tag = ET.SubElement(element, "INCLUDED-DATA-TYPE-SETS")
            for set in sets:
                child_element = ET.SubElement(include_data_type_sets_tag, "INCLUDED-DATA-TYPE-SET")
                self.setARObjectAttributes(child_element, set)
                type_refs = set.getDataTypeRefs()
                if len(type_refs) > 0:
                    data_type_refs_tag = ET.SubElement(child_element, "DATA-TYPE-REFS")
                    for type_ref in type_refs:
                        self.setChildElementOptionalRefType(data_type_refs_tag, "DATA-TYPE-REF", type_ref)

    def writeSwcInternalBehavior(self, element: ET.Element, behavior: SwcInternalBehavior):
        self.logger.debug("writeSwInternalBehavior %s" % behavior.short_name)

        child_element = ET.SubElement(element, "SWC-INTERNAL-BEHAVIOR")
        self.writeInternalBehavior(child_element, behavior)
        self.writeRTEEvents(child_element, behavior)
        self.writeExplicitInterRunnableVariables(child_element, behavior)
        self.setChildElementOptionalLiteral(child_element, "HANDLE-TERMINATION-AND-RESTART", behavior.handle_termination_and_restart)
        self.setIncludedDataTypeSets(child_element, behavior.getIncludedDataTypeSets())
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
                self.setARObjectAttributes(artifact_desc_tag, artifact_desc)
                self.setChildElementOptionalLiteral(artifact_desc_tag, "SHORT-LABEL", artifact_desc.short_label)
                self.setChildElementOptionalLiteral(artifact_desc_tag, "CATEGORY", artifact_desc.category)

    def setCode(self, element: ET.SubElement, code_desc: Code):
        self.logger.debug("setCode %s" % code_desc.short_name)
        child_element = ET.SubElement(element, "CODE")
        self.setIdentifiable(child_element, code_desc)
        self.writeArtifactDescriptor(child_element, code_desc)

    def writeCodeDescriptors(self, element: ET.Element, impl: Implementation):
        descs = impl.getCodeDescriptors()
        if len(descs) > 0:
            child_element = ET.SubElement(element, "CODE-DESCRIPTORS")
            for desc in descs:
                if isinstance(desc, Code):
                    self.setCode(child_element, desc)
                else:
                    self._raiseError("Unsupported Code Descriptor <%s>" % type(desc))

    def setMemorySectionOptions(self, element: ET.Element, options: List[ARLiteral]):
        if len(options) > 0:
            child_element = ET.SubElement(element, "OPTIONS")
            for option in options:
                self.setChildElementOptionalLiteral(child_element, "OPTION", option)
            
    def writeMemorySections(self, element: ET.Element, consumption: ResourceConsumption):
        memory_sections = consumption.getMemorySections()
        if len(memory_sections) > 0:
            sections_tag = ET.SubElement(element, "MEMORY-SECTIONS")
            for memory_section in memory_sections:
                child_element = ET.SubElement(sections_tag, "MEMORY-SECTION")
                self.setIdentifiable(child_element, memory_section)
                self.setChildElementOptionalLiteral(child_element, "ALIGNMENT", memory_section.alignment)
                self.setMemorySectionOptions(child_element, memory_section.getOptions())
                self.setChildElementOptionalNumericalValue(child_element, "SIZE", memory_section.size)
                self.setChildElementOptionalRefType(child_element, "SW-ADDRMETHOD-REF", memory_section.swAddrMethodRef)
                self.setChildElementOptionalLiteral(child_element, "SYMBOL", memory_section.symbol)
                self.logger.debug("writeMemorySections %s" % memory_section.short_name)

    def setResourceConsumption(self, element: ET.Element, consumption: ResourceConsumption):
        if consumption is not None:
            child_element = ET.SubElement(element, "RESOURCE-CONSUMPTION")
            self.setIdentifiable(child_element, consumption)
            self.writeMemorySections(child_element, consumption)

    def writeImplementation(self, element: ET.Element, impl: Implementation):
        self.setIdentifiable(element, impl)
        self.writeCodeDescriptors(element, impl)
        self.setChildElementOptionalLiteral(element, "PROGRAMMING-LANGUAGE", impl.programming_language)
        self.setResourceConsumption(element, impl.getResourceConsumption())
        self.setChildElementOptionalLiteral(element, "SW-VERSION", impl.sw_version)
        self.setChildElementOptionalRefType(element, "SWC-BSW-MAPPING-REF", impl.swc_bsw_mapping_ref)
        self.setChildElementOptionalLiteral(element, "USED-CODE-GENERATOR", impl.used_code_generator)
        self.setChildElementOptionalNumericalValue(element, "VENDOR-ID", impl.vendor_id)

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
                self.setChildElementOptionalNumericalValue(child_element, "DATA-ID", data_id)
    
    def setEndToEndDescription(self, element: ET.Element, key: str, desc: EndToEndDescription):
        if desc is not None:
            child_element = ET.SubElement(element, key)
            self.setChildElementOptionalLiteral(child_element, "CATEGORY", desc.category)
            self.writeEndToEndDescriptionDataId(child_element, desc)
            self.setChildElementOptionalNumericalValue(child_element, "DATA-ID-MODE", desc.dataIdMode)
            self.setChildElementOptionalNumericalValue(child_element, "MAX-DELTA-COUNTER-INIT", desc.maxDeltaCounterInit)
            self.setChildElementOptionalNumericalValue(child_element, "CRC-OFFSET", desc.crcOffset)
            self.setChildElementOptionalNumericalValue(child_element, "COUNTER-OFFSET", desc.counterOffset)

    def setVariableDataPrototypeInSystemInstanceRef(self, element: ET.Element, key: str, iref: VariableDataPrototypeInSystemInstanceRef):
        if iref is not None:
            child_element = ET.SubElement(element, key)
            self.setChildElementOptionalRefType(child_element, "CONTEXT-COMPONENT-REF", iref.context_component_refs)
            self.setChildElementOptionalRefType(child_element, "CONTEXT-COMPOSITION-REF", iref.context_composition_ref)
            self.setChildElementOptionalRefType(child_element, "CONTEXT-PORT-REF", iref.context_port_ref)
            self.setChildElementOptionalRefType(child_element, "TARGET-DATA-PROTOTYPE-REF", iref.target_data_prototype_ref)

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
            self.setIdentifiable(child_element, protection)
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
        self.setIdentifiable(child_element, protection_set)
        self.writeEndToEndProtections(child_element, protection_set)

    def writeAutosarDataPrototype(self, element: ET.Element, prototype: AutosarDataPrototype):
        self.setChildElementOptionalRefType(element, "TYPE-TREF", prototype.typeTRef)

    def writeVariableDataPrototype(self, element: ET.Element, prototype: VariableDataPrototype):
        self.logger.debug("writeVariableDataPrototype %s" % prototype.short_name)
        child_element = ET.SubElement(element, "VARIABLE-DATA-PROTOTYPE")
        self.setIdentifiable(child_element, prototype)
        self.setSwDataDefProps(child_element, "SW-DATA-DEF-PROPS", prototype.swDataDefProps)
        self.writeAutosarDataPrototype(child_element, prototype)
        self.setInitValue(child_element, prototype.initValue)

    def writeSenderReceiverInterfaceDataElements(self, element: ET.Element, sr_interface: SenderReceiverInterface):
        data_elements = sr_interface.getDataElements()
        if len(data_elements) > 0:
            data_elements_tag = ET.SubElement(element, "DATA-ELEMENTS")
            for data_element in data_elements:
                if isinstance(data_element, VariableDataPrototype):
                    self.writeVariableDataPrototype(data_elements_tag, data_element)
                else:
                    self._raiseError("Unsupported Data Element <%s>" % type(data_element))

    def writeSenderReceiverInterfaceInvalidationPolicies(self, element: ET.Element, sr_interface: SenderReceiverInterface):
        policies = sr_interface.getInvalidationPolicies()
        if len(policies) > 0:
            policies_tag = ET.SubElement(element, "INVALIDATION-POLICYS")
            for policy in policies:
                child_element = ET.SubElement(policies_tag, "INVALIDATION-POLICY")
                self.setChildElementOptionalRefType(child_element, "DATA-ELEMENT-REF", policy.getDataElementRef())
                self.setChildElementOptionalLiteral(child_element, "HANDLE-INVALID", policy.getHandleInvalid())

    def writeSenderReceiverInterface(self, element: ET.Element, sr_interface: SenderReceiverInterface):
        self.logger.debug("writeSenderReceiverInterface %s" % sr_interface.short_name)
        child_element = ET.SubElement(element, "SENDER-RECEIVER-INTERFACE")
        self.setIdentifiable(child_element, sr_interface)
        self.setChildElementOptionalBooleanValue(child_element, "IS-SERVICE", sr_interface.getIsService())
        self.writeSenderReceiverInterfaceDataElements(child_element, sr_interface)

    def writerBswModuleDescriptionImplementedEntry(self, element: ET.Element, desc: BswModuleDescription):
        entries = desc.getImplementedEntries()
        if len(entries) > 0:
            entries_tag = ET.SubElement(element, "PROVIDED-ENTRYS")
            for entry in entries:
                entry_tag = ET.SubElement(entries_tag, "BSW-MODULE-ENTRY-REF-CONDITIONAL")
                self.setChildElementOptionalRefType(entry_tag, "BSW-MODULE-ENTRY-REF", entry)

    def setModeDeclarationGroupPrototype(self, element: ET.Element, prototype: ModeDeclarationGroupPrototype):
        self.setIdentifiable(element, prototype)
        self.setChildElementOptionalRefType(element, "TYPE-TREF", prototype.type_tref)

    def writeProvidedModeGroup(self, element: ET.Element, parent: BswModuleDescription):
        mode_groups = parent.getProvidedModeGroups()
        if len(mode_groups) > 0:
            mode_groups_tag = ET.SubElement(element, "PROVIDED-MODE-GROUPS")
            for mode_group in mode_groups:
                child_element = ET.SubElement(mode_groups_tag, "MODE-DECLARATION-GROUP-PROTOTYPE") 
                self.setModeDeclarationGroupPrototype(child_element, mode_group)

    def writeCanEnterExclusiveAreaRefs(self, element: ET.Element, entity: ExecutableEntity):
        refs = entity.getCanEnterExclusiveAreaRefs()
        if len(refs) > 0:
            child_element = ET.SubElement(element, "CAN-ENTER-EXCLUSIVE-AREA-REFS")
            for ref in refs:
                self.setChildElementOptionalRefType(child_element, "CAN-ENTER-EXCLUSIVE-AREA-REF", ref)

    def setExecutableEntity(self, element: ET.Element, entity: ExecutableEntity):
        self.setIdentifiable(element, entity)
        self.writeCanEnterExclusiveAreaRefs(element, entity)
        self.setChildElementOptionalFloatValue(element, "MINIMUM-START-INTERVAL", entity.getMinimumStartInterval())
        self.setChildElementOptionalRefType(element, "SW-ADDR-METHOD-REF", entity.getSwAddrMethodRef())

    def writeBswModuleEntityManagedModeGroup(self, element: ET.Element, entity: BswModuleEntity):
        mode_group_refs = entity.getManagedModeGroupRefs()
        if len(mode_group_refs) > 0:
            mode_groups_tag = ET.SubElement(element, "MANAGED-MODE-GROUPS")
            for mode_group_ref in mode_group_refs:
                child_element = ET.SubElement(mode_groups_tag, "MODE-DECLARATION-GROUP-PROTOTYPE-REF-CONDITIONAL")
                self.setChildElementOptionalRefType(child_element, "MODE-DECLARATION-GROUP-PROTOTYPE-REF", mode_group_ref)

    def setBswModuleEntity(self, element: ET.Element, entity: BswModuleEntity):
        self.setExecutableEntity(element, entity)
        self.setChildElementOptionalRefType(element, "IMPLEMENTED-ENTRY-REF", entity.implementedEntryRef)
        self.writeBswModuleEntityManagedModeGroup(element, entity)

    def setBswCalledEntity(self, element: ET.Element, entity: BswCalledEntity):
        self.logger.debug("setBswCalledEntity %s" % entity.short_name)
        child_element = ET.SubElement(element, "BSW-CALLED-ENTITY")
        self.setBswModuleEntity(child_element, entity)

    def setBswSchedulableEntity(self, element: ET.Element, entity: BswSchedulableEntity):
        self.logger.debug("setBswCalledEntity %s" % entity.short_name)
        child_element = ET.SubElement(element, "BSW-SCHEDULABLE-ENTITY")
        self.setBswModuleEntity(child_element, entity)

    def writeBswInternalBehaviorBswModuleEntities(self, element: ET.Element, parent: BswInternalBehavior):
        entities = parent.getBswModuleEntities()    
        if len(entities) > 0:
            child_element = ET.SubElement(element, "ENTITYS")
            for entity in entities:
                if isinstance(entity, BswCalledEntity):
                    self.setBswCalledEntity(child_element, entity)
                elif isinstance(entity, BswSchedulableEntity):
                    self.setBswSchedulableEntity(child_element, entity)
                else:
                    self._raiseError("Unsupported BswModuleEntity <%s>" % type(entity))

    def setBswEvent(self, element: ET.Element, event: BswEvent):
        self.setIdentifiable(element, event)
        self.setChildElementOptionalRefType(element, "STARTS-ON-EVENT-REF", event.startsOnEventRef)

    def setBswScheduleEvent(self, element: ET.Element, event: BswScheduleEvent):
        self.setBswEvent(element, event)

    def setBswTimingEvent(self, element: ET.Element, event: BswTimingEvent):
        self.logger.debug("setBswTimingEvent %s" % event.short_name)
        child_element = ET.SubElement(element, "BSW-TIMING-EVENT")
        self.setBswScheduleEvent(child_element, event)
        self.setChildElementOptionalFloatValue(child_element, "PERIOD", event.period)

    def writeBswInternalBehaviorBswEvents(self, element: ET.Element, parent: BswInternalBehavior):
        events = parent.getBswEvents()
        if len(events) > 0:
            child_element = ET.SubElement(element, "EVENTS")
            for event in events:
                if isinstance(event, BswTimingEvent):
                    self.setBswTimingEvent(child_element, event)
                else:
                    self._raiseError("Unsupported BswModuleEntity <%s>" % type(event))

    def setBswModeSenderPolicy(self, element: ET.Element, policy: BswModeSenderPolicy):
        child_element = ET.SubElement(element, "BSW-MODE-SENDER-POLICY")
        self.setChildElementOptionalRefType(child_element, "PROVIDED-MODE-GROUP-REF", policy.getProvidedModeGroupRef())
        self.setChildElementOptionalNumericalValue(child_element, "QUEUE-LENGTH", policy.getQueueLength())

    def writeBswInternalBehaviorModeSenderPolicy(self, element: ET.Element, parent: BswInternalBehavior):
        policies = parent.getModeSenderPolicies()
        if len(policies) > 0:
            child_element = ET.SubElement(element, "MODE-SENDER-POLICYS")
            for policy in policies:
                if isinstance(policy, BswModeSenderPolicy):
                    self.setBswModeSenderPolicy(child_element, policy)
                else:
                    self._raiseError("Unsupported ModeSenderPolicy type <%s>." % type(policy))

    def setIncludedModeDeclarationGroupSet(self, element: ET.Element, group_set: IncludedModeDeclarationGroupSet):
        child_element = ET.SubElement(element, "INCLUDED-MODE-DECLARATION-GROUP-SET")

    def writeBswInternalBehaviorIncludedModeDeclarationGroupSets(self, element: ET.Element, behavior: BswInternalBehavior):
        group_sets = behavior.getIncludedModeDeclarationGroupSets()
        if len(group_sets) > 0:
            child_element = ET.SubElement(element, "INCLUDED-MODE-DECLARATION-GROUP-SETS")
            for group_set in group_sets:
                self.setIncludedModeDeclarationGroupSet(child_element, group_set)

    def setBswInternalBehavior(self, element: ET.Element, behavior: BswInternalBehavior):
        child_element = ET.SubElement(element, "BSW-INTERNAL-BEHAVIOR")
        self.writeInternalBehavior(child_element, behavior)
        self.writeBswInternalBehaviorBswModuleEntities(child_element, behavior)
        self.writeBswInternalBehaviorBswEvents(child_element, behavior)
        self.writeBswInternalBehaviorModeSenderPolicy(child_element, behavior)
        self.writeBswInternalBehaviorIncludedModeDeclarationGroupSets(child_element, behavior)

    def writeBswModuleDescriptionInternalBehaviors(self, element: ET.Element, behaviors: List[InternalBehavior]):
        if len(behaviors) > 0:
            child_element = ET.SubElement(element, "INTERNAL-BEHAVIORS")
            for behavior in behaviors:
                if isinstance(behavior, BswInternalBehavior):
                    self.setBswInternalBehavior(child_element, behavior)
                else:
                    self._raiseError("Unsupported BswInternalBehavior <%s>" % type(behavior))

    def writeBswModuleDescription(self, element: ET.Element, desc: BswModuleDescription):
        self.logger.debug("writeBswModuleDescription %s" % desc.short_name)
        child_element = ET.SubElement(element, "BSW-MODULE-DESCRIPTION")
        self.setIdentifiable(child_element, desc)
        self.setChildElementOptionalNumericalValue(child_element, "MODULE-ID", desc.module_id)
        self.writerBswModuleDescriptionImplementedEntry(child_element, desc)
        self.writeProvidedModeGroup(child_element, desc)
        #self.readRequiredModeGroup(element, bsw_module_description)
        self.writeBswModuleDescriptionInternalBehaviors(child_element, desc.getBswInternalBehaviors())

    def writeBswModuleEntityManagedModeGroup(self, element: ET.Element, entity: BswModuleEntity):
        mode_group_refs = entity.getManagedModeGroupRefs()
        if len(mode_group_refs) > 0:
            mode_groups_tag = ET.SubElement(element, "MANAGED-MODE-GROUPS")
            for mode_group_ref in mode_group_refs:
                child_element = ET.SubElement(mode_groups_tag, "MODE-DECLARATION-GROUP-PROTOTYPE-REF-CONDITIONAL")
                self.setChildElementOptionalRefType(child_element, "MODE-DECLARATION-GROUP-PROTOTYPE-REF", mode_group_ref)

    def writeBswModuleEntry(self, element: ET.Element, entry: BswModuleEntry):
        self.logger.debug("writeBswModuleDescription %s" % entry.short_name)
        child_element = ET.SubElement(element, "BSW-MODULE-ENTRY")
        self.setIdentifiable(child_element, entry)
        self.setChildElementOptionalNumericalValue(child_element, "SERVICE-ID", entry.service_id)
        self.setChildElementOptionalBooleanValue(child_element, "IS-REENTRANT", entry.is_reentrant)
        self.setChildElementOptionalBooleanValue(child_element, "IS-SYNCHRONOUS", entry.is_synchronous)
        self.setChildElementOptionalLiteral(child_element, "CALL-TYPE", entry.call_type)
        self.setChildElementOptionalLiteral(child_element, "EXECUTION-CONTEXT", entry.execution_context)
        self.setChildElementOptionalLiteral(child_element, "SW-SERVICE-IMPL-POLICY", entry.sw_service_impl_policy)
        

    def setSwcBswRunnableMapping(self, element: ET.SubElement, mapping: SwcBswRunnableMapping):
        child_element = ET.SubElement(element, "SWC-BSW-RUNNABLE-MAPPING")
        self.setChildElementOptionalRefType(child_element, "BSW-ENTITY-REF", mapping.bswEntityRef)
        self.setChildElementOptionalRefType(child_element, "SWC-RUNNABLE-REF", mapping.swcRunnableRef)

    def writeSwcBswRunnableMappings(self, element: ET.Element, parent: SwcBswMapping):
        runnable_mappings = parent.getRunnableMappings()
        if len(runnable_mappings) > 0:
            child_element = ET.SubElement(element, "RUNNABLE-MAPPINGS")
            for mapping in runnable_mappings:
                if isinstance(mapping, SwcBswRunnableMapping):
                    self.setSwcBswRunnableMapping(child_element, mapping)
                else:
                    self._raiseError("Unsupported Runnable Mapping <%s>" % type(mapping))

    def setSwcBswMapping(self, element: ET.Element, mapping: SwcBswMapping):
        self.logger.debug("writeBswModuleDescription %s" % mapping.short_name)
        child_element = ET.SubElement(element, "SWC-BSW-MAPPING")
        self.setIdentifiable(child_element, mapping)
        self.setChildElementOptionalRefType(child_element, "BSW-BEHAVIOR-REF", mapping.bswBehaviorRef)
        self.writeSwcBswRunnableMappings(child_element, mapping)
        self.setChildElementOptionalRefType(child_element, "SWC-BEHAVIOR-REF", mapping.swcBehaviorRef)

    def writeEngineeringObject(self, element: ET.Element, engineering_obj: EngineeringObject):
        self.setARObjectAttributes(element, engineering_obj)
        self.setChildElementOptionalLiteral(element, "SHORT-LABEL", engineering_obj.short_label)
        self.setChildElementOptionalLiteral(element, "CATEGORY", engineering_obj.category)
        
    def setAutosarEngineeringObject(self, element: ET.Element, obj: AutosarEngineeringObject):
        self.logger.debug("readArtifactDescriptor %s", obj.short_label)
        child_element = ET.SubElement(element, "AUTOSAR-ENGINEERING-OBJECT")
        self.writeEngineeringObject(child_element, obj)

    def writeArtifactDescriptor(self, element: ET.Element, code_desc: Code):
        artifact_descs = code_desc.getArtifactDescriptors()
        if len(artifact_descs) > 0:
            child_element = ET.SubElement(element, "ARTIFACT-DESCRIPTORS")
            for artifact_desc in artifact_descs:
                if isinstance(artifact_desc, AutosarEngineeringObject):
                    self.setAutosarEngineeringObject(child_element, artifact_desc)
                else:
                    self._raiseError("Unsupported Artifact descriptor <%s>" % type(artifact_desc))

    def writeBswImplementationVendorSpecificModuleDefRefs(self, element: ET.Element, parent: BswImplementation):
        refs = parent.getVendorSpecificModuleDefRefs()
        if len(refs) > 0:
            child_element = ET.SubElement(element, "VENDOR-SPECIFIC-MODULE-DEF-REFS")
            if child_element != None:
                for ref in refs:
                    self.setChildElementOptionalRefType(child_element, "VENDOR-SPECIFIC-MODULE-DEF-REF", ref)

    def writeBswImplementation(self, element: ET.Element, impl: BswImplementation):
        self.logger.debug("writeBswModuleDescription %s" % impl.short_name)
        child_element = ET.SubElement(element, "BSW-IMPLEMENTATION")
        self.writeImplementation(child_element, impl)
        self.setChildElementOptionalLiteral(child_element, "AR-RELEASE-VERSION", impl.ar_release_version)
        self.setChildElementOptionalRefType(child_element, "BEHAVIOR-REF", impl.behavior_ref)
        self.writeBswImplementationVendorSpecificModuleDefRefs(child_element, impl)

    def writeImplementationDataTypeElements(self, element: ET.Element, parent: ImplementationDataType):
        sub_elements = parent.getImplementationDataTypeElements()
        if len(sub_elements) > 0:
            sub_elements_tag = ET.SubElement(element, "SUB-ELEMENTS")
            for type_element in sub_elements:
                child_element = ET.SubElement(sub_elements_tag, "IMPLEMENTATION-DATA-TYPE-ELEMENT")
                self.setIdentifiable(child_element, type_element)
                self.setChildElementOptionalLiteral(child_element, "ARRAY-SIZE", type_element.getArraySize())
                self.setChildElementOptionalLiteral(child_element, "ARRAY-SIZE-SEMANTICS", type_element.getArraySizeSemantics())
                self.setSwDataDefProps(child_element, "SW-DATA-DEF-PROPS", type_element.getSwDataDefProps())

    def writeImplementationDataType(self, element: ET.Element, data_type: ImplementationDataType):
        self.logger.debug("writeImplementationDataType %s" % data_type.short_name)
        child_element = ET.SubElement(element, "IMPLEMENTATION-DATA-TYPE")
        self.writeAutosarDataType(child_element, data_type)
        self.writeImplementationDataTypeElements(child_element, data_type)
        self.setChildElementOptionalLiteral(child_element, "TYPE-EMITTER", data_type.getTypeEmitter())

    def writeArgumentDataPrototypes(self, element: ET.Element, parent: ClientServerOperation):
        arguments = parent.getArgumentDataPrototypes()
        if len(arguments) > 0:
            arguments_tag = ET.SubElement(element, "ARGUMENTS")
            for prototype in arguments:
                child_element = ET.SubElement(arguments_tag, "ARGUMENT-DATA-PROTOTYPE")
                self.setIdentifiable(child_element, prototype)
                self.setSwDataDefProps(child_element, "SW-DATA-DEF-PROPS", prototype.swDataDefProps)
                self.setChildElementOptionalRefType(child_element, "TYPE-TREF", prototype.typeTRef)
                self.setChildElementOptionalLiteral(child_element, "DIRECTION", prototype.direction)
                self.setChildElementOptionalLiteral(child_element, "SERVER-ARGUMENT-IMPL-POLICY", prototype.server_argument_impl_policy)

    def writePossibleErrorRefs(self, element: ET.Element, parent: ClientServerOperation):
        error_refs = parent.getPossbileErrorRefs()
        if len(error_refs) > 0:
            error_refs_tag = ET.SubElement(element, "POSSIBLE-ERROR-REFS")
            for error_ref in error_refs:
                self.setChildElementOptionalRefType(error_refs_tag, "POSSIBLE-ERROR-REF", error_ref)

    def writeClientServerOperation(self, element: ET.Element, operation: ClientServerOperation):
        self.logger.debug("writeClientServerOperation %s" % operation.short_name)
        child_element = ET.SubElement(element, "CLIENT-SERVER-OPERATION")
        self.setIdentifiable(child_element, operation)
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
        self.setIdentifiable(child_element, error)
        self.setChildElementOptionalNumericalValue(child_element, "ERROR-CODE", error.error_code)

    def writePossibleErrors(self, element: ET.Element, parent: ClientServerInterface):
        errors = parent.getPossibleErrors()
        if len(errors) > 0:
            errors_tag = ET.SubElement(element, "POSSIBLE-ERRORS")
            for error in errors:
                if isinstance(error, ApplicationError):
                    self.writeApplicationError(errors_tag, error)
                else:
                    self._raiseError("Unsupported PossibleError %s" % type(error))

    def setPortInterface(self, element: ET.Element, port_interface: PortInterface):
        self.setIdentifiable(element, port_interface)
        self.setChildElementOptionalBooleanValue(element, "IS-SERVICE", port_interface.isService)
        self.setChildElementOptionalLiteral(element, "SERVICE-KIND", port_interface.serviceKind)

    def writeClientServerInterface(self, element: ET.Element, cs_interface: ClientServerInterface):
        self.logger.debug("writeClientServerInterface %s" % cs_interface.short_name)
        child_element = ET.SubElement(element, "CLIENT-SERVER-INTERFACE")
        self.setPortInterface(child_element, cs_interface)
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
        self.setIdentifiable(child_element, layout)
        self.setSwRecordLayoutGroup(child_element, "SW-RECORD-LAYOUT-GROUP", layout.swRecordLayoutGroup)

    def writeSwAddrMethod(self, element: ET.Element, method: SwAddrMethod):
        self.logger.debug("writeSwAddrMethod %s" % method.short_name)
        child_element = ET.SubElement(element, "SW-RECORD-LAYOUT")

    def writeTriggerInterface(self, element: ET.Element, trigger_if: TriggerInterface):
        self.logger.debug("writeTriggerInterface %s" % trigger_if.short_name)
        child_element = ET.SubElement(element, "SW-RECORD-LAYOUT")

    def writeServiceSwComponentType(self, element: ET.Element, sw_component: ServiceSwComponentType):
        self.logger.debug("writeServiceSwComponentType %s" % sw_component.short_name)
        child_element = ET.SubElement(element, "SERVICE-SW-COMPONENT-TYPE")
        self.writeAtomicSwComponentType(child_element, sw_component)

    def writeDataTypeMaps(self, element: ET.Element, parent: DataTypeMappingSet):
        maps = parent.getDataTypeMaps()
        if len(maps) > 0:
            maps_tag = ET.SubElement(element, "DATA-TYPE-MAPS")
            for map in maps:
                child_element = ET.SubElement(maps_tag, "DATA-TYPE-MAP")
                self.setARObjectAttributes(child_element, map)
                self.setChildElementOptionalRefType(child_element, "APPLICATION-DATA-TYPE-REF", map.application_data_type_ref)
                self.setChildElementOptionalRefType(child_element, "IMPLEMENTATION-DATA-TYPE-REF", map.implementation_data_type_ref)

    def writeModeRequestTypeMaps(self, element: ET.Element, parent: DataTypeMappingSet):
        maps = parent.getModeRequestTypeMaps()
        if len(maps) > 0:
            maps_tag = ET.SubElement(element, "MODE-REQUEST-TYPE-MAPS")
            for map in maps:
                child_element = ET.SubElement(maps_tag, "MODE-REQUEST-TYPE-MAP")
                self.setARObjectAttributes(child_element, map)
                self.setChildElementOptionalRefType(child_element, "IMPLEMENTATION-DATA-TYPE-REF", map.implementation_data_type_ref)
                self.setChildElementOptionalRefType(child_element, "MODE-GROUP-REF", map.mode_group_ref)

    def writeDataTypeMappingSet(self, element: ET.Element, mapping_set: DataTypeMappingSet):
        self.logger.debug("writeDataTypeMappingSet %s" % mapping_set.short_name)
        child_element = ET.SubElement(element, "DATA-TYPE-MAPPING-SET")
        self.setIdentifiable(child_element, mapping_set)
        self.writeDataTypeMaps(child_element, mapping_set)
        self.writeModeRequestTypeMaps(child_element, mapping_set)

    def setModeDeclaration(self, element: ET.Element, mode_declaration: ModeDeclaration):
        child_element = ET.SubElement(element, "MODE-DECLARATION")
        self.setIdentifiable(child_element, mode_declaration)
        self.setChildElementOptionalNumericalValue(child_element, "VALUE", mode_declaration.getValue())

    def writeModeDeclarationGroupModeDeclaration(self, element: ET.Element, parent: ModeDeclarationGroup):
        mode_declarations = parent.getModeDeclarations()
        if len(mode_declarations) > 0:
            child_element = ET.SubElement(element, "MODE-DECLARATIONS")
            for mode_declaration in mode_declarations:
                self.setModeDeclaration(child_element, mode_declaration)

    def writeModeDeclarationGroup(self, element: ET.Element, group: ModeDeclarationGroup):
        self.logger.debug("writeModeDeclarationGroup %s" % group.short_name)
        child_element = ET.SubElement(element, "MODE-DECLARATION-GROUP")
        self.setIdentifiable(child_element, group)
        self.setChildElementOptionalRefType(child_element, "INITIAL-MODE-REF", group._initial_mode_ref)
        self.writeModeDeclarationGroupModeDeclaration(child_element, group)
        self.setChildElementOptionalNumericalValue(child_element, "ON-TRANSITION-VALUE", group.getOnTransitionValue())

    def writeModeSwitchInterfaceModeGroup(self, element: ET.Element, parent: ModeSwitchInterface):
        mode_groups = parent.getModeGroups()
        if len(mode_groups) > 0:
            mode_group = mode_groups[0]
            child_element = ET.SubElement(element, "MODE-GROUP")
            self.setIdentifiable(child_element, mode_group)
            self.setChildElementOptionalRefType(child_element, "TYPE-TREF", mode_group.type_tref)

    def writeModeSwitchInterface(self, element: ET.Element, mode_interface: ModeSwitchInterface):
        self.logger.debug("writeModeSwitchInterface %s" % mode_interface.short_name)
        child_element = ET.SubElement(element, "MODE-SWITCH-INTERFACE")
        self.setPortInterface(child_element, mode_interface)
        self.writeModeSwitchInterfaceModeGroup(child_element, mode_interface)

    def setEOCExecutableEntityRefSuccessorRefs(self, element: ET.Element, successor_refs: List[RefType]):
        if len(successor_refs) > 0:
            child_element = ET.SubElement(element, "SUCCESSOR-REFS")
            for successor_ref in successor_refs:
                self.setChildElementOptionalRefType(child_element, "SUCCESSOR-REF", successor_ref)

    def writeEOCExecutableEntityRef(self, element: ET.Element, entity_ref: EOCExecutableEntityRef):
        child_element = ET.SubElement(element, "EOC-EXECUTABLE-ENTITY-REF")
        self.setIdentifiable(child_element, entity_ref)
        self.setEOCExecutableEntityRefSuccessorRefs(child_element, entity_ref.getSuccessorRefs())

    def writeExecutionOrderConstraintOrderedElement(self, element: ET.Element, constraint: ExecutionOrderConstraint):
        order_elements = constraint.getOrderedElements()
        if len(order_elements) > 0:
            child_element = ET.SubElement(element, "ORDERED-ELEMENTS")
            for order_element in order_elements:
                if isinstance(order_element, EOCExecutableEntityRef):
                    self.writeEOCExecutableEntityRef(child_element, order_element)
                else:
                    self._raiseError("Unsupported order element <%s>" % type(order_element))

    def writeExecutionOrderConstraint(self, element: ET.Element, constraint: ExecutionOrderConstraint):
        self.logger.debug("writeExecutionOrderConstraint %s" % constraint.short_name)
        child_element = ET.SubElement(element, "EXECUTION-ORDER-CONSTRAINT")
        self.setIdentifiable(child_element, constraint)
        self.writeExecutionOrderConstraintOrderedElement(child_element, constraint)

    def writeTimingRequirements(self, element: ET.Element, extension: TimingExtension):
        requirements = extension.getTimingRequirements()
        if len(requirements) > 0:
            child_element = ET.SubElement(element, "TIMING-REQUIREMENTS")
            for requirement in requirements:
                if isinstance(requirement, ExecutionOrderConstraint):
                    self.writeExecutionOrderConstraint(child_element, requirement)
                else:
                    self._raiseError("Unsupported timing requirement <%s>" % type(requirement))

    def writeTimingExtension(self, element: ET.Element, extension: TimingExtension):
        self.writeTimingRequirements(element, extension)

    def writeSwcTiming(self, element: ET.Element, timing: SwcTiming):
        self.logger.debug("writeSWcTiming %s" % timing.short_name)
        child_element = ET.SubElement(element, "SWC-TIMING")
        self.setIdentifiable(child_element, timing)
        self.writeTimingExtension(child_element, timing)

    def writePduToFrameMappings(self, element: ET.Element, parent: Frame):
        mappings = parent.getPduToFrameMappings()
        if len(mappings) > 0:
            mappings_tags = ET.SubElement(element, "PDU-TO-FRAME-MAPPINGS")
            for mapping in mappings:
                child_element = ET.SubElement(mappings_tags, "PDU-TO-FRAME-MAPPING")
                self.setIdentifiable(child_element, mapping)
                self.setChildElementOptionalLiteral(child_element, "PACKING-BYTE-ORDER", mapping.packingByteOrder)
                self.setChildElementOptionalRefType(child_element, "PDU-REF", mapping.pduRef)
                self.setChildElementOptionalNumericalValue(child_element, "START-POSITION", mapping.startPosition)

    def writeFrame(self, element: ET.Element, frame: Frame):
        self.setIdentifiable(element, frame)
        self.setChildElementOptionalNumericalValue(element, "FRAME-LENGTH",  frame.frameLength)
        self.writePduToFrameMappings(element, frame)

    def writeLinUnconditionalFrame(self, element: ET.Element, frame: LinUnconditionalFrame):
        self.logger.debug("LinUnconditionalFrame %s" % frame.short_name)
        child_element = ET.SubElement(element, "LIN-UNCONDITIONAL-FRAME")
        self.writeFrame(child_element, frame)

    def writeNmNode(self, element: ET.Element, nm_node: NmNode):
        self.setChildElementOptionalRefType(element, "CONTROLLER-REF", nm_node.getControllerRef())
        self.setChildElementOptionalRefType(element, "NM-IF-ECU-REF", nm_node.getNmIfEcuRef())
        self.setChildElementOptionalNumericalValue(element, "NM-NODE-ID", nm_node.getNmNodeId())

        refs = nm_node.getRxNmPduRefs()
        if len(refs) > 0:
            refs_tag = ET.SubElement(element, "RX-NM-PDU-REFS")
            for ref in refs:
                self.setChildElementOptionalRefType(refs_tag, "RX-NM-PDU-REF", ref)

        refs = nm_node.getTxNmPduRefs()
        if len(refs) > 0:
            refs_tag = ET.SubElement(element, "TX-NM-PDU-REFS")
            for ref in refs:
                self.setChildElementOptionalRefType(refs_tag, "TX-NM-PDU-REF", ref)

    def writeCanNmNode(self, element: ET.Element, nm_node: CanNmNode):
        self.logger.debug("writeCanNmNode %s" % nm_node.short_name)
        child_element = ET.SubElement(element, "CAN-NM-NODE")
        self.setIdentifiable(child_element, nm_node)
        self.writeNmNode(child_element, nm_node)

        self.setChildElementOptionalFloatValue(child_element, "NM-MSG-CYCLE-OFFSET", nm_node.getNmMsgCycleOffset())
        self.setChildElementOptionalFloatValue(child_element, "NM-MSG-REDUCED-TIME", nm_node.getNmMsgReducedTime())
        self.setChildElementRxIdentifierRange(child_element, "NM-RANGE-CONFIG", nm_node.getNmRangeConfig())

    def writeNmClusterNmNodes(self, element: ET.Element, parent: NmCluster):
        nodes = parent.getNmNodes()
        if len(nodes) > 0:
            child_element = ET.SubElement(element, "NM-NODES")
            for node in nodes:
                if isinstance(node, CanNmNode):
                    self.writeCanNmNode(child_element, node)
                else:
                    self._raiseError("Unsupported Nm Node <%s>" % type(node))

    def setCanNmClusterCoupling(self, element: ET.Element, coupling: CanNmClusterCoupling):
        child_element = ET.SubElement(element, "CAN-NM-CLUSTER-COUPLING")
        refs = coupling.getCoupledClusterRefs()
        if len(refs) > 0:
            refs_tag = ET.SubElement(child_element, "COUPLED-CLUSTER-REFS")
            for ref in refs:
                self.setChildElementOptionalRefType(refs_tag, "COUPLED-CLUSTER-REF", ref)

        self.setChildElementOptionalBooleanValue(child_element, "NM-BUSLOAD-REDUCTION-ENABLED", coupling.getNmBusloadReductionEnabled())
        self.setChildElementOptionalBooleanValue(child_element, "NM-IMMEDIATE-RESTART-ENABLED", coupling.getNmImmediateRestartEnabled())

    def writeNmConfigNmClusterCouplings(self, element: ET.Element, config: NmConfig):
        self.logger.debug("writeNmConfigNmClusterCouplings %s" % config.getShortName())
        couplings = config.getNmClusterCouplings()
        if len(couplings) > 0:
            child_element= ET.SubElement(element, "NM-CLUSTER-COUPLINGS")
            for coupling in couplings:
                if isinstance(coupling, CanNmClusterCoupling):
                    self.setCanNmClusterCoupling(child_element, coupling)
                else:
                    self._raiseError("Unsupported Nm Cluster Coupling <%s>" % type(coupling))

    def writeNmCluster(self, element: ET.Element, cluster: NmCluster):
        self.setChildElementOptionalRefType(element, "COMMUNICATION-CLUSTER-REF", cluster.communicationClusterRef)
        self.setChildElementOptionalNumericalValue(element, "NM-CHANNEL-ID", cluster.nmChannelId)
        self.setChildElementOptionalBooleanValue(element, "NM-CHANNEL-SLEEP-MASTER", cluster.nmChannelSleepMaster)
        self.writeNmClusterNmNodes(element, cluster)
        self.setChildElementOptionalBooleanValue(element, "NM-SYNCHRONIZING-NETWORK", cluster.getNmSynchronizingNetwork())

    def writeCanNmCluster(self, element: ET.Element, cluster: CanNmCluster):
        self.logger.debug("WriteCanNmCluster %s" % cluster.short_name)
        child_element = ET.SubElement(element, "CAN-NM-CLUSTER")
        self.setIdentifiable(child_element, cluster)
        self.writeNmCluster(child_element, cluster)

        self.setChildElementOptionalBooleanValue(child_element, "NM-BUSLOAD-REDUCTION-ACTIVE", cluster.getNmBusloadReductionActive())
        self.setChildElementOptionalBooleanValue(child_element, "NM-CAR-WAKE-UP-RX-ENABLED", cluster.getNmCarWakeUpRxEnabled())
        self.setChildElementOptionalNumericalValue(child_element, "NM-CBV-POSITION", cluster.getNmCbvPosition())
        self.setChildElementOptionalBooleanValue(child_element, "NM-CHANNEL-ACTIVE", cluster.getNmChannelActive())
        self.setChildElementOptionalFloatValue(child_element, "NM-IMMEDIATE-NM-CYCLE-TIME", cluster.getNmImmediateNmCycleTime())
        self.setChildElementOptionalNumericalValue(child_element, "NM-IMMEDIATE-NM-TRANSMISSIONS", cluster.getNmImmediateNmTransmissions())
        self.setChildElementOptionalFloatValue(child_element, "NM-MESSAGE-TIMEOUT-TIME", cluster.getNmMessageTimeoutTime())
        self.setChildElementOptionalFloatValue(child_element, "NM-MSG-CYCLE-TIME", cluster.getNmMsgCycleTime())
        self.setChildElementOptionalFloatValue(child_element, "NM-NETWORK-TIMEOUT", cluster.getNmNetworkTimeout())
        self.setChildElementOptionalNumericalValue(child_element, "NM-NID-POSITION", cluster.getNmNidPosition())
        self.setChildElementOptionalFloatValue(child_element, "NM-REMOTE-SLEEP-INDICATION-TIME", cluster.getNmRemoteSleepIndicationTime())
        self.setChildElementOptionalFloatValue(child_element, "NM-REPEAT-MESSAGE-TIME", cluster.getNmRepeatMessageTime())
        self.setChildElementOptionalNumericalValue(child_element, "NM-USER-DATA-LENGTH", cluster.getNmUserDataLength())
        self.setChildElementOptionalFloatValue(child_element, "NM-WAIT-BUS-SLEEP-TIME", cluster.getNmWaitBusSleepTime())

    def writeNmConfigNmClusters(self, element: ET.Element, parent: NmConfig):
        clusters = parent.getNmClusters()
        if len(clusters) > 0:
            child_element = ET.SubElement(element, "NM-CLUSTERS")
            for cluster in clusters:
                if isinstance(cluster, CanNmCluster):
                    self.writeCanNmCluster(child_element, cluster)
                else:
                    self._raiseError("Unsupported Nm Cluster <%s>" % type(cluster))

    def writeNmConfig(self, element: ET.Element, config: NmConfig):
        self.logger.debug("WriteNmConfig %s" % config.short_name)
        child_element = ET.SubElement(element, "NM-CONFIG")
        self.setIdentifiable(child_element, config)
        self.writeNmConfigNmClusters(child_element, config)
        self.writeNmConfigNmClusterCouplings(child_element, config)

    def writeNmPdu(self, element: ET.Element, pdu: NmPdu):
        self.logger.debug("NmPdu %s" % pdu.short_name)
        child_element = ET.SubElement(element, "NM-PDU")
        self.setIdentifiable(child_element, pdu)
        self.writeIPdu(child_element, pdu)

    def writeNPdu(self, element: ET.Element, pdu: NPdu):
        self.logger.debug("NPdu %s" % pdu.short_name)
        child_element = ET.SubElement(element, "N-PDU")
        self.setIdentifiable(child_element, pdu)
        self.writeIPdu(child_element, pdu)

    def writeIPdu(self, element: ET.Element, pdu: IPdu):
        self.setChildElementOptionalLiteral(element, "LENGTH", pdu.getLength())

    def writeDcmIPdu(self, element: ET.Element, pdu: DcmIPdu):
        self.logger.debug("DcmIPdu %s" % pdu.short_name)
        child_element = ET.SubElement(element, "DCM-I-PDU")
        self.setIdentifiable(child_element, pdu)
        self.writeIPdu(child_element, pdu)
        self.setChildElementOptionalLiteral(child_element, "DIAG-PDU-TYPE", pdu.getDiagPduType())

    def writeSecuredIPdu(self, element: ET.Element, pdu: DcmIPdu):
        self.logger.debug("SecuredIPdu %s" % pdu.short_name)
        child_element = ET.SubElement(element, "SECURED-I-PDU")
        self.setIdentifiable(child_element, pdu)
        self.writeIPdu(child_element, pdu)

    def writeCanTpConfig(self, element: ET.Element, config: CanTpConfig):
        self.logger.debug("CanTpConfig %s" % config.short_name)
        child_element = ET.SubElement(element, "CAN-TP-CONFIG")
        self.setIdentifiable(child_element, config)

    def writeFrameTriggering(self, element: ET.Element, triggering: FrameTriggering):
        ref_list = triggering.getFramePortRefs()
        if len(ref_list) > 0:
            frame_port_refs_tag = ET.SubElement(element, "FRAME-PORT-REFS")
            for ref in ref_list:
                self.setChildElementOptionalRefType(frame_port_refs_tag, "FRAME-PORT-REF", ref)
        self.setChildElementOptionalRefType(element, "FRAME-REF", triggering.getFrameRef())

        refs = triggering.getPduTriggeringRefs()
        if len(refs) > 0:
            triggerings_tag = ET.SubElement(element, "PDU-TRIGGERINGS")
            for ref in refs:
                 child_element = ET.SubElement(triggerings_tag, 'PDU-TRIGGERING-REF-CONDITIONAL')
                 self.setChildElementOptionalRefType(child_element, "PDU-TRIGGERING-REF", ref)

    def writeCanFrameTriggering(self, element: ET.Element, triggering: CanFrameTriggering):
        self.logger.debug("WRite CanFrameTriggering %s" % triggering.getShortName())
        child_element = ET.SubElement(element, "CAN-FRAME-TRIGGERING")
        self.setIdentifiable(child_element, triggering)
        self.writeFrameTriggering(child_element, triggering)
        self.setChildElementOptionalLiteral(child_element, "CAN-ADDRESSING-MODE", triggering.getCanAddressingMode())
        self.setChildElementOptionalBooleanValue(child_element, "CAN-FD-FRAME-SUPPORT", triggering.getCanFdFrameSupport())
        self.setChildElementOptionalLiteral(child_element, "CAN-FRAME-RX-BEHAVIOR", triggering.getCanFrameRxBehavior())
        self.setChildElementOptionalLiteral(child_element, "CAN-FRAME-TX-BEHAVIOR", triggering.getCanFrameTxBehavior())
        self.setChildElementOptionalNumericalValue(child_element, "IDENTIFIER", triggering.getIdentifier())
        self.setChildElementRxIdentifierRange(child_element, "RX-IDENTIFIER-RANGE", triggering.getRxIdentifierRange())

    def writeLinFrameTriggering(self, element: ET.Element, triggering: LinFrameTriggering):
        self.logger.debug("Write LinFrameTriggering %s" % triggering.getShortName())
        child_element = ET.SubElement(element, "LIN-FRAME-TRIGGERING")
        self.setIdentifiable(child_element, triggering)
        self.writeFrameTriggering(child_element, triggering)
        self.setChildElementOptionalNumericalValue(child_element, "IDENTIFIER", triggering.getIdentifier())
        self.setChildElementOptionalLiteral(child_element, "LIN-CHECKSUM", triggering.getLinChecksum())

    def writeISignalTriggering(self, element: ET.Element, triggering: ISignalTriggering):
        self.logger.debug("Write ISignalTriggering %s" % triggering.getShortName())
        child_element = ET.SubElement(element, "I-SIGNAL-TRIGGERING")
        self.setIdentifiable(child_element, triggering)
        self.setChildElementOptionalRefType(child_element, "I-SIGNAL-GROUP-REF", triggering.getISignalGroupRef())
        ref_list = triggering.getISignalPortRefs()
        if len(ref_list) > 0:
            i_signal_port_refs_tag = ET.SubElement(child_element, "I-SIGNAL-PORT-REFS")
            for ref in ref_list:
                self.setChildElementOptionalRefType(i_signal_port_refs_tag, "I-SIGNAL-PORT-REF", ref)
        self.setChildElementOptionalRefType(child_element, "I-SIGNAL-REF", triggering.getISignalRef())

    def writePduTriggering(self, element: ET.Element, triggering: PduTriggering):
        self.logger.debug("Write PduTriggering %s" % triggering.getShortName())
        child_element = ET.SubElement(element, "PDU-TRIGGERING")
        self.setIdentifiable(child_element, triggering)
        ref_list = triggering.getIPduPortRefs()
        if len(ref_list) > 0:
            i_signal_port_refs_tag = ET.SubElement(child_element, "I-PDU-PORT-REFS")
            for ref in ref_list:
                self.setChildElementOptionalRefType(i_signal_port_refs_tag, "I-PDU-PORT-REF", ref)
        self.setChildElementOptionalRefType(child_element, "I-PDU-REF", triggering.getIPduRef())

        refs = triggering.getISignalTriggeringRefs()
        if len(refs) > 0:
            triggerings_tag = ET.SubElement(child_element, "I-SIGNAL-TRIGGERINGS")
            for ref in refs:
                 child_element = ET.SubElement(triggerings_tag, 'I-SIGNAL-TRIGGERING-REF-CONDITIONAL')
                 self.setChildElementOptionalRefType(child_element, "I-SIGNAL-TRIGGERING-REF", ref)

    def writePhysicalChannel(self, element: ET.Element, channel: PhysicalChannel):
        connectors = channel.getCommConnectorRefs()
        if len(connectors) > 0:
            connectors_tag = ET.SubElement(element, "COMM-CONNECTORS")
            for connector in connectors:
                 child_element = ET.SubElement(connectors_tag, 'COMMUNICATION-CONNECTOR-REF-CONDITIONAL')
                 self.setChildElementOptionalRefType(child_element, "COMMUNICATION-CONNECTOR-REF", connector)

        triggerings = channel.getFrameTriggerings()
        if len(triggerings) > 0:
            triggerings_tag = ET.SubElement(element, "FRAME-TRIGGERINGS")
            for triggering in triggerings:
                if isinstance(triggering, CanFrameTriggering):
                    self.writeCanFrameTriggering(triggerings_tag, triggering)
                elif isinstance(triggering, LinFrameTriggering):
                    self.writeLinFrameTriggering(triggerings_tag, triggering)
                else:
                    raise NotImplementedError("Unsupported Frame Triggering <%s>" % type(triggering))
                
        triggerings = channel.getISignalTriggerings()
        if len(triggerings) > 0:
            triggerings_tag = ET.SubElement(element, "I-SIGNAL-TRIGGERINGS")
            for triggering in triggerings:
                if isinstance(triggering, ISignalTriggering):
                    self.writeISignalTriggering(triggerings_tag, triggering)
                else:
                    raise NotImplementedError("Unsupported ISignalTriggering <%s>" % type(triggering))
                
        triggerings = channel.getPduTriggerings()
        if len(triggerings) > 0:
            triggerings_tag = ET.SubElement(element, "PDU-TRIGGERINGS")
            for triggering in triggerings:
                if isinstance(triggering, PduTriggering):
                    self.writePduTriggering(triggerings_tag, triggering)
                else:
                    raise NotImplementedError("Unsupported PduTriggering <%s>" % type(triggering))

    def writeCanPhysicalChannel(self, element: ET.Element, channel: CanPhysicalChannel):
        self.logger.debug("CanPhysicalChannel %s" % channel.short_name)
        child_element = ET.SubElement(element, "CAN-PHYSICAL-CHANNEL")
        self.setIdentifiable(child_element, channel)
        self.writePhysicalChannel(child_element, channel)

    def writeLinPhysicalChannel(self, element: ET.Element, channel: LinPhysicalChannel):
        self.logger.debug("LinPhysicalChannel %s" % channel.short_name)
        child_element = ET.SubElement(element, "LIN-PHYSICAL-CHANNEL")
        self.setIdentifiable(child_element, channel)
        self.writePhysicalChannel(child_element, channel)

    def writeCommunicationClusterPhysicalChannels(self, element: ET.Element, cluster: CommunicationCluster):
        channels = cluster.getPhysicalChannels()
        if len(channels) > 0:
            child_element = ET.SubElement(element, "PHYSICAL-CHANNELS")
            for channel in channels:
                if isinstance(channel, CanPhysicalChannel):
                    self.writeCanPhysicalChannel(child_element, channel)
                elif isinstance(channel, LinPhysicalChannel):
                    self.writeLinPhysicalChannel(child_element, channel)
                else:
                    raise NotImplementedError("Unsupported Physical Channel <%s>" % type(channel))

    def writeCommunicationCluster(self, element: ET.Element, cluster: CommunicationCluster):
        self.setChildElementOptionalNumericalValue(element, "BAUDRATE", cluster.getBaudrate())
        self.writeCommunicationClusterPhysicalChannels(element, cluster)
        self.setChildElementOptionalLiteral(element, "PROTOCOL-NAME", cluster.getProtocolName())
        self.setChildElementOptionalLiteral(element, "PROTOCOL-VERSION", cluster.getProtocolVersion())

    def readAbstractCanCluster(self, element: ET.Element, cluster: AbstractCanCluster):
        self.setChildElementOptionalNumericalValue(element, "CAN-FD-BAUDRATE", cluster.getCanFdBaudrate())

    def writeLinCluster(self, element: ET.Element, cluster: LinCluster):
        self.logger.debug("LinCluster %s" % cluster.short_name)
        child_element = ET.SubElement(element, "LIN-CLUSTER")
        self.setIdentifiable(child_element, cluster)
        child_element = ET.SubElement(child_element, "LIN-CLUSTER-VARIANTS")
        child_element = ET.SubElement(child_element, "LIN-CLUSTER-CONDITIONAL")
        self.writeCommunicationCluster(child_element, cluster)

    def writeCanCluster(self, element: ET.Element, cluster: CanCluster):
        self.logger.debug("CanCluster %s" % cluster.short_name)
        child_element = ET.SubElement(element, "CAN-CLUSTER")
        self.setIdentifiable(child_element, cluster)

        child_element = ET.SubElement(child_element, "CAN-CLUSTER-VARIANTS")
        child_element = ET.SubElement(child_element, "CAN-CLUSTER-CONDITIONAL")
        self.writeCommunicationCluster(child_element, cluster)
        self.readAbstractCanCluster(child_element, cluster)

    def writeCanFrame(self, element: ET.Element, frame: CanFrame):
        self.logger.debug("CanFrame %s" % frame.short_name)
        child_element = ET.SubElement(element, "CAN-FRAME")
        self.writeFrame(child_element, frame)

    def writeEcuInstance(self, element: ET.Element, instance: EcuInstance):
        self.logger.debug("EcuInstance %s" % instance.short_name)
        child_element = ET.SubElement(element, "ECU-INSTANCE")
        self.setIdentifiable(child_element, instance)

    def writeSystemSignalGroup(self, element: ET.Element, group: SystemSignalGroup):
        self.logger.debug("Write SystemSignalGroup %s" % group.short_name)
        child_element = ET.SubElement(element, "SYSTEM-SIGNAL-GROUP")
        self.setIdentifiable(child_element, group)
        signal_refs = group.getSystemSignalRefs()
        if len(signal_refs) > 0:
            signal_refs_tag = ET.SubElement(child_element, "SYSTEM-SIGNAL-REFS")
            for signal_ref in signal_refs:
                self.setChildElementOptionalRefType(signal_refs_tag, "SYSTEM-SIGNAL-REF", signal_ref)

    def setSenderReceiverToSignalMapping(self, element: ET.Element, mapping: SenderReceiverToSignalMapping):
        child_element = ET.SubElement(element, "SENDER-RECEIVER-TO-SIGNAL-MAPPING")
        self.setVariableDataPrototypeInSystemInstanceRef(child_element, "DATA-ELEMENT-IREF", mapping.getDataElementIRef())
        self.setChildElementOptionalRefType(child_element, "SYSTEM-SIGNAL-REF", mapping.getSystemSignalRef())

    def setSenderReceiverToSignalGroupMapping(self, element: ET.Element, mapping: SenderReceiverToSignalGroupMapping):
        child_element = ET.SubElement(element, "SENDER-RECEIVER-TO-SIGNAL-GROUP-MAPPING")
        self.setVariableDataPrototypeInSystemInstanceRef(child_element, "DATA-ELEMENT-IREF", mapping.getDataElementIRef())
        self.setChildElementOptionalRefType(child_element, "SIGNAL-GROUP-REF", mapping.getSignalGroupRef())
    
    def writeSystemMappingDataMappings(self, element: ET.Element, system_mapping: SystemMapping):
        data_mappings = system_mapping.getDataMappings()
        if len(data_mappings) > 0:
            child_element = ET.SubElement(element, "DATA-MAPPINGS")
            for data_mapping in data_mappings:
                if isinstance(data_mapping, SenderReceiverToSignalMapping):
                    self.setSenderReceiverToSignalMapping(child_element, data_mapping)
                elif isinstance(data_mapping, SenderReceiverToSignalGroupMapping):
                    self.setSenderReceiverToSignalGroupMapping(child_element, data_mapping)
                else:
                    raise NotImplementedError("Unsupported Data Mapping %s" % type(data_mapping))

    def writeSystemMapping(self, element: ET.Element, mapping: SystemMapping):
        self.logger.debug("Write SystemMapping %s" % mapping.short_name)
        child_element = ET.SubElement(element, "SYSTEM-MAPPING")
        self.setIdentifiable(child_element, mapping)
        self.writeSystemMappingDataMappings(child_element, mapping)

    def writeSystemMappings(self, element: ET.Element, system: System):
        mappings = system.getMappings()
        if len(mappings) > 0:
            mappings_tag = ET.SubElement(element, "MAPPINGS")
            for mapping in mappings:
                if isinstance(mapping, SystemMapping):
                    self.writeSystemMapping(mappings_tag, mapping)
                else:
                    raise NotImplementedError("Unsupported Mapping %s" % type(mapping))
                
    def writeSystem(self, element: ET.Element, system: System):
        self.logger.debug("Write System %s" % system.short_name)
        child_element = ET.SubElement(element, "SYSTEM")
        self.setARElement(child_element, system)

        self.setChildElementOptionalLiteral(child_element, "ECU-EXTRACT-VERSION", system.getEcuExtractVersion())
        refs = system.getFibexElementRefs()
        if len(refs) > 0:
            fibex_elements_tag = ET.SubElement(child_element, "FIBEX-ELEMENTS")
            for ref in refs:
                fibex_element_ref_conditional_tag = ET.SubElement(fibex_elements_tag, "FIBEX-ELEMENT-REF-CONDITIONAL")
                self.setChildElementOptionalRefType(fibex_element_ref_conditional_tag, "FIBEX-ELEMENT-REF", ref)

        self.writeSystemMappings(child_element, system)

    def writePhysicalDimension(self, element: ET.Element, dimension: PhysicalDimension):
        self.logger.debug("Write PhysicalDimension %s" % dimension.short_name)
        child_element = ET.SubElement(element, "PHYSICAL-DIMENSION")
        self.setARElement(child_element, dimension)
        self.setChildElementOptionalNumericalValue(child_element, "CURRENT-EXP", dimension.getCurrentExp())
        self.setChildElementOptionalNumericalValue(child_element, "LENGTH-EXP", dimension.getLengthExp())

    def setISignalMappings(self, element: ET.Element, mappings: List[ISignalMapping]):
        if len(mappings) > 0:
            mappings_tag = ET.SubElement(element, "SIGNAL-MAPPINGS")
            for mapping in mappings:
                child_element = ET.SubElement(mappings_tag, "I-SIGNAL-MAPPING")
                self.setChildElementOptionalRefType(child_element, "SOURCE-SIGNAL-REF", mapping.sourceSignalRef)
                self.setChildElementOptionalRefType(child_element, "TARGET-SIGNAL-REF", mapping.targetSignalRef)

    def writeGateway(self, element: ET.Element, gateway: Gateway):
        self.logger.debug("Gateway %s" % gateway.short_name)
        child_element = ET.SubElement(element, "GATEWAY")
        self.setIdentifiable(child_element, gateway)
        self.setChildElementOptionalRefType(child_element, "ECU-REF", gateway.ecuRef)
        self.setISignalMappings(child_element, gateway.getSignalMappings())

    def writeISignal(self, element: ET.Element, signal: ISignal):
        self.logger.debug("ISignal %s" % signal.short_name)
        child_element = ET.SubElement(element, "I-SIGNAL")
        self.setIdentifiable(child_element, signal)
        self.setChildElementOptionalLiteral(child_element, "DATA-TYPE-POLICY", signal.dataTypePolicy)
        self.setInitValue(child_element, signal.initValue)
        self.setChildElementOptionalNumericalValue(child_element, "LENGTH", signal.length)
        self.setSwDataDefProps(child_element, "NETWORK-REPRESENTATION-PROPS", signal.networkRepresentationProps)
        self.setChildElementOptionalRefType(child_element, "SYSTEM-SIGNAL-REF", signal.systemSignalRef)

    def writeEcucValueCollectionEcucValues(self, element: ET.Element, collection: EcucValueCollection):
        value_refs = collection.getEcucValueRefs()
        if len(value_refs) > 0:
            ecuc_values_tag = ET.SubElement(element, "ECUC-VALUES")
            for value_ref in value_refs:
                child_element = ET.SubElement(ecuc_values_tag, "ECUC-MODULE-CONFIGURATION-VALUES-REF-CONDITIONAL")
                self.setChildElementOptionalRefType(child_element, "ECUC-MODULE-CONFIGURATION-VALUES-REF", value_ref) 

    def writeEcucValueCollection(self, element: ET.Element, collection: EcucValueCollection):
        self.logger.debug("EcucValueCollection %s" % collection.short_name)
        child_element = ET.SubElement(element, "ECUC-VALUE-COLLECTION")
        self.setIdentifiable(child_element, collection)
        self.setChildElementOptionalRefType(child_element, "ECU-EXTRACT-REF", collection.getEcuExtractRef())
        self.writeEcucValueCollectionEcucValues(child_element, collection)

    def writeEcucContainerValueSubContainers(self, element: ET.Element, container: EcucContainerValue):
        sub_containers = container.getSubContainers()
        if len(sub_containers) > 0:
            sub_containers_tag = ET.SubElement(element, "SUB-CONTAINERS")
            for sub_container in sub_containers:
                if isinstance(sub_container, EcucContainerValue):
                    self.writeEcucContainValue(sub_containers_tag, sub_container)
                else:
                    raise NotImplementedError("Unsupported Sub Container %s" % type(container)) 
                
    def writeEcucParameterValue(self, element: ET.Element, param_value: EcucParameterValue):
        self.setChildElementOptionalRefType(element, "DEFINITION-REF", param_value.getDefinitionRef())
        self.setAnnotations(element, param_value.getAnnotations())

    def setEcucTextualParamValue(self, element: ET.Element, param_value: EcucTextualParamValue):
        child_element = ET.SubElement(element, "ECUC-TEXTUAL-PARAM-VALUE")
        self.writeEcucParameterValue(child_element, param_value)
        self.setChildElementOptionalLiteral(child_element, "VALUE", param_value.getValue())

    def setEcucNumericalParamValue(self, element: ET.Element, param_value: EcucNumericalParamValue):
        child_element = ET.SubElement(element, "ECUC-NUMERICAL-PARAM-VALUE")
        self.writeEcucParameterValue(child_element, param_value)
        self.setChildElementOptionalNumericalValue(child_element, "VALUE", param_value.getValue())
                
    def writeEcucContainerValueParameterValues(self, element: ET.Element, container_value: EcucContainerValue):
        param_values = container_value.getParameterValues()
        if len(param_values) > 0:
            child_element  = ET.SubElement(element, "PARAMETER-VALUES")
            for param_value in param_values:
                if isinstance(param_value, EcucTextualParamValue):
                    self.setEcucTextualParamValue(child_element, param_value)
                elif isinstance(param_value, EcucNumericalParamValue):
                    self.setEcucNumericalParamValue(child_element, param_value)
                else:
                    raise NotImplementedError("Unsupported EcucParameterValue <%s>" % type(param_value))
                
    def writeEcucAbstractReferenceValue(self, element: ET.Element, value: EcucAbstractReferenceValue):
        self.setChildElementOptionalRefType(element, "DEFINITION-REF", value.getDefinitionRef())
        self.setAnnotations(element, value.getAnnotations())

    def setEcucReferenceValue(self, element: ET.Element, value = EcucReferenceValue()):
        child_element = ET.SubElement(element, "ECUC-REFERENCE-VALUE")
        self.writeEcucAbstractReferenceValue(child_element, value)
        self.setChildElementOptionalRefType(child_element, "VALUE-REF", value.getValueRef())
        return value
    
    def setAnyInstanceRef(self, element: ET.Element, key, instance_ref: AnyInstanceRef):
        if instance_ref is not None:
            child_element = ET.SubElement(element, key)
            self.setChildElementOptionalRefType(child_element, "BASE-REF", instance_ref.getBaseRef()) 
            self.setChildElementOptionalRefType(child_element, "CONTEXT-ELEMENT-REF", instance_ref.getContextElementRef())
            self.setChildElementOptionalRefType(child_element, "TARGET-REF", instance_ref.getTargetRef())
        return instance_ref
    
    def setEcucInstanceReferenceValue(self, element: ET.Element, value : EcucInstanceReferenceValue):
        child_element = ET.SubElement(element, "ECUC-INSTANCE-REFERENCE-VALUE")
        self.writeEcucAbstractReferenceValue(child_element, value)
        self.setAnyInstanceRef(child_element, "VALUE-IREF", value.getValueIRef())
        return value
    
    def writeEcucContainerValueReferenceValues(self, element: ET.Element, container_value: EcucContainerValue):
        reference_values = container_value.getReferenceValues()
        if len(reference_values) > 0:
            child_element  = ET.SubElement(element, "REFERENCE-VALUES")
            for reference_value in reference_values:
                if isinstance(reference_value, EcucReferenceValue):
                    self.setEcucReferenceValue(child_element, reference_value)
                elif isinstance(reference_value, EcucInstanceReferenceValue):
                    self.setEcucInstanceReferenceValue(child_element, reference_value)
                else:
                    raise NotImplementedError("Unsupported EcucParameterValue <%s>" % type(reference_value))

    def writeEcucContainValue(self, element: ET.Element, container_value: EcucContainerValue):
        self.logger.debug("EcucContainerValue %s" % container_value.short_name)
        child_element = ET.SubElement(element, "ECUC-CONTAINER-VALUE")
        self.setIdentifiable(child_element, container_value)
        self.setChildElementOptionalRefType(child_element, "DEFINITION-REF", container_value.getDefinitionRef())
        self.writeEcucContainerValueParameterValues(child_element, container_value)
        self.writeEcucContainerValueReferenceValues(child_element, container_value)
        self.writeEcucContainerValueSubContainers(child_element, container_value)

    def writeEcucModuleConfigurationValuesContainers(self, element: ET.Element, value: EcucModuleConfigurationValues):
        containers = value.getContainers()
        if len(containers) > 0:
            containers_tag = ET.SubElement(element, "CONTAINERS")
            for container in containers:
                if isinstance(container, EcucContainerValue):
                    self.writeEcucContainValue(containers_tag, container)
                else:
                    raise NotImplementedError("Unsupported Container %s" % type(container)) 

    def writeEcucModuleConfigurationValues(self, element: ET.Element, values: EcucModuleConfigurationValues):
        self.logger.debug("EcucModuleConfigurationValues %s" % values.short_name)
        child_element = ET.SubElement(element, "ECUC-MODULE-CONFIGURATION-VALUES")
        self.setIdentifiable(child_element, values)
        self.setChildElementOptionalRefType(child_element, "DEFINITION-REF", values.getDefinitionRef())
        self.setChildElementOptionalLiteral(child_element, "IMPLEMENTATION-CONFIG-VARIANT", values.getImplementationConfigVariant())
        self.setChildElementOptionalRefType(child_element, "MODULE-DESCRIPTION-REF", values.getModuleDescriptionRef())
        self.writeEcucModuleConfigurationValuesContainers(child_element, values)

    def writeISignalGroup(self, element: ET.Element, group: ISignalGroup):
        self.logger.debug("ISignalGroup %s" % group.short_name)
        child_element = ET.SubElement(element, "I-SIGNAL-GROUP")
        self.setIdentifiable(child_element, group)
        signal_refs = group.getISignalRefs()
        if len(signal_refs) > 0:
            signal_refs_tag = ET.SubElement(child_element, "I-SIGNAL-REFS")
            for signal_ref in signal_refs:
                self.setChildElementOptionalRefType(signal_refs_tag, "I-SIGNAL-REF", signal_ref)
        self.setChildElementOptionalRefType(child_element, "SYSTEM-SIGNAL-GROUP-REF", group.getSystemSignalGroupRef())

    def writeISignalIPduGroup(self, element: ET.Element, group: ISignalIPduGroup):
        self.logger.debug("ISignalIPduGroup %s" % group.short_name)
        child_element = ET.SubElement(element, "I-SIGNAL-I-PDU-GROUP")
        self.setIdentifiable(child_element, group)
        self.setChildElementOptionalLiteral(child_element, "COMMUNICATION-DIRECTION", group.getCommunicationDirection())
        self.setChildElementOptionalLiteral(child_element, "COMMUNICATION-MODE", group.getCommunicationMode())
        group_refs = group.getContainedISignalIPduGroupRefs()
        if len(group_refs) > 0:
            pdu_refs_tag = ET.SubElement(child_element, "CONTAINED-I-SIGNAL-I-PDU-GROUP-REFS")
            for pdu_ref in group_refs:
                self.setChildElementOptionalRefType(pdu_refs_tag, "CONTAINED-I-SIGNAL-I-PDU-GROUP-REF", pdu_ref)
        pdu_refs = group.getISignalIPduRefs()
        if len(pdu_refs) > 0:
            pdu_refs_tag = ET.SubElement(child_element, "I-SIGNAL-I-PDUS")
            for pdu_ref in pdu_refs:
                ref_conditional_tag = ET.SubElement(pdu_refs_tag, "I-SIGNAL-I-PDU-REF-CONDITIONAL")
                self.setChildElementOptionalRefType(ref_conditional_tag, "I-SIGNAL-I-PDU-REF", pdu_ref)

    def writeSystemSignal(self, element: ET.Element, signal: SystemSignal):
        self.logger.debug("SystemSignal %s" % signal.short_name)
        child_element = ET.SubElement(element, "SYSTEM-SIGNAL")
        self.setIdentifiable(child_element, signal)
        self.setChildElementOptionalBooleanValue(child_element, "DYNAMIC-LENGTH", signal.getDynamicLength())

    def writeISignalToPduMappings(self, element: ET.Element, parent: ISignalIPdu):
        mappings = parent.getISignalToPduMappings()
        if len(mappings) > 0:
            mappings_tag = ET.SubElement(element, "I-SIGNAL-TO-PDU-MAPPINGS")
            for mapping in mappings:
                child_element = ET.SubElement(mappings_tag, "I-SIGNAL-TO-I-PDU-MAPPING")
                self.setIdentifiable(child_element, mapping)
                self.setChildElementOptionalRefType(child_element, "I-SIGNAL-REF", mapping.getISignalRef())
                self.setChildElementOptionalRefType(child_element, "I-SIGNAL-GROUP-REF", mapping.getISignalGroupRef())
                self.setChildElementOptionalLiteral(child_element, "PACKING-BYTE-ORDER", mapping.getPackingByteOrder())
                self.setChildElementOptionalNumericalValue(child_element, "START-POSITION", mapping.getStartPosition())
                self.setChildElementOptionalLiteral(child_element, "TRANSFER-PROPERTY", mapping.getTransferProperty())
                self.setChildElementOptionalNumericalValue(child_element, "UPDATE-INDICATION-BIT-POSITION", mapping.getUpdateIndicationBitPosition())

    def writeISignalIPdu(self, element: ET.Element, i_pdu: ISignalIPdu):
        self.logger.debug("ISignalIPdu %s" % i_pdu.short_name)
        child_element = ET.SubElement(element, "I-SIGNAL-I-PDU")
        self.setIdentifiable(child_element, i_pdu)
        self.setChildElementOptionalNumericalValue(child_element, "LENGTH", i_pdu.getLength())
        self.writeISignalToPduMappings(child_element, i_pdu)
        self.setChildElementOptionalLiteral(child_element, "UNUSED-BIT-PATTERN", i_pdu.getUnusedBitPattern())

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
            self.setSwcBswMapping(element, ar_element)
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
        elif isinstance(ar_element, ServiceSwComponentType):
            self.writeServiceSwComponentType(element, ar_element)
        elif isinstance(ar_element, DataTypeMappingSet):
            self.writeDataTypeMappingSet(element, ar_element)
        elif isinstance(ar_element, ModeDeclarationGroup):
            self.writeModeDeclarationGroup(element, ar_element)
        elif isinstance(ar_element, ModeSwitchInterface):
            self.writeModeSwitchInterface(element, ar_element)
        elif isinstance(ar_element, SwcTiming):
            self.writeSwcTiming(element, ar_element)
        elif isinstance(ar_element, LinUnconditionalFrame):
            self.writeLinUnconditionalFrame(element, ar_element)
        elif isinstance(ar_element, NmConfig):
            self.writeNmConfig(element, ar_element)
        elif isinstance(ar_element, NmPdu):
            self.writeNmPdu(element, ar_element)
        elif isinstance(ar_element, NPdu):
            self.writeNPdu(element, ar_element)
        elif isinstance(ar_element, DcmIPdu):
            self.writeDcmIPdu(element, ar_element)
        elif isinstance(ar_element, SecuredIPdu):
            self.writeSecuredIPdu(element, ar_element)
        elif isinstance(ar_element, CanTpConfig):
            self.writeCanTpConfig(element, ar_element)
        elif isinstance(ar_element, LinCluster):
            self.writeLinCluster(element, ar_element)
        elif isinstance(ar_element, CanCluster):
            self.writeCanCluster(element, ar_element)
        elif isinstance(ar_element, CanFrame):
            self.writeCanFrame(element, ar_element)
        elif isinstance(ar_element, Gateway):
            self.writeGateway(element, ar_element)
        elif isinstance(ar_element, ISignal):
            self.writeISignal(element, ar_element)
        else:
            raise NotImplementedError("Unsupported Elements of ARPackage <%s>" % type(ar_element))
        
    def writeARPackages(self, element: ET.Element, pkgs: List[ARPackage]):
        if len(pkgs) > 0:
            pkgs_tag = ET.SubElement(element, "AR-PACKAGES")

            for pkg in pkgs:
                pkg_tag  = ET.SubElement(pkgs_tag, "AR-PACKAGE")
            
                self.setIdentifiable(pkg_tag, pkg)
                self.logger.debug("writeARPackage %s" % pkg.full_name)

                if pkg.getTotalElement() > 0:
                    elements_tag = ET.SubElement(pkg_tag, "ELEMENTS")

                    for ar_element in pkg.getElements():
                        if not isinstance(ar_element, ARPackage):
                            self.writeARPackageElement(elements_tag, ar_element)

                self.writeARPackages(pkg_tag, pkg.getARPackages())

    def save(self, filename, document: AUTOSAR):
        self.logger.info("Save %s ..." % filename)

        root = ET.Element("AUTOSAR", self.nsmap)
        root.attrib["xmlns:xsi"] = "http://www.w3.org/2001/XMLSchema-instance"
        root.attrib["xsi:schemaLocation"] = document.schema_location
        
        self.writeARPackages(root, document.getARPackages())

        self.saveToFile(filename, root)
        