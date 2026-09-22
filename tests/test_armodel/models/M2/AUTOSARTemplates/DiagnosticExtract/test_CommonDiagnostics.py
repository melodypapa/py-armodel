"""Model tests for DiagnosticCommonElement (Table 4.1, p.33)."""

from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.DiagnosticExtract.CommonDiagnostics import DiagnosticCommonElement
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ARPackage import ARElement
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable import Identifiable

NOTE = "This meta-class represents a common base class for all diagnostic elements. It does not contribute any specific functionality other than the ability to become the target of a reference."


def _pkg():
    return AUTOSAR.getInstance().createARPackage("DiagPkg")


class ConcreteDiagnosticCommonElement(DiagnosticCommonElement):
    def __init__(self, parent, short_name):
        super().__init__(parent, short_name)


class TestDiagnosticCommonElement:
    """Test cases for DiagnosticCommonElement class (Table 4.1, p.33)."""

    def test_is_abstract(self):
        try:
            DiagnosticCommonElement(_pkg(), "Dce")
            assert False, "DiagnosticCommonElement should not be instantiable"
        except TypeError:
            pass

    def test_is_arelement_subclass(self):
        assert issubclass(DiagnosticCommonElement, ARElement)
        assert issubclass(DiagnosticCommonElement, Identifiable)

    def test_concrete_subclass_initialization(self):
        obj = ConcreteDiagnosticCommonElement(_pkg(), "TestName")
        assert obj.getShortName() == "TestName"

    def test_class_docstring_is_spec_note_verbatim(self):
        assert DiagnosticCommonElement.__doc__ == NOTE

    def test_init_has_no_docstring(self):
        assert DiagnosticCommonElement.__init__.__doc__ is None

    def test_has_no_spec_attributes(self):
        obj = ConcreteDiagnosticCommonElement(_pkg(), "TestName")
        assert not hasattr(obj, "getDiagnosticCommonElements")
        assert not hasattr(obj, "addDiagnosticCommonElement")
