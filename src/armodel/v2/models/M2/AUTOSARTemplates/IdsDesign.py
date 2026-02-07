from typing import List


class IdsDesign(ARElement):
    """
    This meta-class represents the root element of a SecurityExtract file for
    IDS development. It defines the scope of an IDS to be designed and
    implemented by referencing all SecurityExtract meta-classes that need to be
    included into the IDS development process.

    Package: M2::AUTOSARTemplates::SecurityExtractTemplate::IdsDesign

    Sources:
      - AUTOSAR_FO_TPS_SecurityExtractTemplate.pdf (Page 16, Foundation R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # This reference includes an element with IDS related the IdsDesign.
        # atpVariation.
        self._element: List["IdsCommonElement"] = []

    @property
    def element(self) -> List["IdsCommonElement"]:
        """Get element (Pythonic accessor)."""
        return self._element

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getElement(self) -> List["IdsCommonElement"]:
        """
        AUTOSAR-compliant getter for element.

        Returns:
            The element value

        Note:
            Delegates to element property (CODING_RULE_V2_00017)
        """
        return self.element  # Delegates to property

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====
