"""Tests for PrivacyLevel (R23-11 AUTOSAR_FO_TPS_LogAndTraceExtract, Table 3.4, p.18), DltArgument (R23-11 Table E.20, p.13), DltMessage (R23-11 AUTOSAR_CP_TPS_SystemTemplate, Table F.50, p.12), DltContext (R23-11 AUTOSAR_CP_TPS_SystemTemplate, Table F.48, p.9) and DltApplication (R23-11 AUTOSAR_CP_TPS_SystemTemplate, Table F.47, p.9)."""

import inspect

from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ARPackage import ARElement
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable import Identifiable, MultilanguageReferrable, Referrable
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import Boolean, PositiveInteger, RefType, String
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.VariationPointCapable import VariationPointCapable
from armodel.models.M2.AUTOSARTemplates.LogAndTraceExtract import DltApplication, DltArgument, DltContext, DltMessage, PrivacyLevel
from armodel.models.M2.MSR.DataDictionary.DataDefProperties import SwDataDefProps


class TestPrivacyLevel:
    """Test cases for PrivacyLevel (Table 3.4, p.18)."""

    MEMBERS = [
        "compuMethodRef",
        "privacyLevel",
    ]

    def test_inheritance(self):
        assert issubclass(PrivacyLevel, ARObject)

    def test_class_docstring_note(self):
        expected = (
            "This meta-class defines the Privacy Level for a Log and Trace content.\n"
            "\n"
            "[constr_5340] Range of DltMessage.privacyLevel.privacyLevel: The value of DltMessage.privacyLevel.privacyLevel shall be in the range between 0 and 255.\n"
            "\n"
            "[constr_5341] Range of PrivacyLevel.compuMethod: The CompuMethod that is referenced from PrivacyLevel in the role compuMethod shall have the category TEXTTABLE."
        )
        assert inspect.cleandoc(PrivacyLevel.__doc__) == expected

    def test_initialization_defaults(self):
        privacy_level = PrivacyLevel()
        assert privacy_level.getCompuMethodRef() is None
        assert privacy_level.getPrivacyLevel() is None

    def test_member_order(self):
        privacy_level = PrivacyLevel()
        members = [k for k in vars(privacy_level) if k in set(self.MEMBERS)]
        assert members == self.MEMBERS

    def test_get_set_compu_method_ref(self):
        privacy_level = PrivacyLevel()
        ref = RefType()
        ref.setValue("/LogAndTrace/CompuMethods/PrivacyLevels")
        assert privacy_level == privacy_level.setCompuMethodRef(ref)
        assert privacy_level.getCompuMethodRef() is ref
        assert privacy_level.setCompuMethodRef(None) is privacy_level
        assert privacy_level.getCompuMethodRef() is ref

    def test_get_set_privacy_level(self):
        privacy_level = PrivacyLevel()
        value = PositiveInteger()
        value.setValue("1")
        assert privacy_level == privacy_level.setPrivacyLevel(value)
        assert privacy_level.getPrivacyLevel() is value
        assert privacy_level.setPrivacyLevel(None) is privacy_level
        assert privacy_level.getPrivacyLevel() is value


class TestDltArgument:
    """Test cases for DltArgument (R23-11 Table E.20, p.13)."""

    MEMBERS = [
        "dltArgumentEntries",
        "length",
        "networkRepresentation",
        "optional",
        "predefinedText",
        "variableLength",
    ]

    def _create_argument(self, short_name: str = "dlt_argument") -> DltArgument:
        ar_root = AUTOSAR.getInstance().createARPackage("AUTOSAR")
        return DltArgument(ar_root, short_name)

    def test_inheritance(self):
        assert issubclass(DltArgument, ARObject)
        assert issubclass(DltArgument, Referrable)
        assert issubclass(DltArgument, MultilanguageReferrable)
        assert issubclass(DltArgument, Identifiable)

    def test_class_docstring_note(self):
        expected = (
            "This element defines an Argument in a DltMessage.\n"
            "\n"
            "[constr_5302] Restriction in usage of DltArgument.optional attribute: The optional attribute shall not be set in a DltArgument that represents an array dimension.\n"
            "\n"
            "[constr_5303] Restriction of baseTypeSize of a DltArgument: The baseTypeSize in the networkRepresentation of a DltArgument is restricted to 8, 16, 32, and 64 Bits.\n"
            "\n"
            "[constr_5304] Datatype of an Array: The dltArgumentEntry that is aggregated by a DltArgument that has the length attribute set to a value (represents an Array) shall not define a SwBaseType in the networkRepresentation since the data type of the Array is described by the SwBaseType in the networkRepresentation of the aggregating DltArgument.\n"
            "\n"
            "[constr_5305] CompuMethod in DltArgument.networkRepresentation: The CompuMethod that is used in the networkRepresentation of a DltArgument is limited to category TEXTTABLE.\n"
            "\n"
            "[constr_5363] Allowed usage of attributes for description of payload data types: (length / dltArgumentEntry / SwBaseType of top level DltArgument) Predefined Text = NA/NA/NA; primitive Type = NA/NA/D; String = D/NA/D; 1-dimensional Array = D/NA/D; n-dimensional Array = D/D/D; Struct = NA/D/NA.\n"
            "\n"
            "[constr_5364] Allowed usage of attributes in case of a dltArgumentEntry: (length / dltArgumentEntry / SwBaseType of DltArgumentEntry) Struct member = NA/D/D; Array dimension = D/D/NA.\n"
            "\n"
            "[constr_5098] Allowed SwDataDefProps attributes for DltArgument.networkRepresentation: allowed (D) = baseType, compuMethod, dataConstr, displayFormat, unit; not applicable (N/A) = annotation, displayPresentation, invalidValue, swComparisonVariable, swHostVariable, swTextProps."
        )
        assert inspect.cleandoc(DltArgument.__doc__) == expected

    def test_initialization_defaults(self):
        argument = self._create_argument()
        assert isinstance(argument, ARObject)
        assert isinstance(argument, Referrable)
        assert isinstance(argument, MultilanguageReferrable)
        assert isinstance(argument, Identifiable)
        assert argument.short_name == "dlt_argument"
        assert argument.getDltArgumentEntries() == []
        assert argument.getLength() is None
        assert argument.getNetworkRepresentation() is None
        assert argument.getOptional() is None
        assert argument.getPredefinedText() is None
        assert argument.getVariableLength() is None

    def test_member_order(self):
        argument = self._create_argument()
        members = [k for k in vars(argument) if k in set(self.MEMBERS)]
        assert members == self.MEMBERS

    def test_create_dlt_argument_entry(self):
        argument = self._create_argument()
        entry = argument.createDltArgumentEntry("entry1")
        assert isinstance(entry, DltArgument)
        assert entry.short_name == "entry1"
        assert entry.parent == argument
        assert argument.getDltArgumentEntries() == [entry]
        entry2 = argument.createDltArgumentEntry("entry1")
        assert entry2 is entry
        assert len(argument.getDltArgumentEntries()) == 1
        entry3 = argument.createDltArgumentEntry("entry2")
        assert entry3 is not entry
        assert entry3.short_name == "entry2"
        assert len(argument.getDltArgumentEntries()) == 2
        sub = entry.createDltArgumentEntry("sub_entry")
        assert sub.parent == entry
        assert entry.getDltArgumentEntries() == [sub]

    def test_get_set_length(self):
        argument = self._create_argument()
        value = PositiveInteger()
        value.setValue("8")
        assert argument == argument.setLength(value)
        assert argument.getLength() is value
        assert argument.getLength().getValue() == 8
        assert argument.setLength(None) is argument
        assert argument.getLength() is value

    def test_get_set_network_representation(self):
        argument = self._create_argument()
        props = SwDataDefProps()
        assert argument == argument.setNetworkRepresentation(props)
        assert argument.getNetworkRepresentation() is props
        assert argument.setNetworkRepresentation(None) is argument
        assert argument.getNetworkRepresentation() is props

    def test_get_set_optional(self):
        argument = self._create_argument()
        value = Boolean()
        value.setValue("true")
        assert argument == argument.setOptional(value)
        assert argument.getOptional() is value
        assert argument.getOptional().getValue() is True
        assert argument.setOptional(None) is argument
        assert argument.getOptional() is value

    def test_get_set_predefined_text(self):
        argument = self._create_argument()
        value = Boolean()
        value.setValue("true")
        assert argument == argument.setPredefinedText(value)
        assert argument.getPredefinedText() is value
        assert argument.getPredefinedText().getValue() is True
        assert argument.setPredefinedText(None) is argument
        assert argument.getPredefinedText() is value

    def test_get_set_variable_length(self):
        argument = self._create_argument()
        value = Boolean()
        value.setValue("false")
        assert argument == argument.setVariableLength(value)
        assert argument.getVariableLength() is value
        assert argument.getVariableLength().getValue() is False
        assert argument.setVariableLength(None) is argument
        assert argument.getVariableLength() is value


class TestDltMessage:
    """Test cases for DltMessage (R23-11 AUTOSAR_CP_TPS_SystemTemplate, Table F.50, p.12)."""

    MEMBERS = [
        "dltArguments",
        "messageId",
        "messageLineNumber",
        "messageSourceFile",
        "messageTypeInfo",
        "privacyLevel",
    ]

    def _create_message(self, short_name: str = "dlt_message") -> DltMessage:
        ar_root = AUTOSAR.getInstance().createARPackage("AUTOSAR")
        return DltMessage(ar_root, short_name)

    def test_inheritance(self):
        assert issubclass(DltMessage, ARObject)
        assert issubclass(DltMessage, Referrable)
        assert issubclass(DltMessage, MultilanguageReferrable)
        assert issubclass(DltMessage, Identifiable)
        assert issubclass(DltMessage, VariationPointCapable)

    def test_class_docstring_note(self):
        expected = (
            "This element defines a DltMessage.\n"
            "\n"
            "[constr_5301] Existence of DltMessage.messageId: For each DltMessage, the attribute messageId shall exist when the Log And Trace Extract is created."
        )
        assert inspect.cleandoc(DltMessage.__doc__) == expected

    def test_initialization_defaults(self):
        message = self._create_message()
        assert isinstance(message, ARObject)
        assert isinstance(message, Referrable)
        assert isinstance(message, MultilanguageReferrable)
        assert isinstance(message, Identifiable)
        assert isinstance(message, VariationPointCapable)
        assert message.short_name == "dlt_message"
        assert message.getDltArguments() == []
        assert message.getMessageId() is None
        assert message.getMessageLineNumber() is None
        assert message.getMessageSourceFile() is None
        assert message.getMessageTypeInfo() is None
        assert message.getPrivacyLevel() is None

    def test_member_order(self):
        message = self._create_message()
        members = [k for k in vars(message) if k in set(self.MEMBERS)]
        assert members == self.MEMBERS

    def test_create_dlt_argument(self):
        message = self._create_message()
        argument = message.createDltArgument("arg1")
        assert isinstance(argument, DltArgument)
        assert argument.short_name == "arg1"
        assert argument.parent == message
        assert message.getDltArguments() == [argument]
        argument2 = message.createDltArgument("arg1")
        assert argument2 is argument
        assert len(message.getDltArguments()) == 1
        argument3 = message.createDltArgument("arg2")
        assert argument3 is not argument
        assert argument3.short_name == "arg2"
        assert len(message.getDltArguments()) == 2

    def test_get_set_message_id(self):
        message = self._create_message()
        value = PositiveInteger()
        value.setValue("42")
        assert message == message.setMessageId(value)
        assert message.getMessageId() is value
        assert message.getMessageId().getValue() == 42
        assert message.setMessageId(None) is message
        assert message.getMessageId() is value

    def test_get_set_message_line_number(self):
        message = self._create_message()
        value = PositiveInteger()
        value.setValue("17")
        assert message == message.setMessageLineNumber(value)
        assert message.getMessageLineNumber() is value
        assert message.getMessageLineNumber().getValue() == 17
        assert message.setMessageLineNumber(None) is message
        assert message.getMessageLineNumber() is value

    def test_get_set_message_source_file(self):
        message = self._create_message()
        value = String()
        value.setValue("logger.c")
        assert message == message.setMessageSourceFile(value)
        assert message.getMessageSourceFile() is value
        assert message.getMessageSourceFile().getValue() == "logger.c"
        assert message.setMessageSourceFile(None) is message
        assert message.getMessageSourceFile() is value

    def test_get_set_message_type_info(self):
        message = self._create_message()
        value = String()
        value.setValue("DLT_LOG_INFO")
        assert message == message.setMessageTypeInfo(value)
        assert message.getMessageTypeInfo() is value
        assert message.getMessageTypeInfo().getValue() == "DLT_LOG_INFO"
        assert message.setMessageTypeInfo(None) is message
        assert message.getMessageTypeInfo() is value

    def test_get_set_privacy_level(self):
        message = self._create_message()
        value = PrivacyLevel()
        assert message == message.setPrivacyLevel(value)
        assert message.getPrivacyLevel() is value
        assert message.setPrivacyLevel(None) is message
        assert message.getPrivacyLevel() is value


class TestDltContext:
    """Test cases for DltContext (R23-11 AUTOSAR_CP_TPS_SystemTemplate, Table F.48, p.9)."""

    MEMBERS = [
        "contextDescription",
        "contextId",
        "dltMessageRefs",
    ]

    def _create_context(self, short_name: str = "dlt_context") -> DltContext:
        ar_root = AUTOSAR.getInstance().createARPackage("AUTOSAR")
        return DltContext(ar_root, short_name)

    def test_inheritance(self):
        assert issubclass(DltContext, ARObject)
        assert issubclass(DltContext, Referrable)
        assert issubclass(DltContext, MultilanguageReferrable)
        assert issubclass(DltContext, Identifiable)
        assert issubclass(DltContext, ARElement)

    def test_class_docstring_note(self):
        expected = (
            "This meta-class represents the Context that groups Log and Trace Messages that are generated by an application. Tags: atp.recommendedPackage=DltContexts\n"
            "\n"
            "[constr_5298] Existence of DltContext.contextId: For each DltContext, the attribute contextId shall exist when the Log And Trace Extract is created.\n"
            "\n"
            "[constr_5299] Existence of DltContext.contextDescription: For each DltContext, the attribute contextDescription shall exist when the Log And Trace Extract is created.\n"
            "\n"
            "[constr_5300] Existence of DltContext.dltMessage: Each DltContext shall reference at least one DltMessage in the role dltMessage when the Log And Trace Extract is created."
        )
        assert inspect.cleandoc(DltContext.__doc__) == expected

    def test_initialization_defaults(self):
        context = self._create_context()
        assert isinstance(context, ARObject)
        assert isinstance(context, Referrable)
        assert isinstance(context, MultilanguageReferrable)
        assert isinstance(context, Identifiable)
        assert isinstance(context, ARElement)
        assert context.short_name == "dlt_context"
        assert context.getContextDescription() is None
        assert context.getContextId() is None
        assert context.getDltMessageRefs() == []

    def test_member_order(self):
        context = self._create_context()
        members = [k for k in vars(context) if k in set(self.MEMBERS)]
        assert members == self.MEMBERS

    def test_get_set_context_description(self):
        context = self._create_context()
        value = String()
        value.setValue("Context for the diagnostics application")
        assert context == context.setContextDescription(value)
        assert context.getContextDescription() is value
        assert context.getContextDescription().getValue() == "Context for the diagnostics application"
        assert context.setContextDescription(None) is context
        assert context.getContextDescription() is value

    def test_get_set_context_id(self):
        context = self._create_context()
        value = String()
        value.setValue("CTX1")
        assert context == context.setContextId(value)
        assert context.getContextId() is value
        assert context.getContextId().getValue() == "CTX1"
        assert context.setContextId(None) is context
        assert context.getContextId() is value

    def test_add_dlt_message_ref(self):
        context = self._create_context()
        ref1 = RefType()
        ref1.setValue("/Package/DltMessageCollection/Message1")
        assert context == context.addDltMessageRef(ref1)
        assert context.getDltMessageRefs() == [ref1]
        ref2 = RefType()
        ref2.setValue("/Package/DltMessageCollection/Message2")
        context.addDltMessageRef(ref2)
        assert context.getDltMessageRefs() == [ref1, ref2]
        assert context.addDltMessageRef(None) is context
        assert context.getDltMessageRefs() == [ref1, ref2]


class TestDltApplication:
    """Test cases for DltApplication (R23-11 AUTOSAR_CP_TPS_SystemTemplate, Table F.47, p.9)."""

    MEMBERS = [
        "applicationDescription",
        "applicationId",
        "contextRefs",
    ]

    def _create_application(self, short_name: str = "dlt_application") -> DltApplication:
        ar_root = AUTOSAR.getInstance().createARPackage("AUTOSAR")
        return DltApplication(ar_root, short_name)

    def test_inheritance(self):
        assert issubclass(DltApplication, ARObject)
        assert issubclass(DltApplication, Referrable)
        assert issubclass(DltApplication, MultilanguageReferrable)
        assert issubclass(DltApplication, Identifiable)
        assert issubclass(DltApplication, VariationPointCapable)

    def test_class_docstring_note(self):
        expected = (
            "This meta-class represents the application from which the log and trace message originates.\n"
            "\n"
            "[constr_5295] Existence of DltApplication.context: Each DltApplication shall reference at least one DltContext in the role context when the Log And Trace Extract is created.\n"
            "\n"
            "[constr_5296] Existence of DltApplication.applicationId: For each DltApplication, the attribute applicationId shall exist when the Log And Trace Extract is created.\n"
            "\n"
            "[constr_5297] Existence of DltApplication.applicationDescription: For each DltApplication, the attribute applicationDescription shall exist when the Log And Trace Extract is created."
        )
        assert inspect.cleandoc(DltApplication.__doc__) == expected

    def test_initialization_defaults(self):
        application = self._create_application()
        assert isinstance(application, ARObject)
        assert isinstance(application, Referrable)
        assert isinstance(application, MultilanguageReferrable)
        assert isinstance(application, Identifiable)
        assert isinstance(application, VariationPointCapable)
        assert application.short_name == "dlt_application"
        assert application.getApplicationDescription() is None
        assert application.getApplicationId() is None
        assert application.getContextRefs() == []

    def test_member_order(self):
        application = self._create_application()
        members = [k for k in vars(application) if k in set(self.MEMBERS)]
        assert members == self.MEMBERS

    def test_get_set_application_description(self):
        application = self._create_application()
        value = String()
        value.setValue("Diagnostic application of the ECU")
        assert application == application.setApplicationDescription(value)
        assert application.getApplicationDescription() is value
        assert application.getApplicationDescription().getValue() == "Diagnostic application of the ECU"
        assert application.setApplicationDescription(None) is application
        assert application.getApplicationDescription() is value

    def test_get_set_application_id(self):
        application = self._create_application()
        value = String()
        value.setValue("APP1")
        assert application == application.setApplicationId(value)
        assert application.getApplicationId() is value
        assert application.getApplicationId().getValue() == "APP1"
        assert application.setApplicationId(None) is application
        assert application.getApplicationId() is value

    def test_add_context_ref(self):
        application = self._create_application()
        ref1 = RefType()
        ref1.setValue("/Package/DltContextCollection/Context1")
        assert application == application.addContextRef(ref1)
        assert application.getContextRefs() == [ref1]
        ref2 = RefType()
        ref2.setValue("/Package/DltContextCollection/Context2")
        application.addContextRef(ref2)
        assert application.getContextRefs() == [ref1, ref2]
        assert application.addContextRef(None) is application
        assert application.getContextRefs() == [ref1, ref2]
