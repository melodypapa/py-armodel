from typing import Optional

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import PositiveInteger, RefType


class PrivacyLevel(ARObject):
    """
    This meta-class defines the Privacy Level for a Log and Trace content.

    [constr_5340] Range of DltMessage.privacyLevel.privacyLevel: The value of DltMessage.privacyLevel.privacyLevel shall be in the range between 0 and 255.

    [constr_5341] Range of PrivacyLevel.compuMethod: The CompuMethod that is referenced from PrivacyLevel in the role compuMethod shall have the category TEXTTABLE.
    """

    # PrivacyLevel method parity checklist:
    # Spec: AUTOSAR_FO_TPS_LogAndTraceExtract.pdf, Table 3.4, p.18
    # Columns: impl / docstring / test / reader / writer / release   ([—] = no XML element)
    # [x] __init__           [x] impl  [x] docstring  [x] test  [—] reader  [—] writer  R23-11
    # [x] getCompuMethodRef  [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setCompuMethodRef  [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getPrivacyLevel    [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setPrivacyLevel    [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11

    def __init__(self):
        super().__init__()

        # Reference to CompuMethod of category TEXTTABLE that defines the supported user-defined privacy levels.
        self.compuMethodRef: Optional[RefType] = None

        # The value that represents the privacy level and is transported in the Extension Header.
        self.privacyLevel: Optional[PositiveInteger] = None

    def getCompuMethodRef(self) -> Optional[RefType]:
        """
        Reference to CompuMethod of category TEXTTABLE that defines the supported user-defined privacy levels.
        """
        return self.compuMethodRef

    def setCompuMethodRef(self, value: Optional[RefType]) -> "PrivacyLevel":
        """
        Reference to CompuMethod of category TEXTTABLE that defines the supported user-defined privacy levels.

        A None value is a no-op and does not overwrite an existing compuMethodRef.
        """
        if value is not None:
            self.compuMethodRef = value
        return self

    def getPrivacyLevel(self) -> Optional[PositiveInteger]:
        """
        The value that represents the privacy level and is transported in the Extension Header.
        """
        return self.privacyLevel

    def setPrivacyLevel(self, value: Optional[PositiveInteger]) -> "PrivacyLevel":
        """
        The value that represents the privacy level and is transported in the Extension Header.

        A None value is a no-op and does not overwrite an existing privacyLevel.
        """
        if value is not None:
            self.privacyLevel = value
        return self
