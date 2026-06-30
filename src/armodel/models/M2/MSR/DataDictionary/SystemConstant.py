from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import (
    ARObject,
)

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable import Identifiable
from armodel.models.M2.MSR.DataDictionary.DataDefProperties import SwDataDefProps


class SwSystemconst(Identifiable):
    """
    Represents a software system constant in the AUTOSAR model.

    This class is used to define system constants that are used throughout
    the software configuration.

    Attributes:
        value (ValueSpecification): The value of the system constant.
    """

    def __init__(self, parent, short_name: str):
        super().__init__(parent, short_name)

        self.swDataDefProps: SwDataDefProps = None

    def setSwDataDefProps(self, sw_data_def_props: SwDataDefProps):
        """
        Sets the software data definition properties for this system constant.

        Args:
            sw_data_def_props (SwDataDefProps): The software data definition properties to set.
        """
        self.swDataDefProps = sw_data_def_props

        return self

    def getSwDataDefProps(self) -> SwDataDefProps:
        """
        Returns the software data definition properties for this system constant.

        Returns:
            SwDataDefProps: The software data definition properties.
        """
        return self.swDataDefProps
    
