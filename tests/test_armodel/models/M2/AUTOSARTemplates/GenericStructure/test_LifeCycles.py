"""
This module contains comprehensive tests for the LifeCycles.py file
in the AUTOSAR GenericStructure module.
"""

from datetime import datetime

from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    RefType,
    RevisionLabelString,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.LifeCycles import (
    LifeCycleInfo,
    LifeCycleInfoSet,
    LifeCyclePeriod,
)
from armodel.models.M2.MSR.Documentation.TextModel.BlockElements import (
    DocumentationBlock,
)


class TestLifeCyclePeriod:
    """
    Test class for LifeCyclePeriod functionality.
    """

    def test_initialization(self):
        """
        Test LifeCyclePeriod initialization.
        """
        period = LifeCyclePeriod()

        # Verify basic properties
        assert period is not None

        # Verify default values for attributes
        assert period.getArReleaseVersion() is None
        assert period.getDate() is None
        assert period.getProductRelease() is None

    def test_get_ar_release_version(self):
        """
        Test getArReleaseVersion method returns None by default.
        """
        period = LifeCyclePeriod()

        # Verify initial state
        version = period.getArReleaseVersion()
        assert version is None

    def test_set_ar_release_version(self):
        """
        Test setArReleaseVersion method sets the AUTOSAR release version correctly.
        """
        period = LifeCyclePeriod()

        # Create mock RevisionLabelString instance
        version = RevisionLabelString().setValue("4.0.0")

        # Set the AUTOSAR release version
        result = period.setArReleaseVersion(version)
        assert result is period  # Verify method chaining
        assert period.getArReleaseVersion() == version

    def test_set_ar_release_version_none(self):
        """
        Test setArReleaseVersion method handles None value correctly.
        """
        period = LifeCyclePeriod()

        # Set initial value
        initial_version = RevisionLabelString().setValue("4.0.0")
        period.setArReleaseVersion(initial_version)
        assert period.getArReleaseVersion() == initial_version

        # Set to None - should not change the value (per implementation logic)
        result = period.setArReleaseVersion(None)
        assert result is period  # Verify method chaining
        # Value should remain unchanged due to "if value is not None" check
        assert period.getArReleaseVersion() == initial_version

    def test_get_date(self):
        """
        Test getDate method returns None by default.
        """
        period = LifeCyclePeriod()

        # Verify initial state
        date = period.getDate()
        assert date is None

    def test_set_date(self):
        """
        Test setDate method sets the date correctly.
        """
        period = LifeCyclePeriod()

        # Create mock datetime instance
        test_date = datetime.now()

        # Set the date
        result = period.setDate(test_date)
        assert result is period  # Verify method chaining
        assert period.getDate() == test_date

    def test_set_date_none(self):
        """
        Test setDate method handles None value correctly.
        """
        period = LifeCyclePeriod()

        # Set initial value
        initial_date = datetime.now()
        period.setDate(initial_date)
        assert period.getDate() == initial_date

        # Set to None - should not change the value (per implementation logic)
        result = period.setDate(None)
        assert result is period  # Verify method chaining
        # Value should remain unchanged due to "if value is not None" check
        assert period.getDate() == initial_date

    def test_get_product_release(self):
        """
        Test getProductRelease method returns None by default.
        """
        period = LifeCyclePeriod()

        # Verify initial state
        release = period.getProductRelease()
        assert release is None

    def test_set_product_release(self):
        """
        Test setProductRelease method sets the product release correctly.
        """
        period = LifeCyclePeriod()

        # Create mock RevisionLabelString instance
        release = RevisionLabelString().setValue("1.2.3")

        # Set the product release
        result = period.setProductRelease(release)
        assert result is period  # Verify method chaining
        assert period.getProductRelease() == release

    def test_set_product_release_none(self):
        """
        Test setProductRelease method handles None value correctly.
        """
        period = LifeCyclePeriod()

        # Set initial value
        initial_release = RevisionLabelString().setValue("1.2.3")
        period.setProductRelease(initial_release)
        assert period.getProductRelease() == initial_release

        # Set to None - should not change the value (per implementation logic)
        result = period.setProductRelease(None)
        assert result is period  # Verify method chaining
        # Value should remain unchanged due to "if value is not None" check
        assert period.getProductRelease() == initial_release


class TestLifeCycleInfo:
    """
    Test class for LifeCycleInfo functionality.
    """

    def test_initialization(self):
        """
        Test LifeCycleInfo initialization.
        """
        info = LifeCycleInfo()

        # Verify basic properties
        assert info is not None

        # Verify default values for attributes
        assert info.getLcObjectRef() is None
        assert info.getLcStateRef() is None
        assert info.getPeriodBegin() is None
        assert info.getPeriodEnd() is None
        assert info.getRemark() is None
        assert info.getUseInsteadRefs() == []

    def test_get_lc_object_ref(self):
        """
        Test getLcObjectRef method returns None by default.
        """
        info = LifeCycleInfo()

        # Verify initial state
        obj_ref = info.getLcObjectRef()
        assert obj_ref is None

    def test_set_lc_object_ref(self):
        """
        Test setLcObjectRef method sets the life cycle object reference correctly.
        """
        info = LifeCycleInfo()

        # Create mock RefType instance
        obj_ref = RefType().setValue("/Package/Element")

        # Set the life cycle object reference
        result = info.setLcObjectRef(obj_ref)
        assert result is info  # Verify method chaining
        assert info.getLcObjectRef() == obj_ref

    def test_set_lc_object_ref_none(self):
        """
        Test setLcObjectRef method handles None value correctly.
        """
        info = LifeCycleInfo()

        # Set initial value
        initial_ref = RefType().setValue("/Package/Element")
        info.setLcObjectRef(initial_ref)
        assert info.getLcObjectRef() == initial_ref

        # Set to None - should not change the value (per implementation logic)
        result = info.setLcObjectRef(None)
        assert result is info  # Verify method chaining
        # Value should remain unchanged due to "if value is not None" check
        assert info.getLcObjectRef() == initial_ref

    def test_get_lc_state_ref(self):
        """
        Test getLcStateRef method returns None by default.
        """
        info = LifeCycleInfo()

        # Verify initial state
        state_ref = info.getLcStateRef()
        assert state_ref is None

    def test_set_lc_state_ref(self):
        """
        Test setLcStateRef method sets the life cycle state reference correctly.
        """
        info = LifeCycleInfo()

        # Create mock RefType instance
        state_ref = RefType().setValue("/Package/State")

        # Set the life cycle state reference
        result = info.setLcStateRef(state_ref)
        assert result is info  # Verify method chaining
        assert info.getLcStateRef() == state_ref

    def test_set_lc_state_ref_none(self):
        """
        Test setLcStateRef method handles None value correctly.
        """
        info = LifeCycleInfo()

        # Set initial value
        initial_ref = RefType().setValue("/Package/State")
        info.setLcStateRef(initial_ref)
        assert info.getLcStateRef() == initial_ref

        # Set to None - should not change the value (per implementation logic)
        result = info.setLcStateRef(None)
        assert result is info  # Verify method chaining
        # Value should remain unchanged due to "if value is not None" check
        assert info.getLcStateRef() == initial_ref

    def test_get_period_begin(self):
        """
        Test getPeriodBegin method returns None by default.
        """
        info = LifeCycleInfo()

        # Verify initial state
        period_begin = info.getPeriodBegin()
        assert period_begin is None

    def test_set_period_begin(self):
        """
        Test setPeriodBegin method sets the beginning period correctly.
        """
        info = LifeCycleInfo()

        # Create mock LifeCyclePeriod instance
        period = LifeCyclePeriod()

        # Set the beginning period
        result = info.setPeriodBegin(period)
        assert result is info  # Verify method chaining
        assert info.getPeriodBegin() == period

    def test_set_period_begin_none(self):
        """
        Test setPeriodBegin method handles None value correctly.
        """
        info = LifeCycleInfo()

        # Set initial value
        initial_period = LifeCyclePeriod()
        info.setPeriodBegin(initial_period)
        assert info.getPeriodBegin() == initial_period

        # Set to None - should not change the value (per implementation logic)
        result = info.setPeriodBegin(None)
        assert result is info  # Verify method chaining
        # Value should remain unchanged due to "if value is not None" check
        assert info.getPeriodBegin() == initial_period

    def test_get_period_end(self):
        """
        Test getPeriodEnd method returns None by default.
        """
        info = LifeCycleInfo()

        # Verify initial state
        period_end = info.getPeriodEnd()
        assert period_end is None

    def test_set_period_end(self):
        """
        Test setPeriodEnd method sets the ending period correctly.
        """
        info = LifeCycleInfo()

        # Create mock LifeCyclePeriod instance
        period = LifeCyclePeriod()

        # Set the ending period
        result = info.setPeriodEnd(period)
        assert result is info  # Verify method chaining
        assert info.getPeriodEnd() == period

    def test_set_period_end_none(self):
        """
        Test setPeriodEnd method handles None value correctly.
        """
        info = LifeCycleInfo()

        # Set initial value
        initial_period = LifeCyclePeriod()
        info.setPeriodEnd(initial_period)
        assert info.getPeriodEnd() == initial_period

        # Set to None - should not change the value (per implementation logic)
        result = info.setPeriodEnd(None)
        assert result is info  # Verify method chaining
        # Value should remain unchanged due to "if value is not None" check
        assert info.getPeriodEnd() == initial_period

    def test_get_remark(self):
        """
        Test getRemark method returns None by default.
        """
        info = LifeCycleInfo()

        # Verify initial state
        remark = info.getRemark()
        assert remark is None

    def test_set_remark(self):
        """
        Test setRemark method sets the remark documentation correctly.
        """
        info = LifeCycleInfo()

        # Create mock DocumentationBlock instance
        remark = DocumentationBlock()

        # Set the remark documentation
        result = info.setRemark(remark)
        assert result is info  # Verify method chaining
        assert info.getRemark() == remark

    def test_set_remark_none(self):
        """
        Test setRemark method handles None value correctly.
        """
        info = LifeCycleInfo()

        # Set initial value
        initial_remark = DocumentationBlock()
        info.setRemark(initial_remark)
        assert info.getRemark() == initial_remark

        # Set to None - should not change the value (per implementation logic)
        result = info.setRemark(None)
        assert result is info  # Verify method chaining
        # Value should remain unchanged due to "if value is not None" check
        assert info.getRemark() == initial_remark

    def test_get_use_instead_refs(self):
        """
        Test getUseInsteadRefs method returns empty list by default.
        """
        info = LifeCycleInfo()

        # Verify initial state
        refs = info.getUseInsteadRefs()
        assert refs == []
        assert isinstance(refs, list)

    def test_add_use_instead_ref(self):
        """
        Test addUseInsteadRef method adds references correctly.
        """
        info = LifeCycleInfo()

        # Create mock RefType instances
        ref1 = RefType().setValue("Ref1")
        ref2 = RefType().setValue("Ref2")

        # Add first reference
        result = info.addUseInsteadRef(ref1)
        assert result is info  # Verify method chaining
        assert info.getUseInsteadRefs() == [ref1]

        # Add second reference
        info.addUseInsteadRef(ref2)
        assert info.getUseInsteadRefs() == [ref1, ref2]

    def test_add_use_instead_ref_none(self):
        """
        Test addUseInsteadRef method handles None value correctly.
        """
        info = LifeCycleInfo()

        # Add None value - should not add to list
        result = info.addUseInsteadRef(None)
        assert result is info  # Verify method chaining
        assert info.getUseInsteadRefs() == []


class TestLifeCycleInfoSet:
    """
    Test class for LifeCycleInfoSet functionality.
    """

    def test_initialization(self):
        """
        Test LifeCycleInfoSet initialization with parent and short name.
        """
        # Create parent AUTOSAR structure
        parent = AUTOSAR.getInstance()
        ar_root = parent.createARPackage("AUTOSAR")

        # Create LifeCycleInfoSet instance
        info_set = LifeCycleInfoSet(ar_root, "TestLifeCycleInfoSet")

        # Verify basic properties
        assert info_set is not None
        assert info_set.getShortName() == "TestLifeCycleInfoSet"

        # Verify default values for attributes (inherited and specific)
        assert info_set.getDefaultLcStateRef() is None
        assert info_set.getDefaultPeriodBegin() is None
        assert info_set.getDefaultPeriodEnd() is None
        assert info_set.getLifeCycleInfos() == []
        assert info_set.getUsedLifeCycleStateDefinitionGroupRef() is None

    def test_get_default_lc_state_ref(self):
        """
        Test getDefaultLcStateRef method returns None by default.
        """
        parent = AUTOSAR.getInstance()
        ar_root = parent.createARPackage("AUTOSAR")
        info_set = LifeCycleInfoSet(ar_root, "TestLifeCycleInfoSet")

        # Verify initial state
        state_ref = info_set.getDefaultLcStateRef()
        assert state_ref is None

    def test_set_default_lc_state_ref(self):
        """
        Test setDefaultLcStateRef method sets the default life cycle state reference correctly.
        """
        parent = AUTOSAR.getInstance()
        ar_root = parent.createARPackage("AUTOSAR")
        info_set = LifeCycleInfoSet(ar_root, "TestLifeCycleInfoSet")

        # Create mock RefType instance
        state_ref = RefType().setValue("/Package/DefaultState")

        # Set the default life cycle state reference
        result = info_set.setDefaultLcStateRef(state_ref)
        assert result is info_set  # Verify method chaining
        assert info_set.getDefaultLcStateRef() == state_ref

    def test_set_default_lc_state_ref_none(self):
        """
        Test setDefaultLcStateRef method handles None value correctly.
        """
        parent = AUTOSAR.getInstance()
        ar_root = parent.createARPackage("AUTOSAR")
        info_set = LifeCycleInfoSet(ar_root, "TestLifeCycleInfoSet")

        # Set initial value
        initial_ref = RefType().setValue("/Package/DefaultState")
        info_set.setDefaultLcStateRef(initial_ref)
        assert info_set.getDefaultLcStateRef() == initial_ref

        # Set to None - should not change the value (per implementation logic)
        result = info_set.setDefaultLcStateRef(None)
        assert result is info_set  # Verify method chaining
        # Value should remain unchanged due to "if value is not None" check
        assert info_set.getDefaultLcStateRef() == initial_ref

    def test_get_default_period_begin(self):
        """
        Test getDefaultPeriodBegin method returns None by default.
        """
        parent = AUTOSAR.getInstance()
        ar_root = parent.createARPackage("AUTOSAR")
        info_set = LifeCycleInfoSet(ar_root, "TestLifeCycleInfoSet")

        # Verify initial state
        period_begin = info_set.getDefaultPeriodBegin()
        assert period_begin is None

    def test_set_default_period_begin(self):
        """
        Test setDefaultPeriodBegin method sets the default beginning period correctly.
        """
        parent = AUTOSAR.getInstance()
        ar_root = parent.createARPackage("AUTOSAR")
        info_set = LifeCycleInfoSet(ar_root, "TestLifeCycleInfoSet")

        # Create mock LifeCyclePeriod instance
        period = LifeCyclePeriod()

        # Set the default beginning period
        result = info_set.setDefaultPeriodBegin(period)
        assert result is info_set  # Verify method chaining
        assert info_set.getDefaultPeriodBegin() == period

    def test_set_default_period_begin_none(self):
        """
        Test setDefaultPeriodBegin method handles None value correctly.
        """
        parent = AUTOSAR.getInstance()
        ar_root = parent.createARPackage("AUTOSAR")
        info_set = LifeCycleInfoSet(ar_root, "TestLifeCycleInfoSet")

        # Set initial value
        initial_period = LifeCyclePeriod()
        info_set.setDefaultPeriodBegin(initial_period)
        assert info_set.getDefaultPeriodBegin() == initial_period

        # Set to None - should not change the value (per implementation logic)
        result = info_set.setDefaultPeriodBegin(None)
        assert result is info_set  # Verify method chaining
        # Value should remain unchanged due to "if value is not None" check
        assert info_set.getDefaultPeriodBegin() == initial_period

    def test_get_default_period_end(self):
        """
        Test getDefaultPeriodEnd method returns None by default.
        """
        parent = AUTOSAR.getInstance()
        ar_root = parent.createARPackage("AUTOSAR")
        info_set = LifeCycleInfoSet(ar_root, "TestLifeCycleInfoSet")

        # Verify initial state
        period_end = info_set.getDefaultPeriodEnd()
        assert period_end is None

    def test_set_default_period_end(self):
        """
        Test setDefaultPeriodEnd method sets the default ending period correctly.
        """
        parent = AUTOSAR.getInstance()
        ar_root = parent.createARPackage("AUTOSAR")
        info_set = LifeCycleInfoSet(ar_root, "TestLifeCycleInfoSet")

        # Create mock LifeCyclePeriod instance
        period = LifeCyclePeriod()

        # Set the default ending period
        result = info_set.setDefaultPeriodEnd(period)
        assert result is info_set  # Verify method chaining
        assert info_set.getDefaultPeriodEnd() == period

    def test_set_default_period_end_none(self):
        """
        Test setDefaultPeriodEnd method handles None value correctly.
        """
        parent = AUTOSAR.getInstance()
        ar_root = parent.createARPackage("AUTOSAR")
        info_set = LifeCycleInfoSet(ar_root, "TestLifeCycleInfoSet")

        # Set initial value
        initial_period = LifeCyclePeriod()
        info_set.setDefaultPeriodEnd(initial_period)
        assert info_set.getDefaultPeriodEnd() == initial_period

        # Set to None - should not change the value (per implementation logic)
        result = info_set.setDefaultPeriodEnd(None)
        assert result is info_set  # Verify method chaining
        # Value should remain unchanged due to "if value is not None" check
        assert info_set.getDefaultPeriodEnd() == initial_period

    def test_get_life_cycle_infos(self):
        """
        Test getLifeCycleInfos method returns empty list by default.
        """
        parent = AUTOSAR.getInstance()
        ar_root = parent.createARPackage("AUTOSAR")
        info_set = LifeCycleInfoSet(ar_root, "TestLifeCycleInfoSet")

        # Verify initial state
        infos = info_set.getLifeCycleInfos()
        assert infos == []
        assert isinstance(infos, list)

    def test_add_life_cycle_info(self):
        """
        Test addLifeCycleInfo method adds life cycle information correctly.
        """
        parent = AUTOSAR.getInstance()
        ar_root = parent.createARPackage("AUTOSAR")
        info_set = LifeCycleInfoSet(ar_root, "TestLifeCycleInfoSet")

        # Create mock LifeCycleInfo instances
        info1 = LifeCycleInfo()
        info2 = LifeCycleInfo()

        # Add first info
        result = info_set.addLifeCycleInfo(info1)
        assert result is info_set  # Verify method chaining
        assert info_set.getLifeCycleInfos() == [info1]

        # Add second info
        info_set.addLifeCycleInfo(info2)
        assert info_set.getLifeCycleInfos() == [info1, info2]

    def test_add_life_cycle_info_none(self):
        """
        Test addLifeCycleInfo method handles None value correctly.
        """
        parent = AUTOSAR.getInstance()
        ar_root = parent.createARPackage("AUTOSAR")
        info_set = LifeCycleInfoSet(ar_root, "TestLifeCycleInfoSet")

        # Add None value - should not add to list
        result = info_set.addLifeCycleInfo(None)
        assert result is info_set  # Verify method chaining
        assert info_set.getLifeCycleInfos() == []

    def test_get_used_life_cycle_state_definition_group_ref(self):
        """
        Test getUsedLifeCycleStateDefinitionGroupRef method returns None by default.
        """
        parent = AUTOSAR.getInstance()
        ar_root = parent.createARPackage("AUTOSAR")
        info_set = LifeCycleInfoSet(ar_root, "TestLifeCycleInfoSet")

        # Verify initial state
        ref = info_set.getUsedLifeCycleStateDefinitionGroupRef()
        assert ref is None

    def test_set_used_life_cycle_state_definition_group_ref(self):
        """
        Test setUsedLifeCycleStateDefinitionGroupRef method sets the reference correctly.
        """
        parent = AUTOSAR.getInstance()
        ar_root = parent.createARPackage("AUTOSAR")
        info_set = LifeCycleInfoSet(ar_root, "TestLifeCycleInfoSet")

        # Create mock RefType instance
        ref = RefType().setValue("/Package/StateGroup")

        # Set the reference
        result = info_set.setUsedLifeCycleStateDefinitionGroupRef(ref)
        assert result is info_set  # Verify method chaining
        assert info_set.getUsedLifeCycleStateDefinitionGroupRef() == ref

    def test_set_used_life_cycle_state_definition_group_ref_none(self):
        """
        Test setUsedLifeCycleStateDefinitionGroupRef method handles None value correctly.
        """
        parent = AUTOSAR.getInstance()
        ar_root = parent.createARPackage("AUTOSAR")
        info_set = LifeCycleInfoSet(ar_root, "TestLifeCycleInfoSet")

        # Set initial value
        initial_ref = RefType().setValue("/Package/StateGroup")
        info_set.setUsedLifeCycleStateDefinitionGroupRef(initial_ref)
        assert info_set.getUsedLifeCycleStateDefinitionGroupRef() == initial_ref

        # Set to None - should not change the value (per implementation logic)
        result = info_set.setUsedLifeCycleStateDefinitionGroupRef(None)
        assert result is info_set  # Verify method chaining
        # Value should remain unchanged due to "if value is not None" check
        assert info_set.getUsedLifeCycleStateDefinitionGroupRef() == initial_ref
