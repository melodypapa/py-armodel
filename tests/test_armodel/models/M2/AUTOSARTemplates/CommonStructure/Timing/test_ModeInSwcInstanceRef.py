"""
This module contains tests for the ModeInSwcInstanceRef class in the
AUTOSAR CommonStructure.Timing.TimingCondition module.
"""

import inspect
import re
import typing

from armodel.models.M2.AUTOSARTemplates.CommonStructure.Timing.TimingCondition import ModeInSwcBswInstanceRef, ModeInSwcInstanceRef
from armodel.models.M2.AUTOSARTemplates.GenericStructure.AbstractStructure import AtpInstanceRef
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import RefType


class TestModeInSwcInstanceRef:
    """
    Test class for ModeInSwcInstanceRef functionality.
    """

    def test_initialization(self):
        obj = ModeInSwcInstanceRef()
        assert isinstance(obj, ModeInSwcInstanceRef)
        assert obj.getBaseRef() is None
        assert obj.getContextComponentRefs() == []
        assert obj.getContextModeDeclarationGroupPrototypeRef() is None
        assert obj.getContextPortRef() is None
        assert obj.getTargetModeDeclarationRef() is None

    def test_get_set_base_ref(self):
        obj = ModeInSwcInstanceRef()
        ref = RefType().setValue("/Pkg/SwcType").setDest("SW-COMPONENT-TYPE")
        assert obj.setBaseRef(ref) is obj
        assert obj.getBaseRef() is ref
        assert obj.getBaseRef().getValue() == "/Pkg/SwcType"

    def test_set_base_ref_none_noop(self):
        obj = ModeInSwcInstanceRef()
        ref = RefType().setValue("/Pkg/SwcType").setDest("SW-COMPONENT-TYPE")
        obj.setBaseRef(ref)
        assert obj.setBaseRef(None) is obj
        assert obj.getBaseRef() is ref

    def test_add_context_component_ref(self):
        obj = ModeInSwcInstanceRef()
        ref1 = RefType().setValue("/Pkg/SwcProto1").setDest("SW-COMPONENT-PROTOTYPE")
        ref2 = RefType().setValue("/Pkg/SwcProto2").setDest("SW-COMPONENT-PROTOTYPE")
        assert obj.addContextComponentRef(ref1) is obj
        obj.addContextComponentRef(ref2)
        refs = obj.getContextComponentRefs()
        assert len(refs) == 2
        assert refs[0] is ref1
        assert refs[1] is ref2

    def test_add_context_component_ref_none_noop(self):
        obj = ModeInSwcInstanceRef()
        ref1 = RefType().setValue("/Pkg/SwcProto1").setDest("SW-COMPONENT-PROTOTYPE")
        obj.addContextComponentRef(ref1)
        assert obj.addContextComponentRef(None) is obj
        assert len(obj.getContextComponentRefs()) == 1

    def test_get_set_context_mode_declaration_group_prototype_ref(self):
        obj = ModeInSwcInstanceRef()
        ref = RefType().setValue("/Pkg/Mdgp").setDest("MODE-DECLARATION-GROUP-PROTOTYPE")
        assert obj.setContextModeDeclarationGroupPrototypeRef(ref) is obj
        assert obj.getContextModeDeclarationGroupPrototypeRef() is ref
        assert obj.getContextModeDeclarationGroupPrototypeRef().getValue() == "/Pkg/Mdgp"

    def test_set_context_mode_declaration_group_prototype_ref_none_noop(self):
        obj = ModeInSwcInstanceRef()
        ref = RefType().setValue("/Pkg/Mdgp").setDest("MODE-DECLARATION-GROUP-PROTOTYPE")
        obj.setContextModeDeclarationGroupPrototypeRef(ref)
        assert obj.setContextModeDeclarationGroupPrototypeRef(None) is obj
        assert obj.getContextModeDeclarationGroupPrototypeRef() is ref

    def test_get_set_context_port_ref(self):
        obj = ModeInSwcInstanceRef()
        ref = RefType().setValue("/Pkg/Port").setDest("PORT-PROTOTYPE")
        assert obj.setContextPortRef(ref) is obj
        assert obj.getContextPortRef() is ref
        assert obj.getContextPortRef().getValue() == "/Pkg/Port"

    def test_set_context_port_ref_none_noop(self):
        obj = ModeInSwcInstanceRef()
        ref = RefType().setValue("/Pkg/Port").setDest("PORT-PROTOTYPE")
        obj.setContextPortRef(ref)
        assert obj.setContextPortRef(None) is obj
        assert obj.getContextPortRef() is ref

    def test_get_set_target_mode_declaration_ref(self):
        obj = ModeInSwcInstanceRef()
        ref = RefType().setValue("/Pkg/Mode").setDest("MODE-DECLARATION")
        assert obj.setTargetModeDeclarationRef(ref) is obj
        assert obj.getTargetModeDeclarationRef() is ref
        assert obj.getTargetModeDeclarationRef().getValue() == "/Pkg/Mode"

    def test_set_target_mode_declaration_ref_none_noop(self):
        obj = ModeInSwcInstanceRef()
        ref = RefType().setValue("/Pkg/Mode").setDest("MODE-DECLARATION")
        obj.setTargetModeDeclarationRef(ref)
        assert obj.setTargetModeDeclarationRef(None) is obj
        assert obj.getTargetModeDeclarationRef() is ref


class TestModeInSwcInstanceRefSpecContract:
    """
    Spec-contract pins for ModeInSwcInstanceRef (R23-11 CP_TPS_TimingExtensions Table 3.12).

    The in-cell "Stereotypes:"/"Tags: xml.sequenceOffset=N" suffixes are metadata, not
    Note prose, and are kept out of the docstrings per the batch convention
    (VariationPoint Table 7.4 precedent); the [constr_6855/6856/6857/6899] paragraphs
    are section-level constraints, not Note rows (SynchronizationTimingConstraint
    Table 3.54 precedent).
    """

    def test_class_docstring_verbatim(self):
        """
        Test that the class docstring is the Table 3.12 Note verbatim.
        """
        assert ModeInSwcInstanceRef.__doc__.strip() == ("Instance reference to be capable of referencing a ModeDeclaration at a specific Mode Switch Port of a SW-C.")

    def test_init_has_no_docstring(self):
        """
        Test that __init__ has no docstring (spec Notes live in inline member comments).
        """
        assert ModeInSwcInstanceRef.__init__.__doc__ is None

    def test_exact_own_field_set(self):
        """
        Test that __init__ declares exactly the five Table 3.12 attributes in displayed row order.
        """
        source = inspect.getsource(ModeInSwcInstanceRef.__init__)
        assert re.findall(r"self\.(\w+)\s*:", source) == [
            "baseRef",
            "contextComponentRefs",
            "contextModeDeclarationGroupPrototypeRef",
            "contextPortRef",
            "targetModeDeclarationRef",
        ]

    def test_pep526_annotated_members(self):
        """
        Test that every member is a PEP 526 annotated assignment with the spec type and no trailing '# type:' comment.
        """
        source = inspect.getsource(ModeInSwcInstanceRef.__init__)
        assert re.search(r"self\.baseRef:\s*Optional\[RefType\]\s*=\s*None", source)
        assert re.search(r"self\.contextComponentRefs:\s*List\[RefType\]\s*=\s*\[\]", source)
        assert re.search(r"self\.contextModeDeclarationGroupPrototypeRef:\s*Optional\[RefType\]\s*=\s*None", source)
        assert re.search(r"self\.contextPortRef:\s*Optional\[RefType\]\s*=\s*None", source)
        assert re.search(r"self\.targetModeDeclarationRef:\s*Optional\[RefType\]\s*=\s*None", source)
        assert "# type:" not in source

    def test_most_derived_bases(self):
        """
        Test that the Base per Table 3.12 is AtpInstanceRef + ModeInSwcBswInstanceRef (ARObject transitive via both).
        """
        assert ModeInSwcInstanceRef.__bases__ == (AtpInstanceRef, ModeInSwcBswInstanceRef)
        assert issubclass(ModeInSwcInstanceRef, ARObject)

    def test_accessor_order(self):
        """
        Test that accessors follow the displayed row order with get/set pairs (get/add pair for the * aggr).
        """
        source = inspect.getsource(ModeInSwcInstanceRef)
        assert re.findall(r"def (\w+)\(", source) == [
            "__init__",
            "getBaseRef",
            "setBaseRef",
            "getContextComponentRefs",
            "addContextComponentRef",
            "getContextModeDeclarationGroupPrototypeRef",
            "setContextModeDeclarationGroupPrototypeRef",
            "getContextPortRef",
            "setContextPortRef",
            "getTargetModeDeclarationRef",
            "setTargetModeDeclarationRef",
        ]

    def test_base_ref_typed_optional_reftype(self):
        """
        Test that base (SwComponentType, 0..1, ref) is typed Optional[RefType].
        """
        getter_hints = typing.get_type_hints(ModeInSwcInstanceRef.getBaseRef)
        assert getter_hints.get("return") == typing.Optional[RefType]

        setter_hints = typing.get_type_hints(ModeInSwcInstanceRef.setBaseRef)
        assert setter_hints.get("value") == typing.Optional[RefType]
        assert setter_hints.get("return") is ModeInSwcInstanceRef

    def test_context_component_refs_typed_list_reftype(self):
        """
        Test that contextComponent (SwComponentPrototype, *, ref) maps to a List[RefType] accessor pair.
        """
        getter_hints = typing.get_type_hints(ModeInSwcInstanceRef.getContextComponentRefs)
        assert getter_hints.get("return") == typing.List[RefType]

        setter_hints = typing.get_type_hints(ModeInSwcInstanceRef.addContextComponentRef)
        assert setter_hints.get("value") == typing.Optional[RefType]
        assert setter_hints.get("return") is ModeInSwcInstanceRef

    def test_context_mode_declaration_group_prototype_ref_typed(self):
        """
        Test that contextModeDeclarationGroupPrototype (ModeDeclarationGroupPrototype, 0..1, ref) is typed Optional[RefType].
        """
        getter_hints = typing.get_type_hints(ModeInSwcInstanceRef.getContextModeDeclarationGroupPrototypeRef)
        assert getter_hints.get("return") == typing.Optional[RefType]

        setter_hints = typing.get_type_hints(ModeInSwcInstanceRef.setContextModeDeclarationGroupPrototypeRef)
        assert setter_hints.get("value") == typing.Optional[RefType]
        assert setter_hints.get("return") is ModeInSwcInstanceRef

    def test_context_port_ref_typed(self):
        """
        Test that contextPort (PortPrototype, 0..1, ref) is typed Optional[RefType].
        """
        getter_hints = typing.get_type_hints(ModeInSwcInstanceRef.getContextPortRef)
        assert getter_hints.get("return") == typing.Optional[RefType]

        setter_hints = typing.get_type_hints(ModeInSwcInstanceRef.setContextPortRef)
        assert setter_hints.get("value") == typing.Optional[RefType]
        assert setter_hints.get("return") is ModeInSwcInstanceRef

    def test_target_mode_declaration_ref_typed(self):
        """
        Test that targetModeDeclaration (ModeDeclaration, 0..1, ref) is typed Optional[RefType].
        """
        getter_hints = typing.get_type_hints(ModeInSwcInstanceRef.getTargetModeDeclarationRef)
        assert getter_hints.get("return") == typing.Optional[RefType]

        setter_hints = typing.get_type_hints(ModeInSwcInstanceRef.setTargetModeDeclarationRef)
        assert setter_hints.get("value") == typing.Optional[RefType]
        assert setter_hints.get("return") is ModeInSwcInstanceRef

    def test_getter_docstrings_are_notes_verbatim(self):
        """
        Test that getter docstrings are the Table 3.12 Notes verbatim (no Stereotypes/Tags/constr suffixes).
        """
        assert ModeInSwcInstanceRef.getBaseRef.__doc__.strip() == "Specifies the SW component representing the base of the context."
        assert ModeInSwcInstanceRef.getContextComponentRefs.__doc__.strip() == "Specifies the SW component prototype representing the context."
        assert ModeInSwcInstanceRef.getContextModeDeclarationGroupPrototypeRef.__doc__.strip() == "Specifies the mode declaration group prototype that manifests the context."
        assert ModeInSwcInstanceRef.getContextPortRef.__doc__.strip() == "Specifies the port prototype representing the context."
        assert ModeInSwcInstanceRef.getTargetModeDeclarationRef.__doc__.strip() == "Specifies the specific mode declaration in the given context."

    def test_setter_docstrings_are_notes_with_none_noop(self):
        """
        Test that setter/add docstrings are the Table 3.12 Notes verbatim plus the None-no-op sentence.
        """
        assert ModeInSwcInstanceRef.setBaseRef.__doc__.strip() == (
            "Specifies the SW component representing the base of the context. A None value is a no-op and does not overwrite an existing baseRef."
        )
        assert ModeInSwcInstanceRef.addContextComponentRef.__doc__.strip() == ("Specifies the SW component prototype representing the context. A None value is a no-op and does not append anything.")
        assert ModeInSwcInstanceRef.setContextModeDeclarationGroupPrototypeRef.__doc__.strip() == (
            "Specifies the mode declaration group prototype that manifests the context. A None value is a no-op and does not overwrite an existing contextModeDeclarationGroupPrototypeRef."
        )
        assert ModeInSwcInstanceRef.setContextPortRef.__doc__.strip() == (
            "Specifies the port prototype representing the context. A None value is a no-op and does not overwrite an existing contextPortRef."
        )
        assert ModeInSwcInstanceRef.setTargetModeDeclarationRef.__doc__.strip() == (
            "Specifies the specific mode declaration in the given context. A None value is a no-op and does not overwrite an existing targetModeDeclarationRef."
        )

    def test_inline_init_comments_are_notes_verbatim(self):
        """
        Test that the inline __init__ member comments are the Table 3.12 Notes verbatim in displayed row order.
        """
        source = inspect.getsource(ModeInSwcInstanceRef.__init__)
        comments = re.findall(r"^\s*# (.+)$", source, re.MULTILINE)
        assert comments == [
            "Specifies the SW component representing the base of the context.",
            "Specifies the SW component prototype representing the context.",
            "Specifies the mode declaration group prototype that manifests the context.",
            "Specifies the port prototype representing the context.",
            "Specifies the specific mode declaration in the given context.",
        ]
