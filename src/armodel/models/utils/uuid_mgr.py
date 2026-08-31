from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable import Identifiable


class UUIDMgr:
    """
    Manager for UUID-based object tracking and duplicate detection in the
    AUTOSAR model.
    """

    # UUIDMgr method parity checklist:
    # [ ] __init__                     [x] impl  [ ] docstring  [ ] test
    # [ ] addObject                    [x] impl  [ ] docstring  [ ] test
    # [ ] getObjects                   [x] impl  [ ] docstring  [ ] test
    # [ ] getDuplicateUUIDs            [x] impl  [ ] docstring  [ ] test

    def __init__(self):
        self.uuid_object_mappings = {}  # type: Dict[str, List[Identifiable]]

    def addObject(self, obj: Identifiable):
        # The uuid attribute (Table 4.4) is owned by Identifiable. Only objects
        # that derive from Identifiable and actually carry a uuid are tracked.
        uuid = obj.getUuid() if isinstance(obj, Identifiable) else None
        if uuid is None:
            return
        if uuid not in self.uuid_object_mappings:
            self.uuid_object_mappings[uuid] = []

        uuid_obj_list = self.uuid_object_mappings[uuid]
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
