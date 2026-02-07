from abc import ABC, abstractmethod
from typing import List, Optional, Dict, Any
from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import ARObject

class FormulaExpression(ARObject, ABC):
    """
    This class represents the syntax of the formula language. The class is
    modeled as an abstract class in order to be specialized into particular use
    cases. For each use case the referable objects might be specified in the
    specialization.
    
    Package: M2::AUTOSARTemplates::GenericStructure::FormulaLanguage::FormulaExpression
    
    Sources:
      - AUTOSAR_CP_TPS_TimingExtensions.pdf (Page 223, Classic Platform R23-11)
      - AUTOSAR_FO_TPS_FeatureModelExchangeFormat.pdf (Page 73, Foundation
      R23-11)
      - AUTOSAR_FO_TPS_GenericStructureTemplate.pdf (Page 448, Foundation
      R23-11)
    """
    def __init__(self):
        if type(self) is FormulaExpression:
            raise TypeError("FormulaExpression is an abstract class.")
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # The referable object shall yield a numerical / boolean.
        self._atpReference: List[RefType] = []

    @property
    def atp_reference(self) -> List[RefType]:
        """Get atpReference (Pythonic accessor)."""
        return self._atpReference
        # The referable object shall yield a string value.
        # atpAbstract.
        self._atpString: List[RefType] = []

    @property
    def atp_string(self) -> List[RefType]:
        """Get atpString (Pythonic accessor)."""
        return self._atpString

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getAtpReference(self) -> List[RefType]:
        """
        AUTOSAR-compliant getter for atpReference.
        
        Returns:
            The atpReference value
        
        Note:
            Delegates to atp_reference property (CODING_RULE_V2_00017)
        """
        return self.atp_reference  # Delegates to property

    def getAtpString(self) -> List[RefType]:
        """
        AUTOSAR-compliant getter for atpString.
        
        Returns:
            The atpString value
        
        Note:
            Delegates to atp_string property (CODING_RULE_V2_00017)
        """
        return self.atp_string  # Delegates to property

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====