from typing import Dict, List

from .GenericStructure.GeneralTemplateClasses.Identifiable import CollectableElement

from .GenericStructure.GeneralTemplateClasses.ARPackage import ARPackage
from .CommonStructure.implementation_data_types import ImplementationDataType

from .GenericStructure.GeneralTemplateClasses.Identifiable import Referrable

from ...datatype import ApplicationDataType, DataTypeMap, SwBaseType

class AbstractAUTOSAR(CollectableElement):
    def __init__(self):
        super().__init__()

        CollectableElement.__init__(self)

        self.schema_location = ""
        self._appl_impl_type_maps = {}
        self._impl_appl_type_maps = {}
        

        self._ar_packages = {}                  # type: Dict[str, ARPackage]
        self.short_name_mappings = {}           # type: Dict[str, str]

    def reload(self):
        pass

    @property
    def full_name(self):
        return ""

    def clear(self):
        self._ar_packages = {}
        self.elements = {}

    def getElement(self, short_name: str) -> Referrable:
        if (short_name in self._ar_packages):
            return self._ar_packages[short_name]
        return CollectableElement.getElement(self, short_name)

    def getARPackages(self) -> List[ARPackage]:
        #return list(filter(lambda e: isinstance(e, ARPackage), self.elements.values()))
        return list(sorted(self._ar_packages.values(), key= lambda a: a.short_name))

    def createARPackage(self, short_name: str) -> ARPackage:
        if (short_name not in self._ar_packages):
            ar_package = ARPackage(self, short_name)
            self._ar_packages[short_name] = ar_package
        return self._ar_packages[short_name]

    def find(self, referred_name: str) -> Referrable:
        short_name_list = referred_name.split("/")
        element = AUTOSAR.getInstance()
        for short_name in short_name_list:
            if (short_name == ""):
                continue
            element = element.getElement(short_name)
            if (element == None):
                return element
            #    raise ValueError("The %s of reference <%s> does not exist." % (short_name, referred_name))
        return element
    
    def findByShortName(self, short_name: str) -> Referrable:
        pass

    def getDataType(self, data_type: ImplementationDataType) -> ImplementationDataType:
        if (isinstance(data_type, ImplementationDataType) or isinstance(data_type, SwBaseType)):
            if (data_type.category == ImplementationDataType.CATEGORY_TYPE_REFERENCE):
                referred_type = self.find(data_type.swDataDefProps.implementationDataTypeRef.value)
                return self.getDataType(referred_type)
            if (data_type.category == ImplementationDataType.CATEGORY_DATA_REFERENCE):
                if (data_type.swDataDefProps.swPointerTargetProps.target_category == "VALUE"):
                    referred_type = self.find(data_type.swDataDefProps.swPointerTargetProps.sw_data_def_props.baseTypeRef.value)
                    return self.getDataType(referred_type)
            return data_type
        else:
            raise ValueError("%s is not ImplementationDataType." % data_type)
            
    def addDataTypeMap(self, data_type_map: DataTypeMap):
        if (data_type_map.application_data_type_ref is None) or (data_type_map.implementation_data_type_ref is None):
            return
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

    
class AUTOSAR (AbstractAUTOSAR):        
    __instance = None

    @staticmethod
    def getInstance():
        if (AUTOSAR.__instance == None):
            AUTOSAR()
        return AUTOSAR.__instance
    
    def new(self):
        self.clear()

    def __init__(self):
        if (AUTOSAR.__instance != None):
            raise Exception("The AUTOSAR is singleton!")
        
        AUTOSAR.__instance = self

        super().__init__()

class AUTOSARDoc(AbstractAUTOSAR):
    def __init__(self):
        super().__init__()
        
