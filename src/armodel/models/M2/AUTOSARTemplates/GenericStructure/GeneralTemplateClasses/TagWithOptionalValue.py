from typing import Optional

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import Integer, String


class TagWithOptionalValue(ARObject):
    """
    A tagged value is a combination of a tag (key) and a value that gives supplementary information that is attached to a model element. Please note that keys without a value are allowed.
    """

    # TagWithOptionalValue method parity checklist:
    # Spec: AUTOSAR_CP_TPS_SystemTemplate.pdf, Table 6.159, p.478
    # Spec verified: R23-11
    # Columns: impl / docstring / test / reader / writer   ([—] = no XML element)
    # [x] __init__              [x] impl  [x] docstring  [x] test  [—] reader  [—] writer
    # [x] getKey                [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] setKey                [x] impl  [x] docstring  [x] test  [x] reader  [—] writer
    # [x] getSequenceOffset     [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] setSequenceOffset     [x] impl  [x] docstring  [x] test  [x] reader  [—] writer
    # [x] getValue              [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] setValue              [x] impl  [x] docstring  [x] test  [x] reader  [—] writer

    def __init__(self):
        super().__init__()

        # Defines a key.
        self.key: Optional[String] = None

        # The sequenceOffset attribute supports the use case where TagWithOptionalValue is aggregated as splitable. If multiple aggregations define the same value of attribute key then the order in which the value collection is merged might be significant. As an example consider the modeling of the $PATH environment variable by means of a meta class TagWithOptionalValue. The sequenceOffset describes the relative position of each contribution in the concatenated value. The contributions are sorted in increasing integer order.
        self.sequenceOffset: Optional[Integer] = None

        # Defines the corresponding value.
        self.value: Optional[String] = None

    def getKey(self) -> Optional[String]:
        """Defines a key."""
        return self.key

    def setKey(self, value: Optional[String]) -> "TagWithOptionalValue":
        """
        Defines a key.
        A None value is a no-op and does not overwrite an existing key.
        """
        if value is not None:
            self.key = value
        return self

    def getSequenceOffset(self) -> Optional[Integer]:
        """The sequenceOffset attribute supports the use case where TagWithOptionalValue is aggregated as splitable. If multiple aggregations define the same value of attribute key then the order in which the value collection is merged might be significant. As an example consider the modeling of the $PATH environment variable by means of a meta class TagWithOptionalValue. The sequenceOffset describes the relative position of each contribution in the concatenated value. The contributions are sorted in increasing integer order."""
        return self.sequenceOffset

    def setSequenceOffset(self, value: Optional[Integer]) -> "TagWithOptionalValue":
        """
        The sequenceOffset attribute supports the use case where TagWithOptionalValue is aggregated as splitable. If multiple aggregations define the same value of attribute key then the order in which the value collection is merged might be significant. As an example consider the modeling of the $PATH environment variable by means of a meta class TagWithOptionalValue. The sequenceOffset describes the relative position of each contribution in the concatenated value. The contributions are sorted in increasing integer order.
        A None value is a no-op and does not overwrite an existing sequenceOffset.
        """
        if value is not None:
            self.sequenceOffset = value
        return self

    def getValue(self) -> Optional[String]:
        """Defines the corresponding value."""
        return self.value

    def setValue(self, value: Optional[String]) -> "TagWithOptionalValue":
        """
        Defines the corresponding value.
        A None value is a no-op and does not overwrite an existing value.
        """
        if value is not None:
            self.value = value
        return self
