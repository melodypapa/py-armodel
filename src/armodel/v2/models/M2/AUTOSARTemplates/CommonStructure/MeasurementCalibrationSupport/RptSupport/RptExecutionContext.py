from typing import Union

from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import (
        ARObject,
    )
from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    RefType,
)


class RptExecutionContext(ARObject):
    """
    Package: M2::AUTOSARTemplates::CommonStructure::MeasurementCalibrationSupport::RptSupport
    Represents an RPT execution context in AUTOSAR.
    Defines the execution context for RPT functionality.
    """


    def __init__(self) -> None:
        """
        Initializes the RptExecutionContext with default values.
        """
        super().__init__()
        self.contextRef: Union[Union[RefType, None] , None] = None

    def getContextRef(self) -> Union[RefType, None]:
        """
        Gets the context reference.

        Returns:
            Reference to the context
        """
        return self.contextRef

    def setContextRef(self, value: RefType) -> "RptExecutionContext":
        """
        Sets the context reference.

        Args:
            value: The context reference to set

        Returns:
            self for method chaining
        """
        self.contextRef = value
        return self
