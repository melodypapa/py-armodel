"""
Tests for the ComponentInCompositionInstanceRef class
(AUTOSAR_CP_TPS_SoftwareComponentTemplate, Table D.13, p.950).
"""

from armodel.models.M2.AUTOSARTemplates.GenericStructure.AbstractStructure import AtpInstanceRef
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import RefType
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.Composition.InstanceRefs import ComponentInCompositionInstanceRef


def _ref(value, dest="SW-COMPONENT-PROTOTYPE"):
    return RefType().setValue(value).setDest(dest)


class TestComponentInCompositionInstanceRef:
    """
    Test class for ComponentInCompositionInstanceRef functionality.
    """

    def test_docstring_is_spec_note_verbatim(self):
        note = "The ComponentInCompositionInstanceRef points to a concrete SwComponentPrototype within a CompositionSwComponentType."
        assert ComponentInCompositionInstanceRef.__doc__.strip() == note

    def test_init_has_no_docstring(self):
        assert ComponentInCompositionInstanceRef.__init__.__doc__ is None

    def test_heritage(self):
        iref = ComponentInCompositionInstanceRef()
        assert isinstance(iref, AtpInstanceRef)
        assert isinstance(iref, ARObject)

    def test_defaults_in_spec_displayed_order(self):
        iref = ComponentInCompositionInstanceRef()
        assert iref.getBaseRef() is None
        assert iref.getContextComponentRefs() == []
        assert iref.getTargetComponentRef() is None
        assert list(iref.__dict__.keys())[-3:] == ["baseRef", "contextComponentRefs", "targetComponentRef"]

    def test_base_ref_get_set_round_trip_and_none_noop(self):
        iref = ComponentInCompositionInstanceRef()
        ref = _ref("/Pkg/Comp")
        assert iref.setBaseRef(ref) is iref
        assert iref.getBaseRef() is ref
        assert iref.setBaseRef(None) is iref
        assert iref.getBaseRef() is ref

    def test_add_context_component_ref(self):
        iref = ComponentInCompositionInstanceRef()
        ref = _ref("/Pkg/Comp/SwcProto")
        assert iref.addContextComponentRef(ref) is iref
        refs = iref.getContextComponentRefs()
        assert len(refs) == 1
        assert refs[0] is ref

    def test_add_context_component_ref_none_noop(self):
        iref = ComponentInCompositionInstanceRef()
        assert iref.addContextComponentRef(None) is iref
        assert iref.getContextComponentRefs() == []

    def test_set_target_component_ref(self):
        iref = ComponentInCompositionInstanceRef()
        ref = _ref("/Pkg/Comp/SwcProto")
        assert iref.setTargetComponentRef(ref) is iref
        assert iref.getTargetComponentRef() is ref

    def test_set_target_component_ref_none_noop(self):
        iref = ComponentInCompositionInstanceRef()
        ref = _ref("/Pkg/Comp/SwcProto")
        iref.setTargetComponentRef(ref)
        assert iref.setTargetComponentRef(None) is iref
        assert iref.getTargetComponentRef() is ref

    def test_accessor_docstrings_verbatim(self):
        assert ComponentInCompositionInstanceRef.getBaseRef.__doc__.strip() == "Stereotypes: atpDerived Tags: xml.sequenceOffset=10"
        assert ComponentInCompositionInstanceRef.getContextComponentRefs.__doc__.strip() == "The context for the scope of this timing event. Tags: xml.sequenceOffset=20"
        assert ComponentInCompositionInstanceRef.getTargetComponentRef.__doc__.strip() == "Tags: xml.sequenceOffset=30"
