
from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import (
    ARObject,
)


class UUIDMgr:
    def __init__(self) -> None:
        self.uuid_object_mappings: dict[str, list[ARObject]] = {}

    def addObject(self, obj: ARObject) -> None:
        if obj.uuid is None:
            return
        if obj.uuid not in self.uuid_object_mappings:
            self.uuid_object_mappings[obj.uuid] = []

        uuid_obj_list = self.uuid_object_mappings[obj.uuid]
        uuid_obj_list.append(obj)

    def getObjects(self, uuid: str) -> list[ARObject]:
        result = []
        if uuid in self.uuid_object_mappings:
            result = self.uuid_object_mappings[uuid]
        return result

    def getDuplicateUUIDs(self) -> list[str]:
        if len(self.uuid_object_mappings) > 0:
            return list(self.uuid_object_mappings.keys())
        else:
            return []
