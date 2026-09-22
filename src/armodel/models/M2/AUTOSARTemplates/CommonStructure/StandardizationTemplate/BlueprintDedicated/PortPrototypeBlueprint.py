"""
This module defines classes for port prototype blueprints in AUTOSAR standardization templates.

Port prototype blueprints provide a way to define standard templates for port prototypes
that can be reused across different AUTOSAR software components. This is particularly useful
for standardization and blueprint-based development approaches in AUTOSAR architecture.

Classes:
    PortPrototypeBlueprintInitValue: Represents initial value specifications for port prototype blueprints
    PortPrototypeBlueprint: Defines a blueprint for port prototypes with communication specifications
    PortPrototypeBlueprintMapping: Maps a PortPrototypeBlueprint to a PortProtoype
"""

from typing import List, Optional

from armodel.models.M2.AUTOSARTemplates.CommonStructure import ValueSpecification
from armodel.models.M2.AUTOSARTemplates.CommonStructure.StandardizationTemplate.AbstractBlueprintStructure import (
    AtpBlueprintMapping,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.AbstractStructure import AtpStructureElement
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import RefType
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.Communication import PPortComSpec, RPortComSpec


class PortPrototypeBlueprintInitValue(ARObject):
    """
    This meta-class represents the ability to express init values in PortPrototypeBlueprints. These init values act as a kind of blueprint from which for example proper ComSpecs can be derived.
    """

    # PortPrototypeBlueprintInitValue method parity checklist:
    # Spec: AUTOSAR_FO_TPS_StandardizationTemplate.pdf, Table 4.10, p.60
    # Columns: impl / docstring / test / reader / writer / release   ([—] = no XML element)
    # [x] __init__                [x] impl  [x] docstring  [x] test  [—] reader  [—] writer  R23-11
    # [x] getDataPrototypeRef     [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setDataPrototypeRef     [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getValue                [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setValue                [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11

    def __init__(self):
        super().__init__()

        # This is the data prototype for which the init value applies Tags: xml.sequenceOffset=30
        self.dataPrototypeRef: Optional[RefType] = None

        # This is the init value for the particular data prototype. Tags: xml.sequenceOffset=40
        self.value: Optional[ValueSpecification] = None

    def getDataPrototypeRef(self) -> Optional[RefType]:
        """
        This is the data prototype for which the init value applies Tags: xml.sequenceOffset=30
        """
        return self.dataPrototypeRef

    def setDataPrototypeRef(self, value: Optional[RefType]) -> "PortPrototypeBlueprintInitValue":
        """
        This is the data prototype for which the init value applies Tags: xml.sequenceOffset=30
        A None value is a no-op and does not overwrite an existing dataPrototypeRef.
        """
        if value is not None:
            self.dataPrototypeRef = value
        return self

    def getValue(self) -> Optional[ValueSpecification]:
        """
        This is the init value for the particular data prototype. Tags: xml.sequenceOffset=40
        """
        return self.value

    def setValue(self, value: Optional[ValueSpecification]) -> "PortPrototypeBlueprintInitValue":
        """
        This is the init value for the particular data prototype. Tags: xml.sequenceOffset=40
        A None value is a no-op and does not overwrite an existing value.
        """
        if value is not None:
            self.value = value
        return self


class PortPrototypeBlueprint(AtpStructureElement):
    """
    This meta-class represents the ability to express a blueprint of a PortPrototype by referring to a particular PortInterface. This blueprint can then be used as a guidance to create particular PortPrototypes which are defined according to this blueprint. By this it is possible to standardize application interfaces without the need to also standardize software-components with PortPrototypes typed by the standardized PortInterfaces. Tags: atp.recommendedPackage=PortPrototypeBlueprints
    """

    # PortPrototypeBlueprint method parity checklist:
    # Spec: AUTOSAR_FO_TPS_StandardizationTemplate.pdf, Table 4.9, p.60
    # Columns: impl / docstring / test / reader / writer / release   ([—] = no XML element)
    # [x] __init__                   [x] impl  [x] docstring  [x] test  [—] reader  [—] writer  R23-11
    # [x] getInitValues              [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setInitValues              [x] impl  [x] docstring  [x] test  [—] reader  [—] writer  R23-11
    # [x] addInitValue               [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getInterfaceRef            [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setInterfaceRef            [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getProvidedComSpecs        [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setProvidedComSpecs        [x] impl  [x] docstring  [x] test  [—] reader  [—] writer  R23-11
    # [x] addProvidedComSpec         [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getRequiredComSpecs        [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setRequiredComSpecs        [x] impl  [x] docstring  [x] test  [—] reader  [—] writer  R23-11
    # [x] addRequiredComSpec         [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11

    def __init__(self, parent, short_name):
        super().__init__(parent, short_name)

        # This specifies the init values for the dataElements in the particular PortPrototypeBlueprint.
        self.initValues: List[PortPrototypeBlueprintInitValue] = []

        # This is the interface for which the blueprint is defined. It may be a blueprint itself  or a standardized PortInterface
        self.interfaceRef: Optional[RefType] = None

        # Provided communication attributes per interface element (data element or operation).
        self.providedComSpecs: List[PPortComSpec] = []

        # Required communication attributes, one for each interface element.
        self.requiredComSpecs: List[RPortComSpec] = []

    def getInitValues(self) -> List[PortPrototypeBlueprintInitValue]:
        """
        This specifies the init values for the dataElements in the particular PortPrototypeBlueprint.
        """
        return self.initValues

    def setInitValues(self, value: Optional[List[PortPrototypeBlueprintInitValue]]) -> "PortPrototypeBlueprint":
        """
        This specifies the init values for the dataElements in the particular PortPrototypeBlueprint.
        A None value is a no-op and does not overwrite the existing initValues list.
        """
        if value is not None:
            self.initValues = value
        return self

    def addInitValue(self, value: Optional[PortPrototypeBlueprintInitValue]) -> "PortPrototypeBlueprint":
        """
        This specifies the init values for the dataElements in the particular PortPrototypeBlueprint.
        A None value is a no-op and does not extend the initValue list.
        """
        if value is not None:
            self.initValues.append(value)
        return self

    def getInterfaceRef(self) -> Optional[RefType]:
        """
        This is the interface for which the blueprint is defined. It may be a blueprint itself  or a standardized PortInterface
        """
        return self.interfaceRef

    def setInterfaceRef(self, value: Optional[RefType]) -> "PortPrototypeBlueprint":
        """
        This is the interface for which the blueprint is defined. It may be a blueprint itself  or a standardized PortInterface
        A None value is a no-op and does not overwrite an existing interfaceRef.
        """
        if value is not None:
            self.interfaceRef = value
        return self

    def getProvidedComSpecs(self) -> List[PPortComSpec]:
        """
        Provided communication attributes per interface element (data element or operation).
        """
        return self.providedComSpecs

    def setProvidedComSpecs(self, value: Optional[List[PPortComSpec]]) -> "PortPrototypeBlueprint":
        """
        Provided communication attributes per interface element (data element or operation).
        A None value is a no-op and does not overwrite the existing providedComSpecs list.
        """
        if value is not None:
            self.providedComSpecs = value
        return self

    def addProvidedComSpec(self, value: Optional[PPortComSpec]) -> "PortPrototypeBlueprint":
        """
        Provided communication attributes per interface element (data element or operation).
        A None value is a no-op and does not extend the providedComSpec list.
        """
        if value is not None:
            self.providedComSpecs.append(value)
        return self

    def getRequiredComSpecs(self) -> List[RPortComSpec]:
        """
        Required communication attributes, one for each interface element.
        """
        return self.requiredComSpecs

    def setRequiredComSpecs(self, value: Optional[List[RPortComSpec]]) -> "PortPrototypeBlueprint":
        """
        Required communication attributes, one for each interface element.
        A None value is a no-op and does not overwrite the existing requiredComSpecs list.
        """
        if value is not None:
            self.requiredComSpecs = value
        return self

    def addRequiredComSpec(self, value: Optional[RPortComSpec]) -> "PortPrototypeBlueprint":
        """
        Required communication attributes, one for each interface element.
        A None value is a no-op and does not extend the requiredComSpec list.
        """
        if value is not None:
            self.requiredComSpecs.append(value)
        return self


class PortPrototypeBlueprintMapping(AtpBlueprintMapping):
    """
    This meta-class represents the ability to map a PortPrototypeBlueprint to a PortProtoype of which one acts as the blueprint for the other.
    """

    # PortPrototypeBlueprintMapping method parity checklist:
    # Spec: AUTOSAR_00052.xsd, complexType PORT-PROTOTYPE-BLUEPRINT-MAPPING l.93034, group l.92997 (XSD-only; no own table in repo corpus; atp.Status="removed")
    # XSD verified: AUTOSAR_00052.xsd
    # Columns: impl / docstring / test / reader / writer / release   ([—] = no XML element)
    # [x] __init__                        [x] impl  [x] docstring  [x] test  [—] reader  [—] writer  R23-11
    # [x] getPortPrototypeBlueprintRef    [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setPortPrototypeBlueprintRef    [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getDerivedPortPrototypeRef      [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setDerivedPortPrototypeRef      [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11

    def __init__(self):
        super().__init__()

        # The PortPrototypeBlueprint in the context of the mapping.
        self.portPrototypeBlueprintRef: Optional[RefType] = None

        # The PortPrototype in the context of the mapping.
        self.derivedPortPrototypeRef: Optional[RefType] = None

    def getPortPrototypeBlueprintRef(self) -> Optional[RefType]:
        """
        The PortPrototypeBlueprint in the context of the mapping.
        """
        return self.portPrototypeBlueprintRef

    def setPortPrototypeBlueprintRef(self, value: Optional[RefType]) -> "PortPrototypeBlueprintMapping":
        """
        The PortPrototypeBlueprint in the context of the mapping. A None value is a no-op and is not set.
        """
        if value is not None:
            self.portPrototypeBlueprintRef = value
        return self

    def getDerivedPortPrototypeRef(self) -> Optional[RefType]:
        """
        The PortPrototype in the context of the mapping.
        """
        return self.derivedPortPrototypeRef

    def setDerivedPortPrototypeRef(self, value: Optional[RefType]) -> "PortPrototypeBlueprintMapping":
        """
        The PortPrototype in the context of the mapping. A None value is a no-op and is not set.
        """
        if value is not None:
            self.derivedPortPrototypeRef = value
        return self
