# This module contains AUTOSAR System Template classes for data transformation
# It defines transformation technologies and end-to-end protection profiles for data safety and security

from abc import ABC
from typing import List

from armodel.models.M2.MSR.AsamHdo.ComputationMethod import CompuScale
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import AREnum, Boolean, Integer, NameToken, PositiveInteger
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import RefType, String
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable import ARElement, Describable, Identifiable


class DataTransformationKindEnum(AREnum):
    """
    Enumeration defining types of data transformations,
    specifying the kind of transformation to be applied
    to data elements in the communication system.
    """
    # DataTransformationKindEnum method parity checklist:
    # [ ] __init__                     [x] impl  [ ] docstring  [ ] test

    def __init__(self):
        super().__init__([])


class DataTransformation(Identifiable):
    """
    Represents a data transformation in the system, defining
    the type of transformation, execution behavior, and
    references to transformation chains for data processing.
    """
    # DataTransformation method parity checklist:
    # [ ] __init__                     [x] impl  [ ] docstring  [ ] test
    # [ ] getDataTransformationKind    [x] impl  [ ] docstring  [ ] test
    # [ ] setDataTransformationKind    [x] impl  [ ] docstring  [ ] test
    # [ ] getExecuteDespiteDataUnavailability [x] impl  [ ] docstring  [ ] test
    # [ ] setExecuteDespiteDataUnavailability [x] impl  [ ] docstring  [ ] test
    # [ ] getTransformerChainRefs      [x] impl  [ ] docstring  [ ] test
    # [ ] addTransformerChainRef       [x] impl  [ ] docstring  [ ] test

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
    # BufferProperties method parity checklist:
    # [ ] __init__                     [x] impl  [ ] docstring  [ ] test
    # [ ] getBufferComputation         [x] impl  [ ] docstring  [ ] test
    # [ ] setBufferComputation         [x] impl  [ ] docstring  [ ] test
    # [ ] getHeaderLength              [x] impl  [ ] docstring  [ ] test
    # [ ] setHeaderLength              [x] impl  [ ] docstring  [ ] test
    # [ ] getInPlace                   [x] impl  [ ] docstring  [ ] test
    # [ ] setInPlace                   [x] impl  [ ] docstring  [ ] test

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
    # TransformationDescription method parity checklist:
    # [ ] __init__                     [x] impl  [ ] docstring  [ ] test

    def __init__(self):
        if type(self) is TransformationDescription:
            raise TypeError("TransformationDescription is an abstract class.")
        super().__init__()


class DataIdModeEnum(AREnum):

    # DataIdModeEnum method parity checklist:
    # [ ] __init__                     [x] impl  [ ] docstring  [ ] test

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

    # EndToEndProfileBehaviorEnum method parity checklist:
    # [ ] __init__                     [x] impl  [ ] docstring  [ ] test

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
    # EndToEndTransformationDescription method parity checklist:
    # [ ] __init__                     [x] impl  [ ] docstring  [ ] test
    # [ ] getClearFromValidToInvalid   [x] impl  [ ] docstring  [ ] test
    # [ ] setClearFromValidToInvalid   [x] impl  [ ] docstring  [ ] test
    # [ ] getCounterOffset             [x] impl  [ ] docstring  [ ] test
    # [ ] setCounterOffset             [x] impl  [ ] docstring  [ ] test
    # [ ] getCrcOffset                 [x] impl  [ ] docstring  [ ] test
    # [ ] setCrcOffset                 [x] impl  [ ] docstring  [ ] test
    # [ ] getDataIdMode                [x] impl  [ ] docstring  [ ] test
    # [ ] setDataIdMode                [x] impl  [ ] docstring  [ ] test
    # [ ] getDataIdNibbleOffset        [x] impl  [ ] docstring  [ ] test
    # [ ] setDataIdNibbleOffset        [x] impl  [ ] docstring  [ ] test
    # [ ] getE2eProfileCompatibilityPropsRef [x] impl  [ ] docstring  [ ] test
    # [ ] setE2eProfileCompatibilityPropsRef [x] impl  [ ] docstring  [ ] test
    # [ ] getMaxDeltaCounter           [x] impl  [ ] docstring  [ ] test
    # [ ] setMaxDeltaCounter           [x] impl  [ ] docstring  [ ] test
    # [ ] getMaxErrorStateInit         [x] impl  [ ] docstring  [ ] test
    # [ ] setMaxErrorStateInit         [x] impl  [ ] docstring  [ ] test
    # [ ] getMaxErrorStateInvalid      [x] impl  [ ] docstring  [ ] test
    # [ ] setMaxErrorStateInvalid      [x] impl  [ ] docstring  [ ] test
    # [ ] getMaxErrorStateValid        [x] impl  [ ] docstring  [ ] test
    # [ ] setMaxErrorStateValid        [x] impl  [ ] docstring  [ ] test
    # [ ] getMaxNoNewOrRepeatedData    [x] impl  [ ] docstring  [ ] test
    # [ ] setMaxNoNewOrRepeatedData    [x] impl  [ ] docstring  [ ] test
    # [ ] getMinOkStateInit            [x] impl  [ ] docstring  [ ] test
    # [ ] setMinOkStateInit            [x] impl  [ ] docstring  [ ] test
    # [ ] getMinOkStateInvalid         [x] impl  [ ] docstring  [ ] test
    # [ ] setMinOkStateInvalid         [x] impl  [ ] docstring  [ ] test
    # [ ] getMinOkStateValid           [x] impl  [ ] docstring  [ ] test
    # [ ] setMinOkStateValid           [x] impl  [ ] docstring  [ ] test
    # [ ] getOffset                    [x] impl  [ ] docstring  [ ] test
    # [ ] setOffset                    [x] impl  [ ] docstring  [ ] test
    # [ ] getProfileBehavior           [x] impl  [ ] docstring  [ ] test
    # [ ] setProfileBehavior           [x] impl  [ ] docstring  [ ] test
    # [ ] getProfileName               [x] impl  [ ] docstring  [ ] test
    # [ ] setProfileName               [x] impl  [ ] docstring  [ ] test
    # [ ] getSyncCounterInit           [x] impl  [ ] docstring  [ ] test
    # [ ] setSyncCounterInit           [x] impl  [ ] docstring  [ ] test
    # [ ] getUpperHeaderBitsToShift    [x] impl  [ ] docstring  [ ] test
    # [ ] setUpperHeaderBitsToShift    [x] impl  [ ] docstring  [ ] test
    # [ ] getWindowSizeInit            [x] impl  [ ] docstring  [ ] test
    # [ ] setWindowSizeInit            [x] impl  [ ] docstring  [ ] test
    # [ ] getWindowSizeInvalid         [x] impl  [ ] docstring  [ ] test
    # [ ] setWindowSizeInvalid         [x] impl  [ ] docstring  [ ] test
    # [ ] getWindowSizeValid           [x] impl  [ ] docstring  [ ] test
    # [ ] setWindowSizeValid           [x] impl  [ ] docstring  [ ] test

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
    
    # TransformerClassEnum method parity checklist:
    # [ ] __init__                     [x] impl  [ ] docstring  [ ] test

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
    # TransformationTechnology method parity checklist:
    # [ ] __init__                     [x] impl  [ ] docstring  [ ] test
    # [ ] getBufferProperties          [x] impl  [ ] docstring  [ ] test
    # [ ] setBufferProperties          [x] impl  [ ] docstring  [ ] test
    # [ ] getHasInternalState          [x] impl  [ ] docstring  [ ] test
    # [ ] setHasInternalState          [x] impl  [ ] docstring  [ ] test
    # [ ] getNeedsOriginalData         [x] impl  [ ] docstring  [ ] test
    # [ ] setNeedsOriginalData         [x] impl  [ ] docstring  [ ] test
    # [ ] getProtocol                  [x] impl  [ ] docstring  [ ] test
    # [ ] setProtocol                  [x] impl  [ ] docstring  [ ] test
    # [ ] getTransformationDescription [x] impl  [ ] docstring  [ ] test
    # [ ] setTransformationDescription [x] impl  [ ] docstring  [ ] test
    # [ ] getTransformerClass          [x] impl  [ ] docstring  [ ] test
    # [ ] setTransformerClass          [x] impl  [ ] docstring  [ ] test
    # [ ] getVersion                   [x] impl  [ ] docstring  [ ] test
    # [ ] setVersion                   [x] impl  [ ] docstring  [ ] test

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
    # DataTransformationSet method parity checklist:
    # [ ] __init__                     [x] impl  [ ] docstring  [ ] test
    # [ ] getDataTransformations       [x] impl  [ ] docstring  [ ] test
    # [ ] createDataTransformation     [x] impl  [ ] docstring  [ ] test
    # [ ] getTransformationTechnologies [x] impl  [ ] docstring  [ ] test
    # [ ] createTransformationTechnology [x] impl  [ ] docstring  [ ] test

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
    # TransformationISignalProps method parity checklist:
    # [ ] __init__                     [x] impl  [ ] docstring  [ ] test
    # [ ] getCsErrorReaction           [x] impl  [ ] docstring  [ ] test
    # [ ] setCsErrorReaction           [x] impl  [ ] docstring  [ ] test
    # [ ] getDataPrototypeTransformationProps [x] impl  [ ] docstring  [ ] test
    # [ ] setDataPrototypeTransformationProps [x] impl  [ ] docstring  [ ] test
    # [ ] getIdent                     [x] impl  [ ] docstring  [ ] test
    # [ ] setIdent                     [x] impl  [ ] docstring  [ ] test
    # [ ] getTransformerRef            [x] impl  [ ] docstring  [ ] test
    # [ ] setTransformerRef            [x] impl  [ ] docstring  [ ] test

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
    # EndToEndTransformationISignalProps method parity checklist:
    # [ ] __init__                     [x] impl  [ ] docstring  [ ] test
    # [ ] getDataIds                   [x] impl  [ ] docstring  [ ] test
    # [ ] addDataId                    [x] impl  [ ] docstring  [ ] test
    # [ ] getDataLength                [x] impl  [ ] docstring  [ ] test
    # [ ] setDataLength                [x] impl  [ ] docstring  [ ] test
    # [ ] getMaxDataLength             [x] impl  [ ] docstring  [ ] test
    # [ ] setMaxDataLength             [x] impl  [ ] docstring  [ ] test
    # [ ] getMinDataLength             [x] impl  [ ] docstring  [ ] test
    # [ ] setMinDataLength             [x] impl  [ ] docstring  [ ] test
    # [ ] getSourceId                  [x] impl  [ ] docstring  [ ] test
    # [ ] setSourceId                  [x] impl  [ ] docstring  [ ] test

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
