"""
This module contains tests for the SwComponentType class in the
AUTOSAR SWComponentTemplate module.
"""

from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.SwComponentType import (
    SwComponentType,
)


class TestSwComponentType:
    """
    Test class for SwComponentType functionality.
    """

    def test_abstract_initialization(self):
        parent = AUTOSAR.getInstance()
        ar_root = parent.createARPackage("AUTOSAR")
        try:
            _obj = SwComponentType(ar_root, "TestSwComponentType")
            assert False, "SwComponentType should not be instantiable"
        except TypeError:
            pass

    def test_concrete_subclass_initialization(self):
        parent = AUTOSAR.getInstance()
        ar_root = parent.createARPackage("AUTOSAR")

        class ConcreteSwComponentType(SwComponentType):
            def __init__(self, parent, short_name):
                super().__init__(parent, short_name)

        obj = ConcreteSwComponentType(ar_root, "TestName")
        assert obj.getShortName() == "TestName"
