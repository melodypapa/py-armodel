from typing import List, Optional

from armodel.models.M2.AUTOSARTemplates.CommonStructure.Constants import NumericalOrText
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import ARNumerical, RefType, VerbatimString
from armodel.models.M2.MSR.AsamHdo.Units import SingleLanguageUnitNames
from armodel.models.M2.MSR.DataDictionary.DataDefProperties import ValueList
from armodel.models.M2.MSR.Documentation.TextModel.MultilanguageData import MultilanguageLongName


class SwValues(ARObject):
    """
    This meta-class represents a list of values. These values can either be the input values of a curve (abscissa values) or the associated values (ordinate values). For multidimensional structures, the values are ordered such that they follow the memory layout, see [TPS_SWCT_01882] In particular for maps and cuboids etc. the resulting long value list can be subsectioned using Value Group. But the processing needs to be done as if vg is not there.     Note that numerical values and textual values should not be mixed.
    """

    # SwValues method parity checklist:
    # Spec: AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf, Table 5.125, p.458
    # Spec verified: R23-11
    # Columns: impl / docstring / test / reader / writer   ([—] = no XML element)
    # [x] __init__               [x] impl  [x] docstring  [x] test  [—] reader  [—] writer
    # [x] addV                   [x] impl  [x] docstring  [x] test  [x] reader  [—] writer
    # [x] getVs                  [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] addVf                  [x] impl  [x] docstring  [x] test  [x] reader  [—] writer
    # [x] getVfs                 [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] getVg                  [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] setVg                  [x] impl  [x] docstring  [x] test  [x] reader  [—] writer
    # [x] getVt                  [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] setVt                  [x] impl  [x] docstring  [x] test  [x] reader  [—] writer
    # [x] addVtf                 [x] impl  [x] docstring  [x] test  [x] reader  [—] writer
    # [x] getVtfs                [x] impl  [x] docstring  [x] test  [—] reader  [x] writer

    def __init__(self):
        super().__init__()

        # This is a non variant Value. It is provided for sake of Compatibility to ASAM CDF.
        self.v: List[ARNumerical] = []

        # This allows to specify the value as VariationPoint. It is distinguished to non variant for sake of compatibility to ASAM CDF 2.0.
        self.vf: List[ARNumerical] = []

        # This allows to have intersections in the values in order to support specific rendering (eg. using stylesheets). For tools it is important that the v values are always processed in the same (flattened) order and the tool is able to interpret it without respecting vg.
        self.vg: Optional["ValueGroup"] = None

        # This represents the values of textual data elements (Strings). Note that vt uses the | to separate the values for the different bitfield masks in case that the semantics of the related DataPrototype is described by means of a BITFIELD_TEXTTABLE in the associated CompuMethod.
        self.vt: Optional[VerbatimString] = None

        # This aggregation represents the ability to provide a value that is either numerical or text which existence is subject to variability. From the formal point of view, the aggregation needs to have the multiplicity 1 because SwValues is modelled with stereotype <<atpMixed>>. Nevertheless, the existence of vtf is optional and subject to constraints.
        self.vtf: List[NumericalOrText] = []

    def addV(self, v: Optional[ARNumerical]) -> "SwValues":
        """
        This is a non variant Value. It is provided for sake of Compatibility to ASAM CDF.
        A None value is a no-op and does not append anything.

        Args:
            v: This is a non variant Value. It is provided for sake of Compatibility to ASAM CDF. to append

        Returns:
            SwValues: self for method chaining
        """
        if v is not None:
            self.v.append(v)
        return self

    def getVs(self) -> List[ARNumerical]:
        """
        This is a non variant Value. It is provided for sake of Compatibility to ASAM CDF.

        Returns:
            List[ARNumerical]: The list of non variant Values
        """
        return self.v

    def addVf(self, vf: Optional[ARNumerical]) -> "SwValues":
        """
        This allows to specify the value as VariationPoint. It is distinguished to non variant for sake of compatibility to ASAM CDF 2.0.
        A None value is a no-op and does not append anything.

        Args:
            vf: This allows to specify the value as VariationPoint. It is distinguished to non variant for sake of compatibility to ASAM CDF 2.0. to append

        Returns:
            SwValues: self for method chaining
        """
        if vf is not None:
            self.vf.append(vf)
        return self

    def getVfs(self) -> List[ARNumerical]:
        """
        This allows to specify the value as VariationPoint. It is distinguished to non variant for sake of compatibility to ASAM CDF 2.0.

        Returns:
            List[ARNumerical]: The list of variation point Values
        """
        return self.vf

    def getVg(self) -> Optional["ValueGroup"]:
        """
        This allows to have intersections in the values in order to support specific rendering (eg. using stylesheets). For tools it is important that the v values are always processed in the same (flattened) order and the tool is able to interpret it without respecting vg.

        Returns:
            Optional[ValueGroup]: This allows to have intersections in the values in order to support specific rendering (eg. using stylesheets). For tools it is important that the v values are always processed in the same (flattened) order and the tool is able to interpret it without respecting vg., or None if not set
        """
        return self.vg

    def setVg(self, value: Optional["ValueGroup"]) -> "SwValues":
        """
        This allows to have intersections in the values in order to support specific rendering (eg. using stylesheets). For tools it is important that the v values are always processed in the same (flattened) order and the tool is able to interpret it without respecting vg.
        A None value is a no-op and does not overwrite an existing vg.

        Args:
            value: This allows to have intersections in the values in order to support specific rendering (eg. using stylesheets). For tools it is important that the v values are always processed in the same (flattened) order and the tool is able to interpret it without respecting vg. to set

        Returns:
            SwValues: self for method chaining
        """
        if value is not None:
            self.vg = value
        return self

    def getVt(self) -> Optional[VerbatimString]:
        """
        This represents the values of textual data elements (Strings). Note that vt uses the | to separate the values for the different bitfield masks in case that the semantics of the related DataPrototype is described by means of a BITFIELD_TEXTTABLE in the associated CompuMethod.

        Returns:
            Optional[VerbatimString]: This represents the values of textual data elements (Strings). Note that vt uses the | to separate the values for the different bitfield masks in case that the semantics of the related DataPrototype is described by means of a BITFIELD_TEXTTABLE in the associated CompuMethod., or None if not set
        """
        return self.vt

    def setVt(self, value: Optional[VerbatimString]) -> "SwValues":
        """
        This represents the values of textual data elements (Strings). Note that vt uses the | to separate the values for the different bitfield masks in case that the semantics of the related DataPrototype is described by means of a BITFIELD_TEXTTABLE in the associated CompuMethod.
        A None value is a no-op and does not overwrite an existing vt.

        Args:
            value: This represents the values of textual data elements (Strings). Note that vt uses the | to separate the values for the different bitfield masks in case that the semantics of the related DataPrototype is described by means of a BITFIELD_TEXTTABLE in the associated CompuMethod. to set

        Returns:
            SwValues: self for method chaining
        """
        if value is not None:
            self.vt = value
        return self

    def addVtf(self, vtf: Optional[NumericalOrText]) -> "SwValues":
        """
        This aggregation represents the ability to provide a value that is either numerical or text which existence is subject to variability. From the formal point of view, the aggregation needs to have the multiplicity 1 because SwValues is modelled with stereotype <<atpMixed>>. Nevertheless, the existence of vtf is optional and subject to constraints.
        A None value is a no-op and does not append anything.

        Args:
            vtf: This aggregation represents the ability to provide a value that is either numerical or text which existence is subject to variability. From the formal point of view, the aggregation needs to have the multiplicity 1 because SwValues is modelled with stereotype <<atpMixed>>. Nevertheless, the existence of vtf is optional and subject to constraints. to append

        Returns:
            SwValues: self for method chaining
        """
        if vtf is not None:
            self.vtf.append(vtf)
        return self

    def getVtfs(self) -> List[NumericalOrText]:
        """
        This aggregation represents the ability to provide a value that is either numerical or text which existence is subject to variability. From the formal point of view, the aggregation needs to have the multiplicity 1 because SwValues is modelled with stereotype <<atpMixed>>. Nevertheless, the existence of vtf is optional and subject to constraints.

        Returns:
            List[NumericalOrText]: The list of numerical-or-text values subject to variability
        """
        return self.vtf


class SwValueCont(ARObject):
    """This metaclass represents the content of one particular SwInstance."""

    # SwValueCont method parity checklist:
    # Spec: AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf, Table 5.121, p.450
    # Columns: impl / docstring / test / reader / writer / release   ([—] = no XML element)
    # [x] __init__                     [x] impl  [x] docstring  [x] test  [—] reader  [—] writer  R23-11
    # [x] getSwArraysize               [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setSwArraysize               [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getSwValuesPhys              [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setSwValuesPhys              [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getUnitRef                   [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setUnitRef                   [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getUnitDisplayName           [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setUnitDisplayName           [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # Spec verified: R23-11

    def __init__(self):
        super().__init__()

        # This attribute defines the size of each dimension for compound primitives CURVE, MAP, CUBOID, CUBE_4, CUBE_5, COM_AXIS, RES_AXIS, VAL_BLK. For each dimension one value has to be defined, e.g. one in case of COM_AXIS and two or more in case of MAP. Tags: xml.sequenceOffset=40
        self.swArraysize: Optional[ValueList] = None

        # swValuesPhys represents the values in the physical domain. Tags: xml.sequenceOffset=50
        self.swValuesPhys: Optional[SwValues] = None

        # This represents the physical unit of the provided values. Tags: xml.sequenceOffset=20
        self.unitRef: Optional[RefType] = None

        # This specifies how the physical units of the current value set shall be displayed in documents or in user interfaces of tools. Tags: xml.sequenceOffset=30
        self.unitDisplayName: Optional[SingleLanguageUnitNames] = None

    def getSwArraysize(self) -> Optional[ValueList]:
        """This attribute defines the size of each dimension for compound primitives CURVE, MAP, CUBOID, CUBE_4, CUBE_5, COM_AXIS, RES_AXIS, VAL_BLK. For each dimension one value has to be defined, e.g. one in case of COM_AXIS and two or more in case of MAP. Tags: xml.sequenceOffset=40."""
        return self.swArraysize

    def setSwArraysize(self, value: Optional[ValueList]) -> "SwValueCont":
        """This attribute defines the size of each dimension for compound primitives CURVE, MAP, CUBOID, CUBE_4, CUBE_5, COM_AXIS, RES_AXIS, VAL_BLK. For each dimension one value has to be defined, e.g. one in case of COM_AXIS and two or more in case of MAP. Tags: xml.sequenceOffset=40. A None value is a no-op and does not overwrite an existing swArraysize."""
        if value is not None:
            self.swArraysize = value
        return self

    def getSwValuesPhys(self) -> Optional[SwValues]:
        """swValuesPhys represents the values in the physical domain. Tags: xml.sequenceOffset=50."""
        return self.swValuesPhys

    def setSwValuesPhys(self, value: Optional[SwValues]) -> "SwValueCont":
        """swValuesPhys represents the values in the physical domain. Tags: xml.sequenceOffset=50. A None value is a no-op and does not overwrite an existing swValuesPhys."""
        if value is not None:
            self.swValuesPhys = value
        return self

    def getUnitRef(self) -> Optional[RefType]:
        """This represents the physical unit of the provided values. Tags: xml.sequenceOffset=20."""
        return self.unitRef

    def setUnitRef(self, value: Optional[RefType]) -> "SwValueCont":
        """This represents the physical unit of the provided values. Tags: xml.sequenceOffset=20. A None value is a no-op and does not overwrite an existing unitRef."""
        if value is not None:
            self.unitRef = value
        return self

    def getUnitDisplayName(self) -> Optional[SingleLanguageUnitNames]:
        """This specifies how the physical units of the current value set shall be displayed in documents or in user interfaces of tools. Tags: xml.sequenceOffset=30."""
        return self.unitDisplayName

    def setUnitDisplayName(self, value: Optional[SingleLanguageUnitNames]) -> "SwValueCont":
        """This specifies how the physical units of the current value set shall be displayed in documents or in user interfaces of tools. Tags: xml.sequenceOffset=30. A None value is a no-op and does not overwrite an existing unitDisplayName."""
        if value is not None:
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
