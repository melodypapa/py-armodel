from __future__ import annotations
from typing import List, Optional
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.VariationPointCapable import VariationPointCapable

from armodel.models.M2.AUTOSARTemplates.CommonStructure.ServiceNeeds import NvBlockNeeds, RoleBasedDataAssignment
from armodel.models.M2.AUTOSARTemplates.GenericStructure.AbstractStructure import AtpStructureElement
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import Boolean, Identifier, PositiveInteger, RefType
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.Datatype.DataPrototypes import ParameterDataPrototype, VariableDataPrototype
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.SwcInternalBehavior.DataElements import AutosarVariableRef
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.SwcInternalBehavior.InstantiationDataDefProps import InstantiationDataDefProps
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.SwcInternalBehavior.ServiceMapping import RoleBasedPortAssignment


class NvBlockDataMapping(ARObject, VariationPointCapable):
    """
    Defines the mapping between the VariableDataPrototypes in the NvBlockComponents ports and the VariableDataPrototypes of the RAM Block. The data types of the referenced VariableDataPrototypes in the ports and the referenced sub-element (inside a CompositeDataType) of the VariableDataPrototype representing the RAM Block shall be compatible.
    """

    # NvBlockDataMapping method parity checklist:
    # Spec: AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf, Table 11.11, p.689
    # Columns: impl / docstring / test / reader / writer / release   ([—] = no XML element)
    # [x] __init__                     [x] impl  [x] docstring  [x] test  [—] reader  [—] writer  R23-11
    # [x] getBitfieldTextTableMaskNvBlockDescriptor [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setBitfieldTextTableMaskNvBlockDescriptor [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getBitfieldTextTableMaskPortPrototype [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setBitfieldTextTableMaskPortPrototype [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getNvRamBlockElement        [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setNvRamBlockElement        [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getReadNvData               [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setReadNvData               [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getWrittenNvData            [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setWrittenNvData            [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getWrittenReadNvData        [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setWrittenReadNvData        [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11

    def __init__(self):
        super().__init__()

        # This attribute identifies the applicable bit mask on the side of the Nv Block.
        self.bitfieldTextTableMaskNvBlockDescriptor: Optional[PositiveInteger] = None

        # This attribute identifies the applicable bit mask on the side of the PortPrototype.
        self.bitfieldTextTableMaskPortPrototype: Optional[PositiveInteger] = None

        # Reference to a VariableDataPrototype of a RAM Block.
        self.nvRamBlockElement: Optional[AutosarVariableRef] = None

        # Reference to a VariableDataPrototype of a pPort of the NvBlockComponent providing read access to the RAM Block.If there is no PortPrototype providing read access (write-only) the reference can be omitted.
        self.readNvData: Optional[AutosarVariableRef] = None

        # Reference to a VariableDataPrototype of a rPort of the NvBlockComponent providing write access to the RAM Block. If there is no port providing write access (read-only) the reference can be omitted.
        self.writtenNvData: Optional[AutosarVariableRef] = None

        # Reference to a VariableDataPrototype of a PRPortPrototype of the NvBlockSwComponentType providing write and read access to the RAM Block.
        self.writtenReadNvData: Optional[AutosarVariableRef] = None

    def getBitfieldTextTableMaskNvBlockDescriptor(self) -> Optional[PositiveInteger]:
        """
        This attribute identifies the applicable bit mask on the side of the Nv Block.
        """
        return self.bitfieldTextTableMaskNvBlockDescriptor

    def setBitfieldTextTableMaskNvBlockDescriptor(self, value: Optional[PositiveInteger]) -> "NvBlockDataMapping":
        """
        This attribute identifies the applicable bit mask on the side of the Nv Block. A None value is a no-op and does not overwrite an existing bitfieldTextTableMaskNvBlockDescriptor.
        """
        if value is not None:
            self.bitfieldTextTableMaskNvBlockDescriptor = value
        return self

    def getBitfieldTextTableMaskPortPrototype(self) -> Optional[PositiveInteger]:
        """
        This attribute identifies the applicable bit mask on the side of the PortPrototype.
        """
        return self.bitfieldTextTableMaskPortPrototype

    def setBitfieldTextTableMaskPortPrototype(self, value: Optional[PositiveInteger]) -> "NvBlockDataMapping":
        """
        This attribute identifies the applicable bit mask on the side of the PortPrototype. A None value is a no-op and does not overwrite an existing bitfieldTextTableMaskPortPrototype.
        """
        if value is not None:
            self.bitfieldTextTableMaskPortPrototype = value
        return self

    def getNvRamBlockElement(self) -> Optional[AutosarVariableRef]:
        """
        Reference to a VariableDataPrototype of a RAM Block.
        """
        return self.nvRamBlockElement

    def setNvRamBlockElement(self, value: Optional[AutosarVariableRef]) -> "NvBlockDataMapping":
        """
        Reference to a VariableDataPrototype of a RAM Block. A None value is a no-op and does not overwrite an existing nvRamBlockElement.
        """
        if value is not None:
            self.nvRamBlockElement = value
        return self

    def getReadNvData(self) -> Optional[AutosarVariableRef]:
        """
        Reference to a VariableDataPrototype of a pPort of the NvBlockComponent providing read access to the RAM Block.If there is no PortPrototype providing read access (write-only) the reference can be omitted.
        """
        return self.readNvData

    def setReadNvData(self, value: Optional[AutosarVariableRef]) -> "NvBlockDataMapping":
        """
        Reference to a VariableDataPrototype of a pPort of the NvBlockComponent providing read access to the RAM Block.If there is no PortPrototype providing read access (write-only) the reference can be omitted. A None value is a no-op and does not overwrite an existing readNvData.
        """
        if value is not None:
            self.readNvData = value
        return self

    def getWrittenNvData(self) -> Optional[AutosarVariableRef]:
        """
        Reference to a VariableDataPrototype of a rPort of the NvBlockComponent providing write access to the RAM Block. If there is no port providing write access (read-only) the reference can be omitted.
        """
        return self.writtenNvData

    def setWrittenNvData(self, value: Optional[AutosarVariableRef]) -> "NvBlockDataMapping":
        """
        Reference to a VariableDataPrototype of a rPort of the NvBlockComponent providing write access to the RAM Block. If there is no port providing write access (read-only) the reference can be omitted. A None value is a no-op and does not overwrite an existing writtenNvData.
        """
        if value is not None:
            self.writtenNvData = value
        return self

    def getWrittenReadNvData(self) -> Optional[AutosarVariableRef]:
        """
        Reference to a VariableDataPrototype of a PRPortPrototype of the NvBlockSwComponentType providing write and read access to the RAM Block.
        """
        return self.writtenReadNvData

    def setWrittenReadNvData(self, value: Optional[AutosarVariableRef]) -> "NvBlockDataMapping":
        """
        Reference to a VariableDataPrototype of a PRPortPrototype of the NvBlockSwComponentType providing write and read access to the RAM Block. A None value is a no-op and does not overwrite an existing writtenReadNvData.
        """
        if value is not None:
            self.writtenReadNvData = value
        return self


class BulkNvDataDescriptor(AtpStructureElement, VariationPointCapable):
    """
    This meta-class represents one bulk NV Data Block that is read-only for the application software. The purpose of a bulk NV Data Block is to provide access to information uploaded to the vehicle at e.g. the end of the production line.
    """

    # BulkNvDataDescriptor method parity checklist:
    # Spec: AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf, Table 11.12, p.692
    # Columns: impl / docstring / test / reader / writer / release   ([—] = no XML element)
    # [x] __init__                     [x] impl  [x] docstring  [x] test  [—] reader  [—] writer  R23-11
    # [x] createBulkNvBlock            [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getBulkNvBlock               [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] addNvBlockDataMapping        [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getNvBlockDataMappings       [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11

    def __init__(self, parent: ARObject, short_name: str):
        super().__init__(parent, short_name)

        # This aggregation represents the actual bulk NVBlock.
        self.bulkNvBlock: Optional[VariableDataPrototype] = None

        # Defines the mapping between the VariableDataPrototypes in the NvBlockComponents ports and the VariableDataPrototypes of the non-volatile memory. The aggregation of NvBlockDataMapping is subject to variability with the purpose to support the conditional existence of nv data ports.
        self.nvBlockDataMappings: List[NvBlockDataMapping] = []

    def createBulkNvBlock(self, short_name: str) -> VariableDataPrototype:
        """
        This aggregation represents the actual bulk NVBlock.
        """
        if not self.IsElementExists(short_name, VariableDataPrototype):
            block = VariableDataPrototype(self, short_name)
            self.addElement(block)
            self.bulkNvBlock = block
        return self.getElement(short_name, VariableDataPrototype)

    def getBulkNvBlock(self) -> Optional[VariableDataPrototype]:
        """
        This aggregation represents the actual bulk NVBlock.
        """
        return self.bulkNvBlock

    def addNvBlockDataMapping(self, value: Optional[NvBlockDataMapping]) -> "BulkNvDataDescriptor":
        """
        Defines the mapping between the VariableDataPrototypes in the NvBlockComponents ports and the VariableDataPrototypes of the non-volatile memory. The aggregation of NvBlockDataMapping is subject to variability with the purpose to support the conditional existence of nv data ports. A None value is a no-op and does not append anything.
        """
        if value is not None and value not in self.nvBlockDataMappings:
            self.nvBlockDataMappings.append(value)
        return self

    def getNvBlockDataMappings(self) -> List[NvBlockDataMapping]:
        """
        Defines the mapping between the VariableDataPrototypes in the NvBlockComponents ports and the VariableDataPrototypes of the non-volatile memory. The aggregation of NvBlockDataMapping is subject to variability with the purpose to support the conditional existence of nv data ports.
        """
        return self.nvBlockDataMappings


class NvBlockDescriptor(AtpStructureElement, VariationPointCapable):
    """Specifies the properties of exactly on NVRAM Block.

    [constr_1981] Existence of attribute NvBlockDescriptor.nvBlockNeeds: For each NvBlockDescriptor, attribute nvBlockNeeds shall exist at the time when the RTE is generated.
    """

    # NvBlockDescriptor method parity checklist:
    # Spec: AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf, Table 11.6, p.670
    # Columns: impl / docstring / test / reader / writer / release   ([—] = no XML element)
    # [x] __init__                                   [x] impl  [x] docstring  [x] test  [—] reader  [—] writer  R23-11
    # [x] getClientServerPorts                       [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] addClientServerPort                        [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getConstantValueMappingRefs                [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] addConstantValueMappingRef                 [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getDataTypeMappingRefs                     [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] addDataTypeMappingRef                      [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getInstantiationDataDefPropss              [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] addInstantiationDataDefProps               [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getModeSwitchEventTriggeredActivitys       [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] addModeSwitchEventTriggeredActivity        [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getNvBlockDataMappings                     [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] addNvBlockDataMapping                      [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getNvBlockNeeds                            [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] createNvBlockNeeds                         [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getRamBlock                                [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] createRamBlock                             [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getRomBlock                                [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] createRomBlock                             [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getSupportDirtyFlag                        [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setSupportDirtyFlag                        [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getTimingEventRef                          [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setTimingEventRef                          [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getWritingStrategies                       [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] addWritingStrategy                         [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11

    def __init__(self, parent: ARObject, short_name: str):
        super().__init__(parent, short_name)

        # The RoleBasedPortAssignement defines which client server port of the NvBlockSwComponentType serves for which kind of service or notification. In case of notifications one common callback function is provided by the RTE for each individual kind of notification defined by the "role". The aggregation of RoleBasedPortAssignment is subject to variability with the purpose to support the conditional existence of ports.
        self.clientServerPorts: List[RoleBasedPortAssignment] = []

        # Reference to the ConstantSpecificationMapping to be applied for the particular NVRAM Block
        self.constantValueMappingRefs: List[RefType] = []

        # Reference to the DataTypeMapping to be applied for the particular NVRAM Block.
        self.dataTypeMappingRefs: List[RefType] = []

        # The purpose of InstantiationDataDefProps are the refinement of some data def properties of individual instantiations within the context of a NvBlockSwComponentType. The aggregation of InstantiationDataDefProps is subject to variability with the purpose to support the conditional existence of ports, component internal memory objects and those attributes.
        self.instantiationDataDefPropss: List[InstantiationDataDefProps] = []

        # This represents the collection of ModeSwitchEventTriggeredActivities related to the enclosing NvBlockDescriptor.
        self.modeSwitchEventTriggeredActivitys: List[ModeSwitchEventTriggeredActivity] = []

        # Defines the mapping between the VariableDataPrototypes in the NvBlockComponents ports and the VariableDataPrototypes of the RAM Block. The aggregation of NvBlockDataMapping is subject to variability with the purpose to support the conditional existence of nv data ports.
        self.nvBlockDataMappings: List[NvBlockDataMapping] = []

        # Specifies the abstract needs on the configuration of the NVRAM Manager for the single NVRAM Block described by this NvBlockDescriptor. In addition, it may define requirements for writing strategies in an implementation of an NvBlockSwComponentType by the RTE. Please note that the attributes nDataSets and nRomBlocks are not relevant for this aggregation because the RTE will allocate just one block anyway. In a different context, however, they do make sense.
        self.nvBlockNeeds: Optional[NvBlockNeeds] = None

        # Defines the RAM Block of the NVRAM Block provided by NvBlockSwComponentType.
        self.ramBlock: Optional[VariableDataPrototype] = None

        # Defines the ROM Block of the NVRAM Block provided by NvBlockSwComponentType.
        self.romBlock: Optional[ParameterDataPrototype] = None

        # Specifies whether calling of NvM functions for writing and/or status control of potentially modified RAM Blocks to NV memory shall be controlled by the RTE.
        self.supportDirtyFlag: Optional[Boolean] = None

        # this reference can be taken to identify the TimingEvent to be used by the RTE for implementing a cyclic writing strategy for this block
        self.timingEventRef: Optional[RefType] = None

        # This attribute allows for assigning a specific writing strategy for an incoming AutosarDataPrototype.
        self.writingStrategies: List[RoleBasedDataAssignment] = []

    def getClientServerPorts(self) -> List[RoleBasedPortAssignment]:
        """The RoleBasedPortAssignement defines which client server port of the NvBlockSwComponentType serves for which kind of service or notification. In case of notifications one common callback function is provided by the RTE for each individual kind of notification defined by the "role". The aggregation of RoleBasedPortAssignment is subject to variability with the purpose to support the conditional existence of ports."""
        return self.clientServerPorts

    def addClientServerPort(self, value: Optional[RoleBasedPortAssignment]) -> "NvBlockDescriptor":
        """The RoleBasedPortAssignement defines which client server port of the NvBlockSwComponentType serves for which kind of service or notification. In case of notifications one common callback function is provided by the RTE for each individual kind of notification defined by the "role". The aggregation of RoleBasedPortAssignment is subject to variability with the purpose to support the conditional existence of ports. A None value is a no-op and does not append anything."""
        if value is not None and value not in self.clientServerPorts:
            self.clientServerPorts.append(value)
        return self

    def getConstantValueMappingRefs(self) -> List[RefType]:
        """Reference to the ConstantSpecificationMapping to be applied for the particular NVRAM Block"""
        return self.constantValueMappingRefs

    def addConstantValueMappingRef(self, value: Optional[RefType]) -> "NvBlockDescriptor":
        """Reference to the ConstantSpecificationMapping to be applied for the particular NVRAM Block A None value is a no-op and does not append anything."""
        if value is not None and value not in self.constantValueMappingRefs:
            self.constantValueMappingRefs.append(value)
        return self

    def getDataTypeMappingRefs(self) -> List[RefType]:
        """Reference to the DataTypeMapping to be applied for the particular NVRAM Block."""
        return self.dataTypeMappingRefs

    def addDataTypeMappingRef(self, value: Optional[RefType]) -> "NvBlockDescriptor":
        """Reference to the DataTypeMapping to be applied for the particular NVRAM Block. A None value is a no-op and does not append anything."""
        if value is not None and value not in self.dataTypeMappingRefs:
            self.dataTypeMappingRefs.append(value)
        return self

    def getInstantiationDataDefPropss(self) -> List[InstantiationDataDefProps]:
        """The purpose of InstantiationDataDefProps are the refinement of some data def properties of individual instantiations within the context of a NvBlockSwComponentType. The aggregation of InstantiationDataDefProps is subject to variability with the purpose to support the conditional existence of ports, component internal memory objects and those attributes."""
        return self.instantiationDataDefPropss

    def addInstantiationDataDefProps(self, value: Optional[InstantiationDataDefProps]) -> "NvBlockDescriptor":
        """The purpose of InstantiationDataDefProps are the refinement of some data def properties of individual instantiations within the context of a NvBlockSwComponentType. The aggregation of InstantiationDataDefProps is subject to variability with the purpose to support the conditional existence of ports, component internal memory objects and those attributes. A None value is a no-op and does not append anything."""
        if value is not None and value not in self.instantiationDataDefPropss:
            self.instantiationDataDefPropss.append(value)
        return self

    def getModeSwitchEventTriggeredActivitys(self) -> List[ModeSwitchEventTriggeredActivity]:
        """This represents the collection of ModeSwitchEventTriggeredActivities related to the enclosing NvBlockDescriptor."""
        return self.modeSwitchEventTriggeredActivitys

    def addModeSwitchEventTriggeredActivity(self, value: Optional[ModeSwitchEventTriggeredActivity]) -> "NvBlockDescriptor":
        """This represents the collection of ModeSwitchEventTriggeredActivities related to the enclosing NvBlockDescriptor. A None value is a no-op and does not append anything."""
        if value is not None and value not in self.modeSwitchEventTriggeredActivitys:
            self.modeSwitchEventTriggeredActivitys.append(value)
        return self

    def getNvBlockDataMappings(self) -> List[NvBlockDataMapping]:
        """Defines the mapping between the VariableDataPrototypes in the NvBlockComponents ports and the VariableDataPrototypes of the RAM Block. The aggregation of NvBlockDataMapping is subject to variability with the purpose to support the conditional existence of nv data ports."""
        return self.nvBlockDataMappings

    def addNvBlockDataMapping(self, value: Optional[NvBlockDataMapping]) -> "NvBlockDescriptor":
        """Defines the mapping between the VariableDataPrototypes in the NvBlockComponents ports and the VariableDataPrototypes of the RAM Block. The aggregation of NvBlockDataMapping is subject to variability with the purpose to support the conditional existence of nv data ports. A None value is a no-op and does not append anything."""
        if value is not None and value not in self.nvBlockDataMappings:
            self.nvBlockDataMappings.append(value)
        return self

    def getNvBlockNeeds(self) -> Optional[NvBlockNeeds]:
        """Specifies the abstract needs on the configuration of the NVRAM Manager for the single NVRAM Block described by this NvBlockDescriptor. In addition, it may define requirements for writing strategies in an implementation of an NvBlockSwComponentType by the RTE. Please note that the attributes nDataSets and nRomBlocks are not relevant for this aggregation because the RTE will allocate just one block anyway. In a different context, however, they do make sense."""
        return self.nvBlockNeeds

    def createNvBlockNeeds(self, short_name: str) -> NvBlockNeeds:
        """Specifies the abstract needs on the configuration of the NVRAM Manager for the single NVRAM Block described by this NvBlockDescriptor. In addition, it may define requirements for writing strategies in an implementation of an NvBlockSwComponentType by the RTE. Please note that the attributes nDataSets and nRomBlocks are not relevant for this aggregation because the RTE will allocate just one block anyway. In a different context, however, they do make sense."""
        if not self.IsElementExists(short_name, NvBlockNeeds):
            element = NvBlockNeeds(self, short_name)
            self.addElement(element)
            self.nvBlockNeeds = element
        return self.getElement(short_name, NvBlockNeeds)

    def getRamBlock(self) -> Optional[VariableDataPrototype]:
        """Defines the RAM Block of the NVRAM Block provided by NvBlockSwComponentType."""
        return self.ramBlock

    def createRamBlock(self, short_name: str) -> VariableDataPrototype:
        """Defines the RAM Block of the NVRAM Block provided by NvBlockSwComponentType."""
        if not self.IsElementExists(short_name, VariableDataPrototype):
            element = VariableDataPrototype(self, short_name)
            self.addElement(element)
            self.ramBlock = element
        return self.getElement(short_name, VariableDataPrototype)

    def getRomBlock(self) -> Optional[ParameterDataPrototype]:
        """Defines the ROM Block of the NVRAM Block provided by NvBlockSwComponentType."""
        return self.romBlock

    def createRomBlock(self, short_name: str) -> ParameterDataPrototype:
        """Defines the ROM Block of the NVRAM Block provided by NvBlockSwComponentType."""
        if not self.IsElementExists(short_name, ParameterDataPrototype):
            element = ParameterDataPrototype(self, short_name)
            self.addElement(element)
            self.romBlock = element
        return self.getElement(short_name, ParameterDataPrototype)

    def getSupportDirtyFlag(self) -> Optional[Boolean]:
        """Specifies whether calling of NvM functions for writing and/or status control of potentially modified RAM Blocks to NV memory shall be controlled by the RTE."""
        return self.supportDirtyFlag

    def setSupportDirtyFlag(self, value: Optional[Boolean]) -> "NvBlockDescriptor":
        """Specifies whether calling of NvM functions for writing and/or status control of potentially modified RAM Blocks to NV memory shall be controlled by the RTE. A None value is a no-op and does not overwrite an existing supportDirtyFlag."""
        if value is not None:
            self.supportDirtyFlag = value
        return self

    def getTimingEventRef(self) -> Optional[RefType]:
        """this reference can be taken to identify the TimingEvent to be used by the RTE for implementing a cyclic writing strategy for this block"""
        return self.timingEventRef

    def setTimingEventRef(self, value: Optional[RefType]) -> "NvBlockDescriptor":
        """this reference can be taken to identify the TimingEvent to be used by the RTE for implementing a cyclic writing strategy for this block A None value is a no-op and does not overwrite an existing timingEventRef."""
        if value is not None:
            self.timingEventRef = value
        return self

    def getWritingStrategies(self) -> List[RoleBasedDataAssignment]:
        """This attribute allows for assigning a specific writing strategy for an incoming AutosarDataPrototype."""
        return self.writingStrategies

    def addWritingStrategy(self, value: Optional[RoleBasedDataAssignment]) -> "NvBlockDescriptor":
        """This attribute allows for assigning a specific writing strategy for an incoming AutosarDataPrototype. A None value is a no-op and does not append anything."""
        if value is not None and value not in self.writingStrategies:
            self.writingStrategies.append(value)
        return self


class ModeSwitchEventTriggeredActivity(ARObject, VariationPointCapable):
    """
    This meta-class defines an activity of the NvBlockSwComponentType for a specific NvBlock which is triggered by a ModeSwitchEvent.
    """

    # ModeSwitchEventTriggeredActivity method parity checklist:
    # Spec: AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf, Table 11.7, p.675
    # Columns: impl / docstring / test / reader / writer / release   ([—] = no XML element)
    # [x] __init__                     [x] impl  [x] docstring  [x] test  [—] reader  [—] writer  R23-11
    # [x] getRole                      [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setRole                      [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getSwcModeSwitchEventRef     [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setSwcModeSwitchEventRef     [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11

    def __init__(self):
        super().__init__()

        # This attribute indicates which service of the NvM for the NvBlock shall be requested.
        self.role: Optional[Identifier] = None

        # This reference identifies the SwcModeSwitchEvent that triggers the activity.
        self.swcModeSwitchEventRef: Optional[RefType] = None

    def getRole(self) -> Optional[Identifier]:
        """
        This attribute indicates which service of the NvM for the NvBlock shall be requested.
        """
        return self.role

    def setRole(self, value: Optional[Identifier]) -> "ModeSwitchEventTriggeredActivity":
        """
        This attribute indicates which service of the NvM for the NvBlock shall be requested. A None value is a no-op and does not overwrite an existing role.
        """
        if value is not None:
            self.role = value
        return self

    def getSwcModeSwitchEventRef(self) -> Optional[RefType]:
        """
        This reference identifies the SwcModeSwitchEvent that triggers the activity.
        """
        return self.swcModeSwitchEventRef

    def setSwcModeSwitchEventRef(self, value: Optional[RefType]) -> "ModeSwitchEventTriggeredActivity":
        """
        This reference identifies the SwcModeSwitchEvent that triggers the activity. A None value is a no-op and does not overwrite an existing swcModeSwitchEventRef.
        """
        if value is not None:
            self.swcModeSwitchEventRef = value
        return self
