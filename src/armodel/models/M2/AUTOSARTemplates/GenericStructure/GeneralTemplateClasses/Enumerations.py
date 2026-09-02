"""
This module contains enumeration classes for AUTOSAR models
in the GenericStructure module. These enumerations are used to specify
various configuration and behavior options throughout the AUTOSAR model.
"""

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import AREnum


class BindingTimeEnum(AREnum):
    """
    Enumeration for binding time in AUTOSAR variant handling.

    This class specifies the point in time when a variant condition
    may be evaluated at earliest. At this point in time, all referenced
    system constants shall have a value.

    Package: M2::AUTOSARTemplates::GenericStructure::VariantHandling
    """

    # BindingTimeEnum method parity checklist:
    # [ ] __init__                     [x] impl  [ ] docstring  [ ] test

    def __init__(self):
        super().__init__(["codeGenerationTime", "linkTime", "preCompileTime", "systemDesignTime"])


class XmlSpaceEnum(AREnum):
    """
    This attribute is used to signal an intention that in that element, white space
    should be preserved by applications. It is defined according to xml:space as
    declared by W3C.
    """

    # XmlSpaceEnum method parity checklist:
    # (no methods) — enum value form serialized on Sd.xmlSpace; XSD-only (no Enumeration table)
    # [ ] __init__     [x] impl  [ ] docstring  [ ] test  [—] reader  [—] writer

    # The value "default" signals that applications' default white-space processing modes are acceptable for this element. Tags: atp.EnumerationValue=0
    DEFAULT = "default"
    # the value "preserve" indicates the intent that applications preserve all the white space. Tags: atp.EnumerationValue=1
    PRESERVE = "preserve"

    def __init__(self):
        super().__init__((XmlSpaceEnum.DEFAULT, XmlSpaceEnum.PRESERVE))
