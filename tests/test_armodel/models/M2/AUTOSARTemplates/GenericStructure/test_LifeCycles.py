"""
This module contains comprehensive tests for the LifeCycles.py file
in the AUTOSAR GenericStructure module.
"""

import inspect
import re
import typing

from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import DateTime, RefType, RevisionLabelString
from armodel.models.M2.AUTOSARTemplates.GenericStructure.LifeCycles import LifeCycleInfo, LifeCycleInfoSet, LifeCyclePeriod
from armodel.models.M2.MSR.Documentation.TextModel.BlockElements import DocumentationBlock


class TestLifeCyclePeriod:
    """
    Test class for LifeCyclePeriod functionality.
    """

    def test_class_docstring_verbatim(self):
        """
        Test that the class docstring is the Table 12.4 Note verbatim.
        """
        assert (
            LifeCyclePeriod.__doc__.strip()
            == "This meta class represents the ability to specify a point of time within a specified period, e.g. the starting or end point, in which a specific life cycle state is valid/applies to."
        )

    def test_init_has_no_docstring(self):
        """
        Test that __init__ has no docstring (spec Notes live in inline member comments).
        """
        assert LifeCyclePeriod.__init__.__doc__ is None

    def test_ar_release_version_typed_revision_label_string(self):
        """
        Test that arReleaseVersion is typed RevisionLabelString per Table 12.4 (getter/setter annotations).
        """
        getter_hints = typing.get_type_hints(LifeCyclePeriod.getArReleaseVersion)
        assert getter_hints.get("return") == typing.Optional[RevisionLabelString]

        setter_hints = typing.get_type_hints(LifeCyclePeriod.setArReleaseVersion)
        assert setter_hints.get("value") == typing.Optional[RevisionLabelString]
        assert setter_hints.get("return") is LifeCyclePeriod

    def test_date_typed_date_time(self):
        """
        Test that date is typed DateTime per Table 12.4 (getter/setter annotations).
        """
        getter_hints = typing.get_type_hints(LifeCyclePeriod.getDate)
        assert getter_hints.get("return") == typing.Optional[DateTime]

        setter_hints = typing.get_type_hints(LifeCyclePeriod.setDate)
        assert setter_hints.get("value") == typing.Optional[DateTime]
        assert setter_hints.get("return") is LifeCyclePeriod

    def test_product_release_typed_revision_label_string(self):
        """
        Test that productRelease is typed RevisionLabelString per Table 12.4 (getter/setter annotations).
        """
        getter_hints = typing.get_type_hints(LifeCyclePeriod.getProductRelease)
        assert getter_hints.get("return") == typing.Optional[RevisionLabelString]

        setter_hints = typing.get_type_hints(LifeCyclePeriod.setProductRelease)
        assert setter_hints.get("value") == typing.Optional[RevisionLabelString]
        assert setter_hints.get("return") is LifeCyclePeriod

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

        # Create DateTime instance per Table 12.4
        test_date = DateTime().setValue("2023-06-15T12:00:00+01:00")

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
        initial_date = DateTime().setValue("2023-06-15T12:00:00+01:00")
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


class TestLifeCycleInfoSpecContract:
    """
    Spec-contract pins for LifeCycleInfo (R23-11 FO_TPS_GenericStructureTemplate Table 12.5).
    """

    def test_class_docstring_verbatim(self):
        """
        Test that the class docstring is the Table 12.5 Note verbatim.
        """
        assert LifeCycleInfo.__doc__.strip() == "LifeCycleInfo describes the life cycle state of an element together with additional information like what to use instead"

    def test_init_has_no_docstring(self):
        """
        Test that __init__ has no docstring (spec Notes live in inline member comments).
        """
        assert LifeCycleInfo.__init__.__doc__ is None

    def test_exact_own_field_set(self):
        """
        Test that __init__ declares exactly the six Table 12.5 attributes in displayed row order.
        """
        source = inspect.getsource(LifeCycleInfo.__init__)
        assert re.findall(r"self\.(\w+)\s*:", source) == [
            "lcObjectRef",
            "lcStateRef",
            "periodBegin",
            "periodEnd",
            "remark",
            "useInsteadRefs",
        ]

    def test_pep526_annotated_members(self):
        """
        Test that every member is a PEP 526 annotated assignment with the spec type and no trailing '# type:' comment.
        """
        source = inspect.getsource(LifeCycleInfo.__init__)
        assert re.search(r"self\.lcObjectRef:\s*Optional\[RefType\]\s*=\s*None", source)
        assert re.search(r"self\.lcStateRef:\s*Optional\[RefType\]\s*=\s*None", source)
        assert re.search(r"self\.periodBegin:\s*Optional\[LifeCyclePeriod\]\s*=\s*None", source)
        assert re.search(r"self\.periodEnd:\s*Optional\[LifeCyclePeriod\]\s*=\s*None", source)
        assert re.search(r"self\.remark:\s*Optional\[DocumentationBlock\]\s*=\s*None", source)
        assert re.search(r"self\.useInsteadRefs:\s*List\[RefType\]\s*=\s*\[\]", source)
        assert "# type:" not in source

    def test_most_derived_base_ar_object(self):
        """
        Test that the most-derived base is ARObject per the Table 12.5 Base row (XSD 00052 complexType LIFE-CYCLE-INFO L76608).
        """
        assert LifeCycleInfo.__bases__ == (ARObject,)

    def test_accessor_order(self):
        """
        Test that accessors follow the displayed row order with get/set pairs (getUseInsteadRefs/addUseInsteadRef for the * ref).
        """
        source = inspect.getsource(LifeCycleInfo)
        assert re.findall(r"def (\w+)\(", source) == [
            "__init__",
            "getLcObjectRef",
            "setLcObjectRef",
            "getLcStateRef",
            "setLcStateRef",
            "getPeriodBegin",
            "setPeriodBegin",
            "getPeriodEnd",
            "setPeriodEnd",
            "getRemark",
            "setRemark",
            "getUseInsteadRefs",
            "addUseInsteadRef",
        ]

    def test_lc_object_ref_typed(self):
        """
        Test that lcObjectRef accessors carry the Table 12.5 RefType annotations.
        """
        getter_hints = typing.get_type_hints(LifeCycleInfo.getLcObjectRef)
        assert getter_hints.get("return") == typing.Optional[RefType]

        setter_hints = typing.get_type_hints(LifeCycleInfo.setLcObjectRef)
        assert setter_hints.get("value") == typing.Optional[RefType]
        assert setter_hints.get("return") is LifeCycleInfo

    def test_lc_state_ref_typed(self):
        """
        Test that lcStateRef accessors carry the Table 12.5 RefType annotations.
        """
        getter_hints = typing.get_type_hints(LifeCycleInfo.getLcStateRef)
        assert getter_hints.get("return") == typing.Optional[RefType]

        setter_hints = typing.get_type_hints(LifeCycleInfo.setLcStateRef)
        assert setter_hints.get("value") == typing.Optional[RefType]
        assert setter_hints.get("return") is LifeCycleInfo

    def test_period_begin_typed(self):
        """
        Test that periodBegin accessors carry the Table 12.5 LifeCyclePeriod annotations.
        """
        getter_hints = typing.get_type_hints(LifeCycleInfo.getPeriodBegin)
        assert getter_hints.get("return") == typing.Optional[LifeCyclePeriod]

        setter_hints = typing.get_type_hints(LifeCycleInfo.setPeriodBegin)
        assert setter_hints.get("value") == typing.Optional[LifeCyclePeriod]
        assert setter_hints.get("return") is LifeCycleInfo

    def test_period_end_typed(self):
        """
        Test that periodEnd accessors carry the Table 12.5 LifeCyclePeriod annotations.
        """
        getter_hints = typing.get_type_hints(LifeCycleInfo.getPeriodEnd)
        assert getter_hints.get("return") == typing.Optional[LifeCyclePeriod]

        setter_hints = typing.get_type_hints(LifeCycleInfo.setPeriodEnd)
        assert setter_hints.get("value") == typing.Optional[LifeCyclePeriod]
        assert setter_hints.get("return") is LifeCycleInfo

    def test_remark_typed(self):
        """
        Test that remark accessors carry the Table 12.5 DocumentationBlock annotations.
        """
        getter_hints = typing.get_type_hints(LifeCycleInfo.getRemark)
        assert getter_hints.get("return") == typing.Optional[DocumentationBlock]

        setter_hints = typing.get_type_hints(LifeCycleInfo.setRemark)
        assert setter_hints.get("value") == typing.Optional[DocumentationBlock]
        assert setter_hints.get("return") is LifeCycleInfo

    def test_use_instead_refs_typed(self):
        """
        Test that useInsteadRefs accessors carry the Table 12.5 List[RefType] annotations.
        """
        getter_hints = typing.get_type_hints(LifeCycleInfo.getUseInsteadRefs)
        assert getter_hints.get("return") == typing.List[RefType]

        add_hints = typing.get_type_hints(LifeCycleInfo.addUseInsteadRef)
        assert add_hints.get("value") == typing.Optional[RefType]
        assert add_hints.get("return") is LifeCycleInfo

    def test_member_docstrings_verbatim(self):
        """
        Test that every member docstring is the Table 12.5 Note verbatim (setters/add append the None no-op sentence).
        """
        assert LifeCycleInfo.getLcObjectRef.__doc__.strip() == "Element(s) have the life cycle as described in lcState."
        assert (
            LifeCycleInfo.setLcObjectRef.__doc__.strip()
            == "Element(s) have the life cycle as described in lcState. A None value is a no-op and does not overwrite an existing life cycle object reference."
        )
        assert (
            LifeCycleInfo.getLcStateRef.__doc__.strip()
            == "This denotes the particular state assigned to the object. If no lcState is given then the default life cycle state of LifeCycleInfoSet is assumed."
        )
        assert (
            LifeCycleInfo.setLcStateRef.__doc__.strip()
            == "This denotes the particular state assigned to the object. If no lcState is given then the default life cycle state of LifeCycleInfoSet is assumed. A None value is a no-op and does not overwrite an existing life cycle state."
        )
        assert (
            LifeCycleInfo.getPeriodBegin.__doc__.strip()
            == "Starting point of period in which the element has the denoted life cycle state lcState. If no periodBegin is given then the default period begin of LifeCycleInfoSet is assumed."
        )
        assert (
            LifeCycleInfo.setPeriodBegin.__doc__.strip()
            == "Starting point of period in which the element has the denoted life cycle state lcState. If no periodBegin is given then the default period begin of LifeCycleInfoSet is assumed. A None value is a no-op and does not overwrite an existing period begin."
        )
        assert (
            LifeCycleInfo.getPeriodEnd.__doc__.strip()
            == "Expiry date, i.e. end point of period the element does not have the denoted life cycle state lcState any more. If no periodEnd is given then the default period begin of LifeCycleInfoSet is assumed."
        )
        assert (
            LifeCycleInfo.setPeriodEnd.__doc__.strip()
            == "Expiry date, i.e. end point of period the element does not have the denoted life cycle state lcState any more. If no periodEnd is given then the default period begin of LifeCycleInfoSet is assumed. A None value is a no-op and does not overwrite an existing period end."
        )
        assert LifeCycleInfo.getRemark.__doc__.strip() == "Remark describing for example • why the element was given the specified life cycle • the semantics of useInstead"
        assert (
            LifeCycleInfo.setRemark.__doc__.strip()
            == "Remark describing for example • why the element was given the specified life cycle • the semantics of useInstead A None value is a no-op and does not overwrite an existing remark."
        )
        assert (
            LifeCycleInfo.getUseInsteadRefs.__doc__.strip()
            == 'Element(s) that should be used instead of the one denoted in referrable. Only relevant in case of life cycle states lcState unlike "valid". In case there are multiple references the exact semantics shall be individually described in the remark.'
        )
        assert (
            LifeCycleInfo.addUseInsteadRef.__doc__.strip()
            == 'Element(s) that should be used instead of the one denoted in referrable. Only relevant in case of life cycle states lcState unlike "valid". In case there are multiple references the exact semantics shall be individually described in the remark. A None value is a no-op and does not add to useInsteadRefs.'
        )

    def test_inline_init_comments_verbatim(self):
        """
        Test that the inline __init__ member comments carry the Table 12.5 Notes verbatim.
        """
        source = inspect.getsource(LifeCycleInfo.__init__)
        assert "# Element(s) have the life cycle as described in lcState." in source
        assert "# This denotes the particular state assigned to the object. If no lcState is given then the default life cycle state of LifeCycleInfoSet is assumed." in source
        assert (
            "# Starting point of period in which the element has the denoted life cycle state lcState. If no periodBegin is given then the default period begin of LifeCycleInfoSet is assumed."
            in source
        )
        assert (
            "# Expiry date, i.e. end point of period the element does not have the denoted life cycle state lcState any more. If no periodEnd is given then the default period begin of LifeCycleInfoSet is assumed."
            in source
        )
        assert "# Remark describing for example • why the element was given the specified life cycle • the semantics of useInstead" in source
        assert (
            '# Element(s) that should be used instead of the one denoted in referrable. Only relevant in case of life cycle states lcState unlike "valid". In case there are multiple references the exact semantics shall be individually described in the remark.'
            in source
        )


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
