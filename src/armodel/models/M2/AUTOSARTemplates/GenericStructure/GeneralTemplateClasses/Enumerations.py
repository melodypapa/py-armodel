"""
This module contains enumeration classes for AUTOSAR models
in the GenericStructure module. These enumerations are used to specify
various configuration and behavior options throughout the AUTOSAR model.
"""

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import AREnum


class BindingTimeEnum(AREnum):
    """
    This enumerator specifies the applicable binding times for the pre build variation points.
    """

    # BindingTimeEnum method parity checklist:
    # Spec: AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf, Table E.8, p.972
    # Columns: impl / docstring / test / reader / writer / release   ([—] = no XML element)
    # (no methods) — enum value form serialized on AttributeValueVariationPoint.bindingTime + ConditionByFormula.bindingTime (Steps 5/6 N/A: standalone AREnum)

    # • Coding by hand, based on requirements document. • Tool based code generation, e.g. from a model. • The model may contain variants. • Only code for the selected variant(s) is actually generated. Tags: atp.EnumerationLiteralIndex=0
    CODE_GENERATION_TIME = "codeGenerationTime"

    # Configure what is included in object code, and what is omitted Based on which variant(s) are selected E.g. for modules that are delivered as object code (as opposed to those that are delivered as source code) Tags: atp.EnumerationLiteralIndex=1
    LINK_TIME = "linkTime"

    # This is typically the C-Preprocessor. Exclude parts of the code from the compilation process, e.g., because they are not required for the selected variant, because they are incompatible with the selected variant, because they require resources that are not present in the selected variant. Object code is only generated for the selected variant(s). The code that is excluded at this stage code will not be available at later stages. Tags: atp.EnumerationLiteralIndex=2
    PRE_COMPILE_TIME = "preCompileTime"

    # • Designing the VFB. • Software Component types (PortInterfaces). • SWC Prototypes and the Connections between SWCprototypes. • Designing the Topology • ECUs and interconnecting Networks • Designing the Communication Matrix and Data Mapping Tags: atp.EnumerationLiteralIndex=3
    SYSTEM_DESIGN_TIME = "systemDesignTime"

    def __init__(self):
        super().__init__(
            [
                BindingTimeEnum.CODE_GENERATION_TIME,
                BindingTimeEnum.LINK_TIME,
                BindingTimeEnum.PRE_COMPILE_TIME,
                BindingTimeEnum.SYSTEM_DESIGN_TIME,
            ]
        )


class XmlSpaceEnum(AREnum):
    """
    This enumerator specifies the fact that white-space shall be preserved.
    """

    # XmlSpaceEnum method parity checklist:
    # Spec: XSD-only, AUTOSAR_00052.xsd line 145398 (no own table in repo corpus)
    # Columns: impl / docstring / test / reader / writer / release   ([—] = no XML element)
    # (no methods) — enum value form serialized on Sd.xmlSpace (Steps 5/6 N/A: standalone AREnum)
    # [x] __init__     [x] impl  [x] docstring  [x] test  [—] reader  [—] writer  R23-11

    # The value "default" signals that applications' default white-space processing modes are acceptable for this element. Tags: atp.EnumerationLiteralIndex=0
    DEFAULT = "default"
    # the value "preserve" indicates the intent that applications preserve all the white space. Tags: atp.EnumerationLiteralIndex=1
    PRESERVE = "preserve"

    def __init__(self):
        super().__init__((XmlSpaceEnum.DEFAULT, XmlSpaceEnum.PRESERVE))
