# This module contains the EndToEndProtection package classes for SystemTemplate
# (M2::AUTOSARTemplates::SystemTemplate::EndToEndProtection).

from typing import Optional

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.StereotypeMixins import VariationPointCapable
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import Integer, RefType


class EndToEndProtectionISignalIPdu(ARObject, VariationPointCapable):
    """
    It is possible to protect the inter-ECU data exchange of safety-related ISignalGroups at the level of COM IPdus using protection mechanisms provided by E2E Library. For each ISignalGroup to be protected, a separate EndToEndProtectionISignalIPdu element shall be created within the EndToEndProtectionSet. The EndToEndProtectionISignalIPdu element refers to the ISignalGroup that is to be protected and to the ISignalIPdu that transmits the protected ISignalGroup. The information how the referenced ISignalGroup shall be protected (through which E2E Profile and with which E2E settings) is defined in the EndToEnd Description element.

    [constr_9207] Existence of EndToEndProtectionISignalIPdu.iSignalIPdu: For each EndToEndProtectionISignalIPdu, the reference to ISignalIPdu in the role iSignalIPdu shall exist at the time when the System Description is complete.

    [constr_9208] Existence of EndToEndProtectionISignalIPdu.iSignalGroup: For each EndToEndProtectionISignalIPdu, the reference to ISignalGroup in the role iSignalGroup shall exist at the time when the System Description is complete.

    [constr_9209] Existence of EndToEndProtectionISignalIPdu.dataOffset: For each EndToEndProtectionISignalIPdu, the attribute dataOffset shall exist at the time when the System Description is complete.
    """

    # EndToEndProtectionISignalIPdu method parity checklist:
    # Spec: AUTOSAR_CP_TPS_SystemTemplate.pdf, Table 6.56, p.385
    # Columns: impl / docstring / test / reader / writer / release   ([—] = no XML element)
    # [x] __init__             [x] impl  [x] docstring  [x] test  [—] reader  [—] writer  R23-11
    # [x] getDataOffset        [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setDataOffset        [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getISignalGroupRef   [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setISignalGroupRef   [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getISignalIPduRef    [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setISignalIPduRef    [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11

    def __init__(self):
        super().__init__()

        # This attribute defines the beginning offset (in bits) of the Array representation of the Signal Group (including CRC, counter and application signal group) in the IPdu. This attribute is mandatory and the dataOffset shall always be defined.
        self.dataOffset: Optional[Integer] = None

        # Reference to the ISignalGroup that is to be protected.
        self.iSignalGroupRef: Optional[RefType] = None

        # Reference to the ISignalIPdu that transmits the protected ISignalGroup.
        self.iSignalIPduRef: Optional[RefType] = None

    def getDataOffset(self) -> Optional[Integer]:
        """This attribute defines the beginning offset (in bits) of the Array representation of the Signal Group (including CRC, counter and application signal group) in the IPdu. This attribute is mandatory and the dataOffset shall always be defined."""
        return self.dataOffset

    def setDataOffset(self, value: Optional[Integer]) -> "EndToEndProtectionISignalIPdu":
        """
        This attribute defines the beginning offset (in bits) of the Array representation of the Signal Group (including CRC, counter and application signal group) in the IPdu. This attribute is mandatory and the dataOffset shall always be defined.
        A None value is a no-op and does not overwrite an existing dataOffset.
        """
        if value is not None:
            self.dataOffset = value
        return self

    def getISignalGroupRef(self) -> Optional[RefType]:
        """Reference to the ISignalGroup that is to be protected."""
        return self.iSignalGroupRef

    def setISignalGroupRef(self, value: Optional[RefType]) -> "EndToEndProtectionISignalIPdu":
        """
        Reference to the ISignalGroup that is to be protected.
        A None value is a no-op and does not overwrite an existing iSignalGroupRef.
        """
        if value is not None:
            self.iSignalGroupRef = value
        return self

    def getISignalIPduRef(self) -> Optional[RefType]:
        """Reference to the ISignalIPdu that transmits the protected ISignalGroup."""
        return self.iSignalIPduRef

    def setISignalIPduRef(self, value: Optional[RefType]) -> "EndToEndProtectionISignalIPdu":
        """
        Reference to the ISignalIPdu that transmits the protected ISignalGroup.
        A None value is a no-op and does not overwrite an existing iSignalIPduRef.
        """
        if value is not None:
            self.iSignalIPduRef = value
        return self
