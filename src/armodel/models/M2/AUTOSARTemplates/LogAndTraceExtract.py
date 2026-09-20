from typing import List, Optional

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ARPackage import ARElement
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable import Identifiable
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import Boolean, PositiveInteger, RefType, String
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.VariationPointCapable import VariationPointCapable
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


class DltMessage(Identifiable, VariationPointCapable):
    """
    This element defines a DltMessage.

    [constr_5301] Existence of DltMessage.messageId: For each DltMessage, the attribute messageId shall exist when the Log And Trace Extract is created.
    """

    # DltMessage method parity checklist:
    # Spec: AUTOSAR_CP_TPS_SystemTemplate.pdf, Table F.50, p.12 (R23-11)
    # Columns: impl / docstring / test / reader / writer / release   ([—] = no XML element)
    # [x] __init__               [x] impl  [x] docstring  [x] test  [—] reader  [—] writer  R23-11
    # [x] createDltArgument      [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getDltArguments        [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] getMessageId           [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setMessageId           [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getMessageLineNumber   [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setMessageLineNumber   [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getMessageSourceFile   [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setMessageSourceFile   [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getMessageTypeInfo     [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setMessageTypeInfo     [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getPrivacyLevel        [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setPrivacyLevel        [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11

    def __init__(self, parent: ARObject, short_name: str):
        super().__init__(parent, short_name)

        # Ordered collection of DltArguments in the DltMessage.
        self.dltArguments: List[DltArgument] = []

        # This attribute defines the unique Id for the DltMessage.
        self.messageId: Optional[PositiveInteger] = None

        # This attribute describes the position in the source file in which this log message was called.
        self.messageLineNumber: Optional[PositiveInteger] = None

        # This attribute describes the source file in which this log message was called.
        self.messageSourceFile: Optional[String] = None

        # This attribute describes the message Type
        self.messageTypeInfo: Optional[String] = None

        # The Privacy Level helps to identify the Log and Trace content towards the degree of privacy to it.
        self.privacyLevel: Optional[PrivacyLevel] = None

    def createDltArgument(self, short_name: str) -> "DltArgument":
        """
        Ordered collection of DltArguments in the DltMessage.
        """
        if not self.IsElementExists(short_name, DltArgument):
            argument = DltArgument(self, short_name)
            self.addElement(argument)
            self.dltArguments.append(argument)
        return self.getElement(short_name, DltArgument)

    def getDltArguments(self) -> List["DltArgument"]:
        """
        Ordered collection of DltArguments in the DltMessage.
        """
        return self.dltArguments

    def getMessageId(self) -> Optional[PositiveInteger]:
        """
        This attribute defines the unique Id for the DltMessage.
        """
        return self.messageId

    def setMessageId(self, value: Optional[PositiveInteger]) -> "DltMessage":
        """
        This attribute defines the unique Id for the DltMessage.

        A None value is a no-op and does not overwrite an existing messageId.
        """
        if value is not None:
            self.messageId = value
        return self

    def getMessageLineNumber(self) -> Optional[PositiveInteger]:
        """
        This attribute describes the position in the source file in which this log message was called.
        """
        return self.messageLineNumber

    def setMessageLineNumber(self, value: Optional[PositiveInteger]) -> "DltMessage":
        """
        This attribute describes the position in the source file in which this log message was called.

        A None value is a no-op and does not overwrite an existing messageLineNumber.
        """
        if value is not None:
            self.messageLineNumber = value
        return self

    def getMessageSourceFile(self) -> Optional[String]:
        """
        This attribute describes the source file in which this log message was called.
        """
        return self.messageSourceFile

    def setMessageSourceFile(self, value: Optional[String]) -> "DltMessage":
        """
        This attribute describes the source file in which this log message was called.

        A None value is a no-op and does not overwrite an existing messageSourceFile.
        """
        if value is not None:
            self.messageSourceFile = value
        return self

    def getMessageTypeInfo(self) -> Optional[String]:
        """
        This attribute describes the message Type
        """
        return self.messageTypeInfo

    def setMessageTypeInfo(self, value: Optional[String]) -> "DltMessage":
        """
        This attribute describes the message Type

        A None value is a no-op and does not overwrite an existing messageTypeInfo.
        """
        if value is not None:
            self.messageTypeInfo = value
        return self

    def getPrivacyLevel(self) -> Optional[PrivacyLevel]:
        """
        The Privacy Level helps to identify the Log and Trace content towards the degree of privacy to it.
        """
        return self.privacyLevel

    def setPrivacyLevel(self, value: Optional[PrivacyLevel]) -> "DltMessage":
        """
        The Privacy Level helps to identify the Log and Trace content towards the degree of privacy to it.

        A None value is a no-op and does not overwrite an existing privacyLevel.
        """
        if value is not None:
            self.privacyLevel = value
        return self


class DltContext(ARElement):
    """
    This meta-class represents the Context that groups Log and Trace Messages that are generated by an application. Tags: atp.recommendedPackage=DltContexts

    [constr_5298] Existence of DltContext.contextId: For each DltContext, the attribute contextId shall exist when the Log And Trace Extract is created.

    [constr_5299] Existence of DltContext.contextDescription: For each DltContext, the attribute contextDescription shall exist when the Log And Trace Extract is created.

    [constr_5300] Existence of DltContext.dltMessage: Each DltContext shall reference at least one DltMessage in the role dltMessage when the Log And Trace Extract is created.
    """

    # DltContext method parity checklist:
    # Spec: AUTOSAR_CP_TPS_SystemTemplate.pdf, Table F.48, p.9 (R23-11)
    # Columns: impl / docstring / test / reader / writer / release   ([—] = no XML element)
    # [x] __init__               [x] impl  [x] docstring  [x] test  [—] reader  [—] writer  R23-11
    # [x] getContextDescription  [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setContextDescription  [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getContextId           [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setContextId           [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] addDltMessageRef       [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getDltMessageRefs      [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11

    def __init__(self, parent: ARObject, short_name: str):
        super().__init__(parent, short_name)

        # This attribute can be used to describe the contextId that is used in the log and trace message in more detail.
        self.contextDescription: Optional[String] = None

        # This attribute is used to group log and trace messages produced by an application to distinguish functionality.
        self.contextId: Optional[String] = None

        # Group of Log and Trace Messages assigned to the Dlt Context
        self.dltMessageRefs: List[RefType] = []

    def getContextDescription(self) -> Optional[String]:
        """
        This attribute can be used to describe the contextId that is used in the log and trace message in more detail.
        """
        return self.contextDescription

    def setContextDescription(self, value: Optional[String]) -> "DltContext":
        """
        This attribute can be used to describe the contextId that is used in the log and trace message in more detail.

        A None value is a no-op and does not overwrite an existing contextDescription.
        """
        if value is not None:
            self.contextDescription = value
        return self

    def getContextId(self) -> Optional[String]:
        """
        This attribute is used to group log and trace messages produced by an application to distinguish functionality.
        """
        return self.contextId

    def setContextId(self, value: Optional[String]) -> "DltContext":
        """
        This attribute is used to group log and trace messages produced by an application to distinguish functionality.

        A None value is a no-op and does not overwrite an existing contextId.
        """
        if value is not None:
            self.contextId = value
        return self

    def addDltMessageRef(self, value: Optional[RefType]) -> "DltContext":
        """
        Group of Log and Trace Messages assigned to the Dlt Context

        A None value is a no-op and does not append to dltMessageRefs.
        """
        if value is not None:
            self.dltMessageRefs.append(value)
        return self

    def getDltMessageRefs(self) -> List[RefType]:
        """
        Group of Log and Trace Messages assigned to the Dlt Context
        """
        return self.dltMessageRefs


class DltApplication(Identifiable, VariationPointCapable):
    """
    This meta-class represents the application from which the log and trace message originates.

    [constr_5295] Existence of DltApplication.context: Each DltApplication shall reference at least one DltContext in the role context when the Log And Trace Extract is created.

    [constr_5296] Existence of DltApplication.applicationId: For each DltApplication, the attribute applicationId shall exist when the Log And Trace Extract is created.

    [constr_5297] Existence of DltApplication.applicationDescription: For each DltApplication, the attribute applicationDescription shall exist when the Log And Trace Extract is created.
    """

    # DltApplication method parity checklist:
    # Spec: AUTOSAR_CP_TPS_SystemTemplate.pdf, Table F.47, p.9 (R23-11)
    # Columns: impl / docstring / test / reader / writer / release   ([—] = no XML element)
    # [x] __init__                       [x] impl  [x] docstring  [x] test  [—] reader  [—] writer  R23-11
    # [x] getApplicationDescription      [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setApplicationDescription      [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getApplicationId               [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setApplicationId               [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] addContextRef                  [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getContextRefs                 [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11

    def __init__(self, parent: ARObject, short_name: str):
        super().__init__(parent, short_name)

        # This attribute can be used to describe the applicationId that is used in the log and trace message in more detail.
        self.applicationDescription: Optional[String] = None

        # This attribute identifies the SW-C/BSW module in the log and trace message.
        self.applicationId: Optional[String] = None

        # Definition of ContextIds for the Application.
        self.contextRefs: List[RefType] = []

    def getApplicationDescription(self) -> Optional[String]:
        """
        This attribute can be used to describe the applicationId that is used in the log and trace message in more detail.
        """
        return self.applicationDescription

    def setApplicationDescription(self, value: Optional[String]) -> "DltApplication":
        """
        This attribute can be used to describe the applicationId that is used in the log and trace message in more detail.

        A None value is a no-op and does not overwrite an existing applicationDescription.
        """
        if value is not None:
            self.applicationDescription = value
        return self

    def getApplicationId(self) -> Optional[String]:
        """
        This attribute identifies the SW-C/BSW module in the log and trace message.
        """
        return self.applicationId

    def setApplicationId(self, value: Optional[String]) -> "DltApplication":
        """
        This attribute identifies the SW-C/BSW module in the log and trace message.

        A None value is a no-op and does not overwrite an existing applicationId.
        """
        if value is not None:
            self.applicationId = value
        return self

    def addContextRef(self, value: Optional[RefType]) -> "DltApplication":
        """
        Definition of ContextIds for the Application.

        A None value is a no-op and does not append to contextRefs.
        """
        if value is not None:
            self.contextRefs.append(value)
        return self

    def getContextRefs(self) -> List[RefType]:
        """
        Definition of ContextIds for the Application.
        """
        return self.contextRefs
