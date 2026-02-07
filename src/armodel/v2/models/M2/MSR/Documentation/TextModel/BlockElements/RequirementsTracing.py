from typing import TYPE_CHECKING, List, Union

from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.DocumentationOnM1 import (
    StandardNameEnum,
)
from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import (
    ARObject,
)
from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    String,
)

if TYPE_CHECKING:
    from armodel.v2.models.M2.MSR.Documentation.TextModel.BlockElements import (
        DocumentationBlock,
    )
    from armodel.v2.models.M2.AUTOSARTemplates.CommonStructure.Timing.Traceable import (
        Traceable,
    )


def _get_traceable_base():
    """Lazy import of Traceable to avoid circular import."""
    from armodel.v2.models.M2.AUTOSARTemplates.CommonStructure.Timing.Traceable import (
        Traceable,
    )
    return Traceable


class StructuredReq(ARObject):
    def __init__(self) -> None:

        super().__init__()

        self.date: Union[String, None] = None
        self.issuedBy: Union[String, None] = None
        self.type: Union[String, None] = None
        self.importance: Union[String, None] = None
        self.description: Union["DocumentationBlock", None] = None
        self.rationale: Union["DocumentationBlock", None] = None
        self.appliesTo: List["StandardNameEnum"] = []
        self.dependencies: Union["DocumentationBlock", None] = None
        self.useCase: Union["DocumentationBlock", None] = None
        self.conflicts: Union["DocumentationBlock", None] = None
        self.supportingMaterial: Union["DocumentationBlock", None] = None
        self.remark: Union["DocumentationBlock", None] = None
        self.testedItems: List["Traceable"] = []

    def getDate(self) -> Union[String, None]:
        return self.date

    def setDate(self, value: String) -> "StructuredReq":
        self.date = value
        return self

    def getIssuedBy(self) -> Union[String, None]:
        return self.issuedBy

    def setIssuedBy(self, value: String) -> "StructuredReq":
        self.issuedBy = value
        return self

    def getType(self) -> Union[String, None]:
        return self.type

    def setType(self, value: String) -> "StructuredReq":
        self.type = value
        return self

    def getImportance(self) -> Union[String, None]:
        return self.importance

    def setImportance(self, value: String) -> "StructuredReq":
        self.importance = value
        return self

    def getDescription(self) -> Union["DocumentationBlock", None]:
        return self.description

    def setDescription(self, value: "DocumentationBlock") -> "StructuredReq":
        self.description = value
        return self

    def getRationale(self) -> Union["DocumentationBlock", None]:
        return self.rationale

    def setRationale(self, value: "DocumentationBlock") -> "StructuredReq":
        self.rationale = value
        return self

    def getAppliesTo(self) -> List["StandardNameEnum"]:
        return self.appliesTo

    def addAppliesTo(self, value: "StandardNameEnum") -> "StructuredReq":
        self.appliesTo.append(value)
        return self

    def getDependencies(self) -> Union["DocumentationBlock", None]:
        return self.dependencies

    def setDependencies(self, value: "DocumentationBlock") -> "StructuredReq":
        self.dependencies = value
        return self

    def getUseCase(self) -> Union["DocumentationBlock", None]:
        return self.useCase

    def setUseCase(self, value: "DocumentationBlock") -> "StructuredReq":
        self.useCase = value
        return self

    def getConflicts(self) -> Union["DocumentationBlock", None]:
        return self.conflicts

    def setConflicts(self, value: "DocumentationBlock") -> "StructuredReq":
        self.conflicts = value
        return self

    def getSupportingMaterial(self) -> Union["DocumentationBlock", None]:
        return self.supportingMaterial

    def setSupportingMaterial(self, value: "DocumentationBlock") -> "StructuredReq":
        self.supportingMaterial = value
        return self

    def getRemark(self) -> Union["DocumentationBlock", None]:
        return self.remark

    def setRemark(self, value: "DocumentationBlock") -> "StructuredReq":
        self.remark = value
        return self

    def getTestedItems(self) -> List["Traceable"]:
        return self.testedItems

    def addTestedItem(self, value: "Traceable") -> "StructuredReq":
        self.testedItems.append(value)
        return self


class TraceableText(ARObject):
    def __init__(self) -> None:
        super().__init__()

        self.text: Union[String, None] = None
        self.trace: List["Traceable"] = []

    def getText(self) -> Union[String, None]:
        return self.text

    def setText(self, value: String) -> "TraceableText":
        self.text = value
        return self

    def getTrace(self) -> List["Traceable"]:
        return self.trace

    def addTrace(self, value: "Traceable") -> "TraceableText":
        self.trace.append(value)
        return self


__all__ = [
    'StructuredReq',
    'TraceableText',
]
