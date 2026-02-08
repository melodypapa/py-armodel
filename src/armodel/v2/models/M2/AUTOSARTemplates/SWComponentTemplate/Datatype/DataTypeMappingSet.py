from typing import List

from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ARPackage import (
    ARElement,
)


class DataTypeMappingSet(ARElement):
    """
    This class represents a list of mappings between ApplicationDataTypes and
    ImplementationDataTypes. In addition, it can contain mappings between
    ImplementationDataTypes and ModeDeclarationGroups.

    Package: M2::AUTOSARTemplates::SWComponentTemplate::Datatype::Datatypes

    Sources:
      - AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.pdf (Page 311, Classic
      Platform R23-11)
      - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (Page 234, Classic Platform
      R23-11)
      - AUTOSAR_CP_TPS_SystemTemplate.pdf (Page 2015, Classic Platform R23-11)
      - AUTOSAR_FO_TPS_StandardizationTemplate.pdf (Page 180, Foundation R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # This is one particular association between an Application its
        # AbstractImplementationDataType.
        self._dataTypeMap: List["DataTypeMap"] = []

    @property
    def data_type_map(self) -> List["DataTypeMap"]:
        """Get dataTypeMap (Pythonic accessor)."""
        return self._dataTypeMap
        # This is one particular association between an Mode and its
        # AbstractImplementationData.
        self._modeRequest: List["ModeRequestTypeMap"] = []

    @property
    def mode_request(self) -> List["ModeRequestTypeMap"]:
        """Get modeRequest (Pythonic accessor)."""
        return self._modeRequest

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getDataTypeMap(self) -> List["DataTypeMap"]:
        """
        AUTOSAR-compliant getter for dataTypeMap.

        Returns:
            The dataTypeMap value

        Note:
            Delegates to data_type_map property (CODING_RULE_V2_00017)
        """
        return self.data_type_map  # Delegates to property

    def getModeRequest(self) -> List["ModeRequestTypeMap"]:
        """
        AUTOSAR-compliant getter for modeRequest.

        Returns:
            The modeRequest value

        Note:
            Delegates to mode_request property (CODING_RULE_V2_00017)
        """
        return self.mode_request  # Delegates to property

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====
