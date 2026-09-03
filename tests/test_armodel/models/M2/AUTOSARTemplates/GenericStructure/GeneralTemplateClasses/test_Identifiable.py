"""
This module contains comprehensive tests for the Identifiable.py file
in the AUTOSAR GenericStructure module.
"""

from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable import Describable, Identifiable, MultilanguageReferrable, Referrable, ShortNameFragment
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import CategoryString, Identifier, String
from armodel.models.M2.MSR.AsamHdo.AdminData import AdminData
from armodel.models.M2.MSR.Documentation.Annotation import Annotation
from armodel.models.M2.MSR.Documentation.TextModel.BlockElements import DocumentationBlock
from armodel.models.M2.MSR.Documentation.TextModel.MultilanguageData import MultilanguageLongName, MultiLanguageOverviewParagraph


class TestReferrable:
    """
    Test class for Referrable functionality.
    """

    def test_abstract_initialization(self):
        """
        Test that Referrable cannot be instantiated directly (abstract class).
        """
        parent = AUTOSAR.getInstance()
        ar_root = parent.createARPackage("AUTOSAR")
        try:
            _obj = Referrable(ar_root, "TestReferrable")
            assert False, "Referrable should not be instantiable"
        except TypeError:
            pass  # Expected behavior

    def test_get_short_name(self):
        """
        Test getShortName method.
        """
        parent = AUTOSAR.getInstance()
        ar_root = parent.createARPackage("AUTOSAR")

        class ConcreteReferrable(Referrable):
            def __init__(self, parent, short_name):
                super().__init__(parent, short_name)

        obj = ConcreteReferrable(ar_root, "TestName")
        assert obj.getShortName() == "TestName"

    def test_short_name_property(self):
        """
        Test shortName property getter and setter.
        """
        parent = AUTOSAR.getInstance()
        ar_root = parent.createARPackage("AUTOSAR")

        class ConcreteReferrable(Referrable):
            def __init__(self, parent, short_name):
                super().__init__(parent, short_name)

        obj = ConcreteReferrable(ar_root, "TestName")
        assert obj.shortName == "TestName"

        obj.shortName = "NewName"
        assert obj.shortName == "NewName"
        assert obj.getShortName() == "NewName"

    def test_get_parent(self):
        """
        Test getParent method.
        """
        parent = AUTOSAR.getInstance()
        ar_root = parent.createARPackage("AUTOSAR")

        class ConcreteReferrable(Referrable):
            def __init__(self, parent, short_name):
                super().__init__(parent, short_name)

        obj = ConcreteReferrable(ar_root, "TestName")
        assert obj.getParent() == ar_root

    def test_full_name_property(self):
        """
        Test full_name property and getFullName method.
        """
        parent = AUTOSAR.getInstance()
        ar_root = parent.createARPackage("AUTOSAR")

        class ConcreteReferrable(Referrable):
            def __init__(self, parent, short_name):
                super().__init__(parent, short_name)

        obj = ConcreteReferrable(ar_root, "TestName")
        # The full name should be parent's full name + / + short name
        # The parent (ar_root) full name starts with /, so result is /AUTOSAR/TestName
        assert obj.full_name == "/AUTOSAR/TestName"
        assert obj.getFullName() == "/AUTOSAR/TestName"

    def test_get_short_name_fragments_empty_default(self):
        """
        Test that shortNameFragments is empty by default.
        """
        parent = AUTOSAR.getInstance()
        ar_root = parent.createARPackage("AUTOSAR")

        class ConcreteReferrable(Referrable):
            def __init__(self, parent, short_name):
                super().__init__(parent, short_name)

        obj = ConcreteReferrable(ar_root, "TestName")
        assert obj.getShortNameFragments() == []

    def test_add_short_name_fragment(self):
        """
        Test addShortNameFragment appends and returns self for chaining.
        """
        parent = AUTOSAR.getInstance()
        ar_root = parent.createARPackage("AUTOSAR")

        class ConcreteReferrable(Referrable):
            def __init__(self, parent, short_name):
                super().__init__(parent, short_name)

        obj = ConcreteReferrable(ar_root, "TestName")
        fragment = ShortNameFragment()
        result = obj.addShortNameFragment(fragment)
        assert result is obj
        assert obj.getShortNameFragments() == [fragment]

    def test_add_short_name_fragment_none_is_noop(self):
        """
        Test addShortNameFragment with None does not append anything.
        """
        parent = AUTOSAR.getInstance()
        ar_root = parent.createARPackage("AUTOSAR")

        class ConcreteReferrable(Referrable):
            def __init__(self, parent, short_name):
                super().__init__(parent, short_name)

        obj = ConcreteReferrable(ar_root, "TestName")
        result = obj.addShortNameFragment(None)
        assert result is obj
        assert obj.getShortNameFragments() == []


class TestShortNameFragment:
    """
    Test class for ShortNameFragment functionality.
    """

    def test_initialization(self):
        """
        Test that ShortNameFragment initializes with None attributes.
        """
        fragment = ShortNameFragment()
        assert fragment.getRole() is None
        assert fragment.getFragment() is None

    def test_role_setter_getter(self):
        """
        Test setRole and getRole methods.
        """
        fragment = ShortNameFragment()
        assert fragment.setRole("prefix") is fragment
        assert fragment.getRole() == "prefix"

    def test_role_none_is_noop(self):
        """
        Test that setRole(None) does not overwrite an existing role.
        """
        fragment = ShortNameFragment()
        fragment.setRole("prefix")
        fragment.setRole(None)
        assert fragment.getRole() == "prefix"

    def test_fragment_setter_getter(self):
        """
        Test setFragment and getFragment methods.
        """
        fragment = ShortNameFragment()
        value = Identifier().setValue("FragmentText")
        assert fragment.setFragment(value) is fragment
        assert fragment.getFragment() == value

    def test_fragment_none_is_noop(self):
        """
        Test that setFragment(None) does not overwrite an existing fragment.
        """
        fragment = ShortNameFragment()
        value = Identifier().setValue("FragmentText")
        fragment.setFragment(value)
        fragment.setFragment(None)
        assert fragment.getFragment() == value


class TestMultilanguageReferrable:
    """
    Test class for MultilanguageReferrable functionality.
    """

    def test_abstract_initialization(self):
        """
        Test that MultilanguageReferrable cannot be instantiated directly (abstract class).
        """
        parent = AUTOSAR.getInstance()
        ar_root = parent.createARPackage("AUTOSAR")
        try:
            _obj = MultilanguageReferrable(ar_root, "TestMLReferrable")
            assert False, "MultilanguageReferrable should not be instantiable"
        except TypeError:
            pass  # Expected behavior

    def _make_obj(self):
        parent = AUTOSAR.getInstance()
        ar_root = parent.createARPackage("AUTOSAR")

        class ConcreteMultilanguageReferrable(MultilanguageReferrable):
            def __init__(self, parent, short_name):
                super().__init__(parent, short_name)

        return ConcreteMultilanguageReferrable(ar_root, "TestName")

    def test_initialization_default_none(self):
        """
        Test that longName is None by default.
        """
        obj = self._make_obj()
        assert obj.getLongName() is None

    def test_get_set_long_name(self):
        """
        Test getLongName and setLongName round-trip and chaining.
        """
        obj = self._make_obj()

        long_name = MultilanguageLongName()
        result = obj.setLongName(long_name)
        assert result is obj  # method chaining
        assert obj.getLongName() is long_name

    def test_set_long_name_none_is_noop(self):
        """
        Test that setLongName(None) does not overwrite an existing longName.
        """
        obj = self._make_obj()

        long_name = MultilanguageLongName()
        obj.setLongName(long_name)
        assert obj.getLongName() is long_name

        result = obj.setLongName(None)
        assert result is obj  # method chaining with None
        assert obj.getLongName() is long_name  # None is a no-op


class TestIdentifiable:
    """
    Test class for Identifiable functionality (AUTOSAR_FO_TPS_GenericStructureTemplate, Table 4.4).
    """

    class ConcreteIdentifiable(Identifiable):
        def __init__(self, parent, short_name):
            super().__init__(parent, short_name)

    def _make_obj(self):
        parent = AUTOSAR.getInstance()
        ar_root = parent.createARPackage("AUTOSAR")
        return TestIdentifiable.ConcreteIdentifiable(ar_root, "TestName")

    def test_abstract_initialization(self):
        """
        Test that Identifiable cannot be instantiated directly (abstract class).
        """
        parent = AUTOSAR.getInstance()
        ar_root = parent.createARPackage("AUTOSAR")
        try:
            _obj = Identifiable(ar_root, "TestIdentifiable")
            assert False, "Identifiable should not be instantiable"
        except TypeError:
            pass  # Expected behavior

    def test_initialization_defaults(self):
        """
        All spec attributes default to None (or empty list for the annotation aggregation).
        """
        obj = self._make_obj()

        assert obj.getAdminData() is None
        assert obj.getAnnotations() == []
        assert obj.getCategory() is None
        assert obj.getDesc() is None
        assert obj.getIntroduction() is None
        assert obj.getUuid() is None

    def test_get_set_admin_data(self):
        """
        Round-trips adminData; None is a no-op.
        """
        obj = self._make_obj()

        assert obj.getAdminData() is None

        admin_data = AdminData()
        assert obj.setAdminData(admin_data) is obj
        assert obj.getAdminData() is admin_data

        obj.setAdminData(None)
        assert obj.getAdminData() is admin_data

    def test_remove_admin_data(self):
        """
        removeAdminData clears the adminData member.
        """
        obj = self._make_obj()

        admin_data = AdminData()
        obj.setAdminData(admin_data)
        assert obj.getAdminData() is admin_data

        obj.removeAdminData()
        assert obj.getAdminData() is None

    def test_get_set_desc(self):
        """
        Round-trips desc; None is a no-op.
        """
        obj = self._make_obj()

        assert obj.getDesc() is None

        desc = MultiLanguageOverviewParagraph()
        assert obj.setDesc(desc) is obj
        assert obj.getDesc() is desc

        obj.setDesc(None)
        assert obj.getDesc() is desc

    def test_get_set_introduction(self):
        """
        Round-trips introduction; None is a no-op.
        """
        obj = self._make_obj()

        assert obj.getIntroduction() is None

        intro = DocumentationBlock()
        assert obj.setIntroduction(intro) is obj
        assert obj.getIntroduction() is intro

        obj.setIntroduction(None)
        assert obj.getIntroduction() is intro

    def test_add_get_annotations(self):
        """
        addAnnotation appends and returns self for chaining; getAnnotations returns the list.
        """
        obj = self._make_obj()

        assert obj.getAnnotations() == []

        annotation = Annotation()
        assert obj.addAnnotation(annotation) is obj

        annotations = obj.getAnnotations()
        assert len(annotations) == 1
        assert annotations[0] is annotation

    def test_add_annotation_none_is_noop(self):
        """
        addAnnotation(None) does not append anything and still returns self for chaining.
        """
        obj = self._make_obj()

        annotation = Annotation()
        obj.addAnnotation(annotation)
        assert obj.addAnnotation(None) is obj
        assert obj.getAnnotations() == [annotation]

    def test_get_set_category(self):
        """
        Round-trips category as a CategoryString (or a plain string that is converted); None is a no-op.
        """
        obj = self._make_obj()

        assert obj.getCategory() is None

        obj.setCategory("TestCategory")
        category = obj.getCategory()
        assert category is not None
        assert category.getValue() == "TestCategory"

        category_obj = CategoryString().setValue("NewCategory")
        assert obj.setCategory(category_obj) is obj
        assert obj.getCategory() is category_obj

        obj.setCategory(None)
        assert obj.getCategory() is category_obj

    def test_get_set_uuid(self):
        """
        Round-trips uuid (Table 4.4 attribute, owned by Identifiable); None is a no-op.
        """
        obj = self._make_obj()

        assert obj.getUuid() is None

        uuid = String().setValue("DCE:2fac1234-31f8-11b4-a222-08002b34c003")
        assert obj.setUuid(uuid) is obj
        assert obj.getUuid() is uuid

        obj.setUuid(None)
        assert obj.getUuid() is uuid

    def test_element_registry_round_trip(self):
        """
        The element-collection registry owned by Identifiable (framework infra, not a
        Table 4.4 attribute): addElement registers by short name, the lookup helpers
        agree with it, and removeElement drops it again.
        """
        obj = self._make_obj()

        class ConcreteReferrable(Referrable):
            def __init__(self, parent, short_name):
                super().__init__(parent, short_name)

        parent = AUTOSAR.getInstance()
        ar_root = parent.createARPackage("AUTOSAR")
        element = ConcreteReferrable(ar_root, "TestElement")

        assert obj.getTotalElement() == 0
        assert obj.getElements() == []
        assert obj.IsElementExists("TestElement") is False
        assert obj.getElement("TestElement") is None

        obj.addElement(element)
        assert obj.getTotalElement() == 1
        assert obj.getElements() == [element]
        assert obj.IsElementExists("TestElement") is True
        assert obj.getElement("TestElement") is element

        # Adding the same short name + type twice does not duplicate the entry.
        obj.addElement(element)
        assert obj.getTotalElement() == 1

        obj.removeElement("TestElement")
        assert obj.getTotalElement() == 0
        assert obj.getElements() == []

    def test_remove_element_unknown_short_name_raises(self):
        """
        removeElement raises KeyError for a short name that was never registered.
        """
        obj = self._make_obj()

        try:
            obj.removeElement("NonExistent")
            assert False, "removeElement should raise KeyError for an unknown short name"
        except KeyError:
            pass


class TestDescribable:
    """
    Test class for Describable functionality.
    """

    def test_abstract_initialization(self):
        """
        Test that Describable cannot be instantiated directly (abstract class).
        """
        try:
            _obj = Describable()
            assert False, "Describable should not be instantiable"
        except TypeError:
            pass  # Expected behavior

    def test_initialization(self):
        """
        Test that Describable initializes all fields to None.
        """

        class ConcreteDescribable(Describable):
            def __init__(self):
                super().__init__()

        obj = ConcreteDescribable()

        assert obj.getAdminData() is None
        assert obj.getCategory() is None
        assert obj.getDesc() is None
        assert obj.getIntroduction() is None

    def test_get_set_admin_data_describable(self):
        """
        Test getAdminData and setAdminData methods for Describable.
        """

        class ConcreteDescribable(Describable):
            def __init__(self):
                super().__init__()

        obj = ConcreteDescribable()

        assert obj.getAdminData() is None

        admin_data = AdminData()
        result = obj.setAdminData(admin_data)
        assert result is obj  # method chaining
        assert obj.getAdminData() is admin_data

        result = obj.setAdminData(None)
        assert result is obj  # method chaining with None
        assert obj.getAdminData() is admin_data  # None is a no-op

    def test_remove_admin_data_describable(self):
        """
        Test removeAdminData method for Describable.
        """

        class ConcreteDescribable(Describable):
            def __init__(self):
                super().__init__()

        obj = ConcreteDescribable()

        admin_data = AdminData()
        obj.setAdminData(admin_data)
        assert obj.getAdminData() is admin_data

        obj.removeAdminData()
        assert obj.getAdminData() is None

    def test_get_set_category_describable(self):
        """
        Test getCategory and setCategory methods in Describable class.
        """

        class ConcreteDescribable(Describable):
            def __init__(self):
                super().__init__()

        obj = ConcreteDescribable()

        assert obj.getCategory() is None

        category = CategoryString().setValue("TestDescribableCategory")
        result = obj.setCategory(category)
        assert result is obj  # method chaining
        assert obj.getCategory() is category

        result = obj.setCategory(None)
        assert result is obj  # method chaining with None
        assert obj.getCategory() is category  # None is a no-op

    def test_get_set_desc_describable(self):
        """
        Test getDesc and setDesc methods for Describable.
        """

        class ConcreteDescribable(Describable):
            def __init__(self):
                super().__init__()

        obj = ConcreteDescribable()

        assert obj.getDesc() is None

        desc = MultiLanguageOverviewParagraph()
        result = obj.setDesc(desc)
        assert result is obj  # method chaining
        assert obj.getDesc() is desc

        result = obj.setDesc(None)
        assert result is obj  # method chaining with None
        assert obj.getDesc() is desc  # None is a no-op

    def test_get_set_introduction_describable(self):
        """
        Test getIntroduction and setIntroduction methods for Describable.
        """

        class ConcreteDescribable(Describable):
            def __init__(self):
                super().__init__()

        obj = ConcreteDescribable()

        assert obj.getIntroduction() is None

        intro = DocumentationBlock()
        result = obj.setIntroduction(intro)
        assert result is obj  # method chaining
        assert obj.getIntroduction() is intro

        result = obj.setIntroduction(None)
        assert result is obj  # method chaining with None
        assert obj.getIntroduction() is intro  # None is a no-op
