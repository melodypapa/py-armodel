# This module contains AUTOSAR System Template classes for data transformation
# It defines transformation technologies and end-to-end protection profiles for data safety and security

from abc import ABC
from typing import List, Optional

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import AREnum, Boolean, Integer, NameToken, PositiveInteger
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import RefType, String
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable import ARElement, Describable, Identifiable
from armodel.models.M2.AUTOSARTemplates.GenericStructure.AbstractStructure import AtpInstanceRef
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.Communication import TransformationComSpecProps
from armodel.models.M2.MSR.DataDictionary.DataDefProperties import SwDataDefProps


class DataTransformationKindEnum(AREnum):
    """
    This enumeration contributes to the definition of the scope of the DataTransformation.
    """

    # DataTransformationKindEnum method parity checklist:
    # Spec: AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf, Table 4.40, p.150
    # Spec verified: R23-11
    # (no methods)

    # The DataTransformation shall only be applied to the receiving end only, i.e. transform from byte array to data type. Tags: atp.EnumerationLiteralIndex=0
    ASYMMETRIC_FROM_BYTE_ARRAY = "asymmetricFromByteArray"

    # The DataTransformation shall be applied to the sending end only, i.e. from data type to byte array. Tags: atp.EnumerationLiteralIndex=1
    ASYMMETRIC_TO_BYTE_ARRAY = "asymmetricToByteArray"

    # The DataTransformation shall be applied at both the sending and the receiving end of the communication. Tags: atp.EnumerationLiteralIndex=2
    SYMMETRIC = "symmetric"

    def __init__(self):
        super().__init__(
            (
                DataTransformationKindEnum.ASYMMETRIC_FROM_BYTE_ARRAY,
                DataTransformationKindEnum.ASYMMETRIC_TO_BYTE_ARRAY,
                DataTransformationKindEnum.SYMMETRIC,
            )
        )


class DataTransformation(Identifiable):
    """
    A DataTransformation represents a transformer chain. It is an ordered list of transformers.
    """

    # DataTransformation method parity checklist:
    # Spec: AUTOSAR_CP_TPS_SystemTemplate.pdf, Table 7.2, p.763
    # Spec verified: R23-11
    # Columns: impl / docstring / test / reader / writer   ([—] = no XML element)
    # [x] __init__                     [x] impl  [x] docstring  [x] test  [—] reader  [—] writer
    # [x] getDataTransformationKind    [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] setDataTransformationKind    [x] impl  [x] docstring  [x] test  [x] reader  [—] writer
    # [x] getExecuteDespiteDataUnavailability [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] setExecuteDespiteDataUnavailability [x] impl  [x] docstring  [x] test  [x] reader  [—] writer
    # [x] getTransformerChainRefs      [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] addTransformerChainRef       [x] impl  [x] docstring  [x] test  [x] reader  [—] writer

    def __init__(self, parent: ARObject, short_name: str):
        super().__init__(parent, short_name)

        # This attribute controls the kind of DataTransformation to be applied.
        self.dataTransformationKind: Optional[DataTransformationKindEnum] = None

        # Specifies whether the transformer chain is executed even if no input data are available.
        self.executeDespiteDataUnavailability: Optional[Boolean] = None

        # This attribute represents the definition of a chain of transformers that are supposed to be executed according to the order of being referenced from DataTransformation.
        self.transformerChainRefs: List[RefType] = []

    def getDataTransformationKind(self) -> Optional[DataTransformationKindEnum]:
        """
        This attribute controls the kind of DataTransformation to be applied.
        """
        return self.dataTransformationKind

    def setDataTransformationKind(self, value: Optional[DataTransformationKindEnum]) -> "DataTransformation":
        """
        This attribute controls the kind of DataTransformation to be applied.
        A None value is a no-op and does not overwrite an existing dataTransformationKind.
        """
        if value is not None:
            self.dataTransformationKind = value
        return self

    def getExecuteDespiteDataUnavailability(self) -> Optional[Boolean]:
        """
        Specifies whether the transformer chain is executed even if no input data are available.
        """
        return self.executeDespiteDataUnavailability

    def setExecuteDespiteDataUnavailability(self, value: Optional[Boolean]) -> "DataTransformation":
        """
        Specifies whether the transformer chain is executed even if no input data are available.
        A None value is a no-op and does not overwrite an existing executeDespiteDataUnavailability.
        """
        if value is not None:
            self.executeDespiteDataUnavailability = value
        return self

    def getTransformerChainRefs(self) -> List[RefType]:
        """
        This attribute represents the definition of a chain of transformers that are supposed to be executed according to the order of being referenced from DataTransformation.
        """
        return self.transformerChainRefs

    def addTransformerChainRef(self, value: Optional[RefType]) -> "DataTransformation":
        """
        This attribute represents the definition of a chain of transformers that are supposed to be executed according to the order of being referenced from DataTransformation.
        A None value is a no-op and does not add to transformerChainRefs.
        """
        if value is not None:
            self.transformerChainRefs.append(value)
        return self


class BufferProperties(ARObject):
    """
    Configuration of the buffer properties the transformer needs to work.

    [constr_9279] Existence of BufferProperties . headerLength: For each BufferProperties , the attribute headerLength shall exist at the time when the System Description is complete . ()
    [constr_9280] Existence of BufferProperties . inPlace: For each BufferProperties , the attribute inPlace shall exist at the time when the System Description is complete . ()
    """

    # BufferProperties method parity checklist:
    # Spec: AUTOSAR_CP_TPS_SystemTemplate.pdf, Table 7.5, p.767
    # Spec verified: R23-11
    # Columns: impl / docstring / test / reader / writer   ([—] = no XML element)
    # [x] __init__          [x] impl  [x] docstring  [x] test  [—] reader  [—] writer
    # [x] getHeaderLength   [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] setHeaderLength   [x] impl  [x] docstring  [x] test  [x] reader  [—] writer
    # [x] getInPlace        [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] setInPlace        [x] impl  [x] docstring  [x] test  [x] reader  [—] writer

    def __init__(self):
        super().__init__()

        # Defines the length of the header (in bits) this transformer will add in front of the data.
        self.headerLength: Optional[Integer] = None

        # If set, the transformer uses the input buffer as output buffer.
        self.inPlace: Optional[Boolean] = None

    def getHeaderLength(self) -> Optional[Integer]:
        """
        Defines the length of the header (in bits) this transformer will add in front of the data.
        """
        return self.headerLength

    def setHeaderLength(self, value: Optional[Integer]) -> "BufferProperties":
        """
        Defines the length of the header (in bits) this transformer will add in front of the data.
        A None value is a no-op and does not overwrite an existing headerLength.
        """
        if value is not None:
            self.headerLength = value
        return self

    def getInPlace(self) -> Optional[Boolean]:
        """
        If set, the transformer uses the input buffer as output buffer.
        """
        return self.inPlace

    def setInPlace(self, value: Optional[Boolean]) -> "BufferProperties":
        """
        If set, the transformer uses the input buffer as output buffer.
        A None value is a no-op and does not overwrite an existing inPlace.
        """
        if value is not None:
            self.inPlace = value
        return self


class TransformationDescription(Describable, ABC):
    """
    The TransformationDescription is the abstract class that can be used by specific transformers to add transformer specific properties.
    """

    # TransformationDescription method parity checklist:
    # Spec: AUTOSAR_CP_TPS_SystemTemplate.pdf, Table 7.6, p.771
    # Spec verified: R23-11
    # Columns: impl / docstring / test / reader / writer   ([—] = no XML element)
    # [x] __init__  [x] impl  [x] docstring  [x] test  [—] reader  [—] writer

    def __init__(self):
        if type(self) is TransformationDescription:
            raise TypeError("TransformationDescription is an abstract class.")
        super().__init__()


class DataIdModeEnum(AREnum):
    """
    Supported inclusion modes to include the implicit two-byte Data ID in the one-byte CRC.
    """

    # DataIdModeEnum method parity checklist:
    # Spec: AUTOSAR_CP_TPS_SystemTemplate.pdf, Table 7.24, p.807
    # Spec verified: R23-11
    # (no methods)

    # Two bytes are included in the CRC (double ID configuration). Tags: atp.EnumerationLiteralIndex=0
    ALL_16_BIT = "all16Bit"

    # One of the two bytes byte is included, alternating high and low byte, depending on parity of the counter (alternating ID configuration). For even counter low byte is included; For odd counters the high byte is included. Tags: atp.EnumerationLiteralIndex=1
    ALTERNATING_8_BIT = "alternating8Bit"

    # The low byte is included in the implicit CRC calculation, the low nibble of the high byte is transmitted along with the data (i.e. it is explicitly included), the high nibble of the high byte is not used. This is applicable for the IDs up to 12 bits. Tags: atp.EnumerationLiteralIndex=2
    LOWER_12_BIT = "lower12Bit"

    # Only low byte is included, high byte is never used. This is applicable if the IDs in a particular system are 8 bits. Tags: atp.EnumerationLiteralIndex=3
    LOWER_8_BIT = "lower8Bit"

    def __init__(self):
        super().__init__(
            (
                DataIdModeEnum.ALL_16_BIT,
                DataIdModeEnum.ALTERNATING_8_BIT,
                DataIdModeEnum.LOWER_12_BIT,
                DataIdModeEnum.LOWER_8_BIT,
            )
        )


class EndToEndProfileBehaviorEnum(AREnum):
    """
    Behavior of the check functionality
    """

    # EndToEndProfileBehaviorEnum method parity checklist:
    # Spec: AUTOSAR_CP_TPS_SystemTemplate.pdf, Table 7.26, p.808
    # Spec verified: R23-11
    # (no methods)

    # Check has the legacy behavior, before AUTOSAR Release 4.2. Tags: atp.EnumerationLiteralIndex=0 xml.name=PRE-R-4-2
    PRE_R4_2 = "PRE_R4_2"

    # Check behaves like new P4/P5/P6 profiles introduced in AUTOSAR Release 4.2. Tags: atp.EnumerationLiteralIndex=1 xml.name=R-4-2
    R4_2 = "R4_2"

    def __init__(self):
        super().__init__(
            (
                EndToEndProfileBehaviorEnum.PRE_R4_2,
                EndToEndProfileBehaviorEnum.R4_2,
            )
        )


class E2EProfileCompatibilityProps(ARElement):
    """
    This meta-class collects settings for configuration of the E2E state machine. Tags: atp.recommendedPackage=E2EProfileCompatibilityPropsCollection
    """

    # E2EProfileCompatibilityProps method parity checklist:
    # Spec: AUTOSAR_CP_TPS_SystemTemplate.pdf, Table 7.25, p.808
    # Spec verified: R23-11
    # Columns: impl / docstring / test / reader / writer   ([—] = no XML element)
    # [x] __init__                       [x] impl  [x] docstring  [x] test  [x] reader  [x] writer
    # [x] getTransitToInvalidExtended    [x] impl  [x] docstring  [x] test  [x] reader  [x] writer
    # [x] setTransitToInvalidExtended    [x] impl  [x] docstring  [x] test  [x] reader  [x] writer

    def __init__(self, parent: ARObject, short_name: str):
        super().__init__(parent, short_name)

        # E2E State machine behavior concerning transition from NODATA/INIT to INVALID value=0 (false): no direct transition from NODATA to INVALID, no transition from INIT to INVALID due to counter-related faults (Autosar R19-11 or former behavior) value=1 (true): direct transition from NODATA to INVALID covered, transition from INIT to INVALID due to counter-related faults covered (state machine extended)
        self.transitToInvalidExtended: Optional[Boolean] = None

    def getTransitToInvalidExtended(self) -> Optional[Boolean]:
        """
        E2E State machine behavior concerning transition from NODATA/INIT to INVALID value=0 (false): no direct transition from NODATA to INVALID, no transition from INIT to INVALID due to counter-related faults (Autosar R19-11 or former behavior) value=1 (true): direct transition from NODATA to INVALID covered, transition from INIT to INVALID due to counter-related faults covered (state machine extended)
        """
        return self.transitToInvalidExtended

    def setTransitToInvalidExtended(self, value: Optional[Boolean]) -> "E2EProfileCompatibilityProps":
        """
        E2E State machine behavior concerning transition from NODATA/INIT to INVALID value=0 (false): no direct transition from NODATA to INVALID, no transition from INIT to INVALID due to counter-related faults (Autosar R19-11 or former behavior) value=1 (true): direct transition from NODATA to INVALID covered, transition from INIT to INVALID due to counter-related faults covered (state machine extended)

        If value is None, this method does nothing and returns self (no-op for None).
        """
        if value is not None:
            self.transitToInvalidExtended = value
        return self


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
    """
    Specifies the transformer class of a transformer.
    """

    # TransformerClassEnum method parity checklist:
    # Spec: AUTOSAR_CP_TPS_SystemTemplate.pdf, Table 7.4, p.765
    # Spec verified: R23-11
    # (no methods)

    # The transformer is a custom transformer. Tags: atp.EnumerationLiteralIndex=0
    CUSTOM = "custom"

    # The transformer is a safety transformer. Tags: atp.EnumerationLiteralIndex=1
    SAFETY = "safety"

    # The transformer is a security transformer. Tags: atp.EnumerationLiteralIndex=2
    SECURITY = "security"

    # The transformer is a serializing transformer. Tags: atp.EnumerationLiteralIndex=3
    SERIALIZER = "serializer"

    def __init__(self):
        super().__init__([TransformerClassEnum.CUSTOM, TransformerClassEnum.SAFETY, TransformerClassEnum.SECURITY, TransformerClassEnum.SERIALIZER])


class TransformationTechnology(Identifiable):
    """
    A TransformationTechnology is a transformer inside a transformer chain. Tags: xml.namePlural=TRANSFORMATION-TECHNOLOGIES
    """

    # TransformationTechnology method parity checklist:
    # Spec: AUTOSAR_CP_TPS_SystemTemplate.pdf, Table 7.3, p.764
    # Spec verified: R23-11
    # Columns: impl / docstring / test / reader / writer   ([—] = no XML element)
    # [x] __init__          [x] impl  [x] docstring  [x] test  [—] reader  [—] writer
    # [x] setBufferProperties   [x] impl  [x] docstring  [x] test  [x] reader  [—] writer
    # [x] getBufferProperties   [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] setHasInternalState   [x] impl  [x] docstring  [x] test  [x] reader  [—] writer
    # [x] getHasInternalState   [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] setNeedsOriginalData  [x] impl  [x] docstring  [x] test  [x] reader  [—] writer
    # [x] getNeedsOriginalData  [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] setProtocol           [x] impl  [x] docstring  [x] test  [x] reader  [—] writer
    # [x] getProtocol           [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] setTransformationDescription [x] impl  [x] docstring  [x] test  [x] reader  [—] writer
    # [x] getTransformationDescription [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] setTransformerClass    [x] impl  [x] docstring  [x] test  [x] reader  [—] writer
    # [x] getTransformerClass    [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] setVersion             [x] impl  [x] docstring  [x] test  [x] reader  [—] writer
    # [x] getVersion             [x] impl  [x] docstring  [x] test  [—] reader  [x] writer

    def __init__(self, parent: ARObject, short_name: str):
        super().__init__(parent, short_name)

        # Aggregation of the mandatory BufferProperties.
        self.bufferProperties: Optional[BufferProperties] = None

        # This attribute defines whether the Transformer has an internal state or not.
        self.hasInternalState: Optional[Boolean] = None

        # Specifies whether this transformer gets access to the SWC's original data.
        self.needsOriginalData: Optional[Boolean] = None

        # Specifies the protocol that is implemented by this transformer.
        self.protocol: Optional[String] = None

        # A transformer can be configured with transformer specific parameters which are represented by the Transformer Description.
        self.transformationDescription: Optional[TransformationDescription] = None

        # Specifies to which transformer class this transformer belongs.
        self.transformerClass: Optional[TransformerClassEnum] = None

        # Version of the implemented protocol.
        self.version: Optional[String] = None

    def setBufferProperties(self, value: Optional[BufferProperties]) -> "TransformationTechnology":
        """
        Aggregation of the mandatory BufferProperties.
        A None value is a no-op and does not overwrite an existing bufferProperties.
        """
        if value is not None:
            self.bufferProperties = value
        return self

    def getBufferProperties(self) -> Optional[BufferProperties]:
        """
        Aggregation of the mandatory BufferProperties.
        """
        return self.bufferProperties

    def setHasInternalState(self, value: Optional[Boolean]) -> "TransformationTechnology":
        """
        This attribute defines whether the Transformer has an internal state or not.
        A None value is a no-op and does not overwrite an existing hasInternalState.
        """
        if value is not None:
            self.hasInternalState = value
        return self

    def getHasInternalState(self) -> Optional[Boolean]:
        """
        This attribute defines whether the Transformer has an internal state or not.
        """
        return self.hasInternalState

    def setNeedsOriginalData(self, value: Optional[Boolean]) -> "TransformationTechnology":
        """
        Specifies whether this transformer gets access to the SWC's original data.
        A None value is a no-op and does not overwrite an existing needsOriginalData.
        """
        if value is not None:
            self.needsOriginalData = value
        return self

    def getNeedsOriginalData(self) -> Optional[Boolean]:
        """
        Specifies whether this transformer gets access to the SWC's original data.
        """
        return self.needsOriginalData

    def setProtocol(self, value: Optional[String]) -> "TransformationTechnology":
        """
        Specifies the protocol that is implemented by this transformer.
        A None value is a no-op and does not overwrite an existing protocol.
        """
        if value is not None:
            self.protocol = value
        return self

    def getProtocol(self) -> Optional[String]:
        """
        Specifies the protocol that is implemented by this transformer.
        """
        return self.protocol

    def setTransformationDescription(self, value: Optional[TransformationDescription]) -> "TransformationTechnology":
        """
        A transformer can be configured with transformer specific parameters which are represented by the Transformer Description.
        A None value is a no-op and does not overwrite an existing transformationDescription.
        """
        if value is not None:
            self.transformationDescription = value
        return self

    def getTransformationDescription(self) -> Optional[TransformationDescription]:
        """
        A transformer can be configured with transformer specific parameters which are represented by the Transformer Description.
        """
        return self.transformationDescription

    def setTransformerClass(self, value: Optional[TransformerClassEnum]) -> "TransformationTechnology":
        """
        Specifies to which transformer class this transformer belongs.
        A None value is a no-op and does not overwrite an existing transformerClass.
        """
        if value is not None:
            self.transformerClass = value
        return self

    def getTransformerClass(self) -> Optional[TransformerClassEnum]:
        """
        Specifies to which transformer class this transformer belongs.
        """
        return self.transformerClass

    def setVersion(self, value: Optional[String]) -> "TransformationTechnology":
        """
        Version of the implemented protocol.
        A None value is a no-op and does not overwrite an existing version.
        """
        if value is not None:
            self.version = value
        return self

    def getVersion(self) -> Optional[String]:
        """
        Version of the implemented protocol.
        """
        return self.version


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
        if not self.IsElementExists(short_name):
            dfs = DataTransformation(self, short_name)
            self.addElement(dfs)
            self.dataTransformations.append(dfs)
        return self.getElement(short_name)

    def getTransformationTechnologies(self):
        return self.transformationTechnologies

    def createTransformationTechnology(self, short_name: str) -> TransformationTechnology:
        if not self.IsElementExists(short_name):
            tech = TransformationTechnology(self, short_name)
            self.addElement(tech)
            self.transformationTechnologies.append(tech)
        return self.getElement(short_name)


class CSTransformerErrorReactionEnum(AREnum):
    """
    Possible kinds of error reaction in case of a hard transformer error.
    """

    # CSTransformerErrorReactionEnum method parity checklist:
    # Spec: AUTOSAR_CP_TPS_SystemTemplate.pdf, Table 7.9, p.773
    # Spec verified: R23-11
    # (no methods)

    # The application is responsible for any error reaction. No autonomous error reaction of RTE and transformer. Tags: atp.EnumerationLiteralIndex=0
    APPLICATION_ONLY = "applicationOnly"

    # RTE and Transformer coordinate an autonomous error reaction on their own. Tags: atp.EnumerationLiteralIndex=1
    AUTONOMOUS = "autonomous"

    def __init__(self):
        super().__init__([CSTransformerErrorReactionEnum.APPLICATION_ONLY, CSTransformerErrorReactionEnum.AUTONOMOUS])


class TransformationISignalProps(Describable, ABC):
    """
    TransformationISignalProps holds all the attributes for the different TransformationTechnologies that are ISignal specific. Tags: vh.latestBindingTime=postBuild
    """

    # TransformationISignalProps method parity checklist:
    # Spec: AUTOSAR_CP_TPS_SystemTemplate.pdf, Table 7.8, p.772
    # Columns: impl / docstring / test / reader / writer   ([—] = no XML element)
    # [x] __init__                     [x] impl  [x] docstring  [x] test  [—] reader  [—] writer
    # [x] getCsErrorReaction           [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] setCsErrorReaction           [x] impl  [x] docstring  [x] test  [x] reader  [—] writer
    # [x] getDataPrototypeTransformationProps [x] impl  [x] docstring  [x] test  [x] reader  [x] writer
    # [x] setDataPrototypeTransformationProps [x] impl  [x] docstring  [x] test  [x] reader  [—] writer
    # [x] getTransformerRef            [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] setTransformerRef            [x] impl  [x] docstring  [x] test  [x] reader  [—] writer

    def __init__(self):
        if type(self) is TransformationISignalProps:
            raise TypeError("TransformationISignalProps is an abstract class.")
        super().__init__()

        # Defines whether the transformer chain of client/server communication coordinates an autonomous error reaction together with the RTE or whether any error reaction is the responsibility of the application.
        self.csErrorReaction: Optional[CSTransformerErrorReactionEnum] = None

        # Fine granular modeling of TransfromationProps on the level of DataPrototypes. Note: This atpSplitable property has no atp.Splitkey due to atpVariation (PropertySetPattern). Stereotypes: atpSplitable
        self.dataPrototypeTransformationProps: List[DataPrototypeTransformationProps] = []

        # Reference to the TransformationTechnology description that contains transformer specific and ISignal independent configuration properties.
        self.transformerRef: Optional[RefType] = None

    def getCsErrorReaction(self) -> Optional[CSTransformerErrorReactionEnum]:
        """
        Defines whether the transformer chain of client/server communication coordinates an autonomous error reaction together with the RTE or whether any error reaction is the responsibility of the application.
        """
        return self.csErrorReaction

    def setCsErrorReaction(self, value: Optional[CSTransformerErrorReactionEnum]) -> "TransformationISignalProps":
        """
        Defines whether the transformer chain of client/server communication coordinates an autonomous error reaction together with the RTE or whether any error reaction is the responsibility of the application.
        A None value is a no-op and does not overwrite an existing csErrorReaction.
        """
        if value is not None:
            self.csErrorReaction = value
        return self

    def getDataPrototypeTransformationProps(self) -> List:
        """
        Fine granular modeling of TransfromationProps on the level of DataPrototypes. Note: This atpSplitable property has no atp.Splitkey due to atpVariation (PropertySetPattern). Stereotypes: atpSplitable
        """
        return self.dataPrototypeTransformationProps

    def setDataPrototypeTransformationProps(self, value: Optional[List]) -> "TransformationISignalProps":
        """
        Fine granular modeling of TransfromationProps on the level of DataPrototypes. Note: This atpSplitable property has no atp.Splitkey due to atpVariation (PropertySetPattern). Stereotypes: atpSplitable
        A None value is a no-op and does not overwrite an existing dataPrototypeTransformationProps.
        """
        if value is not None:
            self.dataPrototypeTransformationProps = value
        return self

    def addDataPrototypeTransformationProps(self, value: Optional["DataPrototypeTransformationProps"]) -> "TransformationISignalProps":
        """
        Fine granular modeling of TransfromationProps on the level of DataPrototypes. Note: This atpSplitable property has no atp.Splitkey due to atpVariation (PropertySetPattern). Stereotypes: atpSplitable
        A None value is a no-op and does not add to dataPrototypeTransformationProps.
        """
        if value is not None:
            self.dataPrototypeTransformationProps.append(value)
        return self

    def getTransformerRef(self) -> Optional[RefType]:
        """
        Reference to the TransformationTechnology description that contains transformer specific and ISignal independent configuration properties.
        """
        return self.transformerRef

    def setTransformerRef(self, value: Optional[RefType]) -> "TransformationISignalProps":
        """
        Reference to the TransformationTechnology description that contains transformer specific and ISignal independent configuration properties.
        A None value is a no-op and does not overwrite an existing transformerRef.
        """
        if value is not None:
            self.transformerRef = value
        return self


class DataPrototypeReference(ARObject, ABC):
    """
    This meta-class provides the ability to reference a DataPrototype.
    """

    # DataPrototypeReference method parity checklist:
    # Spec: AUTOSAR_CP_TPS_SystemTemplate.pdf, Table 7.18, p.787
    # Spec verified: R23-11
    # Columns: impl / docstring / test / reader / writer   ([—] = no XML element)
    # [x] __init__            [x] impl  [x] docstring  [x] test  [—] reader  [—] writer
    # [x] getTagId            [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] setTagId            [x] impl  [x] docstring  [x] test  [x] reader  [—] writer

    def __init__(self):
        if type(self) is DataPrototypeReference:
            raise TypeError("DataPrototypeReference is an abstract class.")
        super().__init__()

        # This attribute represents the ability to specify a tag-id for the serialization of a specific DataPrototype in the context of a (potentially deeply-nested) composite data structure.
        self.tagId: Optional[PositiveInteger] = None

    def getTagId(self) -> Optional[PositiveInteger]:
        """
        This attribute represents the ability to specify a tag-id for the serialization of a specific DataPrototype in the context of a (potentially deeply-nested) composite data structure.
        """
        return self.tagId

    def setTagId(self, value: Optional[PositiveInteger]) -> "DataPrototypeReference":
        """
        This attribute represents the ability to specify a tag-id for the serialization of a specific DataPrototype in the context of a (potentially deeply-nested) composite data structure.
        A None value is a no-op and does not overwrite an existing tagId.
        """
        if value is not None:
            self.tagId = value
        return self


class DataPrototypeInPortInterfaceRef(DataPrototypeReference):
    """
    This class represents a RootDataPrototype that is typed by an ApplicationDataType or Implementation DataType or a DataTypeElement that is aggregated within a composite application data type (record or array).
    """

    # DataPrototypeInPortInterfaceRef method parity checklist:
    # Spec: AUTOSAR_CP_TPS_SystemTemplate.pdf, Table 7.19, p.788
    # Spec verified: R23-11
    # Columns: impl / docstring / test / reader / writer   ([—] = no XML element)
    # [x] __init__                                [x] impl  [x] docstring  [x] test  [—] reader  [—] writer
    # [x] getDataPrototypeInClientServerInterface [x] impl  [x] docstring  [x] test  [x] reader  [x] writer
    # [x] setDataPrototypeInClientServerInterface [x] impl  [x] docstring  [x] test  [x] reader  [—] writer

    def __init__(self):
        super().__init__()

        # This element defines a reference to a DataPrototype in the context of a ClientServerInterface. InstanceRef implemented by: DataPrototypeInClientServerInterfaceInstanceRef
        self.dataPrototypeInClientServerInterface: Optional["DataPrototypeInClientServerInterfaceInstanceRef"] = None

    def getDataPrototypeInClientServerInterface(self) -> Optional["DataPrototypeInClientServerInterfaceInstanceRef"]:
        """
        This element defines a reference to a DataPrototype in the context of a ClientServerInterface. InstanceRef implemented by: DataPrototypeInClientServerInterfaceInstanceRef
        """
        return self.dataPrototypeInClientServerInterface

    def setDataPrototypeInClientServerInterface(self, value: Optional["DataPrototypeInClientServerInterfaceInstanceRef"]) -> "DataPrototypeInPortInterfaceRef":
        """
        This element defines a reference to a DataPrototype in the context of a ClientServerInterface. InstanceRef implemented by: DataPrototypeInClientServerInterfaceInstanceRef
        A None value is a no-op and does not overwrite an existing dataPrototypeInClientServerInterface.
        """
        if value is not None:
            self.dataPrototypeInClientServerInterface = value
        return self


class DataPrototypeInSenderReceiverInterfaceInstanceRef(AtpInstanceRef, DataPrototypeInPortInterfaceRef):
    """
    Instance reference to a DataPrototype in the context of a SenderReceiverInterface.
    """

    # DataPrototypeInSenderReceiverInterfaceInstanceRef method parity checklist:
    # Spec: AUTOSAR_CP_TPS_SystemTemplate.pdf, Table 7.20, p.788
    # Spec verified: R23-11
    # Columns: impl / docstring / test / reader / writer   ([—] = no XML element)
    # [x] __init__                       [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] getBaseRef                     [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] setBaseRef                     [x] impl  [x] docstring  [x] test  [x] reader  [—] writer
    # [x] getContextDataPrototypeInSrRefs [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] addContextDataPrototypeInSrRefs [x] impl  [x] docstring  [x] test  [x] reader  [—] writer
    # [x] getRootDataPrototypeInSrRef    [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] setRootDataPrototypeInSrRef    [x] impl  [x] docstring  [x] test  [x] reader  [—] writer
    # [x] getTargetDataPrototypeInSrRef  [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] setTargetDataPrototypeInSrRef  [x] impl  [x] docstring  [x] test  [x] reader  [—] writer

    def __init__(self):
        super().__init__()

        # Stereotypes: atpDerived
        self.baseRef: Optional[RefType] = None

        # This is a context in case there are subelements with explicit types. The reference has to be ordered to properly reflect the nested structure. Tags: xml.sequenceOffset=20
        self.contextDataPrototypeInSrRefs: List[RefType] = []

        # Tags: xml.sequenceOffset=10
        self.rootDataPrototypeInSrRef: Optional[RefType] = None

        # Tags: xml.sequenceOffset=30
        self.targetDataPrototypeInSrRef: Optional[RefType] = None

    def getBaseRef(self) -> Optional[RefType]:
        """
        Stereotypes: atpDerived
        """
        return self.baseRef

    def setBaseRef(self, value: Optional[RefType]) -> "DataPrototypeInSenderReceiverInterfaceInstanceRef":
        """
        Stereotypes: atpDerived
        A None value is a no-op and does not overwrite an existing baseRef.
        """
        if value is not None:
            self.baseRef = value
        return self

    def getContextDataPrototypeInSrRefs(self) -> List[RefType]:
        """
        This is a context in case there are subelements with explicit types. The reference has to be ordered to properly reflect the nested structure. Tags: xml.sequenceOffset=20
        """
        return self.contextDataPrototypeInSrRefs

    def addContextDataPrototypeInSrRefs(self, value: Optional[RefType]) -> "DataPrototypeInSenderReceiverInterfaceInstanceRef":
        """
        This is a context in case there are subelements with explicit types. The reference has to be ordered to properly reflect the nested structure. Tags: xml.sequenceOffset=20
        A None value is a no-op and does not add to contextDataPrototypeInSrRefs.
        """
        if value is not None:
            self.contextDataPrototypeInSrRefs.append(value)
        return self

    def getRootDataPrototypeInSrRef(self) -> Optional[RefType]:
        """
        Tags: xml.sequenceOffset=10
        """
        return self.rootDataPrototypeInSrRef

    def setRootDataPrototypeInSrRef(self, value: Optional[RefType]) -> "DataPrototypeInSenderReceiverInterfaceInstanceRef":
        """
        Tags: xml.sequenceOffset=10
        A None value is a no-op and does not overwrite an existing rootDataPrototypeInSrRef.
        """
        if value is not None:
            self.rootDataPrototypeInSrRef = value
        return self

    def getTargetDataPrototypeInSrRef(self) -> Optional[RefType]:
        """
        Tags: xml.sequenceOffset=30
        """
        return self.targetDataPrototypeInSrRef

    def setTargetDataPrototypeInSrRef(self, value: Optional[RefType]) -> "DataPrototypeInSenderReceiverInterfaceInstanceRef":
        """
        Tags: xml.sequenceOffset=30
        A None value is a no-op and does not overwrite an existing targetDataPrototypeInSrRef.
        """
        if value is not None:
            self.targetDataPrototypeInSrRef = value
        return self


class DataPrototypeInClientServerInterfaceInstanceRef(AtpInstanceRef, DataPrototypeInPortInterfaceRef):
    """
    Instance reference to a DataPrototype in the context of a ClientServerInterface.
    """

    # DataPrototypeInClientServerInterfaceInstanceRef method parity checklist:
    # Spec: AUTOSAR_CP_TPS_SystemTemplate.pdf, Table 7.21, p.788
    # Spec verified: R23-11
    # Columns: impl / docstring / test / reader / writer   ([—] = no XML element)
    # [x] __init__                       [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] getBaseRef                     [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] setBaseRef                     [x] impl  [x] docstring  [x] test  [x] reader  [—] writer
    # [x] getContextDataPrototypeInCsRefs [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] addContextDataPrototypeInCsRefs [x] impl  [x] docstring  [x] test  [x] reader  [—] writer
    # [x] getRootDataPrototypeInCsRef    [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] setRootDataPrototypeInCsRef    [x] impl  [x] docstring  [x] test  [x] reader  [—] writer
    # [x] getTargetDataPrototypeInCsRef  [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] setTargetDataPrototypeInCsRef  [x] impl  [x] docstring  [x] test  [x] reader  [—] writer

    def __init__(self):
        super().__init__()

        # Stereotypes: atpDerived
        self.baseRef: Optional[RefType] = None

        # This is a context in case there are subelements with explicit types. The reference has to be ordered to properly reflect the nested structure. Tags: xml.sequenceOffset=20
        self.contextDataPrototypeInCsRefs: List[RefType] = []

        # Tags: xml.sequenceOffset=10
        self.rootDataPrototypeInCsRef: Optional[RefType] = None

        # Tags: xml.sequenceOffset=30
        self.targetDataPrototypeInCsRef: Optional[RefType] = None

    def getBaseRef(self) -> Optional[RefType]:
        """
        Stereotypes: atpDerived
        """
        return self.baseRef

    def setBaseRef(self, value: Optional[RefType]) -> "DataPrototypeInClientServerInterfaceInstanceRef":
        """
        Stereotypes: atpDerived
        A None value is a no-op and does not overwrite an existing baseRef.
        """
        if value is not None:
            self.baseRef = value
        return self

    def getContextDataPrototypeInCsRefs(self) -> List[RefType]:
        """
        This is a context in case there are subelements with explicit types. The reference has to be ordered to properly reflect the nested structure. Tags: xml.sequenceOffset=20
        """
        return self.contextDataPrototypeInCsRefs

    def addContextDataPrototypeInCsRefs(self, value: Optional[RefType]) -> "DataPrototypeInClientServerInterfaceInstanceRef":
        """
        This is a context in case there are subelements with explicit types. The reference has to be ordered to properly reflect the nested structure. Tags: xml.sequenceOffset=20
        A None value is a no-op and does not add to contextDataPrototypeInCsRefs.
        """
        if value is not None:
            self.contextDataPrototypeInCsRefs.append(value)
        return self

    def getRootDataPrototypeInCsRef(self) -> Optional[RefType]:
        """
        Tags: xml.sequenceOffset=10
        """
        return self.rootDataPrototypeInCsRef

    def setRootDataPrototypeInCsRef(self, value: Optional[RefType]) -> "DataPrototypeInClientServerInterfaceInstanceRef":
        """
        Tags: xml.sequenceOffset=10
        A None value is a no-op and does not overwrite an existing rootDataPrototypeInCsRef.
        """
        if value is not None:
            self.rootDataPrototypeInCsRef = value
        return self

    def getTargetDataPrototypeInCsRef(self) -> Optional[RefType]:
        """
        Tags: xml.sequenceOffset=30
        """
        return self.targetDataPrototypeInCsRef

    def setTargetDataPrototypeInCsRef(self, value: Optional[RefType]) -> "DataPrototypeInClientServerInterfaceInstanceRef":
        """
        Tags: xml.sequenceOffset=30
        A None value is a no-op and does not overwrite an existing targetDataPrototypeInCsRef.
        """
        if value is not None:
            self.targetDataPrototypeInCsRef = value
        return self


class ImplementationDataTypeElementInPortInterfaceRef(DataPrototypeReference):
    """
    This meta-class represents the ability to refer to the internal structure of an AutosarDataPrototype which is typed by an ImplementationDatatype in the context of a PortInterface. In other words, this meta-class shall not be used to model a reference to the AutosarDataPrototype as a target itself, even if the AutosarDataPrototype is typed by an ImplementationDataType and even if that ImplementationDataType represents a composite data type.
    """

    # ImplementationDataTypeElementInPortInterfaceRef method parity checklist:
    # Spec: AUTOSAR_CP_TPS_SystemTemplate.pdf, Table 7.22, p.789
    # Spec verified: R23-11
    # Columns: impl / docstring / test / reader / writer   ([—] = no XML element)
    # [x] __init__                              [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] getContextImplementationDataElementRefs [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] addContextImplementationDataElementRefs [x] impl  [x] docstring  [x] test  [x] reader  [—] writer
    # [x] getRootDataPrototypeRef              [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] setRootDataPrototypeRef              [x] impl  [x] docstring  [x] test  [x] reader  [—] writer
    # [x] getTargetImplementationDataTypeElementRef [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] setTargetImplementationDataTypeElementRef [x] impl  [x] docstring  [x] test  [x] reader  [—] writer

    def __init__(self):
        super().__init__()

        # This is a context in case there are subelements with explicit types. The reference has to be ordered to properly reflect the nested structure. Tags: xml.sequenceOffset=20
        self.contextImplementationDataElementRefs: List[RefType] = []

        # This refers to the AutosarDataPrototype which is typed by the ImplementationDatatype. The targetDataPrototype and all defined contextDataPrototypes can be found within this rootDataPrototype. Tags: xml.sequenceOffset=10
        self.rootDataPrototypeRef: Optional[RefType] = None

        # This is a target ImplementationDataTypeElement in case that the rootDataPrototype is composite and the target is a subElement of the rootDataPrototype. Tags: xml.sequenceOffset=30
        self.targetImplementationDataTypeElementRef: Optional[RefType] = None

    def getContextImplementationDataElementRefs(self) -> List[RefType]:
        """
        This is a context in case there are subelements with explicit types. The reference has to be ordered to properly reflect the nested structure. Tags: xml.sequenceOffset=20
        """
        return self.contextImplementationDataElementRefs

    def addContextImplementationDataElementRefs(self, value: Optional[RefType]) -> "ImplementationDataTypeElementInPortInterfaceRef":
        """
        This is a context in case there are subelements with explicit types. The reference has to be ordered to properly reflect the nested structure. Tags: xml.sequenceOffset=20
        A None value is a no-op and does not add to contextImplementationDataElementRefs.
        """
        if value is not None:
            self.contextImplementationDataElementRefs.append(value)
        return self

    def getRootDataPrototypeRef(self) -> Optional[RefType]:
        """
        This refers to the AutosarDataPrototype which is typed by the ImplementationDatatype. The targetDataPrototype and all defined contextDataPrototypes can be found within this rootDataPrototype. Tags: xml.sequenceOffset=10
        """
        return self.rootDataPrototypeRef

    def setRootDataPrototypeRef(self, value: Optional[RefType]) -> "ImplementationDataTypeElementInPortInterfaceRef":
        """
        This refers to the AutosarDataPrototype which is typed by the ImplementationDatatype. The targetDataPrototype and all defined contextDataPrototypes can be found within this rootDataPrototype. Tags: xml.sequenceOffset=10
        A None value is a no-op and does not overwrite an existing rootDataPrototypeRef.
        """
        if value is not None:
            self.rootDataPrototypeRef = value
        return self

    def getTargetImplementationDataTypeElementRef(self) -> Optional[RefType]:
        """
        This is a target ImplementationDataTypeElement in case that the rootDataPrototype is composite and the target is a subElement of the rootDataPrototype. Tags: xml.sequenceOffset=30
        """
        return self.targetImplementationDataTypeElementRef

    def setTargetImplementationDataTypeElementRef(self, value: Optional[RefType]) -> "ImplementationDataTypeElementInPortInterfaceRef":
        """
        This is a target ImplementationDataTypeElement in case that the rootDataPrototype is composite and the target is a subElement of the rootDataPrototype. Tags: xml.sequenceOffset=30
        A None value is a no-op and does not overwrite an existing targetImplementationDataTypeElementRef.
        """
        if value is not None:
            self.targetImplementationDataTypeElementRef = value
        return self


class DataPrototypeTransformationProps(ARObject):
    """
    DataPrototypeTransformationProps allows to set the attributes for the different Transformation Technologies that are DataPrototype specific.
    """

    # DataPrototypeTransformationProps method parity checklist:
    # Spec: AUTOSAR_CP_TPS_SystemTemplate.pdf, Table 7.17, p.787
    # Spec verified: R23-11
    # Columns: impl / docstring / test / reader / writer   ([—] = no XML element)
    # [x] __init__                          [x] impl  [x] docstring  [x] test  [—] reader  [—] writer
    # [x] getDataPrototypeInPortInterfaceRef [x] impl  [x] docstring  [x] test  [x] reader  [x] writer
    # [x] setDataPrototypeInPortInterfaceRef [x] impl  [x] docstring  [x] test  [x] reader  [—] writer
    # [x] getNetworkRepresentationProps     [x] impl  [x] docstring  [x] test  [x] reader  [x] writer
    # [x] setNetworkRepresentationProps     [x] impl  [x] docstring  [x] test  [x] reader  [—] writer
    # [x] getTransformationProps             [x] impl  [x] docstring  [x] test  [x] reader  [x] writer
    # [x] setTransformationProps             [x] impl  [x] docstring  [x] test  [x] reader  [—] writer

    def __init__(self):
        super().__init__()

        # Reference to a DataPrototype that is transported in the serialized ISignal.
        self.dataPrototypeInPortInterfaceRef: Optional[DataPrototypeInPortInterfaceRef] = None

        # Specification of the actual network representation for the referenced primitive DataPrototype. If a network representation is provided then the baseType shall be used by the Transformer as input for the serialization/deserilaization. Stereotypes: atpSplitable Tags: atp.Splitkey=networkRepresentationProps
        self.networkRepresentationProps: Optional[SwDataDefProps] = None

        # Collection of AutosarDataPrototype related configuration settings for a transformer.
        self.transformationProps: Optional[RefType] = None

    def getDataPrototypeInPortInterfaceRef(self) -> Optional[DataPrototypeInPortInterfaceRef]:
        """
        Reference to a DataPrototype that is transported in the serialized ISignal.
        """
        return self.dataPrototypeInPortInterfaceRef

    def setDataPrototypeInPortInterfaceRef(self, value: Optional[DataPrototypeInPortInterfaceRef]) -> "DataPrototypeTransformationProps":
        """
        Reference to a DataPrototype that is transported in the serialized ISignal.
        A None value is a no-op and does not overwrite an existing dataPrototypeInPortInterfaceRef.
        """
        if value is not None:
            self.dataPrototypeInPortInterfaceRef = value
        return self

    def getNetworkRepresentationProps(self) -> Optional[SwDataDefProps]:
        """
        Specification of the actual network representation for the referenced primitive DataPrototype. If a network representation is provided then the baseType shall be used by the Transformer as input for the serialization/deserilaization. Stereotypes: atpSplitable Tags: atp.Splitkey=networkRepresentationProps
        """
        return self.networkRepresentationProps

    def setNetworkRepresentationProps(self, value: Optional[SwDataDefProps]) -> "DataPrototypeTransformationProps":
        """
        Specification of the actual network representation for the referenced primitive DataPrototype. If a network representation is provided then the baseType shall be used by the Transformer as input for the serialization/deserilaization. Stereotypes: atpSplitable Tags: atp.Splitkey=networkRepresentationProps
        A None value is a no-op and does not overwrite an existing networkRepresentationProps.
        """
        if value is not None:
            self.networkRepresentationProps = value
        return self

    def getTransformationProps(self) -> Optional[RefType]:
        """
        Collection of AutosarDataPrototype related configuration settings for a transformer.
        """
        return self.transformationProps

    def setTransformationProps(self, value: Optional[RefType]) -> "DataPrototypeTransformationProps":
        """
        Collection of AutosarDataPrototype related configuration settings for a transformer.
        A None value is a no-op and does not overwrite an existing transformationProps.
        """
        if value is not None:
            self.transformationProps = value
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


class EndToEndTransformationComSpecProps(TransformationComSpecProps):
    """
    The class EndToEndTransformationIComSpecProps specifies port specific configuration properties for EndToEnd transformer attributes.
    """

    # EndToEndTransformationComSpecProps method parity checklist:
    # Spec: AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf, Table 4.92, p.201
    # Spec verified: R23-11
    # Columns: impl / docstring / test / reader / writer   ([—] = no XML element)
    # [ ] __init__                              [x] impl  [ ] docstring  [ ] test
    # [ ] getClearFromValidToInvalid            [x] impl  [x] docstring  [x] test  [x] reader  [x] writer
    # [ ] setClearFromValidToInvalid            [x] impl  [x] docstring  [x] test  [x] reader  [x] writer
    # [ ] getDisableEndToEndCheck               [x] impl  [x] docstring  [x] test  [x] reader  [x] writer
    # [ ] setDisableEndToEndCheck               [x] impl  [x] docstring  [x] test  [x] reader  [x] writer
    # [ ] getDisableEndToEndStateMachine        [x] impl  [x] docstring  [x] test  [x] reader  [x] writer
    # [ ] setDisableEndToEndStateMachine        [x] impl  [x] docstring  [x] test  [x] reader  [x] writer
    # [ ] getE2eProfileCompatibilityPropsRef    [x] impl  [x] docstring  [x] test  [x] reader  [x] writer
    # [ ] setE2eProfileCompatibilityPropsRef    [x] impl  [x] docstring  [x] test  [x] reader  [x] writer
    # [ ] getMaxDeltaCounter                    [x] impl  [x] docstring  [x] test  [x] reader  [x] writer
    # [ ] setMaxDeltaCounter                    [x] impl  [x] docstring  [x] test  [x] reader  [x] writer
    # [ ] getMaxErrorStateInit                  [x] impl  [x] docstring  [x] test  [x] reader  [x] writer
    # [ ] setMaxErrorStateInit                  [x] impl  [x] docstring  [x] test  [x] reader  [x] writer
    # [ ] getMaxErrorStateInvalid               [x] impl  [x] docstring  [x] test  [x] reader  [x] writer
    # [ ] setMaxErrorStateInvalid               [x] impl  [x] docstring  [x] test  [x] reader  [x] writer
    # [ ] getMaxErrorStateValid                 [x] impl  [x] docstring  [x] test  [x] reader  [x] writer
    # [ ] setMaxErrorStateValid                 [x] impl  [x] docstring  [x] test  [x] reader  [x] writer
    # [ ] getMaxNoNewOrRepeatedData             [x] impl  [x] docstring  [x] test  [x] reader  [x] writer
    # [ ] setMaxNoNewOrRepeatedData             [x] impl  [x] docstring  [x] test  [x] reader  [x] writer
    # [ ] getMinOkStateInit                     [x] impl  [x] docstring  [x] test  [x] reader  [x] writer
    # [ ] setMinOkStateInit                     [x] impl  [x] docstring  [x] test  [x] reader  [x] writer
    # [ ] getMinOkStateInvalid                  [x] impl  [x] docstring  [x] test  [x] reader  [x] writer
    # [ ] setMinOkStateInvalid                  [x] impl  [x] docstring  [x] test  [x] reader  [x] writer
    # [ ] getMinOkStateValid                    [x] impl  [x] docstring  [x] test  [x] reader  [x] writer
    # [ ] setMinOkStateValid                    [x] impl  [x] docstring  [x] test  [x] reader  [x] writer
    # [ ] getSyncCounterInit                    [x] impl  [x] docstring  [x] test  [x] reader  [x] writer
    # [ ] setSyncCounterInit                    [x] impl  [x] docstring  [x] test  [x] reader  [x] writer
    # [ ] getWindowSizeInit                     [x] impl  [x] docstring  [x] test  [x] reader  [x] writer
    # [ ] setWindowSizeInit                     [x] impl  [x] docstring  [x] test  [x] reader  [x] writer
    # [ ] getWindowSizeInvalid                  [x] impl  [x] docstring  [x] test  [x] reader  [x] writer
    # [ ] setWindowSizeInvalid                  [x] impl  [x] docstring  [x] test  [x] reader  [x] writer
    # [ ] getWindowSizeValid                    [x] impl  [x] docstring  [x] test  [x] reader  [x] writer
    # [ ] setWindowSizeValid                    [x] impl  [x] docstring  [x] test  [x] reader  [x] writer

    def __init__(self):
        super().__init__()

        # Clear monitoring window on transition from state Valid to state Invalid.
        self.clearFromValidToInvalid: Optional[Boolean] = None

        # Disables/Enables the E2E check. The E2Eheader is removed from the payload independent from the setting of this attribute.
        self.disableEndToEndCheck: Optional[Boolean] = None

        # Disables the E2EStateMachine (only E2E check functionality is performed)
        self.disableEndToEndStateMachine: Optional[Boolean] = None

        # Reference to additional settings for the E2E state machine.
        self.e2eProfileCompatibilityPropsRef: Optional[RefType] = None

        # Maximum allowed difference between two counter values of two consecutively received valid messages. For example, if the receiver gets data with counter 1 and Max DeltaCounter is 3, then at the next reception the receiver can accept Counters with values 2, 3 or 4.
        self.maxDeltaCounter: Optional[PositiveInteger] = None

        # Maximal number of checks in which ProfileStatus equal to E2E_P_ERROR was determined, within the last Window Size checks, for the state E2E_SM_INIT. The minimum value is 0.
        self.maxErrorStateInit: Optional[PositiveInteger] = None

        # Maximal number of checks in which ProfileStatus equal to E2E_P_ERROR was determined, within the last Window Size checks, for the state E2E_SM_INVALID. The minimum value is 0.
        self.maxErrorStateInvalid: Optional[PositiveInteger] = None

        # Maximal number of checks in which ProfileStatus equal to E2E_P_ERROR was determined, within the last Window Size checks, for the state E2E_SM_VALID. The minimum value is 0.
        self.maxErrorStateValid: Optional[PositiveInteger] = None

        # EndToEndTransformationDescription holds these attributes which are profile specific and have the same value for all E2E transformers.
        self.maxNoNewOrRepeatedData: Optional[PositiveInteger] = None

        # Minimal number of checks in which ProfileStatus equal to E2E_P_OK was determined, within the last WindowSize checks, for the state E2E_SM_INIT. The minimum value is 1.
        self.minOkStateInit: Optional[PositiveInteger] = None

        # Minimal number of checks in which ProfileStatus equal to E2E_P_OK was determined, within the last WindowSize checks, for the state E2E_SM_INVALID. The minimum value is 1.
        self.minOkStateInvalid: Optional[PositiveInteger] = None

        # Minimal number of checks in which ProfileStatus equal to E2E_P_OK was determined, within the last WindowSize checks, for the state E2E_SM_VALID. The minimum value is 1.
        self.minOkStateValid: Optional[PositiveInteger] = None

        # EndToEndTransformationDescription holds these attributes which are profile specific and have the same value for all E2E transformers.
        self.syncCounterInit: Optional[PositiveInteger] = None

        # Size of the monitoring window of state Init for the E2E state machine.
        self.windowSizeInit: Optional[PositiveInteger] = None

        # Size of the monitoring window of state Invalid for the E2E state machine.
        self.windowSizeInvalid: Optional[PositiveInteger] = None

        # Size of the monitoring window of state Valid for the E2E state machine.
        self.windowSizeValid: Optional[PositiveInteger] = None

    def getClearFromValidToInvalid(self) -> Optional[Boolean]:
        """
        Clear monitoring window on transition from state Valid to state Invalid.
        """
        return self.clearFromValidToInvalid

    def setClearFromValidToInvalid(self, value: Optional[Boolean]) -> "EndToEndTransformationComSpecProps":
        """
        Clear monitoring window on transition from state Valid to state Invalid.
        A None value is a no-op and does not overwrite an existing clearFromValidToInvalid.
        """
        if value is not None:
            self.clearFromValidToInvalid = value
        return self

    def getDisableEndToEndCheck(self) -> Optional[Boolean]:
        """
        Disables/Enables the E2E check. The E2Eheader is removed from the payload independent from the setting of this attribute.
        """
        return self.disableEndToEndCheck

    def setDisableEndToEndCheck(self, value: Optional[Boolean]) -> "EndToEndTransformationComSpecProps":
        """
        Disables/Enables the E2E check. The E2Eheader is removed from the payload independent from the setting of this attribute.
        A None value is a no-op and does not overwrite an existing disableEndToEndCheck.
        """
        if value is not None:
            self.disableEndToEndCheck = value
        return self

    def getDisableEndToEndStateMachine(self) -> Optional[Boolean]:
        """
        Disables the E2EStateMachine (only E2E check functionality is performed)
        """
        return self.disableEndToEndStateMachine

    def setDisableEndToEndStateMachine(self, value: Optional[Boolean]) -> "EndToEndTransformationComSpecProps":
        """
        Disables the E2EStateMachine (only E2E check functionality is performed)
        A None value is a no-op and does not overwrite an existing disableEndToEndStateMachine.
        """
        if value is not None:
            self.disableEndToEndStateMachine = value
        return self

    def getE2eProfileCompatibilityPropsRef(self) -> Optional[RefType]:
        """
        Reference to additional settings for the E2E state machine.
        """
        return self.e2eProfileCompatibilityPropsRef

    def setE2eProfileCompatibilityPropsRef(self, value: Optional[RefType]) -> "EndToEndTransformationComSpecProps":
        """
        Reference to additional settings for the E2E state machine.
        A None value is a no-op and does not overwrite an existing e2eProfileCompatibilityPropsRef.
        """
        if value is not None:
            self.e2eProfileCompatibilityPropsRef = value
        return self

    def getMaxDeltaCounter(self) -> Optional[PositiveInteger]:
        """
        Maximum allowed difference between two counter values of two consecutively received valid messages. For example, if the receiver gets data with counter 1 and Max DeltaCounter is 3, then at the next reception the receiver can accept Counters with values 2, 3 or 4.
        """
        return self.maxDeltaCounter

    def setMaxDeltaCounter(self, value: Optional[PositiveInteger]) -> "EndToEndTransformationComSpecProps":
        """
        Maximum allowed difference between two counter values of two consecutively received valid messages. For example, if the receiver gets data with counter 1 and Max DeltaCounter is 3, then at the next reception the receiver can accept Counters with values 2, 3 or 4.
        A None value is a no-op and does not overwrite an existing maxDeltaCounter.
        """
        if value is not None:
            self.maxDeltaCounter = value
        return self

    def getMaxErrorStateInit(self) -> Optional[PositiveInteger]:
        """
        Maximal number of checks in which ProfileStatus equal to E2E_P_ERROR was determined, within the last Window Size checks, for the state E2E_SM_INIT. The minimum value is 0.
        """
        return self.maxErrorStateInit

    def setMaxErrorStateInit(self, value: Optional[PositiveInteger]) -> "EndToEndTransformationComSpecProps":
        """
        Maximal number of checks in which ProfileStatus equal to E2E_P_ERROR was determined, within the last Window Size checks, for the state E2E_SM_INIT. The minimum value is 0.
        A None value is a no-op and does not overwrite an existing maxErrorStateInit.
        """
        if value is not None:
            self.maxErrorStateInit = value
        return self

    def getMaxErrorStateInvalid(self) -> Optional[PositiveInteger]:
        """
        Maximal number of checks in which ProfileStatus equal to E2E_P_ERROR was determined, within the last Window Size checks, for the state E2E_SM_INVALID. The minimum value is 0.
        """
        return self.maxErrorStateInvalid

    def setMaxErrorStateInvalid(self, value: Optional[PositiveInteger]) -> "EndToEndTransformationComSpecProps":
        """
        Maximal number of checks in which ProfileStatus equal to E2E_P_ERROR was determined, within the last Window Size checks, for the state E2E_SM_INVALID. The minimum value is 0.
        A None value is a no-op and does not overwrite an existing maxErrorStateInvalid.
        """
        if value is not None:
            self.maxErrorStateInvalid = value
        return self

    def getMaxErrorStateValid(self) -> Optional[PositiveInteger]:
        """
        Maximal number of checks in which ProfileStatus equal to E2E_P_ERROR was determined, within the last Window Size checks, for the state E2E_SM_VALID. The minimum value is 0.
        """
        return self.maxErrorStateValid

    def setMaxErrorStateValid(self, value: Optional[PositiveInteger]) -> "EndToEndTransformationComSpecProps":
        """
        Maximal number of checks in which ProfileStatus equal to E2E_P_ERROR was determined, within the last Window Size checks, for the state E2E_SM_VALID. The minimum value is 0.
        A None value is a no-op and does not overwrite an existing maxErrorStateValid.
        """
        if value is not None:
            self.maxErrorStateValid = value
        return self

    def getMaxNoNewOrRepeatedData(self) -> Optional[PositiveInteger]:
        """
        EndToEndTransformationDescription holds these attributes which are profile specific and have the same value for all E2E transformers.
        """
        return self.maxNoNewOrRepeatedData

    def setMaxNoNewOrRepeatedData(self, value: Optional[PositiveInteger]) -> "EndToEndTransformationComSpecProps":
        """
        EndToEndTransformationDescription holds these attributes which are profile specific and have the same value for all E2E transformers.
        A None value is a no-op and does not overwrite an existing maxNoNewOrRepeatedData.
        """
        if value is not None:
            self.maxNoNewOrRepeatedData = value
        return self

    def getMinOkStateInit(self) -> Optional[PositiveInteger]:
        """
        Minimal number of checks in which ProfileStatus equal to E2E_P_OK was determined, within the last WindowSize checks, for the state E2E_SM_INIT. The minimum value is 1.
        """
        return self.minOkStateInit

    def setMinOkStateInit(self, value: Optional[PositiveInteger]) -> "EndToEndTransformationComSpecProps":
        """
        Minimal number of checks in which ProfileStatus equal to E2E_P_OK was determined, within the last WindowSize checks, for the state E2E_SM_INIT. The minimum value is 1.
        A None value is a no-op and does not overwrite an existing minOkStateInit.
        """
        if value is not None:
            self.minOkStateInit = value
        return self

    def getMinOkStateInvalid(self) -> Optional[PositiveInteger]:
        """
        Minimal number of checks in which ProfileStatus equal to E2E_P_OK was determined, within the last WindowSize checks, for the state E2E_SM_INVALID. The minimum value is 1.
        """
        return self.minOkStateInvalid

    def setMinOkStateInvalid(self, value: Optional[PositiveInteger]) -> "EndToEndTransformationComSpecProps":
        """
        Minimal number of checks in which ProfileStatus equal to E2E_P_OK was determined, within the last WindowSize checks, for the state E2E_SM_INVALID. The minimum value is 1.
        A None value is a no-op and does not overwrite an existing minOkStateInvalid.
        """
        if value is not None:
            self.minOkStateInvalid = value
        return self

    def getMinOkStateValid(self) -> Optional[PositiveInteger]:
        """
        Minimal number of checks in which ProfileStatus equal to E2E_P_OK was determined, within the last WindowSize checks, for the state E2E_SM_VALID. The minimum value is 1.
        """
        return self.minOkStateValid

    def setMinOkStateValid(self, value: Optional[PositiveInteger]) -> "EndToEndTransformationComSpecProps":
        """
        Minimal number of checks in which ProfileStatus equal to E2E_P_OK was determined, within the last WindowSize checks, for the state E2E_SM_VALID. The minimum value is 1.
        A None value is a no-op and does not overwrite an existing minOkStateValid.
        """
        if value is not None:
            self.minOkStateValid = value
        return self

    def getSyncCounterInit(self) -> Optional[PositiveInteger]:
        """
        EndToEndTransformationDescription holds these attributes which are profile specific and have the same value for all E2E transformers.
        """
        return self.syncCounterInit

    def setSyncCounterInit(self, value: Optional[PositiveInteger]) -> "EndToEndTransformationComSpecProps":
        """
        EndToEndTransformationDescription holds these attributes which are profile specific and have the same value for all E2E transformers.
        A None value is a no-op and does not overwrite an existing syncCounterInit.
        """
        if value is not None:
            self.syncCounterInit = value
        return self

    def getWindowSizeInit(self) -> Optional[PositiveInteger]:
        """
        Size of the monitoring window of state Init for the E2E state machine.
        """
        return self.windowSizeInit

    def setWindowSizeInit(self, value: Optional[PositiveInteger]) -> "EndToEndTransformationComSpecProps":
        """
        Size of the monitoring window of state Init for the E2E state machine.
        A None value is a no-op and does not overwrite an existing windowSizeInit.
        """
        if value is not None:
            self.windowSizeInit = value
        return self

    def getWindowSizeInvalid(self) -> Optional[PositiveInteger]:
        """
        Size of the monitoring window of state Invalid for the E2E state machine.
        """
        return self.windowSizeInvalid

    def setWindowSizeInvalid(self, value: Optional[PositiveInteger]) -> "EndToEndTransformationComSpecProps":
        """
        Size of the monitoring window of state Invalid for the E2E state machine.
        A None value is a no-op and does not overwrite an existing windowSizeInvalid.
        """
        if value is not None:
            self.windowSizeInvalid = value
        return self

    def getWindowSizeValid(self) -> Optional[PositiveInteger]:
        """
        Size of the monitoring window of state Valid for the E2E state machine.
        """
        return self.windowSizeValid

    def setWindowSizeValid(self, value: Optional[PositiveInteger]) -> "EndToEndTransformationComSpecProps":
        """
        Size of the monitoring window of state Valid for the E2E state machine.
        A None value is a no-op and does not overwrite an existing windowSizeValid.
        """
        if value is not None:
            self.windowSizeValid = value
        return self
