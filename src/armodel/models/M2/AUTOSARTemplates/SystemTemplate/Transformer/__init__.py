# This module contains AUTOSAR System Template classes for data transformation
# It defines transformation technologies and end-to-end protection profiles for data safety and security

from abc import ABC
from typing import List

from .....M2.MSR.AsamHdo.ComputationMethod import CompuScale
from .....M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import AREnum, Boolean, Integer, NameToken, PositiveInteger
from .....M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import RefType, String
from .....M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import ARObject
from .....M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable import ARElement, Describable, Identifiable


class DataTransformationKindEnum(AREnum):
    """
    Enumeration defining types of data transformations,
    specifying the kind of transformation to be applied
    to data elements in the communication system.
    """
    def __init__(self):
        super().__init__([])


class DataTransformation(Identifiable):
    """
    Represents a data transformation in the system, defining
    the type of transformation, execution behavior, and
    references to transformation chains for data processing.
    """
    def __init__(self, parent: ARObject, short_name: str):
        super().__init__(parent, short_name)

        self.dataTransformationKind: DataTransformationKindEnum = None
        self.executeDespiteDataUnavailability: Boolean = None
        self.transformerChainRefs: List[RefType] = []

    def getDataTransformationKind(self):
        return self.dataTransformationKind

    def setDataTransformationKind(self, value):
        if value is not None:
            self.dataTransformationKind = value
        return self

    def getExecuteDespiteDataUnavailability(self):
        return self.executeDespiteDataUnavailability

    def setExecuteDespiteDataUnavailability(self, value):
        if value is not None:
            self.executeDespiteDataUnavailability = value
        return self

    def getTransformerChainRefs(self):
        return self.transformerChainRefs

    def addTransformerChainRef(self, value):
        if value is not None:
            self.transformerChainRefs.append(value)
        return self
    

class BufferProperties(ARObject):
    """
    Defines properties for data buffers used in transformations,
    specifying computation scales, header lengths, and in-place
    processing capabilities for buffer management.
    """
    def __init__(self):
        super().__init__()

        self.bufferComputation: CompuScale = None
        self.headerLength: Integer = None
        self.inPlace: Boolean = None

    def getBufferComputation(self):
        return self.bufferComputation

    def setBufferComputation(self, value):
        if value is not None:
            self.bufferComputation = value
        return self

    def getHeaderLength(self):
        return self.headerLength

    def setHeaderLength(self, value):
        if value is not None:
            self.headerLength = value
        return self

    def getInPlace(self):
        return self.inPlace

    def setInPlace(self, value):
        if value is not None:
            self.inPlace = value
        return self
    
    
class TransformationDescription(Describable, ABC):
    """
    Abstract base class for transformation descriptions,
    defining common properties for different types of
    data transformation descriptions in the system.
    """
    def __init__(self):
        if type(self) is TransformationDescription:
            raise TypeError("TransformationDescription is an abstract class.")
        super().__init__()


class DataIdModeEnum(AREnum):

    ALL_16_BIT = "all16Bit"
    ALTERNATING_8_BIT = "alternating8Bit"
    LOWER_12_BIT = "lower12Bit"
    LOWER_8_BIT = "lower8Bit"

    def __init__(self):
        super().__init__([
            DataIdModeEnum.ALL_16_BIT,
            DataIdModeEnum.ALTERNATING_8_BIT,
            DataIdModeEnum.LOWER_12_BIT,
            DataIdModeEnum.LOWER_8_BIT
        ])


class EndToEndProfileBehaviorEnum(AREnum):

    PRE_R4_2 = "PRE_R4_2"
    R4_2 = "R4_2"

    def __init__(self):
        super().__init__([
            EndToEndProfileBehaviorEnum.PRE_R4_2,
            EndToEndProfileBehaviorEnum.R4_2
        ])


class EndToEndTransformationDescription(TransformationDescription):
    """
    Defines end-to-end transformation properties for data protection,
    specifying counter offsets, CRC calculations, data ID modes,
    and profile behavior for safe data transmission.
    """
    def __init__(self):
        super().__init__()

        self.clearFromValidToInvalid: Boolean = None
        self.counterOffset: PositiveInteger = None
        self.crcOffset: PositiveInteger = None
        self.dataIdMode: DataIdModeEnum = None
        self.dataIdNibbleOffset: PositiveInteger = None
        self.e2eProfileCompatibilityPropsRef: RefType = None
        self.maxDeltaCounter: PositiveInteger = None
        self.maxErrorStateInit: PositiveInteger = None
        self.maxErrorStateInvalid: PositiveInteger = None
        self.maxErrorStateValid: PositiveInteger = None
        self.maxNoNewOrRepeatedData: PositiveInteger = None
        self.minOkStateInit: PositiveInteger = None
        self.minOkStateInvalid: PositiveInteger = None
        self.minOkStateValid: PositiveInteger = None
        self.offset: PositiveInteger = None
        self.profileBehavior: EndToEndProfileBehaviorEnum = None
        self.profileName: NameToken = None
        self.syncCounterInit: PositiveInteger = None
        self.upperHeaderBitsToShift: PositiveInteger = None
        self.windowSizeInit: PositiveInteger = None
        self.windowSizeInvalid: PositiveInteger = None
        self.windowSizeValid: PositiveInteger = None

    def getClearFromValidToInvalid(self):
        return self.clearFromValidToInvalid

    def setClearFromValidToInvalid(self, value):
        if value is not None:
            self.clearFromValidToInvalid = value
        return self

    def getCounterOffset(self):
        return self.counterOffset

    def setCounterOffset(self, value):
        if value is not None:
            self.counterOffset = value
        return self

    def getCrcOffset(self):
        return self.crcOffset

    def setCrcOffset(self, value):
        if value is not None:
            self.crcOffset = value
        return self

    def getDataIdMode(self):
        return self.dataIdMode

    def setDataIdMode(self, value):
        if value is not None:
            self.dataIdMode = value
        return self

    def getDataIdNibbleOffset(self):
        return self.dataIdNibbleOffset

    def setDataIdNibbleOffset(self, value):
        if value is not None:
            self.dataIdNibbleOffset = value
        return self

    def getE2eProfileCompatibilityPropsRef(self):
        return self.e2eProfileCompatibilityPropsRef

    def setE2eProfileCompatibilityPropsRef(self, value):
        if value is not None:
            self.e2eProfileCompatibilityPropsRef = value
        return self

    def getMaxDeltaCounter(self):
        return self.maxDeltaCounter

    def setMaxDeltaCounter(self, value):
        if value is not None:
            self.maxDeltaCounter = value
        return self

    def getMaxErrorStateInit(self):
        return self.maxErrorStateInit

    def setMaxErrorStateInit(self, value):
        if value is not None:
            self.maxErrorStateInit = value
        return self

    def getMaxErrorStateInvalid(self):
        return self.maxErrorStateInvalid

    def setMaxErrorStateInvalid(self, value):
        if value is not None:
            self.maxErrorStateInvalid = value
        return self

    def getMaxErrorStateValid(self):
        return self.maxErrorStateValid

    def setMaxErrorStateValid(self, value):
        if value is not None:
            self.maxErrorStateValid = value
        return self

    def getMaxNoNewOrRepeatedData(self):
        return self.maxNoNewOrRepeatedData

    def setMaxNoNewOrRepeatedData(self, value):
        if value is not None:
            self.maxNoNewOrRepeatedData = value
        return self

    def getMinOkStateInit(self):
        return self.minOkStateInit

    def setMinOkStateInit(self, value):
        if value is not None:
            self.minOkStateInit = value
        return self

    def getMinOkStateInvalid(self):
        return self.minOkStateInvalid

    def setMinOkStateInvalid(self, value):
        if value is not None:
            self.minOkStateInvalid = value
        return self

    def getMinOkStateValid(self):
        return self.minOkStateValid

    def setMinOkStateValid(self, value):
        if value is not None:
            self.minOkStateValid = value
        return self

    def getOffset(self):
        return self.offset

    def setOffset(self, value):
        if value is not None:
            self.offset = value
        return self

    def getProfileBehavior(self):
        return self.profileBehavior

    def setProfileBehavior(self, value):
        if value is not None:
            self.profileBehavior = value
        return self

    def getProfileName(self):
        return self.profileName

    def setProfileName(self, value):
        if value is not None:
            self.profileName = value
        return self

    def getSyncCounterInit(self):
        return self.syncCounterInit

    def setSyncCounterInit(self, value):
        if value is not None:
            self.syncCounterInit = value
        return self

    def getUpperHeaderBitsToShift(self):
        return self.upperHeaderBitsToShift

    def setUpperHeaderBitsToShift(self, value):
        if value is not None:
            self.upperHeaderBitsToShift = value
        return self

    def getWindowSizeInit(self):
        return self.windowSizeInit

    def setWindowSizeInit(self, value):
        if value is not None:
            self.windowSizeInit = value
        return self

    def getWindowSizeInvalid(self):
        return self.windowSizeInvalid

    def setWindowSizeInvalid(self, value):
        if value is not None:
            self.windowSizeInvalid = value
        return self

    def getWindowSizeValid(self):
        return self.windowSizeValid

    def setWindowSizeValid(self, value):
        if value is not None:
            self.windowSizeValid = value
        return self


class TransformerClassEnum(AREnum):
    
    CUSTOM = "custom"
    SAFETY = "safety"
    SECURITY = "security"
    SERIALIZER = "serializer"

    def __init__(self):
        super().__init__([
            TransformerClassEnum.CUSTOM,
            TransformerClassEnum.SAFETY,
            TransformerClassEnum.SECURITY,
            TransformerClassEnum.SERIALIZER
        ])


class TransformationTechnology(Identifiable):
    """
    Represents a transformation technology in the system,
    defining buffer properties, state management, protocol
    specifications, and transformer class for data transformation.
    """
    def __init__(self, parent: ARObject, short_name: str):
        super().__init__(parent, short_name)

        self.bufferProperties: BufferProperties = None
        self.hasInternalState: Boolean = None
        self.needsOriginalData: Boolean = None
        self.protocol: String = None
        self.transformationDescription: TransformationDescription = None
        self.transformerClass: TransformerClassEnum = None
        self.version: String = None

    def getBufferProperties(self):
        return self.bufferProperties

    def setBufferProperties(self, value):
        if value is not None:
            self.bufferProperties = value
        return self

    def getHasInternalState(self):
        return self.hasInternalState

    def setHasInternalState(self, value):
        if value is not None:
            self.hasInternalState = value
        return self

    def getNeedsOriginalData(self):
        return self.needsOriginalData

    def setNeedsOriginalData(self, value):
        if value is not None:
            self.needsOriginalData = value
        return self

    def getProtocol(self):
        return self.protocol

    def setProtocol(self, value):
        if value is not None:
            self.protocol = value
        return self

    def getTransformationDescription(self):
        return self.transformationDescription

    def setTransformationDescription(self, value):
        if value is not None:
            self.transformationDescription = value
        return self

    def getTransformerClass(self):
        return self.transformerClass

    def setTransformerClass(self, value):
        if value is not None:
            self.transformerClass = value
        return self

    def getVersion(self):
        return self.version

    def setVersion(self, value):
        if value is not None:
            self.version = value
        return self


class DataTransformationSet(ARElement):
    """
    Represents a set of data transformations in the system,
    organizing multiple data transformations and transformation
    technologies for comprehensive data processing configurations.
    """
    def __init__(self, parent: ARObject, short_name: str):
        super().__init__(parent, short_name)

        self.dataTransformations: List[DataTransformation] = []
        self.transformationTechnologies: List[TransformationTechnology] = []

    def getDataTransformations(self):
        return self.dataTransformations

    def createDataTransformation(self, short_name: str) -> DataTransformation:
        if (not self.IsElementExists(short_name)):
            dfs = DataTransformation(self, short_name)
            self.addElement(dfs)
            self.dataTransformations.append(dfs)
        return self.getElement(short_name)

    def getTransformationTechnologies(self):
        return self.transformationTechnologies

    def createTransformationTechnology(self, short_name: str) -> TransformationTechnology:
        if (not self.IsElementExists(short_name)):
            tech = TransformationTechnology(self, short_name)
            self.addElement(tech)
            self.transformationTechnologies.append(tech)
        return self.getElement(short_name)


class TransformationISignalProps(Describable, ABC):
    """
    Abstract base class for transformation interaction signal properties,
    defining common properties for signal transformation including
    error reactions, data prototype properties, and transformer references.
    """
    def __init__(self):
        if type(self) is TransformationISignalProps:
            raise TypeError("TransformationISignalProps is an abstract class.")
        super().__init__()

        self.csErrorReaction = None
        self.dataPrototypeTransformationProps: List = []
        self.ident = None
        self.transformerRef: RefType = None

    def getCsErrorReaction(self):
        return self.csErrorReaction

    def setCsErrorReaction(self, value):
        if value is not None:
            self.csErrorReaction = value
        return self

    def getDataPrototypeTransformationProps(self):
        return self.dataPrototypeTransformationProps

    def setDataPrototypeTransformationProps(self, value):
        if value is not None:
            self.dataPrototypeTransformationProps = value
        return self

    def getIdent(self):
        return self.ident

    def setIdent(self, value):
        if value is not None:
            self.ident = value
        return self

    def getTransformerRef(self):
        return self.transformerRef

    def setTransformerRef(self, value):
        if value is not None:
            self.transformerRef = value
        return self


class EndToEndTransformationISignalProps(TransformationISignalProps):
    """
    Defines end-to-end transformation properties for interaction signals,
    specifying data IDs, length constraints, and source identifiers
    for protected signal transmission.
    """
    def __init__(self):
        super().__init__()

        self.dataIds: List[PositiveInteger] = []
        self.dataLength: PositiveInteger = None
        self.maxDataLength: PositiveInteger = None
        self.minDataLength: PositiveInteger = None
        self.sourceId: PositiveInteger = None

    def getDataIds(self):
        return self.dataIds

    def addDataId(self, value):
        if value is not None:
            self.dataIds.append(value)
        return self

    def getDataLength(self):
        return self.dataLength

    def setDataLength(self, value):
        if value is not None:
            self.dataLength = value
        return self

    def getMaxDataLength(self):
        return self.maxDataLength

    def setMaxDataLength(self, value):
        if value is not None:
            self.maxDataLength = value
        return self

    def getMinDataLength(self):
        return self.minDataLength

    def setMinDataLength(self, value):
        if value is not None:
            self.minDataLength = value
        return self

    def getSourceId(self):
        return self.sourceId

    def setSourceId(self, value):
        if value is not None:
            self.sourceId = value
        return self