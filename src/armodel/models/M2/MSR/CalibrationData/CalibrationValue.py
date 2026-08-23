from typing import List, Optional

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import ARNumerical
from armodel.models.M2.MSR.Documentation.TextModel.MultilanguageData import MultilanguageLongName


class SwValues(ARObject):
    """
    Collection of numerical values for calibration data.
    """

    # SwValues method parity checklist:
    # [ ] __init__                     [x] impl  [ ] docstring  [ ] test
    # [ ] addV                         [x] impl  [ ] docstring  [ ] test
    # [ ] getVs                        [x] impl  [ ] docstring  [ ] test

    def __init__(self):
        super().__init__()

        self._v = []  # type: List[ARNumerical]
        self.vt = None  # type: float
        self.vg: Optional[ValueGroup] = None

    def addV(self, v: ARNumerical):
        self._v.append(v)

    def getVs(self) -> List[ARNumerical]:
        return self._v

    def getVg(self) -> Optional["ValueGroup"]:
        return self.vg

    def setVg(self, value: Optional["ValueGroup"]) -> "SwValues":
        if value is not None:
            self.vg = value
        return self


class SwValueCont(ARObject):
    """
    Container for calibration values with array size, physical values,
    and unit reference.
    """

    # SwValueCont method parity checklist:
    # [ ] __init__                     [x] impl  [ ] docstring  [ ] test
    # [ ] getSwArraysize               [x] impl  [ ] docstring  [ ] test
    # [ ] setSwArraysize               [x] impl  [ ] docstring  [ ] test
    # [ ] getSwValuesPhys              [x] impl  [ ] docstring  [ ] test
    # [ ] setSwValuesPhys              [x] impl  [ ] docstring  [ ] test
    # [ ] getUnitRef                   [x] impl  [ ] docstring  [ ] test
    # [ ] setUnitRef                   [x] impl  [ ] docstring  [ ] test
    # [ ] getUnitDisplayName           [x] impl  [ ] docstring  [ ] test
    # [ ] setUnitDisplayName           [x] impl  [ ] docstring  [ ] test

    def __init__(self):
        super().__init__()

        self.swArraysize = None  # type: ValueList
        self.swValuesPhys = None  # type: SwValues
        self.unitRef = None  # type: RefType
        self.unitDisplayName = None  # type: SingleLanguageUnitNames

    def getSwArraysize(self):
        return self.swArraysize

    def setSwArraysize(self, value):
        self.swArraysize = value
        return self

    def getSwValuesPhys(self):
        return self.swValuesPhys

    def setSwValuesPhys(self, value):
        self.swValuesPhys = value
        return self

    def getUnitRef(self):
        return self.unitRef

    def setUnitRef(self, value):
        self.unitRef = value
        return self

    def getUnitDisplayName(self):
        return self.unitDisplayName

    def setUnitDisplayName(self, value):
        self.unitDisplayName = value
        return self


class ValueGroup(ARObject):
    """
    This element enables values to be grouped. It can be used to perform row and column-orientated groupings, so that these can be rendered properly e.g. as a table.
    """

    # ValueGroup method parity checklist:
    # Spec: AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf, Table 5.126, p.459
    # Spec verified: R23-11
    # Columns: impl / docstring / test / reader / writer   ([—] = no XML element)
    # [x] __init__               [x] impl  [x] docstring  [x] test  [—] reader  [—] writer
    # [x] getLabel               [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] setLabel               [x] impl  [x] docstring  [x] test  [x] reader  [—] writer
    # [x] getVgContents          [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] setVgContents          [x] impl  [x] docstring  [x] test  [x] reader  [—] writer

    def __init__(self):
        super().__init__()

        # This label allows to give the valueGroup a particular name. It can be used if the Values are rendered as a table.
        self.label: Optional[MultilanguageLongName] = None

        # This represents the contents of the value group.
        self.vgContents: Optional[SwValues] = None

    def getLabel(self) -> Optional[MultilanguageLongName]:
        """
        This label allows to give the valueGroup a particular name. It can be used if the Values are rendered as a table.

        Returns:
            Optional[MultilanguageLongName]: This label allows to give the valueGroup a particular name. It can be used if the Values are rendered as a table., or None if not set
        """
        return self.label

    def setLabel(self, value: Optional[MultilanguageLongName]) -> "ValueGroup":
        """
        This label allows to give the valueGroup a particular name. It can be used if the Values are rendered as a table.
        A None value is a no-op and does not overwrite an existing label.

        Args:
            value: This label allows to give the valueGroup a particular name. It can be used if the Values are rendered as a table. to set

        Returns:
            ValueGroup: self for method chaining
        """
        if value is not None:
            self.label = value
        return self

    def getVgContents(self) -> Optional[SwValues]:
        """
        This represents the contents of the value group.

        Returns:
            Optional[SwValues]: This represents the contents of the value group., or None if not set
        """
        return self.vgContents

    def setVgContents(self, value: Optional[SwValues]) -> "ValueGroup":
        """
        This represents the contents of the value group.
        A None value is a no-op and does not overwrite an existing vgContents.

        Args:
            value: This represents the contents of the value group. to set

        Returns:
            ValueGroup: self for method chaining
        """
        if value is not None:
            self.vgContents = value
        return self
