"""
This module contains comprehensive tests for the Identifiable.py file
in the AUTOSAR GenericStructure module.
"""

import inspect
import typing

import pytest

from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.CommonStructure.ImplementationDataTypes import ArraySizeSemanticsEnum
from armodel.models.M2.AUTOSARTemplates.CommonStructure.ServiceNeeds import DiagEventDebounceCounterBased, DiagEventDebounceMonitorInternal, DiagEventDebounceTimeBased
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.AnyInstanceRef import AnyInstanceRef
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import (
    ARObject,
    DdsCpServiceInstanceEvent,
    DdsCpServiceInstanceOperation,
    DdsDeadline,
    DdsDestinationOrder,
    DdsDurability,
    DdsDurabilityService,
    DdsHistory,
    DdsLatencyBudget,
    DdsLifespan,
    DdsLiveliness,
    DdsOwnership,
    DdsOwnershipStrength,
    DdsReliability,
    DdsResourceLimits,
    DdsTopicData,
    DdsTransportPriority,
    DiagnosticParameter,
    RoleBasedResourceDependency,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable import (
    BinaryManifestAddressableObject,
    BinaryManifestItem,
    BinaryManifestResource,
    CpSoftwareClusterResource,
    DdsCpConsumedServiceInstance,
    DdsCpDomain,
    DdsCpPartition,
    DdsCpQosProfile,
    DdsCpServiceInstance,
    DdsCpTopic,
    Describable,
    DiagnosticAuthTransmitCertificateEvaluation,
    DiagnosticDataElement,
    DiagnosticDebounceAlgorithmProps,
    DiagnosticFunctionInhibitSource,
    DiagnosticParameterElement,
    DiagnosticRequestRoutineResults,
    DiagnosticRoutineSubfunction,
    DiagnosticStartRoutine,
    DiagnosticStopRoutine,
    GlobalTimeGateway,
    GlobalTimeMaster,
    GlobalTimeSlave,
    Identifiable,
    MultilanguageReferrable,
    Referrable,
    ShortNameFragment,
    SingleLanguageReferrable,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Address,
    AnyVersionString,
    Boolean,
    CategoryString,
    DiagnosticDebounceBehaviorEnum,
    GlobalTimeIcvSupportEnum,
    GlobalTimeIcvVerificationEnum,
    Identifier,
    PositiveInteger,
    RefType,
    String,
    SymbolString,
    TimeValue,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.StereotypeMixins import VariationPointCapable
from armodel.models.M2.AUTOSARTemplates.GenericStructure.VariantHandling import VariationPoint
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

        assert obj.getTotalReferrableElement() == 0
        assert obj.getReferrableElements() == []
        assert obj.IsReferrableElementExists("TestElement") is False
        assert obj.getReferrableElement("TestElement") is None

        obj.addReferrableElement(element)
        assert obj.getTotalReferrableElement() == 1
        assert obj.getReferrableElements() == [element]
        assert obj.IsReferrableElementExists("TestElement") is True
        assert obj.getReferrableElement("TestElement") is element

        # Adding the same short name + type twice does not duplicate the entry.
        obj.addReferrableElement(element)
        assert obj.getTotalReferrableElement() == 1

        obj.removeReferrableElement("TestElement")
        assert obj.getTotalReferrableElement() == 0
        assert obj.getReferrableElements() == []

    def test_remove_element_unknown_short_name_raises(self):
        """
        removeElement raises KeyError for a short name that was never registered.
        """
        obj = self._make_obj()

        try:
            obj.removeReferrableElement("NonExistent")
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


class TestDiagnosticRoutineSubfunction:
    """
    Test class for DiagnosticRoutineSubfunction functionality.

    Spec: AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf, Table 4.84, p.121
    """

    CLASS_NOTE = "This meta-class acts as an abstract base class to routine subfunctions."

    def test_abstract_instantiation_raises(self):
        """
        Test that instantiating the abstract DiagnosticRoutineSubfunction raises TypeError.
        """
        with pytest.raises(TypeError, match="DiagnosticRoutineSubfunction is an abstract class."):
            DiagnosticRoutineSubfunction(AUTOSAR.getInstance(), "Subfunction1")

    def test_subclass_chain(self):
        """
        Test that the concrete subfunctions derive from DiagnosticRoutineSubfunction (Identifiable).
        """
        assert issubclass(DiagnosticRoutineSubfunction, Identifiable)
        assert issubclass(DiagnosticStartRoutine, DiagnosticRoutineSubfunction)

    def test_initialization_defaults_via_subclass(self):
        """
        Test that a concrete subclass is initialized with the spec defaults.
        """
        obj = DiagnosticStartRoutine(AUTOSAR.getInstance(), "StartRoutine1")

        assert obj.getShortName() == "StartRoutine1"
        assert obj.getAccessPermission() is None

    def test_class_docstring_is_spec_note_verbatim(self):
        """
        Test that the class docstring is the spec Note verbatim.
        """
        assert DiagnosticRoutineSubfunction.__doc__ == self.CLASS_NOTE

    def test_init_has_no_docstring(self):
        """
        Test that __init__ carries no docstring.
        """
        assert DiagnosticRoutineSubfunction.__init__.__doc__ is None

    def test_get_set_access_permission(self):
        """
        Round-trips accessPermission; None is a no-op.
        """
        obj = DiagnosticStartRoutine(AUTOSAR.getInstance(), "StartRoutine1")

        value = RefType()
        value.setDest("DIAGNOSTIC-ACCESS-PERMISSION")
        value.setValue("/AUTOSAR/DiagnosticAccessPermissions/Level1")
        result = obj.setAccessPermission(value)
        assert result is obj  # method chaining
        assert obj.getAccessPermission() is value
        assert obj.getAccessPermission().getValue() == "/AUTOSAR/DiagnosticAccessPermissions/Level1"
        assert obj.getAccessPermission().getDest() == "DIAGNOSTIC-ACCESS-PERMISSION"

        obj.setAccessPermission(None)
        assert obj.getAccessPermission() is value  # None is a no-op

    def test_get_set_type_hints(self):
        """
        Pin the accessor annotations to the spec types (Rule 0003).
        """
        getter_hints = typing.get_type_hints(DiagnosticRoutineSubfunction.getAccessPermission)
        assert getter_hints.get("return") == typing.Optional[RefType]

        setter_hints = typing.get_type_hints(DiagnosticRoutineSubfunction.setAccessPermission)
        assert setter_hints.get("value") == typing.Optional[RefType]
        assert setter_hints.get("return") is DiagnosticRoutineSubfunction


class TestDiagnosticStartRoutine:
    """
    Test class for DiagnosticStartRoutine functionality.

    Spec: AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf, Table 4.86, p.124
    """

    CLASS_NOTE = "This represents the ability to start a diagnostic routine."

    def _make_obj(self) -> DiagnosticStartRoutine:
        return DiagnosticStartRoutine(AUTOSAR.getInstance(), "StartRoutine1")

    def test_subclass_chain(self):
        """
        Test that DiagnosticStartRoutine derives from DiagnosticRoutineSubfunction.
        """
        assert issubclass(DiagnosticStartRoutine, DiagnosticRoutineSubfunction)

    def test_initialization_defaults(self):
        """
        Test that DiagnosticStartRoutine is initialized with the spec defaults.
        """
        obj = self._make_obj()

        assert obj.getShortName() == "StartRoutine1"
        assert obj.getRequest() == []
        assert obj.getResponse() == []

    def test_class_docstring_is_spec_note_verbatim(self):
        """
        Test that the class docstring is the spec Note verbatim.
        """
        assert DiagnosticStartRoutine.__doc__ == self.CLASS_NOTE

    def test_init_has_no_docstring(self):
        """
        Test that __init__ carries no docstring.
        """
        assert DiagnosticStartRoutine.__init__.__doc__ is None

    def test_add_get_request(self):
        """
        Appends request parameters; None is a no-op.
        """
        obj = self._make_obj()

        first = DiagnosticParameter()
        result = obj.addRequest(first)
        assert result is obj  # method chaining
        second = DiagnosticParameter()
        obj.addRequest(second)
        assert obj.getRequest() == [first, second]

        obj.addRequest(None)
        assert obj.getRequest() == [first, second]  # None is a no-op

    def test_add_get_response(self):
        """
        Appends response parameters; None is a no-op.
        """
        obj = self._make_obj()

        value = DiagnosticParameter()
        result = obj.addResponse(value)
        assert result is obj  # method chaining
        assert obj.getResponse() == [value]

        obj.addResponse(None)
        assert obj.getResponse() == [value]  # None is a no-op

    def test_get_add_type_hints(self):
        """
        Pin the accessor annotations to the spec types (Rule 0003).
        """
        getter_hints = typing.get_type_hints(DiagnosticStartRoutine.getRequest)
        assert getter_hints.get("return") == typing.List[DiagnosticParameter]

        adder_hints = typing.get_type_hints(DiagnosticStartRoutine.addRequest)
        assert adder_hints.get("value") == typing.Optional[DiagnosticParameter]
        assert adder_hints.get("return") is DiagnosticStartRoutine

        getter_hints = typing.get_type_hints(DiagnosticStartRoutine.getResponse)
        assert getter_hints.get("return") == typing.List[DiagnosticParameter]

        adder_hints = typing.get_type_hints(DiagnosticStartRoutine.addResponse)
        assert adder_hints.get("value") == typing.Optional[DiagnosticParameter]
        assert adder_hints.get("return") is DiagnosticStartRoutine

    def test_accessor_docstrings_are_spec_notes_verbatim(self):
        """
        Accessor docstrings carry the spec Note verbatim (adder + None-no-op sentence).
        """
        assert inspect.cleandoc(DiagnosticStartRoutine.getRequest.__doc__) == "This represents the request parameters."
        assert inspect.cleandoc(DiagnosticStartRoutine.addRequest.__doc__) == "This represents the request parameters.\nA None value is a no-op and does not append a request."
        assert inspect.cleandoc(DiagnosticStartRoutine.getResponse.__doc__) == "This represents the response parameters."
        assert inspect.cleandoc(DiagnosticStartRoutine.addResponse.__doc__) == "This represents the response parameters.\nA None value is a no-op and does not append a response."


class TestDiagnosticStopRoutine:
    """
    Test class for DiagnosticStopRoutine functionality.

    Spec: AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf, Table 4.87, p.125
    """

    CLASS_NOTE = "This represents the ability to stop a diagnostic routine."

    def _make_obj(self) -> DiagnosticStopRoutine:
        return DiagnosticStopRoutine(AUTOSAR.getInstance(), "StopRoutine1")

    def test_subclass_chain(self):
        """
        Test that DiagnosticStopRoutine derives from DiagnosticRoutineSubfunction.
        """
        assert issubclass(DiagnosticStopRoutine, DiagnosticRoutineSubfunction)

    def test_initialization_defaults(self):
        """
        Test that DiagnosticStopRoutine is initialized with the spec defaults.
        """
        obj = self._make_obj()

        assert obj.getShortName() == "StopRoutine1"
        assert obj.getRequest() == []
        assert obj.getResponse() == []

    def test_class_docstring_is_spec_note_verbatim(self):
        """
        Test that the class docstring is the spec Note verbatim.
        """
        assert DiagnosticStopRoutine.__doc__ == self.CLASS_NOTE

    def test_init_has_no_docstring(self):
        """
        Test that __init__ carries no docstring.
        """
        assert DiagnosticStopRoutine.__init__.__doc__ is None

    def test_add_get_request(self):
        """
        Appends request parameters; None is a no-op.
        """
        obj = self._make_obj()

        first = DiagnosticParameter()
        result = obj.addRequest(first)
        assert result is obj  # method chaining
        second = DiagnosticParameter()
        obj.addRequest(second)
        assert obj.getRequest() == [first, second]

        obj.addRequest(None)
        assert obj.getRequest() == [first, second]  # None is a no-op

    def test_add_get_response(self):
        """
        Appends response parameters; None is a no-op.
        """
        obj = self._make_obj()

        value = DiagnosticParameter()
        result = obj.addResponse(value)
        assert result is obj  # method chaining
        assert obj.getResponse() == [value]

        obj.addResponse(None)
        assert obj.getResponse() == [value]  # None is a no-op

    def test_get_add_type_hints(self):
        """
        Pin the accessor annotations to the spec types (Rule 0003).
        """
        getter_hints = typing.get_type_hints(DiagnosticStopRoutine.getRequest)
        assert getter_hints.get("return") == typing.List[DiagnosticParameter]

        adder_hints = typing.get_type_hints(DiagnosticStopRoutine.addRequest)
        assert adder_hints.get("value") == typing.Optional[DiagnosticParameter]
        assert adder_hints.get("return") is DiagnosticStopRoutine

        getter_hints = typing.get_type_hints(DiagnosticStopRoutine.getResponse)
        assert getter_hints.get("return") == typing.List[DiagnosticParameter]

        adder_hints = typing.get_type_hints(DiagnosticStopRoutine.addResponse)
        assert adder_hints.get("value") == typing.Optional[DiagnosticParameter]
        assert adder_hints.get("return") is DiagnosticStopRoutine

    def test_accessor_docstrings_are_spec_notes_verbatim(self):
        """
        Accessor docstrings carry the spec Note verbatim (adder + None-no-op sentence).
        """
        assert inspect.cleandoc(DiagnosticStopRoutine.getRequest.__doc__) == "This represents the request parameters."
        assert inspect.cleandoc(DiagnosticStopRoutine.addRequest.__doc__) == "This represents the request parameters.\nA None value is a no-op and does not append a request."
        assert inspect.cleandoc(DiagnosticStopRoutine.getResponse.__doc__) == "This represents the response parameters."
        assert inspect.cleandoc(DiagnosticStopRoutine.addResponse.__doc__) == "This represents the response parameters.\nA None value is a no-op and does not append a response."


class TestDiagnosticRequestRoutineResults:
    """
    Test class for DiagnosticRequestRoutineResults functionality.

    Spec: AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf, Table 4.88, p.125
    """

    CLASS_NOTE = "This meta-class represents the ability to define the result of a diagnostic routine execution."

    def _make_obj(self) -> DiagnosticRequestRoutineResults:
        return DiagnosticRequestRoutineResults(AUTOSAR.getInstance(), "RequestResults1")

    def test_subclass_chain(self):
        """
        Test that DiagnosticRequestRoutineResults derives from DiagnosticRoutineSubfunction.
        """
        assert issubclass(DiagnosticRequestRoutineResults, DiagnosticRoutineSubfunction)

    def test_initialization_defaults(self):
        """
        Test that DiagnosticRequestRoutineResults is initialized with the spec defaults.
        """
        obj = self._make_obj()

        assert obj.getShortName() == "RequestResults1"
        assert obj.getRequest() == []
        assert obj.getResponse() == []

    def test_class_docstring_is_spec_note_verbatim(self):
        """
        Test that the class docstring is the spec Note verbatim.
        """
        assert DiagnosticRequestRoutineResults.__doc__ == self.CLASS_NOTE

    def test_init_has_no_docstring(self):
        """
        Test that __init__ carries no docstring.
        """
        assert DiagnosticRequestRoutineResults.__init__.__doc__ is None

    def test_add_get_request(self):
        """
        Appends request parameters; None is a no-op.
        """
        obj = self._make_obj()

        first = DiagnosticParameter()
        result = obj.addRequest(first)
        assert result is obj  # method chaining
        second = DiagnosticParameter()
        obj.addRequest(second)
        assert obj.getRequest() == [first, second]

        obj.addRequest(None)
        assert obj.getRequest() == [first, second]  # None is a no-op

    def test_add_get_response(self):
        """
        Appends response parameters; None is a no-op.
        """
        obj = self._make_obj()

        value = DiagnosticParameter()
        result = obj.addResponse(value)
        assert result is obj  # method chaining
        assert obj.getResponse() == [value]

        obj.addResponse(None)
        assert obj.getResponse() == [value]  # None is a no-op

    def test_get_add_type_hints(self):
        """
        Pin the accessor annotations to the spec types (Rule 0003).
        """
        getter_hints = typing.get_type_hints(DiagnosticRequestRoutineResults.getRequest)
        assert getter_hints.get("return") == typing.List[DiagnosticParameter]

        adder_hints = typing.get_type_hints(DiagnosticRequestRoutineResults.addRequest)
        assert adder_hints.get("value") == typing.Optional[DiagnosticParameter]
        assert adder_hints.get("return") is DiagnosticRequestRoutineResults

        getter_hints = typing.get_type_hints(DiagnosticRequestRoutineResults.getResponse)
        assert getter_hints.get("return") == typing.List[DiagnosticParameter]

        adder_hints = typing.get_type_hints(DiagnosticRequestRoutineResults.addResponse)
        assert adder_hints.get("value") == typing.Optional[DiagnosticParameter]
        assert adder_hints.get("return") is DiagnosticRequestRoutineResults

    def test_accessor_docstrings_are_spec_notes_verbatim(self):
        """
        Accessor docstrings carry the spec Note verbatim (adder + None-no-op sentence).
        """
        assert inspect.cleandoc(DiagnosticRequestRoutineResults.getRequest.__doc__) == "This represents the request parameters."
        assert inspect.cleandoc(DiagnosticRequestRoutineResults.addRequest.__doc__) == "This represents the request parameters.\nA None value is a no-op and does not append a request."
        assert inspect.cleandoc(DiagnosticRequestRoutineResults.getResponse.__doc__) == "This represents the response parameters."
        assert inspect.cleandoc(DiagnosticRequestRoutineResults.addResponse.__doc__) == "This represents the response parameters.\nA None value is a no-op and does not append a response."


class TestDiagnosticDebounceAlgorithmProps:
    """
    Test class for DiagnosticDebounceAlgorithmProps functionality.

    Spec: AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf, Table 4.187, p.196
    """

    CLASS_NOTE = "Defines properties for the debounce algorithm class."

    def _make_obj(self) -> DiagnosticDebounceAlgorithmProps:
        return DiagnosticDebounceAlgorithmProps(AUTOSAR.getInstance(), "DebounceProps1")

    def _make_behavior(self, value: str = "freeze") -> DiagnosticDebounceBehaviorEnum:
        # DiagnosticDebounceBehaviorEnum is a stub until its Table 4.192 sync lands
        # in this batch — construct around the not-yet-synced __init__.
        behavior = DiagnosticDebounceBehaviorEnum.__new__(DiagnosticDebounceBehaviorEnum)
        behavior.setValue(value)
        return behavior

    def test_subclass_chain(self):
        """
        Test that DiagnosticDebounceAlgorithmProps derives from Identifiable.
        """
        assert issubclass(DiagnosticDebounceAlgorithmProps, Identifiable)

    def test_initialization_defaults(self):
        """
        Test that DiagnosticDebounceAlgorithmProps is initialized with the spec defaults.
        """
        obj = self._make_obj()

        assert obj.getShortName() == "DebounceProps1"
        assert obj.getDebounceAlgorithm() is None
        assert obj.getDebounceBehavior() is None
        assert obj.getDebounceCounterStorage() is None

    def test_class_docstring_is_spec_note_verbatim(self):
        """
        Test that the class docstring is the spec Note verbatim.
        """
        assert DiagnosticDebounceAlgorithmProps.__doc__ == self.CLASS_NOTE

    def test_init_has_no_docstring(self):
        """
        Test that __init__ carries no docstring.
        """
        assert DiagnosticDebounceAlgorithmProps.__init__.__doc__ is None

    def test_create_get_debounce_algorithm(self):
        """
        Creates a counter-based algorithm; duplicate short name returns the existing element.
        """
        obj = self._make_obj()

        algorithm = obj.createDiagEventDebounceCounterBased("CounterBased1")
        assert isinstance(algorithm, DiagEventDebounceCounterBased)
        assert obj.getDebounceAlgorithm() is algorithm

        again = obj.createDiagEventDebounceCounterBased("CounterBased1")
        assert again is algorithm

    def test_create_monitor_internal_replaces_algorithm(self):
        """
        The 0..1 aggregation assigns the single field; another subtype replaces it.
        """
        obj = self._make_obj()

        first = obj.createDiagEventDebounceCounterBased("CounterBased1")
        second = obj.createDiagEventDebounceMonitorInternal("MonitorInternal1")
        assert isinstance(second, DiagEventDebounceMonitorInternal)
        assert obj.getDebounceAlgorithm() is second
        assert obj.getDebounceAlgorithm() is not first

    def test_create_time_based_algorithm(self):
        """
        Creates a time-based algorithm and assigns the aggregation.
        """
        obj = self._make_obj()

        algorithm = obj.createDiagEventDebounceTimeBased("TimeBased1")
        assert isinstance(algorithm, DiagEventDebounceTimeBased)
        assert obj.getDebounceAlgorithm() is algorithm

    def test_get_set_debounce_behavior(self):
        """
        Setter returns self, value round-trips, None is a no-op.
        """
        obj = self._make_obj()

        value = self._make_behavior("freeze")
        result = obj.setDebounceBehavior(value)
        assert result is obj  # method chaining
        assert obj.getDebounceBehavior() is value

        obj.setDebounceBehavior(None)
        assert obj.getDebounceBehavior() is value  # None is a no-op

    def test_get_set_debounce_counter_storage(self):
        """
        Setter returns self, value round-trips, None is a no-op.
        """
        obj = self._make_obj()

        value = Boolean()
        value.setValue(True)
        result = obj.setDebounceCounterStorage(value)
        assert result is obj  # method chaining
        assert obj.getDebounceCounterStorage() is value
        assert obj.getDebounceCounterStorage().getValue() is True

        obj.setDebounceCounterStorage(None)
        assert obj.getDebounceCounterStorage() is value  # None is a no-op

    def test_get_set_type_hints(self):
        """
        Pin the accessor annotations to the spec types (Rule 0003).
        """
        setter_hints = typing.get_type_hints(DiagnosticDebounceAlgorithmProps.setDebounceBehavior)
        assert setter_hints.get("value") == typing.Optional[DiagnosticDebounceBehaviorEnum]
        assert setter_hints.get("return") is DiagnosticDebounceAlgorithmProps

        getter_hints = typing.get_type_hints(DiagnosticDebounceAlgorithmProps.getDebounceCounterStorage)
        assert getter_hints.get("return") == typing.Optional[Boolean]

        setter_hints = typing.get_type_hints(DiagnosticDebounceAlgorithmProps.setDebounceCounterStorage)
        assert setter_hints.get("value") == typing.Optional[Boolean]
        assert setter_hints.get("return") is DiagnosticDebounceAlgorithmProps

    def test_accessor_docstrings_are_spec_notes_verbatim(self):
        """
        Accessor docstrings carry the spec Note verbatim (setter + None-no-op sentence).
        """
        assert inspect.cleandoc(DiagnosticDebounceAlgorithmProps.getDebounceAlgorithm.__doc__) == "This represents the actual debounce algorithm."
        assert (
            inspect.cleandoc(DiagnosticDebounceAlgorithmProps.getDebounceBehavior.__doc__)
            == "This attribute defines how the event debounce algorithm will behave, if a related enable condition is not fulfilled or ControlDTCSetting of the related event is disabled."
        )
        assert (
            inspect.cleandoc(DiagnosticDebounceAlgorithmProps.setDebounceBehavior.__doc__)
            == "This attribute defines how the event debounce algorithm will behave, if a related enable condition is not fulfilled or ControlDTCSetting of the related event is disabled.\nA None value is a no-op and does not overwrite an existing debounceBehavior."
        )
        assert (
            inspect.cleandoc(DiagnosticDebounceAlgorithmProps.getDebounceCounterStorage.__doc__)
            == "Switch to store the debounce counter value non-volatile or not. true: debounce counter value shall be stored non-volatile false: debounce counter value is volatile Please note that this attribute is not relevant for the adaptive platform."
        )
        assert (
            inspect.cleandoc(DiagnosticDebounceAlgorithmProps.setDebounceCounterStorage.__doc__)
            == "Switch to store the debounce counter value non-volatile or not. true: debounce counter value shall be stored non-volatile false: debounce counter value is volatile Please note that this attribute is not relevant for the adaptive platform.\nA None value is a no-op and does not overwrite an existing debounceCounterStorage."
        )


class TestDiagnosticFunctionInhibitSource:
    """
    Test class for DiagnosticFunctionInhibitSource functionality.

    Spec: AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf, Table 4.216, p.216
    """

    CLASS_NOTE = "This meta-class represents the ability to define an inhibition source in the context of the Fim configuration."
    EVENT_NOTE = "This represents the alias event applicable for the referencing inhibition source."
    EVENT_GROUP_NOTE = "This represents the event group applicable for the referencing inhibition source."

    def _make_obj(self) -> DiagnosticFunctionInhibitSource:
        return DiagnosticFunctionInhibitSource(AUTOSAR.getInstance(), "InhibitSource1")

    def test_subclass_chain(self):
        """
        Test that DiagnosticFunctionInhibitSource derives from Identifiable.
        """
        assert issubclass(DiagnosticFunctionInhibitSource, Identifiable)

    def test_initialization_defaults(self):
        """
        Test that DiagnosticFunctionInhibitSource is initialized with the spec defaults.
        """
        obj = self._make_obj()

        assert obj.getShortName() == "InhibitSource1"
        assert obj.getEventRef() is None
        assert obj.getEventGroupRef() is None

    def test_class_docstring_is_spec_note_verbatim(self):
        """
        Test that the class docstring is the spec Note verbatim.
        """
        assert DiagnosticFunctionInhibitSource.__doc__ == self.CLASS_NOTE

    def test_init_has_no_docstring(self):
        """
        Test that __init__ carries no docstring.
        """
        assert DiagnosticFunctionInhibitSource.__init__.__doc__ is None

    def test_get_set_event_ref(self):
        """
        Setter returns self, value round-trips, None is a no-op.
        """
        obj = self._make_obj()

        value = RefType().setValue("/Fim/DiagnosticFimAliasEvents/AliasEvent1")
        result = obj.setEventRef(value)
        assert result is obj  # method chaining
        assert obj.getEventRef() is value
        assert obj.getEventRef().getValue() == "/Fim/DiagnosticFimAliasEvents/AliasEvent1"

        obj.setEventRef(None)
        assert obj.getEventRef() is value  # None is a no-op

    def test_get_set_event_group_ref(self):
        """
        Setter returns self, value round-trips, None is a no-op.
        """
        obj = self._make_obj()

        value = RefType().setValue("/Fim/DiagnosticFimAliasEventGroups/AliasEventGroup1")
        result = obj.setEventGroupRef(value)
        assert result is obj  # method chaining
        assert obj.getEventGroupRef() is value
        assert obj.getEventGroupRef().getValue() == "/Fim/DiagnosticFimAliasEventGroups/AliasEventGroup1"

        obj.setEventGroupRef(None)
        assert obj.getEventGroupRef() is value  # None is a no-op

    def test_get_set_type_hints(self):
        """
        Pin the accessor annotations to the spec types (Rule 0003).
        """
        setter_hints = typing.get_type_hints(DiagnosticFunctionInhibitSource.setEventRef)
        assert setter_hints.get("value") == typing.Optional[RefType]
        assert setter_hints.get("return") is DiagnosticFunctionInhibitSource

        getter_hints = typing.get_type_hints(DiagnosticFunctionInhibitSource.getEventRef)
        assert getter_hints.get("return") == typing.Optional[RefType]

        setter_hints = typing.get_type_hints(DiagnosticFunctionInhibitSource.setEventGroupRef)
        assert setter_hints.get("value") == typing.Optional[RefType]
        assert setter_hints.get("return") is DiagnosticFunctionInhibitSource

        getter_hints = typing.get_type_hints(DiagnosticFunctionInhibitSource.getEventGroupRef)
        assert getter_hints.get("return") == typing.Optional[RefType]

    def test_accessor_docstrings_are_spec_notes_verbatim(self):
        """
        Accessor docstrings carry the spec Note verbatim (setter + None-no-op sentence).
        """
        assert inspect.cleandoc(DiagnosticFunctionInhibitSource.getEventRef.__doc__) == self.EVENT_NOTE
        assert inspect.cleandoc(DiagnosticFunctionInhibitSource.setEventRef.__doc__) == (self.EVENT_NOTE + "\nA None value is a no-op and does not overwrite an existing eventRef.")
        assert inspect.cleandoc(DiagnosticFunctionInhibitSource.getEventGroupRef.__doc__) == self.EVENT_GROUP_NOTE
        assert inspect.cleandoc(DiagnosticFunctionInhibitSource.setEventGroupRef.__doc__) == (self.EVENT_GROUP_NOTE + "\nA None value is a no-op and does not overwrite an existing eventGroupRef.")


class TestDdsCpTopic:
    """
    Test class for DdsCpTopic functionality.

    Spec: AUTOSAR_CP_TPS_SystemTemplate.pdf, Table 6.177, p.527
    """

    CLASS_NOTE = "Definition of a DDS Partition. Tags: atp.Status=candidate"
    DDS_PARTITION_NOTE = "Reference to the DDS Partition this topic is communicated. Tags: atp.Status=candidate"
    TOPIC_NAME_NOTE = "Definition of the DDS Topic Name. Tags: atp.Status=candidate"

    def _create_topic(self) -> DdsCpTopic:
        return DdsCpTopic(AUTOSAR.getInstance(), "Topic1")

    def test_initialization(self):
        """
        Test that a new DdsCpTopic initializes all attributes to their defaults.
        """
        obj = self._create_topic()

        assert obj.getShortName() == "Topic1"
        assert obj.getDdsPartitionRef() is None
        assert obj.getTopicName() is None

    def test_is_identifiable_subclass(self):
        """
        Test that DdsCpTopic derives from Identifiable (Base column most-derived synced class).
        """
        assert issubclass(DdsCpTopic, Identifiable)
        assert issubclass(DdsCpTopic, ARObject)

    def test_class_docstring_is_spec_note_verbatim(self):
        """
        Test that the class docstring is the spec Note verbatim (the spec Note itself says "DDS Partition" — copied as rendered).
        """
        assert inspect.cleandoc(DdsCpTopic.__doc__) == self.CLASS_NOTE

    def test_init_has_no_docstring(self):
        """
        Test that __init__ carries no docstring.
        """
        assert DdsCpTopic.__init__.__doc__ is None

    def test_get_set_dds_partition_ref(self):
        """
        Test getDdsPartitionRef and setDdsPartitionRef round-trip and None no-op.
        """
        obj = self._create_topic()

        value = RefType().setDest("DDS-CP-PARTITION").setValue("/DdsCpConfig/Domains/Domain1/Partitions/Partition1")
        result = obj.setDdsPartitionRef(value)
        assert result is obj  # method chaining
        assert obj.getDdsPartitionRef() is value
        assert obj.getDdsPartitionRef().getValue() == "/DdsCpConfig/Domains/Domain1/Partitions/Partition1"
        assert obj.getDdsPartitionRef().getDest() == "DDS-CP-PARTITION"

        result = obj.setDdsPartitionRef(None)
        assert result is obj  # method chaining with None
        assert obj.getDdsPartitionRef() is value  # None is a no-op

    def test_get_set_topic_name(self):
        """
        Test getTopicName and setTopicName round-trip and None no-op.
        """
        obj = self._create_topic()

        value = String().setValue("MyDdsTopic")
        result = obj.setTopicName(value)
        assert result is obj  # method chaining
        assert obj.getTopicName() is value
        assert obj.getTopicName().getValue() == "MyDdsTopic"

        result = obj.setTopicName(None)
        assert result is obj  # method chaining with None
        assert obj.getTopicName() is value  # None is a no-op

    def test_accessor_docstrings_are_spec_notes_verbatim(self):
        """
        Getter and setter docstrings carry the spec Note verbatim (setter + None-no-op sentence).
        """
        assert inspect.cleandoc(DdsCpTopic.getDdsPartitionRef.__doc__) == self.DDS_PARTITION_NOTE
        assert inspect.cleandoc(DdsCpTopic.setDdsPartitionRef.__doc__) == (self.DDS_PARTITION_NOTE + "\n\nA None value is a no-op and does not overwrite an existing ddsPartitionRef.")
        assert inspect.cleandoc(DdsCpTopic.getTopicName.__doc__) == self.TOPIC_NAME_NOTE
        assert inspect.cleandoc(DdsCpTopic.setTopicName.__doc__) == (self.TOPIC_NAME_NOTE + "\n\nA None value is a no-op and does not overwrite an existing topicName.")


class TestDdsCpQosProfile:
    """
    Test class for DdsCpQosProfile functionality.

    Spec: AUTOSAR_CP_TPS_SystemTemplate.pdf, Table 6.179, p.529
    """

    CLASS_NOTE = "Definition of a DDS QOS Profile. Tags: atp.Status=candidate"

    # Attribute Note cells verbatim, in the displayed row order of Table 6.179.
    NOTES = {
        "Deadline": "Defines the DDS DEADLINE QoS policy. Tags: atp.Status=candidate",
        "DestinationOrder": "Defines the DDS DESTINATION_ORDER QoS policy.",
        "Durability": "Defines the DDS DURABILITY QoS policy. Tags: atp.Status=candidate",
        "DurabilityService": "Defines the DDS DURABILITY_SERVICE QoS policy. Tags: atp.Status=candidate",
        "History": "Defines the DDS HISTORY QoS policy.",
        "LatencyBudget": "Defines the DDS LATENCY_BUDGET QoS policy. Tags: atp.Status=candidate",
        "Lifespan": "Defines the DDS LIFESPAN QoS policy.",
        "Liveliness": "Defines the DDS LIVELINESS QoS policy. Tags: atp.Status=candidate",
        "Ownership": "Defines the DDS OWNERSHIP QoS policy. Tags: atp.Status=candidate",
        "OwnershipStrength": "Defines the DDS OWNERSHIP_STRENGTH QoS policy. Tags: atp.Status=candidate",
        "Reliability": "Defines the DDS RELIABILITY QoS policy.",
        "ResourceLimits": "Defines the DDS RESOURCE_LIMITS QoS policy.",
        "TopicData": "Defines the DDS TOPIC_DATA QoS policy.",
        "TransportPriority": "Defines the DDS TRANSPORT_PRIORITY QoS policy.",
    }

    FIELD_NAMES = [
        "Deadline",
        "DestinationOrder",
        "Durability",
        "DurabilityService",
        "History",
        "LatencyBudget",
        "Lifespan",
        "Liveliness",
        "Ownership",
        "OwnershipStrength",
        "Reliability",
        "ResourceLimits",
        "TopicData",
        "TransportPriority",
    ]

    def _create_profile(self) -> DdsCpQosProfile:
        return DdsCpQosProfile(AUTOSAR.getInstance(), "QosProfile1")

    def test_initialization(self):
        """
        Test that a new DdsCpQosProfile initializes all attributes to their defaults.
        """
        obj = self._create_profile()

        assert obj.getShortName() == "QosProfile1"
        assert obj.getDeadline() is None
        assert obj.getDestinationOrder() is None
        assert obj.getDurability() is None
        assert obj.getDurabilityService() is None
        assert obj.getHistory() is None
        assert obj.getLatencyBudget() is None
        assert obj.getLifespan() is None
        assert obj.getLiveliness() is None
        assert obj.getOwnership() is None
        assert obj.getOwnershipStrength() is None
        assert obj.getReliability() is None
        assert obj.getResourceLimits() is None
        assert obj.getTopicData() is None
        assert obj.getTransportPriority() is None

    def test_is_identifiable_subclass(self):
        """
        Test that DdsCpQosProfile derives from Identifiable (Base column most-derived synced class).
        """
        assert issubclass(DdsCpQosProfile, Identifiable)
        assert issubclass(DdsCpQosProfile, ARObject)

    def test_class_docstring_is_spec_note_verbatim(self):
        """
        Test that the class docstring is the spec Note verbatim.
        """
        assert inspect.cleandoc(DdsCpQosProfile.__doc__) == self.CLASS_NOTE

    def test_init_has_no_docstring(self):
        """
        Test that __init__ carries no docstring.
        """
        assert DdsCpQosProfile.__init__.__doc__ is None

    def test_accessor_names(self):
        """
        Test that the 14 spec accessor pairs exist under their spec-derived names (Table 6.179 row order).
        """
        for name in (
            "getDeadline",
            "setDeadline",
            "getDestinationOrder",
            "setDestinationOrder",
            "getDurability",
            "setDurability",
            "getDurabilityService",
            "setDurabilityService",
            "getHistory",
            "setHistory",
            "getLatencyBudget",
            "setLatencyBudget",
            "getLifespan",
            "setLifespan",
            "getLiveliness",
            "setLiveliness",
            "getOwnership",
            "setOwnership",
            "getOwnershipStrength",
            "setOwnershipStrength",
            "getReliability",
            "setReliability",
            "getResourceLimits",
            "setResourceLimits",
            "getTopicData",
            "setTopicData",
            "getTransportPriority",
            "setTransportPriority",
        ):
            assert hasattr(DdsCpQosProfile, name), name

    def test_get_set_pairs_round_trip_and_none_no_op(self):
        """
        Every 0..1 aggr attribute: setter returns self, value round-trips, setXxx(None) is a no-op.
        """
        obj = self._create_profile()

        values = {
            "Deadline": DdsDeadline(),
            "DestinationOrder": DdsDestinationOrder(),
            "Durability": DdsDurability(),
            "DurabilityService": DdsDurabilityService(),
            "History": DdsHistory(),
            "LatencyBudget": DdsLatencyBudget(),
            "Lifespan": DdsLifespan(),
            "Liveliness": DdsLiveliness(),
            "Ownership": DdsOwnership(),
            "OwnershipStrength": DdsOwnershipStrength(),
            "Reliability": DdsReliability(),
            "ResourceLimits": DdsResourceLimits(),
            "TopicData": DdsTopicData(),
            "TransportPriority": DdsTransportPriority(),
        }
        for name in self.FIELD_NAMES:
            getter = getattr(obj, f"get{name}")
            setter = getattr(obj, f"set{name}")
            value = values[name]
            assert setter(value) is obj  # method chaining
            assert getter() is value

            assert setter(None) is obj  # None is a no-op
            assert getter() is value

    def test_accessor_docstrings_are_spec_notes_verbatim(self):
        """
        Getter and setter docstrings carry the spec Note verbatim (setter + None-no-op sentence).
        """
        for name in self.FIELD_NAMES:
            getter = getattr(DdsCpQosProfile, f"get{name}")
            setter = getattr(DdsCpQosProfile, f"set{name}")
            field_name = name[0].lower() + name[1:]
            assert inspect.cleandoc(getter.__doc__) == self.NOTES[name], name
            assert inspect.cleandoc(setter.__doc__) == (self.NOTES[name] + f"\n\nA None value is a no-op and does not overwrite an existing {field_name}."), name


class TestDdsCpServiceInstance:
    """
    Test class for DdsCpServiceInstance functionality.

    Spec: AUTOSAR_CP_TPS_SystemTemplate.pdf, Table 6.152, p.472 (abstract; Base most-derived
    synced = Identifiable — AbstractServiceInstance is cycle-blocked from Identifiable.py,
    wave-1 DdsCp* precedent 0babf1fb0). Concrete subclass DdsCpConsumedServiceInstance is
    used where an instance is required.
    """

    CLASS_NOTE = "Provided and Consumed Dds Service Instances that are available at the ApplicationEndpoint. Tags: atp.Status=candidate"
    FIELD_REPLY_NOTE = "Reference to the DdsTopic used as fragment for the topic name of field setters. Tags: atp.Status=candidate"
    FIELD_REQUEST_NOTE = "Reference to the DdsTopic used as fragment for the topic name of field getters. Tags: atp.Status=candidate"
    METHOD_REPLY_NOTE = "Reference to the DdsTopic used as fragment for the topic name of method replies. Tags: atp.Status=candidate"
    METHOD_REQUEST_NOTE = "Reference to the DdsTopic used as fragment for the topic name of method requests. Tags: atp.Status=candidate"
    QOS_PROFILE_NOTE = "Reference to the QOS Profile used for the service. Tags: atp.Status=candidate"
    INSTANCE_ID_NOTE = "Identification number that is used by DDS to identify DomainParticipants associated with an instance of the service. Tags: atp.Status=candidate"
    INTERFACE_ID_NOTE = "Unique Identifier that identifies the ServiceInterface in DDS. This Identifier is encoded in the USER_DATA QoS of the DomainParticipant associated with the Service Instance and its value is propagated by DDS Discovery messages. Tags: atp.Status=candidate"

    def _create_instance(self):
        return DdsCpConsumedServiceInstance(AUTOSAR.getInstance(), "DdsInstance1")

    def test_abstract_instantiation_blocked(self):
        """
        Test that the abstract DdsCpServiceInstance cannot be instantiated directly.
        """
        with pytest.raises(TypeError):
            DdsCpServiceInstance(AUTOSAR.getInstance(), "Abstract1")

    def test_subclass_inherits_identifiable(self):
        """
        Test that DdsCpServiceInstance derives from Identifiable and the concrete subclass inherits it.
        """
        assert issubclass(DdsCpServiceInstance, Identifiable)
        assert issubclass(DdsCpServiceInstance, ARObject)
        assert issubclass(DdsCpConsumedServiceInstance, DdsCpServiceInstance)

    def test_initialization(self):
        """
        Test that a new DdsCpServiceInstance subclass initializes all attributes to their defaults.
        """
        obj = self._create_instance()

        assert obj.getShortName() == "DdsInstance1"
        assert obj.getDdsFieldReplyTopicRef() is None
        assert obj.getDdsFieldRequestTopicRef() is None
        assert obj.getDdsMethodReplyTopicRef() is None
        assert obj.getDdsMethodRequestTopicRef() is None
        assert obj.getDdsServiceQosProfileRef() is None
        assert obj.getServiceInstanceId() is None
        assert obj.getServiceInterfaceId() is None

    def test_class_docstring_is_spec_note_verbatim(self):
        """
        Test that the class docstring is the spec Note verbatim.
        """
        assert inspect.cleandoc(DdsCpServiceInstance.__doc__) == self.CLASS_NOTE

    def test_init_has_no_docstring(self):
        """
        Test that __init__ carries no docstring.
        """
        assert DdsCpServiceInstance.__init__.__doc__ is None

    def _check_ref(self, getter_name, setter_name, dest):
        obj = self._create_instance()
        getter = getattr(obj, getter_name)
        setter = getattr(obj, setter_name)
        value = RefType().setDest(dest).setValue("/DdsCpConfig/Topics/Topic1")
        assert setter(value) is obj
        assert getter() is value
        assert getter().getDest() == dest
        assert setter(None) is obj
        assert getter() is value

    def test_get_set_dds_field_reply_topic_ref(self):
        """Test get/setDdsFieldReplyTopicRef round-trip and None no-op."""
        self._check_ref("getDdsFieldReplyTopicRef", "setDdsFieldReplyTopicRef", "DDS-CP-TOPIC")

    def test_get_set_dds_field_request_topic_ref(self):
        """Test get/setDdsFieldRequestTopicRef round-trip and None no-op."""
        self._check_ref("getDdsFieldRequestTopicRef", "setDdsFieldRequestTopicRef", "DDS-CP-TOPIC")

    def test_get_set_dds_method_reply_topic_ref(self):
        """Test get/setDdsMethodReplyTopicRef round-trip and None no-op."""
        self._check_ref("getDdsMethodReplyTopicRef", "setDdsMethodReplyTopicRef", "DDS-CP-TOPIC")

    def test_get_set_dds_method_request_topic_ref(self):
        """Test get/setDdsMethodRequestTopicRef round-trip and None no-op."""
        self._check_ref("getDdsMethodRequestTopicRef", "setDdsMethodRequestTopicRef", "DDS-CP-TOPIC")

    def test_get_set_dds_service_qos_profile_ref(self):
        """Test get/setDdsServiceQosProfileRef round-trip and None no-op."""
        self._check_ref("getDdsServiceQosProfileRef", "setDdsServiceQosProfileRef", "DDS-CP-QOS-PROFILE")

    def test_get_set_service_instance_id(self):
        """
        Test getServiceInstanceId/setServiceInstanceId round-trip and None no-op.
        """
        obj = self._create_instance()
        value = PositiveInteger().setValue("42")
        assert obj.setServiceInstanceId(value) is obj
        assert obj.getServiceInstanceId() is value
        assert obj.getServiceInstanceId().getValue() == 42
        obj.setServiceInstanceId(None)
        assert obj.getServiceInstanceId() is value

    def test_get_set_service_interface_id(self):
        """
        Test getServiceInterfaceId/setServiceInterfaceId round-trip and None no-op.
        """
        obj = self._create_instance()
        value = String().setValue("MyServiceInterface")
        assert obj.setServiceInterfaceId(value) is obj
        assert obj.getServiceInterfaceId() is value
        assert obj.getServiceInterfaceId().getValue() == "MyServiceInterface"
        obj.setServiceInterfaceId(None)
        assert obj.getServiceInterfaceId() is value

    def test_type_annotations(self):
        """
        Getter returns and setter parameters match the spec multiplicity (all 0..1 → Optional).
        """
        assert typing.get_type_hints(DdsCpServiceInstance.setDdsFieldReplyTopicRef)["value"] == typing.Optional[RefType]
        assert typing.get_type_hints(DdsCpServiceInstance.setDdsServiceQosProfileRef)["value"] == typing.Optional[RefType]
        assert typing.get_type_hints(DdsCpServiceInstance.setServiceInstanceId)["value"] == typing.Optional[PositiveInteger]
        assert typing.get_type_hints(DdsCpServiceInstance.setServiceInterfaceId)["value"] == typing.Optional[String]
        assert typing.get_type_hints(DdsCpServiceInstance.getServiceInterfaceId)["return"] == typing.Optional[String]

    def test_accessor_docstrings_are_spec_notes_verbatim(self):
        """
        Getter and setter docstrings carry the spec Note verbatim (setter + None-no-op sentence).
        """
        pairs = [
            ("DdsFieldReplyTopicRef", self.FIELD_REPLY_NOTE),
            ("DdsFieldRequestTopicRef", self.FIELD_REQUEST_NOTE),
            ("DdsMethodReplyTopicRef", self.METHOD_REPLY_NOTE),
            ("DdsMethodRequestTopicRef", self.METHOD_REQUEST_NOTE),
            ("DdsServiceQosProfileRef", self.QOS_PROFILE_NOTE),
            ("ServiceInstanceId", self.INSTANCE_ID_NOTE),
            ("ServiceInterfaceId", self.INTERFACE_ID_NOTE),
        ]
        for suffix, note in pairs:
            getter = getattr(DdsCpServiceInstance, f"get{suffix}")
            setter = getattr(DdsCpServiceInstance, f"set{suffix}")
            field_name = suffix[0].lower() + suffix[1:]
            assert inspect.cleandoc(getter.__doc__) == note, suffix
            assert inspect.cleandoc(setter.__doc__) == (note + f"\n\nA None value is a no-op and does not overwrite an existing {field_name}."), suffix


class TestDdsCpConsumedServiceInstance:
    """
    Test class for DdsCpConsumedServiceInstance functionality.

    Spec: AUTOSAR_CP_TPS_SystemTemplate.pdf, Table 6.154, p.475
    """

    CLASS_NOTE = "This meta-class represents the ability to describe the existence and configuration of a consumed (required) service instance in a concrete implementation on top of DDS. Tags: atp.Status=candidate"
    OPERATIONS_NOTE = (
        "Collection of consumed operations. Stereotypes: atpSplitable; atpVariation Tags: atp.Splitkey=consumedDdsOperation, consumedDds Operation.variationPoint.shortLabel atp.Status=candidate"
    )
    EVENTS_NOTE = "Collection of consumed events. Stereotypes: atpSplitable; atpVariation Tags: atp.Splitkey=consumedDdsServiceEvent, consumedDds ServiceEvent.variationPoint.shortLabel atp.Status=candidate vh.latestBindingTime=systemDesignTime"
    LOCAL_UNICAST_NOTE = "The local address over which the Service is consumed. Stereotypes: atpSplitable; atpVariation Tags: atp.Splitkey=localUnicastAddress.applicationEndpoint, localUnicastAddress.variationPoint.shortLabel atp.Status=candidate vh.latestBindingTime=systemDesignTime xml.namePlural=LOCAL-UNICAST-ADDRESSES"
    MINOR_VERSION_NOTE = "Minor Version of the ServiceInterface. Value can be set to a number that represents the Minor Version of the searched service or to ANY."
    MULTICAST_NOTE = "This reference defines the remote multicast address of the Service provider. This reference shall ONLY be used if the remote multicast address of the server is determined from the configuration and not at runtime. Stereotypes: atpSplitable; atpVariation Tags: atp.Splitkey=staticRemoteMulticastAddress.application Endpoint, staticRemoteMulticastAddress.variation Point.shortLabel atp.Status=candidate vh.latestBindingTime=systemDesignTime xml.namePlural=STATIC-REMOTE-MULTICAST-ADDRESSES"
    UNICAST_NOTE = "This reference defines the remote unicast address of the Service provider. This reference shall ONLY be used if the remote unicast address of the server is determined from the configuration and not at runtime. Stereotypes: atpSplitable; atpVariation Tags: atp.Splitkey=staticRemoteUnicastAddress.application Endpoint, staticRemoteUnicastAddress.variation Point.shortLabel atp.Status=candidate vh.latestBindingTime=systemDesignTime xml.namePlural=STATIC-REMOTE-UNICAST-ADDRESSES"

    def _create_instance(self) -> DdsCpConsumedServiceInstance:
        return DdsCpConsumedServiceInstance(AUTOSAR.getInstance(), "ConsumedInstance1")

    def test_initialization(self):
        """
        Test that a new DdsCpConsumedServiceInstance initializes all attributes to their defaults.
        """
        obj = self._create_instance()

        assert obj.getShortName() == "ConsumedInstance1"
        assert obj.getConsumedDdsOperations() == []
        assert obj.getConsumedDdsServiceEvents() == []
        assert obj.getLocalUnicastAddressRef() is None
        assert obj.getMinorVersion() is None
        assert obj.getStaticRemoteMulticastAddressRef() is None
        assert obj.getStaticRemoteUnicastAddressRef() is None

    def test_is_concrete_subclass_of_base(self):
        """
        Test that DdsCpConsumedServiceInstance derives from DdsCpServiceInstance and is concrete.
        """
        assert issubclass(DdsCpConsumedServiceInstance, DdsCpServiceInstance)
        assert issubclass(DdsCpConsumedServiceInstance, Identifiable)
        assert issubclass(DdsCpConsumedServiceInstance, ARObject)
        obj = self._create_instance()
        assert isinstance(obj, DdsCpServiceInstance)

    def test_class_docstring_is_spec_note_verbatim(self):
        """
        Test that the class docstring is the spec Note verbatim.
        """
        assert inspect.cleandoc(DdsCpConsumedServiceInstance.__doc__) == self.CLASS_NOTE

    def test_init_has_no_docstring(self):
        """
        Test that __init__ carries no docstring.
        """
        assert DdsCpConsumedServiceInstance.__init__.__doc__ is None

    def test_add_get_consumed_dds_operations(self):
        """
        Test addConsumedDdsOperation appends and getConsumedDdsOperations returns the list; None is a no-op.
        """
        obj = self._create_instance()

        operation = DdsCpServiceInstanceOperation()
        operation.setDdsOperationRequestTriggeringRef(RefType().setDest("IDENTIFIABLE").setValue("/Swc/InternTrigger1"))
        result = obj.addConsumedDdsOperation(operation)
        assert result is obj
        assert obj.getConsumedDdsOperations() == [operation]
        assert obj.getConsumedDdsOperations()[0].getDdsOperationRequestTriggeringRef().getValue() == "/Swc/InternTrigger1"

        assert obj.addConsumedDdsOperation(None) is obj
        assert obj.getConsumedDdsOperations() == [operation]

    def test_add_get_consumed_dds_service_events(self):
        """
        Test addConsumedDdsServiceEvent appends and getConsumedDdsServiceEvents returns the list; None is a no-op.
        """
        obj = self._create_instance()

        event = DdsCpServiceInstanceEvent()
        event.setDdsEventRef(RefType().setDest("IDENTIFIABLE").setValue("/Swc/Event1"))
        result = obj.addConsumedDdsServiceEvent(event)
        assert result is obj
        assert obj.getConsumedDdsServiceEvents() == [event]
        assert obj.getConsumedDdsServiceEvents()[0].getDdsEventRef().getValue() == "/Swc/Event1"

        assert obj.addConsumedDdsServiceEvent(None) is obj
        assert obj.getConsumedDdsServiceEvents() == [event]

    def test_get_set_local_unicast_address_ref(self):
        """
        Test get/setLocalUnicastAddressRef round-trip and None no-op.
        """
        obj = self._create_instance()

        value = RefType().setDest("APPLICATION-ENDPOINT").setValue("/Cluster/Connector/Endpoint1")
        result = obj.setLocalUnicastAddressRef(value)
        assert result is obj
        assert obj.getLocalUnicastAddressRef() is value
        assert obj.getLocalUnicastAddressRef().getValue() == "/Cluster/Connector/Endpoint1"
        assert obj.getLocalUnicastAddressRef().getDest() == "APPLICATION-ENDPOINT"

        result = obj.setLocalUnicastAddressRef(None)
        assert result is obj
        assert obj.getLocalUnicastAddressRef() is value

    def test_get_set_minor_version(self):
        """
        Test get/setMinorVersion round-trip and None no-op (AnyVersionString "2" and "ANY").
        """
        obj = self._create_instance()

        value = AnyVersionString().setValue("2")
        result = obj.setMinorVersion(value)
        assert result is obj
        assert obj.getMinorVersion() is value
        assert obj.getMinorVersion().getValue() == "2"

        any_value = AnyVersionString().setValue("ANY")
        obj.setMinorVersion(any_value)
        assert obj.getMinorVersion().getValue() == "ANY"

        result = obj.setMinorVersion(None)
        assert result is obj
        assert obj.getMinorVersion() is any_value

    def test_get_set_static_remote_multicast_address_ref(self):
        """
        Test get/setStaticRemoteMulticastAddressRef round-trip and None no-op.
        """
        obj = self._create_instance()

        value = RefType().setDest("APPLICATION-ENDPOINT").setValue("/Cluster/Connector/MulticastEndpoint")
        result = obj.setStaticRemoteMulticastAddressRef(value)
        assert result is obj
        assert obj.getStaticRemoteMulticastAddressRef() is value
        assert obj.getStaticRemoteMulticastAddressRef().getValue() == "/Cluster/Connector/MulticastEndpoint"

        result = obj.setStaticRemoteMulticastAddressRef(None)
        assert result is obj
        assert obj.getStaticRemoteMulticastAddressRef() is value

    def test_get_set_static_remote_unicast_address_ref(self):
        """
        Test get/setStaticRemoteUnicastAddressRef round-trip and None no-op (Table 6.154 Mult 0..1 — single ref).
        """
        obj = self._create_instance()

        value = RefType().setDest("APPLICATION-ENDPOINT").setValue("/Cluster/Connector/UnicastEndpoint")
        result = obj.setStaticRemoteUnicastAddressRef(value)
        assert result is obj
        assert obj.getStaticRemoteUnicastAddressRef() is value
        assert obj.getStaticRemoteUnicastAddressRef().getValue() == "/Cluster/Connector/UnicastEndpoint"

        result = obj.setStaticRemoteUnicastAddressRef(None)
        assert result is obj
        assert obj.getStaticRemoteUnicastAddressRef() is value

    def test_inherited_base_accessors(self):
        """
        Test that the inherited DdsCpServiceInstance group members still round-trip on the subclass.
        """
        obj = self._create_instance()
        value = PositiveInteger().setValue("7")
        assert obj.setServiceInstanceId(value) is obj
        assert obj.getServiceInstanceId() is value

    def test_type_annotations(self):
        """
        Getter returns and setter parameters match the spec multiplicity (lists for `*`, Optional for 0..1).
        """
        assert typing.get_type_hints(DdsCpConsumedServiceInstance.addConsumedDdsOperation)["value"] == typing.Optional[DdsCpServiceInstanceOperation]
        assert typing.get_type_hints(DdsCpConsumedServiceInstance.getConsumedDdsOperations)["return"] == typing.List[DdsCpServiceInstanceOperation]
        assert typing.get_type_hints(DdsCpConsumedServiceInstance.addConsumedDdsServiceEvent)["value"] == typing.Optional[DdsCpServiceInstanceEvent]
        assert typing.get_type_hints(DdsCpConsumedServiceInstance.getConsumedDdsServiceEvents)["return"] == typing.List[DdsCpServiceInstanceEvent]
        assert typing.get_type_hints(DdsCpConsumedServiceInstance.setLocalUnicastAddressRef)["value"] == typing.Optional[RefType]
        assert typing.get_type_hints(DdsCpConsumedServiceInstance.getLocalUnicastAddressRef)["return"] == typing.Optional[RefType]
        assert typing.get_type_hints(DdsCpConsumedServiceInstance.setMinorVersion)["value"] == typing.Optional[AnyVersionString]
        assert typing.get_type_hints(DdsCpConsumedServiceInstance.getMinorVersion)["return"] == typing.Optional[AnyVersionString]
        assert typing.get_type_hints(DdsCpConsumedServiceInstance.setStaticRemoteMulticastAddressRef)["value"] == typing.Optional[RefType]
        assert typing.get_type_hints(DdsCpConsumedServiceInstance.setStaticRemoteUnicastAddressRef)["value"] == typing.Optional[RefType]

    def test_accessor_docstrings_are_spec_notes_verbatim(self):
        """
        Getter and setter docstrings carry the spec Note verbatim (setter/add + None-no-op sentence).
        """
        assert inspect.cleandoc(DdsCpConsumedServiceInstance.addConsumedDdsOperation.__doc__) == (
            self.OPERATIONS_NOTE + "\n\nA None value is a no-op and does not extend the consumedDdsOperations list."
        )
        assert inspect.cleandoc(DdsCpConsumedServiceInstance.getConsumedDdsOperations.__doc__) == self.OPERATIONS_NOTE
        assert inspect.cleandoc(DdsCpConsumedServiceInstance.addConsumedDdsServiceEvent.__doc__) == (
            self.EVENTS_NOTE + "\n\nA None value is a no-op and does not extend the consumedDdsServiceEvents list."
        )
        assert inspect.cleandoc(DdsCpConsumedServiceInstance.getConsumedDdsServiceEvents.__doc__) == self.EVENTS_NOTE
        assert inspect.cleandoc(DdsCpConsumedServiceInstance.getLocalUnicastAddressRef.__doc__) == self.LOCAL_UNICAST_NOTE
        assert inspect.cleandoc(DdsCpConsumedServiceInstance.setLocalUnicastAddressRef.__doc__) == (
            self.LOCAL_UNICAST_NOTE + "\n\nA None value is a no-op and does not overwrite an existing localUnicastAddressRef."
        )
        assert inspect.cleandoc(DdsCpConsumedServiceInstance.getMinorVersion.__doc__) == self.MINOR_VERSION_NOTE
        assert inspect.cleandoc(DdsCpConsumedServiceInstance.setMinorVersion.__doc__) == (self.MINOR_VERSION_NOTE + "\n\nA None value is a no-op and does not overwrite an existing minorVersion.")
        assert inspect.cleandoc(DdsCpConsumedServiceInstance.getStaticRemoteMulticastAddressRef.__doc__) == self.MULTICAST_NOTE
        assert inspect.cleandoc(DdsCpConsumedServiceInstance.setStaticRemoteMulticastAddressRef.__doc__) == (
            self.MULTICAST_NOTE + "\n\nA None value is a no-op and does not overwrite an existing staticRemoteMulticastAddressRef."
        )
        assert inspect.cleandoc(DdsCpConsumedServiceInstance.getStaticRemoteUnicastAddressRef.__doc__) == self.UNICAST_NOTE
        assert inspect.cleandoc(DdsCpConsumedServiceInstance.setStaticRemoteUnicastAddressRef.__doc__) == (
            self.UNICAST_NOTE + "\n\nA None value is a no-op and does not overwrite an existing staticRemoteUnicastAddressRef."
        )


class TestDdsCpDomain:
    """
    Test class for DdsCpDomain functionality.

    Spec: AUTOSAR_CP_TPS_SystemTemplate.pdf, Table 6.176, p.526
    """

    CLASS_NOTE = "Definition of a DDS Domain. Tags: atp.Status=candidate"
    DDS_PARTITION_NOTE = "Collection of DDS Partition definitions. Tags: atp.Status=candidate"
    DDS_TOPIC_NOTE = "Collection of DDS Topics. Tags: atp.Status=candidate"
    DOMAIN_ID_NOTE = "Definition of the DDS Domain Id. Tags: atp.Status=candidate"

    def _create_domain(self) -> DdsCpDomain:
        return DdsCpDomain(AUTOSAR.getInstance(), "Domain1")

    def test_initialization(self):
        """
        Test that a new DdsCpDomain initializes all attributes to their defaults.
        """
        obj = self._create_domain()

        assert obj.getShortName() == "Domain1"
        assert obj.getDdsPartitions() == []
        assert obj.getDdsTopics() == []
        assert obj.getDomainId() is None

    def test_is_identifiable_subclass(self):
        """
        Test that DdsCpDomain derives from Identifiable (Base column most-derived class).
        """
        assert issubclass(DdsCpDomain, Identifiable)
        assert issubclass(DdsCpDomain, ARObject)

    def test_class_docstring_is_spec_note_verbatim(self):
        """
        Test that the class docstring is the spec Note verbatim.
        """
        assert inspect.cleandoc(DdsCpDomain.__doc__) == self.CLASS_NOTE

    def test_init_has_no_docstring(self):
        """
        Test that __init__ carries no docstring.
        """
        assert DdsCpDomain.__init__.__doc__ is None

    def test_create_dds_partition(self):
        """
        Test createDdsPartition appends a DdsCpPartition and returns the existing one for a duplicate short name.
        """
        obj = self._create_domain()

        partition = obj.createDdsPartition("Partition1")
        assert isinstance(partition, DdsCpPartition)
        assert partition.getShortName() == "Partition1"
        assert obj.getDdsPartitions() == [partition]

        duplicate = obj.createDdsPartition("Partition1")
        assert duplicate is partition
        assert len(obj.getDdsPartitions()) == 1

    def test_create_dds_topic(self):
        """
        Test createDdsTopic appends a DdsCpTopic and returns the existing one for a duplicate short name.
        """
        obj = self._create_domain()

        topic = obj.createDdsTopic("Topic1")
        assert isinstance(topic, DdsCpTopic)
        assert topic.getShortName() == "Topic1"
        assert obj.getDdsTopics() == [topic]

        duplicate = obj.createDdsTopic("Topic1")
        assert duplicate is topic
        assert len(obj.getDdsTopics()) == 1

    def test_get_set_domain_id(self):
        """
        Test get/setDomainId round-trip and None no-op.
        """
        obj = self._create_domain()

        value = PositiveInteger().setValue("1")
        result = obj.setDomainId(value)
        assert result is obj
        assert obj.getDomainId() is value
        assert obj.getDomainId().getValue() == 1

        result = obj.setDomainId(None)
        assert result is obj
        assert obj.getDomainId() is value

    def test_type_annotations(self):
        """
        Getter returns and setter parameters match the spec multiplicity (List for `*`, Optional for 0..1).
        """
        assert typing.get_type_hints(DdsCpDomain.createDdsPartition)["short_name"] is str
        assert typing.get_type_hints(DdsCpDomain.getDdsPartitions)["return"] == typing.List[DdsCpPartition]
        assert typing.get_type_hints(DdsCpDomain.createDdsTopic)["short_name"] is str
        assert typing.get_type_hints(DdsCpDomain.getDdsTopics)["return"] == typing.List[DdsCpTopic]
        assert typing.get_type_hints(DdsCpDomain.setDomainId)["value"] == typing.Optional[PositiveInteger]
        assert typing.get_type_hints(DdsCpDomain.getDomainId)["return"] == typing.Optional[PositiveInteger]

    def test_accessor_docstrings_are_spec_notes_verbatim(self):
        """
        Accessor docstrings carry the spec Note verbatim (setter + None-no-op sentence).
        """
        assert inspect.cleandoc(DdsCpDomain.createDdsPartition.__doc__) == self.DDS_PARTITION_NOTE
        assert inspect.cleandoc(DdsCpDomain.getDdsPartitions.__doc__) == self.DDS_PARTITION_NOTE
        assert inspect.cleandoc(DdsCpDomain.createDdsTopic.__doc__) == self.DDS_TOPIC_NOTE
        assert inspect.cleandoc(DdsCpDomain.getDdsTopics.__doc__) == self.DDS_TOPIC_NOTE
        assert inspect.cleandoc(DdsCpDomain.getDomainId.__doc__) == self.DOMAIN_ID_NOTE
        assert inspect.cleandoc(DdsCpDomain.setDomainId.__doc__) == (self.DOMAIN_ID_NOTE + "\n\nA None value is a no-op and does not overwrite an existing domainId.")


class TestDdsCpPartition:
    """
    Test class for DdsCpPartition functionality.

    Spec: AUTOSAR_CP_TPS_SystemTemplate.pdf, Table 6.178, p.527
    """

    CLASS_NOTE = "Definition of a DDS Partition. Tags: atp.Status=candidate"
    PARTITION_NAME_NOTE = "Definition of the DDS Partition Name. '*' may be used to define the default partition. Tags: atp.Status=candidate"

    def _create_partition(self) -> DdsCpPartition:
        return DdsCpPartition(AUTOSAR.getInstance(), "Partition1")

    def test_initialization(self):
        """
        Test that a new DdsCpPartition initializes all attributes to their defaults.
        """
        obj = self._create_partition()

        assert obj.getShortName() == "Partition1"
        assert obj.getPartitionName() is None

    def test_is_identifiable_subclass(self):
        """
        Test that DdsCpPartition derives from Identifiable (Base column most-derived class).
        """
        assert issubclass(DdsCpPartition, Identifiable)
        assert issubclass(DdsCpPartition, ARObject)

    def test_class_docstring_is_spec_note_verbatim(self):
        """
        Test that the class docstring is the spec Note verbatim.
        """
        assert inspect.cleandoc(DdsCpPartition.__doc__) == self.CLASS_NOTE

    def test_init_has_no_docstring(self):
        """
        Test that __init__ carries no docstring.
        """
        assert DdsCpPartition.__init__.__doc__ is None

    def test_get_set_partition_name(self):
        """
        Test get/setPartitionName round-trip and None no-op.
        """
        obj = self._create_partition()

        value = String().setValue("Partition_A")
        result = obj.setPartitionName(value)
        assert result is obj
        assert obj.getPartitionName() is value
        assert obj.getPartitionName().getValue() == "Partition_A"

        default = String().setValue("*")
        obj.setPartitionName(default)
        assert obj.getPartitionName().getValue() == "*"

        result = obj.setPartitionName(None)
        assert result is obj
        assert obj.getPartitionName() is default

    def test_type_annotations(self):
        """
        Getter returns and setter parameters match the spec multiplicity (0..1 → Optional).
        """
        assert typing.get_type_hints(DdsCpPartition.setPartitionName)["value"] == typing.Optional[String]
        assert typing.get_type_hints(DdsCpPartition.getPartitionName)["return"] == typing.Optional[String]

    def test_accessor_docstrings_are_spec_notes_verbatim(self):
        """
        Getter and setter docstrings carry the spec Note verbatim (setter + None-no-op sentence).
        """
        assert inspect.cleandoc(DdsCpPartition.getPartitionName.__doc__) == self.PARTITION_NAME_NOTE
        assert inspect.cleandoc(DdsCpPartition.setPartitionName.__doc__) == (self.PARTITION_NAME_NOTE + "\n\nA None value is a no-op and does not overwrite an existing partitionName.")


class ConcreteGlobalTimeMaster(GlobalTimeMaster):
    pass


class ConcreteGlobalTimeSlave(GlobalTimeSlave):
    pass


class TestGlobalTimeSlave:
    """
    Test class for GlobalTimeSlave functionality.

    Spec: AUTOSAR_CP_TPS_SystemTemplate.pdf, Table 9.5, p.861
    (abstract; subclasses GlobalTimeCanSlave, GlobalTimeEthSlave, GlobalTimeFrSlave and
    UserDefinedGlobalTimeSlave — exercised through a local concrete subclass per the
    abstract-class test convention.)
    """

    CLASS_NOTE = "This represents the generic concept of a global time slave."
    COMMUNICATION_CONNECTOR_REF_NOTE = "The GlobalTimeSlave is bound to the Communication Connector."
    FOLLOW_UP_TIMEOUT_VALUE_NOTE = "Rx timeout for the follow-up message."
    ICV_VERIFICATION_NOTE = "Defines how an Integrity Check Value (ICV) shall be handled at the receiver. Tags: atp.Status=candidate"
    TIME_LEAP_FUTURE_THRESHOLD_NOTE = "Defines the maximum allowed positive difference between the current Local Time Base value and a newly received Global Time Base value."
    TIME_LEAP_HEALING_COUNTER_NOTE = "Defines the required number of updates to the Time Base where the time difference to the previous received value has to remain within the bounds of timeLeapFutureThreshold and timeLeapPastThreshold until that Time Base is considered healed."
    TIME_LEAP_PAST_THRESHOLD_NOTE = "Defines the maximum allowed negative difference between the current Local Time Base value and a newly received Global Time Base value."

    def _create_slave(self) -> ConcreteGlobalTimeSlave:
        return ConcreteGlobalTimeSlave(AUTOSAR.getInstance(), "slave")

    def test_abstract_initialization(self):
        """
        GlobalTimeSlave is abstract and cannot be instantiated directly.
        """
        with pytest.raises(TypeError):
            GlobalTimeSlave(AUTOSAR.getInstance(), "slave")

    def test_is_identifiable_subclass_with_variation_point_capable(self):
        """
        Test that GlobalTimeSlave derives from Identifiable per the Table 9.5 Base row
        (ARObject, Identifiable, MultilanguageReferrable, Referrable — most-derived
        Identifiable) and from VariationPointCapable (the atpVariation on the owning
        GlobalTimeDomain.slave row makes the class VP-capable; the XSD GLOBAL-TIME-SLAVE
        group carries VARIATION-POINT last, xml.sequenceOffset=10000).
        """
        assert issubclass(GlobalTimeSlave, Identifiable)
        assert issubclass(GlobalTimeSlave, VariationPointCapable)

    def test_class_docstring_is_spec_note_verbatim(self):
        """
        Test that the class docstring is the spec Note verbatim.
        """
        assert inspect.cleandoc(GlobalTimeSlave.__doc__) == self.CLASS_NOTE

    def test_init_has_no_docstring(self):
        """
        Test that __init__ carries no docstring.
        """
        assert GlobalTimeSlave.__init__.__doc__ is None

    def test_member_order_follows_spec_rows(self):
        """
        Test that the accessors follow the Table 9.5 displayed row order (getter first per attribute).
        """
        methods = [name for name, value in GlobalTimeSlave.__dict__.items() if callable(value) and not name.startswith("_")]
        assert methods == [
            "getCommunicationConnectorRef",
            "setCommunicationConnectorRef",
            "getFollowUpTimeoutValue",
            "setFollowUpTimeoutValue",
            "getIcvVerification",
            "setIcvVerification",
            "getTimeLeapFutureThreshold",
            "setTimeLeapFutureThreshold",
            "getTimeLeapHealingCounter",
            "setTimeLeapHealingCounter",
            "getTimeLeapPastThreshold",
            "setTimeLeapPastThreshold",
        ]

    def test_initialization_defaults(self):
        """
        Test that a concrete subclass initializes all attributes to their defaults.
        """
        obj = self._create_slave()

        assert obj.getShortName() == "slave"
        assert obj.getChecksum() is None
        assert obj.getCommunicationConnectorRef() is None
        assert obj.getFollowUpTimeoutValue() is None
        assert obj.getIcvVerification() is None
        assert obj.getTimeLeapFutureThreshold() is None
        assert obj.getTimeLeapHealingCounter() is None
        assert obj.getTimeLeapPastThreshold() is None
        assert obj.getVariationPoint() is None

    def test_annotations_are_optional_typed(self):
        """
        Test that the accessors carry the spec types (0..1 rows).
        """
        hints = typing.get_type_hints(GlobalTimeSlave.getCommunicationConnectorRef)
        assert hints.get("return") == typing.Optional[RefType]
        hints = typing.get_type_hints(GlobalTimeSlave.setCommunicationConnectorRef)
        assert hints.get("value") == typing.Optional[RefType]
        assert hints.get("return") is GlobalTimeSlave

        hints = typing.get_type_hints(GlobalTimeSlave.getFollowUpTimeoutValue)
        assert hints.get("return") == typing.Optional[TimeValue]
        hints = typing.get_type_hints(GlobalTimeSlave.getIcvVerification)
        assert hints.get("return") == typing.Optional[GlobalTimeIcvVerificationEnum]
        hints = typing.get_type_hints(GlobalTimeSlave.getTimeLeapFutureThreshold)
        assert hints.get("return") == typing.Optional[TimeValue]
        hints = typing.get_type_hints(GlobalTimeSlave.getTimeLeapHealingCounter)
        assert hints.get("return") == typing.Optional[PositiveInteger]
        hints = typing.get_type_hints(GlobalTimeSlave.getTimeLeapPastThreshold)
        assert hints.get("return") == typing.Optional[TimeValue]

    def test_get_set_communication_connector_ref(self):
        """
        Test getCommunicationConnectorRef and setCommunicationConnectorRef round-trip and None no-op.
        """
        obj = self._create_slave()

        value = RefType()
        value.setValue("/CommunicationClusters/Cluster/Connector")
        result = obj.setCommunicationConnectorRef(value)
        assert result is obj
        assert obj.getCommunicationConnectorRef() is value
        assert obj.getCommunicationConnectorRef().getValue() == "/CommunicationClusters/Cluster/Connector"

        result = obj.setCommunicationConnectorRef(None)
        assert result is obj
        assert obj.getCommunicationConnectorRef() is value

    def test_get_set_follow_up_timeout_value(self):
        """
        Test getFollowUpTimeoutValue and setFollowUpTimeoutValue round-trip and None no-op.
        """
        obj = self._create_slave()

        value = TimeValue()
        value.setValue("0.05")
        result = obj.setFollowUpTimeoutValue(value)
        assert result is obj
        assert obj.getFollowUpTimeoutValue() is value

        result = obj.setFollowUpTimeoutValue(None)
        assert result is obj
        assert obj.getFollowUpTimeoutValue() is value

    def test_get_set_icv_verification(self):
        """
        Test getIcvVerification and setIcvVerification round-trip and None no-op.
        """
        obj = self._create_slave()

        value = GlobalTimeIcvVerificationEnum()
        value.setValue(GlobalTimeIcvVerificationEnum.ICV_VERIFIED)
        result = obj.setIcvVerification(value)
        assert result is obj
        assert obj.getIcvVerification() is value
        assert obj.getIcvVerification().getValue() == GlobalTimeIcvVerificationEnum.ICV_VERIFIED

        result = obj.setIcvVerification(None)
        assert result is obj
        assert obj.getIcvVerification() is value

    def test_get_set_time_leap_thresholds(self):
        """
        Test the timeLeap* getter/setter pairs round-trip and None no-op.
        """
        obj = self._create_slave()

        future = TimeValue()
        future.setValue("0.5")
        result = obj.setTimeLeapFutureThreshold(future)
        assert result is obj
        assert obj.getTimeLeapFutureThreshold() is future

        healing = PositiveInteger()
        healing.setValue("4")
        result = obj.setTimeLeapHealingCounter(healing)
        assert result is obj
        assert obj.getTimeLeapHealingCounter() is healing
        assert obj.getTimeLeapHealingCounter().getValue() == 4

        past = TimeValue()
        past.setValue("-0.5")
        result = obj.setTimeLeapPastThreshold(past)
        assert result is obj
        assert obj.getTimeLeapPastThreshold() is past

        result = obj.setTimeLeapFutureThreshold(None)
        assert result is obj
        assert obj.getTimeLeapFutureThreshold() is future

    def test_variation_point_base_accessors(self):
        """
        Exercise the inherited VariationPointCapable accessors: chaining, round-trip, None no-op.
        """
        obj = self._create_slave()

        variation_point = VariationPoint()
        assert obj.setVariationPoint(variation_point) is obj
        assert obj.getVariationPoint() is variation_point

        obj.setVariationPoint(None)
        assert obj.getVariationPoint() is variation_point

    def test_accessor_docstrings_are_spec_notes_verbatim(self):
        """
        Getter and setter docstrings carry the spec Note verbatim (setter + None-no-op sentence).
        """
        assert inspect.cleandoc(GlobalTimeSlave.getCommunicationConnectorRef.__doc__) == self.COMMUNICATION_CONNECTOR_REF_NOTE
        assert inspect.cleandoc(GlobalTimeSlave.setCommunicationConnectorRef.__doc__) == (
            self.COMMUNICATION_CONNECTOR_REF_NOTE + "\n\nA None value is a no-op and does not overwrite an existing communicationConnectorRef."
        )
        assert inspect.cleandoc(GlobalTimeSlave.getFollowUpTimeoutValue.__doc__) == self.FOLLOW_UP_TIMEOUT_VALUE_NOTE
        assert inspect.cleandoc(GlobalTimeSlave.setFollowUpTimeoutValue.__doc__) == (
            self.FOLLOW_UP_TIMEOUT_VALUE_NOTE + "\n\nA None value is a no-op and does not overwrite an existing followUpTimeoutValue."
        )
        assert inspect.cleandoc(GlobalTimeSlave.getIcvVerification.__doc__) == self.ICV_VERIFICATION_NOTE
        assert inspect.cleandoc(GlobalTimeSlave.setIcvVerification.__doc__) == (self.ICV_VERIFICATION_NOTE + "\n\nA None value is a no-op and does not overwrite an existing icvVerification.")
        assert inspect.cleandoc(GlobalTimeSlave.getTimeLeapFutureThreshold.__doc__) == self.TIME_LEAP_FUTURE_THRESHOLD_NOTE
        assert inspect.cleandoc(GlobalTimeSlave.setTimeLeapFutureThreshold.__doc__) == (
            self.TIME_LEAP_FUTURE_THRESHOLD_NOTE + "\n\nA None value is a no-op and does not overwrite an existing timeLeapFutureThreshold."
        )
        assert inspect.cleandoc(GlobalTimeSlave.getTimeLeapHealingCounter.__doc__) == self.TIME_LEAP_HEALING_COUNTER_NOTE
        assert inspect.cleandoc(GlobalTimeSlave.setTimeLeapHealingCounter.__doc__) == (
            self.TIME_LEAP_HEALING_COUNTER_NOTE + "\n\nA None value is a no-op and does not overwrite an existing timeLeapHealingCounter."
        )
        assert inspect.cleandoc(GlobalTimeSlave.getTimeLeapPastThreshold.__doc__) == self.TIME_LEAP_PAST_THRESHOLD_NOTE
        assert inspect.cleandoc(GlobalTimeSlave.setTimeLeapPastThreshold.__doc__) == (
            self.TIME_LEAP_PAST_THRESHOLD_NOTE + "\n\nA None value is a no-op and does not overwrite an existing timeLeapPastThreshold."
        )


class TestGlobalTimeMaster:
    """
    Test class for GlobalTimeMaster functionality.

    Spec: AUTOSAR_CP_TPS_SystemTemplate.pdf, Table 9.4, p.860
    (abstract; subclasses GlobalTimeCanMaster, GlobalTimeEthMaster, GlobalTimeFrMaster and
    UserDefinedGlobalTimeMaster — exercised through a local concrete subclass per the
    abstract-class test convention.)
    """

    CLASS_NOTE = "This represents the generic concept of a global time master."
    COMMUNICATION_CONNECTOR_REF_NOTE = "The GlobalTimeMaster is bound to the Communication Connector."
    ICV_SECURED_NOTE = "Defines whether an Integrity Check Value (ICV) shall be added to the sent time sync messages. Tags: atp.Status=candidate"
    IMMEDIATE_RESUME_TIME_NOTE = 'Defines the minimum time between an "immediate" message and the next periodic message.'
    IS_SYSTEM_WIDE_GLOBAL_TIME_MASTER_NOTE = "If set to TRUE, the GlobalTimeMaster is supposed to act as the root of global time information."
    SYNC_PERIOD_NOTE = "This represents the period. Unit: seconds"

    def _create_master(self) -> ConcreteGlobalTimeMaster:
        return ConcreteGlobalTimeMaster(AUTOSAR.getInstance(), "master")

    def test_abstract_initialization(self):
        """
        GlobalTimeMaster is abstract and cannot be instantiated directly.
        """
        with pytest.raises(TypeError):
            GlobalTimeMaster(AUTOSAR.getInstance(), "master")

    def test_is_identifiable_subclass_with_variation_point_capable(self):
        """
        Test that GlobalTimeMaster derives from Identifiable per the Table 9.4 Base row
        (ARObject, Identifiable, MultilanguageReferrable, Referrable — most-derived
        Identifiable) and from VariationPointCapable (the atpVariation on the owning
        GlobalTimeDomain.globalTimeMaster row makes the class VP-capable; the XSD
        GLOBAL-TIME-MASTER group carries VARIATION-POINT last, xml.sequenceOffset=10000).
        """
        assert issubclass(GlobalTimeMaster, Identifiable)
        assert issubclass(GlobalTimeMaster, VariationPointCapable)

    def test_class_docstring_is_spec_note_verbatim(self):
        """
        Test that the class docstring is the spec Note verbatim.
        """
        assert inspect.cleandoc(GlobalTimeMaster.__doc__) == self.CLASS_NOTE

    def test_init_has_no_docstring(self):
        """
        Test that __init__ carries no docstring.
        """
        assert GlobalTimeMaster.__init__.__doc__ is None

    def test_member_order_follows_spec_rows(self):
        """
        Test that the accessors follow the Table 9.4 displayed row order (getter first per attribute).
        """
        methods = [name for name, value in GlobalTimeMaster.__dict__.items() if callable(value) and not name.startswith("_")]
        assert methods == [
            "getCommunicationConnectorRef",
            "setCommunicationConnectorRef",
            "getIcvSecured",
            "setIcvSecured",
            "getImmediateResumeTime",
            "setImmediateResumeTime",
            "getIsSystemWideGlobalTimeMaster",
            "setIsSystemWideGlobalTimeMaster",
            "getSyncPeriod",
            "setSyncPeriod",
        ]

    def test_initialization_defaults(self):
        """
        Test that a concrete subclass initializes all attributes to their defaults.
        """
        obj = self._create_master()

        assert obj.getShortName() == "master"
        assert obj.getChecksum() is None
        assert obj.getCommunicationConnectorRef() is None
        assert obj.getIcvSecured() is None
        assert obj.getImmediateResumeTime() is None
        assert obj.getIsSystemWideGlobalTimeMaster() is None
        assert obj.getSyncPeriod() is None
        assert obj.getVariationPoint() is None

    def test_annotations_are_optional_typed(self):
        """
        Test that the accessors carry the spec types (0..1 rows).
        """
        hints = typing.get_type_hints(GlobalTimeMaster.getCommunicationConnectorRef)
        assert hints.get("return") == typing.Optional[RefType]
        hints = typing.get_type_hints(GlobalTimeMaster.setCommunicationConnectorRef)
        assert hints.get("value") == typing.Optional[RefType]
        assert hints.get("return") is GlobalTimeMaster

        hints = typing.get_type_hints(GlobalTimeMaster.getIcvSecured)
        assert hints.get("return") == typing.Optional[GlobalTimeIcvSupportEnum]
        hints = typing.get_type_hints(GlobalTimeMaster.getImmediateResumeTime)
        assert hints.get("return") == typing.Optional[TimeValue]
        hints = typing.get_type_hints(GlobalTimeMaster.getIsSystemWideGlobalTimeMaster)
        assert hints.get("return") == typing.Optional[Boolean]
        hints = typing.get_type_hints(GlobalTimeMaster.getSyncPeriod)
        assert hints.get("return") == typing.Optional[TimeValue]

    def test_get_set_communication_connector_ref(self):
        """
        Test getCommunicationConnectorRef and setCommunicationConnectorRef round-trip and None no-op.
        """
        obj = self._create_master()

        value = RefType()
        value.setValue("/CommunicationClusters/Cluster/Connector")
        result = obj.setCommunicationConnectorRef(value)
        assert result is obj
        assert obj.getCommunicationConnectorRef() is value
        assert obj.getCommunicationConnectorRef().getValue() == "/CommunicationClusters/Cluster/Connector"

        result = obj.setCommunicationConnectorRef(None)
        assert result is obj
        assert obj.getCommunicationConnectorRef() is value

    def test_get_set_icv_secured(self):
        """
        Test getIcvSecured and setIcvSecured round-trip and None no-op.
        """
        obj = self._create_master()

        value = GlobalTimeIcvSupportEnum()
        value.setValue(GlobalTimeIcvSupportEnum.ICV_SUPPORTED)
        result = obj.setIcvSecured(value)
        assert result is obj
        assert obj.getIcvSecured() is value
        assert obj.getIcvSecured().getValue() == GlobalTimeIcvSupportEnum.ICV_SUPPORTED

        result = obj.setIcvSecured(None)
        assert result is obj
        assert obj.getIcvSecured() is value

    def test_get_set_immediate_resume_time(self):
        """
        Test getImmediateResumeTime and setImmediateResumeTime round-trip and None no-op.
        """
        obj = self._create_master()

        value = TimeValue()
        value.setValue("2.0")
        result = obj.setImmediateResumeTime(value)
        assert result is obj
        assert obj.getImmediateResumeTime() is value

        result = obj.setImmediateResumeTime(None)
        assert result is obj
        assert obj.getImmediateResumeTime() is value

    def test_get_set_is_system_wide_global_time_master(self):
        """
        Test getIsSystemWideGlobalTimeMaster and setIsSystemWideGlobalTimeMaster round-trip and None no-op.
        """
        obj = self._create_master()

        value = Boolean().setValue(True)
        result = obj.setIsSystemWideGlobalTimeMaster(value)
        assert result is obj
        assert obj.getIsSystemWideGlobalTimeMaster() is value
        assert obj.getIsSystemWideGlobalTimeMaster().getValue() is True

        result = obj.setIsSystemWideGlobalTimeMaster(None)
        assert result is obj
        assert obj.getIsSystemWideGlobalTimeMaster() is value

    def test_get_set_sync_period(self):
        """
        Test getSyncPeriod and setSyncPeriod round-trip and None no-op.
        """
        obj = self._create_master()

        value = TimeValue()
        value.setValue("0.2")
        result = obj.setSyncPeriod(value)
        assert result is obj
        assert obj.getSyncPeriod() is value

        result = obj.setSyncPeriod(None)
        assert result is obj
        assert obj.getSyncPeriod() is value

    def test_variation_point_base_accessors(self):
        """
        Exercise the inherited VariationPointCapable accessors: chaining, round-trip, None no-op.
        """
        obj = self._create_master()

        variation_point = VariationPoint()
        assert obj.setVariationPoint(variation_point) is obj
        assert obj.getVariationPoint() is variation_point

        obj.setVariationPoint(None)
        assert obj.getVariationPoint() is variation_point

    def test_accessor_docstrings_are_spec_notes_verbatim(self):
        """
        Getter and setter docstrings carry the spec Note verbatim (setter + None-no-op sentence).
        """
        assert inspect.cleandoc(GlobalTimeMaster.getCommunicationConnectorRef.__doc__) == self.COMMUNICATION_CONNECTOR_REF_NOTE
        assert inspect.cleandoc(GlobalTimeMaster.setCommunicationConnectorRef.__doc__) == (
            self.COMMUNICATION_CONNECTOR_REF_NOTE + "\n\nA None value is a no-op and does not overwrite an existing communicationConnectorRef."
        )
        assert inspect.cleandoc(GlobalTimeMaster.getIcvSecured.__doc__) == self.ICV_SECURED_NOTE
        assert inspect.cleandoc(GlobalTimeMaster.setIcvSecured.__doc__) == (self.ICV_SECURED_NOTE + "\n\nA None value is a no-op and does not overwrite an existing icvSecured.")
        assert inspect.cleandoc(GlobalTimeMaster.getImmediateResumeTime.__doc__) == self.IMMEDIATE_RESUME_TIME_NOTE
        assert inspect.cleandoc(GlobalTimeMaster.setImmediateResumeTime.__doc__) == (
            self.IMMEDIATE_RESUME_TIME_NOTE + "\n\nA None value is a no-op and does not overwrite an existing immediateResumeTime."
        )
        assert inspect.cleandoc(GlobalTimeMaster.getIsSystemWideGlobalTimeMaster.__doc__) == self.IS_SYSTEM_WIDE_GLOBAL_TIME_MASTER_NOTE
        assert inspect.cleandoc(GlobalTimeMaster.setIsSystemWideGlobalTimeMaster.__doc__) == (
            self.IS_SYSTEM_WIDE_GLOBAL_TIME_MASTER_NOTE + "\n\nA None value is a no-op and does not overwrite an existing isSystemWideGlobalTimeMaster."
        )
        assert inspect.cleandoc(GlobalTimeMaster.getSyncPeriod.__doc__) == self.SYNC_PERIOD_NOTE
        assert inspect.cleandoc(GlobalTimeMaster.setSyncPeriod.__doc__) == (self.SYNC_PERIOD_NOTE + "\n\nA None value is a no-op and does not overwrite an existing syncPeriod.")


class TestGlobalTimeGateway:
    """
    Test class for GlobalTimeGateway functionality.

    Spec: AUTOSAR_CP_TPS_SystemTemplate.pdf, Table 9.6, p.861
    (concrete; the Table 9.6 Base row's most-derived class is Identifiable.)
    """

    CLASS_NOTE = "This represents the ability to define a time gateway for establishing a global time domain over several communication clusters."
    HOST_REF_NOTE = "The GlobalTimeGateway is hosted by the referenced Ecu Instance."
    MASTER_REF_NOTE = "This represents the master of the global time gateway."
    SLAVE_REF_NOTE = "This represents the slave of the GlobalTimeGateway."

    def _create_gateway(self) -> GlobalTimeGateway:
        return GlobalTimeGateway(AUTOSAR.getInstance(), "gateway")

    def test_is_identifiable_subclass_with_variation_point_capable(self):
        """
        Test that GlobalTimeGateway derives from Identifiable per the Table 9.6 Base row
        (ARObject, Identifiable, MultilanguageReferrable, Referrable — most-derived
        Identifiable) and from VariationPointCapable (the atpVariation on the owning
        GlobalTimeDomain.gateway row makes the class VP-capable; the XSD GLOBAL-TIME-GATEWAY
        group carries VARIATION-POINT last, xml.sequenceOffset=10000).
        """
        assert issubclass(GlobalTimeGateway, Identifiable)
        assert issubclass(GlobalTimeGateway, VariationPointCapable)

    def test_class_docstring_is_spec_note_verbatim(self):
        """
        Test that the class docstring is the spec Note verbatim.
        """
        assert inspect.cleandoc(GlobalTimeGateway.__doc__) == self.CLASS_NOTE

    def test_init_has_no_docstring(self):
        """
        Test that __init__ carries no docstring.
        """
        assert GlobalTimeGateway.__init__.__doc__ is None

    def test_member_order_follows_spec_rows(self):
        """
        Test that the accessors follow the Table 9.6 displayed row order (getter first per attribute).
        """
        methods = [name for name, value in GlobalTimeGateway.__dict__.items() if callable(value) and not name.startswith("_")]
        assert methods == [
            "getHostRef",
            "setHostRef",
            "getMasterRef",
            "setMasterRef",
            "getSlaveRef",
            "setSlaveRef",
        ]

    def test_initialization_defaults(self):
        """
        Test that the instance initializes all attributes to their defaults.
        """
        obj = self._create_gateway()

        assert obj.getShortName() == "gateway"
        assert obj.getChecksum() is None
        assert obj.getHostRef() is None
        assert obj.getMasterRef() is None
        assert obj.getSlaveRef() is None
        assert obj.getVariationPoint() is None

    def test_annotations_are_optional_typed(self):
        """
        Test that the accessors carry the spec types (0..1 ref rows).
        """
        hints = typing.get_type_hints(GlobalTimeGateway.getHostRef)
        assert hints.get("return") == typing.Optional[RefType]
        hints = typing.get_type_hints(GlobalTimeGateway.setHostRef)
        assert hints.get("value") == typing.Optional[RefType]
        assert hints.get("return") is GlobalTimeGateway

        hints = typing.get_type_hints(GlobalTimeGateway.getMasterRef)
        assert hints.get("return") == typing.Optional[RefType]
        hints = typing.get_type_hints(GlobalTimeGateway.getSlaveRef)
        assert hints.get("return") == typing.Optional[RefType]

    def test_get_set_refs(self):
        """
        Test the host/master/slave ref getter/setter pairs round-trip and None no-op.
        """
        obj = self._create_gateway()

        host = RefType()
        host.setValue("/ECU/EcuInstance1")
        result = obj.setHostRef(host)
        assert result is obj
        assert obj.getHostRef() is host
        assert obj.getHostRef().getValue() == "/ECU/EcuInstance1"

        master = RefType()
        master.setValue("/TimeDomains/Domain1/Master")
        result = obj.setMasterRef(master)
        assert result is obj
        assert obj.getMasterRef() is master

        slave = RefType()
        slave.setValue("/TimeDomains/Domain1/Slave")
        result = obj.setSlaveRef(slave)
        assert result is obj
        assert obj.getSlaveRef() is slave

        result = obj.setHostRef(None)
        assert result is obj
        assert obj.getHostRef() is host

    def test_variation_point_base_accessors(self):
        """
        Exercise the inherited VariationPointCapable accessors: chaining, round-trip, None no-op.
        """
        obj = self._create_gateway()

        variation_point = VariationPoint()
        assert obj.setVariationPoint(variation_point) is obj
        assert obj.getVariationPoint() is variation_point

        obj.setVariationPoint(None)
        assert obj.getVariationPoint() is variation_point

    def test_accessor_docstrings_are_spec_notes_verbatim(self):
        """
        Getter and setter docstrings carry the spec Note verbatim (setter + None-no-op sentence).
        """
        assert inspect.cleandoc(GlobalTimeGateway.getHostRef.__doc__) == self.HOST_REF_NOTE
        assert inspect.cleandoc(GlobalTimeGateway.setHostRef.__doc__) == (self.HOST_REF_NOTE + "\n\nA None value is a no-op and does not overwrite an existing hostRef.")
        assert inspect.cleandoc(GlobalTimeGateway.getMasterRef.__doc__) == self.MASTER_REF_NOTE
        assert inspect.cleandoc(GlobalTimeGateway.setMasterRef.__doc__) == (self.MASTER_REF_NOTE + "\n\nA None value is a no-op and does not overwrite an existing masterRef.")
        assert inspect.cleandoc(GlobalTimeGateway.getSlaveRef.__doc__) == self.SLAVE_REF_NOTE
        assert inspect.cleandoc(GlobalTimeGateway.setSlaveRef.__doc__) == (self.SLAVE_REF_NOTE + "\n\nA None value is a no-op and does not overwrite an existing slaveRef.")


class TestBinaryManifestResource:
    """
    Test class for BinaryManifestResource functionality.

    Spec: AUTOSAR_CP_TPS_SystemTemplate.pdf, Table 11.19, p.916
    (abstract; subclasses BinaryManifestProvideResource and BinaryManifestRequireResource are
    unsynced later-wave stubs — exercised through a local concrete subclass per the
    abstract-class test convention.)
    """

    CLASS_NOTE = "This meta-class acts as an abstract base class for specializations."
    GLOBAL_RESOURCE_ID_NOTE = "A unique identifiers per resource used for the connection process. The identifier is required to be unique in the scope of a single machine. If software clusters are designed to be reused on multiple machines the uniqueness requirements applies for all the intended machines."
    ITEM_NOTE = "This aggregation represents the collection of binary manifest handles owned by the enclosing binary manifest resource."
    RESOURCE_NOTE = "This reference identifies the CpSoftwareClusterResource (on design level) that corresponds to the BinaryManifest Resource (on integration level)."

    def _create_resource(self) -> BinaryManifestResource:
        class ConcreteBinaryManifestResource(BinaryManifestResource):
            pass

        return ConcreteBinaryManifestResource(AUTOSAR.getInstance(), "resource")

    def test_cannot_instantiate_abstract(self):
        """
        BinaryManifestResource is abstract per Table 11.19 and cannot be instantiated directly.
        """
        with pytest.raises(TypeError):
            BinaryManifestResource(AUTOSAR.getInstance(), "resource")

    def test_is_identifiable_subclass(self):
        """
        Test that BinaryManifestResource derives from Identifiable per the Table 11.19 Base row
        (ARObject, Identifiable, MultilanguageReferrable, Referrable — most-derived Identifiable).
        """
        import abc

        assert issubclass(BinaryManifestResource, Identifiable)
        assert issubclass(BinaryManifestResource, ARObject)
        assert issubclass(BinaryManifestResource, abc.ABC)

    def test_class_docstring_is_spec_note_verbatim(self):
        """
        Test that the class docstring is the spec Note verbatim.
        """
        assert inspect.cleandoc(BinaryManifestResource.__doc__) == self.CLASS_NOTE

    def test_init_has_no_docstring(self):
        """
        Test that __init__ carries no docstring.
        """
        assert BinaryManifestResource.__init__.__doc__ is None

    def test_member_order_follows_spec_rows(self):
        """
        Test that the accessors follow the Table 11.19 displayed row order
        (getter first per scalar attribute, mutator first per aggregated attribute).
        """
        methods = [name for name, value in BinaryManifestResource.__dict__.items() if callable(value) and not name.startswith("_")]
        assert methods == [
            "getGlobalResourceId",
            "setGlobalResourceId",
            "createItem",
            "getItems",
            "getResourceRef",
            "setResourceRef",
        ]

    def test_initialization_defaults(self):
        """
        Test that a concrete subclass initializes all Table 11.19 attributes to their defaults.
        """
        obj = self._create_resource()

        assert obj.getShortName() == "resource"
        assert obj.getChecksum() is None
        assert obj.getGlobalResourceId() is None
        assert obj.getItems() == []
        assert obj.getResourceRef() is None

    def test_annotations_are_spec_typed(self):
        """
        Test that the accessors carry the Table 11.19 Type column types
        (PositiveInteger 0..1, BinaryManifestItem *, CpSoftwareClusterResource ref 0..1).
        """
        hints = typing.get_type_hints(BinaryManifestResource.getGlobalResourceId)
        assert hints.get("return") == typing.Optional[PositiveInteger]
        hints = typing.get_type_hints(BinaryManifestResource.setGlobalResourceId)
        assert hints.get("value") == typing.Optional[PositiveInteger]
        assert hints.get("return") is BinaryManifestResource

        hints = typing.get_type_hints(BinaryManifestResource.createItem)
        assert hints.get("short_name") is str
        assert hints.get("return") is BinaryManifestItem
        hints = typing.get_type_hints(BinaryManifestResource.getItems)
        assert hints.get("return") == typing.List[BinaryManifestItem]

        hints = typing.get_type_hints(BinaryManifestResource.getResourceRef)
        assert hints.get("return") == typing.Optional[RefType]
        hints = typing.get_type_hints(BinaryManifestResource.setResourceRef)
        assert hints.get("value") == typing.Optional[RefType]
        assert hints.get("return") is BinaryManifestResource

    def test_get_set_global_resource_id(self):
        """
        Test setGlobalResourceId and getGlobalResourceId round-trip and None no-op.
        """
        obj = self._create_resource()

        result = obj.setGlobalResourceId(PositiveInteger().setValue("4"))
        assert result is obj
        assert obj.getGlobalResourceId().getValue() == 4

        obj.setGlobalResourceId(None)
        assert obj.getGlobalResourceId().getValue() == 4

    def test_create_item(self):
        """
        Test that createItem appends a BinaryManifestItem and returns the existing one on a
        duplicate short name.
        """
        obj = self._create_resource()

        item = obj.createItem("Handle1")
        assert isinstance(item, BinaryManifestItem)
        assert item.getShortName() == "Handle1"
        assert obj.getItems() == [item]

        duplicate = obj.createItem("Handle1")
        assert duplicate is item
        assert obj.getItems() == [item]

    def test_get_set_resource_ref(self):
        """
        Test setResourceRef and getResourceRef round-trip and None no-op.
        """
        obj = self._create_resource()

        ref = RefType().setValue("/AUTOSAR/CpSoftwareClusterResources/Res1").setDest("CP-SOFTWARE-CLUSTER-RESOURCE")
        result = obj.setResourceRef(ref)
        assert result is obj
        assert obj.getResourceRef() is ref
        assert obj.getResourceRef().getValue() == "/AUTOSAR/CpSoftwareClusterResources/Res1"

        obj.setResourceRef(None)
        assert obj.getResourceRef() is ref

    def test_accessor_docstrings_are_spec_notes_verbatim(self):
        """
        Getter/setter docstrings carry the spec Note verbatim (setter + None-no-op sentence).
        """
        assert inspect.cleandoc(BinaryManifestResource.getGlobalResourceId.__doc__) == self.GLOBAL_RESOURCE_ID_NOTE
        assert inspect.cleandoc(BinaryManifestResource.setGlobalResourceId.__doc__) == (
            self.GLOBAL_RESOURCE_ID_NOTE + "\n\nA None value is a no-op and does not overwrite an existing globalResourceId."
        )
        assert inspect.cleandoc(BinaryManifestResource.createItem.__doc__) == self.ITEM_NOTE
        assert inspect.cleandoc(BinaryManifestResource.getItems.__doc__) == self.ITEM_NOTE
        assert inspect.cleandoc(BinaryManifestResource.getResourceRef.__doc__) == self.RESOURCE_NOTE
        assert inspect.cleandoc(BinaryManifestResource.setResourceRef.__doc__) == (self.RESOURCE_NOTE + "\n\nA None value is a no-op and does not overwrite an existing resourceRef.")


class TestBinaryManifestAddressableObject:
    """
    Test class for BinaryManifestAddressableObject functionality.

    Spec: AUTOSAR_CP_TPS_SystemTemplate.pdf, Table 11.24, p.921
    (abstract; subclasses BinaryManifestItem and BinaryManifestMetaDataField — exercised through
    a local concrete subclass per the abstract-class test convention.)
    """

    CLASS_NOTE = "This meta-class acts as an abstract base class for addressable objects in the context of the binary manifest of a CP software cluster."
    ADDRESS_NOTE = "This attribute specifies the address of the enclosing addressable object."
    SYMBOL_NOTE = "This attribute specifies the symbol of the addressable object."

    def _create_object(self) -> BinaryManifestAddressableObject:
        class ConcreteBinaryManifestAddressableObject(BinaryManifestAddressableObject):
            pass

        return ConcreteBinaryManifestAddressableObject(AUTOSAR.getInstance(), "Addressable1")

    def test_cannot_instantiate_abstract(self):
        """
        BinaryManifestAddressableObject is abstract per Table 11.24 and cannot be instantiated directly.
        """
        with pytest.raises(TypeError):
            BinaryManifestAddressableObject(AUTOSAR.getInstance(), "Addressable1")

    def test_is_identifiable_subclass(self):
        """
        Test that BinaryManifestAddressableObject derives from Identifiable per the Table 11.24
        Base row (ARObject, Identifiable, MultilanguageReferrable, Referrable — most-derived
        Identifiable).
        """
        import abc

        assert issubclass(BinaryManifestAddressableObject, Identifiable)
        assert issubclass(BinaryManifestAddressableObject, ARObject)
        assert issubclass(BinaryManifestAddressableObject, abc.ABC)

    def test_class_docstring_is_spec_note_verbatim(self):
        """
        Test that the class docstring is the spec Note verbatim.
        """
        assert inspect.cleandoc(BinaryManifestAddressableObject.__doc__) == self.CLASS_NOTE

    def test_init_has_no_docstring(self):
        """
        Test that __init__ carries no docstring.
        """
        assert BinaryManifestAddressableObject.__init__.__doc__ is None

    def test_member_order_follows_spec_rows(self):
        """
        Test that the accessors follow the Table 11.24 displayed row order (getter first per attribute).
        """
        methods = [name for name, value in BinaryManifestAddressableObject.__dict__.items() if callable(value) and not name.startswith("_")]
        assert methods == [
            "getAddress",
            "setAddress",
            "getSymbol",
            "setSymbol",
        ]

    def test_initialization_defaults(self):
        """
        Test that a concrete subclass initializes all Table 11.24 attributes to their defaults.
        """
        obj = self._create_object()

        assert obj.getShortName() == "Addressable1"
        assert obj.getChecksum() is None
        assert obj.getAddress() is None
        assert obj.getSymbol() is None

    def test_annotations_are_spec_typed(self):
        """
        Test that the accessors carry the Table 11.24 Type column types (Address 0..1, SymbolString 0..1).
        """
        hints = typing.get_type_hints(BinaryManifestAddressableObject.getAddress)
        assert hints.get("return") == typing.Optional[Address]
        hints = typing.get_type_hints(BinaryManifestAddressableObject.setAddress)
        assert hints.get("value") == typing.Optional[Address]
        assert hints.get("return") is BinaryManifestAddressableObject

        hints = typing.get_type_hints(BinaryManifestAddressableObject.getSymbol)
        assert hints.get("return") == typing.Optional[SymbolString]
        hints = typing.get_type_hints(BinaryManifestAddressableObject.setSymbol)
        assert hints.get("value") == typing.Optional[SymbolString]
        assert hints.get("return") is BinaryManifestAddressableObject

    def test_get_set_address(self):
        """
        Test setAddress and getAddress round-trip and None no-op.
        """
        obj = self._create_object()

        address = Address().setValue("0x0000A000")
        result = obj.setAddress(address)
        assert result is obj
        assert obj.getAddress() is address
        assert obj.getAddress().getValue() == "0x0000A000"

        obj.setAddress(None)
        assert obj.getAddress() is address

    def test_get_set_symbol(self):
        """
        Test setSymbol and getSymbol round-trip and None no-op.
        """
        obj = self._create_object()

        symbol = SymbolString().setValue("HandleSymbol")
        result = obj.setSymbol(symbol)
        assert result is obj
        assert obj.getSymbol() is symbol
        assert obj.getSymbol().getValue() == "HandleSymbol"

        obj.setSymbol(None)
        assert obj.getSymbol() is symbol

    def test_accessor_docstrings_are_spec_notes_verbatim(self):
        """
        Getter/setter docstrings carry the spec Note verbatim (setter + None-no-op sentence).
        """
        assert inspect.cleandoc(BinaryManifestAddressableObject.getAddress.__doc__) == self.ADDRESS_NOTE
        assert inspect.cleandoc(BinaryManifestAddressableObject.setAddress.__doc__) == (self.ADDRESS_NOTE + "\n\nA None value is a no-op and does not overwrite an existing address.")
        assert inspect.cleandoc(BinaryManifestAddressableObject.getSymbol.__doc__) == self.SYMBOL_NOTE
        assert inspect.cleandoc(BinaryManifestAddressableObject.setSymbol.__doc__) == (self.SYMBOL_NOTE + "\n\nA None value is a no-op and does not overwrite an existing symbol.")
