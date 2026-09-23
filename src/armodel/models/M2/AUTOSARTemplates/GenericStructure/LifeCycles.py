"""
This module contains classes for representing AUTOSAR life cycle information
in the GenericStructure module.
"""

from typing import List, Optional

from armodel.models.M2.MSR.Documentation.TextModel.BlockElements import DocumentationBlock
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import DateTime, RefType, RevisionLabelString
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ARPackage import ARElement


class LifeCyclePeriod(ARObject):
    """
    This meta class represents the ability to specify a point of time within a specified period, e.g. the starting or end point, in which a specific life cycle state is valid/applies to.
    """

    # LifeCyclePeriod method parity checklist:
    # Spec: AUTOSAR_FO_TPS_GenericStructureTemplate.pdf, Table 12.4, p.392
    # Columns: impl / docstring / test / reader / writer / release   ([—] = no XML element)
    # [x] __init__              [x] impl  [x] docstring  [x] test  [—] reader  [—] writer  R23-11
    # [x] getArReleaseVersion   [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setArReleaseVersion   [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getDate               [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setDate               [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getProductRelease     [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setProductRelease     [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11

    def __init__(self):
        super().__init__()

        # Version of the AUTOSAR Release the element referred to is part of. The numbering contains three levels (major, minor, revision) which are defined by AUTOSAR. Tags: xml.sequenceOffset=20
        self.arReleaseVersion: Optional[RevisionLabelString] = None

        # Date within period. Tags: xml.sequenceOffset=10
        self.date: Optional[DateTime] = None

        # Version of the product within the period. Tags: xml.sequenceOffset=30
        self.productRelease: Optional[RevisionLabelString] = None

    def getArReleaseVersion(self) -> Optional[RevisionLabelString]:
        """
        Version of the AUTOSAR Release the element referred to is part of. The numbering contains three levels (major, minor, revision) which are defined by AUTOSAR.
        """
        return self.arReleaseVersion

    def setArReleaseVersion(self, value: Optional[RevisionLabelString]) -> "LifeCyclePeriod":
        """
        Version of the AUTOSAR Release the element referred to is part of. The numbering contains three levels (major, minor, revision) which are defined by AUTOSAR. A None value is a no-op and does not overwrite an existing AUTOSAR release version.
        """
        if value is not None:
            self.arReleaseVersion = value
        return self

    def getDate(self) -> Optional[DateTime]:
        """
        Date within period.
        """
        return self.date

    def setDate(self, value: Optional[DateTime]) -> "LifeCyclePeriod":
        """
        Date within period. A None value is a no-op and does not overwrite an existing date.
        """
        if value is not None:
            self.date = value
        return self

    def getProductRelease(self) -> Optional[RevisionLabelString]:
        """
        Version of the product within the period.
        """
        return self.productRelease

    def setProductRelease(self, value: Optional[RevisionLabelString]) -> "LifeCyclePeriod":
        """
        Version of the product within the period. A None value is a no-op and does not overwrite an existing product release.
        """
        if value is not None:
            self.productRelease = value
        return self


class LifeCycleInfo(ARObject):
    """
    LifeCycleInfo describes the life cycle state of an element together with additional information like what to use instead
    """

    # LifeCycleInfo method parity checklist:
    # Spec: AUTOSAR_FO_TPS_GenericStructureTemplate.pdf, Table 12.5, pp.392-393
    # Columns: impl / docstring / test / reader / writer / release   ([—] = no XML element)
    # Table split across a page break: body main fragment (header + lcObject/lcState/periodBegin rows) p.392,
    # `Table 12.5: LifeCycleInfo` caption + continuation fragment (periodEnd/remark/useInstead) p.393.
    # R4.3.1 reproduction: AUTOSAR_TPS_GenericStructureTemplate.pdf Table 11.5, p.364 (identical except useInstead
    # Note "must" vs R23-11 "shall" and no Aggregated-by row); appendix Table C.63 (AUTOSAR_FO_TPS_StandardizationTemplate)
    # carries the identical Note — FO GST Table 12.5 cited.
    # XSD 00052: group LIFE-CYCLE-INFO L76529 sequence LC-OBJECT-REF (0..1) → LC-STATE-REF (0..1) → PERIOD-BEGIN (0..1)
    # → PERIOD-END (0..1) → REMARK (0..1) → USE-INSTEAD-REFS (0..1, unbounded USE-INSTEAD-REF); complexType
    # LIFE-CYCLE-INFO L76608 abstract="false" = AR-OBJECT group + own group (Base row ARObject).
    # Reader readLifeCycleInfo / writer writeLifeCycleInfo dispatched from read/writeLifeCycleInfoSetLifeCycleInfos
    # (arxml_parser.py / arxml_writer.py); PERIOD-END coverage added this sync (was silently dropped both sides).
    # [x] __init__            [x] impl  [x] docstring  [x] test  [—] reader  [—] writer  R23-11
    # [x] getLcObjectRef      [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setLcObjectRef      [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getLcStateRef       [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setLcStateRef       [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getPeriodBegin      [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setPeriodBegin      [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getPeriodEnd        [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setPeriodEnd        [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getRemark           [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setRemark           [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getUseInsteadRefs   [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] addUseInsteadRef    [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11

    def __init__(self):
        super().__init__()

        # Element(s) have the life cycle as described in lcState.
        self.lcObjectRef: Optional[RefType] = None

        # This denotes the particular state assigned to the object. If no lcState is given then the default life cycle state of LifeCycleInfoSet is assumed.
        self.lcStateRef: Optional[RefType] = None

        # Starting point of period in which the element has the denoted life cycle state lcState. If no periodBegin is given then the default period begin of LifeCycleInfoSet is assumed.
        self.periodBegin: Optional[LifeCyclePeriod] = None

        # Expiry date, i.e. end point of period the element does not have the denoted life cycle state lcState any more. If no periodEnd is given then the default period begin of LifeCycleInfoSet is assumed.
        self.periodEnd: Optional[LifeCyclePeriod] = None

        # Remark describing for example • why the element was given the specified life cycle • the semantics of useInstead
        self.remark: Optional[DocumentationBlock] = None

        # Element(s) that should be used instead of the one denoted in referrable. Only relevant in case of life cycle states lcState unlike "valid". In case there are multiple references the exact semantics shall be individually described in the remark.
        self.useInsteadRefs: List[RefType] = []

    def getLcObjectRef(self) -> Optional[RefType]:
        """
        Element(s) have the life cycle as described in lcState.
        """
        return self.lcObjectRef

    def setLcObjectRef(self, value: Optional[RefType]) -> "LifeCycleInfo":
        """
        Element(s) have the life cycle as described in lcState. A None value is a no-op and does not overwrite an existing life cycle object reference.
        """
        if value is not None:
            self.lcObjectRef = value
        return self

    def getLcStateRef(self) -> Optional[RefType]:
        """
        This denotes the particular state assigned to the object. If no lcState is given then the default life cycle state of LifeCycleInfoSet is assumed.
        """
        return self.lcStateRef

    def setLcStateRef(self, value: Optional[RefType]) -> "LifeCycleInfo":
        """
        This denotes the particular state assigned to the object. If no lcState is given then the default life cycle state of LifeCycleInfoSet is assumed. A None value is a no-op and does not overwrite an existing life cycle state.
        """
        if value is not None:
            self.lcStateRef = value
        return self

    def getPeriodBegin(self) -> Optional[LifeCyclePeriod]:
        """
        Starting point of period in which the element has the denoted life cycle state lcState. If no periodBegin is given then the default period begin of LifeCycleInfoSet is assumed.
        """
        return self.periodBegin

    def setPeriodBegin(self, value: Optional[LifeCyclePeriod]) -> "LifeCycleInfo":
        """
        Starting point of period in which the element has the denoted life cycle state lcState. If no periodBegin is given then the default period begin of LifeCycleInfoSet is assumed. A None value is a no-op and does not overwrite an existing period begin.
        """
        if value is not None:
            self.periodBegin = value
        return self

    def getPeriodEnd(self) -> Optional[LifeCyclePeriod]:
        """
        Expiry date, i.e. end point of period the element does not have the denoted life cycle state lcState any more. If no periodEnd is given then the default period begin of LifeCycleInfoSet is assumed.
        """
        return self.periodEnd

    def setPeriodEnd(self, value: Optional[LifeCyclePeriod]) -> "LifeCycleInfo":
        """
        Expiry date, i.e. end point of period the element does not have the denoted life cycle state lcState any more. If no periodEnd is given then the default period begin of LifeCycleInfoSet is assumed. A None value is a no-op and does not overwrite an existing period end.
        """
        if value is not None:
            self.periodEnd = value
        return self

    def getRemark(self) -> Optional[DocumentationBlock]:
        """
        Remark describing for example • why the element was given the specified life cycle • the semantics of useInstead
        """
        return self.remark

    def setRemark(self, value: Optional[DocumentationBlock]) -> "LifeCycleInfo":
        """
        Remark describing for example • why the element was given the specified life cycle • the semantics of useInstead A None value is a no-op and does not overwrite an existing remark.
        """
        if value is not None:
            self.remark = value
        return self

    def getUseInsteadRefs(self) -> List[RefType]:
        """
        Element(s) that should be used instead of the one denoted in referrable. Only relevant in case of life cycle states lcState unlike "valid". In case there are multiple references the exact semantics shall be individually described in the remark.
        """
        return self.useInsteadRefs

    def addUseInsteadRef(self, value: Optional[RefType]) -> "LifeCycleInfo":
        """
        Element(s) that should be used instead of the one denoted in referrable. Only relevant in case of life cycle states lcState unlike "valid". In case there are multiple references the exact semantics shall be individually described in the remark. A None value is a no-op and does not add to useInsteadRefs.
        """
        if value is not None:
            self.useInsteadRefs.append(value)
        return self


class LifeCycleInfoSet(ARElement):
    """
    Represents a set of life cycle information in AUTOSAR models.
    This class organizes and manages multiple life cycle information entries.
    """

    # LifeCycleInfoSet method parity checklist:
    # [ ] __init__                     [x] impl  [ ] docstring  [x] test
    # [x] getDefaultLcStateRef         [x] impl  [x] docstring  [x] test
    # [x] setDefaultLcStateRef         [x] impl  [x] docstring  [x] test
    # [x] getDefaultPeriodBegin        [x] impl  [x] docstring  [x] test
    # [x] setDefaultPeriodBegin        [x] impl  [x] docstring  [x] test
    # [x] getDefaultPeriodEnd          [x] impl  [x] docstring  [x] test
    # [x] setDefaultPeriodEnd          [x] impl  [x] docstring  [x] test
    # [x] getLifeCycleInfos            [x] impl  [x] docstring  [x] test
    # [x] addLifeCycleInfo             [x] impl  [x] docstring  [x] test
    # [x] getUsedLifeCycleStateDefinitionGroupRef [x] impl  [x] docstring  [x] test
    # [x] setUsedLifeCycleStateDefinitionGroupRef [x] impl  [x] docstring  [x] test

    def __init__(self, parent, short_name: str):
        super().__init__(parent, short_name)

        self.defaultLcStateRef: Optional[RefType] = None
        self.defaultPeriodBegin: Optional[LifeCyclePeriod] = None
        self.defaultPeriodEnd: Optional[LifeCyclePeriod] = None
        self.lifeCycleInfos: List[LifeCycleInfo] = []
        self.usedLifeCycleStateDefinitionGroupRef: Optional[RefType] = None

    def getDefaultLcStateRef(self) -> Optional[RefType]:
        """
        Gets the default life cycle state reference.

        Returns:
            RefType representing the default life cycle state reference, or None if not set
        """
        return self.defaultLcStateRef

    def setDefaultLcStateRef(self, value: RefType):
        """
        Sets the default life cycle state reference.
        Only sets the value if it is not None.

        Args:
            value: The default life cycle state reference to set

        Returns:
            self for method chaining
        """
        if value is not None:
            self.defaultLcStateRef = value
        return self

    def getDefaultPeriodBegin(self) -> Optional[LifeCyclePeriod]:
        """
        Gets the default beginning period.

        Returns:
            LifeCyclePeriod representing the default beginning period, or None if not set
        """
        return self.defaultPeriodBegin

    def setDefaultPeriodBegin(self, value: LifeCyclePeriod):
        """
        Sets the default beginning period.
        Only sets the value if it is not None.

        Args:
            value: The default beginning period to set

        Returns:
            self for method chaining
        """
        if value is not None:
            self.defaultPeriodBegin = value
        return self

    def getDefaultPeriodEnd(self) -> Optional[LifeCyclePeriod]:
        """
        Gets the default ending period.

        Returns:
            LifeCyclePeriod representing the default ending period, or None if not set
        """
        return self.defaultPeriodEnd

    def setDefaultPeriodEnd(self, value: LifeCyclePeriod):
        """
        Sets the default ending period.
        Only sets the value if it is not None.

        Args:
            value: The default ending period to set

        Returns:
            self for method chaining
        """
        if value is not None:
            self.defaultPeriodEnd = value
        return self

    def getLifeCycleInfos(self) -> List[LifeCycleInfo]:
        """
        Gets the list of life cycle information entries.

        Returns:
            List of LifeCycleInfo instances
        """
        return self.lifeCycleInfos

    def addLifeCycleInfo(self, value: LifeCycleInfo):
        """
        Adds a life cycle information entry.
        Only adds the value if it is not None.

        Args:
            value: The life cycle information entry to add

        Returns:
            self for method chaining
        """
        if value is not None:
            self.lifeCycleInfos.append(value)
        return self

    def getUsedLifeCycleStateDefinitionGroupRef(self) -> Optional[RefType]:
        """
        Gets the reference to used life cycle state definition group.

        Returns:
            RefType representing the reference to used life cycle state definition group, or None if not set
        """
        return self.usedLifeCycleStateDefinitionGroupRef

    def setUsedLifeCycleStateDefinitionGroupRef(self, value: RefType):
        """
        Sets the reference to used life cycle state definition group.
        Only sets the value if it is not None.

        Args:
            value: The reference to used life cycle state definition group to set

        Returns:
            self for method chaining
        """
        if value is not None:
            self.usedLifeCycleStateDefinitionGroupRef = value
        return self
