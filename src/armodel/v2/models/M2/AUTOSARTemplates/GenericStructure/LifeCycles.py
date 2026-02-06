"""
This module contains classes for representing AUTOSAR life cycle information
in the GenericStructure module.
"""

from datetime import datetime
from typing import (
    List,
    Optional,
)

from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import (
    ARObject,
)
from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable import (
    ARElement,
)
from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    RefType,
    RevisionLabelString,
)
from armodel.v2.models.M2.MSR.Documentation.TextModel.BlockElements import (
    DocumentationBlock,
)


class LifeCyclePeriod(ARObject):

    def _validate_abstract(self) -> None:
        """Validate this is a concrete class."""
        pass

    '''
        This meta class represents the ability to specify a point of time within a specified period, e.g. the starting
        or end point, in which a specific life cycle state is valid/applies to.
    '''

    def __init__(self) -> None:
        super().__init__()

        self.arReleaseVersion: Union[Optional[RevisionLabelString] , None] = None
        self.date: Union[Optional[datetime] , None] = None
        self.productRelease: Union[Optional[RevisionLabelString] , None] = None

    def getArReleaseVersion(self) -> Optional[RevisionLabelString]:
        """
        Gets the AUTOSAR release version for this life cycle period.

        Returns:
            RevisionLabelString representing the AUTOSAR release version, or None if not set
        """
        return self.arReleaseVersion

    def setArReleaseVersion(self, value: RevisionLabelString):
        """
        Sets the AUTOSAR release version for this life cycle period.
        Only sets the value if it is not None.

        Args:
            value: The AUTOSAR release version to set

        Returns:
            self for method chaining
        """
        if value is not None:
            self.arReleaseVersion = value
        return self

    def getDate(self) -> Optional[datetime]:
        """
        Gets the date for this life cycle period.

        Returns:
            datetime object representing the date, or None if not set
        """
        return self.date

    def setDate(self, value: datetime):
        """
        Sets the date for this life cycle period.
        Only sets the value if it is not None.

        Args:
            value: The date to set

        Returns:
            self for method chaining
        """
        if value is not None:
            self.date = value
        return self

    def getProductRelease(self) -> Optional[RevisionLabelString]:
        """
        Gets the product release for this life cycle period.

        Returns:
            RevisionLabelString representing the product release, or None if not set
        """
        return self.productRelease

    def setProductRelease(self, value: RevisionLabelString):
        """
        Sets the product release for this life cycle period.
        Only sets the value if it is not None.

        Args:
            value: The product release to set

        Returns:
            self for method chaining
        """
        if value is not None:
            self.productRelease = value
        return self


class LifeCycleInfo(ARObject):
    """
    Represents life cycle information in AUTOSAR models.
    This class defines information about the life cycle of AUTOSAR elements.
    """


    def _validate_abstract(self) -> None:
        """Validate this is a concrete class."""
        pass

    def __init__(self) -> None:
        super().__init__()

        self.lcObjectRef: Union[Optional[RefType] , None] = None
        self.lcStateRef: Union[Optional[RefType] , None] = None
        self.periodBegin: Union[Optional[LifeCyclePeriod] , None] = None
        self.periodEnd: Union[Optional[LifeCyclePeriod] , None] = None
        self.remark: Union[Optional[DocumentationBlock] , None] = None
        self.useInsteadRefs: List[RefType] = []

    def getLcObjectRef(self) -> Optional[RefType]:
        """
        Gets the life cycle object reference.

        Returns:
            RefType representing the life cycle object reference, or None if not set
        """
        return self.lcObjectRef

    def setLcObjectRef(self, value: RefType):
        """
        Sets the life cycle object reference.
        Only sets the value if it is not None.

        Args:
            value: The life cycle object reference to set

        Returns:
            self for method chaining
        """
        if value is not None:
            self.lcObjectRef = value
        return self

    def getLcStateRef(self) -> Optional[RefType]:
        """
        Gets the life cycle state reference.

        Returns:
            RefType representing the life cycle state reference, or None if not set
        """
        return self.lcStateRef

    def setLcStateRef(self, value: RefType):
        """
        Sets the life cycle state reference.
        Only sets the value if it is not None.

        Args:
            value: The life cycle state reference to set

        Returns:
            self for method chaining
        """
        if value is not None:
            self.lcStateRef = value
        return self

    def getPeriodBegin(self) -> Optional[LifeCyclePeriod]:
        """
        Gets the beginning period of the life cycle.

        Returns:
            LifeCyclePeriod representing the beginning period, or None if not set
        """
        return self.periodBegin

    def setPeriodBegin(self, value: LifeCyclePeriod):
        """
        Sets the beginning period of the life cycle.
        Only sets the value if it is not None.

        Args:
            value: The beginning period to set

        Returns:
            self for method chaining
        """
        if value is not None:
            self.periodBegin = value
        return self

    def getPeriodEnd(self) -> Optional[LifeCyclePeriod]:
        """
        Gets the ending period of the life cycle.

        Returns:
            LifeCyclePeriod representing the ending period, or None if not set
        """
        return self.periodEnd

    def setPeriodEnd(self, value: LifeCyclePeriod):
        """
        Sets the ending period of the life cycle.
        Only sets the value if it is not None.

        Args:
            value: The ending period to set

        Returns:
            self for method chaining
        """
        if value is not None:
            self.periodEnd = value
        return self

    def getRemark(self) -> Optional[DocumentationBlock]:
        """
        Gets the remark documentation for this life cycle information.

        Returns:
            DocumentationBlock instance, or None if not set
        """
        return self.remark

    def setRemark(self, value: DocumentationBlock):
        """
        Sets the remark documentation for this life cycle information.
        Only sets the value if it is not None.

        Args:
            value: The remark documentation to set

        Returns:
            self for method chaining
        """
        if value is not None:
            self.remark = value
        return self

    def getUseInsteadRefs(self) -> List[RefType]:
        """
        Gets the list of "use instead" references.

        Returns:
            List of RefType instances
        """
        return self.useInsteadRefs

    def addUseInsteadRef(self, value: RefType):
        """
        Adds a "use instead" reference.
        Only adds the value if it is not None.

        Args:
            value: The "use instead" reference to add

        Returns:
            self for method chaining
        """
        if value is not None:
            self.useInsteadRefs.append(value)
        return self


class LifeCycleInfoSet(ARElement):
    """
    Represents a set of life cycle information in AUTOSAR models.
    This class organizes and manages multiple life cycle information entries.
    """

    def __init__(self, parent, short_name: str) -> None:
        super().__init__(parent, short_name)

        self.defaultLcStateRef: Union[Optional[RefType] , None] = None
        self.defaultPeriodBegin: Union[Optional[LifeCyclePeriod] , None] = None
        self.defaultPeriodEnd: Union[Optional[LifeCyclePeriod] , None] = None
        self.lifeCycleInfos: List[LifeCycleInfo] = []
        self.usedLifeCycleStateDefinitionGroupRef: Union[Optional[RefType] , None] = None

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
