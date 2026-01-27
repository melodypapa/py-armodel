"""
This module contains classes for representing AUTOSAR hardware attribute values
in the EcuResourceTemplate module.
"""

from typing import Optional

from ....M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import RefType
from ....M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable import Identifiable
from ....M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import ARObject


class HwAttributeValue(ARObject):
    """
    Represents a hardware attribute value in AUTOSAR hardware descriptions.
    This class defines the actual values assigned to hardware attributes in the model.
    """
    
    def __init__(self):
        """
        Initializes the HwAttributeValue.
        """
        super().__init__()

        self.hwAttributeDefRef: Optional[RefType] = None
        self.value: Optional[str] = None

    def getHwAttributeDefRef(self) -> Optional[RefType]:
        """
        Gets the reference to the hardware attribute definition for this value.
        
        Returns:
            RefType representing the attribute definition reference, or None if not set
        """
        return self.hwAttributeDefRef

    def setHwAttributeDefRef(self, value: RefType):
        """
        Sets the reference to the hardware attribute definition for this value.
        Only sets the value if it is not None.
        
        Args:
            value: The attribute definition reference to set
            
        Returns:
            self for method chaining
        """
        if value is not None:
            self.hwAttributeDefRef = value
        return self

    def getValue(self) -> Optional[str]:
        """
        Gets the actual value for this hardware attribute.
        
        Returns:
            String representing the attribute value, or None if not set
        """
        return self.value

    def setValue(self, value: str):
        """
        Sets the actual value for this hardware attribute.
        Only sets the value if it is not None.
        
        Args:
            value: The attribute value to set
            
        Returns:
            self for method chaining
        """
        if value is not None:
            self.value = value
        return self


class HwAttributeLiteralDef(Identifiable):
    """
    Represents a hardware attribute literal definition in AUTOSAR hardware descriptions.
    This class defines the possible literal values for an enumerated hardware attribute.
    """

    def __init__(self, parent, short_name: str):
        """
        Initializes the HwAttributeLiteralDef with a parent and short name.

        Args:
            parent: The parent ARObject that contains this hardware attribute literal definition
            short_name: The unique short name of this hardware attribute literal definition
        """
        super().__init__(parent, short_name)

        self.value: Optional[str] = None

    def getValue(self) -> Optional[str]:
        """
        Gets the literal value for this attribute literal definition.
        
        Returns:
            String representing the literal value, or None if not set
        """
        return self.value

    def setValue(self, value: str):
        """
        Sets the literal value for this attribute literal definition.
        Only sets the value if it is not None.
        
        Args:
            value: The literal value to set
            
        Returns:
            self for method chaining
        """
        if value is not None:
            self.value = value
        return self