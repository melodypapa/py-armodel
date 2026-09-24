from typing import Optional

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ARPackage import ARElement
from armodel.models.M2.MSR.DataDictionary.DataDefProperties import SwDataDefProps


class SwSystemconst(ARElement):
    """
    This element defines a system constant which serves an input to select a particular variation point. In particular a system constant serves as an operand of the binding function (swSyscond) in a Variation point. Note that the binding process can only happen if a value was assigned to to the referenced system constants. Tags: atp.recommendedPackage=SwSystemconsts
    """

    # SwSystemconst method parity checklist:
    # Spec: AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf, Table 5.120, p.448
    # Columns: impl / docstring / test / reader / writer / release   ([—] = no XML element)
    # [x] __init__            [x] impl  [x] docstring  [x] test  [—] reader  [—] writer  R23-11
    # [x] getSwDataDefProps   [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setSwDataDefProps   [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11

    def __init__(self, parent, short_name: str):
        super().__init__(parent, short_name)

        # This denotes the data definition properties of the system constant. This supports to express the limits and optionally a conversion within the internal to physical values by a compu method. Stereotypes: atpSplitable Tags: atp.Splitkey=swDataDefProps xml.sequenceOffset=40
        self.swDataDefProps: Optional[SwDataDefProps] = None

    def getSwDataDefProps(self) -> Optional[SwDataDefProps]:
        """
        This denotes the data definition properties of the system constant. This supports to express the limits and optionally a conversion within the internal to physical values by a compu method. Stereotypes: atpSplitable Tags: atp.Splitkey=swDataDefProps xml.sequenceOffset=40.
        """
        return self.swDataDefProps

    def setSwDataDefProps(self, sw_data_def_props: Optional[SwDataDefProps]) -> "SwSystemconst":
        """
        This denotes the data definition properties of the system constant. This supports to express the limits and optionally a conversion within the internal to physical values by a compu method. Stereotypes: atpSplitable Tags: atp.Splitkey=swDataDefProps xml.sequenceOffset=40.
        A None value is a no-op and does not overwrite an existing swDataDefProps.
        """
        if sw_data_def_props is not None:
            self.swDataDefProps = sw_data_def_props

        return self
