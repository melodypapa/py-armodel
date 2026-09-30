from abc import ABC
from typing import List, Optional

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    AREnum,
    Boolean,
    Limit,
    PositiveInteger,
    RegularExpression,
)


class FullBindingTimeEnum(AREnum):
    """
    This enumeration specifies the BindingTimes that can be used in AUTOSAR models.
    """

    # FullBindingTimeEnum method parity checklist:
    # Spec: AUTOSAR_FO_TPS_GenericStructureTemplate.pdf, Table 4.39, p.105
    # Columns: impl / docstring / test / reader / writer / release   ([—] = no XML element)
    # (no methods) — enum value form serialized on AbstractVariationRestriction.validBindingTimes (VALID-BINDING-TIME elements)
    # [x] __init__  [x] impl  [x] docstring  [x] test  [—] reader  [—] writer  R23-11

    # The point in time when an object is created from a blueprint. Tags: atp.EnumerationLiteralIndex=0
    BLUEPRINT_DERIVATION_TIME = "BLUEPRINT-DERIVATION-TIME"

    # • Designing the VFB. • Software Component types (PortInterfaces). • SWC Prototypes and the Connections between SWCprototypes. • Designing the Topology • ECUs and interconnecting Networks • Designing the Communication Matrix and Data Mapping Tags: atp.EnumerationLiteralIndex=1
    SYSTEM_DESIGN_TIME = "SYSTEM-DESIGN-TIME"

    # • Coding by hand, based on requirements document. • Tool based code generation, e.g. from a model. • The model may contain variants. • Only code for the selected variant(s) is actually generated. Tags: atp.EnumerationLiteralIndex=2
    CODE_GENERATION_TIME = "CODE-GENERATION-TIME"

    # This is typically the C-Preprocessor. Exclude parts of the code from the compilation process, e.g., because they are not required for the selected variant, because they are incompatible with the selected variant, because they require resources that are not present in the selected variant. Object code is only generated for the selected variant(s). The code that is excluded at this stage code will not be available at later stages. Tags: atp.EnumerationLiteralIndex=3
    PRE_COMPILE_TIME = "PRE-COMPILE-TIME"

    # Configure what is included in object code, and what is omitted Based on which variant(s) are selected E.g. for modules that are delivered as object code (as opposed to those that are delivered as source code) Tags: atp.EnumerationLiteralIndex=4
    LINK_TIME = "LINK-TIME"

    # PostBuild is the binding time which is bound latest at startup of the ECU. In other words this is everything between creation of the executable program and startup of the ECU. Tags: atp.EnumerationLiteralIndex=5
    POST_BUILD = "POST-BUILD"

    def __init__(self):
        super().__init__(
            (
                FullBindingTimeEnum.BLUEPRINT_DERIVATION_TIME,
                FullBindingTimeEnum.SYSTEM_DESIGN_TIME,
                FullBindingTimeEnum.CODE_GENERATION_TIME,
                FullBindingTimeEnum.PRE_COMPILE_TIME,
                FullBindingTimeEnum.LINK_TIME,
                FullBindingTimeEnum.POST_BUILD,
            )
        )


class AbstractValueRestriction(ARObject, ABC):
    """
    Restricts primitive values. A value is valid if all rules that are defined by this restriction evaluate to true.
    """

    # AbstractValueRestriction method parity checklist:
    # Spec: AUTOSAR_FO_TPS_GenericStructureTemplate.pdf, Table 4.37, p.103
    # Columns: impl / docstring / test / reader / writer / release   ([—] = no XML element)
    # [x] __init__         [x] impl  [x] docstring  [x] test  [x] reader  [x] writer  R23-11
    # [x] getMax           [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setMax           [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getMaxLength     [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setMaxLength     [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getMin           [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setMin           [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getMinLength     [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setMinLength     [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getPattern       [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setPattern       [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11

    def __init__(self):
        if type(self) is AbstractValueRestriction:
            raise TypeError("AbstractValueRestriction is an abstract class.")

        super().__init__()

        # Specifies the upper bounds for numeric values.
        self.max: Optional[Limit] = None

        # Specifies the maximum number of characters of textual values.
        self.maxLength: Optional[PositiveInteger] = None

        # Specifies the lower bounds for numeric values.
        self.min: Optional[Limit] = None

        # Specifies the minimal number of characters of textual values.
        self.minLength: Optional[PositiveInteger] = None

        # Defines the exact sequence of characters that are acceptable.
        self.pattern: Optional[RegularExpression] = None

    def getMax(self) -> Optional[Limit]:
        """
        Specifies the upper bounds for numeric values.

        Returns:
            The upper bound limit, or None if not set
        """
        return self.max

    def setMax(self, value: Optional[Limit]):
        """
        Specifies the upper bounds for numeric values.

        Args:
            value: The upper bound limit to set

        Returns:
            self for method chaining
        """
        self.max = value
        return self

    def getMaxLength(self) -> Optional[PositiveInteger]:
        """
        Specifies the maximum number of characters of textual values.

        Returns:
            The maximum length, or None if not set
        """
        return self.maxLength

    def setMaxLength(self, value: Optional[PositiveInteger]):
        """
        Specifies the maximum number of characters of textual values.

        Args:
            value: The maximum length to set

        Returns:
            self for method chaining
        """
        self.maxLength = value
        return self

    def getMin(self) -> Optional[Limit]:
        """
        Specifies the lower bounds for numeric values.

        Returns:
            The lower bound limit, or None if not set
        """
        return self.min

    def setMin(self, value: Optional[Limit]):
        """
        Specifies the lower bounds for numeric values.

        Args:
            value: The lower bound limit to set

        Returns:
            self for method chaining
        """
        self.min = value
        return self

    def getMinLength(self) -> Optional[PositiveInteger]:
        """
        Specifies the minimal number of characters of textual values.

        Returns:
            The minimum length, or None if not set
        """
        return self.minLength

    def setMinLength(self, value: Optional[PositiveInteger]):
        """
        Specifies the minimal number of characters of textual values.

        Args:
            value: The minimum length to set

        Returns:
            self for method chaining
        """
        self.minLength = value
        return self

    def getPattern(self) -> Optional[RegularExpression]:
        """
        Defines the exact sequence of characters that are acceptable.

        Returns:
            The regular expression pattern, or None if not set
        """
        return self.pattern

    def setPattern(self, value: Optional[RegularExpression]):
        """
        Defines the exact sequence of characters that are acceptable.

        Args:
            value: The regular expression pattern to set

        Returns:
            self for method chaining
        """
        self.pattern = value
        return self


class ValueRestrictionWithSeverity(AbstractValueRestriction):
    pass


class AbstractVariationRestriction(ARObject, ABC):
    """
    Defines constraints on the usage of variation and on the valid binding times.
    """

    # AbstractVariationRestriction method parity checklist:
    # Spec: AUTOSAR_FO_TPS_GenericStructureTemplate.pdf, Table 4.38, p.104
    # Columns: impl / docstring / test / reader / writer / release   ([—] = no XML element)
    # [x] __init__              [x] impl  [x] docstring  [x] test  [x] reader  [x] writer  R23-11
    # [x] getVariation          [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setVariation          [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getValidBindingTimes  [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setValidBindingTimes  [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] addValidBindingTime   [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11

    def __init__(self):
        if type(self) is AbstractVariationRestriction:
            raise TypeError("AbstractVariationRestriction is an abstract class.")

        super().__init__()

        # Defines if the AUTOSAR model may define a Variation Point at this location. Tags: xml.sequenceOffset=10
        self.variation: Optional[Boolean] = None

        # List of valid binding times. Tags: xml.sequenceOffset=20
        self.validBindingTimes: List[FullBindingTimeEnum] = []

    def getVariation(self) -> Optional[Boolean]:
        """
        Defines if the AUTOSAR model may define a Variation Point at this location.

        Returns:
            The variation flag, or None if not set
        """
        return self.variation

    def setVariation(self, value: Optional[Boolean]):
        """
        Defines if the AUTOSAR model may define a Variation Point at this location.

        Args:
            value: The variation flag to set

        Returns:
            self for method chaining
        """
        self.variation = value
        return self

    def getValidBindingTimes(self) -> List[FullBindingTimeEnum]:
        """
        List of valid binding times.

        Returns:
            The list of valid binding times
        """
        return self.validBindingTimes

    def setValidBindingTimes(self, values: List[FullBindingTimeEnum]):
        """
        List of valid binding times.

        Args:
            values: The list of valid binding times to set

        Returns:
            self for method chaining
        """
        self.validBindingTimes = values
        return self

    def addValidBindingTime(self, value: FullBindingTimeEnum):
        """
        List of valid binding times.

        Args:
            value: The valid binding time to append

        Returns:
            self for method chaining
        """
        self.validBindingTimes.append(value)
        return self


class VariationRestrictionWithSeverity(AbstractVariationRestriction):
    pass
