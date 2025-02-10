from typing import Dict, List


from ...M2.MSR.AsamHdo.SpecialData import Sdg
from ...M2.MSR.AsamHdo import AdminData
from ...M2.MSR.AsamHdo.BaseTypes import SwBaseType
from ...M2.MSR.Documentation.TextModel.BlockElements import DocumentationBlock
from ...M2.AUTOSARTemplates.CommonStructure.InternalBehavior import InternalBehavior
from ...M2.AUTOSARTemplates.CommonStructure.Implementation import Implementation
from ...M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import ARObject
from ...M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable import CollectableElement, Referrable
from ...M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ARPackage import ARPackage
from ...M2.AUTOSARTemplates.SWComponentTemplate.Datatype.Datatypes import ApplicationDataType, DataTypeMap
from ...M2.AUTOSARTemplates.SWComponentTemplate.Components import CompositionSwComponentType
from ...M2.AUTOSARTemplates.CommonStructure.ImplementationDataTypes import ImplementationDataType
from ...M2.AUTOSARTemplates.SystemTemplate import RootSwCompositionPrototype, System


class FileInfoComment(ARObject):
    def __init__(self):
        super().__init__()

        self.sdgs = []                                      # type: List[Sdg]

    def getSdgs(self):
        return self.sdgs

    def setSdgs(self, value):
        self.sdgs = value
        return self


class AbstractAUTOSAR(CollectableElement):
    def __init__(self):
        super().__init__()

        self.release_xsd_mappings = {
            "4.0.3": "AUTOSAR_4-0-3.xsd",
            "4.1.0": "AUTOSAR_4-1-0.xsd",
            "4.2.1": "AUTOSAR_4-2-1.xsd",
            "4.3.0": "AUTOSAR_00043.xsd",
            "4.3.1": "AUTOSAR_00045.xsd",
            "4.4.0": "AUTOSAR_00047.xsd",
            "R19-11": "AUTOSAR_00048.xsd",
            "R20-11": "AUTOSAR_00049.xsd",
            "R21-11": "AUTOSAR_00050.xsd",
            "R22-11": "AUTOSAR_00051.xsd",
            "R23-11": "AUTOSAR_00052.xsd",
            "R24-11": "AUTOSAR_00053.xsd",
        }

        self.clear()

    def getAdminData(self):
        return self.adminData

    def setAdminData(self, value):
        if value is not None:
            self.adminData = value
        return self
    
    def removeAdminData(self):
        self.adminData = None

    def getFileInfoComment(self):
        return self.fileInfoComment

    def setFileInfoComment(self, value):
        self.fileInfoComment = value
        return self

    def getIntroduction(self):
        return self.introduction

    def setIntroduction(self, value):
        self.introduction = value
        return self

    def reload(self):
        pass

    @property
    def full_name(self):
        return ""

    def clear(self):
        CollectableElement.__init__(self)

        self.schema_location = None
        self._appl_impl_type_maps = {}
        self._impl_appl_type_maps = {}

        self._behavior_impl_maps = {}                       # type: Dict[str, str]
        self._impl_behavior_maps = {}                       # type: Dict[str, str]

        self.uuid_objects = {}                              # type: Dict[str, ARObject]

        self.systems = {}                                   # type: Dict[str, System]
        self.compositionSwComponentTypes = {}               # type: Dict[str, CompositionSwComponentType]

        self.rootSwCompositionPrototype = None              # type: RootSwCompositionPrototype

        self.adminData = None                               # type: AdminData
        self.arPackages = {}                                # type: Dict[str, ARPackage]
        self.fileInfoComment = None                         # type: FileInfoComment
        self.introduction = None                            # type: DocumentationBlock

    def getElement(self, short_name: str) -> Referrable:
        if (short_name in self.arPackages):
            return self.arPackages[short_name]
        return CollectableElement.getElement(self, short_name)

    def getARPackages(self) -> List[ARPackage]:
        # return list(filter(lambda e: isinstance(e, ARPackage), self.elements.values()))
        return list(sorted(self.arPackages.values(), key=lambda a: a.short_name))

    def createARPackage(self, short_name: str) -> ARPackage:
        if (short_name not in self.arPackages):
            ar_package = ARPackage(self, short_name)
            self.arPackages[short_name] = ar_package
        return self.arPackages[short_name]

    def find(self, referred_name: str) -> Referrable:
        short_name_list = referred_name.split("/")
        element = AUTOSAR.getInstance()
        for short_name in short_name_list:
            if (short_name == ""):
                continue
            element = element.getElement(short_name)
            if (element is None):
                return element
            #    raise ValueError("The %s of reference <%s> does not exist." % (short_name, referred_name))
        return element
    
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
        if (data_type_map.applicationDataTypeRef is None) or (data_type_map.implementationDataTypeRef is None):
            return
        self._appl_impl_type_maps[data_type_map.applicationDataTypeRef.value] = data_type_map.implementationDataTypeRef.value
        self._impl_appl_type_maps[data_type_map.implementationDataTypeRef.value] = data_type_map.applicationDataTypeRef.value

    def convertToImplementationDataType(self, appl_data_type: str) -> ImplementationDataType:
        if (appl_data_type not in self._appl_impl_type_maps.keys()):
            raise IndexError("Invalid application data type <%s>" % appl_data_type)

        return self.find(self._appl_impl_type_maps[appl_data_type])

    def convertToApplicationDataType(self, impl_data_type: str) -> ApplicationDataType:
        if (impl_data_type not in self._impl_appl_type_maps.keys()):
            raise IndexError("Invalid Implementation data type <%s>" % impl_data_type)
        
        return self.find(self._impl_appl_type_maps[impl_data_type])
    
    def getRootSwCompositionPrototype(self):
        return self.rootSwCompositionPrototype

    def setRootSwCompositionPrototype(self, value):
        if value is not None:
            self.rootSwCompositionPrototype = value
        return self

    def addImplementationBehaviorMap(self, impl: str, behavior: str) -> Implementation:
        self._behavior_impl_maps[behavior] = impl
        self._impl_behavior_maps[impl] = behavior

    def getBehavior(self, impl_ref: str) -> InternalBehavior:
        if impl_ref in self._impl_behavior_maps:
            return self.find(self._impl_behavior_maps[impl_ref])
        return None

    def getImplementation(self, behavior_ref: str):
        if behavior_ref in self._behavior_impl_maps:
            return self.find(self._behavior_impl_maps[behavior_ref])
        return None
    
    def addSystem(self, system: System):
        short_name = system.getShortName()
        if short_name not in self.systems:
            self.systems[short_name] = system
    
    def getSystems(self) -> List[System]:
        return list(sorted(self.systems.values(), key=lambda a: a.getShortName()))
    
    def getCompositionSwComponentTypes(self):
        return self.compositionSwComponentTypes
    
    def getCompositionSwComponentType(self, short_name: str):
        return self.compositionSwComponentTypes[short_name]

    def addCompositionSwComponentType(self, sw_component_type: CompositionSwComponentType):
        if sw_component_type is not None:
            short_name = sw_component_type.getShortName()
            if short_name not in self.compositionSwComponentTypes:
                self.compositionSwComponentTypes[short_name] = sw_component_type
        return self
    
    def getARObjectByUUID(self, uuid: str):
        if uuid in self.uuid_objects:
            return self.uuid_objects[uuid]
        return None

    def addARObject(self, value: ARObject):
        if value is not None:
            self.uuid_objects[value.uuid] = value
        return self
    
    def setARRelease(self, release: str):
        if release not in self.release_xsd_mappings:
            raise "invalid AUTOSAR Release <%s>" % release
        self.schema_location = self.release_xsd_mappings[release]
        return self


class AUTOSAR (AbstractAUTOSAR):
    __instance = None

    @staticmethod
    def getInstance():
        if (AUTOSAR.__instance is None):
            AUTOSAR()
        return AUTOSAR.__instance
    
    def new(self):
        self.clear()

    def __init__(self):
        if (AUTOSAR.__instance is not None):
            raise Exception("The AUTOSAR is singleton!")
        
        AUTOSAR.__instance = self

        super().__init__()


class AUTOSARDoc(AbstractAUTOSAR):
    def __init__(self):
        super().__init__()
        
