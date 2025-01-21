from abc import ABCMeta
from typing import List

from .....M2.MSR.AsamHdo.ComputationMethod import CompuScale
from .....M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import AREnum, Boolean, Integer, NameToken, PositiveInteger
from .....M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import RefType, String
from .....M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import ARObject
from .....M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable import ARElement, Describable, Identifiable


class DataTransformationKindEnum(AREnum):
    def __init__(self):
        super().__init__([])


class DataTransformation(Identifiable):
    def __init__(self, parent: ARObject, short_name: str):
        super().__init__(parent, short_name)

        self.dataTransformationKind = None                              # type: DataTransformationKindEnum
        self.executeDespiteDataUnavailability = None                    # type: Boolean
        self.transformerChainRefs = []                                  # type: List[RefType]

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
    def __init__(self):
        super().__init__()

        self.bufferComputation = None                       # type: CompuScale
        self.headerLength = None                            # type: Integer
        self.inPlace = None                                 # type: Boolean

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
    
    
class TransformationDescription(Describable, metaclass=ABCMeta):
    def __init__(self):
        if type(self) is TransformationDescription:
            raise NotImplementedError("TransformationDescription is an abstract class.")
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
    def __init__(self):
        super().__init__()

        self.clearFromValidToInvalid = None                                 # type: Boolean
        self.counterOffset = None                                           # type: PositiveInteger
        self.crcOffset = None                                               # type: PositiveInteger
        self.dataIdMode = None                                              # type: DataIdModeEnum
        self.dataIdNibbleOffset = None                                      # type: PositiveInteger
        self.e2eProfileCompatibilityPropsRef = None                         # type: RefType
        self.maxDeltaCounter = None                                         # type: PositiveInteger
        self.maxErrorStateInit = None                                       # type: PositiveInteger
        self.maxErrorStateInvalid = None                                    # type: PositiveInteger
        self.maxErrorStateValid = None                                      # type: PositiveInteger
        self.maxNoNewOrRepeatedData = None                                  # type: PositiveInteger
        self.minOkStateInit = None                                          # type: PositiveInteger
        self.minOkStateInvalid = None                                       # type: PositiveInteger
        self.minOkStateValid = None                                         # type: PositiveInteger
        self.offset = None                                                  # type: PositiveInteger
        self.profileBehavior = None                                         # type: EndToEndProfileBehaviorEnum
        self.profileName = None                                             # type: NameToken
        self.syncCounterInit = None                                         # type: PositiveInteger
        self.upperHeaderBitsToShift = None                                  # type: PositiveInteger
        self.windowSizeInit = None                                          # type: PositiveInteger
        self.windowSizeInvalid = None                                       # type: PositiveInteger
        self.windowSizeValid = None                                         # type: PositiveInteger

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
    def __init__(self, parent: ARObject, short_name: str):
        super().__init__(parent, short_name)

        self.bufferProperties = None                        # type: BufferProperties
        self.hasInternalState = None                        # type: Boolean
        self.needsOriginalData = None                       # type: Boolean
        self.protocol = None                                # type: String
        self.transformationDescription = None               # type: TransformationDescription
        self.transformerClass = None                        # type: TransformerClassEnum
        self.version = None                                 # type: String

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
    def __init__(self, parent: ARObject, short_name: str):
        super().__init__(parent, short_name)

        self.dataTransformations = []                       # type: List[DataTransformation]
        self.transformationTechnologies = []                # type: List[TransformationTechnology]

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


class TransformationISignalProps(Describable, metaclass=ABCMeta):
    def __init__(self):
        super().__init__()

        self.csErrorReaction = None                                 # type: CSTransformerErrorReactionEnum
        self.dataPrototypeTransformationProps = []                  # type: List[DataPrototypeTransformationProps]
        self.ident = None                                           # type: TransformationISignalPropsIdent
        self.transformerRef = None                                  # type: RefType

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
    def __init__(self):
        super().__init__()

        self.dataIds = []                                   # type: List[PositiveInteger]
        self.dataLength = None                              # type: PositiveInteger
        self.maxDataLength = None                           # type: PositiveInteger
        self.minDataLength = None                           # type: PositiveInteger
        self.sourceId = None                                # type: PositiveInteger

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
