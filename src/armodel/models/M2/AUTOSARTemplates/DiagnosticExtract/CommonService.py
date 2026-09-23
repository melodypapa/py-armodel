from abc import ABC
from typing import Optional

from armodel.models.M2.AUTOSARTemplates.DiagnosticExtract.CommonDiagnostics import DiagnosticCommonElement
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import RefType


class DiagnosticServiceInstance(DiagnosticCommonElement, ABC):
    """This represents a concrete instance of a diagnostic service."""

    # DiagnosticServiceInstance method parity checklist:
    # Spec: AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf, Table 4.26, p.70
    # Columns: impl / docstring / test / reader / writer / release   ([—] = no XML element)
    # [x] __init__                [x] impl  [x] docstring  [x] test  [—] reader  [—] writer  R23-11
    # [x] setAccessPermissionRef  [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getAccessPermissionRef  [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setServiceClassRef      [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getServiceClassRef      [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11

    def __init__(self, parent: ARObject, short_name: str):
        if type(self) is DiagnosticServiceInstance:
            raise TypeError("DiagnosticServiceInstance is an abstract class.")
        super().__init__(parent, short_name)

        # This represents the collection of DiagnosticAccessPermissions that allow for the execution of the referencing DiagnosticServiceInstance..
        self.accessPermissionRef: Optional[RefType] = None

        # This represents the corresponding "class", i.e. this meta-class provides properties that are shared among all instances of applicable sub-classes of DiagnosticServiceInstance. The subclasses that affected by this pattern implement references to the applicable "class"-role that substantiate this abstract reference. Stereotypes: atpAbstract
        self.serviceClassRef: Optional[RefType] = None

    def getAccessPermissionRef(self) -> Optional[RefType]:
        """
        This represents the collection of DiagnosticAccessPermissions that allow for the execution of the referencing DiagnosticServiceInstance..
        """
        return self.accessPermissionRef

    def setAccessPermissionRef(self, value: Optional[RefType]):
        """
        This represents the collection of DiagnosticAccessPermissions that allow for the execution of the referencing DiagnosticServiceInstance..

        A None value is a no-op and does not overwrite an existing accessPermissionRef.
        """
        if value is not None:
            self.accessPermissionRef = value
        return self

    def getServiceClassRef(self) -> Optional[RefType]:
        """
        This represents the corresponding "class", i.e. this meta-class provides properties that are shared among all instances of applicable sub-classes of DiagnosticServiceInstance. The subclasses that affected by this pattern implement references to the applicable "class"-role that substantiate this abstract reference. Stereotypes: atpAbstract
        """
        return self.serviceClassRef

    def setServiceClassRef(self, value: Optional[RefType]):
        """
        This represents the corresponding "class", i.e. this meta-class provides properties that are shared among all instances of applicable sub-classes of DiagnosticServiceInstance. The subclasses that affected by this pattern implement references to the applicable "class"-role that substantiate this abstract reference. Stereotypes: atpAbstract

        A None value is a no-op and does not overwrite an existing serviceClassRef.
        """
        if value is not None:
            self.serviceClassRef = value
        return self


class DiagnosticServiceClass(DiagnosticCommonElement, ABC):
    """This meta-class provides the ability to define common properties that are shared among all instances of sub-classes of DiagnosticServiceInstance."""

    # DiagnosticServiceClass method parity checklist:
    # Spec: AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf, Table 4.25, p.69
    # Columns: impl / docstring / test / reader / writer / release   ([—] = no XML element)
    # [x] __init__  [x] impl  [x] docstring  [x] test  [—] reader  [—] writer  R23-11

    def __init__(self, parent: ARObject, short_name: str):
        if type(self) is DiagnosticServiceClass:
            raise TypeError("DiagnosticServiceClass is an abstract class.")
        super().__init__(parent, short_name)
