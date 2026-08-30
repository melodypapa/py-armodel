from typing import TYPE_CHECKING, Optional

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import RefType

if TYPE_CHECKING:
    from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.SwcInternalBehavior.DataElements import (
        AutosarParameterRef,
        AutosarVariableRef,
    )


class SwVariableRefProxy(ARObject):
    """
    Proxy class for several kinds of references to a variable.
    """

    # SwVariableRefProxy method parity checklist:
    # Spec: AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf, Table 5.57, p.370
    # Spec verified: R23-11
    # Columns: impl / docstring / test / reader / writer   ([—] = no XML element)
    # [x] __init__                 [x] impl  [x] docstring  [x] test  [—] reader  [—] writer
    # [x] getAutosarVariable       [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] setAutosarVariable       [x] impl  [x] docstring  [x] test  [x] reader  [—] writer
    # [x] getMcDataInstanceVarRef [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] setMcDataInstanceVarRef [x] impl  [x] docstring  [x] test  [x] reader  [—] writer

    def __init__(self):
        super().__init__()

        # This represents the reference to a Variable in an Autosar system. Note that the target of the reference within AutosarVariableRef shall be typed by a primitive data type
        self.autosarVariable: Optional["AutosarVariableRef"] = None

        # This reference is used in the McSupport file to express the final instance of input values etc. It is not allowed to use this outside of an McDataInstance. The referenced mcDataInstance shall be originated from a VariableDataPrototype.
        self.mcDataInstanceVarRef: Optional[RefType] = None

    def getAutosarVariable(self) -> Optional["AutosarVariableRef"]:
        """
        This represents the reference to a Variable in an Autosar system. Note that the target of the reference within AutosarVariableRef shall be typed by a primitive data type.
        """
        return self.autosarVariable

    def setAutosarVariable(self, value: Optional["AutosarVariableRef"]) -> "SwVariableRefProxy":
        """
        This represents the reference to a Variable in an Autosar system. Note that the target of the reference within AutosarVariableRef shall be typed by a primitive data type. A None value is a no-op and does not overwrite an existing autosarVariable.
        """
        if value is not None:
            self.autosarVariable = value
        return self

    def getMcDataInstanceVarRef(self) -> Optional[RefType]:
        """
        This reference is used in the McSupport file to express the final instance of input values etc. It is not allowed to use this outside of an McDataInstance. The referenced mcDataInstance shall be originated from a VariableDataPrototype.
        """
        return self.mcDataInstanceVarRef

    def setMcDataInstanceVarRef(self, value: Optional[RefType]) -> "SwVariableRefProxy":
        """
        This reference is used in the McSupport file to express the final instance of input values etc. It is not allowed to use this outside of an McDataInstance. The referenced mcDataInstance shall be originated from a VariableDataPrototype. A None value is a no-op and does not overwrite an existing mcDataInstanceVarRef.
        """
        if value is not None:
            self.mcDataInstanceVarRef = value
        return self


class SwCalprmRefProxy(ARObject):
    """
    Wrapper class for different kinds of references to a calibration parameter.
    """

    # SwCalprmRefProxy method parity checklist:
    # Spec: AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf, Table 5.56, p.370
    # Spec verified: R23-11
    # Columns: impl / docstring / test / reader / writer   ([—] = no XML element)
    # [x] __init__                 [x] impl  [x] docstring  [x] test  [—] reader  [—] writer
    # [x] getArParameter           [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] setArParameter           [x] impl  [x] docstring  [x] test  [x] reader  [—] writer
    # [x] getMcDataInstanceRef     [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] setMcDataInstanceRef     [x] impl  [x] docstring  [x] test  [x] reader  [—] writer

    def __init__(self):
        super().__init__()

        # This represents a Parameter within AUTOSAR. Note that the Datatype of the referenced ParameterDataPrototype shall be an ApplicationDataType of category VALUE.
        self.arParameter: Optional["AutosarParameterRef"] = None

        # This reference is used in the McSupport file to express the final instance of group axis etc. It is not allowed to use this outside of an McDataInstance. The referenced mcDataInstance shall be originated from a ParameterDataPrototype.
        self.mcDataInstanceRef: Optional[RefType] = None

    def getArParameter(self) -> Optional["AutosarParameterRef"]:
        """
        This represents a Parameter within AUTOSAR. Note that the Datatype of the referenced ParameterDataPrototype shall be an ApplicationDataType of category VALUE.
        """
        return self.arParameter

    def setArParameter(self, value: Optional["AutosarParameterRef"]) -> "SwCalprmRefProxy":
        """
        This represents a Parameter within AUTOSAR. Note that the Datatype of the referenced ParameterDataPrototype shall be an ApplicationDataType of category VALUE. A None value is a no-op and does not overwrite an existing arParameter.
        """
        if value is not None:
            self.arParameter = value
        return self

    def getMcDataInstanceRef(self) -> Optional[RefType]:
        """
        This reference is used in the McSupport file to express the final instance of group axis etc. It is not allowed to use this outside of an McDataInstance. The referenced mcDataInstance shall be originated from a ParameterDataPrototype.
        """
        return self.mcDataInstanceRef

    def setMcDataInstanceRef(self, value: Optional[RefType]) -> "SwCalprmRefProxy":
        """
        This reference is used in the McSupport file to express the final instance of group axis etc. It is not allowed to use this outside of an McDataInstance. The referenced mcDataInstance shall be originated from a ParameterDataPrototype. A None value is a no-op and does not overwrite an existing mcDataInstanceRef.
        """
        if value is not None:
            self.mcDataInstanceRef = value
        return self
