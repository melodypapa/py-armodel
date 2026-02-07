from typing import Dict, List, Union

from armodel.v2.models.M2.AUTOSARTemplates.BswModuleTemplate.BswBehavior import (
    BswCalledEntity,
    BswSchedulableEntity,
)
from armodel.v2.models.M2.AUTOSARTemplates.BswModuleTemplate.BswInterfaces import (
    BswModuleEntry,
)
from armodel.v2.models.M2.AUTOSARTemplates.CommonStructure.Implementation import (
    Implementation,
)
from armodel.v2.models.M2.AUTOSARTemplates.CommonStructure.ImplementationDataTypes import (
    ImplementationDataType,
)
from armodel.v2.models.M2.AUTOSARTemplates.CommonStructure.InternalBehavior import (
    InternalBehavior,
)
from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import (
    ARObject,
)
from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ARPackage import (
    ARPackage,
)
from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ElementCollection import (
    CollectableElement,
)
from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable import (
    Referrable,
)
from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    RefType,
)
from armodel.v2.models.M2.AUTOSARTemplates.SWComponentTemplate.Components import (
    AtomicSwComponentType,
    PortPrototype,
)
from armodel.v2.models.M2.AUTOSARTemplates.SWComponentTemplate.Composition import (
    CompositionSwComponentType,
)
from armodel.v2.models.M2.AUTOSARTemplates.SWComponentTemplate.Datatype.DataPrototypes import (
    VariableDataPrototype,
)
from armodel.v2.models.M2.AUTOSARTemplates.SWComponentTemplate.Datatype.Datatypes import (
    ApplicationDataType,
    DataTypeMap,
)
from armodel.v2.models.M2.AUTOSARTemplates.SWComponentTemplate.SwcInternalBehavior import (
    RunnableEntity,
)
from armodel.v2.models.M2.AUTOSARTemplates.SystemTemplate import (
    RootSwCompositionPrototype as RootSwCompositionPrototype,
)
from armodel.v2.models.M2.AUTOSARTemplates.SystemTemplate import System
from armodel.v2.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore.CoreCommunication import (
    SystemSignal,
    SystemSignalGroup,
)
from armodel.v2.models.M2.MSR.AsamHdo.AdminData import AdminData
from armodel.v2.models.M2.MSR.AsamHdo.BaseTypes import SwBaseType
from armodel.v2.models.M2.MSR.AsamHdo.Sdg import Sdg
from armodel.v2.models.M2.MSR.Documentation.TextModel.BlockElements import (
    DocumentationBlock as DocumentationBlock,
)
from armodel.v2.models.utils.uuid_mgr import UUIDMgr


class FileInfoComment(ARObject):

    def __init__(self) -> None:
        super().__init__()

        self.sdgs: List[Sdg] = []

    def getSdgs(self):
        return self.sdgs

    def setSdgs(self, value):
        self.sdgs = value
        return self


class AbstractAUTOSAR(CollectableElement):
    def __init__(self) -> None:
        super().__init__()

        self.release_xsd_mappings = {
            "4.0.3": "AUTOSAR_4-0-3.xsd",
            "4.1.0": "AUTOSAR_4-1-0.xsd",
            "4.1.1": "AUTOSAR_4-1-1.xsd",
            "4.1.2": "AUTOSAR_4-1-2.xsd",
            "4.1.3": "AUTOSAR_4-1-3.xsd",
            "4.2.1": "AUTOSAR_4-2-1.xsd",
            "4.2.2": "AUTOSAR_4-2-2.xsd",
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

    def getAdminData(self) -> Union[AdminData, None]:
        return self.adminData

    def setAdminData(self, value: Union[AdminData, None]) -> "AbstractAUTOSAR":
        if value is not None:
            self.adminData = value
        return self

    def removeAdminData(self) -> None:
        self.adminData = None

    def getFileInfoComment(self) -> Union[FileInfoComment, None]:
        return self.fileInfoComment

    def setFileInfoComment(self, value: Union[FileInfoComment, None]) -> "AbstractAUTOSAR":
        self.fileInfoComment = value
        return self

    def getIntroduction(self) -> Union[DocumentationBlock, None]:
        return self.introduction

    def setIntroduction(self, value: Union[DocumentationBlock, None]) -> "AbstractAUTOSAR":
        self.introduction = value
        return self

    def reload(self) -> None:
        pass

    @property
    def full_name(self) -> str:
        return ""

    def clear(self) -> None:
        CollectableElement.__init__(self)

        self.schema_location: Union[str, None] = None
        self._appl_impl_type_maps: Dict[str, str] = {}
        self._impl_appl_type_maps: Dict[str, str] = {}

        self._behavior_impl_maps = {}                       # type: Dict[str, str]
        self._impl_behavior_maps = {}                       # type: Dict[str, str]

        self.uuid_mgr = UUIDMgr()

        self.systems: Dict[str, System] = {}
        self.compositionSwComponentTypes: Dict[str, CompositionSwComponentType] = {}

        self.rootSwCompositionPrototype: Union[RootSwCompositionPrototype, None] = None

        self.arPackages: Dict[str, ARPackage] = {}

    def getElement(self, short_name: str) -> Union[Referrable, None]:
        if (short_name in self.arPackages):
            return self.arPackages[short_name]
        return CollectableElement.getElement(self, short_name)

    def getARPackages(self) -> List[ARPackage]:
        return sorted(self.arPackages.values(), key=lambda a: a.short_name)

    def createARPackage(self, short_name: str) -> ARPackage:
        if (short_name not in self.arPackages):
            ar_package = ARPackage(self, short_name)
            self.arPackages[short_name] = ar_package
        return self.arPackages[short_name]

    def find(self, referred: Union[str, RefType]) -> Union[Referrable, None]:
        if isinstance(referred, RefType):
            referred_name = referred.getValue()
            referred_type = referred.getDest()
        else:
            referred_name = referred
            referred_type = None

        short_name_list = referred_name.split("/")
        element = AUTOSAR.getInstance()
        for short_name in short_name_list:
            if (short_name == ""):
                continue
            element = element.getElement(short_name)
            if (element is None):
                return element

        # validate the dest
        if referred_type is not None and referred_type != "":
            base_type = self.getDestType(element)
            if base_type != referred_type:
                raise ValueError("The type does not matched of <%s> (Dest: %s, Actual: %s)" % (referred_name, referred_type, base_type))

        return element

    def getDestType(self, type: Union[Referrable, None]) -> Union[str, None]:
        if type is None:
            return None
        if isinstance(type, ImplementationDataType):
            return "IMPLEMENTATION-DATA-TYPE"
        elif isinstance(type, ApplicationDataType):
            return "APPLICATION-DATA-TYPE"
        elif isinstance(type, AtomicSwComponentType):
            return "ATOMIC-SW-COMPONENT-TYPE"
        elif isinstance(type, CompositionSwComponentType):
            return "COMPOSITION-SW-COMPONENT-TYPE"
        elif isinstance(type, SystemSignal):
            return "SYSTEM-SIGNAL"
        elif isinstance(type, SystemSignalGroup):
            return "SYSTEM-SIGNAL-GROUP"
        elif isinstance(type, RunnableEntity):
            return "RUNNABLE-ENTITY"
        elif isinstance(type, BswSchedulableEntity):
            return "BSW-SCHEDULABLE-ENTITY"
        elif isinstance(type, BswModuleEntry):
            return "BSW-MODULE-ENTRY"
        elif isinstance(type, BswCalledEntity):
            return "BSW-CALLED-ENTITY"

        raise NotImplementedError("The type <%s> is not implemented for getDestType method" % type.__class__.__name__)

    def findAtomicSwComponentType(self, referred: str) -> Union[AtomicSwComponentType, Referrable]:
        return self.find(referred)

    def findSystemSignal(self, referred: str) -> Union[SystemSignal, Referrable]:
        return self.find(referred)

    def findSystemSignalGroup(self, referred: str) -> Union[SystemSignalGroup, Referrable]:
        return self.find(referred)

    def findPort(self, referred: str) -> Union[PortPrototype, Referrable]:
        return self.find(referred)

    def findVariableDataPrototype(self, referred: str) -> Union[VariableDataPrototype, Referrable]:
        return self.find(referred)

    def findImplementationDataType(self, referred: str) -> Union[ImplementationDataType, Referrable]:
        return self.find(referred)

    def getDataType(self, data_type: ImplementationDataType) -> ImplementationDataType:
        if (isinstance(data_type, (ImplementationDataType, SwBaseType))):
            if (data_type.category == ImplementationDataType.CATEGORY_TYPE_REFERENCE and
                data_type.swDataDefProps is not None and
                data_type.swDataDefProps.implementationDataTypeRef is not None):
                referred_type = self.find(data_type.swDataDefProps.implementationDataTypeRef.value)
                return self.getDataType(referred_type)
            if (data_type.category == ImplementationDataType.CATEGORY_DATA_REFERENCE and
                data_type.swDataDefProps is not None and
                data_type.swDataDefProps.swPointerTargetProps is not None and
                data_type.swDataDefProps.swPointerTargetProps.getTargetCategory() == "VALUE" and
                data_type.swDataDefProps.swPointerTargetProps.getSwDataDefProps() is not None):
                referred_type = self.find(data_type.swDataDefProps.swPointerTargetProps.getSwDataDefProps().getBaseTypeRef())
                return self.getDataType(referred_type)
            return data_type
        else:
            raise ValueError("%s is not ImplementationDataType." % data_type)

    def addDataTypeMap(self, data_type_map: DataTypeMap) -> "AbstractAUTOSAR":
        if (data_type_map.applicationDataTypeRef is None) or (data_type_map.implementationDataTypeRef is None):
            return self
        self._appl_impl_type_maps[data_type_map.applicationDataTypeRef.value] = data_type_map.implementationDataTypeRef.value
        self._impl_appl_type_maps[data_type_map.implementationDataTypeRef.value] = data_type_map.applicationDataTypeRef.value
        return self

    def convertToImplementationDataType(self, appl_data_type: str) -> Union[ImplementationDataType, Referrable]:
        if (appl_data_type not in self._appl_impl_type_maps):
            raise IndexError("Invalid application data type <%s>" % appl_data_type)

        return self.find(self._appl_impl_type_maps[appl_data_type])

    def convertToApplicationDataType(self, impl_data_type: str) -> Union[ApplicationDataType, Referrable]:
        if (impl_data_type not in self._impl_appl_type_maps):
            raise IndexError("Invalid Implementation data type <%s>" % impl_data_type)

        return self.find(self._impl_appl_type_maps[impl_data_type])

    def getRootSwCompositionPrototype(self) -> Union["RootSwCompositionPrototype", None]:
        return self.rootSwCompositionPrototype

    def setRootSwCompositionPrototype(self, value: "RootSwCompositionPrototype") -> "AbstractAUTOSAR":
        if value is not None:
            if self.rootSwCompositionPrototype is not None:
                if value.getShortName() != self.rootSwCompositionPrototype.getShortName():
                    raise ValueError("RootSwCompositionPrototype already set to <%s>, cannot set to <%s>."
                                     % (self.rootSwCompositionPrototype.getShortName(), value.getShortName()))
            else:
                self.rootSwCompositionPrototype = value
        return self

    def addImplementationBehaviorMap(self, impl: str, behavior: str) -> "AbstractAUTOSAR":
        self._behavior_impl_maps[behavior] = impl
        self._impl_behavior_maps[impl] = behavior
        return self

    def getBehavior(self, impl_ref: str) -> Union[InternalBehavior, Referrable, None]:
        if impl_ref in self._impl_behavior_maps:
            return self.find(self._impl_behavior_maps[impl_ref])
        return None

    def getImplementation(self, behavior_ref: str) -> Union[Implementation, Referrable, None]:
        if behavior_ref in self._behavior_impl_maps:
            return self.find(self._behavior_impl_maps[behavior_ref])
        return None

    def addSystem(self, system: System) -> "AbstractAUTOSAR":
        short_name = system.getShortName()
        if short_name not in self.systems:
            self.systems[short_name] = system
        return self

    def getSystems(self) -> List[System]:
        return sorted(self.systems.values(), key=lambda a: a.getShortName())

    def getCompositionSwComponentTypes(self) -> Dict[str, CompositionSwComponentType]:
        return self.compositionSwComponentTypes

    def getCompositionSwComponentType(self, short_name: str) -> Union[CompositionSwComponentType, None]:
        return self.compositionSwComponentTypes.get(short_name)

    def addCompositionSwComponentType(self, sw_component_type: CompositionSwComponentType) -> "AbstractAUTOSAR":
        if sw_component_type is not None:
            short_name = sw_component_type.getShortName()
            if short_name not in self.compositionSwComponentTypes:
                self.compositionSwComponentTypes[short_name] = sw_component_type
        return self

    def getARObjectByUUID(self, uuid: str) -> List[ARObject]:
        return self.uuid_mgr.getObjects(uuid)

    def addARObject(self, value: ARObject) -> "AbstractAUTOSAR":
        if value is not None:
            self.uuid_mgr.addObject(value)
        return self

    def getDuplicateUUIDs(self) -> List[str]:
        return self.uuid_mgr.getDuplicateUUIDs()

    def setARRelease(self, release: str) -> "AbstractAUTOSAR":
        if release not in self.release_xsd_mappings:
            raise ValueError("invalid AUTOSAR Release <%s>" % release)
        self.schema_location = "http://autosar.org/schema/r4.0 %s" % self.release_xsd_mappings[release]
        return self


class AUTOSAR (AbstractAUTOSAR):
    __instance = None

    @staticmethod
    def getInstance() -> "AUTOSAR":
        if (AUTOSAR.__instance is None):
            AUTOSAR()
        return AUTOSAR.__instance

    def new(self) -> "AUTOSAR":
        self.clear()
        return self

    def __init__(self) -> None:
        if (AUTOSAR.__instance is not None):
            raise Exception("The AUTOSAR is singleton!")

        AUTOSAR.__instance = self

        super().__init__()


class AUTOSARDoc(AbstractAUTOSAR):
    def __init__(self) -> None:
        super().__init__()


__all__ = [
    'AbstractAUTOSAR',
    'AUTOSAR',
    'AUTOSARDoc',
    'FileInfoComment',
]
