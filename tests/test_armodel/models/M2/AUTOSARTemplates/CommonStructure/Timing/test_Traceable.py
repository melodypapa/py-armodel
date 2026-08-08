"""
This module contains tests for the Traceable class in the
AUTOSAR CommonStructure.Timing module.
"""

from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.CommonStructure.Timing.Traceable import (
    Traceable,
)


class TestTraceable:
    """
    Test class for Traceable functionality.
    """

    def test_abstract_initialization(self):
        parent = AUTOSAR.getInstance()
        ar_root = parent.createARPackage("AUTOSAR")
        try:
            _obj = Traceable(ar_root, "TestTraceable")
            assert False, "Traceable should not be instantiable"
        except TypeError:
            pass

    def test_concrete_subclass_initialization(self):
        parent = AUTOSAR.getInstance()
        ar_root = parent.createARPackage("AUTOSAR")

        class ConcreteTraceable(Traceable):
            def __init__(self, parent, short_name):
                super().__init__(parent, short_name)

        obj = ConcreteTraceable(ar_root, "TestName")
        assert obj.getShortName() == "TestName"
