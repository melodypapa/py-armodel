"""
This module contains classes for representing AUTOSAR measurement and calibration
support data (MC support data) in software component and BSW module templates.
"""

from __future__ import annotations
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.VariationPointCapable import VariationPointCapable

from armodel.models.M2.AUTOSARTemplates.GenericStructure.AbstractStructure import AtpInstanceRef
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable import Identifiable
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import Identifier, McdIdentifier, PositiveInteger, RefType, SymbolString
from armodel.models.M2.MSR.DataDictionary.DataDefProperties import SwDataDefProps
from typing import TYPE_CHECKING, List, Optional

if TYPE_CHECKING:
    from armodel.models.M2.AUTOSARTemplates.CommonStructure.MeasurementCalibrationSupport.RptSupport import McFunctionDataRefSet, RptSupportData, RptSwPrototypingAccess
    from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.RPTScenario import RptImplPolicy


class RteEventInEcuInstanceRef(AtpInstanceRef):
    """
    Instance reference to an RTE event in the context of an ECU extract.
    The navigation path begins at the root composition of the ECU extract, passes
    through the atomic component that contains the RTE event and ends at the RTE
    event itself.
    """

    # RteEventInEcuInstanceRef method parity checklist:
    # [ ] __init__                         [ ] impl  [ ] docstring  [ ] test
    # [ ] getBaseRef                       [ ] impl  [ ] docstring  [ ] test
    # [ ] setBaseRef                       [ ] impl  [ ] docstring  [ ] test
    # [ ] getContextRootCompositionRef     [ ] impl  [ ] docstring  [ ] test
    # [ ] setContextRootCompositionRef     [ ] impl  [ ] docstring  [ ] test
    # [ ] getContextAtomicComponentRef     [ ] impl  [ ] docstring  [ ] test
    # [ ] setContextAtomicComponentRef     [ ] impl  [ ] docstring  [ ] test
    # [ ] getTargetRteEventRef             [ ] impl  [ ] docstring  [ ] test
    # [ ] setTargetRteEventRef             [ ] impl  [ ] docstring  [ ] test

    def __init__(self):
        """
        Initializes the RteEventInEcuInstanceRef with default values.
        """
        super().__init__()

        # The base from which the navigation path begins. Stereotypes: atpDerived
        self.baseRef: Optional[RefType] = None

        # The root composition of the ECU extract that contains the referenced RTE event. Tags: xml.sequenceOffset=20
        self.contextRootCompositionRef: Optional[RefType] = None

        # The atomic component in the ECU extract that contains the referenced RTE event. Tags: xml.sequenceOffset=30
        self.contextAtomicComponentRef: Optional[RefType] = None

        # The target RTE event. Tags: xml.sequenceOffset=40
        self.targetRteEventRef: Optional[RefType] = None

    def getBaseRef(self) -> Optional[RefType]:
        """
        Gets the base from which the navigation path begins.

        Returns:
            RefType referencing the base classifier, or None if not set
        """
        return self.baseRef

    def setBaseRef(self, value: Optional[RefType]) -> "RteEventInEcuInstanceRef":
        """
        Sets the base from which the navigation path begins.
        A None value is a no-op and does not overwrite an existing reference.

        Args:
            value: The base reference to set

        Returns:
            self for method chaining
        """
        if value is not None:
            self.baseRef = value
        return self

    def getContextRootCompositionRef(self) -> Optional[RefType]:
        """
        Gets the reference to the root composition of the ECU extract containing the referenced RTE event.

        Returns:
            RefType referencing the RootSwCompositionPrototype, or None if not set
        """
        return self.contextRootCompositionRef

    def setContextRootCompositionRef(self, value: Optional[RefType]) -> "RteEventInEcuInstanceRef":
        """
        Sets the reference to the root composition of the ECU extract containing the referenced RTE event.
        A None value is a no-op and does not overwrite an existing reference.

        Args:
            value: The context root composition reference to set

        Returns:
            self for method chaining
        """
        if value is not None:
            self.contextRootCompositionRef = value
        return self

    def getContextAtomicComponentRef(self) -> Optional[RefType]:
        """
        Gets the reference to the atomic component in the ECU extract containing the referenced RTE event.

        Returns:
            RefType referencing the SwComponentPrototype, or None if not set
        """
        return self.contextAtomicComponentRef

    def setContextAtomicComponentRef(self, value: Optional[RefType]) -> "RteEventInEcuInstanceRef":
        """
        Sets the reference to the atomic component in the ECU extract containing the referenced RTE event.
        A None value is a no-op and does not overwrite an existing reference.

        Args:
            value: The context atomic component reference to set

        Returns:
            self for method chaining
        """
        if value is not None:
            self.contextAtomicComponentRef = value
        return self

    def getTargetRteEventRef(self) -> Optional[RefType]:
        """
        Gets the reference to the target RTE event.

        Returns:
            RefType referencing the RTEEvent, or None if not set
        """
        return self.targetRteEventRef

    def setTargetRteEventRef(self, value: Optional[RefType]) -> "RteEventInEcuInstanceRef":
        """
        Sets the reference to the target RTE event.
        A None value is a no-op and does not overwrite an existing reference.

        Args:
            value: The target RTE event reference to set

        Returns:
            self for method chaining
        """
        if value is not None:
            self.targetRteEventRef = value
        return self


class VariableAccessInEcuInstanceRef(AtpInstanceRef):
    """
    Instance reference to a VariableAccess in the context of an ECU extract.
    The navigation path begins at the root composition of the ECU extract, passes
    through the atomic component that contains the variable access and ends at the
    VariableAccess itself.
    """

    # VariableAccessInEcuInstanceRef method parity checklist:
    # [ ] __init__                             [ ] impl  [ ] docstring  [ ] test
    # [ ] getBaseRef                           [ ] impl  [ ] docstring  [ ] test
    # [ ] setBaseRef                           [ ] impl  [ ] docstring  [ ] test
    # [ ] getContextRootCompositionRef         [ ] impl  [ ] docstring  [ ] test
    # [ ] setContextRootCompositionRef         [ ] impl  [ ] docstring  [ ] test
    # [ ] getContextAtomicComponentRef         [ ] impl  [ ] docstring  [ ] test
    # [ ] setContextAtomicComponentRef         [ ] impl  [ ] docstring  [ ] test
    # [ ] getTargetVariableAccessRef           [ ] impl  [ ] docstring  [ ] test
    # [ ] setTargetVariableAccessRef           [ ] impl  [ ] docstring  [ ] test

    def __init__(self):
        """
        Initializes the VariableAccessInEcuInstanceRef with default values.
        """
        super().__init__()

        # The base from which the navigation path begins. Stereotypes: atpDerived
        self.baseRef: Optional[RefType] = None

        # The root composition of the ECU extract that contains the referenced VariableAccess. Tags: xml.sequenceOffset=20
        self.contextRootCompositionRef: Optional[RefType] = None

        # The atomic component in the ECU extract that contains the referenced VariableAccess. Tags: xml.sequenceOffset=30
        self.contextAtomicComponentRef: Optional[RefType] = None

        # The target VariableAccess. Tags: xml.sequenceOffset=40
        self.targetVariableAccessRef: Optional[RefType] = None

    def getBaseRef(self) -> Optional[RefType]:
        """
        Gets the base from which the navigation path begins.

        Returns:
            RefType referencing the base classifier, or None if not set
        """
        return self.baseRef

    def setBaseRef(self, value: Optional[RefType]) -> "VariableAccessInEcuInstanceRef":
        """
        Sets the base from which the navigation path begins.
        A None value is a no-op and does not overwrite an existing reference.

        Args:
            value: The base reference to set

        Returns:
            self for method chaining
        """
        if value is not None:
            self.baseRef = value
        return self

    def getContextRootCompositionRef(self) -> Optional[RefType]:
        """
        Gets the reference to the root composition of the ECU extract containing the referenced VariableAccess.

        Returns:
            RefType referencing the RootSwCompositionPrototype, or None if not set
        """
        return self.contextRootCompositionRef

    def setContextRootCompositionRef(self, value: Optional[RefType]) -> "VariableAccessInEcuInstanceRef":
        """
        Sets the reference to the root composition of the ECU extract containing the referenced VariableAccess.
        A None value is a no-op and does not overwrite an existing reference.

        Args:
            value: The context root composition reference to set

        Returns:
            self for method chaining
        """
        if value is not None:
            self.contextRootCompositionRef = value
        return self

    def getContextAtomicComponentRef(self) -> Optional[RefType]:
        """
        Gets the reference to the atomic component in the ECU extract containing the referenced VariableAccess.

        Returns:
            RefType referencing the SwComponentPrototype, or None if not set
        """
        return self.contextAtomicComponentRef

    def setContextAtomicComponentRef(self, value: Optional[RefType]) -> "VariableAccessInEcuInstanceRef":
        """
        Sets the reference to the atomic component in the ECU extract containing the referenced VariableAccess.
        A None value is a no-op and does not overwrite an existing reference.

        Args:
            value: The context atomic component reference to set

        Returns:
            self for method chaining
        """
        if value is not None:
            self.contextAtomicComponentRef = value
        return self

    def getTargetVariableAccessRef(self) -> Optional[RefType]:
        """
        Gets the reference to the target VariableAccess.

        Returns:
            RefType referencing the VariableAccess, or None if not set
        """
        return self.targetVariableAccessRef

    def setTargetVariableAccessRef(self, value: Optional[RefType]) -> "VariableAccessInEcuInstanceRef":
        """
        Sets the reference to the target VariableAccess.
        A None value is a no-op and does not overwrite an existing reference.

        Args:
            value: The target VariableAccess reference to set

        Returns:
            self for method chaining
        """
        if value is not None:
            self.targetVariableAccessRef = value
        return self


class McDataAccessDetails(ARObject):
    """
    This meta-class allows to attach detailed information about the usage of a data buffer by the RTE to a corresponding McDataInstance. Use Case: Direct memory access to RTE internal buffers for rapid prototyping. In case of implicit communication, the various task local buffers need to be identified in relation to RTE events and variable access points. Note that the SwComponentPrototype, the RunnableEntity and the VariableDataPrototype are implicitly given be the referred instances of RTEEvent and VariableAccess.
    [constr_4073] Within one given McDataAccessDetails, all instances of System referenced as the base of any McDataAccessDetails.variableAccess or as the base of any McDataAccessDetails.rteEvent shall be identical and of category ECU_EXTRACT.
    """

    # McDataAccessDetails method parity checklist:
    # Spec: AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.pdf, Table 9.12, p.195
    # Spec verified: R23-11
    # [x] __init__                      [x] impl  [x] docstring  [x] test
    # [x] addRteEventIRef               [x] impl  [x] docstring  [x] test
    # [x] getRteEventIRefs              [x] impl  [x] docstring  [x] test
    # [x] addVariableAccessIRef         [x] impl  [x] docstring  [x] test
    # [x] getVariableAccessIRefs        [x] impl  [x] docstring  [x] test

    def __init__(self):
        """
        Initializes the McDataAccessDetails with default values.
        """
        super().__init__()

        # The RTE event used to receive the data via this buffer. InstanceRef implemented by: RteEventInEcuInstanceRef. [constr_10347] For each McDataAccessDetails, the instanceRef in the role rteEvent shall exist at least once at the time when the configuration of the BSW module is finished.
        self.rteEventIRefs: List[RteEventInEcuInstanceRef] = []

        # The VariableAccess for which the data buffer is used. InstanceRef implemented by: VariableAccessInEcuInstanceRef. [constr_10329] For each McDataAccessDetails, the instanceRef in the role variableAccess shall exist at least once at the time when the configuration of the BSW module is finished.
        self.variableAccessIRefs: List[VariableAccessInEcuInstanceRef] = []

    def addRteEventIRef(self, value: Optional[RteEventInEcuInstanceRef]) -> "McDataAccessDetails":
        """
        Adds an RTE event instance reference, referencing the RTE event used to receive the data via this buffer.
        A None value is a no-op and does not append anything.

        Args:
            value: The RteEventInEcuInstanceRef to add

        Returns:
            self for method chaining
        """
        if value is not None:
            self.rteEventIRefs.append(value)
        return self

    def getRteEventIRefs(self) -> List[RteEventInEcuInstanceRef]:
        """
        Gets the RTE event instance references, referencing the RTE events used to receive the data via this buffer.
        [constr_10347] For each McDataAccessDetails, the instanceRef in the role rteEvent shall exist at least once at the time when the configuration of the BSW module is finished.

        Returns:
            List of RteEventInEcuInstanceRef instances
        """
        return self.rteEventIRefs

    def addVariableAccessIRef(self, value: Optional[VariableAccessInEcuInstanceRef]) -> "McDataAccessDetails":
        """
        Adds a VariableAccess instance reference, referencing the VariableAccess for which the data buffer is used.
        A None value is a no-op and does not append anything.

        Args:
            value: The VariableAccessInEcuInstanceRef to add

        Returns:
            self for method chaining
        """
        if value is not None:
            self.variableAccessIRefs.append(value)
        return self

    def getVariableAccessIRefs(self) -> List[VariableAccessInEcuInstanceRef]:
        """
        Gets the VariableAccess instance references, referencing the VariableAccesses for which the data buffer is used.
        [constr_10329] For each McDataAccessDetails, the instanceRef in the role variableAccess shall exist at least once at the time when the configuration of the BSW module is finished.

        Returns:
            List of VariableAccessInEcuInstanceRef instances
        """
        return self.variableAccessIRefs


class McParameterElementGroup(ARObject):
    """
    Denotes a group of calibration parameters which are handled by the RTE as one data structure.
    """

    # McParameterElementGroup method parity checklist:
    # Spec: AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.pdf, Table 9.6, p.181
    # Spec verified: R23-11
    # [x] __init__                     [x] impl  [x] docstring  [x] test
    # [x] getRamLocationRef            [x] impl  [x] docstring  [x] test
    # [x] setRamLocationRef            [x] impl  [x] docstring  [x] test
    # [x] getRomLocationRef            [x] impl  [x] docstring  [x] test
    # [x] setRomLocationRef            [x] impl  [x] docstring  [x] test
    # [x] getShortLabel                [x] impl  [x] docstring  [x] test
    # [x] setShortLabel                [x] impl  [x] docstring  [x] test

    def __init__(self):
        """
        Initializes the McParameterElementGroup with default values.
        """
        super().__init__()

        # Refers to the RAM location of this parameter group. To be used for the init-RAM method. [constr_10342] For each McParameterElementGroup, the reference in the role ramLocation shall exist at the time when the configuration of the BSW module is finished.
        self.ramLocationRef: Optional[RefType] = None

        # Refers to the ROM location of this parameter group. To be used for the init-RAM method. [constr_10343] For each McParameterElementGroup, the reference in the role romLocation shall exist at the time when the configuration of the BSW module is finished.
        self.romLocationRef: Optional[RefType] = None

        # Assigns a name to this element. [constr_10344] For each McParameterElementGroup, the attribute shortLabel shall exist at the time when the configuration of the BSW module is finished. Tags: xml.sequenceOffset=-100
        self.shortLabel: Optional[Identifier] = None

    def getRamLocationRef(self) -> Optional[RefType]:
        """
        Gets the reference to the RAM location of this parameter group. To be used for the init-RAM method.

        Returns:
            RefType referencing the VariableDataPrototype holding the RAM location, or None if not set
        """
        return self.ramLocationRef

    def setRamLocationRef(self, value: Optional[RefType]) -> "McParameterElementGroup":
        """
        Sets the reference to the RAM location of this parameter group. To be used for the init-RAM method.
        A None value is a no-op and does not overwrite an existing reference.

        Args:
            value: The RAM location reference to set

        Returns:
            self for method chaining
        """
        if value is not None:
            self.ramLocationRef = value
        return self

    def getRomLocationRef(self) -> Optional[RefType]:
        """
        Gets the reference to the ROM location of this parameter group. To be used for the init-RAM method.

        Returns:
            RefType referencing the ParameterDataPrototype holding the ROM location, or None if not set
        """
        return self.romLocationRef

    def setRomLocationRef(self, value: Optional[RefType]) -> "McParameterElementGroup":
        """
        Sets the reference to the ROM location of this parameter group. To be used for the init-RAM method.
        A None value is a no-op and does not overwrite an existing reference.

        Args:
            value: The ROM location reference to set

        Returns:
            self for method chaining
        """
        if value is not None:
            self.romLocationRef = value
        return self

    def getShortLabel(self) -> Optional[Identifier]:
        """
        Gets the name assigned to this element.

        Returns:
            Identifier representing the short label, or None if not set
        """
        return self.shortLabel

    def setShortLabel(self, value: Optional[Identifier]) -> "McParameterElementGroup":
        """
        Sets the name assigned to this element.
        A None value is a no-op and does not overwrite an existing short label.

        Args:
            value: The short label identifier to set

        Returns:
            self for method chaining
        """
        if value is not None:
            self.shortLabel = value
        return self


class McSwEmulationMethodSupport(ARObject, VariationPointCapable):
    """
    This denotes the method used by the RTE to handle the calibration data. It is published by the RTE generator and can be used e.g. to generate the corresponding emulation method in a Complex Driver. According to the actual method given by the category attribute, not all attributes are always needed: • double pointered method: only baseReference is mandatory • single pointered method: only referenceTable is mandatory • initRam method: only elementGroup(s) are mandatory Note: For single/double pointered method the group locations are implicitly accessed via the reference table and their location can be found from the initial values in the M1 model of the respective pointers. Therefore, the description of elementGroups is not needed in these cases. Likewise, for double pointered method the reference table description can be accessed via the M1 model under baseReference.
    """

    # McSwEmulationMethodSupport method parity checklist:
    # Spec: AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.pdf, Table 9.5, p.180
    # Spec verified: R23-11
    # [x] __init__                     [x] impl  [x] docstring  [x] test
    # [x] getBaseReferenceRef          [x] impl  [x] docstring  [x] test
    # [x] setBaseReferenceRef          [x] impl  [x] docstring  [x] test
    # [x] getCategory                  [x] impl  [x] docstring  [x] test
    # [x] setCategory                  [x] impl  [x] docstring  [x] test
    # [x] addElementGroup              [x] impl  [x] docstring  [x] test
    # [x] getElementGroups             [x] impl  [x] docstring  [x] test
    # [x] getReferenceTableRef         [x] impl  [x] docstring  [x] test
    # [x] setReferenceTableRef         [x] impl  [x] docstring  [x] test
    # [x] getShortLabel                [x] impl  [x] docstring  [x] test
    # [x] setShortLabel                [x] impl  [x] docstring  [x] test

    def __init__(self):
        """
        Initializes the McSwEmulationMethodSupport with default values.
        """
        super().__init__()

        # Refers to the base pointer in case of the double-pointered method.
        self.baseReferenceRef: Optional[RefType] = None

        # Identifies the actual method. The possible names shall correspond to the symbols of the ECU configuration parameter for the calibration method of the RTE, and can include vendor specific methods. [constr_10340] For each McSwEmulationMethodSupport, the attribute category shall exist at the time when the configuration of the BSW module is finished. Tags: xml.sequenceOffset=-90
        self.category: Optional[Identifier] = None

        # Denotes the grouping of calibration parameters in the actual RTE code. Depending on the category, this information maybe required to set up the emulation code.
        self.elementGroups: List[McParameterElementGroup] = []

        # Refers to the pointer table in case of the single-pointered method.
        self.referenceTableRef: Optional[RefType] = None

        # Assigns a name to this element. [constr_10341] For each McSwEmulationMethodSupport, the attribute shortLabel shall exist at the time when the configuration of the BSW module is finished. Tags: xml.sequenceOffset=-100
        self.shortLabel: Optional[Identifier] = None

    def getBaseReferenceRef(self) -> Optional[RefType]:
        """
        Gets the reference to the base pointer in case of the double-pointered method.

        Returns:
            RefType referencing the VariableDataPrototype used as base pointer, or None if not set
        """
        return self.baseReferenceRef

    def setBaseReferenceRef(self, value: Optional[RefType]) -> "McSwEmulationMethodSupport":
        """
        Sets the reference to the base pointer in case of the double-pointered method.
        A None value is a no-op and does not overwrite an existing reference.

        Args:
            value: The base reference to set

        Returns:
            self for method chaining
        """
        if value is not None:
            self.baseReferenceRef = value
        return self

    def getCategory(self) -> Optional[Identifier]:
        """
        Gets the category identifying the actual method. The possible names shall correspond to the symbols of the ECU configuration parameter for the calibration method of the RTE, and can include vendor specific methods.

        Returns:
            Identifier representing the category, or None if not set
        """
        return self.category

    def setCategory(self, value: Optional[Identifier]) -> "McSwEmulationMethodSupport":
        """
        Sets the category identifying the actual method. The possible names shall correspond to the symbols of the ECU configuration parameter for the calibration method of the RTE, and can include vendor specific methods.
        A None value is a no-op and does not overwrite an existing category.

        Args:
            value: The category identifier to set

        Returns:
            self for method chaining
        """
        if value is not None:
            self.category = value
        return self

    def addElementGroup(self, value: Optional[McParameterElementGroup]) -> "McSwEmulationMethodSupport":
        """
        Adds a grouping of calibration parameters in the actual RTE code. Depending on the category, this information maybe required to set up the emulation code.
        A None value is a no-op and does not append anything.

        Args:
            value: The McParameterElementGroup to add

        Returns:
            self for method chaining
        """
        if value is not None:
            self.elementGroups.append(value)
        return self

    def getElementGroups(self) -> List[McParameterElementGroup]:
        """
        Gets the groupings of calibration parameters in the actual RTE code aggregated by this emulation method support.

        Returns:
            List of McParameterElementGroup instances
        """
        return self.elementGroups

    def getReferenceTableRef(self) -> Optional[RefType]:
        """
        Gets the reference to the pointer table in case of the single-pointered method.

        Returns:
            RefType referencing the VariableDataPrototype used as pointer table, or None if not set
        """
        return self.referenceTableRef

    def setReferenceTableRef(self, value: Optional[RefType]) -> "McSwEmulationMethodSupport":
        """
        Sets the reference to the pointer table in case of the single-pointered method.
        A None value is a no-op and does not overwrite an existing reference.

        Args:
            value: The reference table reference to set

        Returns:
            self for method chaining
        """
        if value is not None:
            self.referenceTableRef = value
        return self

    def getShortLabel(self) -> Optional[Identifier]:
        """
        Gets the name assigned to this element.

        Returns:
            Identifier representing the short label, or None if not set
        """
        return self.shortLabel

    def setShortLabel(self, value: Optional[Identifier]) -> "McSwEmulationMethodSupport":
        """
        Sets the name assigned to this element.
        A None value is a no-op and does not overwrite an existing short label.

        Args:
            value: The short label identifier to set

        Returns:
            self for method chaining
        """
        if value is not None:
            self.shortLabel = value
        return self


class ImplementationElementInParameterInstanceRef(ARObject):
    """
    Describes a reference to a particular ImplementationDataTypeElement instance in the context of a given ParameterDataPrototype. Thus it refers to a particular element in the implementation description of a software data structure. Use Case: The RTE generator publishes its generated structure of calibration parameters in its BSW module description using the "constantMemory" role of ParameterDataPrototypes. Each ParameterDataPrototype describes a group of single calibration parameters. In order to point to these single parameters, this "instance ref" is needed. Note that this class follows the pattern of an InstanceRef but is not implemented based on the abstract classes because the ImplementationDataType isn't either, especially because ImplementationDataTypeElement isn't derived from AtpPrototype.
    [constr_4034] Target and context of MC emulation reference: Within one ImplementationElementInParameterInstanceRef, the target shall refer to a subelement of the ParameterDataPrototype which is referred as context.
    [constr_4061] Completeness of MC emulation reference: If an McDataInstance in the role of a subElement of another McDataInstance specifies an instanceInMemory, then the containing McDataInstance shall also specify an instanceInMemory. The target of the latter (i.e. upper level) instanceInMemory shall be identical (including array index, if defined) to the context of the first (i.e. lower level) instanceInMemory.
    """

    # ImplementationElementInParameterInstanceRef method parity checklist:
    # Spec: AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.pdf, Table 9.7, p.184
    # Spec verified: R23-11
    # [x] __init__                     [x] impl  [x] docstring  [x] test
    # [x] getContextRef                [x] impl  [x] docstring  [x] test
    # [x] setContextRef                [x] impl  [x] docstring  [x] test
    # [x] getTargetRef                 [x] impl  [x] docstring  [x] test
    # [x] setTargetRef                 [x] impl  [x] docstring  [x] test

    def __init__(self):
        """
        Initializes the ImplementationElementInParameterInstanceRef with default values.
        """
        super().__init__()

        # The context for the referred element. [constr_10345] For each ImplementationElementInParameterInstanceRef, the reference in the role context shall exist at the time when the configuration of the BSW module is finished. Tags: xml.sequenceOffset=20
        self.contextRef: Optional[RefType] = None

        # The referred data element. [constr_10346] For each ImplementationElementInParameterInstanceRef, the reference in the role target shall exist at the time when the configuration of the BSW module is finished. Tags: xml.sequenceOffset=30
        self.targetRef: Optional[RefType] = None

    def getContextRef(self) -> Optional[RefType]:
        """
        Gets the reference to the ParameterDataPrototype providing the context for the referred element.
        [constr_10345] For each ImplementationElementInParameterInstanceRef, the reference in the role context shall exist at the time when the configuration of the BSW module is finished.

        Returns:
            RefType referencing the context ParameterDataPrototype, or None if not set
        """
        return self.contextRef

    def setContextRef(self, value: Optional[RefType]) -> "ImplementationElementInParameterInstanceRef":
        """
        Sets the reference to the ParameterDataPrototype providing the context for the referred element.
        A None value is a no-op and does not overwrite an existing reference.

        Args:
            value: The context reference to set

        Returns:
            self for method chaining
        """
        if value is not None:
            self.contextRef = value
        return self

    def getTargetRef(self) -> Optional[RefType]:
        """
        Gets the reference to the referred AbstractImplementationDataTypeElement. [constr_4034] The target shall refer to a subelement of the ParameterDataPrototype which is referred as context.
        [constr_10346] For each ImplementationElementInParameterInstanceRef, the reference in the role target shall exist at the time when the configuration of the BSW module is finished.

        Returns:
            RefType referencing the target data element, or None if not set
        """
        return self.targetRef

    def setTargetRef(self, value: Optional[RefType]) -> "ImplementationElementInParameterInstanceRef":
        """
        Sets the reference to the referred AbstractImplementationDataTypeElement.
        A None value is a no-op and does not overwrite an existing reference.

        Args:
            value: The target reference to set

        Returns:
            self for method chaining
        """
        if value is not None:
            self.targetRef = value
        return self


class McFunction(Identifiable):
    """
    Represents a functional element to be used as input to support measurement and calibration. It is used to • assign calibration parameters to a logical function • assign measurement variables to a logical function • structure functions hierarchically
    """

    # McFunction method parity checklist:
    # Spec: AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.pdf, Table 9.8, p.186
    # Spec verified: R23-11
    # [x] __init__                       [x] impl  [x] docstring  [x] test
    # [x] getDefCalprmSet                [x] impl  [x] docstring  [x] test
    # [x] setDefCalprmSet                [x] impl  [x] docstring  [x] test
    # [x] getInMeasurementSet            [x] impl  [x] docstring  [x] test
    # [x] setInMeasurementSet            [x] impl  [x] docstring  [x] test
    # [x] getLocMeasurementSet           [x] impl  [x] docstring  [x] test
    # [x] setLocMeasurementSet           [x] impl  [x] docstring  [x] test
    # [x] getOutMeasurementSet           [x] impl  [x] docstring  [x] test
    # [x] setOutMeasurementSet           [x] impl  [x] docstring  [x] test
    # [x] getRefCalprmSet                [x] impl  [x] docstring  [x] test
    # [x] setRefCalprmSet                [x] impl  [x] docstring  [x] test
    # [x] addSubFunctionRef              [x] impl  [x] docstring  [x] test
    # [x] getSubFunctionRefs             [x] impl  [x] docstring  [x] test

    def __init__(self, parent: ARObject, short_name: str):
        """
        Initializes the McFunction with a parent and short name.

        Args:
            parent: The parent ARObject that contains this function
            short_name: The unique short name of this function
        """
        super().__init__(parent, short_name)

        # Refers to the set of adjustable data (= calibration parameters) defined in this function. Tags: atp.Splitkey=defCalprmSet xml.sequenceOffset=10
        self.defCalprmSet: Optional[McFunctionDataRefSet] = None

        # Refers to the set of measurable input data for this function. Tags: atp.Splitkey=inMeasurementSet xml.sequenceOffset=30
        self.inMeasurementSet: Optional[McFunctionDataRefSet] = None

        # Refers to the set of measurable local data in this function. Tags: atp.Splitkey=locMeasurementSet xml.sequenceOffset=50
        self.locMeasurementSet: Optional[McFunctionDataRefSet] = None

        # Refers to the set of measurable output data from this function. Tags: atp.Splitkey=outMeasurementSet
        self.outMeasurementSet: Optional[McFunctionDataRefSet] = None

        # Refers to the set of adjustable data (= calibration parameters) referred by this function. Tags: atp.Splitkey=refCalprmSet xml.sequenceOffset=20
        self.refCalprmSet: Optional[McFunctionDataRefSet] = None

        # A sub-function that is seen as part of the enclosing function.
        self.subFunctionRefs: List[RefType] = []

    def getDefCalprmSet(self) -> Optional[McFunctionDataRefSet]:
        """
        Gets the set of adjustable data (= calibration parameters) defined in this function.

        Returns:
            McFunctionDataRefSet instance, or None if not set
        """
        return self.defCalprmSet

    def setDefCalprmSet(self, value: Optional[McFunctionDataRefSet]) -> "McFunction":
        """
        Sets the set of adjustable data (= calibration parameters) defined in this function.
        A None value is a no-op and does not overwrite an existing set.

        Args:
            value: The McFunctionDataRefSet to set

        Returns:
            self for method chaining
        """
        if value is not None:
            self.defCalprmSet = value
        return self

    def getInMeasurementSet(self) -> Optional[McFunctionDataRefSet]:
        """
        Gets the set of measurable input data for this function.

        Returns:
            McFunctionDataRefSet instance, or None if not set
        """
        return self.inMeasurementSet

    def setInMeasurementSet(self, value: Optional[McFunctionDataRefSet]) -> "McFunction":
        """
        Sets the set of measurable input data for this function.
        A None value is a no-op and does not overwrite an existing set.

        Args:
            value: The McFunctionDataRefSet to set

        Returns:
            self for method chaining
        """
        if value is not None:
            self.inMeasurementSet = value
        return self

    def getLocMeasurementSet(self) -> Optional[McFunctionDataRefSet]:
        """
        Gets the set of measurable local data in this function.

        Returns:
            McFunctionDataRefSet instance, or None if not set
        """
        return self.locMeasurementSet

    def setLocMeasurementSet(self, value: Optional[McFunctionDataRefSet]) -> "McFunction":
        """
        Sets the set of measurable local data in this function.
        A None value is a no-op and does not overwrite an existing set.

        Args:
            value: The McFunctionDataRefSet to set

        Returns:
            self for method chaining
        """
        if value is not None:
            self.locMeasurementSet = value
        return self

    def getOutMeasurementSet(self) -> Optional[McFunctionDataRefSet]:
        """
        Gets the set of measurable output data from this function.

        Returns:
            McFunctionDataRefSet instance, or None if not set
        """
        return self.outMeasurementSet

    def setOutMeasurementSet(self, value: Optional[McFunctionDataRefSet]) -> "McFunction":
        """
        Sets the set of measurable output data from this function.
        A None value is a no-op and does not overwrite an existing set.

        Args:
            value: The McFunctionDataRefSet to set

        Returns:
            self for method chaining
        """
        if value is not None:
            self.outMeasurementSet = value
        return self

    def getRefCalprmSet(self) -> Optional[McFunctionDataRefSet]:
        """
        Gets the set of adjustable data (= calibration parameters) referred by this function.

        Returns:
            McFunctionDataRefSet instance, or None if not set
        """
        return self.refCalprmSet

    def setRefCalprmSet(self, value: Optional[McFunctionDataRefSet]) -> "McFunction":
        """
        Sets the set of adjustable data (= calibration parameters) referred by this function.
        A None value is a no-op and does not overwrite an existing set.

        Args:
            value: The McFunctionDataRefSet to set

        Returns:
            self for method chaining
        """
        if value is not None:
            self.refCalprmSet = value
        return self

    def addSubFunctionRef(self, value: Optional[RefType]) -> "McFunction":
        """
        Adds a reference to a sub-function that is seen as part of the enclosing function.
        A None value is a no-op and does not append anything.

        Args:
            value: The sub-function reference to add

        Returns:
            self for method chaining
        """
        if value is not None:
            self.subFunctionRefs.append(value)
        return self

    def getSubFunctionRefs(self) -> List[RefType]:
        """
        Gets the references to sub-functions that are seen as part of the enclosing function.

        Returns:
            List of RefType instances referencing McFunction elements
        """
        return self.subFunctionRefs


class RoleBasedMcDataAssignment(ARObject, VariationPointCapable):
    """
    This meta-class allows to define links that specify logical relationships between single McDataInstances. The details on the existence and semantics of such links are not standardized. Possible Use Case: Rapid Prototyping solutions in which additional communication buffers and switches are implemented in the RTE that allow to switch between the usage of the original and the bypass buffers. The different buffers and the switch can be represented by McDataInstances (in order to be accessed by MC tools) which have relationships to each other.
    """

    # RoleBasedMcDataAssignment method parity checklist:
    # Spec: AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.pdf, Table D.55, p.329
    # Spec verified: R23-11
    # [x] __init__                     [x] impl  [x] docstring  [x] test
    # [x] addExecutionContextRef       [x] impl  [x] docstring  [x] test  [x] reader  [—] writer
    # [x] getExecutionContextRefs      [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] addMcDataInstanceRef         [x] impl  [x] docstring  [x] test  [x] reader  [—] writer
    # [x] getMcDataInstanceRefs        [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] getRole                      [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] setRole                      [x] impl  [x] docstring  [x] test  [x] reader  [—] writer

    def __init__(self):
        """
        Initializes the RoleBasedMcDataAssignment.
        """
        super().__init__()

        # Determines the executionContext in which the McDataInstance describing a local (e.g Task-Local) buffer of a global buffer is valid.
        self.executionContextRefs: List[RefType] = []

        # The target of the assignment.
        self.mcDataInstanceRefs: List[RefType] = []

        # Shall be used to specify the role of the assigned data instance in relation to the instance that owns the assignment.
        self.role: Optional[Identifier] = None

    def getExecutionContextRefs(self) -> List[RefType]:
        """
        Gets the references to the execution context the assigned data instance is used in.

        Returns:
            List of RefType referencing the execution context
        """
        return self.executionContextRefs

    def addExecutionContextRef(self, value: Optional[RefType]) -> "RoleBasedMcDataAssignment":
        """
        Adds a reference to the execution context the assigned data instance is used in.
        A None value is a no-op and does not append anything.

        Args:
            value: The execution context reference to add

        Returns:
            self for method chaining
        """
        if value is not None:
            self.executionContextRefs.append(value)
        return self

    def getMcDataInstanceRefs(self) -> List[RefType]:
        """
        Gets the references to the McDataInstance the role is assigned to.

        Returns:
            List of RefType referencing the McDataInstance
        """
        return self.mcDataInstanceRefs

    def addMcDataInstanceRef(self, value: Optional[RefType]) -> "RoleBasedMcDataAssignment":
        """
        Adds a reference to the McDataInstance the role is assigned to.
        A None value is a no-op and does not append anything.

        Args:
            value: The McDataInstance reference to add

        Returns:
            self for method chaining
        """
        if value is not None:
            self.mcDataInstanceRefs.append(value)
        return self

    def getRole(self) -> Optional[Identifier]:
        """
        Gets the role of the assigned data instance in relation to the instance that owns the assignment.

        Returns:
            Identifier representing the role, or None if not set
        """
        return self.role

    def setRole(self, value: Optional[Identifier]) -> "RoleBasedMcDataAssignment":
        """
        Sets the role of the assigned data instance in relation to the instance that owns the assignment.
        A None value is a no-op and does not overwrite an existing role.

        Args:
            value: The role identifier to set

        Returns:
            self for method chaining
        """
        if value is not None:
            self.role = value
        return self


class McDataInstance(Identifiable, VariationPointCapable):
    """
    Describes the specific properties of one data instance in order to support measurement and/or calibration of this data instance. The most important attributes are: • Its shortName is copied from the ECU Flat map (if applicable) and will be used as identifier and for display by the MC system. • The category is copied from the corresponding data type (ApplicationDataType if defined, otherwise ImplementationDataType) as far as applicable. • The symbol is the one used in the programming language. It will be used to find out the actual memory address by the final generation tool with the help of linker generated information. It is assumed that in the M1 model this part and all the aggregated and referred elements (with the exception of the Flat Map and the references from ImplementationElementInParameterInstanceRef and McAccessDetails) are completely generated from "upstream" information. This means, that even if an element like e.g. a CompuMethod is only used via reference here, it will be copied into the M1 artifact which holds the complete McSupportData for a given Implementation.
    """

    # McDataInstance method parity checklist:
    # Spec: AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.pdf, Table 9.4, p.177
    # Spec verified: R23-11
    # [x] __init__                            [x] impl  [x] docstring  [x] test
    # [x] getArraySize                        [x] impl  [x] docstring  [x] test
    # [x] setArraySize                        [x] impl  [x] docstring  [x] test
    # [x] getDisplayIdentifier                [x] impl  [x] docstring  [x] test
    # [x] setDisplayIdentifier                [x] impl  [x] docstring  [x] test
    # [x] getFlatMapEntryRef                  [x] impl  [x] docstring  [x] test
    # [x] setFlatMapEntryRef                  [x] impl  [x] docstring  [x] test
    # [x] getInstanceInMemory                 [x] impl  [x] docstring  [x] test
    # [x] setInstanceInMemory                 [x] impl  [x] docstring  [x] test
    # [x] getMcDataAccessDetails              [x] impl  [x] docstring  [x] test
    # [x] setMcDataAccessDetails              [x] impl  [x] docstring  [x] test
    # [x] addMcDataAssignment                 [x] impl  [x] docstring  [x] test
    # [x] getMcDataAssignments                [x] impl  [x] docstring  [x] test
    # [x] getResultingProperties              [x] impl  [x] docstring  [x] test
    # [x] setResultingProperties              [x] impl  [x] docstring  [x] test
    # [x] getResultingRptSwPrototypingAccess  [x] impl  [x] docstring  [x] test
    # [x] setResultingRptSwPrototypingAccess  [x] impl  [x] docstring  [x] test
    # [x] getRole                             [x] impl  [x] docstring  [x] test
    # [x] setRole                             [x] impl  [x] docstring  [x] test
    # [x] getRptImplPolicy                    [x] impl  [x] docstring  [x] test
    # [x] setRptImplPolicy                    [x] impl  [x] docstring  [x] test
    # [x] createSubElement                    [x] impl  [x] docstring  [x] test
    # [x] getSubElements                      [x] impl  [x] docstring  [x] test
    # [x] getSymbol                           [x] impl  [x] docstring  [x] test
    # [x] setSymbol                           [x] impl  [x] docstring  [x] test

    def __init__(self, parent: ARObject, short_name: str):
        """
        Initializes the McDataInstance with a parent and short name.

        Args:
            parent: The parent ARObject that contains this data instance
            short_name: The unique short name of this data instance
        """
        super().__init__(parent, short_name)

        # The existence of this attribute turns the data instance into an array of data. The attribute determines the size of the array in terms of number of elements.
        self.arraySize: Optional[PositiveInteger] = None

        # An optional attribute to be used to set the ASAM ASAP2 DISPLAY_IDENTIFIER attribute.
        self.displayIdentifier: Optional[McdIdentifier] = None

        # Reference to the corresponding entry in the ECU Flat Map. This allows to trace back to the original specification of the generated data instance. This link shall be added by the RTE generator mainly for documentation purposes.
        self.flatMapEntryRef: Optional[RefType] = None

        # Reference to the corresponding data instance in the description of calibration data structures published by the RTE generator. This is used to support emulation methods inside the ECU, it is not required for A2L generation.
        self.instanceInMemory: Optional[ImplementationElementInParameterInstanceRef] = None

        # Refers to "upstream" information on how the RTE uses this data instance. Use Case: Rapid Prototyping
        self.mcDataAccessDetails: Optional[McDataAccessDetails] = None

        # An assignment between McDataInstances. This supports the indication of related McDataElement implementing the of "RP global buffer", "RP global measurement buffer", "RP enabler flag".
        self.mcDataAssignments: List[RoleBasedMcDataAssignment] = []

        # These are the generated properties resulting from decisions taken by the RTE generator for the actually implemented data instance. Only those properties are relevant here, which are needed for the measurement and calibration system.
        self.resultingProperties: Optional[SwDataDefProps] = None

        # Describes the implemented accessibility of data and modes by the rapid prototyping tooling.
        self.resultingRptSwPrototypingAccess: Optional[RptSwPrototypingAccess] = None

        # An optional attribute to be used for additional information on the role of this data instance, for example in the context of rapid prototyping.
        self.role: Optional[Identifier] = None

        # Describes the implemented code preparation for rapid prototyping at data accesses for a hook based bypassing.
        self.rptImplPolicy: Optional[RptImplPolicy] = None

        # This relation indicates, that the target element is part of a "struct" which is given by the source element. This information will be used by the final generator to set up the correct addressing scheme.
        self.subElements: List[McDataInstance] = []

        # This String is used to determine the memory address during final generation of the MC configuration data (e.g. "A2L" file) . It shall be the name of the element in the programming language such that it can be identified in linker generated information. In case the McDataInstance is part of composite data in the programming language, the symbol String may include parts denoting the element context, unless the context is given by the symbol attribute of an enclosing McDataInstance. This means in particular for the C language that the "." character shall be used as a separator between the name of a "struct" variable the name of one of its elements. The symbol can differ from the shortName in case of generated C data declarations. It is an optional attribute since it may be missing in case the instance represents an element (e.g. a single array element) which has no name in the linker map.
        self.symbol: Optional[SymbolString] = None

    def getArraySize(self) -> Optional[PositiveInteger]:
        """
        Gets the array size. The existence of this attribute turns the data instance into an array of data; the value determines the size of the array in terms of number of elements.

        Returns:
            PositiveInteger representing the array size, or None if not set
        """
        return self.arraySize

    def setArraySize(self, value: Optional[PositiveInteger]) -> "McDataInstance":
        """
        Sets the array size. The existence of this attribute turns the data instance into an array of data; the value determines the size of the array in terms of number of elements.
        A None value is a no-op and does not overwrite an existing arraySize.

        Args:
            value: The array size to set

        Returns:
            self for method chaining
        """
        if value is not None:
            self.arraySize = value
        return self

    def getDisplayIdentifier(self) -> Optional[McdIdentifier]:
        """
        Gets the optional ASAM ASAP2 DISPLAY_IDENTIFIER attribute.

        Returns:
            McdIdentifier used to set the ASAM ASAP2 DISPLAY_IDENTIFIER attribute, or None if not set
        """
        return self.displayIdentifier

    def setDisplayIdentifier(self, value: Optional[McdIdentifier]) -> "McDataInstance":
        """
        Sets the optional ASAM ASAP2 DISPLAY_IDENTIFIER attribute.
        A None value is a no-op and does not overwrite an existing displayIdentifier.

        Args:
            value: The McdIdentifier to set

        Returns:
            self for method chaining
        """
        if value is not None:
            self.displayIdentifier = value
        return self

    def getFlatMapEntryRef(self) -> Optional[RefType]:
        """
        Gets the reference to the corresponding entry in the ECU Flat Map, allowing to trace back to the original specification of the generated data instance. This link shall be added by the RTE generator mainly for documentation purposes.

        Returns:
            RefType referencing the flat map entry, or None if not set
        """
        return self.flatMapEntryRef

    def setFlatMapEntryRef(self, value: Optional[RefType]) -> "McDataInstance":
        """
        Sets the reference to the corresponding entry in the ECU Flat Map, allowing to trace back to the original specification of the generated data instance. This link shall be added by the RTE generator mainly for documentation purposes.
        A None value is a no-op and does not overwrite an existing flatMapEntryRef.

        Args:
            value: The flat map entry reference to set

        Returns:
            self for method chaining
        """
        if value is not None:
            self.flatMapEntryRef = value
        return self

    def getInstanceInMemory(self) -> Optional[ImplementationElementInParameterInstanceRef]:
        """
        Gets the reference to the corresponding data instance in the description of calibration data structures published by the RTE generator. This is used to support emulation methods inside the ECU, it is not required for A2L generation.

        Returns:
            ImplementationElementInParameterInstanceRef referencing the data instance in memory, or None if not set
        """
        return self.instanceInMemory

    def setInstanceInMemory(self, value: Optional[ImplementationElementInParameterInstanceRef]) -> "McDataInstance":
        """
        Sets the reference to the corresponding data instance in the description of calibration data structures published by the RTE generator. This is used to support emulation methods inside the ECU, it is not required for A2L generation.
        A None value is a no-op and does not overwrite an existing instanceInMemory.

        Args:
            value: The instance in memory reference to set

        Returns:
            self for method chaining
        """
        if value is not None:
            self.instanceInMemory = value
        return self

    def getMcDataAccessDetails(self) -> Optional[McDataAccessDetails]:
        """
        Gets the upstream information on how the RTE uses this data instance (use case: Rapid Prototyping).

        Returns:
            McDataAccessDetails instance, or None if not set
        """
        return self.mcDataAccessDetails

    def setMcDataAccessDetails(self, value: Optional[McDataAccessDetails]) -> "McDataInstance":
        """
        Sets the upstream information on how the RTE uses this data instance (use case: Rapid Prototyping).
        A None value is a no-op and does not overwrite an existing mcDataAccessDetails.

        Args:
            value: The McDataAccessDetails to set

        Returns:
            self for method chaining
        """
        if value is not None:
            self.mcDataAccessDetails = value
        return self

    def addMcDataAssignment(self, value: Optional[RoleBasedMcDataAssignment]) -> "McDataInstance":
        """
        Adds an assignment between McDataInstances. This supports the indication of related McDataElement implementing of "RP global buffer", "RP global measurement buffer", "RP enabler flag".
        A None value is a no-op and does not append anything.

        Args:
            value: The role-based MC data assignment to add

        Returns:
            self for method chaining
        """
        if value is not None:
            self.mcDataAssignments.append(value)
        return self

    def getMcDataAssignments(self) -> List[RoleBasedMcDataAssignment]:
        """
        Gets the assignments between McDataInstances aggregated by this data instance.

        Returns:
            List of RoleBasedMcDataAssignment instances
        """
        return self.mcDataAssignments

    def getResultingProperties(self) -> Optional[SwDataDefProps]:
        """
        Gets the generated properties resulting from decisions taken by the RTE generator for the actually implemented data instance. Only those properties are relevant here, which are needed for the measurement and calibration system.

        Returns:
            SwDataDefProps instance, or None if not set
        """
        return self.resultingProperties

    def setResultingProperties(self, value: Optional[SwDataDefProps]) -> "McDataInstance":
        """
        Sets the generated properties resulting from decisions taken by the RTE generator for the actually implemented data instance. Only those properties are relevant here, which are needed for the measurement and calibration system.
        A None value is a no-op and does not overwrite an existing resultingProperties.

        Args:
            value: The SwDataDefProps to set

        Returns:
            self for method chaining
        """
        if value is not None:
            self.resultingProperties = value
        return self

    def getResultingRptSwPrototypingAccess(self) -> Optional[RptSwPrototypingAccess]:
        """
        Gets the implemented accessibility of data and modes by the rapid prototyping tooling.

        Returns:
            RptSwPrototypingAccess instance, or None if not set
        """
        return self.resultingRptSwPrototypingAccess

    def setResultingRptSwPrototypingAccess(self, value: Optional[RptSwPrototypingAccess]) -> "McDataInstance":
        """
        Sets the implemented accessibility of data and modes by the rapid prototyping tooling.
        A None value is a no-op and does not overwrite an existing resultingRptSwPrototypingAccess.

        Args:
            value: The RptSwPrototypingAccess to set

        Returns:
            self for method chaining
        """
        if value is not None:
            self.resultingRptSwPrototypingAccess = value
        return self

    def getRole(self) -> Optional[Identifier]:
        """
        Gets the additional information on the role of this data instance, for example in the context of rapid prototyping.

        Returns:
            Identifier representing the role, or None if not set
        """
        return self.role

    def setRole(self, value: Optional[Identifier]) -> "McDataInstance":
        """
        Sets the additional information on the role of this data instance, for example in the context of rapid prototyping.
        A None value is a no-op and does not overwrite an existing role.

        Args:
            value: The role identifier to set

        Returns:
            self for method chaining
        """
        if value is not None:
            self.role = value
        return self

    def getRptImplPolicy(self) -> Optional[RptImplPolicy]:
        """
        Gets the implemented code preparation for rapid prototyping at data accesses for a hook based bypassing.

        Returns:
            RptImplPolicy instance, or None if not set
        """
        return self.rptImplPolicy

    def setRptImplPolicy(self, value: Optional[RptImplPolicy]) -> "McDataInstance":
        """
        Sets the implemented code preparation for rapid prototyping at data accesses for a hook based bypassing.
        A None value is a no-op and does not overwrite an existing policy.

        Args:
            value: The RptImplPolicy to set

        Returns:
            self for method chaining
        """
        if value is not None:
            self.rptImplPolicy = value
        return self

    def createSubElement(self, short_name: str) -> "McDataInstance":
        """
        Creates a McDataInstance sub element and adds it to this data instance.
        If a sub element with the given short name already exists, it is returned instead.

        Args:
            short_name: The short name for the new sub element

        Returns:
            The created (or existing) McDataInstance
        """
        for sub_element in self.subElements:
            if sub_element.short_name == short_name:
                return sub_element
        sub_element = McDataInstance(self, short_name)
        self.subElements.append(sub_element)
        return sub_element

    def getSubElements(self) -> List["McDataInstance"]:
        """
        Gets the sub elements aggregated by this data instance.

        Returns:
            List of McDataInstance sub elements
        """
        return self.subElements

    def getSymbol(self) -> Optional[SymbolString]:
        """
        Gets the symbol used to determine the memory address during final generation of the MC configuration data (e.g. "A2L" file).

        Returns:
            SymbolString representing the symbol, or None if not set
        """
        return self.symbol

    def setSymbol(self, value: Optional[SymbolString]) -> "McDataInstance":
        """
        Sets the symbol used to determine the memory address during final generation of the MC configuration data (e.g. "A2L" file).
        A None value is a no-op and does not overwrite an existing symbol.

        Args:
            value: The SymbolString to set

        Returns:
            self for method chaining
        """
        if value is not None:
            self.symbol = value
        return self


class McSupportData(ARObject):
    """
    Root element for all measurement and calibration support data related to one Implementation artifact on an ECU. There shall be one such element related to the RTE implementation (if it owns MC data) and a separate one for each module or component, which owns private MC data.
    """

    # McSupportData method parity checklist:
    # Spec: AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.pdf, Table 9.1, p.172
    # Spec verified: R23-11
    # [x] __init__                              [x] impl  [x] docstring  [x] test
    # [x] addEmulationSupport                   [x] impl  [x] docstring  [x] test
    # [x] getEmulationSupports                  [x] impl  [x] docstring  [x] test
    # [x] createMcParameterInstance             [x] impl  [x] docstring  [x] test
    # [x] getMcParameterInstances               [x] impl  [x] docstring  [x] test
    # [x] createMcVariableInstance              [x] impl  [x] docstring  [x] test
    # [x] getMcVariableInstances                [x] impl  [x] docstring  [x] test
    # [x] addMeasurableSystemConstantValuesRef  [x] impl  [x] docstring  [x] test
    # [x] getMeasurableSystemConstantValuesRefs [x] impl  [x] docstring  [x] test
    # [x] getRptSupportData                     [x] impl  [x] docstring  [x] test
    # [x] setRptSupportData                     [x] impl  [x] docstring  [x] test

    def __init__(self):
        """
        Initializes the McSupportData with default values.
        """
        super().__init__()

        # Describes the calibration method used by the RTE. This information is not needed for A2L generation, but to setup software emulation in the ECU.
        self.emulationSupports: List[McSwEmulationMethodSupport] = []

        # A data instance to be used for calibration.
        self.mcParameterInstances: List[McDataInstance] = []

        # A data instance to be used for measurement.
        self.mcVariableInstances: List[McDataInstance] = []

        # Sets of system constant values to be transferred to the MCD system, because the system constants have been specified with "swCalibrationAccess" = readonly.
        self.measurableSystemConstantValuesRefs: List[RefType] = []

        # The rapid prototyping support data belonging to this implementation. The aggregtion is <<atpSplitable>> because in case of an already exisiting BSW Implementation model, this description will be added later in the process, namely at code generation time.
        self.rptSupportData: Optional[RptSupportData] = None

    def addEmulationSupport(self, value: Optional[McSwEmulationMethodSupport]) -> "McSupportData":
        """
        Adds an emulation support to this MC support data.
        A None value is a no-op and does not append anything.

        Args:
            value: The emulation support to add

        Returns:
            self for method chaining
        """
        if value is not None:
            self.emulationSupports.append(value)
        return self

    def getEmulationSupports(self) -> List[McSwEmulationMethodSupport]:
        """
        Gets the emulation supports aggregated by this MC support data.

        Returns:
            List of McSwEmulationMethodSupport instances
        """
        return self.emulationSupports

    def createMcParameterInstance(self, short_name: str) -> McDataInstance:
        """
        Creates a McDataInstance for calibration and adds it to this MC support data.
        If a data instance with the given short name already exists, it is returned instead.

        Args:
            short_name: The short name for the new calibration data instance

        Returns:
            The created (or existing) McDataInstance
        """
        for instance in self.mcParameterInstances:
            if instance.short_name == short_name:
                return instance
        instance = McDataInstance(self, short_name)
        self.mcParameterInstances.append(instance)
        return instance

    def getMcParameterInstances(self) -> List[McDataInstance]:
        """
        Gets the calibration data instances aggregated by this MC support data.

        Returns:
            List of McDataInstance instances used for calibration
        """
        return self.mcParameterInstances

    def createMcVariableInstance(self, short_name: str) -> McDataInstance:
        """
        Creates a McDataInstance for measurement and adds it to this MC support data.
        If a data instance with the given short name already exists, it is returned instead.

        Args:
            short_name: The short name for the new measurement data instance

        Returns:
            The created (or existing) McDataInstance
        """
        for instance in self.mcVariableInstances:
            if instance.short_name == short_name:
                return instance
        instance = McDataInstance(self, short_name)
        self.mcVariableInstances.append(instance)
        return instance

    def getMcVariableInstances(self) -> List[McDataInstance]:
        """
        Gets the measurement data instances aggregated by this MC support data.

        Returns:
            List of McDataInstance instances used for measurement
        """
        return self.mcVariableInstances

    def addMeasurableSystemConstantValuesRef(self, value: Optional[RefType]) -> "McSupportData":
        """
        Adds a reference to a set of system constant values to be transferred to the MCD system.
        A None value is a no-op and does not append anything.

        Args:
            value: The reference to a SwSystemconstantValueSet

        Returns:
            self for method chaining
        """
        if value is not None:
            self.measurableSystemConstantValuesRefs.append(value)
        return self

    def getMeasurableSystemConstantValuesRefs(self) -> List[RefType]:
        """
        Gets the references to sets of system constant values to be transferred to the MCD system.

        Returns:
            List of RefType instances referencing SwSystemconstantValueSet elements
        """
        return self.measurableSystemConstantValuesRefs

    def getRptSupportData(self) -> Optional[RptSupportData]:
        """
        Gets the rapid prototyping support data belonging to this implementation.

        Returns:
            RptSupportData instance, or None if not set
        """
        return self.rptSupportData

    def setRptSupportData(self, value: Optional[RptSupportData]) -> "McSupportData":
        """
        Sets the rapid prototyping support data belonging to this implementation.
        A None value is a no-op and does not overwrite existing support data.

        Args:
            value: The rapid prototyping support data to set

        Returns:
            self for method chaining
        """
        if value is not None:
            self.rptSupportData = value
        return self


__all__ = [
    "ImplementationElementInParameterInstanceRef",
    "McDataAccessDetails",
    "McDataInstance",
    "McFunction",
    "McParameterElementGroup",
    "McSupportData",
    "McSwEmulationMethodSupport",
    "RoleBasedMcDataAssignment",
    "RteEventInEcuInstanceRef",
    "VariableAccessInEcuInstanceRef",
]
