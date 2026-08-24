"""
This module contains tests for the BswSchedulerNamePrefix class in the
AUTOSAR BswModuleTemplate.BswBehavior module.
"""

from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.BswModuleTemplate.BswBehavior.BswSchedulerNamePrefix import (
    BswSchedulerNamePrefix,
)
from armodel.models.M2.AUTOSARTemplates.CommonStructure.Implementation import ImplementationProps
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import CIdentifier


class TestBswSchedulerNamePrefix:
    """
    Test class for BswSchedulerNamePrefix functionality.
    """

    def test_initialization(self):
        """BswSchedulerNamePrefix derives from ImplementationProps and has no own attributes."""
        parent = AUTOSAR.getInstance()
        ar_root = parent.createARPackage("AUTOSAR")
        obj = BswSchedulerNamePrefix(ar_root, "SchM_BswM")

        assert isinstance(obj, BswSchedulerNamePrefix)
        assert isinstance(obj, ImplementationProps)
        assert obj.getShortName() == "SchM_BswM"
        assert obj.getSymbol() is None

    def test_symbol_round_trip(self):
        """The prefix is carried by the inherited symbol attribute of ImplementationProps."""
        parent = AUTOSAR.getInstance()
        ar_root = parent.createARPackage("AUTOSAR")
        obj = BswSchedulerNamePrefix(ar_root, "SchM_BswM")

        symbol = CIdentifier()
        symbol.setValue("SchM_BswM_")
        result = obj.setSymbol(symbol)
        assert result is obj
        assert obj.getSymbol() == symbol

        # None is a no-op
        obj.setSymbol(None)
        assert obj.getSymbol() == symbol
