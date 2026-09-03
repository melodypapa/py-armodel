from typing import List, Optional
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.VariationPointCapable import VariationPointCapable

from armodel.models.M2.AUTOSARTemplates.CommonStructure.ServiceNeeds import NvBlockNeeds, RoleBasedDataAssignment
from armodel.models.M2.AUTOSARTemplates.GenericStructure.AbstractStructure import AtpStructureElement
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import PositiveInteger, RefType
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
    # Columns: impl / docstring / test / reader / writer   ([—] = no XML element)
    # [x] __init__                     [x] impl  [x] docstring  [x] test  [—] reader  [—] writer
    # [x] getBitfieldTextTableMaskNvBlockDescriptor [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] setBitfieldTextTableMaskNvBlockDescriptor [x] impl  [x] docstring  [x] test  [x] reader  [—] writer
    # [x] getBitfieldTextTableMaskPortPrototype [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] setBitfieldTextTableMaskPortPrototype [x] impl  [x] docstring  [x] test  [x] reader  [—] writer
    # [x] getNvRamBlockElement        [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] setNvRamBlockElement        [x] impl  [x] docstring  [x] test  [x] reader  [—] writer
    # [x] getReadNvData               [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] setReadNvData               [x] impl  [x] docstring  [x] test  [x] reader  [—] writer
    # [x] getWrittenNvData            [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] setWrittenNvData            [x] impl  [x] docstring  [x] test  [x] reader  [—] writer
    # [x] getWrittenReadNvData        [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] setWrittenReadNvData        [x] impl  [x] docstring  [x] test  [x] reader  [—] writer

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

        # Reference to a VariableDataPrototype of a rPort of the Nv BlockComponent providing write access to the RAM Block. If there is no port providing write access (read-only) the reference can be omitted.
        self.writtenNvData: Optional[AutosarVariableRef] = None

        # Reference to a VariableDataPrototype of a PRPort Prototype of the NvBlockSwComponentType providing write and read access to the RAM Block.
        self.writtenReadNvData: Optional[AutosarVariableRef] = None

    def getBitfieldTextTableMaskNvBlockDescriptor(self) -> Optional[PositiveInteger]:
        """
        Gets the bit field text table mask of the NvBlockDescriptor.

        This attribute identifies the applicable bit mask on the side of the Nv Block.

        Returns:
            PositiveInteger, or None if not set
        """
        return self.bitfieldTextTableMaskNvBlockDescriptor

    def setBitfieldTextTableMaskNvBlockDescriptor(self, value: Optional[PositiveInteger]) -> "NvBlockDataMapping":
        """
        Sets the bit field text table mask of the NvBlockDescriptor.
        A None value is a no-op and does not overwrite an existing bit mask.

        This attribute identifies the applicable bit mask on the side of the Nv Block.

        Args:
            value: The bit mask to set

        Returns:
            self for method chaining
        """
        if value is not None:
            self.bitfieldTextTableMaskNvBlockDescriptor = value
        return self

    def getBitfieldTextTableMaskPortPrototype(self) -> Optional[PositiveInteger]:
        """
        Gets the bit field text table mask of the PortPrototype.

        This attribute identifies the applicable bit mask on the side of the PortPrototype.

        Returns:
            PositiveInteger, or None if not set
        """
        return self.bitfieldTextTableMaskPortPrototype

    def setBitfieldTextTableMaskPortPrototype(self, value: Optional[PositiveInteger]) -> "NvBlockDataMapping":
        """
        Sets the bit field text table mask of the PortPrototype.
        A None value is a no-op and does not overwrite an existing bit mask.

        This attribute identifies the applicable bit mask on the side of the PortPrototype.

        Args:
            value: The bit mask to set

        Returns:
            self for method chaining
        """
        if value is not None:
            self.bitfieldTextTableMaskPortPrototype = value
        return self

    def getNvRamBlockElement(self) -> Optional[AutosarVariableRef]:
        """
        Gets the NV RAM block element.

        Reference to a VariableDataPrototype of a RAM Block.

        Returns:
            AutosarVariableRef, or None if not set
        """
        return self.nvRamBlockElement

    def setNvRamBlockElement(self, value: Optional[AutosarVariableRef]) -> "NvBlockDataMapping":
        """
        Sets the NV RAM block element.
        A None value is a no-op and does not overwrite an existing reference.

        Reference to a VariableDataPrototype of a RAM Block.

        Args:
            value: The AutosarVariableRef to set

        Returns:
            self for method chaining
        """
        if value is not None:
            self.nvRamBlockElement = value
        return self

    def getReadNvData(self) -> Optional[AutosarVariableRef]:
        """
        Gets the read NV data.

        Reference to a VariableDataPrototype of a pPort of the NvBlockComponent providing read access to the RAM Block.If there is no PortPrototype providing read access (write-only) the reference can be omitted.

        Returns:
            AutosarVariableRef, or None if not set
        """
        return self.readNvData

    def setReadNvData(self, value: Optional[AutosarVariableRef]) -> "NvBlockDataMapping":
        """
        Sets the read NV data.
        A None value is a no-op and does not overwrite an existing reference.

        Reference to a VariableDataPrototype of a pPort of the NvBlockComponent providing read access to the RAM Block.If there is no PortPrototype providing read access (write-only) the reference can be omitted.

        Args:
            value: The AutosarVariableRef to set

        Returns:
            self for method chaining
        """
        if value is not None:
            self.readNvData = value
        return self

    def getWrittenNvData(self) -> Optional[AutosarVariableRef]:
        """
        Gets the written NV data.

        Reference to a VariableDataPrototype of a rPort of the Nv BlockComponent providing write access to the RAM Block. If there is no port providing write access (read-only) the reference can be omitted.

        Returns:
            AutosarVariableRef, or None if not set
        """
        return self.writtenNvData

    def setWrittenNvData(self, value: Optional[AutosarVariableRef]) -> "NvBlockDataMapping":
        """
        Sets the written NV data.
        A None value is a no-op and does not overwrite an existing reference.

        Reference to a VariableDataPrototype of a rPort of the Nv BlockComponent providing write access to the RAM Block. If there is no port providing write access (read-only) the reference can be omitted.

        Args:
            value: The AutosarVariableRef to set

        Returns:
            self for method chaining
        """
        if value is not None:
            self.writtenNvData = value
        return self

    def getWrittenReadNvData(self) -> Optional[AutosarVariableRef]:
        """
        Gets the written read NV data.

        Reference to a VariableDataPrototype of a PRPort Prototype of the NvBlockSwComponentType providing write and read access to the RAM Block.

        Returns:
            AutosarVariableRef, or None if not set
        """
        return self.writtenReadNvData

    def setWrittenReadNvData(self, value: Optional[AutosarVariableRef]) -> "NvBlockDataMapping":
        """
        Sets the written read NV data.
        A None value is a no-op and does not overwrite an existing reference.

        Reference to a VariableDataPrototype of a PRPort Prototype of the NvBlockSwComponentType providing write and read access to the RAM Block.

        Args:
            value: The AutosarVariableRef to set

        Returns:
            self for method chaining
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
    # Columns: impl / docstring / test / reader / writer   ([—] = no XML element)
    # [x] __init__                     [x] impl  [x] docstring  [x] test  [—] reader  [—] writer
    # [x] getBulkNvBlock               [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] setBulkNvBlock               [x] impl  [x] docstring  [x] test  [x] reader  [—] writer
    # [x] getNvBlockDataMappings       [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] addNvBlockDataMapping        [x] impl  [x] docstring  [x] test  [x] reader  [—] writer

    def __init__(self, parent: ARObject, short_name: str):
        super().__init__(parent, short_name)

        # This aggregation represents the actual bulk NVBlock.
        self.bulkNvBlock: Optional[VariableDataPrototype] = None

        # Defines the mapping between the VariableData Prototypes in the NvBlockComponents ports and the VariableDataPrototypes of the non-volatile memory. The aggregation of NvBlockDataMapping is subject to variability with the purpose to support the conditional existence of nv data ports. Stereotypes: atpSplitable; atpVariation Tags: atp.Splitkey=nvBlockDataMapping, nvBlockData Mapping.variationPoint.shortLabel vh.latestBindingTime=preCompileTime
        self.nvBlockDataMappings: List[NvBlockDataMapping] = []

    def getBulkNvBlock(self) -> Optional[VariableDataPrototype]:
        """
        Gets the actual bulk NVBlock.

        This aggregation represents the actual bulk NVBlock.

        Returns:
            VariableDataPrototype, or None if not set
        """
        return self.bulkNvBlock

    def setBulkNvBlock(self, value: Optional[VariableDataPrototype]) -> "BulkNvDataDescriptor":
        """
        Sets the actual bulk NVBlock.
        A None value is a no-op and does not overwrite an existing block.

        This aggregation represents the actual bulk NVBlock.

        Args:
            value: The VariableDataPrototype to set

        Returns:
            self for method chaining
        """
        if value is not None:
            self.bulkNvBlock = value
        return self

    def getNvBlockDataMappings(self) -> List[NvBlockDataMapping]:
        """
        Gets the mappings between the VariableDataPrototypes in the NvBlockComponents ports and the VariableDataPrototypes of the non-volatile memory.

        Defines the mapping between the VariableData Prototypes in the NvBlockComponents ports and the VariableDataPrototypes of the non-volatile memory. The aggregation of NvBlockDataMapping is subject to variability with the purpose to support the conditional existence of nv data ports. Stereotypes: atpSplitable; atpVariation Tags: atp.Splitkey=nvBlockDataMapping, nvBlockData Mapping.variationPoint.shortLabel vh.latestBindingTime=preCompileTime

        Returns:
            List of NvBlockDataMapping instances
        """
        return self.nvBlockDataMappings

    def addNvBlockDataMapping(self, value: NvBlockDataMapping) -> "BulkNvDataDescriptor":
        """
        Adds a mapping between the VariableDataPrototypes in the NvBlockComponents ports and the VariableDataPrototypes of the non-volatile memory.
        A None value is a no-op and does not append anything.

        Defines the mapping between the VariableData Prototypes in the NvBlockComponents ports and the VariableDataPrototypes of the non-volatile memory. The aggregation of NvBlockDataMapping is subject to variability with the purpose to support the conditional existence of nv data ports. Stereotypes: atpSplitable; atpVariation Tags: atp.Splitkey=nvBlockDataMapping, nvBlockData Mapping.variationPoint.shortLabel vh.latestBindingTime=preCompileTime

        Args:
            value: The NvBlockDataMapping to add

        Returns:
            self for method chaining
        """
        if value is not None and value not in self.nvBlockDataMappings:
            self.nvBlockDataMappings.append(value)
        return self


class NvBlockDescriptor(AtpStructureElement, VariationPointCapable):
    """
    Specifies the properties of exactly on NVRAM Block.
    """

    # NvBlockDescriptor method parity checklist:
    # Spec: AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf, Table 11.6, p.670
    # Columns: impl / docstring / test / reader / writer   ([—] = no XML element)
    # [x] __init__                     [x] impl  [x] docstring  [x] test  [—] reader  [—] writer
    # [x] getClientServerPorts         [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] addClientServerPort          [x] impl  [x] docstring  [x] test  [x] reader  [—] writer
    # [x] getConstantValueMappingRefs  [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] addConstantValueMappingRef   [x] impl  [x] docstring  [x] test  [x] reader  [—] writer
    # [x] getDataTypeMappingRefs       [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] addDataTypeMappingRef        [x] impl  [x] docstring  [x] test  [x] reader  [—] writer
    # [x] getInstantiationDataDefPropss [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] addInstantiationDataDefProps [x] impl  [x] docstring  [x] test  [x] reader  [—] writer
    # [x] getModeSwitchEventTriggeredActivitys [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] addModeSwitchEventTriggeredActivity [x] impl  [x] docstring  [x] test  [x] reader  [—] writer
    # [x] getNvBlockDataMappings       [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] addNvBlockDataMapping        [x] impl  [x] docstring  [x] test  [x] reader  [—] writer
    # [x] getNvBlockNeeds              [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] setNvBlockNeeds              [x] impl  [x] docstring  [x] test  [x] reader  [—] writer
    # [x] getRamBlock                  [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] setRamBlock                  [x] impl  [x] docstring  [x] test  [x] reader  [—] writer
    # [x] getRomBlock                  [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] setRomBlock                  [x] impl  [x] docstring  [x] test  [x] reader  [—] writer
    # [x] getSupportDirtyFlag          [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] setSupportDirtyFlag          [x] impl  [x] docstring  [x] test  [x] reader  [—] writer
    # [x] getTimingEventRef            [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] setTimingEventRef            [x] impl  [x] docstring  [x] test  [x] reader  [—] writer
    # [x] getWritingStrategies         [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] addWritingStrategy           [x] impl  [x] docstring  [x] test  [x] reader  [—] writer

    def __init__(self, parent: ARObject, short_name: str):
        super().__init__(parent, short_name)

        # The RoleBasedPortAssignement defines which client server port of the NvBlockSwComponentType serves for which kind of service or notification. In case of notifications one common callback function is provided by the RTE for each individual kind of notification defined by the "role". The aggregation of RoleBasedPortAssignment is subject to variability with the purpose to support the conditional existence of ports. Stereotypes: atpSplitable; atpVariation Tags: atp.Splitkey=clientServerPort, clientServerPort.variation Point.shortLabel vh.latestBindingTime=preCompileTime
        self.clientServerPorts: List[RoleBasedPortAssignment] = []

        # Reference to the ConstantSpecificationMapping to be applied for the particular NVRAM Block Stereotypes: atpSplitable Tags: atp.Splitkey=constantValueMapping
        self.constantValueMappingRefs: List[RefType] = []

        # Reference to the DataTypeMapping to be applied for the particular NVRAM Block. Stereotypes: atpSplitable Tags: atp.Splitkey=dataTypeMapping
        self.dataTypeMappingRefs: List[RefType] = []

        # The purpose of InstantiationDataDefProps are the refinement of some data def properties of individual instantiations within the context of a NvBlockSw ComponentType. The aggregation of InstantiationDataDefProps is subject to variability with the purpose to support the conditional existence of ports, component internal memory objects and those attributes. Stereotypes: atpSplitable; atpVariation Tags: atp.Splitkey=instantiationDataDefProps, instantiationData DefProps.variationPoint.shortLabel vh.latestBindingTime=preCompileTime
        self.instantiationDataDefPropss: List[InstantiationDataDefProps] = []

        # This represents the collection of ModeSwitchEvent TriggeredActivities related to the enclosing NvBlock Descriptor. Stereotypes: atpSplitable; atpVariation Tags: atp.Splitkey=modeSwitchEventTriggeredActivity, mode SwitchEventTriggeredActivity.variationPoint.shortLabel vh.latestBindingTime=preCompileTime
        self.modeSwitchEventTriggeredActivitys: List[ModeSwitchEventTriggeredActivity] = []

        # Defines the mapping between the VariableData Prototypes in the NvBlockComponents ports and the VariableDataPrototypes of the RAM Block. The aggregation of NvBlockDataMapping is subject to variability with the purpose to support the conditional existence of nv data ports. Stereotypes: atpSplitable; atpVariation Tags: atp.Splitkey=nvBlockDataMapping, nvBlockData Mapping.variationPoint.shortLabel vh.latestBindingTime=preCompileTime
        self.nvBlockDataMappings: List[NvBlockDataMapping] = []

        # Specifies the abstract needs on the configuration of the NVRAM Manager for the single NVRAM Block described by this NvBlockDescriptor. In addition, it may define requirements for writing strategies in an implementation of an NvBlockSw ComponentType by the RTE. Please note that the attributes nDataSets and nRom Blocks are not relevant for this aggregation because the RTE will allocate just one block anyway. In a different context, however, they do make sense.
        self.nvBlockNeeds: Optional[NvBlockNeeds] = None

        # Defines the RAM Block of the NVRAM Block provided by NvBlockSwComponentType.
        self.ramBlock: Optional[VariableDataPrototype] = None

        # Defines the ROM Block of the NVRAM Block provided by NvBlockSwComponentType.
        self.romBlock: Optional[ParameterDataPrototype] = None

        # Specifies whether calling of NvM functions for writing and/ or status control of potentially modified RAM Blocks to NV memory shall be controlled by the RTE.
        self.supportDirtyFlag: Optional[bool] = None

        # this reference can be taken to identify the TimingEvent to be used by the RTE for implementing a cyclic writing strategy for this block
        self.timingEventRef: Optional[RefType] = None

        # This attribute allows for assigning a specific writing strategy for an incoming AutosarDataPrototype.
        self.writingStrategies: List[RoleBasedDataAssignment] = []

    def getClientServerPorts(self) -> List[RoleBasedPortAssignment]:
        """
        Gets the role-based port assignments for the client server ports of the NvBlockSwComponentType.

        The RoleBasedPortAssignement defines which client server port of the NvBlockSwComponentType serves for which kind of service or notification. In case of notifications one common callback function is provided by the RTE for each individual kind of notification defined by the "role". The aggregation of RoleBasedPortAssignment is subject to variability with the purpose to support the conditional existence of ports. Stereotypes: atpSplitable; atpVariation Tags: atp.Splitkey=clientServerPort, clientServerPort.variation Point.shortLabel vh.latestBindingTime=preCompileTime

        Returns:
            List of RoleBasedPortAssignment instances
        """
        return self.clientServerPorts

    def addClientServerPort(self, value: RoleBasedPortAssignment) -> "NvBlockDescriptor":
        """
        Adds a role-based port assignment for a client server port of the NvBlockSwComponentType.
        A None value is a no-op and does not append anything.

        The RoleBasedPortAssignement defines which client server port of the NvBlockSwComponentType serves for which kind of service or notification. In case of notifications one common callback function is provided by the RTE for each individual kind of notification defined by the "role". The aggregation of RoleBasedPortAssignment is subject to variability with the purpose to support the conditional existence of ports. Stereotypes: atpSplitable; atpVariation Tags: atp.Splitkey=clientServerPort, clientServerPort.variation Point.shortLabel vh.latestBindingTime=preCompileTime

        Args:
            value: The RoleBasedPortAssignment to add

        Returns:
            self for method chaining
        """
        if value is not None and value not in self.clientServerPorts:
            self.clientServerPorts.append(value)
        return self

    def getConstantValueMappingRefs(self) -> List[RefType]:
        """
        Gets the references to the ConstantSpecificationMapping to be applied for the particular NVRAM Block.

        Reference to the ConstantSpecificationMapping to be applied for the particular NVRAM Block Stereotypes: atpSplitable Tags: atp.Splitkey=constantValueMapping

        Returns:
            List of RefType instances
        """
        return self.constantValueMappingRefs

    def addConstantValueMappingRef(self, value: RefType) -> "NvBlockDescriptor":
        """
        Adds a reference to the ConstantSpecificationMapping to be applied for the particular NVRAM Block.
        A None value is a no-op and does not append anything.

        Reference to the ConstantSpecificationMapping to be applied for the particular NVRAM Block Stereotypes: atpSplitable Tags: atp.Splitkey=constantValueMapping

        Args:
            value: The RefType to add

        Returns:
            self for method chaining
        """
        if value is not None and value not in self.constantValueMappingRefs:
            self.constantValueMappingRefs.append(value)
        return self

    def getDataTypeMappingRefs(self) -> List[RefType]:
        """
        Gets the references to the DataTypeMapping to be applied for the particular NVRAM Block.

        Reference to the DataTypeMapping to be applied for the particular NVRAM Block. Stereotypes: atpSplitable Tags: atp.Splitkey=dataTypeMapping

        Returns:
            List of RefType instances
        """
        return self.dataTypeMappingRefs

    def addDataTypeMappingRef(self, value: RefType) -> "NvBlockDescriptor":
        """
        Adds a reference to the DataTypeMapping to be applied for the particular NVRAM Block.
        A None value is a no-op and does not append anything.

        Reference to the DataTypeMapping to be applied for the particular NVRAM Block. Stereotypes: atpSplitable Tags: atp.Splitkey=dataTypeMapping

        Args:
            value: The RefType to add

        Returns:
            self for method chaining
        """
        if value is not None and value not in self.dataTypeMappingRefs:
            self.dataTypeMappingRefs.append(value)
        return self

    def getInstantiationDataDefPropss(self) -> List[InstantiationDataDefProps]:
        """
        Gets the refinement of some data def properties of individual instantiations within the context of a NvBlockSwComponentType.

        The purpose of InstantiationDataDefProps are the refinement of some data def properties of individual instantiations within the context of a NvBlockSw ComponentType. The aggregation of InstantiationDataDefProps is subject to variability with the purpose to support the conditional existence of ports, component internal memory objects and those attributes. Stereotypes: atpSplitable; atpVariation Tags: atp.Splitkey=instantiationDataDefProps, instantiationData DefProps.variationPoint.shortLabel vh.latestBindingTime=preCompileTime

        Returns:
            List of InstantiationDataDefProps instances
        """
        return self.instantiationDataDefPropss

    def addInstantiationDataDefProps(self, value: InstantiationDataDefProps) -> "NvBlockDescriptor":
        """
        Adds a refinement of some data def properties of an instantiation within the context of a NvBlockSwComponentType.
        A None value is a no-op and does not append anything.

        The purpose of InstantiationDataDefProps are the refinement of some data def properties of individual instantiations within the context of a NvBlockSw ComponentType. The aggregation of InstantiationDataDefProps is subject to variability with the purpose to support the conditional existence of ports, component internal memory objects and those attributes. Stereotypes: atpSplitable; atpVariation Tags: atp.Splitkey=instantiationDataDefProps, instantiationData DefProps.variationPoint.shortLabel vh.latestBindingTime=preCompileTime

        Args:
            value: The InstantiationDataDefProps to add

        Returns:
            self for method chaining
        """
        if value is not None and value not in self.instantiationDataDefPropss:
            self.instantiationDataDefPropss.append(value)
        return self

    def getModeSwitchEventTriggeredActivitys(self) -> "List[ModeSwitchEventTriggeredActivity]":
        """
        Gets the collection of ModeSwitchEventTriggeredActivities related to the enclosing NvBlockDescriptor.

        This represents the collection of ModeSwitchEvent TriggeredActivities related to the enclosing NvBlock Descriptor. Stereotypes: atpSplitable; atpVariation Tags: atp.Splitkey=modeSwitchEventTriggeredActivity, mode SwitchEventTriggeredActivity.variationPoint.shortLabel vh.latestBindingTime=preCompileTime

        Returns:
            List of ModeSwitchEventTriggeredActivity instances
        """
        return self.modeSwitchEventTriggeredActivitys

    def addModeSwitchEventTriggeredActivity(self, value: "ModeSwitchEventTriggeredActivity") -> "NvBlockDescriptor":
        """
        Adds a ModeSwitchEventTriggeredActivity related to the enclosing NvBlockDescriptor.
        A None value is a no-op and does not append anything.

        This represents the collection of ModeSwitchEvent TriggeredActivities related to the enclosing NvBlock Descriptor. Stereotypes: atpSplitable; atpVariation Tags: atp.Splitkey=modeSwitchEventTriggeredActivity, mode SwitchEventTriggeredActivity.variationPoint.shortLabel vh.latestBindingTime=preCompileTime

        Args:
            value: The ModeSwitchEventTriggeredActivity to add

        Returns:
            self for method chaining
        """
        if value is not None and value not in self.modeSwitchEventTriggeredActivitys:
            self.modeSwitchEventTriggeredActivitys.append(value)
        return self

    def getNvBlockDataMappings(self) -> List[NvBlockDataMapping]:
        """
        Gets the mappings between the VariableDataPrototypes in the NvBlockComponents ports and the VariableDataPrototypes of the RAM Block.

        Defines the mapping between the VariableData Prototypes in the NvBlockComponents ports and the VariableDataPrototypes of the RAM Block. The aggregation of NvBlockDataMapping is subject to variability with the purpose to support the conditional existence of nv data ports. Stereotypes: atpSplitable; atpVariation Tags: atp.Splitkey=nvBlockDataMapping, nvBlockData Mapping.variationPoint.shortLabel vh.latestBindingTime=preCompileTime

        Returns:
            List of NvBlockDataMapping instances
        """
        return self.nvBlockDataMappings

    def addNvBlockDataMapping(self, value: NvBlockDataMapping) -> "NvBlockDescriptor":
        """
        Adds a mapping between the VariableDataPrototypes in the NvBlockComponents ports and the VariableDataPrototypes of the RAM Block.
        A None value is a no-op and does not append anything.

        Defines the mapping between the VariableData Prototypes in the NvBlockComponents ports and the VariableDataPrototypes of the RAM Block. The aggregation of NvBlockDataMapping is subject to variability with the purpose to support the conditional existence of nv data ports. Stereotypes: atpSplitable; atpVariation Tags: atp.Splitkey=nvBlockDataMapping, nvBlockData Mapping.variationPoint.shortLabel vh.latestBindingTime=preCompileTime

        Args:
            value: The NvBlockDataMapping to add

        Returns:
            self for method chaining
        """
        if value is not None and value not in self.nvBlockDataMappings:
            self.nvBlockDataMappings.append(value)
        return self

    def getNvBlockNeeds(self):
        """
        Gets the abstract needs on the configuration of the NVRAM Manager for the single NVRAM Block described by this NvBlockDescriptor.

        Specifies the abstract needs on the configuration of the NVRAM Manager for the single NVRAM Block described by this NvBlockDescriptor. In addition, it may define requirements for writing strategies in an implementation of an NvBlockSw ComponentType by the RTE. Please note that the attributes nDataSets and nRom Blocks are not relevant for this aggregation because the RTE will allocate just one block anyway. In a different context, however, they do make sense.

        Returns:
            NvBlockNeeds, or None if not set
        """
        return self.nvBlockNeeds

    def setNvBlockNeeds(self, value) -> "NvBlockDescriptor":
        """
        Sets the abstract needs on the configuration of the NVRAM Manager for the single NVRAM Block described by this NvBlockDescriptor.
        A None value is a no-op and does not overwrite an existing value.

        Specifies the abstract needs on the configuration of the NVRAM Manager for the single NVRAM Block described by this NvBlockDescriptor. In addition, it may define requirements for writing strategies in an implementation of an NvBlockSw ComponentType by the RTE. Please note that the attributes nDataSets and nRom Blocks are not relevant for this aggregation because the RTE will allocate just one block anyway. In a different context, however, they do make sense.

        Args:
            value: The NvBlockNeeds to set

        Returns:
            self for method chaining
        """
        if value is not None:
            self.nvBlockNeeds = value
        return self

    def getRamBlock(self) -> Optional[VariableDataPrototype]:
        """
        Gets the RAM Block of the NVRAM Block provided by NvBlockSwComponentType.

        Defines the RAM Block of the NVRAM Block provided by NvBlockSwComponentType.

        Returns:
            VariableDataPrototype, or None if not set
        """
        return self.ramBlock

    def setRamBlock(self, value: Optional[VariableDataPrototype]) -> "NvBlockDescriptor":
        """
        Sets the RAM Block of the NVRAM Block provided by NvBlockSwComponentType.
        A None value is a no-op and does not overwrite an existing block.

        Defines the RAM Block of the NVRAM Block provided by NvBlockSwComponentType.

        Args:
            value: The VariableDataPrototype to set

        Returns:
            self for method chaining
        """
        if value is not None:
            self.ramBlock = value
        return self

    def getRomBlock(self):
        """
        Gets the ROM Block of the NVRAM Block provided by NvBlockSwComponentType.

        Defines the ROM Block of the NVRAM Block provided by NvBlockSwComponentType.

        Returns:
            ParameterDataPrototype, or None if not set
        """
        return self.romBlock

    def setRomBlock(self, value) -> "NvBlockDescriptor":
        """
        Sets the ROM Block of the NVRAM Block provided by NvBlockSwComponentType.
        A None value is a no-op and does not overwrite an existing block.

        Defines the ROM Block of the NVRAM Block provided by NvBlockSwComponentType.

        Args:
            value: The ParameterDataPrototype to set

        Returns:
            self for method chaining
        """
        if value is not None:
            self.romBlock = value
        return self

    def getSupportDirtyFlag(self):
        """
        Gets whether calling of NvM functions for writing and/or status control of potentially modified RAM Blocks to NV memory shall be controlled by the RTE.

        Specifies whether calling of NvM functions for writing and/ or status control of potentially modified RAM Blocks to NV memory shall be controlled by the RTE.

        Returns:
            Boolean, or None if not set
        """
        return self.supportDirtyFlag

    def setSupportDirtyFlag(self, value) -> "NvBlockDescriptor":
        """
        Sets whether calling of NvM functions for writing and/or status control of potentially modified RAM Blocks to NV memory shall be controlled by the RTE.
        A None value is a no-op and does not overwrite an existing flag.

        Specifies whether calling of NvM functions for writing and/ or status control of potentially modified RAM Blocks to NV memory shall be controlled by the RTE.

        Args:
            value: The supportDirtyFlag flag to set

        Returns:
            self for method chaining
        """
        if value is not None:
            self.supportDirtyFlag = value
        return self

    def getTimingEventRef(self):
        """
        Gets the reference to the TimingEvent to be used by the RTE for implementing a cyclic writing strategy for this block.

        this reference can be taken to identify the TimingEvent to be used by the RTE for implementing a cyclic writing strategy for this block

        Returns:
            RefType, or None if not set
        """
        return self.timingEventRef

    def setTimingEventRef(self, value) -> "NvBlockDescriptor":
        """
        Sets the reference to the TimingEvent to be used by the RTE for implementing a cyclic writing strategy for this block.
        A None value is a no-op and does not overwrite an existing reference.

        this reference can be taken to identify the TimingEvent to be used by the RTE for implementing a cyclic writing strategy for this block

        Args:
            value: The timingEventRef to set

        Returns:
            self for method chaining
        """
        if value is not None:
            self.timingEventRef = value
        return self

    def getWritingStrategies(self) -> List[RoleBasedDataAssignment]:
        """
        Gets the writing strategies for an incoming AutosarDataPrototype.

        This attribute allows for assigning a specific writing strategy for an incoming AutosarDataPrototype.

        Returns:
            List of RoleBasedDataAssignment instances
        """
        return self.writingStrategies

    def addWritingStrategy(self, value: RoleBasedDataAssignment) -> "NvBlockDescriptor":
        """
        Adds a writing strategy for an incoming AutosarDataPrototype.
        A None value is a no-op and does not append anything.

        This attribute allows for assigning a specific writing strategy for an incoming AutosarDataPrototype.

        Args:
            value: The RoleBasedDataAssignment to add

        Returns:
            self for method chaining
        """
        if value is not None and value not in self.writingStrategies:
            self.writingStrategies.append(value)
        return self


class ModeSwitchEventTriggeredActivity(ARObject, VariationPointCapable):
    """
    This meta-class defines an activity of the NvBlockSwComponentType for a specific NvBlock which is triggered by a ModeSwitchEvent.
    """

    # ModeSwitchEventTriggeredActivity method parity checklist:
    # Spec: AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf, Table 11.7, p.675
    # Columns: impl / docstring / test / reader / writer   ([—] = no XML element)
    # [x] __init__                     [x] impl  [x] docstring  [x] test  [—] reader  [—] writer
    # [x] getRole                      [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] setRole                      [x] impl  [x] docstring  [x] test  [x] reader  [—] writer
    # [x] getSwcModeSwitchEventRef     [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] setSwcModeSwitchEventRef     [x] impl  [x] docstring  [x] test  [x] reader  [—] writer

    def __init__(self):
        super().__init__()

        # This attribute indicates which service of the NvM for the NvBlock shall be requested.
        self.role = None

        # This reference identifies the SwcModeSwitchEvent that triggers the activity.
        self.swcModeSwitchEventRef: Optional[RefType] = None

    def getRole(self):
        """
        Gets which service of the NvM for the NvBlock shall be requested.

        This attribute indicates which service of the NvM for the NvBlock shall be requested.

        Returns:
            Identifier, or None if not set
        """
        return self.role

    def setRole(self, value) -> "ModeSwitchEventTriggeredActivity":
        """
        Sets which service of the NvM for the NvBlock shall be requested.
        A None value is a no-op and does not overwrite an existing value.

        This attribute indicates which service of the NvM for the NvBlock shall be requested.

        Args:
            value: The role to set

        Returns:
            self for method chaining
        """
        if value is not None:
            self.role = value
        return self

    def getSwcModeSwitchEventRef(self) -> Optional[RefType]:
        """
        Gets the reference that identifies the SwcModeSwitchEvent that triggers the activity.

        This reference identifies the SwcModeSwitchEvent that triggers the activity.

        Returns:
            RefType, or None if not set
        """
        return self.swcModeSwitchEventRef

    def setSwcModeSwitchEventRef(self, value: Optional[RefType]) -> "ModeSwitchEventTriggeredActivity":
        """
        Sets the reference that identifies the SwcModeSwitchEvent that triggers the activity.
        A None value is a no-op and does not overwrite an existing reference.

        This reference identifies the SwcModeSwitchEvent that triggers the activity.

        Args:
            value: The swcModeSwitchEventRef to set

        Returns:
            self for method chaining
        """
        if value is not None:
            self.swcModeSwitchEventRef = value
        return self
