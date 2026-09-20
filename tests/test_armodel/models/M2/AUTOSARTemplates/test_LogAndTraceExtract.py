"""Tests for PrivacyLevel (R23-11 AUTOSAR_FO_TPS_LogAndTraceExtract, Table 3.4, p.18) and DltArgument (R23-11 Table E.20, p.13)."""

import inspect

from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable import Identifiable, MultilanguageReferrable, Referrable
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import Boolean, PositiveInteger, RefType
from armodel.models.M2.AUTOSARTemplates.LogAndTraceExtract import DltArgument, PrivacyLevel
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
