import getopt
import sys

from ..models import AUTOSAR, ARPackage, AtomicSwComponentType, VariableAccess, SwComponentType, DataTypeMappingSet
from ..models import SwcInternalBehavior, ImplementationDataType
from ..models import PortPrototype, RPortPrototype, PPortPrototype
from ..models import SenderReceiverInterface, ClientServerInterface
from ..parser import ARXMLParser

def show_variable_access(indent:int, variable_access: VariableAccess):
    if (variable_access.accessed_variable_ref != None):
        accessed_variable_ref = variable_access.accessed_variable_ref
        if (accessed_variable_ref.autosar_variable_in_impl_datatype != None):
            autosar_variable_in_impl_datatype = accessed_variable_ref.autosar_variable_in_impl_datatype
            print("%s: %s" % (" " * indent, autosar_variable_in_impl_datatype.port_prototype.value))
            print("%s: %s" % (" " * indent, autosar_variable_in_impl_datatype.target_data_prototype.value))

def show_port(indent:int, port_portotype: PortPrototype):
    if (isinstance(port_portotype, RPortPrototype)):
        print("%s-RPort: %s (%s)" % (" " * indent, port_portotype.short_name, port_portotype.required_interface_tref.value))
        for client_com_spec in port_portotype.getClientComSpecs():
            print("%s    : %s (ClientComSpec)" % (" " * (indent + 2), client_com_spec.operation_ref.value))
        for com_spec in port_portotype.getNonqueuedReceiverComSpecs():
            print("%s    : %s (NonqueuedReceiverComSpec)" % (" " * (indent + 2), com_spec.data_element_ref.value))
    elif (isinstance(port_portotype, PPortPrototype)):
        print("%s-PPort: %s (%s)" % (" " * indent, port_portotype.short_name, port_portotype.provided_interface_tref.value))
        for com_spec in port_portotype.getNonqueuedSenderComSpecs():
            print("%s    : %s (NonqueuedSenderComSpec)" % (" " * (indent + 2), com_spec.data_element_ref.value))
    else:
        raise ValueError("Unsupported Port prototype")

def show_type(indent: int, data_type: ImplementationDataType):
    print("%s-Implementation Type: %s (%s)" % (" " * indent, data_type.short_name, data_type.parent.full_name))
    print("%s                    : %s" % (" " * indent, data_type.category))
    if (data_type.sw_data_def_props != None):
        if (data_type.sw_data_def_props.base_type_ref != None):
            base_type_ref = data_type.sw_data_def_props.base_type_ref
            print("%s                    : %s (%s)" % (" " * indent, base_type_ref.value, base_type_ref.dest))
            
        if (data_type.sw_data_def_props.implementation_data_type_ref != None):
            implementation_data_type_ref = data_type.sw_data_def_props.implementation_data_type_ref
            print("%s                    : %s (%s)" % (" " * indent, implementation_data_type_ref.value, implementation_data_type_ref.dest))

def show_data_type_mapping(indent: int, mapping_set: DataTypeMappingSet):
    print("%s- Data Mapping Set <%s>:" % (" " * indent, mapping_set.short_name))
    for mapping in mapping_set.getDataTypeMaps():
        print("%s- appl: %s" % (" " * (indent + 2), mapping.application_data_type_ref.value))
        print("%s- impl: %s" % (" " * (indent + 4), mapping.implementation_data_type_ref.value))

def show_behavior(indent:int, behavior: SwcInternalBehavior):
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
            print("%s-scp : %s" % (" " * (indent + 4), variable_access.short_name))
            if (server_call_point.operation_iref != None):
                print("%s: %s" % (" " * (indent + 9), server_call_point.operation_iref.conext_r_port.value))
                print("%s: %s" % (" " * (indent + 9), server_call_point.operation_iref.target_required_operation.value))
    for event in behavior.getOperationInvokedEvents():
        print("   - OperationInvokedEvent : %s" % event.short_name)
        print("                           : %s" % (event.start_on_event_ref.value))
    for event in behavior.getTimingEvents():
        print("")
        print("   - TimingEvent : %s (%d ms)" % (event.short_name, event.peroid_ms))
        print("                 : %s" % (event.start_on_event_ref.value))

def show_sw_component(indent: int, sw_component: SwComponentType):
    print("%s%s" % (" " * indent, sw_component.short_name))
    for prototype in sw_component.getRPortPrototypes():
        show_port(indent + 2, prototype)
    for prototype in sw_component.getPPortPrototypes():
        show_port(indent + 2, prototype)
    show_behavior(indent + 2, sw_component.internal_behavior) 

def show_sender_receiver_interface(indent: int, sr_interface: SenderReceiverInterface):
    print("%s%s" % (" " * indent, sr_interface.short_name))
    for data_element in sr_interface.getDataElements():
        print("%sData Element:%s (%s) " % (" " * (indent + 2), data_element.short_name, data_element.type_ref.value))

def show_client_server_interface(indent: int, cs_interface: ClientServerInterface):
    print("%s%s" % (" " * indent, cs_interface.short_name))
    for operation in cs_interface.getOperations():
        print("%sOperation:%s" % (" " * (indent + 2), operation.short_name))
        for argument in operation.getArgumentDataPrototypes():
            print("%s         :%s (%s: %s)" % (" " * (indent + 2), argument.short_name, 
                argument.direction, argument.type_tref.value))

def show_ar_package(indent: int, ar_package: ARPackage):
    print("%s-%s (Pkg)" % (" " * indent, ar_package.short_name))
     
    #for data_type in ar_package.getImplementationDataTypes():
    #    show_type(indent + 2, data_type)
    #for mapping_set in ar_package.getDataTypeMappingSets():
    #    show_data_type_mapping(indent + 2, mapping_set)
    #for sw_component in ar_package.getAtomicSwComponents():
    #    show_sw_component(indent + 2, sw_component)
    #for sr_interface in ar_package.getSenderReceiverInterfaces():
    #    show_sender_receiver_interface(indent + 2, sr_interface)
    for cs_interface in ar_package.getClientServerInterfaces():
        show_client_server_interface(indent + 2, cs_interface)
    for child_pkg in ar_package.getARPackages():
        show_ar_package(indent + 2, child_pkg)

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
    
    arxml_files = []
    for o, arg in opts:
        if o in ("--arxml"):
            arxml_files.append(arg)
        elif o in ("-h", "--help"):
            _usage()
        else:
            assert False, "unhandled option"

    if (len(arxml_files) == 0):
        _usage()

    document = AUTOSAR().getInstance()
    parser = ARXMLParser()
    
    for arxml_file in arxml_files:
        parser.load(arxml_file, document)

    #obj = AUTOSAR.getInstance().find("/AUTOSAR_Platform/ImplementationDataTypes/uint8")
    #print(obj)
    for pkg in document.getARPackages():
        show_ar_package(0, pkg)