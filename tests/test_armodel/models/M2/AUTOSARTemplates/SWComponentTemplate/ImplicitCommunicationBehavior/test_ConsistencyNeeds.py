"""
This module contains the model tests for the synced ConsistencyNeeds class
(Swc TPS Table 4.99): base chain, initialization defaults, create*/get*
semantics, verbatim spec Note docstrings, and typing pins.
"""

import inspect
import typing
from typing import List

from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.CommonStructure.StandardizationTemplate.AbstractBlueprintStructure import AtpBlueprint
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.StereotypeMixins import VariationPointCapable
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.ImplicitCommunicationBehavior import (
    ConsistencyNeeds,
    DataPrototypeGroup,
    RunnableEntityGroup,
)


class TestConsistencyNeeds:
    """Test class for the ConsistencyNeeds class (Swc TPS Table 4.99)."""

    def test_spec_base(self):
        """Test the most-derived spec base and VP capability (Table 4.99 Base chain: AtpBlueprint; XSD anchors VARIATION-POINT)."""
        document = AUTOSAR.getInstance()
        ar_root = document.createARPackage("AUTOSAR")
        assert issubclass(ConsistencyNeeds, AtpBlueprint)
        assert issubclass(ConsistencyNeeds, VariationPointCapable)
        consistency_needs = ConsistencyNeeds(ar_root, "BaseNeeds")
        assert consistency_needs.parent == ar_root
        assert consistency_needs.short_name == "BaseNeeds"

    def test_initialization(self):
        """Test all __init__ field defaults per Table 4.99."""
        document = AUTOSAR.getInstance()
        ar_root = document.createARPackage("AUTOSAR")
        consistency_needs = ConsistencyNeeds(ar_root, "DefaultsNeeds")
        assert consistency_needs.dpgDoesNotRequireCoherencys == []
        assert consistency_needs.dpgRequiresCoherencys == []
        assert consistency_needs.regDoesNotRequireStabilitys == []
        assert consistency_needs.regRequiresStabilitys == []
        assert consistency_needs.getDpgDoesNotRequireCoherencys() == []
        assert consistency_needs.getDpgRequiresCoherencys() == []
        assert consistency_needs.getRegDoesNotRequireStabilitys() == []
        assert consistency_needs.getRegRequiresStabilitys() == []
        assert consistency_needs.getBlueprintPolicys() == []
        assert consistency_needs.getVariationPoint() is None

    def test_class_docstring_note_verbatim(self):
        """Test the class docstring is the spec Note verbatim (Table 4.99)."""
        expected = "This meta-class represents the ability to define requirements on the implicit communication behavior."
        assert inspect.cleandoc(ConsistencyNeeds.__doc__) == expected

    def test_init_docless(self):
        """Test __init__ has no docstring (Rule 0012.2.4)."""
        assert ConsistencyNeeds.__init__.__doc__ is None

    def test_spec_notes_are_verbatim(self):
        """Test per-attribute Note texts are verbatim in the create*/get* docstrings (Table 4.99)."""
        expected_notes = {
            "createDpgDoesNotRequireCoherency": "This group of VariableDataPrototypes does not require coherency with respect to the implicit communication behavior.",
            "getDpgDoesNotRequireCoherencys": "This group of VariableDataPrototypes does not require coherency with respect to the implicit communication behavior.",
            "createDpgRequiresCoherency": "This group of VariableDataPrototypes requires coherency with respect to the implicit communication behavior, i.e. all read and write access to VariableDataPrototypes in the DataPrototypeGroup by the RunnableEntitys of the RunnableEntityGroup need to be handled in a coherent manner.",
            "getDpgRequiresCoherencys": "This group of VariableDataPrototypes requires coherency with respect to the implicit communication behavior, i.e. all read and write access to VariableDataPrototypes in the DataPrototypeGroup by the RunnableEntitys of the RunnableEntityGroup need to be handled in a coherent manner.",
            "createRegDoesNotRequireStability": "This group of RunnableEntities does not require stability with respect to the implicit communication behavior.",
            "getRegDoesNotRequireStabilitys": "This group of RunnableEntities does not require stability with respect to the implicit communication behavior.",
            "createRegRequiresStability": "This group of RunnableEntities requires stability with respect to the implicit communication behavior, i.e. all read and write access to VariableDataPrototypes in the DataPrototypeGroup by the RunnableEntitys of the RunnableEntityGroup need to be handled in a stable manner.",
            "getRegRequiresStabilitys": "This group of RunnableEntities requires stability with respect to the implicit communication behavior, i.e. all read and write access to VariableDataPrototypes in the DataPrototypeGroup by the RunnableEntitys of the RunnableEntityGroup need to be handled in a stable manner.",
        }
        for method, note in expected_notes.items():
            assert getattr(ConsistencyNeeds, method).__doc__.strip() == note

    def test_type_hints(self):
        """Test factory and getter annotations carry the spec * quota shape (Rule 0003); field form is gated by test_member_annotations."""
        for create, getter, child_type in [
            ("createDpgDoesNotRequireCoherency", "getDpgDoesNotRequireCoherencys", DataPrototypeGroup),
            ("createDpgRequiresCoherency", "getDpgRequiresCoherencys", DataPrototypeGroup),
            ("createRegDoesNotRequireStability", "getRegDoesNotRequireStabilitys", RunnableEntityGroup),
            ("createRegRequiresStability", "getRegRequiresStabilitys", RunnableEntityGroup),
        ]:
            hints = typing.get_type_hints(getattr(ConsistencyNeeds, create))
            assert hints.get("short_name") is str
            assert hints.get("return") is child_type
            hints = typing.get_type_hints(getattr(ConsistencyNeeds, getter))
            assert hints.get("return") == List[child_type]

    def test_create_dpg_does_not_require_coherency(self):
        """Test createDpgDoesNotRequireCoherency appends and a duplicate short name returns the existing element."""
        document = AUTOSAR.getInstance()
        ar_root = document.createARPackage("AUTOSAR")
        consistency_needs = ConsistencyNeeds(ar_root, "Needs")
        data_group = consistency_needs.createDpgDoesNotRequireCoherency("GroupA")
        assert isinstance(data_group, DataPrototypeGroup)
        assert consistency_needs.getDpgDoesNotRequireCoherencys() == [data_group]
        assert consistency_needs.createDpgDoesNotRequireCoherency("GroupA") is data_group

    def test_create_dpg_requires_coherency(self):
        """Test createDpgRequiresCoherency appends and a duplicate short name returns the existing element."""
        document = AUTOSAR.getInstance()
        ar_root = document.createARPackage("AUTOSAR")
        consistency_needs = ConsistencyNeeds(ar_root, "Needs")
        data_group = consistency_needs.createDpgRequiresCoherency("GroupB")
        assert isinstance(data_group, DataPrototypeGroup)
        assert consistency_needs.getDpgRequiresCoherencys() == [data_group]
        assert consistency_needs.createDpgRequiresCoherency("GroupB") is data_group

    def test_create_reg_does_not_require_stability(self):
        """Test createRegDoesNotRequireStability appends and a duplicate short name returns the existing element."""
        document = AUTOSAR.getInstance()
        ar_root = document.createARPackage("AUTOSAR")
        consistency_needs = ConsistencyNeeds(ar_root, "Needs")
        runnable_group = consistency_needs.createRegDoesNotRequireStability("GroupC")
        assert isinstance(runnable_group, RunnableEntityGroup)
        assert consistency_needs.getRegDoesNotRequireStabilitys() == [runnable_group]
        assert consistency_needs.createRegDoesNotRequireStability("GroupC") is runnable_group

    def test_create_reg_requires_stability(self):
        """Test createRegRequiresStability appends and a duplicate short name returns the existing element."""
        document = AUTOSAR.getInstance()
        ar_root = document.createARPackage("AUTOSAR")
        consistency_needs = ConsistencyNeeds(ar_root, "Needs")
        runnable_group = consistency_needs.createRegRequiresStability("GroupD")
        assert isinstance(runnable_group, RunnableEntityGroup)
        assert consistency_needs.getRegRequiresStabilitys() == [runnable_group]
        assert consistency_needs.createRegRequiresStability("GroupD") is runnable_group
