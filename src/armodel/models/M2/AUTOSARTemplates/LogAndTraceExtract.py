from typing import List, Optional

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable import Identifiable
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import Boolean, PositiveInteger, RefType
from armodel.models.M2.MSR.DataDictionary.DataDefProperties import SwDataDefProps


class PrivacyLevel(ARObject):
    """
    This meta-class defines the Privacy Level for a Log and Trace content.

    [constr_5340] Range of DltMessage.privacyLevel.privacyLevel: The value of DltMessage.privacyLevel.privacyLevel shall be in the range between 0 and 255.

    [constr_5341] Range of PrivacyLevel.compuMethod: The CompuMethod that is referenced from PrivacyLevel in the role compuMethod shall have the category TEXTTABLE.
    """

    # PrivacyLevel method parity checklist:
    # Spec: AUTOSAR_FO_TPS_LogAndTraceExtract.pdf, Table 3.4, p.18
    # Columns: impl / docstring / test / reader / writer / release   ([—] = no XML element)
    # [x] __init__           [x] impl  [x] docstring  [x] test  [—] reader  [—] writer  R23-11
    # [x] getCompuMethodRef  [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setCompuMethodRef  [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getPrivacyLevel    [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setPrivacyLevel    [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11

    def __init__(self):
        super().__init__()

        # Reference to CompuMethod of category TEXTTABLE that defines the supported user-defined privacy levels.
        self.compuMethodRef: Optional[RefType] = None

        # The value that represents the privacy level and is transported in the Extension Header.
        self.privacyLevel: Optional[PositiveInteger] = None

    def getCompuMethodRef(self) -> Optional[RefType]:
        """
        Reference to CompuMethod of category TEXTTABLE that defines the supported user-defined privacy levels.
        """
        return self.compuMethodRef

    def setCompuMethodRef(self, value: Optional[RefType]) -> "PrivacyLevel":
        """
        Reference to CompuMethod of category TEXTTABLE that defines the supported user-defined privacy levels.

        A None value is a no-op and does not overwrite an existing compuMethodRef.
        """
        if value is not None:
            self.compuMethodRef = value
        return self

    def getPrivacyLevel(self) -> Optional[PositiveInteger]:
        """
        The value that represents the privacy level and is transported in the Extension Header.
        """
        return self.privacyLevel

    def setPrivacyLevel(self, value: Optional[PositiveInteger]) -> "PrivacyLevel":
        """
        The value that represents the privacy level and is transported in the Extension Header.

        A None value is a no-op and does not overwrite an existing privacyLevel.
        """
        if value is not None:
            self.privacyLevel = value
        return self


class DltArgument(Identifiable):
    """
    This element defines an Argument in a DltMessage.

    [constr_5302] Restriction in usage of DltArgument.optional attribute: The optional attribute shall not be set in a DltArgument that represents an array dimension.

    [constr_5303] Restriction of baseTypeSize of a DltArgument: The baseTypeSize in the networkRepresentation of a DltArgument is restricted to 8, 16, 32, and 64 Bits.

    [constr_5304] Datatype of an Array: The dltArgumentEntry that is aggregated by a DltArgument that has the length attribute set to a value (represents an Array) shall not define a SwBaseType in the networkRepresentation since the data type of the Array is described by the SwBaseType in the networkRepresentation of the aggregating DltArgument.

    [constr_5305] CompuMethod in DltArgument.networkRepresentation: The CompuMethod that is used in the networkRepresentation of a DltArgument is limited to category TEXTTABLE.

    [constr_5363] Allowed usage of attributes for description of payload data types: (length / dltArgumentEntry / SwBaseType of top level DltArgument) Predefined Text = NA/NA/NA; primitive Type = NA/NA/D; String = D/NA/D; 1-dimensional Array = D/NA/D; n-dimensional Array = D/D/D; Struct = NA/D/NA.

    [constr_5364] Allowed usage of attributes in case of a dltArgumentEntry: (length / dltArgumentEntry / SwBaseType of DltArgumentEntry) Struct member = NA/D/D; Array dimension = D/D/NA.

    [constr_5098] Allowed SwDataDefProps attributes for DltArgument.networkRepresentation: allowed (D) = baseType, compuMethod, dataConstr, displayFormat, unit; not applicable (N/A) = annotation, displayPresentation, invalidValue, swComparisonVariable, swHostVariable, swTextProps.
    """

    # DltArgument method parity checklist:
    # Spec: AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf, Table E.20, p.13 (R23-11)
    # Columns: impl / docstring / test / reader / writer / release   ([—] = no XML element)
    # [x] __init__                  [x] impl  [x] docstring  [x] test  [—] reader  [—] writer  R23-11
    # [x] createDltArgumentEntry    [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getDltArgumentEntries     [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] getLength                 [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setLength                 [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getNetworkRepresentation  [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setNetworkRepresentation  [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getOptional               [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setOptional               [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getPredefinedText         [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setPredefinedText         [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getVariableLength         [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setVariableLength         [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11

    def __init__(self, parent: ARObject, short_name: str):
        super().__init__(parent, short_name)

        # This aggregation is used to describe subElements of a Dlt Argument that defines a Structure.
        self.dltArgumentEntries: List[DltArgument] = []

        # Describes the DltArgument length in case of Arrays and Strings in number of BaseTypes.
        self.length: Optional[PositiveInteger] = None

        # Definition of the networkRepresentation of the Dlt Argument.
        self.networkRepresentation: Optional[SwDataDefProps] = None

        # This attribute defines whether the argument is optional or not. If set to true, the argument can be omitted from the payload of a DLT message.
        self.optional: Optional[Boolean] = None

        # This attribute defines whether the DltArgument is a predefinedText (Static Data).
        self.predefinedText: Optional[Boolean] = None

        # This attribute defines whether the length of the Dlt Argument is variable (determined at runtime) or not.
        self.variableLength: Optional[Boolean] = None

    def createDltArgumentEntry(self, short_name: str) -> "DltArgument":
        """
        This aggregation is used to describe subElements of a Dlt Argument that defines a Structure.
        """
        if not self.IsElementExists(short_name, DltArgument):
            entry = DltArgument(self, short_name)
            self.addElement(entry)
            self.dltArgumentEntries.append(entry)
        return self.getElement(short_name, DltArgument)

    def getDltArgumentEntries(self) -> List["DltArgument"]:
        """
        This aggregation is used to describe subElements of a Dlt Argument that defines a Structure.
        """
        return self.dltArgumentEntries

    def getLength(self) -> Optional[PositiveInteger]:
        """
        Describes the DltArgument length in case of Arrays and Strings in number of BaseTypes.
        """
        return self.length

    def setLength(self, value: Optional[PositiveInteger]) -> "DltArgument":
        """
        Describes the DltArgument length in case of Arrays and Strings in number of BaseTypes.

        A None value is a no-op and does not overwrite an existing length.
        """
        if value is not None:
            self.length = value
        return self

    def getNetworkRepresentation(self) -> Optional[SwDataDefProps]:
        """
        Definition of the networkRepresentation of the Dlt Argument.
        """
        return self.networkRepresentation

    def setNetworkRepresentation(self, value: Optional[SwDataDefProps]) -> "DltArgument":
        """
        Definition of the networkRepresentation of the Dlt Argument.

        A None value is a no-op and does not overwrite an existing networkRepresentation.
        """
        if value is not None:
            self.networkRepresentation = value
        return self

    def getOptional(self) -> Optional[Boolean]:
        """
        This attribute defines whether the argument is optional or not. If set to true, the argument can be omitted from the payload of a DLT message.
        """
        return self.optional

    def setOptional(self, value: Optional[Boolean]) -> "DltArgument":
        """
        This attribute defines whether the argument is optional or not. If set to true, the argument can be omitted from the payload of a DLT message.

        A None value is a no-op and does not overwrite an existing optional.
        """
        if value is not None:
            self.optional = value
        return self

    def getPredefinedText(self) -> Optional[Boolean]:
        """
        This attribute defines whether the DltArgument is a predefinedText (Static Data).
        """
        return self.predefinedText

    def setPredefinedText(self, value: Optional[Boolean]) -> "DltArgument":
        """
        This attribute defines whether the DltArgument is a predefinedText (Static Data).

        A None value is a no-op and does not overwrite an existing predefinedText.
        """
        if value is not None:
            self.predefinedText = value
        return self

    def getVariableLength(self) -> Optional[Boolean]:
        """
        This attribute defines whether the length of the Dlt Argument is variable (determined at runtime) or not.
        """
        return self.variableLength

    def setVariableLength(self, value: Optional[Boolean]) -> "DltArgument":
        """
        This attribute defines whether the length of the Dlt Argument is variable (determined at runtime) or not.

        A None value is a no-op and does not overwrite an existing variableLength.
        """
        if value is not None:
            self.variableLength = value
        return self
