import getopt
import logging
import sys
from typing import Optional

from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.BswModuleTemplate.BswBehavior import BswInternalBehavior, BswModuleEntity
from armodel.models.M2.AUTOSARTemplates.BswModuleTemplate.BswInterfaces import BswModuleEntry
from armodel.models.M2.AUTOSARTemplates.BswModuleTemplate.BswOverview import BswModuleDescription
from armodel.models.M2.AUTOSARTemplates.CommonStructure.ImplementationDataTypes import ImplementationDataType
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ARPackage import ARPackage
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable import Identifiable
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import RefType
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.Components import AtomicSwComponentType, PortPrototype, PPortPrototype, RPortPrototype, SwComponentType
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.Datatype.Datatypes import DataTypeMappingSet
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.PortInterface import ClientServerInterface, SenderReceiverInterface
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.SwcInternalBehavior import SwcInternalBehavior
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.SwcInternalBehavior.DataElements import VariableAccess
from armodel.parser import ARXMLParser


def _ref_value(ref: Optional[RefType]) -> Optional[str]:
    return ref.getValue() if ref is not None else None


def show_variable_access(indent: int, variable_access: VariableAccess):
    accessed_variable_ref = variable_access.getAccessedVariable()
    if accessed_variable_ref is not None:
        autosar_variable_in_impl_datatype = accessed_variable_ref.getAutosarVariableInImplDatatype()
        if autosar_variable_in_impl_datatype is not None:
            print("%s: %s" % (" " * indent, _ref_value(autosar_variable_in_impl_datatype.getPortPrototypeRef())))
            print("%s: %s" % (" " * indent, _ref_value(autosar_variable_in_impl_datatype.getTargetDataPrototypeRef())))


def show_port(indent: int, port_prototype: PortPrototype):
    if isinstance(port_prototype, RPortPrototype):
        print("%s-RPort: %s (%s)" % (" " * indent, port_prototype.short_name, _ref_value(port_prototype.getRequiredInterfaceTRef())))
        for client_com_spec in port_prototype.getClientComSpecs():
            print("%s    : %s (ClientComSpec)" % (" " * (indent + 2), _ref_value(client_com_spec.getOperationRef())))
        for receiver_com_spec in port_prototype.getNonqueuedReceiverComSpecs():
            print("%s    : %s (NonqueuedReceiverComSpec)" % (" " * (indent + 2), _ref_value(receiver_com_spec.getDataElementRef())))
    elif isinstance(port_prototype, PPortPrototype):
        print("%s-PPort: %s (%s)" % (" " * indent, port_prototype.short_name, _ref_value(port_prototype.getProvidedInterfaceTRef())))
        for sender_com_spec in port_prototype.getNonqueuedSenderComSpecs():
            print("%s    : %s (NonqueuedSenderComSpec)" % (" " * (indent + 2), _ref_value(sender_com_spec.getDataElementRef())))
    else:
        raise ValueError("Unsupported Port prototype")


def show_type(indent: int, data_type: ImplementationDataType):
    parent = data_type.parent
    parent_full_name = parent.full_name if isinstance(parent, Identifiable) else ""
    print("%s-Implementation Type: %s (%s)" % (" " * indent, data_type.short_name, parent_full_name))
    print("%s                    : %s" % (" " * indent, data_type.getCategory()))
    sw_data_def_props = data_type.getSwDataDefProps()
    if sw_data_def_props is not None:
        base_type_ref = sw_data_def_props.getBaseTypeRef()
        if base_type_ref is not None:
            print("%s                    : %s (%s)" % (" " * indent, base_type_ref.getValue(), base_type_ref.getDest()))

        implementation_data_type_ref = sw_data_def_props.getImplementationDataTypeRef()
        if implementation_data_type_ref is not None:
            print("%s                    : %s (%s)" % (" " * indent, implementation_data_type_ref.getValue(), implementation_data_type_ref.getDest()))


def show_data_type_mapping(indent: int, mapping_set: DataTypeMappingSet):
    print("%s- Data Mapping Set <%s>:" % (" " * indent, mapping_set.short_name))
    for mapping in mapping_set.getDataTypeMaps():
        print("%s- appl: %s" % (" " * (indent + 2), _ref_value(mapping.applicationDataTypeRef)))
        print("%s- impl: %s" % (" " * (indent + 4), _ref_value(mapping.implementationDataTypeRef)))


def show_behavior(indent: int, behavior: SwcInternalBehavior):
    print("%s-Behavior: %s" % (" " * indent, behavior.short_name))
    for runnable in behavior.getRunnableEntities():
        print("%s-Runnable: %s" % (" " * (indent + 2), runnable.short_name))
        print("%s-symbol: %s" % (" " * (indent + 4), runnable.symbol))
        for variable_access in runnable.getDataReceivePointByArguments():
            print("%s-drpa: %s" % (" " * (indent + 4), variable_access.short_name))
            show_variable_access(indent + 9, variable_access)
        for variable_access in runnable.getDataSendPoints():
            print("%s-dsp : %s" % (" " * (indent + 4), variable_access.short_name))
            show_variable_access(indent + 9, variable_access)
        for server_call_point in runnable.getServerCallPoints():
            print("%s-scp : %s" % (" " * (indent + 4), server_call_point.short_name))
            operation_iref = server_call_point.getOperationIRef()
            if operation_iref is not None:
                print("%s: %s" % (" " * (indent + 9), _ref_value(operation_iref.getContextRPortRef())))
                print("%s: %s" % (" " * (indent + 9), _ref_value(operation_iref.getTargetRequiredOperationRef())))
    for event in behavior.getOperationInvokedEvents():
        print("   - OperationInvokedEvent : %s" % event.short_name)
        print("                           : %s" % _ref_value(event.getStartOnEventRef()))
    for timing_event in behavior.getTimingEvents():
        period_ms = timing_event.periodMs
        print("")
        print("   - TimingEvent : %s (%d ms)" % (timing_event.short_name, period_ms if period_ms is not None else 0))
        print("                 : %s" % _ref_value(timing_event.getStartOnEventRef()))


def show_sw_component(indent: int, sw_component: SwComponentType):
    print("%s%s" % (" " * indent, sw_component.short_name))
    for r_prototype in sw_component.getRPortPrototypes():
        show_port(indent + 2, r_prototype)
    for p_prototype in sw_component.getPPortPrototypes():
        show_port(indent + 2, p_prototype)
    if isinstance(sw_component, AtomicSwComponentType):
        behavior = sw_component.getInternalBehavior()
        if behavior is not None:
            show_behavior(indent + 2, behavior)


def show_sender_receiver_interface(indent: int, sr_interface: SenderReceiverInterface):
    print("%s%s" % (" " * indent, sr_interface.short_name))
    for data_element in sr_interface.getDataElements():
        print("%sData Element:%s (%s) " % (" " * (indent + 2), data_element.short_name, _ref_value(data_element.getTypeTRef())))


def show_client_server_interface(indent: int, cs_interface: ClientServerInterface):
    print("%s%s" % (" " * indent, cs_interface.short_name))
    for operation in cs_interface.getOperations():
        print("%sOperation:%s" % (" " * (indent + 2), operation.short_name))
        for argument in operation.getArguments():
            print("%s         :%s (%s: %s)" % (" " * (indent + 2), argument.short_name, argument.direction, _ref_value(argument.getTypeTRef())))


def show_bsw_internal_behavior(indent: int, behavior: BswInternalBehavior):
    document = AUTOSAR.getInstance()

    print("%s-%s" % (" " * indent, behavior.short_name))

    for event in behavior.getBswModeSwitchEvents():
        print("%s-%s" % (" " * (indent + 2), event.short_name))

    for timing_event in behavior.getBswTimingEvents():
        print("%s-%s" % (" " * (indent + 2), timing_event.short_name))
        starts_on_event_path = _ref_value(timing_event.getStartsOnEventRef())
        print("%s-%s: %s" % (" " * (indent + 4), "StartsOnEventRef", starts_on_event_path))
        if starts_on_event_path is None:
            continue
        starts_on_event = document.find(starts_on_event_path)
        if not isinstance(starts_on_event, BswModuleEntity):
            continue
        print("%s-%s: %s" % (" " * (indent + 4), "StartsOnEvent", starts_on_event.short_name))
        implemented_entry_path = _ref_value(starts_on_event.getImplementedEntryRef())
        print("%s-%s: %s" % (" " * (indent + 4), "ImplementedEntryRef", implemented_entry_path))
        if implemented_entry_path is None:
            continue
        implemented_entry = document.find(implemented_entry_path)
        if not isinstance(implemented_entry, BswModuleEntry):
            continue
        print("%s-%s: %s" % (" " * (indent + 4), "ImplementedEntry", implemented_entry.short_name))
        print("%s-%s: %s" % (" " * (indent + 6), "Service Id", implemented_entry.getServiceId()))


def show_bsw_module_description(indent: int, description: BswModuleDescription):
    print("%s-%s" % (" " * indent, description.short_name))

    for behavior in description.getInternalBehaviors():
        show_bsw_internal_behavior(indent + 2, behavior)


def show_ar_package(indent: int, ar_package: ARPackage):
    print("%s-%s (Pkg)" % (" " * indent, ar_package.short_name))

    for sub_package in ar_package.getARPackages():
        show_ar_package(indent + 2, sub_package)
    # for data_type in ar_package.getImplementationDataTypes():
    #    show_type(indent + 2, data_type)
    # for mapping_set in ar_package.getDataTypeMappingSets():
    #    show_data_type_mapping(indent + 2, mapping_set)
    # for sw_component in ar_package.getAtomicSwComponents():
    #    show_sw_component(indent + 2, sw_component)
    # for sr_interface in ar_package.getSenderReceiverInterfaces():
    #    show_sender_receiver_interface(indent + 2, sr_interface)
    for cs_interface in ar_package.getClientServerInterfaces():
        show_client_server_interface(indent + 2, cs_interface)
    for child_pkg in ar_package.getARPackages():
        show_ar_package(indent + 2, child_pkg)
    for bsw_module_description in ar_package.getBswModuleDescriptions():
        show_bsw_module_description(indent + 2, bsw_module_description)


def _usage():
    print("Dump all the arxml data to screen")
    print("arxml-dump --arxml arg -h")
    print("   --arxml arg : the name of the arxml file")
    print("   -h          : show the help information")
    sys.exit(2)


def cli_main():
    try:
        opts, _ = getopt.getopt(sys.argv[1:], "h", ["arxml=", "help"])
    except getopt.GetoptError as err:
        # print help information and exit:
        print(str(err))  # will print something like "option -a not recognized"
        _usage()

    logging.basicConfig(format="[%(levelname)s] : %(message)s", level=logging.DEBUG)

    arxml_files = []
    for o, arg in opts:
        if o in ("--arxml"):
            arxml_files.append(arg)
        elif o in ("-h", "--help"):
            _usage()
        else:
            assert False, "unhandled option"

    if len(arxml_files) == 0:
        _usage()

    document = AUTOSAR().getInstance()
    parser = ARXMLParser()

    for arxml_file in arxml_files:
        parser.load(arxml_file, document)

    # obj = AUTOSAR.getInstance().find("/AUTOSAR_Platform/ImplementationDataTypes/uint8")
    # print(obj)
    for pkg in document.getARPackages():
        show_ar_package(0, pkg)
