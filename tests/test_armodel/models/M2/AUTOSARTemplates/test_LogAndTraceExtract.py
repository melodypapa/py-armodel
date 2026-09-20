"""Tests for PrivacyLevel (R23-11 AUTOSAR_FO_TPS_LogAndTraceExtract, Table 3.4, p.18)."""

import inspect

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import PositiveInteger, RefType
from armodel.models.M2.AUTOSARTemplates.LogAndTraceExtract import PrivacyLevel


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
