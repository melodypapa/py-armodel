"""
This module contains tests for the AtpDefinition model class
(src/armodel/models/M2/AUTOSARTemplates/GenericStructure/RolesAndRights.py),
synced from AUTOSAR_FO_TPS_GenericStructureTemplate Table 11.3 (R23-11, p.383).
"""

from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable import (
    Identifiable,
    Referrable,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.RolesAndRights import AtpDefinition


class TestAtpDefinition:
    """
    Test class for the AtpDefinition abstract shell (Table 11.3).
    """

    SPEC_NOTE = (
        'This abstract meta class represents "definition"-elements which identify '
        "the respective values. For example the value of a particular system "
        "constant is identified by the definition of this system constant."
    )

    def test_abstract_initialization(self):
        """
        AtpDefinition cannot be instantiated directly (abstract class).
        """
        parent = AUTOSAR.getInstance()
        ar_root = parent.createARPackage("AUTOSAR")
        try:
            _obj = AtpDefinition(ar_root, "TestAtpDefinition")
            assert False, "AtpDefinition should not be instantiable"
        except TypeError as e:
            assert "abstract class" in str(e).lower()

    def test_direct_base_is_referrable(self):
        """
        Spec Table 11.3 Base closure = {ARObject, Referrable}; the most-derived
        direct base must be Referrable (not Identifiable, which is absent from the
        closure).
        """
        assert AtpDefinition.__bases__[0] is Referrable
        assert issubclass(AtpDefinition, Referrable)

    def test_not_identifiable(self):
        """
        Identifiable is NOT in the Table 11.3 Base closure, so AtpDefinition must
        not inherit it. (Subclasses that need uuid reach Identifiable through their
        own base, e.g. HwCategory via PackageableElement.)
        """
        assert Identifiable not in AtpDefinition.__mro__

    def test_concrete_subclass_initialization(self):
        """
        A concrete subclass reaches parent/short_name through the Referrable chain.
        """
        parent = AUTOSAR.getInstance()
        ar_root = parent.createARPackage("AUTOSAR")

        class ConcreteAtpDefinition(AtpDefinition):
            def __init__(self, parent, short_name):
                super().__init__(parent, short_name)

        obj = ConcreteAtpDefinition(ar_root, "ConcreteAtpDefinition")
        assert obj is not None
        assert obj.getShortName() == "ConcreteAtpDefinition"
        assert obj.getParent() == ar_root

    def test_class_docstring_matches_spec_note(self):
        """
        The class docstring must equal the verbatim Table 11.3 Note.
        """
        assert AtpDefinition.__doc__ == self.SPEC_NOTE
