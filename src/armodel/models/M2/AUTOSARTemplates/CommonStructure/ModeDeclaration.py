from typing import List
from ....M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import ARObject
from ....M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable import Identifiable
from ....M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import ARNumerical, PositiveInteger, RefType, TRefType


class ModeDeclarationGroupPrototypeMapping(ARObject):
    def __init__(self):
        super().__init__()

        self.firstModeGroupRef = None                           # type: RefType
        self.modeDeclarationMappingSetRef = None                # type: RefType
        self.secondModeGroupRef = None                          # type: RefType

    def getFirstModeGroupRef(self):
        return self.firstModeGroupRef

    def setFirstModeGroupRef(self, value):
        if value is not None:
            self.firstModeGroupRef = value
        return self

    def getModeDeclarationMappingSetRef(self):
        return self.modeDeclarationMappingSetRef

    def setModeDeclarationMappingSetRef(self, value):
        if value is not None:
            self.modeDeclarationMappingSetRef = value
        return self

    def getSecondModeGroupRef(self):
        return self.secondModeGroupRef

    def setSecondModeGroupRef(self, value):
        if value is not None:
            self.secondModeGroupRef = value
        return self


class ModeDeclaration(Identifiable):
    def __init__(self, parent: ARObject, short_name: str):
        super().__init__(parent, short_name)

        self.value = None                                               # type: ARNumerical

    def setValue(self, value):
        self.value = value
        return self

    def getValue(self) -> ARNumerical:
        return self.value


class ModeRequestTypeMap(ARObject):
    def __init__(self):
        super().__init__()

        self.implementationDataTypeRef = None               # type: RefType
        self.modeGroupRef = None                            # type: RefType

    def getImplementationDataTypeRef(self):
        return self.implementationDataTypeRef

    def setImplementationDataTypeRef(self, value):
        self.implementationDataTypeRef = value
        return self

    def getModeGroupRef(self):
        return self.modeGroupRef

    def setModeGroupRef(self, value):
        self.modeGroupRef = value
        return self


class ModeDeclarationGroup(Identifiable):
    def __init__(self, parent: ARObject, short_name: str):
        super().__init__(parent, short_name)

        self.initialModeRef = None                          # type: RefType
        self.modeDeclarations = []                          # type: ModeDeclaration
        self.modeManagerErrorBehavior = None                # type: ModeErrorBehavior
        self.modeTransition = None                          # type: ModeTransition
        self.modeUserErrorBehavior = None                   # type: ModeErrorBehavior
        self.onTransitionValue = None                       # type: PositiveInteger

    def createModeDeclaration(self, short_name: str) -> ModeDeclaration:
        if not self.IsElementExists(short_name):
            spec = ModeDeclaration(self, short_name)
            self.addElement(spec)
        return self.getElement(short_name, ModeDeclaration)

    def getModeDeclarations(self) -> List[ModeDeclaration]:
        return list(sorted(filter(lambda a: isinstance(a, ModeDeclaration), self.elements), key=lambda o: o.short_name))

    def setInitialModeRef(self, ref: RefType):
        self.initialModeRef = ref
        return self

    def getInitialModeRef(self) -> RefType:
        return self.initialModeRef

    def setOnTransitionValue(self, value):
        if isinstance(value, int):
            value = ARNumerical()
            value.setValue(value)
        self.onTransitionValue = value
        return self

    def getOnTransitionValue(self) -> ARNumerical:
        return self.onTransitionValue


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
