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
    This meta-class contains information about end-to-end protection. The set of applicable attributes depends on the actual value of the category attribute of EndToEndProtection.
    """

    # EndToEndDescription method parity checklist:
    # Spec: AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf, Table 4.95, p.206 (R23-11)
    # Columns: impl / docstring / test / reader / writer / release   ([—] = no XML element)
    # [x] __init__                     [x] impl  [x] docstring  [x] test  [—] reader  [—] writer  R23-11
    # [x] getCategory                  [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setCategory                  [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getCounterOffset             [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setCounterOffset             [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getCrcOffset                 [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setCrcOffset                 [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] addDataId                    [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getDataIds                   [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] getDataIdMode                [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setDataIdMode                [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getDataIdNibbleOffset        [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setDataIdNibbleOffset        [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getDataLength                [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setDataLength                [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getMaxDeltaCounterInit       [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setMaxDeltaCounterInit       [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getMaxNoNewOrRepeatedData    [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setMaxNoNewOrRepeatedData    [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getSyncCounterInit           [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setSyncCounterInit           [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11

    def __init__(self):
        super().__init__()

        # The category represents the identification of the concrete E2E profile. The applicable values are specified in a semantic constraint and determine the applicable attributes of EndToEndDescription.
        self.category: Optional[NameToken] = None

        # Bit offset of Counter from the beginning of the Array representation of the Signal Group/VariableDataPrototype (MSB order, bit numbering: bit 0 is the least important). The offset shall be a multiplicity of 4 and it should be 8 whenever possible. For example, offset 8 means that the counter will take the low nibble of the byte 1, i.e. bits 8 .. 11. If counterOffset is not present the value is defined by the selected profile.
        self.counterOffset: Optional[PositiveInteger] = None

        # Bit offset of CRC from the beginning of the Array representation of the Signal Group/VariableDataPrototype (MSB order, bit numbering: bit 0 is the least important). The offset shall be a multiplicity of 8 and it should be 0 whenever possible. For example, offset 8 means that the CRC will take the byte 1, i.e. bits 8..15. If crcOffset is not present the value is defined by the selected profile.
        self.crcOffset: Optional[PositiveInteger] = None

        # This represents a unique numerical identifier. Note: ID is used for protection against masquerading. The details concerning the maximum number of values (this information is specific for each E2E profile) applicable for this attribute are controlled by a semantic constraint that depends on the category of the EndToEndProtection.
        self.dataIds: List[PositiveInteger] = []

        # There are three inclusion modes how the implicit two-byte Data ID is included in the one-byte CRC: • dataIDMode = 0: Two bytes are included in the CRC (double ID configuration) This is used in variant 1A. • dataIDMode = 1: One of the two bytes byte is included, alternating high and low byte, depending on parity of the counter (alternating ID configuration). For even counter low byte is included; For odd counters the high byte is included. This is used in variant 1B. • dataIDMode = 2: Only low byte is included, high byte is never used. This is applicable if the IDs in a particular system are 8 bits. • dataIdMode = 3: The low byte is included in the implicit CRC calculation, the low nibble of the high byte is transmitted along with the data (i.e. it is explicitly included), the high nibble of the high byte is not used. This is applicable for the IDs up to 12 bits.
        self.dataIdMode: Optional[PositiveInteger] = None

        # Bit offset of the low nibble of the high byte of Data ID. The applicability of this attribute is controlled by [constr_1261].
        self.dataIdNibbleOffset: Optional[PositiveInteger] = None

        # This attribute represents the length of the Array representation of the Signal Group/VariableDataPrototype including CRC and Counter in bits.
        self.dataLength: Optional[PositiveInteger] = None

        # Initial maximum allowed gap between two counter values of two consecutively received valid Data, i.e. how many subsequent lost data is accepted. For example, if the receiver gets Data with counter 1 and MaxDeltaCounterInit is 1, then at the next reception the receiver can accept Counters with values 2 and 3, but not 4. Note that if the receiver does not receive new Data at a consecutive read, then the receiver increments the tolerance by 1.
        self.maxDeltaCounterInit: Optional[PositiveInteger] = None

        # The maximum amount of missing or repeated Data which the receiver does not expect to exceed under normal communication conditions.
        self.maxNoNewOrRepeatedData: Optional[PositiveInteger] = None

        # Number of Data required for validating the consistency of the counter that shall be received with a valid counter (i.e. counter within the allowed lock-in range) after the detection of an unexpected behavior of a received counter.
        self.syncCounterInit: Optional[PositiveInteger] = None

    def getCategory(self) -> Optional[NameToken]:
        """
        The category represents the identification of the concrete E2E profile. The applicable values are specified in a semantic constraint and determine the applicable attributes of EndToEndDescription.
        """
        return self.category

    def setCategory(self, value: Optional[NameToken]) -> "EndToEndDescription":
        """
        The category represents the identification of the concrete E2E profile. The applicable values are specified in a semantic constraint and determine the applicable attributes of EndToEndDescription. A None value is a no-op and does not overwrite an existing category.
        """
        if value is not None:
            self.category = value
        return self

    def getCounterOffset(self) -> Optional[PositiveInteger]:
        """
        Bit offset of Counter from the beginning of the Array representation of the Signal Group/VariableDataPrototype (MSB order, bit numbering: bit 0 is the least important). The offset shall be a multiplicity of 4 and it should be 8 whenever possible. For example, offset 8 means that the counter will take the low nibble of the byte 1, i.e. bits 8 .. 11. If counterOffset is not present the value is defined by the selected profile.
        """
        return self.counterOffset

    def setCounterOffset(self, value: Optional[PositiveInteger]) -> "EndToEndDescription":
        """
        Bit offset of Counter from the beginning of the Array representation of the Signal Group/VariableDataPrototype (MSB order, bit numbering: bit 0 is the least important). The offset shall be a multiplicity of 4 and it should be 8 whenever possible. For example, offset 8 means that the counter will take the low nibble of the byte 1, i.e. bits 8 .. 11. If counterOffset is not present the value is defined by the selected profile. A None value is a no-op and does not overwrite an existing counterOffset.
        """
        if value is not None:
            self.counterOffset = value
        return self

    def getCrcOffset(self) -> Optional[PositiveInteger]:
        """
        Bit offset of CRC from the beginning of the Array representation of the Signal Group/VariableDataPrototype (MSB order, bit numbering: bit 0 is the least important). The offset shall be a multiplicity of 8 and it should be 0 whenever possible. For example, offset 8 means that the CRC will take the byte 1, i.e. bits 8..15. If crcOffset is not present the value is defined by the selected profile.
        """
        return self.crcOffset

    def setCrcOffset(self, value: Optional[PositiveInteger]) -> "EndToEndDescription":
        """
        Bit offset of CRC from the beginning of the Array representation of the Signal Group/VariableDataPrototype (MSB order, bit numbering: bit 0 is the least important). The offset shall be a multiplicity of 8 and it should be 0 whenever possible. For example, offset 8 means that the CRC will take the byte 1, i.e. bits 8..15. If crcOffset is not present the value is defined by the selected profile. A None value is a no-op and does not overwrite an existing crcOffset.
        """
        if value is not None:
            self.crcOffset = value
        return self

    def addDataId(self, value: Optional[PositiveInteger]) -> "EndToEndDescription":
        """
        This represents a unique numerical identifier. Note: ID is used for protection against masquerading. The details concerning the maximum number of values (this information is specific for each E2E profile) applicable for this attribute are controlled by a semantic constraint that depends on the category of the EndToEndProtection. A None value is a no-op and does not append to the dataIds.
        """
        if value is not None:
            self.dataIds.append(value)
        return self

    def getDataIds(self) -> List[PositiveInteger]:
        """
        This represents a unique numerical identifier. Note: ID is used for protection against masquerading. The details concerning the maximum number of values (this information is specific for each E2E profile) applicable for this attribute are controlled by a semantic constraint that depends on the category of the EndToEndProtection.
        """
        return self.dataIds

    def getDataIdMode(self) -> Optional[PositiveInteger]:
        """
        There are three inclusion modes how the implicit two-byte Data ID is included in the one-byte CRC: • dataIDMode = 0: Two bytes are included in the CRC (double ID configuration) This is used in variant 1A. • dataIDMode = 1: One of the two bytes byte is included, alternating high and low byte, depending on parity of the counter (alternating ID configuration). For even counter low byte is included; For odd counters the high byte is included. This is used in variant 1B. • dataIDMode = 2: Only low byte is included, high byte is never used. This is applicable if the IDs in a particular system are 8 bits. • dataIdMode = 3: The low byte is included in the implicit CRC calculation, the low nibble of the high byte is transmitted along with the data (i.e. it is explicitly included), the high nibble of the high byte is not used. This is applicable for the IDs up to 12 bits.
        """
        return self.dataIdMode

    def setDataIdMode(self, value: Optional[PositiveInteger]) -> "EndToEndDescription":
        """
        There are three inclusion modes how the implicit two-byte Data ID is included in the one-byte CRC: • dataIDMode = 0: Two bytes are included in the CRC (double ID configuration) This is used in variant 1A. • dataIDMode = 1: One of the two bytes byte is included, alternating high and low byte, depending on parity of the counter (alternating ID configuration). For even counter low byte is included; For odd counters the high byte is included. This is used in variant 1B. • dataIDMode = 2: Only low byte is included, high byte is never used. This is applicable if the IDs in a particular system are 8 bits. • dataIdMode = 3: The low byte is included in the implicit CRC calculation, the low nibble of the high byte is transmitted along with the data (i.e. it is explicitly included), the high nibble of the high byte is not used. This is applicable for the IDs up to 12 bits. A None value is a no-op and does not overwrite an existing dataIdMode.
        """
        if value is not None:
            self.dataIdMode = value
        return self

    def getDataIdNibbleOffset(self) -> Optional[PositiveInteger]:
        """
        Bit offset of the low nibble of the high byte of Data ID. The applicability of this attribute is controlled by [constr_1261].
        """
        return self.dataIdNibbleOffset

    def setDataIdNibbleOffset(self, value: Optional[PositiveInteger]) -> "EndToEndDescription":
        """
        Bit offset of the low nibble of the high byte of Data ID. The applicability of this attribute is controlled by [constr_1261]. A None value is a no-op and does not overwrite an existing dataIdNibbleOffset.
        """
        if value is not None:
            self.dataIdNibbleOffset = value
        return self

    def getDataLength(self) -> Optional[PositiveInteger]:
        """
        This attribute represents the length of the Array representation of the Signal Group/VariableDataPrototype including CRC and Counter in bits.
        """
        return self.dataLength

    def setDataLength(self, value: Optional[PositiveInteger]) -> "EndToEndDescription":
        """
        This attribute represents the length of the Array representation of the Signal Group/VariableDataPrototype including CRC and Counter in bits. A None value is a no-op and does not overwrite an existing dataLength.
        """
        if value is not None:
            self.dataLength = value
        return self

    def getMaxDeltaCounterInit(self) -> Optional[PositiveInteger]:
        """
        Initial maximum allowed gap between two counter values of two consecutively received valid Data, i.e. how many subsequent lost data is accepted. For example, if the receiver gets Data with counter 1 and MaxDeltaCounterInit is 1, then at the next reception the receiver can accept Counters with values 2 and 3, but not 4. Note that if the receiver does not receive new Data at a consecutive read, then the receiver increments the tolerance by 1.
        """
        return self.maxDeltaCounterInit

    def setMaxDeltaCounterInit(self, value: Optional[PositiveInteger]) -> "EndToEndDescription":
        """
        Initial maximum allowed gap between two counter values of two consecutively received valid Data, i.e. how many subsequent lost data is accepted. For example, if the receiver gets Data with counter 1 and MaxDeltaCounterInit is 1, then at the next reception the receiver can accept Counters with values 2 and 3, but not 4. Note that if the receiver does not receive new Data at a consecutive read, then the receiver increments the tolerance by 1. A None value is a no-op and does not overwrite an existing maxDeltaCounterInit.
        """
        if value is not None:
            self.maxDeltaCounterInit = value
        return self

    def getMaxNoNewOrRepeatedData(self) -> Optional[PositiveInteger]:
        """
        The maximum amount of missing or repeated Data which the receiver does not expect to exceed under normal communication conditions.
        """
        return self.maxNoNewOrRepeatedData

    def setMaxNoNewOrRepeatedData(self, value: Optional[PositiveInteger]) -> "EndToEndDescription":
        """
        The maximum amount of missing or repeated Data which the receiver does not expect to exceed under normal communication conditions. A None value is a no-op and does not overwrite an existing maxNoNewOrRepeatedData.
        """
        if value is not None:
            self.maxNoNewOrRepeatedData = value
        return self

    def getSyncCounterInit(self) -> Optional[PositiveInteger]:
        """
        Number of Data required for validating the consistency of the counter that shall be received with a valid counter (i.e. counter within the allowed lock-in range) after the detection of an unexpected behavior of a received counter.
        """
        return self.syncCounterInit

    def setSyncCounterInit(self, value: Optional[PositiveInteger]) -> "EndToEndDescription":
        """
        Number of Data required for validating the consistency of the counter that shall be received with a valid counter (i.e. counter within the allowed lock-in range) after the detection of an unexpected behavior of a received counter. A None value is a no-op and does not overwrite an existing syncCounterInit.
        """
        if value is not None:
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
