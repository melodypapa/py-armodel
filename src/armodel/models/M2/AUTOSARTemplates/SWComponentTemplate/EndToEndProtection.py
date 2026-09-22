"""
This module contains classes for representing AUTOSAR end-to-end protection
mechanisms in the SWComponentTemplate module. It includes classes for
defining end-to-end protection profiles, variables, and protection sets
used to ensure data integrity in communication systems.
"""

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable import Identifiable
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.VariationPointCapable import VariationPointCapable
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ARPackage import ARElement
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import Identifier, NameToken, PositiveInteger
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.InstanceRefs import VariableDataPrototypeInSystemInstanceRef
from typing import List, Optional, TYPE_CHECKING

if TYPE_CHECKING:
    from armodel.models.M2.AUTOSARTemplates.SystemTemplate.EndToEndProtection import EndToEndProtectionISignalIPdu


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


class EndToEndProtectionVariablePrototype(ARObject, VariationPointCapable):
    """
    It is possible to protect the data exchanged between software components. For this purpose, for each communication to be protected, the user defines a separate EndToEndProtection (specifying a set of protection settings) and refers to a variableDataPrototype in the role of sender and to one or many variableDataPrototypes in the role of receiver. For details, see EndToEnd Library. Caveat: The E2E wrapper approach involves technologies that are not subjected to the AUTOSAR standard and is superseded by the superior E2E transformer approach (which is fully standardized by AUTOSAR). Hence, new projects (without legacy constraints due to carry-over parts) shall use the fully standardized E2E transformer approach.
    """

    # EndToEndProtectionVariablePrototype method parity checklist:
    # Spec: AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf, Table 4.98, p.216 (R23-11)
    # Spec verified: R23-11
    # Columns: impl / docstring / test / reader / writer / release   ([—] = no XML element)
    # [x] __init__          [x] impl  [x] docstring  [x] test  [—] reader  [—] writer  R23-11
    # [x] addReceiverIref   [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getReceiverIrefs  [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] getSenderIref     [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setSenderIref     [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getShortLabel     [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setShortLabel     [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11

    def __init__(self):
        super().__init__()

        # This represents the receiver. Note that 1:n communication is supported for this use case. InstanceRef implemented by: VariableDataPrototypeInSystemInstanceRef
        self.receiverIRefs: List[VariableDataPrototypeInSystemInstanceRef] = []

        # This represents the sender. Can be optional if an ecu extract is provided and the sender is part of the extract. InstanceRef implemented by: VariableDataPrototypeInSystemInstanceRef
        self.senderIRef: Optional[VariableDataPrototypeInSystemInstanceRef] = None

        # This serves as part of the split key in case of more than one EndToEndProtectionVariablePrototype is aggregated in the bound model. Stereotypes: atpIdentityContributor
        self.shortLabel: Optional[Identifier] = None

    def addReceiverIref(self, iref: Optional[VariableDataPrototypeInSystemInstanceRef]) -> "EndToEndProtectionVariablePrototype":
        """
        This represents the receiver. Note that 1:n communication is supported for this use case. InstanceRef implemented by: VariableDataPrototypeInSystemInstanceRef A None value is a no-op and does not append to the receiverIRefs.
        """
        if iref is not None:
            self.receiverIRefs.append(iref)
        return self

    def getReceiverIrefs(self) -> List[VariableDataPrototypeInSystemInstanceRef]:
        """
        This represents the receiver. Note that 1:n communication is supported for this use case. InstanceRef implemented by: VariableDataPrototypeInSystemInstanceRef
        """
        return self.receiverIRefs

    def getSenderIref(self) -> Optional[VariableDataPrototypeInSystemInstanceRef]:
        """
        This represents the sender. Can be optional if an ecu extract is provided and the sender is part of the extract. InstanceRef implemented by: VariableDataPrototypeInSystemInstanceRef
        """
        return self.senderIRef

    def setSenderIref(self, value: Optional[VariableDataPrototypeInSystemInstanceRef]) -> "EndToEndProtectionVariablePrototype":
        """
        This represents the sender. Can be optional if an ecu extract is provided and the sender is part of the extract. InstanceRef implemented by: VariableDataPrototypeInSystemInstanceRef A None value is a no-op and does not overwrite an existing senderIRef.
        """
        if value is not None:
            self.senderIRef = value
        return self

    def getShortLabel(self) -> Optional[Identifier]:
        """
        This serves as part of the split key in case of more than one EndToEndProtectionVariablePrototype is aggregated in the bound model. Stereotypes: atpIdentityContributor
        """
        return self.shortLabel

    def setShortLabel(self, value: Optional[Identifier]) -> "EndToEndProtectionVariablePrototype":
        """
        This serves as part of the split key in case of more than one EndToEndProtectionVariablePrototype is aggregated in the bound model. Stereotypes: atpIdentityContributor A None value is a no-op and does not overwrite an existing shortLabel.
        """
        if value is not None:
            self.shortLabel = value
        return self


class EndToEndProtection(Identifiable, VariationPointCapable):
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
    This represents a container for collection EndToEndProtectionInformation.
    """

    # EndToEndProtectionSet method parity checklist:
    # Spec: AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf, Table 4.96, p.214 (R23-11)
    # Spec verified: R23-11
    # Columns: impl / docstring / test / reader / writer / release   ([—] = no XML element)
    # [x] __init__                     [x] impl  [x] docstring  [x] test  [—] reader  [—] writer  R23-11
    # [x] createEndToEndProtection     [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getEndToEndProtections       [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11

    def __init__(self, parent: ARObject, short_name: str):
        super().__init__(parent, short_name)

        # This is one particular EndToEndProtection.
        self.endToEndProtections: List[EndToEndProtection] = []

    def createEndToEndProtection(self, short_name: str) -> EndToEndProtection:
        """
        This is one particular EndToEndProtection.
        """
        if not self.IsElementExists(short_name, EndToEndProtection):
            protection = EndToEndProtection(self, short_name)
            self.addElement(protection)
            self.endToEndProtections.append(protection)
        return self.getElement(short_name, EndToEndProtection)

    def getEndToEndProtections(self) -> List[EndToEndProtection]:
        """
        This is one particular EndToEndProtection.
        """
        return self.endToEndProtections
