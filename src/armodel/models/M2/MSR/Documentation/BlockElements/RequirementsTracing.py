from __future__ import annotations

from typing import TYPE_CHECKING, List, Optional

from abc import ABC
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable import (
    Identifiable,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import DateTime, RefType, String
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.VariationPointCapable import VariationPointCapable

if TYPE_CHECKING:
    from armodel.models.M2.AUTOSARTemplates.GenericStructure.DocumentationOnM1 import StandardNameEnum
    from armodel.models.M2.MSR.Documentation.TextModel.BlockElements import DocumentationBlock


class Traceable(Identifiable, ABC):
    """
    This meta class represents the ability to be subject to tracing within an AUTOSAR model. Note that it is expected that its subclasses inherit either from MultilanguageReferrable or from Identifiable. Nevertheless it also inherits from MultilanguageReferrable in order to provide a common reference target for all Traceables.
    """

    # Traceable method parity checklist:
    # Spec: AUTOSAR_FO_TPS_GenericStructureTemplate.pdf, Table 9.29, p.313
    # Spec verified: R23-11
    # Columns: impl / docstring / test / reader / writer   ([—] = no XML element)
    # [x] __init__         [x] impl  [x] docstring  [x] test  [x] reader  [x] writer
    # [x] getTraceRefs     [x] impl  [x] docstring  [x] test  [x] reader  [x] writer
    # [x] addTraceRef      [x] impl  [x] docstring  [x] test  [x] reader  [x] writer

    def __init__(self, parent, short_name: str):
        if type(self) is Traceable:
            raise TypeError("Traceable is an abstract class.")
        super().__init__(parent, short_name)

        # This association represents the ability to trace to upstream requirements / constraints.
        self.traceRefs: List[RefType] = []

    def getTraceRefs(self) -> List[RefType]:
        """
        This association represents the ability to trace to upstream requirements / constraints.

        Returns:
            The upstream requirements / constraints references
        """
        return self.traceRefs

    def addTraceRef(self, value: Optional[RefType]) -> "Traceable":
        """
        This association represents the ability to trace to upstream requirements / constraints. A None value is a no-op and is not appended.

        Returns:
            self for method chaining
        """
        if value is not None:
            self.traceRefs.append(value)
        return self


class TraceableText(Traceable):
    """
    This meta-class represents the ability to denote a traceable text item such as requirements etc. The following approach applies: shortName represents the tag for tracing, longName represents the head line, category represents the kind of the tagged text (see [constr_2540])
    """

    # TraceableText method parity checklist:
    # Spec: AUTOSAR_FO_TPS_GenericStructureTemplate.pdf, Table 9.30, p.313
    # Spec verified: R23-11
    # Columns: impl / docstring / test / reader / writer / release   ([—] = no XML element)
    # [x] __init__         [x] impl  [x] docstring  [x] test  [—] reader  [—] writer  R23-11
    # [x] getText          [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setText          [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getTraceRefs     [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11  (inherited from Traceable, Table 9.29)
    # [x] addTraceRef      [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11  (inherited from Traceable, Table 9.29)

    def __init__(self, parent, short_name: str):
        super().__init__(parent, short_name)

        # This represents the text to which the tag applies.
        self.text: Optional["DocumentationBlock"] = None

    def getText(self) -> Optional["DocumentationBlock"]:
        """
        This represents the text to which the tag applies.

        Returns:
            The text to which the tag applies
        """
        return self.text

    def setText(self, value: Optional["DocumentationBlock"]) -> "TraceableText":
        """
        This represents the text to which the tag applies. A None value is a no-op and is not set.

        Returns:
            self for method chaining
        """
        if value is not None:
            self.text = value
        return self


class StructuredReq(Traceable, VariationPointCapable):
    """
    This represents a structured requirement. This is intended for a case where specific requirements for features are collected. Note that this can be rendered as a labeled list.
    """

    # StructuredReq method parity checklist:
    # Spec: AUTOSAR_FO_TPS_GenericStructureTemplate.pdf, Table 9.31, p.314
    # Spec verified: R23-11
    # Columns: impl / docstring / test / reader / writer / release   ([—] = no XML element)
    # [x] __init__               [x] impl  [x] docstring  [x] test  [—] reader  [—] writer  R23-11
    # [x] getAppliesTos          [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] addAppliesTo           [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getConflicts           [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setConflicts           [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getDate                [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setDate                [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getDependencies        [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setDependencies        [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getDescription         [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setDescription         [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getImportance          [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setImportance          [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getIssuedBy            [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setIssuedBy            [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getRationale           [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setRationale           [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getRemark              [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setRemark              [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getSupportingMaterial  [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setSupportingMaterial  [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getTestedItemRefs      [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] addTestedItemRef       [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getType                [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setType                [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getUseCase             [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setUseCase             [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getVariationPoint      [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11  (inherited from Identifiable; XSD VARIATION-POINT)
    # [x] setVariationPoint      [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11  (inherited from Identifiable; XSD VARIATION-POINT)

    def __init__(self, parent, short_name: str):
        super().__init__(parent, short_name)

        # This attribute represents the platform the requirement is assigned to.
        self.appliesTo: List[StandardNameEnum] = []

        # This represents an informal specification of conflicts.
        self.conflicts: Optional["DocumentationBlock"] = None

        # This represents the date when the requirement was initiated.
        self.date: Optional[DateTime] = None

        # This represents an informal specification of dependencies. Note that upstream tracing should be formalized in the property trace provided by the superclass Traceable.
        self.dependencies: Optional["DocumentationBlock"] = None

        # This represents the general description of the requirement.
        self.description: Optional["DocumentationBlock"] = None

        # This allows to represent the importance of the requirement.
        self.importance: Optional[String] = None

        # This represents the person, organization or authority which issued the requirement.
        self.issuedBy: Optional[String] = None

        # This represents the rationale of the requirement.
        self.rationale: Optional["DocumentationBlock"] = None

        # This represents an informal remark. Note that this is not modeled as annotation, since these remark is still essential part of the requirement.
        self.remark: Optional["DocumentationBlock"] = None

        # This represents an informal specification of the supporting material.
        self.supportingMaterial: Optional["DocumentationBlock"] = None

        # This association represents the ability to trace on the same specification level. This supports for example the of acceptance tests.
        self.testedItemRefs: List[RefType] = []

        # This attribute allows to denote the type of requirement to denote for example is it an "enhancement", "new feature" etc.
        self.type: Optional[String] = None

        # This describes the relevant use cases. Note that formal references to use cases should be done in the trace relation.
        self.useCase: Optional["DocumentationBlock"] = None

    def getAppliesTos(self) -> List[StandardNameEnum]:
        """
        This attribute represents the platform the requirement is assigned to.

        Returns:
            The platforms the requirement is assigned to
        """
        return self.appliesTo

    def addAppliesTo(self, value: Optional[StandardNameEnum]) -> "StructuredReq":
        """
        This attribute represents the platform the requirement is assigned to. A None value is a no-op and is not appended.

        Returns:
            self for method chaining
        """
        if value is not None:
            self.appliesTo.append(value)
        return self

    def getConflicts(self) -> Optional["DocumentationBlock"]:
        """
        This represents an informal specification of conflicts.

        Returns:
            The informal specification of conflicts
        """
        return self.conflicts

    def setConflicts(self, value: Optional["DocumentationBlock"]) -> "StructuredReq":
        """
        This represents an informal specification of conflicts. A None value is a no-op and does not overwrite an existing conflicts.

        Returns:
            self for method chaining
        """
        if value is not None:
            self.conflicts = value
        return self

    def getDate(self) -> Optional[DateTime]:
        """
        This represents the date when the requirement was initiated.

        Returns:
            The date when the requirement was initiated
        """
        return self.date

    def setDate(self, value: Optional[DateTime]) -> "StructuredReq":
        """
        This represents the date when the requirement was initiated. A None value is a no-op and does not overwrite an existing date.

        Returns:
            self for method chaining
        """
        if value is not None:
            self.date = value
        return self

    def getDependencies(self) -> Optional["DocumentationBlock"]:
        """
        This represents an informal specification of dependencies.

        Returns:
            The informal specification of dependencies
        """
        return self.dependencies

    def setDependencies(self, value: Optional["DocumentationBlock"]) -> "StructuredReq":
        """
        This represents an informal specification of dependencies. A None value is a no-op and does not overwrite an existing dependencies.

        Returns:
            self for method chaining
        """
        if value is not None:
            self.dependencies = value
        return self

    def getDescription(self) -> Optional["DocumentationBlock"]:
        """
        This represents the general description of the requirement.

        Returns:
            The general description of the requirement
        """
        return self.description

    def setDescription(self, value: Optional["DocumentationBlock"]) -> "StructuredReq":
        """
        This represents the general description of the requirement. A None value is a no-op and does not overwrite an existing description.

        Returns:
            self for method chaining
        """
        if value is not None:
            self.description = value
        return self

    def getImportance(self) -> Optional[String]:
        """
        This allows to represent the importance of the requirement.

        Returns:
            The importance of the requirement
        """
        return self.importance

    def setImportance(self, value: Optional[String]) -> "StructuredReq":
        """
        This allows to represent the importance of the requirement. A None value is a no-op and does not overwrite an existing importance.

        Returns:
            self for method chaining
        """
        if value is not None:
            self.importance = value
        return self

    def getIssuedBy(self) -> Optional[String]:
        """
        This represents the person, organization or authority which issued the requirement.

        Returns:
            The person, organization or authority which issued the requirement
        """
        return self.issuedBy

    def setIssuedBy(self, value: Optional[String]) -> "StructuredReq":
        """
        This represents the person, organization or authority which issued the requirement. A None value is a no-op and does not overwrite an existing issuedBy.

        Returns:
            self for method chaining
        """
        if value is not None:
            self.issuedBy = value
        return self

    def getRationale(self) -> Optional["DocumentationBlock"]:
        """
        This represents the rationale of the requirement.

        Returns:
            The rationale of the requirement
        """
        return self.rationale

    def setRationale(self, value: Optional["DocumentationBlock"]) -> "StructuredReq":
        """
        This represents the rationale of the requirement. A None value is a no-op and does not overwrite an existing rationale.

        Returns:
            self for method chaining
        """
        if value is not None:
            self.rationale = value
        return self

    def getRemark(self) -> Optional["DocumentationBlock"]:
        """
        This represents an informal remark. Note that this is not modeled as annotation, since these remark is still essential part of the requirement.

        Returns:
            The informal remark
        """
        return self.remark

    def setRemark(self, value: Optional["DocumentationBlock"]) -> "StructuredReq":
        """
        This represents an informal remark. Note that this is not modeled as annotation, since these remark is still essential part of the requirement. A None value is a no-op and does not overwrite an existing remark.

        Returns:
            self for method chaining
        """
        if value is not None:
            self.remark = value
        return self

    def getSupportingMaterial(self) -> Optional["DocumentationBlock"]:
        """
        This represents an informal specification of the supporting material.

        Returns:
            The informal specification of the supporting material
        """
        return self.supportingMaterial

    def setSupportingMaterial(self, value: Optional["DocumentationBlock"]) -> "StructuredReq":
        """
        This represents an informal specification of the supporting material. A None value is a no-op and does not overwrite an existing supportingMaterial.

        Returns:
            self for method chaining
        """
        if value is not None:
            self.supportingMaterial = value
        return self

    def getTestedItemRefs(self) -> List[RefType]:
        """
        This association represents the ability to trace on the same specification level. This supports for example the of acceptance tests.

        Returns:
            The references on the same specification level
        """
        return self.testedItemRefs

    def addTestedItemRef(self, value: Optional[RefType]) -> "StructuredReq":
        """
        This association represents the ability to trace on the same specification level. This supports for example the of acceptance tests. A None value is a no-op and is not appended.

        Returns:
            self for method chaining
        """
        if value is not None:
            self.testedItemRefs.append(value)
        return self

    def getType(self) -> Optional[String]:
        """
        This attribute allows to denote the type of requirement to denote for example is it an "enhancement", "new feature" etc.

        Returns:
            The type of requirement
        """
        return self.type

    def setType(self, value: Optional[String]) -> "StructuredReq":
        """
        This attribute allows to denote the type of requirement to denote for example is it an "enhancement", "new feature" etc. A None value is a no-op and does not overwrite an existing type.

        Returns:
            self for method chaining
        """
        if value is not None:
            self.type = value
        return self

    def getUseCase(self) -> Optional["DocumentationBlock"]:
        """
        This describes the relevant use cases. Note that formal references to use cases should be done in the trace relation.

        Returns:
            The relevant use cases
        """
        return self.useCase

    def setUseCase(self, value: Optional["DocumentationBlock"]) -> "StructuredReq":
        """
        This describes the relevant use cases. Note that formal references to use cases should be done in the trace relation. A None value is a no-op and does not overwrite an existing useCase.

        Returns:
            self for method chaining
        """
        if value is not None:
            self.useCase = value
        return self
