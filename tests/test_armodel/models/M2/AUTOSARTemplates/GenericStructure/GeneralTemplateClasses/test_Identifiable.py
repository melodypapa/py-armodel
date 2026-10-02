"""
This module contains comprehensive tests for the Identifiable.py file
in the AUTOSAR GenericStructure module.
"""

import typing

from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.CommonStructure.ImplementationDataTypes import ArraySizeSemanticsEnum
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.AnyInstanceRef import AnyInstanceRef
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import RoleBasedResourceDependency
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable import (
    CpSoftwareClusterResource,
    Describable,
    DiagnosticAuthTransmitCertificateEvaluation,
    DiagnosticDataElement,
    DiagnosticParameterElement,
    Identifiable,
    MultilanguageReferrable,
    Referrable,
    ShortNameFragment,
    SingleLanguageReferrable,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import Boolean, CategoryString, Identifier, PositiveInteger, RefType, String
from armodel.models.M2.AUTOSARTemplates.GenericStructure.ViewMapSet import ViewMap
from armodel.models.M2.MSR.AsamHdo.AdminData import AdminData
from armodel.models.M2.MSR.DataDictionary.DataDefProperties import SwDataDefProps
from armodel.models.M2.MSR.Documentation.Annotation import Annotation
from armodel.models.M2.MSR.Documentation.TextModel.BlockElements import DocumentationBlock
from armodel.models.M2.MSR.Documentation.TextModel.MultilanguageData import MultilanguageLongName, MultiLanguageOverviewParagraph
from armodel.models.M2.MSR.Documentation.TextModel.SingleLanguageData import SingleLanguageLongName


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

    def test_class_docstring_verbatim(self):
        """
        Test that the class docstring is the Table 4.13 Note verbatim.
        """
        assert ShortNameFragment.__doc__.strip() == "This class describes how the Referrable.shortName is composed of several shortNameFragments."

    def test_init_has_no_docstring(self):
        """
        Test that __init__ has no docstring (spec Notes live in inline member comments).
        """
        assert ShortNameFragment.__init__.__doc__ is None

    def test_initialization(self):
        """
        Test that ShortNameFragment initializes with None attributes.
        """
        fragment = ShortNameFragment()
        assert fragment.getRole() is None
        assert fragment.getFragment() is None

    def test_role_typed_string(self):
        """
        Test that role is typed String per Table 4.13 (getter/setter annotations).
        """
        getter_hints = typing.get_type_hints(ShortNameFragment.getRole)
        assert getter_hints.get("return") == typing.Optional[String]

        setter_hints = typing.get_type_hints(ShortNameFragment.setRole)
        assert setter_hints.get("value") == typing.Optional[String]
        assert setter_hints.get("return") is ShortNameFragment

    def test_fragment_typed_identifier(self):
        """
        Test that fragment is typed Identifier per Table 4.13 (getter/setter annotations).
        """
        getter_hints = typing.get_type_hints(ShortNameFragment.getFragment)
        assert getter_hints.get("return") == typing.Optional[Identifier]

        setter_hints = typing.get_type_hints(ShortNameFragment.setFragment)
        assert setter_hints.get("value") == typing.Optional[Identifier]
        assert setter_hints.get("return") is ShortNameFragment

    def test_role_setter_getter(self):
        """
        Test setRole and getRole methods.
        """
        fragment = ShortNameFragment()
        assert fragment.setRole(String().setValue("prefix")) is fragment
        assert isinstance(fragment.getRole(), String)
        assert fragment.getRole().getValue() == "prefix"

    def test_role_none_is_noop(self):
        """
        Test that setRole(None) does not overwrite an existing role.
        """
        fragment = ShortNameFragment()
        fragment.setRole(String().setValue("prefix"))
        fragment.setRole(None)
        assert fragment.getRole().getValue() == "prefix"

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


class TestSingleLanguageReferrable:
    """
    Test class for SingleLanguageReferrable functionality (AUTOSAR_FO_TPS_GenericStructureTemplate, Table 4.12).
    """

    def test_abstract_initialization(self):
        """
        Test that SingleLanguageReferrable cannot be instantiated directly (abstract class).
        """
        parent = AUTOSAR.getInstance()
        ar_root = parent.createARPackage("AUTOSAR")
        try:
            _obj = SingleLanguageReferrable(ar_root, "TestSLReferrable")
            assert False, "SingleLanguageReferrable should not be instantiable"
        except TypeError:
            pass  # Expected behavior

    def _make_obj(self):
        parent = AUTOSAR.getInstance()
        ar_root = parent.createARPackage("AUTOSAR")

        class ConcreteSingleLanguageReferrable(SingleLanguageReferrable):
            def __init__(self, parent, short_name):
                super().__init__(parent, short_name)

        return ConcreteSingleLanguageReferrable(ar_root, "TestName")

    def test_initialization_default_none(self):
        """
        Test that longName1 is None by default and the Referrable base is initialized.
        """
        obj = self._make_obj()
        assert obj.getLongName1() is None
        assert obj.getShortName() == "TestName"
        assert obj.getParent() is not None

    def test_get_set_long_name1(self):
        """
        Test getLongName1 and setLongName1 round-trip and chaining.
        """
        obj = self._make_obj()

        long_name = SingleLanguageLongName()
        result = obj.setLongName1(long_name)
        assert result is obj  # method chaining
        assert obj.getLongName1() is long_name

    def test_set_long_name1_none_is_noop(self):
        """
        Test that setLongName1(None) does not overwrite an existing longName1.
        """
        obj = self._make_obj()

        long_name = SingleLanguageLongName()
        obj.setLongName1(long_name)
        assert obj.getLongName1() is long_name

        result = obj.setLongName1(None)
        assert result is obj  # method chaining with None
        assert obj.getLongName1() is long_name  # None is a no-op


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


class TestViewMap:
    """
    Test class for ViewMap functionality.
    """

    def _create_view_map(self) -> ViewMap:
        parent = AUTOSAR.getInstance()
        ar_root = parent.createARPackage("AUTOSAR")
        return ViewMap(ar_root, "TestViewMap")

    def test_initialization(self):
        """
        Test that ViewMap is initialized with the spec defaults.
        """
        obj = self._create_view_map()

        assert obj.getShortName() == "TestViewMap"
        assert isinstance(obj, Identifiable)
        assert obj.getFirstElementRefs() == []
        assert obj.getFirstElementIRefs() == []
        assert obj.getRole() is None
        assert obj.getSecondElementRefs() == []
        assert obj.getSecondElementIRefs() == []

    def test_get_set_role(self):
        """
        Test getRole and setRole round-trip and None no-op.
        """
        obj = self._create_view_map()

        assert obj.getRole() is None

        role = Identifier()
        role.setValue("AR_SystemDescription_SystemExtract")
        result = obj.setRole(role)
        assert result is obj  # method chaining
        assert obj.getRole() is role

        result = obj.setRole(None)
        assert result is obj  # method chaining with None
        assert obj.getRole() is role  # None is a no-op

    def test_add_get_first_element_refs(self):
        """
        Test getFirstElementRefs and addFirstElementRef round-trip and None no-op.
        """
        obj = self._create_view_map()

        assert obj.getFirstElementRefs() == []

        ref = RefType()
        ref.setValue("/AUTOSAR/First/Element")
        result = obj.addFirstElementRef(ref)
        assert result is obj  # method chaining
        assert obj.getFirstElementRefs() == [ref]

        obj.addFirstElementRef(None)
        assert obj.getFirstElementRefs() == [ref]  # None is a no-op

    def test_add_get_first_element_irefs(self):
        """
        Test getFirstElementIRefs and addFirstElementIRef round-trip and None no-op.
        """
        obj = self._create_view_map()

        assert obj.getFirstElementIRefs() == []

        iref = AnyInstanceRef()
        result = obj.addFirstElementIRef(iref)
        assert result is obj  # method chaining
        assert obj.getFirstElementIRefs() == [iref]

        obj.addFirstElementIRef(None)
        assert obj.getFirstElementIRefs() == [iref]  # None is a no-op

    def test_add_get_second_element_refs(self):
        """
        Test getSecondElementRefs and addSecondElementRef round-trip and None no-op.
        """
        obj = self._create_view_map()

        assert obj.getSecondElementRefs() == []

        ref = RefType()
        ref.setValue("/AUTOSAR/Second/Element")
        result = obj.addSecondElementRef(ref)
        assert result is obj  # method chaining
        assert obj.getSecondElementRefs() == [ref]

        obj.addSecondElementRef(None)
        assert obj.getSecondElementRefs() == [ref]  # None is a no-op

    def test_add_get_second_element_irefs(self):
        """
        Test getSecondElementIRefs and addSecondElementIRef round-trip and None no-op.
        """
        obj = self._create_view_map()

        assert obj.getSecondElementIRefs() == []

        iref = AnyInstanceRef()
        result = obj.addSecondElementIRef(iref)
        assert result is obj  # method chaining
        assert obj.getSecondElementIRefs() == [iref]

        obj.addSecondElementIRef(None)
        assert obj.getSecondElementIRefs() == [iref]  # None is a no-op


class TestDiagnosticParameterElement:
    """
    Test class for DiagnosticParameterElement functionality.

    Spec: AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf, Table 4.6, p.36
    (Base DiagnosticAbstractParameter is an un-synced stub queued within this
    batch — only DiagnosticParameterElement's own Table 4.6 rows are exercised
    here.)
    """

    def _make_obj(self) -> DiagnosticParameterElement:
        parent = AUTOSAR.getInstance()
        return DiagnosticParameterElement(parent, "Elem1")

    def test_initialization_defaults(self):
        """
        Test that DiagnosticParameterElement is initialized with the spec defaults.
        """
        obj = self._make_obj()

        assert obj.getShortName() == "Elem1"
        assert obj.getArraySize() is None
        assert obj.getSubElements() == []

    def test_get_set_array_size(self):
        """
        Round-trips arraySize; None is a no-op.
        """
        obj = self._make_obj()

        value = PositiveInteger()
        value.setValue("8")
        result = obj.setArraySize(value)
        assert result is obj  # method chaining
        assert obj.getArraySize() is value
        assert obj.getArraySize().getValue() == 8

        obj.setArraySize(None)
        assert obj.getArraySize() is value  # None is a no-op

    def test_get_set_array_size_type_hints(self):
        """
        Pin the accessor annotations to the spec type (Rule 0003).
        """
        getter_hints = typing.get_type_hints(DiagnosticParameterElement.getArraySize)
        assert getter_hints.get("return") == typing.Optional[PositiveInteger]

        setter_hints = typing.get_type_hints(DiagnosticParameterElement.setArraySize)
        assert setter_hints.get("value") == typing.Optional[PositiveInteger]
        assert setter_hints.get("return") is DiagnosticParameterElement

    def test_create_sub_element(self):
        """
        Test createSubElement creates, appends and returns the existing one for a duplicate short name.
        """
        obj = self._make_obj()

        sub_element = obj.createSubElement("Sub1")
        assert sub_element is not None
        assert sub_element.getShortName() == "Sub1"
        assert sub_element.getParent() is obj
        assert obj.getSubElements() == [sub_element]

        duplicate = obj.createSubElement("Sub1")
        assert duplicate is sub_element  # duplicate short name returns the existing element
        assert len(obj.getSubElements()) == 1

        second = obj.createSubElement("Sub2")
        assert obj.getSubElements() == [sub_element, second]

    def test_get_sub_elements_default(self):
        """
        Test that getSubElements returns an empty list by default and None add is a no-op via the factory contract.
        """
        obj = self._make_obj()

        assert obj.getSubElements() == []

    def test_get_sub_elements_type_hints(self):
        """
        Pin the subElement aggregation annotations to the spec types (Rule 0003).
        """
        getter_hints = typing.get_type_hints(DiagnosticParameterElement.getSubElements)
        assert getter_hints.get("return") == typing.List[DiagnosticParameterElement]

        factory_hints = typing.get_type_hints(DiagnosticParameterElement.createSubElement)
        assert factory_hints.get("short_name") is str
        assert factory_hints.get("return") is DiagnosticParameterElement


class TestDiagnosticDataElement:
    """
    Test class for DiagnosticDataElement functionality.

    Spec: AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf, Table 4.9, p.41
    """

    def _make_obj(self) -> DiagnosticDataElement:
        parent = AUTOSAR.getInstance()
        return DiagnosticDataElement(parent, "De1")

    def test_initialization_defaults(self):
        """
        Test that DiagnosticDataElement is initialized with the spec defaults.
        """
        obj = self._make_obj()

        assert obj.getShortName() == "De1"
        assert obj.getArraySizeSemantics() is None
        assert obj.getMaxNumberOfElements() is None
        assert obj.getScalingInfoSize() is None
        assert obj.getSwDataDefProps() is None
        assert obj.getVariationPoint() is None

    def test_get_set_array_size_semantics(self):
        """
        Round-trips arraySizeSemantics; None is a no-op.
        """
        obj = self._make_obj()

        value = ArraySizeSemanticsEnum().setValue(ArraySizeSemanticsEnum.FIXED_SIZE)
        result = obj.setArraySizeSemantics(value)
        assert result is obj  # method chaining
        assert obj.getArraySizeSemantics() is value

        obj.setArraySizeSemantics(None)
        assert obj.getArraySizeSemantics() is value  # None is a no-op

    def test_get_set_max_number_of_elements(self):
        """
        Round-trips maxNumberOfElements; None is a no-op.
        """
        obj = self._make_obj()

        value = PositiveInteger()
        value.setValue("4")
        result = obj.setMaxNumberOfElements(value)
        assert result is obj  # method chaining
        assert obj.getMaxNumberOfElements() is value
        assert obj.getMaxNumberOfElements().getValue() == 4

        obj.setMaxNumberOfElements(None)
        assert obj.getMaxNumberOfElements() is value  # None is a no-op

    def test_get_set_scaling_info_size(self):
        """
        Round-trips scalingInfoSize; None is a no-op.
        """
        obj = self._make_obj()

        value = PositiveInteger()
        value.setValue("8")
        result = obj.setScalingInfoSize(value)
        assert result is obj  # method chaining
        assert obj.getScalingInfoSize() is value

        obj.setScalingInfoSize(None)
        assert obj.getScalingInfoSize() is value  # None is a no-op

    def test_get_set_sw_data_def_props(self):
        """
        Round-trips swDataDefProps; None is a no-op.
        """
        obj = self._make_obj()

        value = SwDataDefProps()
        result = obj.setSwDataDefProps(value)
        assert result is obj  # method chaining
        assert obj.getSwDataDefProps() is value

        obj.setSwDataDefProps(None)
        assert obj.getSwDataDefProps() is value  # None is a no-op

    def test_variation_point_mixin(self):
        """
        Test the VariationPointCapable mixin accessors (VP-capable per Rule 0020: XSD group DIAGNOSTIC-DATA-ELEMENT carries VARIATION-POINT, Applicable for DiagnosticAbstractParameter.dataElement).
        """
        obj = self._make_obj()

        assert obj.getVariationPoint() is None

    def test_get_set_max_number_of_elements_type_hints(self):
        """
        Pin the PositiveInteger accessor annotations to the spec type (Rule 0003).
        (arraySizeSemantics / swDataDefProps are TYPE_CHECKING cross-package names —
        nothing pins those two annotations at runtime; see the class checklist.)
        """
        import typing

        getter_hints = typing.get_type_hints(DiagnosticDataElement.getMaxNumberOfElements)
        assert getter_hints.get("return") == typing.Optional[PositiveInteger]

        setter_hints = typing.get_type_hints(DiagnosticDataElement.setMaxNumberOfElements)
        assert setter_hints.get("value") == typing.Optional[PositiveInteger]
        assert setter_hints.get("return") is DiagnosticDataElement

        getter_hints = typing.get_type_hints(DiagnosticDataElement.getScalingInfoSize)
        assert getter_hints.get("return") == typing.Optional[PositiveInteger]

        setter_hints = typing.get_type_hints(DiagnosticDataElement.setScalingInfoSize)
        assert setter_hints.get("value") == typing.Optional[PositiveInteger]
        assert setter_hints.get("return") is DiagnosticDataElement


class TestDiagnosticAuthTransmitCertificateEvaluation:
    """
    Test class for DiagnosticAuthTransmitCertificateEvaluation functionality.

    Spec: AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf, Table 4.59, p.101
    """

    CLASS_NOTE = "This meta-class represents the ability to configure a certificate evaluation in the context of a diagnostic authentication."

    def _make_obj(self) -> DiagnosticAuthTransmitCertificateEvaluation:
        parent = AUTOSAR.getInstance()
        return DiagnosticAuthTransmitCertificateEvaluation(parent, "Eval1")

    def test_initialization_defaults(self):
        """
        Test that DiagnosticAuthTransmitCertificateEvaluation is initialized with the spec defaults.
        """
        obj = self._make_obj()

        assert obj.getShortName() == "Eval1"
        assert obj.getEvaluationId() is None
        assert obj.getFunction() is None

    def test_class_docstring_is_spec_note_verbatim(self):
        """
        Test that the class docstring is the spec Note verbatim.
        """
        assert DiagnosticAuthTransmitCertificateEvaluation.__doc__ == self.CLASS_NOTE

    def test_init_has_no_docstring(self):
        """
        Test that __init__ carries no docstring.
        """
        assert DiagnosticAuthTransmitCertificateEvaluation.__init__.__doc__ is None

    def test_get_set_evaluation_id(self):
        """
        Round-trips evaluationId; None is a no-op.
        """
        obj = self._make_obj()

        value = PositiveInteger()
        value.setValue("2")
        result = obj.setEvaluationId(value)
        assert result is obj  # method chaining
        assert obj.getEvaluationId() is value
        assert obj.getEvaluationId().getValue() == 2

        obj.setEvaluationId(None)
        assert obj.getEvaluationId() is value  # None is a no-op

    def test_get_set_function(self):
        """
        Round-trips function; None is a no-op.
        """
        obj = self._make_obj()

        value = String()
        value.setValue("FUNCTION_SECURE_CODING")
        result = obj.setFunction(value)
        assert result is obj  # method chaining
        assert obj.getFunction() is value
        assert obj.getFunction().getValue() == "FUNCTION_SECURE_CODING"

        obj.setFunction(None)
        assert obj.getFunction() is value  # None is a no-op

    def test_get_set_type_hints(self):
        """
        Pin the accessor annotations to the spec types (Rule 0003).
        """
        getter_hints = typing.get_type_hints(DiagnosticAuthTransmitCertificateEvaluation.getEvaluationId)
        assert getter_hints.get("return") == typing.Optional[PositiveInteger]

        setter_hints = typing.get_type_hints(DiagnosticAuthTransmitCertificateEvaluation.setEvaluationId)
        assert setter_hints.get("value") == typing.Optional[PositiveInteger]
        assert setter_hints.get("return") is DiagnosticAuthTransmitCertificateEvaluation

        getter_hints = typing.get_type_hints(DiagnosticAuthTransmitCertificateEvaluation.getFunction)
        assert getter_hints.get("return") == typing.Optional[String]

        setter_hints = typing.get_type_hints(DiagnosticAuthTransmitCertificateEvaluation.setFunction)
        assert setter_hints.get("value") == typing.Optional[String]
        assert setter_hints.get("return") is DiagnosticAuthTransmitCertificateEvaluation

    def test_create_via_parent_certificate(self):
        """
        Test creation through the owning DiagnosticAuthTransmitCertificate aggregation and duplicate reuse.
        """
        package = AUTOSAR.getInstance().createARPackage("AuthTransmitCertificates")
        certificate = package.createDiagnosticAuthTransmitCertificate("Certificate1")

        evaluation = certificate.createDiagnosticAuthTransmitCertificateEvaluation("Eval1")
        assert evaluation is not None
        assert isinstance(evaluation, DiagnosticAuthTransmitCertificateEvaluation)
        assert evaluation.getShortName() == "Eval1"
        assert evaluation.getParent() is certificate
        assert certificate.getCertificateEvaluations() == [evaluation]

        duplicate = certificate.createDiagnosticAuthTransmitCertificateEvaluation("Eval1")
        assert duplicate is evaluation  # duplicate short name returns the existing element
        assert len(certificate.getCertificateEvaluations()) == 1


class TestCpSoftwareClusterResource:
    """
    Test class for CpSoftwareClusterResource functionality.

    Spec: AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf, Table 5.44, p.271
    """

    CLASS_NOTE = "Represents a single resource required or provided by a CP Software Cluster. Tags: atp.recommendedPackage=Resources"

    def _make_obj(self) -> CpSoftwareClusterResource:
        parent = AUTOSAR.getInstance()
        ar_root = parent.createARPackage("AUTOSAR")
        return CpSoftwareClusterResource(ar_root, "TestResource")

    def test_is_concrete(self):
        """
        Test that a concrete CpSoftwareClusterResource instantiates with the spec defaults.
        """
        obj = self._make_obj()

        assert obj.getShortName() == "TestResource"
        assert obj.getDependentResources() == []
        assert obj.getGlobalResourceId() is None
        assert obj.getIsMandatory() is None

    def test_class_docstring_is_spec_note_verbatim(self):
        """
        Test that the class docstring is the spec Note verbatim.
        """
        assert CpSoftwareClusterResource.__doc__ == self.CLASS_NOTE

    def test_init_has_no_docstring(self):
        """
        Test that __init__ carries no docstring.
        """
        assert CpSoftwareClusterResource.__init__.__doc__ is None

    def test_add_get_dependent_resources(self):
        """
        Round-trips the dependentResource aggregation; None is a no-op on add.
        """
        obj = self._make_obj()

        dep1 = RoleBasedResourceDependency()
        result = obj.addDependentResource(dep1)
        assert result is obj  # method chaining
        dep2 = RoleBasedResourceDependency()
        obj.addDependentResource(dep2)

        deps = obj.getDependentResources()
        assert len(deps) == 2
        assert deps[0] is dep1
        assert deps[1] is dep2

        result = obj.addDependentResource(None)
        assert result is obj  # method chaining with None
        assert len(obj.getDependentResources()) == 2  # None is a no-op

    def test_get_set_global_resource_id_and_is_mandatory(self):
        """
        Round-trips the attributes; None is a no-op.
        """
        obj = self._make_obj()

        gid = PositiveInteger()
        gid.setValue("42")
        obj.setGlobalResourceId(gid)
        mandatory = Boolean()
        mandatory.setValue(True)
        obj.setIsMandatory(mandatory)

        assert obj.getGlobalResourceId() is gid
        assert obj.getGlobalResourceId().getValue() == 42
        assert obj.getIsMandatory() is mandatory
        assert obj.getIsMandatory().getValue() is True

        obj.setGlobalResourceId(None)
        obj.setIsMandatory(None)
        assert obj.getGlobalResourceId() is gid  # None is a no-op
        assert obj.getIsMandatory() is mandatory  # None is a no-op


class TestRoleBasedResourceDependency:
    """
    Test class for RoleBasedResourceDependency functionality.

    Spec: AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf, Table 5.45, p.272
    """

    CLASS_NOTE = "This class specifies a dependency between CpSoftwareClusterResources."

    def _make_obj(self) -> RoleBasedResourceDependency:
        return RoleBasedResourceDependency()

    def test_is_concrete(self):
        """
        Test that a concrete RoleBasedResourceDependency instantiates with the spec defaults.
        """
        obj = self._make_obj()

        assert obj is not None
        assert obj.getResourceRef() is None
        assert obj.getRole() is None

    def test_class_docstring_is_spec_note_verbatim(self):
        """
        Test that the class docstring is the spec Note verbatim.
        """
        assert RoleBasedResourceDependency.__doc__ == self.CLASS_NOTE

    def test_init_has_no_docstring(self):
        """
        Test that __init__ carries no docstring.
        """
        assert RoleBasedResourceDependency.__init__.__doc__ is None

    def test_get_set_resource_ref_and_role(self):
        """
        Round-trips the reference and the role; None is a no-op.
        """
        obj = self._make_obj()

        ref = RefType().setValue("/AUTOSAR/Resources/Res1").setDest("CP-SOFTWARE-CLUSTER-RESOURCE")
        obj.setResourceRef(ref)
        role = Identifier()
        role.setValue("consumer")
        obj.setRole(role)

        assert obj.getResourceRef() is ref
        assert obj.getRole() is role
        assert obj.getRole().getValue() == "consumer"

        obj.setResourceRef(None)
        obj.setRole(None)
        assert obj.getResourceRef() is ref  # None is a no-op
        assert obj.getRole() is role  # None is a no-op
