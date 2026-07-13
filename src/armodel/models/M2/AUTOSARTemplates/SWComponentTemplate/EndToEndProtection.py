"""
This module contains classes for representing AUTOSAR end-to-end protection
mechanisms in the SWComponentTemplate module. It includes classes for
defining end-to-end protection profiles, variables, and protection sets
used to ensure data integrity in communication systems.
"""

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable import Identifiable, ARElement
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import Integer, NameToken, PositiveInteger, RefType
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.InstanceRefs import VariableDataPrototypeInSystemInstanceRef
from typing import List


class EndToEndDescription(ARObject):
    """
    End-to-end protection profile description defining CRC, counter, and
    data ID configuration for data integrity protection.
    """
    # EndToEndDescription method parity checklist:
    # [ ] __init__                     [x] impl  [ ] docstring  [ ] test
    # [ ] getCategory                  [x] impl  [x] docstring  [ ] test
    # [ ] setCategory                  [x] impl  [x] docstring  [ ] test
    # [ ] getCounterOffset             [x] impl  [x] docstring  [ ] test
    # [ ] setCounterOffset             [x] impl  [x] docstring  [ ] test
    # [ ] getCrcOffset                 [x] impl  [x] docstring  [ ] test
    # [ ] setCrcOffset                 [x] impl  [x] docstring  [ ] test
    # [ ] getDataIds                   [x] impl  [x] docstring  [ ] test
    # [ ] addDataId                    [x] impl  [x] docstring  [ ] test
    # [ ] getDataIdMode                [x] impl  [x] docstring  [ ] test
    # [ ] setDataIdMode                [x] impl  [x] docstring  [ ] test
    # [ ] getDataIdNibbleOffset        [x] impl  [x] docstring  [ ] test
    # [ ] setDataIdNibbleOffset        [x] impl  [x] docstring  [ ] test
    # [ ] getDataLength                [x] impl  [x] docstring  [ ] test
    # [ ] setDataLength                [x] impl  [x] docstring  [ ] test
    # [ ] getMaxDeltaCounterInit       [x] impl  [x] docstring  [ ] test
    # [ ] setMaxDeltaCounterInit       [x] impl  [x] docstring  [ ] test
    # [ ] getMaxNoNewOrRepeatedData    [x] impl  [x] docstring  [ ] test
    # [ ] setMaxNoNewOrRepeatedData    [x] impl  [x] docstring  [ ] test
    # [ ] getSyncCounterInit           [x] impl  [x] docstring  [ ] test
    # [ ] setSyncCounterInit           [x] impl  [x] docstring  [ ] test


    def __init__(self):
        super().__init__()

        self.category: NameToken = None
        self.counterOffset: PositiveInteger = None
        self.crcOffset: PositiveInteger = None
        self.dataIds: List[PositiveInteger] = []
        self.dataIdMode: PositiveInteger = None
        self.dataIdNibbleOffset: PositiveInteger = None
        self.dataLength: PositiveInteger = None
        self.maxDeltaCounterInit: PositiveInteger = None
        self.maxNoNewOrRepeatedData: int = None
        self.syncCounterInit: PositiveInteger = None

    def getCategory(self):
        """
        Gets the category of the end-to-end protection profile.

        Returns:
            NameToken: The category
        """
        return self.category

    def setCategory(self, value):
        """
        Sets the category of the end-to-end protection profile.

        Args:
            value: The category to set

        Returns:
            self for method chaining
        """
        self.category = value
        return self

    def getCounterOffset(self):
        """
        Gets the counter offset.

        Returns:
            PositiveInteger: The counter offset
        """
        return self.counterOffset

    def setCounterOffset(self, value):
        """
        Sets the counter offset.

        Args:
            value: The counter offset to set

        Returns:
            self for method chaining
        """
        self.counterOffset = value
        return self

    def getCrcOffset(self):
        """
        Gets the CRC offset.

        Returns:
            PositiveInteger: The CRC offset
        """
        return self.crcOffset

    def setCrcOffset(self, value):
        """
        Sets the CRC offset.

        Args:
            value: The CRC offset to set

        Returns:
            self for method chaining
        """
        self.crcOffset = value
        return self

    def getDataIds(self) -> List[PositiveInteger]:
        """
        Gets the list of data IDs used for protection against masquerading.

        Returns:
            List[PositiveInteger]: The list of data IDs
        """
        # return sorted(self.dataIds, key = lambda a: a.getValue())
        return self.dataIds

    def addDataId(self, id: PositiveInteger):
        """
        Adds a data ID.

        Args:
            id: The data ID to add

        Returns:
            self for method chaining
        """
        self.dataIds.append(id)
        return self

    def getDataIdMode(self):
        """
        Gets the data ID mode.

        Returns:
            PositiveInteger: The data ID mode
        """
        return self.dataIdMode

    def setDataIdMode(self, value):
        """
        Sets the data ID mode.

        Args:
            value: The data ID mode to set

        Returns:
            self for method chaining
        """
        self.dataIdMode = value
        return self

    def getDataIdNibbleOffset(self):
        """
        Gets the bit offset of the low nibble of the high byte of Data ID.

        Returns:
            PositiveInteger: The data ID nibble offset
        """
        return self.dataIdNibbleOffset

    def setDataIdNibbleOffset(self, value):
        """
        Sets the bit offset of the low nibble of the high byte of Data ID.

        Args:
            value: The data ID nibble offset to set

        Returns:
            self for method chaining
        """
        self.dataIdNibbleOffset = value
        return self

    def getDataLength(self):
        """
        Gets the length of the data including CRC and counter in bits.

        Returns:
            PositiveInteger: The data length
        """
        return self.dataLength

    def setDataLength(self, value):
        """
        Sets the length of the data including CRC and counter in bits.

        Args:
            value: The data length to set

        Returns:
            self for method chaining
        """
        self.dataLength = value
        return self

    def getMaxDeltaCounterInit(self):
        """
        Gets the initial maximum allowed gap between two counter values.

        Returns:
            PositiveInteger: The maximum delta counter
        """
        return self.maxDeltaCounterInit

    def setMaxDeltaCounterInit(self, value):
        """
        Sets the initial maximum allowed gap between two counter values.

        Args:
            value: The maximum delta counter to set

        Returns:
            self for method chaining
        """
        self.maxDeltaCounterInit = value
        return self

    def getMaxNoNewOrRepeatedData(self):
        """
        Gets the maximum amount of missing or repeated data.

        Returns:
            The maximum amount of missing or repeated data
        """
        return self.maxNoNewOrRepeatedData

    def setMaxNoNewOrRepeatedData(self, value):
        """
        Sets the maximum amount of missing or repeated data.

        Args:
            value: The value to set

        Returns:
            self for method chaining
        """
        self.maxNoNewOrRepeatedData = value
        return self

    def getSyncCounterInit(self):
        """
        Gets the number of data required for validating counter consistency.

        Returns:
            PositiveInteger: The sync counter initial value
        """
        return self.syncCounterInit

    def setSyncCounterInit(self, value):
        """
        Sets the number of data required for validating counter consistency.

        Args:
            value: The sync counter initial value to set

        Returns:
            self for method chaining
        """
        self.syncCounterInit = value
        return self


class EndToEndProtectionVariablePrototype(ARObject):
    """
    Associates a VariableDataPrototype with sender and receiver roles
    for end-to-end data protection.
    """
    # EndToEndProtectionVariablePrototype method parity checklist:
    # [ ] __init__                     [x] impl  [ ] docstring  [ ] test
    # [ ] addReceiverIref              [x] impl  [x] docstring  [ ] test
    # [ ] getReceiverIrefs             [x] impl  [x] docstring  [ ] test


    def __init__(self):
        super().__init__()

        self._receiverIRefs: List[VariableDataPrototypeInSystemInstanceRef] = []
        self.senderIRef: VariableDataPrototypeInSystemInstanceRef = None
        self.shortLabel: str = None

    def addReceiverIref(self, iref: VariableDataPrototypeInSystemInstanceRef):
        """
        Adds a receiver instance reference.

        Args:
            iref: The receiver instance reference to add
        """
        self._receiverIRefs.append(iref)

    def getReceiverIrefs(self) -> List[VariableDataPrototypeInSystemInstanceRef]:
        """
        Gets the list of receiver instance references.

        Returns:
            List[VariableDataPrototypeInSystemInstanceRef]: The receiver
                references
        """
        return self._receiverIRefs


class EndToEndProtectionISignalIPdu(ARObject):
    """
    Defines to which ISignalIPdu-ISignalGroup pair an EndToEndProtection
    applies.
    """
    # EndToEndProtectionISignalIPdu method parity checklist:
    # [ ] __init__                     [x] impl  [ ] docstring  [ ] test
    # [ ] getDataOffset                [x] impl  [x] docstring  [ ] test
    # [ ] setDataOffset                [x] impl  [x] docstring  [ ] test
    # [ ] getISignalGroupRef           [x] impl  [x] docstring  [ ] test
    # [ ] setISignalGroupRef           [x] impl  [x] docstring  [ ] test
    # [ ] getISignalIPduRef            [x] impl  [x] docstring  [ ] test
    # [ ] setISignalIPduRef            [x] impl  [x] docstring  [ ] test


    def __init__(self):
        super().__init__()

        self.dataOffset: Integer = None
        self.iSignalGroupRef: RefType = None
        self.iSignalIPduRef: RefType = None

    def getDataOffset(self):
        """
        Gets the data offset.

        Returns:
            Integer: The data offset
        """
        return self.dataOffset

    def setDataOffset(self, value):
        """
        Sets the data offset.

        Args:
            value: The data offset to set

        Returns:
            self for method chaining
        """
        self.dataOffset = value
        return self

    def getISignalGroupRef(self):
        """
        Gets the ISignalGroup reference.

        Returns:
            RefType: The ISignalGroup reference
        """
        return self.iSignalGroupRef

    def setISignalGroupRef(self, value):
        """
        Sets the ISignalGroup reference.

        Args:
            value: The ISignalGroup reference to set

        Returns:
            self for method chaining
        """
        self.iSignalGroupRef = value
        return self

    def getISignalIPduRef(self):
        """
        Gets the ISignalIPdu reference.

        Returns:
            RefType: The ISignalIPdu reference
        """
        return self.iSignalIPduRef

    def setISignalIPduRef(self, value):
        """
        Sets the ISignalIPdu reference.

        Args:
            value: The ISignalIPdu reference to set

        Returns:
            self for method chaining
        """
        self.iSignalIPduRef = value
        return self


class EndToEndProtection(Identifiable):
    """
    This meta-class represents the ability to describe a particular end to
    end protection.
    """
    # EndToEndProtection method parity checklist:
    # [ ] __init__                     [x] impl  [ ] docstring  [ ] test
    # [ ] getEndToEndProfile           [x] impl  [x] docstring  [ ] test
    # [ ] setEndToEndProfile           [x] impl  [x] docstring  [ ] test
    # [ ] getEndToEndProtectionISignalIPdus [x] impl  [x] docstring  [ ] test
    # [ ] addEndToEndProtectionISignalIPdu [x] impl  [x] docstring  [ ] test
    # [ ] getEndToEndProtectionVariablePrototypes [x] impl  [x] docstring  [ ] test
    # [ ] addEndToEndProtectionVariablePrototype [x] impl  [x] docstring  [ ] test


    def __init__(self, parent: ARObject, short_name: str):
        super().__init__(parent, short_name)

        self.endToEndProfile: EndToEndDescription = None
        self.endToEndProtectionISignalIPdus: List[EndToEndProtectionISignalIPdu] = []
        self.endToEndProtectionVariablePrototypes: List[EndToEndProtectionVariablePrototype] = []

    def getEndToEndProfile(self):
        """
        Gets the end-to-end protection profile description.

        Returns:
            EndToEndDescription: The end-to-end profile
        """
        return self.endToEndProfile

    def setEndToEndProfile(self, value):
        """
        Sets the end-to-end protection profile description.

        Args:
            value: The end-to-end profile to set

        Returns:
            self for method chaining
        """
        if value is not None:
            self.endToEndProfile = value
        return self

    def getEndToEndProtectionISignalIPdus(self):
        """
        Gets the list of EndToEndProtectionISignalIPdu definitions.

        Returns:
            List[EndToEndProtectionISignalIPdu]: The ISignalIPdu definitions
        """
        return self.endToEndProtectionISignalIPdus

    def addEndToEndProtectionISignalIPdu(self, value):
        """
        Adds an EndToEndProtectionISignalIPdu definition.

        Args:
            value: The ISignalIPdu definition to add

        Returns:
            self for method chaining
        """
        if value is not None:
            self.endToEndProtectionISignalIPdus.append(value)
        return self

    def getEndToEndProtectionVariablePrototypes(self) -> List[EndToEndProtectionVariablePrototype]:
        """
        Gets the list of end-to-end protection variable prototypes.

        Returns:
            List[EndToEndProtectionVariablePrototype]: The variable prototypes
        """
        return self.endToEndProtectionVariablePrototypes

    def addEndToEndProtectionVariablePrototype(self, value: EndToEndProtectionVariablePrototype):
        """
        Adds an end-to-end protection variable prototype.

        Args:
            value: The variable prototype to add

        Returns:
            self for method chaining
        """
        if value is not None:
            self.endToEndProtectionVariablePrototypes.append(value)
        return self


class EndToEndProtectionSet(ARElement):
    """
    This represents a container for the collection of EndToEndProtection
    information.
    """
    # EndToEndProtectionSet method parity checklist:
    # [ ] __init__                     [x] impl  [ ] docstring  [ ] test
    # [ ] createEndToEndProtection     [x] impl  [x] docstring  [ ] test
    # [ ] getEndToEndProtections       [x] impl  [x] docstring  [ ] test


    def __init__(self, parent: ARObject, short_name: str):
        super().__init__(parent, short_name)

    def createEndToEndProtection(self, short_name: str) -> EndToEndProtection:
        """
        Creates or retrieves an EndToEndProtection element.

        Args:
            short_name: The short name for the protection element

        Returns:
            EndToEndProtection: The created or existing element
        """
        if not self.IsElementExists(short_name):
            protection = EndToEndProtection(self, short_name)
            self.addElement(protection)
        return self.getElement(short_name, EndToEndProtection)

    def getEndToEndProtections(self) -> List[EndToEndProtection]:
        """
        Gets sorted EndToEndProtection elements.

        Returns:
            List[EndToEndProtection]: Sorted list of EndToEndProtection
        """
        return sorted(filter(lambda c: isinstance(c, EndToEndProtection), self.elements), key=lambda e: e.short_name)
