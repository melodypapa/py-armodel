from typing import Dict, List

from ..M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import ARObject


class UUIDMgr:
    def __init__(self):
        self.uuid_object_mappings = {}          # type: Dict[str, List[ARObject]]

    def addObject(self, obj: ARObject):
        if obj.uuid is None:
            return
        if obj.uuid not in self.uuid_object_mappings:
            self.uuid_object_mappings[obj.uuid] = []
        
        uuid_obj_list = self.uuid_object_mappings[obj.uuid]
        uuid_obj_list.append(obj)

    def getObjects(self, uuid: str):
        result = []
        if uuid in self.uuid_object_mappings:
            result = self.uuid_object_mappings[uuid]
        return result
    
    def getDuplicateUUIDs(self):
        if len(self.uuid_object_mappings) > 0:
            return self.uuid_object_mappings.keys()
        else:
            return []
