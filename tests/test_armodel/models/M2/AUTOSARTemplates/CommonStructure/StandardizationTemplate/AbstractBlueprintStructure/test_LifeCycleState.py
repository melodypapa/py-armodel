"""
This module contains tests for the LifeCycleState class in the
AbstractBlueprintStructure module (spec: AUTOSAR_FO_TPS_GenericStructureTemplate,
Table 12.2, p.388, R23-11).
"""

from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.CommonStructure.StandardizationTemplate.AbstractBlueprintStructure import (
    AtpBlueprint,
    AtpBlueprintable,
    LifeCycleState,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable import (
    Identifiable,
    MultilanguageReferrable,
    Referrable,
)


class TestLifeCycleState:
    """
    Test class for LifeCycleState functionality (Table 12.2, p.388).
    """

    def test_concrete_instantiation(self):
        """
        Table 12.2 does not mark LifeCycleState abstract (it is the concrete
        LIFE-CYCLE-STATE element aggregated by
        LifeCycleStateDefinitionGroup.lcState), so it must be directly instantiable.
        """
        parent = AUTOSAR.getInstance()
        ar_root = parent.createARPackage("AUTOSAR")

        obj = LifeCycleState(ar_root, "valid")
        assert obj is not None
        assert obj.getShortName() == "valid"
        assert obj.getParent() == ar_root

    def test_direct_base_is_atp_blueprint(self):
        """
        Rule 0001.2 / 0001.11: the Base row of Table 12.2 lists ARObject,
        AtpBlueprint, AtpBlueprintable, Identifiable, MultilanguageReferrable,
        Referrable; the most-derived base is AtpBlueprint.
        """
        assert LifeCycleState.__bases__[0] is AtpBlueprint

    def test_mro_has_spec_closure(self):
        """
        Rule 0001.11: the Base closure of Table 12.2 is ARObject, AtpBlueprint,
        AtpBlueprintable, Identifiable, MultilanguageReferrable, Referrable.
        AtpBlueprintable is part of the closure but NOT of the MRO (AtpBlueprint
        derives from Identifiable), mirroring the AtpBlueprint heritage.
        """
        for base in (AtpBlueprint, Identifiable, MultilanguageReferrable, Referrable, ARObject):
            assert base in LifeCycleState.__mro__, "%s missing from MRO" % base
        assert AtpBlueprintable not in LifeCycleState.__mro__

    def test_no_own_members(self):
        """
        Table 12.2 lists no Attribute rows (the attribute section carries only the
        "-" placeholder row): LifeCycleState contributes no own fields or methods
        beyond the AtpBlueprint base.
        """
        own = [name for name, value in LifeCycleState.__dict__.items() if not name.startswith("_")]
        assert own == [], "LifeCycleState must define no own members, found: %s" % own

    def test_initialization_defaults(self):
        """
        The inherited blueprintPolicys aggregation starts as an empty list.
        """
        parent = AUTOSAR.getInstance()
        ar_root = parent.createARPackage("AUTOSAR")

        obj = LifeCycleState(ar_root, "valid")
        assert obj.blueprintPolicys == []
        assert obj.getBlueprintPolicys() == []

    def test_inherited_add_get_blueprint_policys(self):
        """
        addBlueprintPolicy/getBlueprintPolicys inherited from AtpBlueprint work on
        LifeCycleState (incl. None no-op).
        """
        parent = AUTOSAR.getInstance()
        ar_root = parent.createARPackage("AUTOSAR")

        obj = LifeCycleState(ar_root, "valid")

        value = ARObject.__new__(ARObject)
        assert obj.addBlueprintPolicy(value) is obj
        assert obj.getBlueprintPolicys() == [value]

        obj.addBlueprintPolicy(None)
        assert obj.getBlueprintPolicys() == [value]

    def test_class_docstring_verbatim(self):
        """
        Rule 0001.4 / 0012.2.4: class docstring == spec Table 12.2 Note verbatim
        (AUTOSAR_FO_TPS_GenericStructureTemplate, p.388).
        """
        assert LifeCycleState.__doc__ == "This meta class represents one particular state in the LifeCycle."
