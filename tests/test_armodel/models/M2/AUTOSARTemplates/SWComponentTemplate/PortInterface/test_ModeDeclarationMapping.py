import typing

from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import RefType
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.PortInterface import ModeDeclarationMapping

SPEC_NOTE = "This meta-class implements a concrete mapping of two ModeDeclarations."
FIRST_MODE_NOTE = (
    "This represents the first ModeDeclaration of the ModeDeclarationMapping. This reference has the multiplicity "
    "1 .. * to support use cases where e.g. one mode of the mode user is mapped to several modes of the mode manager."
)
SECOND_MODE_NOTE = "This represents the second ModeDeclaration of the ModeDeclarationMapping."


def _ref(value):
    ref = RefType()
    ref.setDest("MODE-DECLARATION")
    ref.setValue(value)
    return ref


class TestModeDeclarationMapping:
    def test_initialization(self):
        document = AUTOSAR.getInstance()
        ar_root = document.createARPackage("Pkg")
        mapping = ModeDeclarationMapping(ar_root, "MDM")

        assert mapping.getShortName() == "MDM"
        assert mapping.getFirstModeRefs() == []
        assert mapping.getSecondModeRef() is None

    def test_heritage(self):
        from armodel.models.M2.AUTOSARTemplates.GenericStructure.AbstractStructure import AtpStructureElement
        from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable import Identifiable

        document = AUTOSAR.getInstance()
        ar_root = document.createARPackage("Pkg")
        mapping = ModeDeclarationMapping(ar_root, "MDM")

        assert type(mapping).__bases__ == (AtpStructureElement,)
        for ancestor in (AtpStructureElement, Identifiable):
            assert isinstance(mapping, ancestor)

    def test_class_docstring_verbatim(self):
        assert ModeDeclarationMapping.__doc__.strip() == SPEC_NOTE

    def test_add_first_mode_ref(self):
        document = AUTOSAR.getInstance()
        ar_root = document.createARPackage("Pkg")
        mapping = ModeDeclarationMapping(ar_root, "MDM")
        ref1 = _ref("/Pkg/Mode1")
        ref2 = _ref("/Pkg/Mode2")

        result = mapping.addFirstModeRef(ref1)
        assert result is mapping
        mapping.addFirstModeRef(ref2)
        assert mapping.getFirstModeRefs() == [ref1, ref2]
        mapping.addFirstModeRef(None)
        assert mapping.getFirstModeRefs() == [ref1, ref2]

    def test_get_set_second_mode_ref(self):
        document = AUTOSAR.getInstance()
        ar_root = document.createARPackage("Pkg")
        mapping = ModeDeclarationMapping(ar_root, "MDM")
        ref = _ref("/Pkg/ModeMgr")

        result = mapping.setSecondModeRef(ref)
        assert result is mapping
        assert mapping.getSecondModeRef() is ref
        mapping.setSecondModeRef(None)
        assert mapping.getSecondModeRef() is ref

    def test_docstrings_verbatim(self):
        document = AUTOSAR.getInstance()
        ar_root = document.createARPackage("Pkg")
        mapping = ModeDeclarationMapping(ar_root, "MDM")

        def norm(doc):
            return " ".join(doc.split())

        assert norm(mapping.getFirstModeRefs.__doc__) == FIRST_MODE_NOTE
        assert norm(mapping.addFirstModeRef.__doc__) == (
            FIRST_MODE_NOTE + " A None value is a no-op and does not append anything."
        )
        assert norm(mapping.getSecondModeRef.__doc__) == SECOND_MODE_NOTE
        assert norm(mapping.setSecondModeRef.__doc__) == (
            SECOND_MODE_NOTE + " A None value is a no-op and does not overwrite an existing secondModeRef."
        )

    def test_get_type_hints_pins(self):
        hints = typing.get_type_hints(ModeDeclarationMapping.getFirstModeRefs)
        assert hints.get("return") == typing.List[RefType]

        hints = typing.get_type_hints(ModeDeclarationMapping.addFirstModeRef)
        assert hints.get("value") == typing.Optional[RefType]
        assert hints.get("return") is ModeDeclarationMapping

        hints = typing.get_type_hints(ModeDeclarationMapping.getSecondModeRef)
        assert hints.get("return") == typing.Optional[RefType]
