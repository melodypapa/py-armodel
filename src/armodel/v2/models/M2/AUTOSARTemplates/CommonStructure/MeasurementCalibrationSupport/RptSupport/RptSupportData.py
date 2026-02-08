from typing import List, Union

from armodel.v2.models.M2.AUTOSARTemplates.CommonStructure.MeasurementCalibrationSupport.RptSupport.RptEnablerImplTypeEnum import (
    RptEnablerImplTypeEnum,
)
from armodel.v2.models.M2.AUTOSARTemplates.CommonStructure.MeasurementCalibrationSupport.RptSupport.RptExecutionControlEnum import (
    RptExecutionControlEnum,
)
from armodel.v2.models.M2.AUTOSARTemplates.CommonStructure.MeasurementCalibrationSupport.RptSupport.RptPreparationEnum import (
    RptPreparationEnum,
)
from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import (
    ARObject,
)
from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    RefType,
)


class RptSupportData(ARObject):
    """
    Represents RPT support data in AUTOSAR.
    Defines data structures for supporting read-protect-transform functionality.
    """


    def __init__(self) -> None:
        """
        Initializes the RptSupportData with default values.
        """
        super().__init__()
        self.rptComponents: List[RefType] = []
        self.rptEnablerImplType: Union[Union[RptEnablerImplTypeEnum, None] , None] = None
        self.rptExecutionControl: Union[Union[RptExecutionControlEnum, None] , None] = None
        self.rptPreparation: Union[Union[RptPreparationEnum, None] , None] = None

    def addRptComponent(self, ref: RefType):
        """
        Adds an RPT component reference.

        Args:
            ref: The RPT component reference to add

        Returns:
            self for method chaining
        """
        self.rptComponents.append(ref)
        return self

    def getRptComponents(self) -> List[RefType]:
        """
        Gets the list of RPT component references.

        Returns:
            List of RPT component references
        """
        return self.rptComponents

    def getRptEnablerImplType(self) -> Union[RptEnablerImplTypeEnum, None]:
        """
        Gets the RPT enabler implementation type.

        Returns:
            RPT enabler implementation type enum value
        """
        return self.rptEnablerImplType

    def setRptEnablerImplType(self, value: RptEnablerImplTypeEnum) -> "RptSupportData":
        """
        Sets the RPT enabler implementation type.

        Args:
            value: RPT enabler implementation type enum value to set

        Returns:
            self for method chaining
        """
        self.rptEnablerImplType = value
        return self

    def getRptExecutionControl(self) -> Union[RptExecutionControlEnum, None]:
        """
        Gets the RPT execution control type.

        Returns:
            RPT execution control enum value
        """
        return self.rptExecutionControl

    def setRptExecutionControl(self, value: RptExecutionControlEnum) -> "RptSupportData":
        """
        Sets the RPT execution control type.

        Args:
            value: RPT execution control enum value to set

        Returns:
            self for method chaining
        """
        self.rptExecutionControl = value
        return self

    def getRptPreparation(self) -> Union[RptPreparationEnum, None]:
        """
        Gets the RPT preparation type.

        Returns:
            RPT preparation enum value
        """
        return self.rptPreparation

    def setRptPreparation(self, value: RptPreparationEnum) -> "RptSupportData":
        """
        Sets the RPT preparation type.

        Args:
            value: RPT preparation enum value to set

        Returns:
            self for method chaining
        """
        self.rptPreparation = value
        return self
