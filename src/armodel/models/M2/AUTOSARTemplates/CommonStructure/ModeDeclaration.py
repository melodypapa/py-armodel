from typing import List
from ....M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import ARObject
from ....M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable import Identifiable
from ....M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import ARNumerical, RefType, TRefType

class ModeDeclaration(Identifiable):
    def __init__(self, parent: ARObject, short_name: str):
        super().__init__(parent, short_name)

        self.value = None                           # type: ARNumerical

    def setValue(self, value):
        self.value = value
        return self

    def getValue(self) -> ARNumerical:
        return self.value


class ModeRequestTypeMap(ARObject):
    def __init__(self):
        super().__init__()

        self.implementation_data_type_ref = None           # type: RefType
        self.mode_group_ref = None                        # type: RefType


class ModeDeclarationGroup(Identifiable):
    def __init__(self, parent: ARObject, short_name: str):
        super().__init__(parent, short_name)

        self._initial_mode_ref = None                      # type: RefType
        self._on_transition_value = None                   # type: ARNumerical

    def createModeDeclaration(self, short_name: str) -> ModeDeclaration:
        if (short_name not in self.elements):
            spec = ModeDeclaration(self, short_name)
            self.elements[short_name] = spec
        return self.elements[short_name]

    def getModeDeclarations(self) -> List[ModeDeclaration]:
        return list(sorted(filter(lambda a: isinstance(a, ModeDeclaration), self.elements.values()), key= lambda o:o.short_name))

    def setInitialModeRef(self, ref: RefType):
        self._initial_mode_ref = ref
        return self

    def getInitialModeRef(self) -> RefType:
        return self._initial_mode_ref

    def setOnTransitionValue(self, value):
        if isinstance(value, int):
            value = ARNumerical()
            value.setValue(value)
        self._on_transition_value = value
        return self

    def getOnTransitionValue(self) -> ARNumerical:
        return self._on_transition_value


class ModeDeclarationGroupPrototype(Identifiable):

    """
    The ModeDeclarationGroupPrototype specifies a set of Modes (ModeDeclarationGroup) which is provided or required in the given context.
    """

    def __init__(self, parent: ARObject, short_name: str):
        super().__init__(parent, short_name)

        self._swCalibrationAccess = None        # type: str
        self.typeTRef = None                    # type: TRefType

    @property
    def sw_calibration_access(self):
        return self._swCalibrationAccess

    @sw_calibration_access.setter
    def sw_calibration_access(self, value):
        if (value not in ("notAccessible", "readOnly", "readWrite")):
            raise ValueError("Invalid SwCalibrationAccess <%s> of ModeDeclarationGroupPrototype <%s>" % (value, self.short_name))
        self._swCalibrationAccess = value

    def getSwCalibrationAccess(self):
        return self.swCalibrationAccess

    def setSwCalibrationAccess(self, value):
        self.swCalibrationAccess = value
        return self

    def getTypeTRef(self):
        return self.typeTRef

    def setTypeTRef(self, value):
        self.typeTRef = value
        return self