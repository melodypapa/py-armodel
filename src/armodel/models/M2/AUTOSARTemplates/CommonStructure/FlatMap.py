"""
This module contains classes for representing AUTOSAR flat map structures
in the CommonStructure module. Flat maps are used to describe instance
hierarchies in a flat manner, typically used for code generation purposes.
"""

from typing import List
from ....M2.AUTOSARTemplates.GenericStructure.AbstractStructure import AtpBlueprintable
from ....M2.MSR.DataDictionary.DataDefProperties import SwDataDefProps
from ....M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import Identifier
from ....M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.AnyInstanceRef import AnyInstanceRef
from ....M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import ARObject
from ....M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable import ARElement, Identifiable


class FlatInstanceDescriptor(Identifiable):
    """
    Represents a flat instance descriptor in AUTOSAR models.
    This class describes a single instance in a flattened instance hierarchy, typically used for code generation.
    """
    
    def __init__(self, parent: ARObject, short_name: str):
        """
        Initializes the FlatInstanceDescriptor with a parent and short name.
        
        Args:
            parent: The parent ARObject that contains this instance descriptor
            short_name: The unique short name of this instance descriptor
        """
        super().__init__(parent, short_name)
        
        # Instance reference to ECU extract reference
        self.ecuExtractReferenceIRef: AnyInstanceRef = None                     
        # Role identifier for this instance descriptor
        self.role: Identifier = None                                        
        # RTE plugin properties for this instance (forward reference)
        self.rtePluginProps = None                              
        # Software data definition properties for this instance
        self.swDataDefProps: SwDataDefProps = None                              
        # Upstream instance reference for this instance descriptor
        self.upstreamReferenceIRef: AnyInstanceRef = None                       

    def getEcuExtractReferenceIRef(self):
        """
        Gets the instance reference to ECU extract reference.
        
        Returns:
            AnyInstanceRef: The ECU extract reference instance reference
        """
        return self.ecuExtractReferenceIRef

    def setEcuExtractReferenceIRef(self, value):
        """
        Sets the instance reference to ECU extract reference.
        
        Args:
            value: The ECU extract reference instance reference to set
            
        Returns:
            self for method chaining
        """
        self.ecuExtractReferenceIRef = value
        return self

    def getRole(self):
        """
        Gets the role identifier for this instance descriptor.
        
        Returns:
            Identifier: The role identifier
        """
        return self.role

    def setRole(self, value):
        """
        Sets the role identifier for this instance descriptor.
        
        Args:
            value: The role identifier to set
            
        Returns:
            self for method chaining
        """
        self.role = value
        return self

    def getRtePluginProps(self):
        """
        Gets the RTE plugin properties for this instance.
        
        Returns:
            RtePluginProps: The RTE plugin properties
        """
        return self.rtePluginProps

    def setRtePluginProps(self, value):
        """
        Sets the RTE plugin properties for this instance.
        
        Args:
            value: The RTE plugin properties to set
            
        Returns:
            self for method chaining
        """
        self.rtePluginProps = value
        return self

    def getSwDataDefProps(self):
        """
        Gets the software data definition properties for this instance.
        
        Returns:
            SwDataDefProps: The software data definition properties
        """
        return self.swDataDefProps

    def setSwDataDefProps(self, value):
        """
        Sets the software data definition properties for this instance.
        
        Args:
            value: The software data definition properties to set
            
        Returns:
            self for method chaining
        """
        self.swDataDefProps = value
        return self

    def getUpstreamReferenceIRef(self):
        """
        Gets the upstream instance reference for this instance descriptor.
        
        Returns:
            AnyInstanceRef: The upstream reference instance reference
        """
        return self.upstreamReferenceIRef

    def setUpstreamReferenceIRef(self, value):
        """
        Sets the upstream instance reference for this instance descriptor.
        
        Args:
            value: The upstream reference instance reference to set
            
        Returns:
            self for method chaining
        """
        self.upstreamReferenceIRef = value
        return self


class FlatMap(AtpBlueprintable):
    """
    Represents a flat map in AUTOSAR models.
    This class contains a collection of flat instance descriptors that define a flattened view of instance hierarchies.
    """
    
    def __init__(self, parent: ARObject, short_name: str):
        """
        Initializes the FlatMap with a parent and short name.
        
        Args:
            parent: The parent ARObject that contains this flat map
            short_name: The unique short name of this flat map
        """
        super().__init__(parent, short_name)

        # List of flat instance descriptors in this flat map
        self.instances: List['FlatInstanceDescriptor'] = []

    def getInstances(self):
        """
        Gets all flat instance descriptors from the elements list, sorted by short name.
        
        Returns:
            List of FlatInstanceDescriptor instances sorted by short name
        """
        return list(sorted(filter(lambda a: isinstance(a, FlatInstanceDescriptor), self.elements), key=lambda o: o.short_name))

    def createFlatInstanceDescriptor(self, short_name: str):
        """
        Creates and adds a FlatInstanceDescriptor to this flat map.
        
        Args:
            short_name: The short name for the new instance descriptor
            
        Returns:
            The created FlatInstanceDescriptor instance
        """
        if (short_name not in self.elements):
            element = FlatInstanceDescriptor(self, short_name)
            self.addElement(element)
            self.instances.append(element)
        return self.getElement(short_name)
