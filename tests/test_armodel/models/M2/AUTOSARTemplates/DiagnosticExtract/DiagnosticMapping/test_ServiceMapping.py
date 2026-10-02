from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.DiagnosticExtract.DiagnosticMapping.ServiceMapping import (
    BswServiceDependencyIdent,
)

CLASS_NOTE = "This meta-class is created to add the ability to become the target of a reference to the non-Referrable BswServiceDependency."


class TestBswServiceDependencyIdent:
    """
    Test class for BswServiceDependencyIdent functionality.

    Spec: AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf, Table 5.16, p.240
    """

    def test_initialization(self):
        """
        Test that a concrete BswServiceDependencyIdent instantiates with the spec defaults.
        """
        document = AUTOSAR.getInstance()
        ar_root = document.createARPackage("AUTOSAR")
        ident = BswServiceDependencyIdent(ar_root, "test_ident")

        assert ident is not None
        assert ident.getShortName() == "test_ident"

    def test_class_docstring_is_spec_note_verbatim(self):
        """
        Test that the class docstring is the spec Note verbatim.
        """
        assert BswServiceDependencyIdent.__doc__ == CLASS_NOTE

    def test_init_has_no_docstring(self):
        """
        Test that __init__ carries no docstring.
        """
        assert BswServiceDependencyIdent.__init__.__doc__ is None
