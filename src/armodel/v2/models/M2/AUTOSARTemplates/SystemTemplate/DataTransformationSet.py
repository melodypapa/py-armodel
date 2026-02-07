from typing import List


class DataTransformationSet(ARElement):
    """
    This element is the system wide container of DataTransformations which
    represent transformer chains.

    Package: M2::AUTOSARTemplates::SystemTemplate::Transformer::DataTransformationSet

    Sources:
      - AUTOSAR_CP_TPS_SystemTemplate.pdf (Page 762, Classic Platform R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # This container consists of all transformer chains which be used for
                # transformation of data communication.
        # atpVariation.
        self._data: List["DataTransformation"] = []

    @property
    def data(self) -> List["DataTransformation"]:
        """Get data (Pythonic accessor)."""
        return self._data
        # Transformer that is used in a transformer chain for transformation of data
                # communication.
        # atpVariation.
        self._transformation: List["Transformation"] = []

    @property
    def transformation(self) -> List["Transformation"]:
        """Get transformation (Pythonic accessor)."""
        return self._transformation

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getData(self) -> List["DataTransformation"]:
        """
        AUTOSAR-compliant getter for data.

        Returns:
            The data value

        Note:
            Delegates to data property (CODING_RULE_V2_00017)
        """
        return self.data  # Delegates to property

    def getTransformation(self) -> List["Transformation"]:
        """
        AUTOSAR-compliant getter for transformation.

        Returns:
            The transformation value

        Note:
            Delegates to transformation property (CODING_RULE_V2_00017)
        """
        return self.transformation  # Delegates to property

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====
