from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.DiagnosticExtract.DiagnosticMapping.ServiceMapping import (
    BswServiceDependencyIdent,
)


class TestBswServiceDependencyIdent:
    """Test cases for BswServiceDependencyIdent class - allows a non-Referrable BswServiceDependency to become the target of a reference."""

    def test_initialization(self):
        document = AUTOSAR.getInstance()
        ar_root = document.createARPackage("AUTOSAR")
        ident = BswServiceDependencyIdent(ar_root, "test_ident")

        assert ident.short_name == "test_ident"
