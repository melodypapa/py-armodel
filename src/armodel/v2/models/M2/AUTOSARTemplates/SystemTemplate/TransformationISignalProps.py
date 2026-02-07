from abc import ABC, abstractmethod
from typing import List, Optional, Dict, Any
from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import ARObject

class TransformationISignalProps(ARObject, ABC):
    """
    TransformationISignalProps holds all the attributes for the different
    TransformationTechnologies that are ISignal specific. Tags:
    vh.latestBindingTime=postBuild
    
    Package: M2::AUTOSARTemplates::SystemTemplate::Transformer::TransformationISignalProps
    
    Sources:
      - AUTOSAR_CP_TPS_SystemTemplate.pdf (Page 772, Classic Platform R23-11)
    """
    def __init__(self):
        if type(self) is TransformationISignalProps:
            raise TypeError("TransformationISignalProps is an abstract class.")
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # Defines whether the transformer chain of client/server coordinates an
        # autonomous error reaction the RTE or whether any error reaction is the the
        # application.
        self._csErrorReaction: Optional["CSTransformerError"] = None

    @property
    def cs_error_reaction(self) -> Optional["CSTransformerError"]:
        """Get csErrorReaction (Pythonic accessor)."""
        return self._csErrorReaction

    @cs_error_reaction.setter
    def cs_error_reaction(self, value: Optional["CSTransformerError"]) -> None:
        """
        Set csErrorReaction with validation.
        
        Args:
            value: The csErrorReaction to set
        
        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._csErrorReaction = None
            return

        if not isinstance(value, CSTransformerError):
            raise TypeError(
                f"csErrorReaction must be CSTransformerError or None, got {type(value).__name__}"
            )
        self._csErrorReaction = value
        # Fine granular modeling of TransfromationProps on the level of DataPrototypes.
        # This atpSplitable property has no atp.
        # Splitkey due (PropertySetPattern).
        self._dataPrototype: List[RefType] = []

    @property
    def data_prototype(self) -> List[RefType]:
        """Get dataPrototype (Pythonic accessor)."""
        return self._dataPrototype
        # Reference to the TransformationTechnology description contains transformer
        # specific and ISignal properties.
        self._transformer: Optional["Transformation"] = None

    @property
    def transformer(self) -> Optional["Transformation"]:
        """Get transformer (Pythonic accessor)."""
        return self._transformer

    @transformer.setter
    def transformer(self, value: Optional["Transformation"]) -> None:
        """
        Set transformer with validation.
        
        Args:
            value: The transformer to set
        
        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._transformer = None
            return

        if not isinstance(value, Transformation):
            raise TypeError(
                f"transformer must be Transformation or None, got {type(value).__name__}"
            )
        self._transformer = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getCsErrorReaction(self) -> "CSTransformerError":
        """
        AUTOSAR-compliant getter for csErrorReaction.
        
        Returns:
            The csErrorReaction value
        
        Note:
            Delegates to cs_error_reaction property (CODING_RULE_V2_00017)
        """
        return self.cs_error_reaction  # Delegates to property

    def setCsErrorReaction(self, value: "CSTransformerError") -> "TransformationISignalProps":
        """
        AUTOSAR-compliant setter for csErrorReaction with method chaining.
        
        Args:
            value: The csErrorReaction to set
        
        Returns:
            self for method chaining
        
        Note:
            Delegates to cs_error_reaction property setter (gets validation automatically)
        """
        self.cs_error_reaction = value  # Delegates to property setter
        return self

    def getDataPrototype(self) -> List[RefType]:
        """
        AUTOSAR-compliant getter for dataPrototype.
        
        Returns:
            The dataPrototype value
        
        Note:
            Delegates to data_prototype property (CODING_RULE_V2_00017)
        """
        return self.data_prototype  # Delegates to property

    def getTransformer(self) -> "Transformation":
        """
        AUTOSAR-compliant getter for transformer.
        
        Returns:
            The transformer value
        
        Note:
            Delegates to transformer property (CODING_RULE_V2_00017)
        """
        return self.transformer  # Delegates to property

    def setTransformer(self, value: "Transformation") -> "TransformationISignalProps":
        """
        AUTOSAR-compliant setter for transformer with method chaining.
        
        Args:
            value: The transformer to set
        
        Returns:
            self for method chaining
        
        Note:
            Delegates to transformer property setter (gets validation automatically)
        """
        self.transformer = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_cs_error_reaction(self, value: Optional["CSTransformerError"]) -> "TransformationISignalProps":
        """
        Set csErrorReaction and return self for chaining.
        
        Args:
            value: The csErrorReaction to set
        
        Returns:
            self for method chaining
        
        Example:
            >>> obj.with_cs_error_reaction("value")
        """
        self.cs_error_reaction = value  # Use property setter (gets validation)
        return self

    def with_transformer(self, value: Optional["Transformation"]) -> "TransformationISignalProps":
        """
        Set transformer and return self for chaining.
        
        Args:
            value: The transformer to set
        
        Returns:
            self for method chaining
        
        Example:
            >>> obj.with_transformer("value")
        """
        self.transformer = value  # Use property setter (gets validation)
        return self