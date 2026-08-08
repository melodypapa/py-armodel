"""
This module contains classes for representing AUTOSAR Run-Time Protection (RPT) scenarios
and access point identification elements in software component templates.
"""

from abc import ABC
from typing import Optional

from armodel.models.M2.AUTOSARTemplates.CommonStructure.MeasurementCalibrationSupport.RptSupport import RptEnablerImplTypeEnum, RptExecutionControlEnum, RptPreparationEnum
from armodel.models.M2.AUTOSARTemplates.GenericStructure.AbstractStructure import AtpStructureElement
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import AREnum, PositiveInteger


class IdentCaption(AtpStructureElement, ABC):
    """
    Abstract base class for identification captions used in access points.
    """

    # IdentCaption method parity checklist:
    # [ ] __init__                     [x] impl  [ ] docstring  [ ] test

    def __init__(self, parent: ARObject, short_name: str):
        if type(self) is IdentCaption:
            raise TypeError("IdentCaption is an abstract class.")

        super().__init__(parent, short_name)


class ModeAccessPointIdent(IdentCaption):
    """
    Identification of a mode access point used to reference a specific
    access point within a runnable entity.
    """

    # ModeAccessPointIdent method parity checklist:
    # [ ] __init__                     [x] impl  [ ] docstring  [ ] test

    def __init__(self, parent: ARObject, short_name: str):
        super().__init__(parent, short_name)


class RptServicePointEnum(AREnum):
    """
    Specifies whether the invocation of ExecutableEntitys due to activation of specific RteEvents/BswEvents requires the insertion of Service Points.
    """

    # RptServicePointEnum method parity checklist:
    # Spec: AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf, Table 14.15, p.860
    # Spec verified: R23-11
    # [x] __init__                     [x] impl  [x] docstring  [x] test

    # Enables generation of service points by the RTE generator. atp.EnumerationLiteralIndex=0
    ENABLED = "enabled"

    # No Service Points are requested. atp.EnumerationLiteralIndex=1
    NONE = "none"

    def __init__(self):
        super().__init__(
            (
                RptServicePointEnum.ENABLED,
                RptServicePointEnum.NONE,
            )
        )


class RptImplPolicy(ARObject):
    """
    Describes the code preparation for rapid prototyping at data accesses.
    """

    # RptImplPolicy method parity checklist:
    # Spec: AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf, Table 14.8, p.854
    # Spec verified: R23-11
    # [x] __init__                          [x] impl  [x] docstring  [x] test
    # [x] getRptEnablerImplType             [x] impl  [x] docstring  [x] test
    # [x] setRptEnablerImplType             [x] impl  [x] docstring  [x] test
    # [x] getRptPreparationLevel            [x] impl  [x] docstring  [x] test
    # [x] setRptPreparationLevel            [x] impl  [x] docstring  [x] test

    def __init__(self):
        """
        Initializes the RptImplPolicy.
        """
        super().__init__()

        # For Level 2 or Level3 this property determines how the RTE implements the additional "RP enabler" flag.
        self.rptEnablerImplType: Optional[RptEnablerImplTypeEnum] = None

        # Mandates RP preparation level for access to VariableDataPrototype within generated RTE implementation.
        self.rptPreparationLevel: Optional[RptPreparationEnum] = None

    def getRptEnablerImplType(self) -> Optional[RptEnablerImplTypeEnum]:
        """
        Gets how the RTE implements the additional "RP enabler" flag for Level 2 or Level 3.

        Returns:
            RptEnablerImplTypeEnum describing the enabler flag implementation, or None if not set
        """
        return self.rptEnablerImplType

    def setRptEnablerImplType(self, value: Optional[RptEnablerImplTypeEnum]) -> "RptImplPolicy":
        """
        Sets how the RTE implements the additional "RP enabler" flag for Level 2 or Level 3.
        A None value is a no-op and does not overwrite an existing enabler implementation type.

        Args:
            value: The RptEnablerImplTypeEnum to set

        Returns:
            self for method chaining
        """
        if value is not None:
            self.rptEnablerImplType = value
        return self

    def getRptPreparationLevel(self) -> Optional[RptPreparationEnum]:
        """
        Gets the mandated RP preparation level for access to a VariableDataPrototype within the generated RTE implementation.

        Returns:
            RptPreparationEnum describing the preparation level, or None if not set
        """
        return self.rptPreparationLevel

    def setRptPreparationLevel(self, value: Optional[RptPreparationEnum]) -> "RptImplPolicy":
        """
        Sets the mandated RP preparation level for access to a VariableDataPrototype within the generated RTE implementation.
        A None value is a no-op and does not overwrite an existing preparation level.

        Args:
            value: The RptPreparationEnum to set

        Returns:
            self for method chaining
        """
        if value is not None:
            self.rptPreparationLevel = value
        return self


class RptExecutableEntityProperties(ARObject):
    """
    Describes the code preparation for rapid prototyping at ExecutableEntity invocation.
    """

    # RptExecutableEntityProperties method parity checklist:
    # Spec: AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf, Table 14.13, p.859
    # Spec verified: R23-11
    # [x] __init__                          [x] impl  [x] docstring  [x] test
    # [x] getMaxRptEventId                  [x] impl  [x] docstring  [x] test
    # [x] setMaxRptEventId                  [x] impl  [x] docstring  [x] test
    # [x] getMinRptEventId                  [x] impl  [x] docstring  [x] test
    # [x] setMinRptEventId                  [x] impl  [x] docstring  [x] test
    # [x] getRptExecutionControl           [x] impl  [x] docstring  [x] test
    # [x] setRptExecutionControl           [x] impl  [x] docstring  [x] test
    # [x] getRptServicePoint               [x] impl  [x] docstring  [x] test
    # [x] setRptServicePoint               [x] impl  [x] docstring  [x] test

    def __init__(self):
        """
        Initializes the RptExecutableEntityProperties.
        """
        super().__init__()

        # Highest RPT event id usable for RTE generated service points. This attribute is relevant, if dedicated id range shall be applied to the ExecutableEntitys of a software component or specific ExecutableEntitys.
        self.maxRptEventId: Optional[PositiveInteger] = None

        # Lowest RPT event id usable for RTE generated service points. This attribute is relevant, if dedicated id range shall be applied to the ExecutableEntitys of a software component or specific ExecutableEntitys.
        self.minRptEventId: Optional[PositiveInteger] = None

        # This attribute specifies the rapid prototyping control of the executable
        self.rptExecutionControl: Optional[RptExecutionControlEnum] = None

        # Enables generation of service points by the RTE generator.
        self.rptServicePoint: Optional[RptServicePointEnum] = None

    def getMaxRptEventId(self) -> Optional[PositiveInteger]:
        """
        Gets the highest RPT event id usable for RTE generated service points.

        Returns:
            PositiveInteger representing the highest RPT event id, or None if not set
        """
        return self.maxRptEventId

    def setMaxRptEventId(self, value: Optional[PositiveInteger]) -> "RptExecutableEntityProperties":
        """
        Sets the highest RPT event id usable for RTE generated service points.
        A None value is a no-op and does not overwrite an existing id.

        Args:
            value: The highest RPT event id to set

        Returns:
            self for method chaining
        """
        if value is not None:
            self.maxRptEventId = value
        return self

    def getMinRptEventId(self) -> Optional[PositiveInteger]:
        """
        Gets the lowest RPT event id usable for RTE generated service points.

        Returns:
            PositiveInteger representing the lowest RPT event id, or None if not set
        """
        return self.minRptEventId

    def setMinRptEventId(self, value: Optional[PositiveInteger]) -> "RptExecutableEntityProperties":
        """
        Sets the lowest RPT event id usable for RTE generated service points.
        A None value is a no-op and does not overwrite an existing id.

        Args:
            value: The lowest RPT event id to set

        Returns:
            self for method chaining
        """
        if value is not None:
            self.minRptEventId = value
        return self

    def getRptExecutionControl(self) -> Optional[RptExecutionControlEnum]:
        """
        Gets the rapid prototyping control of the executable.

        Returns:
            RptExecutionControlEnum describing the rapid prototyping control, or None if not set
        """
        return self.rptExecutionControl

    def setRptExecutionControl(self, value: Optional[RptExecutionControlEnum]) -> "RptExecutableEntityProperties":
        """
        Sets the rapid prototyping control of the executable.
        A None value is a no-op and does not overwrite an existing control.

        Args:
            value: The RptExecutionControlEnum to set

        Returns:
            self for method chaining
        """
        if value is not None:
            self.rptExecutionControl = value
        return self

    def getRptServicePoint(self) -> Optional[RptServicePointEnum]:
        """
        Gets whether generation of service points by the RTE generator is enabled.

        Returns:
            RptServicePointEnum describing the service point generation, or None if not set
        """
        return self.rptServicePoint

    def setRptServicePoint(self, value: Optional[RptServicePointEnum]) -> "RptExecutableEntityProperties":
        """
        Sets whether generation of service points by the RTE generator is enabled.
        A None value is a no-op and does not overwrite an existing value.

        Args:
            value: The RptServicePointEnum to set

        Returns:
            self for method chaining
        """
        if value is not None:
            self.rptServicePoint = value
        return self
