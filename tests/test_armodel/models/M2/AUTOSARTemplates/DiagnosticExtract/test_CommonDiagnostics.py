"""
This module contains tests for the DiagnosticCommonElement class in the
AUTOSAR DiagnosticExtract module.
"""

from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.DiagnosticExtract.CommonDiagnostics import (
    DiagnosticCommonElement,
)


class TestDiagnosticCommonElement:
    """
    Test class for DiagnosticCommonElement functionality.
    """

    def test_abstract_initialization(self):
        parent = AUTOSAR.getInstance()
        ar_root = parent.createARPackage("AUTOSAR")
        try:
            _obj = DiagnosticCommonElement(ar_root, "TestDiagnosticCommonElement")
            assert False, "DiagnosticCommonElement should not be instantiable"
        except TypeError:
            pass

    def test_concrete_subclass_initialization(self):
        parent = AUTOSAR.getInstance()
        ar_root = parent.createARPackage("AUTOSAR")

        class ConcreteDiagnosticCommonElement(DiagnosticCommonElement):
            def __init__(self, parent, short_name):
                super().__init__(parent, short_name)

        obj = ConcreteDiagnosticCommonElement(ar_root, "TestName")
        assert obj.getShortName() == "TestName"
