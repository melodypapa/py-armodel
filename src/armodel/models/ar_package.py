from typing import List
from .general_structure import Identifiable, ARObject, Referrable, CollectableElement
from .port_interface import SenderReceiverInterface, ClientServerInterface
from .sw_component import SwComponentType, EcuAbstractionSwComponentType, AtomicSwComponentType, ApplicationSwComponentType, ServiceSwComponentType, CompositionSwComponentType
from .datatype import ImplementationDataType, ApplicationDataType, DataTypeMappingSet, DataTypeMap, SwBaseType, ApplicationPrimitiveDataType, ApplicationRecordDataType
from .m2_msr import CompuMethod

class ARPackage(Identifiable, CollectableElement):
    def __init__(self, parent: ARObject, short_name: str):
        Identifiable.__init__(self, parent, short_name)
        CollectableElement.__init__(self)

    def getARPackages(self):
        return list(filter(lambda e: isinstance(e, ARPackage), self.elements.values()))

    def createARPackage(self, short_name: str):
        if (short_name not in self.elements):
            ar_package = ARPackage(self, short_name)
            self.elements[short_name] = ar_package
        return self.elements[short_name]

    def createEcuAbstractionSwComponentType(self, short_name: str) -> EcuAbstractionSwComponentType:
        if (short_name not in self.elements):
            sw_component = EcuAbstractionSwComponentType(self, short_name)
            self.elements[short_name] = sw_component
        return self.elements[short_name]

    def createApplicationSwComponentType(self, short_name: str) -> ApplicationSwComponentType:
        if (short_name not in self.elements):
            sw_component = ApplicationSwComponentType(self, short_name)
            self.elements[short_name] = sw_component
        return self.elements[short_name]

    def createServiceSwComponentType(self, short_name: str) -> ServiceSwComponentType:
        if (short_name not in self.elements):
            sw_component = ServiceSwComponentType(self, short_name)
            self.elements[short_name] = sw_component
        return self.elements[short_name]

    def createCompositionSwComponentType(self, short_name: str) -> CompositionSwComponentType:
        if (short_name not in self.elements):
            sw_component = CompositionSwComponentType(self, short_name)
            self.elements[short_name] = sw_component
        return self.elements[short_name]

    def createSenderReceiverInterface(self, short_name: str) -> SenderReceiverInterface:
        if (short_name not in self.elements):
            sr_interface = SenderReceiverInterface(self, short_name)
            self.elements[short_name] = sr_interface
        return self.elements[short_name]

    def createClientServerInterface(self, short_name: str) -> ClientServerInterface:
        if (short_name not in self.elements):
            sr_interface = ClientServerInterface(self, short_name)
            self.elements[short_name] = sr_interface
        return self.elements[short_name]

    def createApplicationPrimitiveDataType(self, short_name: str) -> ApplicationPrimitiveDataType:
        if (short_name not in self.elements):
            data_type = ApplicationPrimitiveDataType(self, short_name)
            self.elements[short_name] = data_type
        return self.elements[short_name]

    def createApplicationRecordDataType(self, short_name: str) -> ApplicationPrimitiveDataType:
        if (short_name not in self.elements):
            data_type = ApplicationRecordDataType(self, short_name)
            self.elements[short_name] = data_type
        return self.elements[short_name]

    def createImplementationDataType(self, short_name: str) -> ImplementationDataType:
        if (short_name not in self.elements):
            data_type = ImplementationDataType(self, short_name)
            self.elements[short_name] = data_type
        return self.elements[short_name]

    def createSwBaseType(self, short_name: str) -> SwBaseType:
        if (short_name not in self.elements):
            base_type = SwBaseType(self, short_name)
            self.elements[short_name] = base_type
        return self.elements[short_name]

    def createDataTypeMappingSet(self, short_name: str) -> DataTypeMappingSet:
        if (short_name not in self.elements):
            mapping_set = DataTypeMappingSet(self, short_name)
            self.elements[short_name] = mapping_set
        return self.elements[short_name]

    def createCompuMethod(self, short_name: str) -> CompuMethod:
        if (short_name not in self.elements):
            compu_method = CompuMethod(self, short_name)
            self.elements[short_name] = compu_method
        return self.elements[short_name]

    def getApplicationPrimitiveDataTypes(self) -> List[ApplicationPrimitiveDataType]:
        return list(filter(lambda a: isinstance(a, ApplicationPrimitiveDataType), self.elements.values()))

    def getImplementationDataTypes(self) -> List[ImplementationDataType]:
        return list(filter(lambda a: isinstance(a, ImplementationDataType), self.elements.values()))

    def getSwBaseTypes(self) -> List[SwBaseType]:
        return list(filter(lambda a: isinstance(a, SwBaseType), self.elements.values()))

    def getSwComponentTypes(self) -> List[SwComponentType]:
        return list(filter(lambda a : isinstance(a, SwComponentType), self.elements.values()))

    def getAtomicSwComponentTypes(self) -> List[AtomicSwComponentType]:
        return list(filter(lambda a : isinstance(a, AtomicSwComponentType), self.elements.values()))

    def getCompositionSwComponentTypes(self) -> List[CompositionSwComponentType]:
        return list(filter(lambda a : isinstance(a, CompositionSwComponentType), self.elements.values()))

    def getSenderReceiverInterfaces(self) -> List[SenderReceiverInterface]:
        return list(filter(lambda a : isinstance(a, SenderReceiverInterface), self.elements.values()))

    def getClientServerInterfaces(self) -> List[ClientServerInterface]:
        return list(filter(lambda a : isinstance(a, ClientServerInterface), self.elements.values()))

    def getDataTypeMappingSets(self) -> List[DataTypeMappingSet]:
        return list(filter(lambda a: isinstance(a, DataTypeMappingSet), self.elements.values()))
    
    def getCompuMethods(self) -> List[CompuMethod]:
        return list(filter(lambda a: isinstance(a, CompuMethod), self.elements.values()))

class AUTOSAR (ARObject, CollectableElement):
    __instance = None

    @staticmethod
    def getInstance():
        if (AUTOSAR.__instance == None):
            AUTOSAR()
        return AUTOSAR.__instance

    def __init__(self):
        if (AUTOSAR.__instance != None):
            raise Exception("The AUTOSAR is singleton!")
        CollectableElement.__init__(self)

        self.version = "4.3.0"
        self._appl_impl_type_maps = {}
        self._impl_appl_type_maps = {}
        AUTOSAR.__instance = self

    @property
    def full_name(self):
        return ""

    def getARPackages(self):
        return list(filter(lambda e: isinstance(e, ARPackage), self.elements.values()))

    def createARPackage(self, short_name: str) -> ARPackage:
        if (short_name not in self.elements):
            ar_package = ARPackage(self, short_name)
            self.elements[short_name] = ar_package
        return self.elements[short_name]

    def find(self, referred_name: str) -> Referrable:
        short_name_list = referred_name.split("/")
        element = AUTOSAR.getInstance()
        for short_name in short_name_list:
            if (short_name == ""):
                continue
            element = element.getElement(short_name)
            #print("<%s>" % short_name)
            if (element == None):
                raise ValueError("The %s of reference <%s> does not exist." % (short_name, referred_name))
        return element

    def getDataType(self, data_type: ImplementationDataType) -> ImplementationDataType:
        if (isinstance(data_type, ImplementationDataType) or isinstance(data_type, SwBaseType)):
            if (data_type.category == ImplementationDataType.CATEGORY_TYPE_REFERENCE):
                referred_type = self.find(data_type.sw_data_def_props.implementation_data_type_ref.value)
                return self.getDataType(referred_type)
            if (data_type.category == ImplementationDataType.CATEGORY_DATA_REFERENCE):
                if (data_type.sw_data_def_props.sw_pointer_target_props.target_category == "VALUE"):
                    referred_type = self.find(data_type.sw_data_def_props.sw_pointer_target_props.sw_data_def_props.base_type_ref.value)
                    return self.getDataType(referred_type)
            return data_type
        else:
            raise ValueError("%s is not ImplementationDataType." % data_type)
            
    def addDataTypeMap(self, data_type_map: DataTypeMap):
        self._appl_impl_type_maps[data_type_map.application_data_type_ref.value] = data_type_map.implementation_data_type_ref.value
        self._impl_appl_type_maps[data_type_map.implementation_data_type_ref.value] = data_type_map.application_data_type_ref.value

    def convertToImplementationDataType(self, appl_data_type: str) -> ImplementationDataType:
        if (appl_data_type not in self._appl_impl_type_maps.keys()):
            raise IndexError("Invalid application data type <%s>" % appl_data_type)

        return self.find(self._appl_impl_type_maps[appl_data_type])

    def convertToApplicationDataType(self, impl_data_type: str) -> ApplicationDataType:
        if (impl_data_type not in self._impl_appl_type_maps.keys()):
            raise IndexError("Invalid Implementation data type <%s>" % impl_data_type)
        
        return self.find(self._impl_appl_type_maps[impl_data_type])
