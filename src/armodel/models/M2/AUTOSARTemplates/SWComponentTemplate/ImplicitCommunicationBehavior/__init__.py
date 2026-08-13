"""
This module contains the classes of the ImplicitCommunicationBehavior
sub-package of the SWComponentTemplate module, together with its
InstanceRefs sub-module.
"""

from typing import List, Optional

from armodel.models.M2.AUTOSARTemplates.GenericStructure.AbstractStructure import AtpStructureElement
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import ARObject
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.ImplicitCommunicationBehavior.InstanceRefs import *  # noqa: F401,F403
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.ImplicitCommunicationBehavior.InstanceRefs import (
    InnerDataPrototypeGroupInCompositionInstanceRef,
    VariableDataPrototypeInCompositionInstanceRef,
)


class DataPrototypeGroup(AtpStructureElement):
    """
    This meta-class represents the ability to define a collection of
    DataPrototypes that are subject to the formal definition of implicit
    communication behavior. The definition of the collection can be nested.
    """

    # DataPrototypeGroup method parity checklist:
    # Spec: AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf, Table 4.101, p.223
    # Spec verified: R23-11
    # Columns: impl / docstring / test / reader / writer
    # [x] __init__                     [x] impl  [x] docstring  [x] test  [—] reader  [—] writer
    # [x] addDataPrototypeGroupIRef    [x] impl  [x] docstring  [x] test  [x] reader  [—] writer
    # [x] getDataPrototypeGroupIRefs   [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] addImplicitDataAccessIRef    [x] impl  [x] docstring  [x] test  [x] reader  [—] writer
    # [x] getImplicitDataAccessIRefs   [x] impl  [x] docstring  [x] test  [—] reader  [x] writer

    def __init__(self, parent: ARObject, short_name: str):
        """
        Initializes the DataPrototypeGroup with default values.
        """
        super().__init__(parent, short_name)

        # This represents the ability to define nested groups of
        # VariableDataPrototypes.
        self.dataPrototypeGroupIRefs: List[InnerDataPrototypeGroupInCompositionInstanceRef] = []

        # This represents a collection of VariableDataPrototypes that belong to
        # the enclosing DataPrototypeGroup
        self.implicitDataAccessIRefs: List[VariableDataPrototypeInCompositionInstanceRef] = []

    def addDataPrototypeGroupIRef(self, value: Optional[InnerDataPrototypeGroupInCompositionInstanceRef]) -> "DataPrototypeGroup":
        """
        This represents the ability to define nested groups of
        VariableDataPrototypes. A None value is a no-op and does not append to
        dataPrototypeGroupIRefs.

        Args:
            value: The InnerDataPrototypeGroupInCompositionInstanceRef to add

        Returns:
            DataPrototypeGroup: self for method chaining
        """
        if value is not None:
            self.dataPrototypeGroupIRefs.append(value)
        return self

    def getDataPrototypeGroupIRefs(self) -> List[InnerDataPrototypeGroupInCompositionInstanceRef]:
        """
        This represents the ability to define nested groups of
        VariableDataPrototypes.

        Returns:
            List[InnerDataPrototypeGroupInCompositionInstanceRef]: The list of
            dataPrototypeGroup instance references
        """
        return self.dataPrototypeGroupIRefs

    def addImplicitDataAccessIRef(self, value: Optional[VariableDataPrototypeInCompositionInstanceRef]) -> "DataPrototypeGroup":
        """
        This represents a collection of VariableDataPrototypes that belong to
        the enclosing DataPrototypeGroup A None value is a no-op and does not
        append to implicitDataAccessIRefs.

        Args:
            value: The VariableDataPrototypeInCompositionInstanceRef to add

        Returns:
            DataPrototypeGroup: self for method chaining
        """
        if value is not None:
            self.implicitDataAccessIRefs.append(value)
        return self

    def getImplicitDataAccessIRefs(self) -> List[VariableDataPrototypeInCompositionInstanceRef]:
        """
        This represents a collection of VariableDataPrototypes that belong to
        the enclosing DataPrototypeGroup

        Returns:
            List[VariableDataPrototypeInCompositionInstanceRef]: The list of
            implicitDataAccess instance references
        """
        return self.implicitDataAccessIRefs
