"""
This module defines measurement and calibration group classes in AUTOSAR.
"""

from __future__ import annotations

from typing import List, Optional

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ARPackage import ARElement
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import RefType


class McGroup(ARElement):
    """
    Represents a group element to be used as input to support measurement and calibration. It is used to provide selection lists (groups) of calibration parameters, measurement variables, and functions in a hierarchical manner (subGroups).
    """

    # McGroup method parity checklist:
    # Spec: AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.pdf, Table 9.10, p.190
    # Spec verified: R23-11
    # [x] __init__                       [x] impl  [x] docstring  [x] test
    # [x] addMcFunctionRef               [x] impl  [x] docstring  [x] test
    # [x] getMcFunctionRefs              [x] impl  [x] docstring  [x] test
    # [x] getRefCalprmSet                [x] impl  [x] docstring  [x] test
    # [x] setRefCalprmSet                [x] impl  [x] docstring  [x] test
    # [x] getRefMeasurementSet           [x] impl  [x] docstring  [x] test
    # [x] setRefMeasurementSet           [x] impl  [x] docstring  [x] test
    # [x] addSubGroupRef                 [x] impl  [x] docstring  [x] test
    # [x] getSubGroupRefs                [x] impl  [x] docstring  [x] test

    def __init__(self, parent: ARObject, short_name: str):
        """
        Initializes the McGroup with a parent and short name.

        Args:
            parent: The parent ARObject that contains this group
            short_name: The unique short name of this group
        """
        super().__init__(parent, short_name)

        # A McFunction that is seen as part of the enclosing group. Tags: atp.Splitkey=mcFunction xml.sequenceOffset=40
        self.mcFunctionRefs: List[RefType] = []

        # Refers to the set of adjustable data (= calibration parameters) referred by this McGroup. Tags: atp.Splitkey=refCalprmSet xml.sequenceOffset=20
        self.refCalprmSet: Optional[McGroupDataRefSet] = None

        # Refers to the set of measurable belonging to this Mc Group. Tags: atp.Splitkey=refMeasurementSet xml.sequenceOffset=30
        self.refMeasurementSet: Optional[McGroupDataRefSet] = None

        # A sub-group that is seen as part of the enclosing group. Tags: atp.Splitkey=subGroup xml.sequenceOffset=10
        self.subGroupRefs: List[RefType] = []

    def addMcFunctionRef(self, value: Optional[RefType]) -> "McGroup":
        """
        Adds a reference to an McFunction that is seen as part of the enclosing group.
        A None value is a no-op and does not append anything.

        Args:
            value: The McFunction reference to add

        Returns:
            self for method chaining
        """
        if value is not None:
            self.mcFunctionRefs.append(value)
        return self

    def getMcFunctionRefs(self) -> List[RefType]:
        """
        Gets the references to McFunctions that are seen as part of the enclosing group.

        Returns:
            List of RefType instances referencing McFunction elements
        """
        return self.mcFunctionRefs

    def getRefCalprmSet(self) -> Optional[McGroupDataRefSet]:
        """
        Gets the set of adjustable data (= calibration parameters) referred by this McGroup.

        Returns:
            McGroupDataRefSet instance, or None if not set
        """
        return self.refCalprmSet

    def setRefCalprmSet(self, value: Optional[McGroupDataRefSet]) -> "McGroup":
        """
        Sets the set of adjustable data (= calibration parameters) referred by this McGroup.
        A None value is a no-op and does not overwrite an existing set.

        Args:
            value: The McGroupDataRefSet to set

        Returns:
            self for method chaining
        """
        if value is not None:
            self.refCalprmSet = value
        return self

    def getRefMeasurementSet(self) -> Optional[McGroupDataRefSet]:
        """
        Gets the set of measurable belonging to this Mc Group.

        Returns:
            McGroupDataRefSet instance, or None if not set
        """
        return self.refMeasurementSet

    def setRefMeasurementSet(self, value: Optional[McGroupDataRefSet]) -> "McGroup":
        """
        Sets the set of measurable belonging to this Mc Group.
        A None value is a no-op and does not overwrite an existing set.

        Args:
            value: The McGroupDataRefSet to set

        Returns:
            self for method chaining
        """
        if value is not None:
            self.refMeasurementSet = value
        return self

    def addSubGroupRef(self, value: Optional[RefType]) -> "McGroup":
        """
        Adds a reference to a sub-group that is seen as part of the enclosing group.
        A None value is a no-op and does not append anything.

        Args:
            value: The sub-group reference to add

        Returns:
            self for method chaining
        """
        if value is not None:
            self.subGroupRefs.append(value)
        return self

    def getSubGroupRefs(self) -> List[RefType]:
        """
        Gets the references to sub-groups that are seen as part of the enclosing group.

        Returns:
            List of RefType instances referencing McGroup elements
        """
        return self.subGroupRefs


class McGroupDataRefSet(ARObject):
    """
    Refers to a set of data assigned to an McGroup in a particular role. The data are given • either by entries in a FlatMap • or by data instances that are part of MC support data. These two possibilities can be mixed within a given McGroupDataRefSet. Which one to use depends on the process and tool environment. The set is subject to variability because the same functional model may be used with various representation of the data.
    """

    # McGroupDataRefSet method parity checklist:
    # Spec: AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.pdf, Table 9.11, p.191
    # Spec verified: R23-11
    # [x] __init__                       [x] impl  [x] docstring  [x] test
    # [x] addFlatMapEntryRef             [x] impl  [x] docstring  [x] test
    # [x] getFlatMapEntryRefs            [x] impl  [x] docstring  [x] test
    # [x] addMcDataInstanceRef           [x] impl  [x] docstring  [x] test
    # [x] getMcDataInstanceRefs          [x] impl  [x] docstring  [x] test

    def __init__(self):
        """
        Initializes the McGroupDataRefSet with default values.
        """
        super().__init__()

        # Refers to an entry in a FlatMap that is part of the set, for example a calibration parameter or measured variable. Tags: xml.sequenceOffset=50
        self.flatMapEntryRefs: List[RefType] = []

        # Refers to a data instance within MC support data that is part of the set, i.e. a calibration parameter or measured variable. Tags: xml.sequenceOffset=60
        self.mcDataInstanceRefs: List[RefType] = []

    def addFlatMapEntryRef(self, value: Optional[RefType]) -> "McGroupDataRefSet":
        """
        Adds a reference to an entry in a FlatMap that is part of the set, for example a calibration parameter or measured variable.
        A None value is a no-op and does not append anything.

        Args:
            value: The FlatMap entry reference to add

        Returns:
            self for method chaining
        """
        if value is not None:
            self.flatMapEntryRefs.append(value)
        return self

    def getFlatMapEntryRefs(self) -> List[RefType]:
        """
        Gets the references to entries in a FlatMap that are part of the set, for example calibration parameters or measured variables.

        Returns:
            List of RefType instances referencing FlatInstanceDescriptor elements
        """
        return self.flatMapEntryRefs

    def addMcDataInstanceRef(self, value: Optional[RefType]) -> "McGroupDataRefSet":
        """
        Adds a reference to a data instance within MC support data that is part of the set, i.e. a calibration parameter or measured variable.
        A None value is a no-op and does not append anything.

        Args:
            value: The MC data instance reference to add

        Returns:
            self for method chaining
        """
        if value is not None:
            self.mcDataInstanceRefs.append(value)
        return self

    def getMcDataInstanceRefs(self) -> List[RefType]:
        """
        Gets the references to data instances within MC support data that are part of the set, i.e. calibration parameters or measured variables.

        Returns:
            List of RefType instances referencing McDataInstance elements
        """
        return self.mcDataInstanceRefs


__all__ = ["McGroup", "McGroupDataRefSet"]
