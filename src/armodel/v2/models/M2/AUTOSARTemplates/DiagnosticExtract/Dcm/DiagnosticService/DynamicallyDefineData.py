"""
AUTOSAR Package - DynamicallyDefineData

Package: M2::AUTOSARTemplates::DiagnosticExtract::Dcm::DiagnosticService::DynamicallyDefineData
"""

from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    AREnum,
)


class DiagnosticHandleDDDIConfigurationEnum(AREnum):
    """
    DiagnosticHandleDDDIConfigurationEnum enumeration

This meta-class represents the options for controlling how the configuration of the DynamicallyDefine DataIdentifiers is done in the given context. Aggregated by DiagnosticDynamicallyDefineDataIdentifierClass.configurationHandling

Package: M2::AUTOSARTemplates::DiagnosticExtract::Dcm::DiagnosticService::DynamicallyDefineData
    """
    # This indicates that the configuration of DynamicallyDefineDataIdentifier shall be stored as non-volatile
    nonVolatile = "0"

    # This indicates that the configuration of DynamicallyDefineDataIdentifier shall be handled as volatile
    volatile = "1"



class DiagnosticDynamicallyDefineDataIdentifierSubfunctionEnum(AREnum):
    """
    DiagnosticDynamicallyDefineDataIdentifierSubfunctionEnum enumeration

This meta-class contains a list of possible subfunctions for the UDS service 0x2C. Aggregated by DiagnosticDynamicallyDefineDataIdentifierClass.subfunction

Package: M2::AUTOSARTemplates::DiagnosticExtract::Dcm::DiagnosticService::DynamicallyDefineData
    """
    # Clear the specified dynamic data identifier.
    clearDynamicallyDefineDataIdentifier = "0"

    # The definition of dynamic data identifier shall be done via a reference to a diagnostic data identifier.
    defineByIdentifier = "1"

    # The definition of dynamic data identifier shall be done via a reference to a memory address.
    defineByMemoryAddress = "2"
