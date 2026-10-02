"""
This module contains classes for representing AUTOSAR measurement and calibration
support data (MC support data) in software component and BSW module templates.
"""

from __future__ import annotations
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.StereotypeMixins import VariationPointCapable

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
    Instance reference to an RTE event in the context of an ECU extract. The navigation path begins at the root composition of the ECU extract, passes through the atomic component that contains the RTE event and ends at the RTE event itself. (XSD-only class: no own spec table in the repo corpus; attributes derived from the XSD group RTE-EVENT-IN-ECU-INSTANCE-REF.)
    """

    # RteEventInEcuInstanceRef method parity checklist:
    # Spec: XSD-only, AUTOSAR_00052.xsd line 100605 (no own table in repo corpus)
    # XSD verified: AUTOSAR_00052.xsd
    # Columns: impl / docstring / test / reader / writer / release   ([—] = no XML element)
    # [x] __init__                        [x] impl  [x] docstring  [x] test  [—] reader  [—] writer  R23-11
    # [x] getContextRootCompositionRef    [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setContextRootCompositionRef    [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getContextAtomicComponentRef    [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setContextAtomicComponentRef    [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getTargetRteEventRef            [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setTargetRteEventRef            [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11

    def __init__(self):
        super().__init__()

        # CONTEXT-ROOT-COMPOSITION-REF (DEST ROOT-SW-COMPOSITION-PROTOTYPE--SUBTYPES-ENUM); xml.sequenceOffset=20
        self.contextRootCompositionRef: Optional[RefType] = None

        # CONTEXT-ATOMIC-COMPONENT-REF (DEST SW-COMPONENT-PROTOTYPE--SUBTYPES-ENUM); xml.sequenceOffset=30
        self.contextAtomicComponentRef: Optional[RefType] = None

        # TARGET-RTE-EVENT-REF (DEST RTE-EVENT--SUBTYPES-ENUM); xml.sequenceOffset=40
        self.targetRteEventRef: Optional[RefType] = None

    def getContextRootCompositionRef(self) -> Optional[RefType]:
        """The root composition of the ECU extract that contains the referenced RTE event."""
        return self.contextRootCompositionRef

    def setContextRootCompositionRef(self, value: Optional[RefType]) -> RteEventInEcuInstanceRef:
        """
        The root composition of the ECU extract that contains the referenced RTE event.
        A None value is a no-op and does not overwrite an existing contextRootCompositionRef.
        """
        if value is not None:
            self.contextRootCompositionRef = value
        return self

    def getContextAtomicComponentRef(self) -> Optional[RefType]:
        """The atomic component in the ECU extract that contains the referenced RTE event."""
        return self.contextAtomicComponentRef

    def setContextAtomicComponentRef(self, value: Optional[RefType]) -> RteEventInEcuInstanceRef:
        """
        The atomic component in the ECU extract that contains the referenced RTE event.
        A None value is a no-op and does not overwrite an existing contextAtomicComponentRef.
        """
        if value is not None:
            self.contextAtomicComponentRef = value
        return self

    def getTargetRteEventRef(self) -> Optional[RefType]:
        """The target RTE event."""
        return self.targetRteEventRef

    def setTargetRteEventRef(self, value: Optional[RefType]) -> RteEventInEcuInstanceRef:
        """
        The target RTE event.
        A None value is a no-op and does not overwrite an existing targetRteEventRef.
        """
        if value is not None:
            self.targetRteEventRef = value
        return self


class VariableAccessInEcuInstanceRef(AtpInstanceRef):
    """
    Instance reference to a VariableAccess in the context of an ECU extract. The navigation path begins at the root composition of the ECU extract, passes through the atomic component that contains the VariableAccess and ends at the VariableAccess itself. (XSD-only class: no own spec table in the repo corpus; attributes derived from the XSD group VARIABLE-ACCESS-IN-ECU-INSTANCE-REF.)
    """

    # VariableAccessInEcuInstanceRef method parity checklist:
    # Spec: XSD-only, AUTOSAR_00052.xsd line 129566 (no own table in repo corpus)
    # XSD verified: AUTOSAR_00052.xsd
    # Columns: impl / docstring / test / reader / writer / release   ([—] = no XML element)
    # [x] __init__                        [x] impl  [x] docstring  [x] test  [—] reader  [—] writer  R23-11
    # [x] getContextRootCompositionRef    [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setContextRootCompositionRef    [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getContextAtomicComponentRef    [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setContextAtomicComponentRef    [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getTargetVariableAccessRef      [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setTargetVariableAccessRef      [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11

    def __init__(self):
        super().__init__()

        # CONTEXT-ROOT-COMPOSITION-REF (DEST ROOT-SW-COMPOSITION-PROTOTYPE--SUBTYPES-ENUM); xml.sequenceOffset=20
        self.contextRootCompositionRef: Optional[RefType] = None

        # CONTEXT-ATOMIC-COMPONENT-REF (DEST SW-COMPONENT-PROTOTYPE--SUBTYPES-ENUM); xml.sequenceOffset=30
        self.contextAtomicComponentRef: Optional[RefType] = None

        # TARGET-VARIABLE-ACCESS-REF (DEST VARIABLE-ACCESS--SUBTYPES-ENUM); xml.sequenceOffset=40
        self.targetVariableAccessRef: Optional[RefType] = None

    def getContextRootCompositionRef(self) -> Optional[RefType]:
        """The root composition of the ECU extract that contains the referenced VariableAccess."""
        return self.contextRootCompositionRef

    def setContextRootCompositionRef(self, value: Optional[RefType]) -> VariableAccessInEcuInstanceRef:
        """
        The root composition of the ECU extract that contains the referenced VariableAccess.
        A None value is a no-op and does not overwrite an existing contextRootCompositionRef.
        """
        if value is not None:
            self.contextRootCompositionRef = value
        return self

    def getContextAtomicComponentRef(self) -> Optional[RefType]:
        """The atomic component in the ECU extract that contains the referenced VariableAccess."""
        return self.contextAtomicComponentRef

    def setContextAtomicComponentRef(self, value: Optional[RefType]) -> VariableAccessInEcuInstanceRef:
        """
        The atomic component in the ECU extract that contains the referenced VariableAccess.
        A None value is a no-op and does not overwrite an existing contextAtomicComponentRef.
        """
        if value is not None:
            self.contextAtomicComponentRef = value
        return self

    def getTargetVariableAccessRef(self) -> Optional[RefType]:
        """The target VariableAccess."""
        return self.targetVariableAccessRef

    def setTargetVariableAccessRef(self, value: Optional[RefType]) -> VariableAccessInEcuInstanceRef:
        """
        The target VariableAccess.
        A None value is a no-op and does not overwrite an existing targetVariableAccessRef.
        """
        if value is not None:
            self.targetVariableAccessRef = value
        return self


class McDataAccessDetails(ARObject):
    """
    This meta-class allows to attach detailed information about the usage of a data buffer by the RTE to a corresponding McDataInstance. Use Case: Direct memory access to RTE internal buffers for rapid prototyping. In case of implicit communication, the various task local buffers need to be identified in relation to RTE events and variable access points. Note that the SwComponentPrototype, the RunnableEntity and the VariableDataPrototype are implicitly given be the referred instances of RTEEvent and VariableAccess.
    """

    # McDataAccessDetails method parity checklist:
    # Spec: AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.pdf, Table 9.12, p.195
    # Columns: impl / docstring / test / reader / writer / release   ([—] = no XML element)
    # [x] __init__    [x] impl  [x] docstring  [x] test  [—] reader  [—] writer  R23-11
    # [x] getRteEventIRefs            [x] impl  [x] docstring  [x] test  [x] reader  [x] writer  R23-11
    # [x] addRteEventIRef             [x] impl  [x] docstring  [x] test  [x] reader  [x] writer  R23-11
    # [x] getVariableAccessIRefs      [x] impl  [x] docstring  [x] test  [x] reader  [x] writer  R23-11
    # [x] addVariableAccessIRef       [x] impl  [x] docstring  [x] test  [x] reader  [x] writer  R23-11

    def __init__(self):
        super().__init__()

        # The RTE event used to receive the data via this buffer. InstanceRef implemented by: RteEventInEcuInstance Ref
        self.rteEventIRefs: List[RteEventInEcuInstanceRef] = []

        # The VariableAccess for which the data buffer is used. InstanceRef implemented by: VariableAccessInEcu InstanceRef
        self.variableAccessIRefs: List[VariableAccessInEcuInstanceRef] = []

    def addRteEventIRef(self, value: Optional[RteEventInEcuInstanceRef]) -> McDataAccessDetails:
        """
        The RTE event used to receive the data via this buffer. InstanceRef implemented by: RteEventInEcuInstance Ref
        A None value is a no-op and does not append to rteEventIRefs.
        """
        if value is not None:
            self.rteEventIRefs.append(value)
        return self

    def getRteEventIRefs(self) -> List[RteEventInEcuInstanceRef]:
        """
        The RTE event used to receive the data via this buffer. InstanceRef implemented by: RteEventInEcuInstance Ref
        """
        return self.rteEventIRefs

    def addVariableAccessIRef(self, value: Optional[VariableAccessInEcuInstanceRef]) -> McDataAccessDetails:
        """
        The VariableAccess for which the data buffer is used. InstanceRef implemented by: VariableAccessInEcu InstanceRef
        A None value is a no-op and does not append to variableAccessIRefs.
        """
        if value is not None:
            self.variableAccessIRefs.append(value)
        return self

    def getVariableAccessIRefs(self) -> List[VariableAccessInEcuInstanceRef]:
        """
        The VariableAccess for which the data buffer is used. InstanceRef implemented by: VariableAccessInEcu InstanceRef
        """
        return self.variableAccessIRefs


class McParameterElementGroup(ARObject):
    """
    Denotes a group of calibration parameters which are handled by the RTE as one data structure.
    """

    # McParameterElementGroup method parity checklist:
    # Spec: AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.pdf, Table 9.6, p.181
    # Columns: impl / docstring / test / reader / writer / release   ([—] = no XML element)
    # [x] __init__    [x] impl  [x] docstring  [x] test  [—] reader  [—] writer  R23-11
    # [x] getRamLocationRef           [x] impl  [x] docstring  [x] test  [x] reader  [x] writer  R23-11
    # [x] setRamLocationRef           [x] impl  [x] docstring  [x] test  [x] reader  [x] writer  R23-11
    # [x] getRomLocationRef           [x] impl  [x] docstring  [x] test  [x] reader  [x] writer  R23-11
    # [x] setRomLocationRef           [x] impl  [x] docstring  [x] test  [x] reader  [x] writer  R23-11
    # [x] getShortLabel               [x] impl  [x] docstring  [x] test  [x] reader  [x] writer  R23-11
    # [x] setShortLabel               [x] impl  [x] docstring  [x] test  [x] reader  [x] writer  R23-11

    def __init__(self):
        super().__init__()

        # Refers to the RAM location of this parameter group. To be used for the init-RAM method.
        self.ramLocationRef: Optional[RefType] = None

        # Refers to the ROM location of this parameter group. To be used for the init-RAM method.
        self.romLocationRef: Optional[RefType] = None

        # Assigns a name to this element. Tags: xml.sequenceOffset=-100
        self.shortLabel: Optional[Identifier] = None

    def getRamLocationRef(self) -> Optional[RefType]:
        """
        Refers to the RAM location of this parameter group. To be used for the init-RAM method.
        """
        return self.ramLocationRef

    def setRamLocationRef(self, value: Optional[RefType]) -> McParameterElementGroup:
        """
        Refers to the RAM location of this parameter group. To be used for the init-RAM method.
        A None value is a no-op and does not overwrite an existing ramLocationRef.
        """
        if value is not None:
            self.ramLocationRef = value
        return self

    def getRomLocationRef(self) -> Optional[RefType]:
        """
        Refers to the ROM location of this parameter group. To be used for the init-RAM method.
        """
        return self.romLocationRef

    def setRomLocationRef(self, value: Optional[RefType]) -> McParameterElementGroup:
        """
        Refers to the ROM location of this parameter group. To be used for the init-RAM method.
        A None value is a no-op and does not overwrite an existing romLocationRef.
        """
        if value is not None:
            self.romLocationRef = value
        return self

    def getShortLabel(self) -> Optional[Identifier]:
        """
        Assigns a name to this element. Tags: xml.sequenceOffset=-100
        """
        return self.shortLabel

    def setShortLabel(self, value: Optional[Identifier]) -> McParameterElementGroup:
        """
        Assigns a name to this element. Tags: xml.sequenceOffset=-100
        A None value is a no-op and does not overwrite an existing shortLabel.
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
    # Columns: impl / docstring / test / reader / writer / release   ([—] = no XML element)
    # [x] __init__    [x] impl  [x] docstring  [x] test  [—] reader  [—] writer  R23-11
    # [x] getBaseReferenceRef         [x] impl  [x] docstring  [x] test  [x] reader  [x] writer  R23-11
    # [x] setBaseReferenceRef         [x] impl  [x] docstring  [x] test  [x] reader  [x] writer  R23-11
    # [x] getCategory                 [x] impl  [x] docstring  [x] test  [x] reader  [x] writer  R23-11
    # [x] setCategory                 [x] impl  [x] docstring  [x] test  [x] reader  [x] writer  R23-11
    # [x] getElementGroups            [x] impl  [x] docstring  [x] test  [x] reader  [x] writer  R23-11
    # [x] addElementGroup             [x] impl  [x] docstring  [x] test  [x] reader  [x] writer  R23-11
    # [x] getReferenceTableRef        [x] impl  [x] docstring  [x] test  [x] reader  [x] writer  R23-11
    # [x] setReferenceTableRef        [x] impl  [x] docstring  [x] test  [x] reader  [x] writer  R23-11
    # [x] getShortLabel               [x] impl  [x] docstring  [x] test  [x] reader  [x] writer  R23-11
    # [x] setShortLabel               [x] impl  [x] docstring  [x] test  [x] reader  [x] writer  R23-11

    def __init__(self):
        super().__init__()

        # Refers to the base pointer in case of the double-pointered method.
        self.baseReferenceRef: Optional[RefType] = None

        # Identifies the actual method. The possible names shall correspond to the symbols of the ECU configuration parameter for the calibration method of the RTE, and can include vendor specific methods. Tags: xml.sequenceOffset=-90
        self.category: Optional[Identifier] = None

        # Denotes the grouping of calibration parameters in the actual RTE code. Depending on the category, this information maybe required to set up the emulation code.
        self.elementGroups: List[McParameterElementGroup] = []

        # Refers to the pointer table in case of the single-pointered method.
        self.referenceTableRef: Optional[RefType] = None

        # Assigns a name to this element. Tags: xml.sequenceOffset=-100
        self.shortLabel: Optional[Identifier] = None

    def getBaseReferenceRef(self) -> Optional[RefType]:
        """
        Refers to the base pointer in case of the double-pointered method.
        """
        return self.baseReferenceRef

    def setBaseReferenceRef(self, value: Optional[RefType]) -> McSwEmulationMethodSupport:
        """
        Refers to the base pointer in case of the double-pointered method.
        A None value is a no-op and does not overwrite an existing baseReferenceRef.
        """
        if value is not None:
            self.baseReferenceRef = value
        return self

    def getCategory(self) -> Optional[Identifier]:
        """
        Identifies the actual method. The possible names shall correspond to the symbols of the ECU configuration parameter for the calibration method of the RTE, and can include vendor specific methods. Tags: xml.sequenceOffset=-90
        """
        return self.category

    def setCategory(self, value: Optional[Identifier]) -> McSwEmulationMethodSupport:
        """
        Identifies the actual method. The possible names shall correspond to the symbols of the ECU configuration parameter for the calibration method of the RTE, and can include vendor specific methods. Tags: xml.sequenceOffset=-90
        A None value is a no-op and does not overwrite an existing category.
        """
        if value is not None:
            self.category = value
        return self

    def addElementGroup(self, value: Optional[McParameterElementGroup]) -> McSwEmulationMethodSupport:
        """
        Denotes the grouping of calibration parameters in the actual RTE code. Depending on the category, this information maybe required to set up the emulation code.
        A None value is a no-op and does not append to elementGroups.
        """
        if value is not None:
            self.elementGroups.append(value)
        return self

    def getElementGroups(self) -> List[McParameterElementGroup]:
        """
        Denotes the grouping of calibration parameters in the actual RTE code. Depending on the category, this information maybe required to set up the emulation code.
        """
        return self.elementGroups

    def getReferenceTableRef(self) -> Optional[RefType]:
        """
        Refers to the pointer table in case of the single-pointered method.
        """
        return self.referenceTableRef

    def setReferenceTableRef(self, value: Optional[RefType]) -> McSwEmulationMethodSupport:
        """
        Refers to the pointer table in case of the single-pointered method.
        A None value is a no-op and does not overwrite an existing referenceTableRef.
        """
        if value is not None:
            self.referenceTableRef = value
        return self

    def getShortLabel(self) -> Optional[Identifier]:
        """
        Assigns a name to this element. Tags: xml.sequenceOffset=-100
        """
        return self.shortLabel

    def setShortLabel(self, value: Optional[Identifier]) -> McSwEmulationMethodSupport:
        """
        Assigns a name to this element. Tags: xml.sequenceOffset=-100
        A None value is a no-op and does not overwrite an existing shortLabel.
        """
        if value is not None:
            self.shortLabel = value
        return self


class ImplementationElementInParameterInstanceRef(ARObject):
    """
    Describes a reference to a particular ImplementationDataTypeElement instance in the context of a given ParameterDataPrototype. Thus it refers to a particular element in the implementation description of a software data structure. Use Case: The RTE generator publishes its generated structure of calibration parameters in its BSW module description using the "constantMemory" role of ParameterDataPrototypes. Each ParameterData Prototype describes a group of single calibration parameters. In order to point to these single parameters, this "instance ref" is needed. Note that this class follows the pattern of an InstanceRef but is not implemented based on the abstract classes because the ImplementationDataType isn't either, especially because ImplementationDataType Element isn't derived from AtpPrototype.
    """

    # ImplementationElementInParameterInstanceRef method parity checklist:
    # Spec: AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.pdf, Table 9.7, p.184
    # Columns: impl / docstring / test / reader / writer / release   ([—] = no XML element)
    # [x] __init__    [x] impl  [x] docstring  [x] test  [—] reader  [—] writer  R23-11
    # [x] getContextRef               [x] impl  [x] docstring  [x] test  [x] reader  [x] writer  R23-11
    # [x] setContextRef               [x] impl  [x] docstring  [x] test  [x] reader  [x] writer  R23-11
    # [x] getTargetRef                [x] impl  [x] docstring  [x] test  [x] reader  [x] writer  R23-11
    # [x] setTargetRef                [x] impl  [x] docstring  [x] test  [x] reader  [x] writer  R23-11

    def __init__(self):
        super().__init__()

        # The context for the referred element. Tags: xml.sequenceOffset=20
        self.contextRef: Optional[RefType] = None

        # The referred data element. Tags: xml.sequenceOffset=30
        self.targetRef: Optional[RefType] = None

    def getContextRef(self) -> Optional[RefType]:
        """
        The context for the referred element. Tags: xml.sequenceOffset=20
        """
        return self.contextRef

    def setContextRef(self, value: Optional[RefType]) -> ImplementationElementInParameterInstanceRef:
        """
        The context for the referred element. Tags: xml.sequenceOffset=20
        A None value is a no-op and does not overwrite an existing contextRef.
        """
        if value is not None:
            self.contextRef = value
        return self

    def getTargetRef(self) -> Optional[RefType]:
        """
        The referred data element. Tags: xml.sequenceOffset=30
        """
        return self.targetRef

    def setTargetRef(self, value: Optional[RefType]) -> ImplementationElementInParameterInstanceRef:
        """
        The referred data element. Tags: xml.sequenceOffset=30
        A None value is a no-op and does not overwrite an existing targetRef.
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
    # Columns: impl / docstring / test / reader / writer / release   ([—] = no XML element)
    # [x] __init__    [x] impl  [x] docstring  [x] test  [—] reader  [—] writer  R23-11
    # [x] getDefCalprmSet             [x] impl  [x] docstring  [x] test  [x] reader  [x] writer  R23-11
    # [x] setDefCalprmSet             [x] impl  [x] docstring  [x] test  [x] reader  [x] writer  R23-11
    # [x] getInMeasurementSet         [x] impl  [x] docstring  [x] test  [x] reader  [x] writer  R23-11
    # [x] setInMeasurementSet         [x] impl  [x] docstring  [x] test  [x] reader  [x] writer  R23-11
    # [x] getLocMeasurementSet        [x] impl  [x] docstring  [x] test  [x] reader  [x] writer  R23-11
    # [x] setLocMeasurementSet        [x] impl  [x] docstring  [x] test  [x] reader  [x] writer  R23-11
    # [x] getOutMeasurementSet        [x] impl  [x] docstring  [x] test  [x] reader  [x] writer  R23-11
    # [x] setOutMeasurementSet        [x] impl  [x] docstring  [x] test  [x] reader  [x] writer  R23-11
    # [x] getRefCalprmSet             [x] impl  [x] docstring  [x] test  [x] reader  [x] writer  R23-11
    # [x] setRefCalprmSet             [x] impl  [x] docstring  [x] test  [x] reader  [x] writer  R23-11
    # [x] getSubFunctionRefs          [x] impl  [x] docstring  [x] test  [x] reader  [x] writer  R23-11
    # [x] addSubFunctionRef           [x] impl  [x] docstring  [x] test  [x] reader  [x] writer  R23-11

    def __init__(self, parent: ARObject, short_name: str):
        super().__init__(parent, short_name)

        # Refers to the set of adjustable data (= calibration parameters) defined in this function. Stereotypes: atpSplitable Tags: atp.Splitkey=defCalprmSet xml.sequenceOffset=10
        self.defCalprmSet: Optional[McFunctionDataRefSet] = None

        # Refers to the set of measurable input data for this function. Stereotypes: atpSplitable Tags: atp.Splitkey=inMeasurementSet xml.sequenceOffset=30
        self.inMeasurementSet: Optional[McFunctionDataRefSet] = None

        # Refers to the set of measurable local data in this function. Stereotypes: atpSplitable Tags: atp.Splitkey=locMeasurementSet xml.sequenceOffset=50
        self.locMeasurementSet: Optional[McFunctionDataRefSet] = None

        # Refers to the set of measurable output data from this function. Stereotypes: atpSplitable Tags: atp.Splitkey=outMeasurementSet
        self.outMeasurementSet: Optional[McFunctionDataRefSet] = None

        # Refers to the set of adjustable data (= calibration parameters) referred by this function. Stereotypes: atpSplitable Tags: atp.Splitkey=refCalprmSet xml.sequenceOffset=20
        self.refCalprmSet: Optional[McFunctionDataRefSet] = None

        # A sub-function that is seen as part of the enclosing function. Stereotypes: atpSplitable Tags: atp.Splitkey=subFunction xml.sequenceOffset=70
        self.subFunctionRefs: List[RefType] = []

    def getDefCalprmSet(self) -> Optional[McFunctionDataRefSet]:
        """
        Refers to the set of adjustable data (= calibration parameters) defined in this function. Stereotypes: atpSplitable Tags: atp.Splitkey=defCalprmSet xml.sequenceOffset=10
        """
        return self.defCalprmSet

    def setDefCalprmSet(self, value: Optional[McFunctionDataRefSet]) -> McFunction:
        """
        Refers to the set of adjustable data (= calibration parameters) defined in this function. Stereotypes: atpSplitable Tags: atp.Splitkey=defCalprmSet xml.sequenceOffset=10
        A None value is a no-op and does not overwrite an existing defCalprmSet.
        """
        if value is not None:
            self.defCalprmSet = value
        return self

    def getInMeasurementSet(self) -> Optional[McFunctionDataRefSet]:
        """
        Refers to the set of measurable input data for this function. Stereotypes: atpSplitable Tags: atp.Splitkey=inMeasurementSet xml.sequenceOffset=30
        """
        return self.inMeasurementSet

    def setInMeasurementSet(self, value: Optional[McFunctionDataRefSet]) -> McFunction:
        """
        Refers to the set of measurable input data for this function. Stereotypes: atpSplitable Tags: atp.Splitkey=inMeasurementSet xml.sequenceOffset=30
        A None value is a no-op and does not overwrite an existing inMeasurementSet.
        """
        if value is not None:
            self.inMeasurementSet = value
        return self

    def getLocMeasurementSet(self) -> Optional[McFunctionDataRefSet]:
        """
        Refers to the set of measurable local data in this function. Stereotypes: atpSplitable Tags: atp.Splitkey=locMeasurementSet xml.sequenceOffset=50
        """
        return self.locMeasurementSet

    def setLocMeasurementSet(self, value: Optional[McFunctionDataRefSet]) -> McFunction:
        """
        Refers to the set of measurable local data in this function. Stereotypes: atpSplitable Tags: atp.Splitkey=locMeasurementSet xml.sequenceOffset=50
        A None value is a no-op and does not overwrite an existing locMeasurementSet.
        """
        if value is not None:
            self.locMeasurementSet = value
        return self

    def getOutMeasurementSet(self) -> Optional[McFunctionDataRefSet]:
        """
        Refers to the set of measurable output data from this function. Stereotypes: atpSplitable Tags: atp.Splitkey=outMeasurementSet
        """
        return self.outMeasurementSet

    def setOutMeasurementSet(self, value: Optional[McFunctionDataRefSet]) -> McFunction:
        """
        Refers to the set of measurable output data from this function. Stereotypes: atpSplitable Tags: atp.Splitkey=outMeasurementSet
        A None value is a no-op and does not overwrite an existing outMeasurementSet.
        """
        if value is not None:
            self.outMeasurementSet = value
        return self

    def getRefCalprmSet(self) -> Optional[McFunctionDataRefSet]:
        """
        Refers to the set of adjustable data (= calibration parameters) referred by this function. Stereotypes: atpSplitable Tags: atp.Splitkey=refCalprmSet xml.sequenceOffset=20
        """
        return self.refCalprmSet

    def setRefCalprmSet(self, value: Optional[McFunctionDataRefSet]) -> McFunction:
        """
        Refers to the set of adjustable data (= calibration parameters) referred by this function. Stereotypes: atpSplitable Tags: atp.Splitkey=refCalprmSet xml.sequenceOffset=20
        A None value is a no-op and does not overwrite an existing refCalprmSet.
        """
        if value is not None:
            self.refCalprmSet = value
        return self

    def addSubFunctionRef(self, value: Optional[RefType]) -> McFunction:
        """
        A sub-function that is seen as part of the enclosing function. Stereotypes: atpSplitable Tags: atp.Splitkey=subFunction xml.sequenceOffset=70
        A None value is a no-op and does not append to subFunctionRefs.
        """
        if value is not None:
            self.subFunctionRefs.append(value)
        return self

    def getSubFunctionRefs(self) -> List[RefType]:
        """
        A sub-function that is seen as part of the enclosing function. Stereotypes: atpSplitable Tags: atp.Splitkey=subFunction xml.sequenceOffset=70
        """
        return self.subFunctionRefs


class RoleBasedMcDataAssignment(ARObject, VariationPointCapable):
    """
    This meta-class allows to define links that specify logical relationships between single McDataInstances. The details on the existence and semantics of such links are not standardized. Possible Use Case: Rapid Prototyping solutions in which additional communication buffers and switches are implemented in the RTE that allow to switch between the usage of the original and the bypass buffers. The different buffers and the switch can be represented by McDataInstances (in order to be accessed by MC tools) which have relationships to each other.
    """

    # RoleBasedMcDataAssignment method parity checklist:
    # Spec: AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.pdf, Table D.55, p.329
    # Columns: impl / docstring / test / reader / writer / release   ([—] = no XML element)
    # [x] __init__    [x] impl  [x] docstring  [x] test  [—] reader  [—] writer  R23-11
    # [x] getExecutionContextRefs     [x] impl  [x] docstring  [x] test  [x] reader  [x] writer  R23-11
    # [x] addExecutionContextRef      [x] impl  [x] docstring  [x] test  [x] reader  [x] writer  R23-11
    # [x] getMcDataInstanceRefs       [x] impl  [x] docstring  [x] test  [x] reader  [x] writer  R23-11
    # [x] addMcDataInstanceRef        [x] impl  [x] docstring  [x] test  [x] reader  [x] writer  R23-11
    # [x] getRole                     [x] impl  [x] docstring  [x] test  [x] reader  [x] writer  R23-11
    # [x] setRole                     [x] impl  [x] docstring  [x] test  [x] reader  [x] writer  R23-11

    def __init__(self):
        super().__init__()

        # Determines the executionContext in which the McData Instance describing a local (e.g Task-Local) buffer of a global buffer is valid.
        self.executionContextRefs: List[RefType] = []

        # The target of the assignment.
        self.mcDataInstanceRefs: List[RefType] = []

        # Shall be used to specify the role of the assigned data instance in relation to the instance that owns the assignment. The standardized roles of the RoleBasedMcData Assignment.role attribute are: • GlobalMeasurementBuffer • RpEnablerFlag • RpRunnableDisablerFlag • BufferOf
        self.role: Optional[Identifier] = None

    def getExecutionContextRefs(self) -> List[RefType]:
        """
        Determines the executionContext in which the McData Instance describing a local (e.g Task-Local) buffer of a global buffer is valid.
        """
        return self.executionContextRefs

    def addExecutionContextRef(self, value: Optional[RefType]) -> RoleBasedMcDataAssignment:
        """
        Determines the executionContext in which the McData Instance describing a local (e.g Task-Local) buffer of a global buffer is valid.
        A None value is a no-op and does not append to executionContextRefs.
        """
        if value is not None:
            self.executionContextRefs.append(value)
        return self

    def getMcDataInstanceRefs(self) -> List[RefType]:
        """
        The target of the assignment.
        """
        return self.mcDataInstanceRefs

    def addMcDataInstanceRef(self, value: Optional[RefType]) -> RoleBasedMcDataAssignment:
        """
        The target of the assignment.
        A None value is a no-op and does not append to mcDataInstanceRefs.
        """
        if value is not None:
            self.mcDataInstanceRefs.append(value)
        return self

    def getRole(self) -> Optional[Identifier]:
        """
        Shall be used to specify the role of the assigned data instance in relation to the instance that owns the assignment. The standardized roles of the RoleBasedMcData Assignment.role attribute are: • GlobalMeasurementBuffer • RpEnablerFlag • RpRunnableDisablerFlag • BufferOf
        """
        return self.role

    def setRole(self, value: Optional[Identifier]) -> RoleBasedMcDataAssignment:
        """
        Shall be used to specify the role of the assigned data instance in relation to the instance that owns the assignment. The standardized roles of the RoleBasedMcData Assignment.role attribute are: • GlobalMeasurementBuffer • RpEnablerFlag • RpRunnableDisablerFlag • BufferOf
        A None value is a no-op and does not overwrite an existing role.
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
    # Columns: impl / docstring / test / reader / writer / release   ([—] = no XML element)
    # [x] __init__    [x] impl  [x] docstring  [x] test  [—] reader  [—] writer  R23-11
    # [x] getArraySize                [x] impl  [x] docstring  [x] test  [x] reader  [x] writer  R23-11
    # [x] setArraySize                [x] impl  [x] docstring  [x] test  [x] reader  [x] writer  R23-11
    # [x] getDisplayIdentifier        [x] impl  [x] docstring  [x] test  [x] reader  [x] writer  R23-11
    # [x] setDisplayIdentifier        [x] impl  [x] docstring  [x] test  [x] reader  [x] writer  R23-11
    # [x] getFlatMapEntryRef          [x] impl  [x] docstring  [x] test  [x] reader  [x] writer  R23-11
    # [x] setFlatMapEntryRef          [x] impl  [x] docstring  [x] test  [x] reader  [x] writer  R23-11
    # [x] getInstanceInMemory         [x] impl  [x] docstring  [x] test  [x] reader  [x] writer  R23-11
    # [x] setInstanceInMemory         [x] impl  [x] docstring  [x] test  [x] reader  [x] writer  R23-11
    # [x] getMcDataAccessDetails      [x] impl  [x] docstring  [x] test  [x] reader  [x] writer  R23-11
    # [x] setMcDataAccessDetails      [x] impl  [x] docstring  [x] test  [x] reader  [x] writer  R23-11
    # [x] getMcDataAssignments        [x] impl  [x] docstring  [x] test  [x] reader  [x] writer  R23-11
    # [x] addMcDataAssignment         [x] impl  [x] docstring  [x] test  [x] reader  [x] writer  R23-11
    # [x] getResultingProperties      [x] impl  [x] docstring  [x] test  [x] reader  [x] writer  R23-11
    # [x] setResultingProperties      [x] impl  [x] docstring  [x] test  [x] reader  [x] writer  R23-11
    # [x] getResultingRptSwPrototypingAccess[x] impl  [x] docstring  [x] test  [x] reader  [x] writer  R23-11
    # [x] setResultingRptSwPrototypingAccess[x] impl  [x] docstring  [x] test  [x] reader  [x] writer  R23-11
    # [x] getRole                     [x] impl  [x] docstring  [x] test  [x] reader  [x] writer  R23-11
    # [x] setRole                     [x] impl  [x] docstring  [x] test  [x] reader  [x] writer  R23-11
    # [x] getRptImplPolicy            [x] impl  [x] docstring  [x] test  [x] reader  [x] writer  R23-11
    # [x] setRptImplPolicy            [x] impl  [x] docstring  [x] test  [x] reader  [x] writer  R23-11
    # [x] getSubElements              [x] impl  [x] docstring  [x] test  [x] reader  [x] writer  R23-11
    # [x] createSubElement            [x] impl  [x] docstring  [x] test  [x] reader  [x] writer  R23-11
    # [x] getSymbol                   [x] impl  [x] docstring  [x] test  [x] reader  [x] writer  R23-11
    # [x] setSymbol                   [x] impl  [x] docstring  [x] test  [x] reader  [x] writer  R23-11

    def __init__(self, parent: ARObject, short_name: str):
        super().__init__(parent, short_name)

        # The existence of this attribute turns the data instance into an array of data. The attribute determines the size of the array in terms of number of elements.
        self.arraySize: Optional[PositiveInteger] = None

        # An optional attribute to be used to set the ASAM ASAP2 DISPLAY_IDENTIFIER attribute.
        self.displayIdentifier: Optional[McdIdentifier] = None

        # Reference to the corresponding entry in the ECU Flat Map. This allows to trace back to the original specification of the generated data instance. This link shall be added by the RTE generator mainly for documentation purposes. The reference is optional because • The McDataInstance may represent an array or struct in which only the subElements correspond to FlatMap entries. • The McDataInstance may represent a task local buffer for rapid prototyping access which is different from the "main instance" used for measurement access.
        self.flatMapEntryRef: Optional[RefType] = None

        # Reference to the corresponding data instance in the description of calibration data structures published by the RTE generator. This is used to support emulation methods inside the ECU, it is not required for A2L generation.
        self.instanceInMemory: Optional[ImplementationElementInParameterInstanceRef] = None

        # Refers to "upstream" information on how the RTE uses this data instance. Use Case: Rapid Prototyping
        self.mcDataAccessDetails: Optional[McDataAccessDetails] = None

        # An assignment between McDataInstances. This supports the indication of related McDataElement implementing the of "RP global buffer", "RP global measurement buffer", "RP enabler flag".
        self.mcDataAssignments: List[RoleBasedMcDataAssignment] = []

        # These are the generated properties resulting from decisions taken by the RTE generator for the actually implemented data instance. Only those properties are relevant here, which are needed for the measurement and calibration system. Stereotypes: atpSplitable Tags: atp.Splitkey=resultingProperties
        self.resultingProperties: Optional[SwDataDefProps] = None

        # Describes the implemented accessibility of data and modes by the rapid prototyping tooling.
        self.resultingRptSwPrototypingAccess: Optional[RptSwPrototypingAccess] = None

        # An optional attribute to be used for additional information on the role of this data instance, for example in the context of rapid prototyping.
        self.role: Optional[Identifier] = None

        # Describes the implemented code preparation for rapid prototyping at data accesses for a hook based bypassing.
        self.rptImplPolicy: Optional[RptImplPolicy] = None

        # This relation indicates, that the target element is part of a "struct" which is given by the source element. This information will be used by the final generator to set up the correct addressing scheme. Stereotypes: atpSplitable; atpVariation Tags: atp.Splitkey=subElement.shortName, sub Element.variationPoint.shortLabel vh.latestBindingTime=preCompileTime
        self.subElements: List[McDataInstance] = []

        # This String is used to determine the memory address during final generation of the MC configuration data (e.g. "A2L" file) . It shall be the name of the element in the programming language such that it can be identified in linker generated information. In case the McDataInstance is part of composite data in the programming language, the symbol String may include parts denoting the element context, unless the context is given by the symbol attribute of an enclosing McDataInstance. This means in particular for the C language that the "." character shall be used as a separator between the name of a "struct" variable the name of one of its elements. The symbol can differ from the shortName in case of generated C data declarations. It is an optional attribute since it may be missing in case the instance represents an element (e.g. a single array element) which has no name in the linker map. Stereotypes: atpSplitable Tags: atp.Splitkey=symbol
        self.symbol: Optional[SymbolString] = None

    def getArraySize(self) -> Optional[PositiveInteger]:
        """
        The existence of this attribute turns the data instance into an array of data. The attribute determines the size of the array in terms of number of elements.
        """
        return self.arraySize

    def setArraySize(self, value: Optional[PositiveInteger]) -> McDataInstance:
        """
        The existence of this attribute turns the data instance into an array of data. The attribute determines the size of the array in terms of number of elements.
        A None value is a no-op and does not overwrite an existing arraySize.
        """
        if value is not None:
            self.arraySize = value
        return self

    def getDisplayIdentifier(self) -> Optional[McdIdentifier]:
        """
        An optional attribute to be used to set the ASAM ASAP2 DISPLAY_IDENTIFIER attribute.
        """
        return self.displayIdentifier

    def setDisplayIdentifier(self, value: Optional[McdIdentifier]) -> McDataInstance:
        """
        An optional attribute to be used to set the ASAM ASAP2 DISPLAY_IDENTIFIER attribute.
        A None value is a no-op and does not overwrite an existing displayIdentifier.
        """
        if value is not None:
            self.displayIdentifier = value
        return self

    def getFlatMapEntryRef(self) -> Optional[RefType]:
        """
        Reference to the corresponding entry in the ECU Flat Map. This allows to trace back to the original specification of the generated data instance. This link shall be added by the RTE generator mainly for documentation purposes. The reference is optional because • The McDataInstance may represent an array or struct in which only the subElements correspond to FlatMap entries. • The McDataInstance may represent a task local buffer for rapid prototyping access which is different from the "main instance" used for measurement access.
        """
        return self.flatMapEntryRef

    def setFlatMapEntryRef(self, value: Optional[RefType]) -> McDataInstance:
        """
        Reference to the corresponding entry in the ECU Flat Map. This allows to trace back to the original specification of the generated data instance. This link shall be added by the RTE generator mainly for documentation purposes. The reference is optional because • The McDataInstance may represent an array or struct in which only the subElements correspond to FlatMap entries. • The McDataInstance may represent a task local buffer for rapid prototyping access which is different from the "main instance" used for measurement access.
        A None value is a no-op and does not overwrite an existing flatMapEntryRef.
        """
        if value is not None:
            self.flatMapEntryRef = value
        return self

    def getInstanceInMemory(self) -> Optional[ImplementationElementInParameterInstanceRef]:
        """
        Reference to the corresponding data instance in the description of calibration data structures published by the RTE generator. This is used to support emulation methods inside the ECU, it is not required for A2L generation.
        """
        return self.instanceInMemory

    def setInstanceInMemory(self, value: Optional[ImplementationElementInParameterInstanceRef]) -> McDataInstance:
        """
        Reference to the corresponding data instance in the description of calibration data structures published by the RTE generator. This is used to support emulation methods inside the ECU, it is not required for A2L generation.
        A None value is a no-op and does not overwrite an existing instanceInMemory.
        """
        if value is not None:
            self.instanceInMemory = value
        return self

    def getMcDataAccessDetails(self) -> Optional[McDataAccessDetails]:
        """
        Refers to "upstream" information on how the RTE uses this data instance. Use Case: Rapid Prototyping
        """
        return self.mcDataAccessDetails

    def setMcDataAccessDetails(self, value: Optional[McDataAccessDetails]) -> McDataInstance:
        """
        Refers to "upstream" information on how the RTE uses this data instance. Use Case: Rapid Prototyping
        A None value is a no-op and does not overwrite an existing mcDataAccessDetails.
        """
        if value is not None:
            self.mcDataAccessDetails = value
        return self

    def addMcDataAssignment(self, value: Optional[RoleBasedMcDataAssignment]) -> McDataInstance:
        """
        An assignment between McDataInstances. This supports the indication of related McDataElement implementing the of "RP global buffer", "RP global measurement buffer", "RP enabler flag".
        A None value is a no-op and does not append to mcDataAssignments.
        """
        if value is not None:
            self.mcDataAssignments.append(value)
        return self

    def getMcDataAssignments(self) -> List[RoleBasedMcDataAssignment]:
        """
        An assignment between McDataInstances. This supports the indication of related McDataElement implementing the of "RP global buffer", "RP global measurement buffer", "RP enabler flag".
        """
        return self.mcDataAssignments

    def getResultingProperties(self) -> Optional[SwDataDefProps]:
        """
        These are the generated properties resulting from decisions taken by the RTE generator for the actually implemented data instance. Only those properties are relevant here, which are needed for the measurement and calibration system. Stereotypes: atpSplitable Tags: atp.Splitkey=resultingProperties
        """
        return self.resultingProperties

    def setResultingProperties(self, value: Optional[SwDataDefProps]) -> McDataInstance:
        """
        These are the generated properties resulting from decisions taken by the RTE generator for the actually implemented data instance. Only those properties are relevant here, which are needed for the measurement and calibration system. Stereotypes: atpSplitable Tags: atp.Splitkey=resultingProperties
        A None value is a no-op and does not overwrite an existing resultingProperties.
        """
        if value is not None:
            self.resultingProperties = value
        return self

    def getResultingRptSwPrototypingAccess(self) -> Optional[RptSwPrototypingAccess]:
        """
        Describes the implemented accessibility of data and modes by the rapid prototyping tooling.
        """
        return self.resultingRptSwPrototypingAccess

    def setResultingRptSwPrototypingAccess(self, value: Optional[RptSwPrototypingAccess]) -> McDataInstance:
        """
        Describes the implemented accessibility of data and modes by the rapid prototyping tooling.
        A None value is a no-op and does not overwrite an existing resultingRptSwPrototypingAccess.
        """
        if value is not None:
            self.resultingRptSwPrototypingAccess = value
        return self

    def getRole(self) -> Optional[Identifier]:
        """
        An optional attribute to be used for additional information on the role of this data instance, for example in the context of rapid prototyping.
        """
        return self.role

    def setRole(self, value: Optional[Identifier]) -> McDataInstance:
        """
        An optional attribute to be used for additional information on the role of this data instance, for example in the context of rapid prototyping.
        A None value is a no-op and does not overwrite an existing role.
        """
        if value is not None:
            self.role = value
        return self

    def getRptImplPolicy(self) -> Optional[RptImplPolicy]:
        """
        Describes the implemented code preparation for rapid prototyping at data accesses for a hook based bypassing.
        """
        return self.rptImplPolicy

    def setRptImplPolicy(self, value: Optional[RptImplPolicy]) -> McDataInstance:
        """
        Describes the implemented code preparation for rapid prototyping at data accesses for a hook based bypassing.
        A None value is a no-op and does not overwrite an existing rptImplPolicy.
        """
        if value is not None:
            self.rptImplPolicy = value
        return self

    def createSubElement(self, short_name: str) -> McDataInstance:
        """
        This relation indicates, that the target element is part of a "struct" which is given by the source element. This information will be used by the final generator to set up the correct addressing scheme. Stereotypes: atpSplitable; atpVariation Tags: atp.Splitkey=subElement.shortName, sub Element.variationPoint.shortLabel vh.latestBindingTime=preCompileTime
        """
        for sub_element in self.subElements:
            if sub_element.short_name == short_name:
                return sub_element
        sub_element = McDataInstance(self, short_name)
        self.subElements.append(sub_element)
        return sub_element

    def getSubElements(self) -> List[McDataInstance]:
        """
        This relation indicates, that the target element is part of a "struct" which is given by the source element. This information will be used by the final generator to set up the correct addressing scheme. Stereotypes: atpSplitable; atpVariation Tags: atp.Splitkey=subElement.shortName, sub Element.variationPoint.shortLabel vh.latestBindingTime=preCompileTime
        """
        return self.subElements

    def getSymbol(self) -> Optional[SymbolString]:
        """
        This String is used to determine the memory address during final generation of the MC configuration data (e.g. "A2L" file) . It shall be the name of the element in the programming language such that it can be identified in linker generated information. In case the McDataInstance is part of composite data in the programming language, the symbol String may include parts denoting the element context, unless the context is given by the symbol attribute of an enclosing McDataInstance. This means in particular for the C language that the "." character shall be used as a separator between the name of a "struct" variable the name of one of its elements. The symbol can differ from the shortName in case of generated C data declarations. It is an optional attribute since it may be missing in case the instance represents an element (e.g. a single array element) which has no name in the linker map. Stereotypes: atpSplitable Tags: atp.Splitkey=symbol
        """
        return self.symbol

    def setSymbol(self, value: Optional[SymbolString]) -> McDataInstance:
        """
        This String is used to determine the memory address during final generation of the MC configuration data (e.g. "A2L" file) . It shall be the name of the element in the programming language such that it can be identified in linker generated information. In case the McDataInstance is part of composite data in the programming language, the symbol String may include parts denoting the element context, unless the context is given by the symbol attribute of an enclosing McDataInstance. This means in particular for the C language that the "." character shall be used as a separator between the name of a "struct" variable the name of one of its elements. The symbol can differ from the shortName in case of generated C data declarations. It is an optional attribute since it may be missing in case the instance represents an element (e.g. a single array element) which has no name in the linker map. Stereotypes: atpSplitable Tags: atp.Splitkey=symbol
        A None value is a no-op and does not overwrite an existing symbol.
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
    # Columns: impl / docstring / test / reader / writer / release   ([—] = no XML element)
    # [x] __init__    [x] impl  [x] docstring  [x] test  [—] reader  [—] writer  R23-11
    # [x] getEmulationSupports        [x] impl  [x] docstring  [x] test  [x] reader  [x] writer  R23-11
    # [x] addEmulationSupport         [x] impl  [x] docstring  [x] test  [x] reader  [x] writer  R23-11
    # [x] getMcParameterInstances     [x] impl  [x] docstring  [x] test  [x] reader  [x] writer  R23-11
    # [x] createMcParameterInstance   [x] impl  [x] docstring  [x] test  [x] reader  [x] writer  R23-11
    # [x] getMcVariableInstances      [x] impl  [x] docstring  [x] test  [x] reader  [x] writer  R23-11
    # [x] createMcVariableInstance    [x] impl  [x] docstring  [x] test  [x] reader  [x] writer  R23-11
    # [x] getMeasurableSystemConstantValuesRefs[x] impl  [x] docstring  [x] test  [x] reader  [x] writer  R23-11
    # [x] addMeasurableSystemConstantValuesRef[x] impl  [x] docstring  [x] test  [x] reader  [x] writer  R23-11
    # [x] getRptSupportData           [x] impl  [x] docstring  [x] test  [x] reader  [x] writer  R23-11
    # [x] setRptSupportData           [x] impl  [x] docstring  [x] test  [x] reader  [x] writer  R23-11

    def __init__(self):
        super().__init__()

        # Describes the calibration method used by the RTE. This information is not needed for A2L generation, but to setup software emulation in the ECU. Stereotypes: atpSplitable; atpVariation Tags: atp.Splitkey=emulationSupport, emulation Support.variationPoint.shortLabel vh.latestBindingTime=preCompileTime
        self.emulationSupports: List[McSwEmulationMethodSupport] = []

        # A data instance to be used for calibration. Stereotypes: atpSplitable; atpVariation Tags: atp.Splitkey=mcParameterInstance.shortName, mc ParameterInstance.variationPoint.shortLabel vh.latestBindingTime=postBuild
        self.mcParameterInstances: List[McDataInstance] = []

        # A data instance to be used for measurement. Stereotypes: atpSplitable; atpVariation Tags: atp.Splitkey=mcVariableInstance.shortName, mcVariable Instance.variationPoint.shortLabel vh.latestBindingTime=postBuild
        self.mcVariableInstances: List[McDataInstance] = []

        # Sets of system constant values to be transferred to the MCD system, because the system constants have been specified with "swCalibrationAccess" = readonly.
        self.measurableSystemConstantValuesRefs: List[RefType] = []

        # The rapid prototyping support data belonging to this implementation. The aggregtion is <<atpSplitable>> because in case of an already exisiting BSW Implementation model, this description will be added later in the process, namely at code generation time. Stereotypes: atpSplitable Tags: atp.Splitkey=rptSupportData
        self.rptSupportData: Optional[RptSupportData] = None

    def addEmulationSupport(self, value: Optional[McSwEmulationMethodSupport]) -> McSupportData:
        """
        Describes the calibration method used by the RTE. This information is not needed for A2L generation, but to setup software emulation in the ECU. Stereotypes: atpSplitable; atpVariation Tags: atp.Splitkey=emulationSupport, emulation Support.variationPoint.shortLabel vh.latestBindingTime=preCompileTime
        A None value is a no-op and does not append to emulationSupports.
        """
        if value is not None:
            self.emulationSupports.append(value)
        return self

    def getEmulationSupports(self) -> List[McSwEmulationMethodSupport]:
        """
        Describes the calibration method used by the RTE. This information is not needed for A2L generation, but to setup software emulation in the ECU. Stereotypes: atpSplitable; atpVariation Tags: atp.Splitkey=emulationSupport, emulation Support.variationPoint.shortLabel vh.latestBindingTime=preCompileTime
        """
        return self.emulationSupports

    def createMcParameterInstance(self, short_name: str) -> McDataInstance:
        """
        A data instance to be used for calibration. Stereotypes: atpSplitable; atpVariation Tags: atp.Splitkey=mcParameterInstance.shortName, mc ParameterInstance.variationPoint.shortLabel vh.latestBindingTime=postBuild
        """
        for instance in self.mcParameterInstances:
            if instance.short_name == short_name:
                return instance
        instance = McDataInstance(self, short_name)
        self.mcParameterInstances.append(instance)
        return instance

    def getMcParameterInstances(self) -> List[McDataInstance]:
        """
        A data instance to be used for calibration. Stereotypes: atpSplitable; atpVariation Tags: atp.Splitkey=mcParameterInstance.shortName, mc ParameterInstance.variationPoint.shortLabel vh.latestBindingTime=postBuild
        """
        return self.mcParameterInstances

    def createMcVariableInstance(self, short_name: str) -> McDataInstance:
        """
        A data instance to be used for measurement. Stereotypes: atpSplitable; atpVariation Tags: atp.Splitkey=mcVariableInstance.shortName, mcVariable Instance.variationPoint.shortLabel vh.latestBindingTime=postBuild
        A None value is a no-op and does not overwrite an existing mcVariableInstances.
        """
        for instance in self.mcVariableInstances:
            if instance.short_name == short_name:
                return instance
        instance = McDataInstance(self, short_name)
        self.mcVariableInstances.append(instance)
        return instance

    def getMcVariableInstances(self) -> List[McDataInstance]:
        """
        A data instance to be used for measurement. Stereotypes: atpSplitable; atpVariation Tags: atp.Splitkey=mcVariableInstance.shortName, mcVariable Instance.variationPoint.shortLabel vh.latestBindingTime=postBuild
        """
        return self.mcVariableInstances

    def addMeasurableSystemConstantValuesRef(self, value: Optional[RefType]) -> McSupportData:
        """
        Sets of system constant values to be transferred to the MCD system, because the system constants have been specified with "swCalibrationAccess" = readonly.
        A None value is a no-op and does not append to measurableSystemConstantValuesRefs.
        """
        if value is not None:
            self.measurableSystemConstantValuesRefs.append(value)
        return self

    def getMeasurableSystemConstantValuesRefs(self) -> List[RefType]:
        """
        Sets of system constant values to be transferred to the MCD system, because the system constants have been specified with "swCalibrationAccess" = readonly.
        """
        return self.measurableSystemConstantValuesRefs

    def getRptSupportData(self) -> Optional[RptSupportData]:
        """
        The rapid prototyping support data belonging to this implementation. The aggregtion is <<atpSplitable>> because in case of an already exisiting BSW Implementation model, this description will be added later in the process, namely at code generation time. Stereotypes: atpSplitable Tags: atp.Splitkey=rptSupportData
        """
        return self.rptSupportData

    def setRptSupportData(self, value: Optional[RptSupportData]) -> McSupportData:
        """
        The rapid prototyping support data belonging to this implementation. The aggregtion is <<atpSplitable>> because in case of an already exisiting BSW Implementation model, this description will be added later in the process, namely at code generation time. Stereotypes: atpSplitable Tags: atp.Splitkey=rptSupportData
        A None value is a no-op and does not overwrite an existing rptSupportData.
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
