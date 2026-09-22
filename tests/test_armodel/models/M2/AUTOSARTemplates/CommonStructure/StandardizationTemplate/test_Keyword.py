from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.CommonStructure.StandardizationTemplate.Keyword import Keyword, KeywordSet
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable import Identifiable
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import NameToken

# Table 6.2 Note (AUTOSAR_TPS_StandardizationTemplate (R4.3.1), p.91), verbatim per the XSD
# documentation (AUTOSAR_00044.xsd l.52245) including its two-paragraph structure.
KEYWORD_NOTE = (
    "This meta-class represents the ability to predefine keywords which may subsequently be used to construct names "
    "following a given naming convention, e.g. the AUTOSAR naming conventions.\n"
    "\n"
    "Note that such names is not only shortName. It could be symbol, or even longName. Application of keywords is not "
    "limited to particular names."
)

# Keyword.abbrName Note, verbatim per the XSD documentation (l.52258; XSD keeps the
# "to  the" double space).
ABBR_NAME_NOTE = (
    "This attribute specifies an abbreviated name of a keyword. This abbreviation may e.g. be used for constructing "
    "valid shortNames according to  the AUTOSAR naming conventions.\n"
    "\n"
    "Unlike shortName, it may contain any name token. E.g. it may consist of digits only."
)

# Keyword.classification Note, verbatim per the XSD documentation (l.52267).
CLASSIFICATION_NOTE = "This attribute allows to attach classification to the Keyword such as MEAN, ACTION, CONDITION, INDEX, PREPOSITION"


def _doc(doc):
    return "\n".join(line.strip() for line in doc.strip().splitlines())


class TestKeyword:
    def test_initialization(self):
        """Test Keyword default values (Table 6.2)."""
        parent = AUTOSAR.getInstance()
        ar_root = parent.createARPackage("AUTOSAR")
        keyword = Keyword(ar_root, "TestKeyword")

        assert isinstance(keyword, Identifiable)
        assert keyword.getShortName() == "TestKeyword"
        assert keyword.getAbbrName() is None
        assert keyword.getClassifications() == []

    def test_issubclass(self):
        """Base per Table 6.2 is Identifiable (deepest of the Base closure in the model)."""
        assert issubclass(Keyword, Identifiable)

    def test_docstring(self):
        """Class docstring is the Table 6.2 Note verbatim; member Notes on accessors."""
        assert _doc(Keyword.__doc__) == KEYWORD_NOTE
        assert Keyword.__init__.__doc__ is None

        assert _doc(Keyword.getAbbrName.__doc__) == ABBR_NAME_NOTE
        assert _doc(Keyword.setAbbrName.__doc__) == (ABBR_NAME_NOTE + "\nA None value is a no-op and does not overwrite an existing abbrName.")
        assert _doc(Keyword.getClassifications.__doc__) == CLASSIFICATION_NOTE
        assert _doc(Keyword.addClassification.__doc__) == (CLASSIFICATION_NOTE + "\nA None value is a no-op and does not extend the classification list.")

    def test_get_set_abbr_name(self):
        """Test setAbbrName/getAbbrName round-trip and chaining."""
        parent = AUTOSAR.getInstance()
        ar_root = parent.createARPackage("AUTOSAR")
        keyword = Keyword(ar_root, "TestKeyword")
        test_value = NameToken().setValue("Cmft")
        result = keyword.setAbbrName(test_value)
        assert result is keyword
        assert keyword.getAbbrName() == test_value

    def test_set_abbr_name_none(self):
        """Test setAbbrName with None value"""
        parent = AUTOSAR.getInstance()
        ar_root = parent.createARPackage("AUTOSAR")
        keyword = Keyword(ar_root, "TestKeyword")
        keyword.setAbbrName(NameToken().setValue("Cmft"))
        result = keyword.setAbbrName(None)
        assert result is keyword
        assert keyword.getAbbrName().getValue() == "Cmft"

    def test_add_classification(self):
        """Test addClassification aggregation."""
        parent = AUTOSAR.getInstance()
        ar_root = parent.createARPackage("AUTOSAR")
        keyword = Keyword(ar_root, "TestKeyword")
        first = NameToken().setValue("MEAN")
        second = NameToken().setValue("ACTION")
        assert keyword.addClassification(first) is keyword
        assert keyword.addClassification(second) is keyword
        assert keyword.addClassification(None) is keyword
        assert keyword.getClassifications() == [first, second]


class TestKeywordSet:
    def test_initialization(self):
        """Test KeywordSet initialization"""
        parent = AUTOSAR.getInstance()
        ar_root = parent.createARPackage("AUTOSAR")
        keyword_set = KeywordSet(ar_root, "TestKeywordSet")

        assert keyword_set is not None
        assert keyword_set.getShortName() == "TestKeywordSet"
        assert keyword_set.keywords == []

    def test_get_keywords(self):
        """Test getKeywords method"""
        parent = AUTOSAR.getInstance()
        ar_root = parent.createARPackage("AUTOSAR")
        keyword_set = KeywordSet(ar_root, "TestKeywordSet")
        assert keyword_set.getKeywords() == []

    def test_create_keyword(self):
        """Test createKeyword method"""
        parent = AUTOSAR.getInstance()
        ar_root = parent.createARPackage("AUTOSAR")
        keyword_set = KeywordSet(ar_root, "TestKeywordSet")

        keyword = keyword_set.createKeyword("NewKeyword")
        assert keyword is not None
        assert keyword.getShortName() == "NewKeyword"
        assert keyword in keyword_set.getKeywords()
        assert len(keyword_set.getKeywords()) == 1

    def test_create_keyword_duplicate(self):
        """Test createKeyword with duplicate name"""
        parent = AUTOSAR.getInstance()
        ar_root = parent.createARPackage("AUTOSAR")
        keyword_set = KeywordSet(ar_root, "TestKeywordSet")

        keyword1 = keyword_set.createKeyword("TestKeyword")
        keyword2 = keyword_set.createKeyword("TestKeyword")  # Should return same instance

        assert keyword1 is keyword2
        assert len(keyword_set.getKeywords()) == 1

    def test_keyword_properties(self):
        """Test properties of created Keyword through KeywordSet"""
        parent = AUTOSAR.getInstance()
        ar_root = parent.createARPackage("AUTOSAR")
        keyword_set = KeywordSet(ar_root, "TestKeywordSet")

        keyword = keyword_set.createKeyword("TestKeyword")

        # Test keyword properties
        abbr_value = NameToken().setValue("TEST")
        keyword.setAbbrName(abbr_value)

        assert keyword.getAbbrName() == abbr_value
