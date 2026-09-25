import inspect
import re

import pytest

from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.CommonStructure.Timing.TimingDescription.TimingDescriptionEvents.TDEventVfb import (
    ConcreteTDEventVfb,
    TDEventModeDeclaration,
    TDEventOperation,
    TDEventTrigger,
    TDEventVariableDataPrototype,
    TDEventVfb,
    TDEventVfbPort,
    TDEventVfbReference,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import RefType
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.Composition.InstanceRefs import ComponentInCompositionInstanceRef


class TestTDEventVfbFamily:
    def _parent(self):
        document = AUTOSAR.getInstance()
        document.clear()
        document.setARRelease("R23-11")
        return document.createARPackage("AUTOSAR")

    def test_vfb_abstract(self):
        with pytest.raises(TypeError, match="TDEventVfb is an abstract class"):
            TDEventVfb(self._parent(), "Event1")

    def test_vfb_port_abstract(self):
        with pytest.raises(TypeError, match="TDEventVfbPort is an abstract class"):
            TDEventVfbPort(self._parent(), "Event1")

    def test_concrete_subclass_of_base_chain(self):
        event = ConcreteTDEventVfb(self._parent(), "Event1")
        assert isinstance(event, TDEventVfb)
        assert event.getShortName() == "Event1"
        assert event.getComponentIRef() is None

    def test_vfb_reference(self):
        parent = self._parent()
        event = TDEventVfbReference(parent, "Event1")
        assert isinstance(event, TDEventVfb)
        assert event.getReferencedTDEventVfbRef() is None

    def test_mode_declaration_defaults(self):
        parent = self._parent()
        event = TDEventModeDeclaration(parent, "Event1")
        assert isinstance(event, TDEventVfbPort)
        assert event.getIsExternal() is None
        assert event.getPortRef() is None
        assert event.getPortPrototypeBlueprintRef() is None
        assert event.getEntryModeDeclarationRef() is None
        assert event.getExitModeDeclarationRef() is None
        assert event.getModeDeclarationRef() is None

    def test_operation_members(self):
        parent = self._parent()
        event = TDEventOperation(parent, "Event1")
        assert event.getOperationRef() is None
        assert event.getTdEventOperationType() is None

    def test_trigger_members(self):
        parent = self._parent()
        event = TDEventTrigger(parent, "Event1")
        assert event.getTriggerRef() is None
        assert event.getTdEventTriggerType() is None

    def test_variable_data_prototype_members(self):
        parent = self._parent()
        event = TDEventVariableDataPrototype(parent, "Event1")
        assert event.getDataElementRef() is None
        assert event.getTdEventVariableDataPrototypeType() is None


class TestConcreteTDEventVfbSpecContract:
    """XSD-only spec contract for ConcreteTDEventVfb: the class has NO own
    table in either corpus (R23-11 / R4.3.1 markdown caption + tolerant greps
    0 hits) and no own XSD complexType — its grounding is the R23-11 XSD's
    TD-EVENT-VFB--SUBTYPES-ENUM (AUTOSAR_00052.xsd line 122350, enum value
    "TD-EVENT-VFB" at line 122356; byte-identical enum in AUTOSAR_00044.xsd
    L85995-86005), which permits the abstract TDEventVfb directly as a choice
    member. Body = abstract group TD-EVENT-VFB (AUTOSAR_00052.xsd line 122335,
    COMPONENT-IREF) owned by the base class, so the concrete subclass declares
    no attributes of its own."""

    def _parent(self):
        document = AUTOSAR.getInstance()
        document.clear()
        document.setARRelease("R23-11")
        return document.createARPackage("AUTOSAR")

    def test_class_docstring_is_xsd_derivation_note(self):
        """
        Test that the class docstring documents the XSD-only derivation
        honestly (no spec Note exists anywhere for this class — no table in
        either corpus, and the XSD group documentation "This is the abstract
        parent class..." belongs to the base TDEventVfb).
        """
        assert ConcreteTDEventVfb.__doc__.strip() == (
            "Concrete direct-use instantiation of the abstract TDEventVfb "
            "(XSD-only: no own table in the repo corpus; the meta-model permits the abstract TDEventVfb directly "
            "— TD-EVENT-VFB in the TD-EVENT-VFB--SUBTYPES-ENUM, AUTOSAR_00052.xsd — and the class carries no attributes of its own)."
        )

    def test_init_defined_on_class(self):
        """
        Test that the class defines its own __init__ (family form: every
        sibling concrete event class declares an explicit __init__ chaining to
        the base — the intake orphan inherited the base's __init__ instead).
        """
        assert "__init__" in ConcreteTDEventVfb.__dict__

    def test_init_has_no_docstring(self):
        """
        Test that __init__ has no docstring (spec Notes live in inline member
        comments; this class has no own members at all).
        """
        assert ConcreteTDEventVfb.__init__.__doc__ is None

    def test_no_own_fields_declared(self):
        """
        Test the field-to-spec cross-check in the no-attributes direction:
        the SUBTYPES-ENUM instantiation adds nothing to the abstract base body
        (group TD-EVENT-VFB, COMPONENT-IREF only, owned by the base), so
        ConcreteTDEventVfb.__init__ declares zero own fields.
        """
        init_source = inspect.getsource(ConcreteTDEventVfb.__init__)
        assert re.findall(r"self\.(\w+)\s*:", init_source) == []

    def test_bases_is_tdevent_vfb(self):
        """
        Test that the most-derived base is exactly the abstract TDEventVfb
        (R23-11 Table 3.14, p.51 — stamped) and the class is no
        TDEventVfbPort.
        """
        assert ConcreteTDEventVfb.__bases__ == (TDEventVfb,)
        assert not issubclass(ConcreteTDEventVfb, TDEventVfbPort)

    def test_instantiable_not_abstract(self):
        """
        Test that the class is the concrete direct-use form: instantiation
        must not raise (unlike the abstract bases), yields a TDEventVfb.
        """
        event = ConcreteTDEventVfb(self._parent(), "Event1")
        assert isinstance(event, TDEventVfb)
        assert event.getShortName() == "Event1"

    def test_no_own_accessors(self):
        """
        Test that the class defines no get/set accessors of its own and the
        inherited COMPONENT-IREF accessor pair is the base's implementation
        (coverage rows live on the stamped base checklist).
        """
        class_source = inspect.getsource(ConcreteTDEventVfb)
        assert re.findall(r"def (get\w+|set\w+)\(", class_source) == []
        assert ConcreteTDEventVfb.getComponentIRef is TDEventVfb.getComponentIRef
        assert ConcreteTDEventVfb.setComponentIRef is TDEventVfb.setComponentIRef

    def test_inherited_component_iref_round_trip_and_none_noop(self):
        """
        Test that the inherited componentIRef contract (Table 3.14 attribute,
        XSD COMPONENT-IREF of type COMPONENT-IN-COMPOSITION-INSTANCE-REF)
        round-trips through the concrete subclass with the None no-op.
        """
        event = ConcreteTDEventVfb(self._parent(), "Event1")
        assert event.getComponentIRef() is None
        iref = ComponentInCompositionInstanceRef()
        iref.setTargetComponentRef(RefType().setValue("/Pkg/Comp/SwcProto").setDest("SW-COMPONENT-PROTOTYPE"))
        assert event.setComponentIRef(iref) is event
        assert event.getComponentIRef() is iref
        assert event.setComponentIRef(None) is event
        assert event.getComponentIRef() is iref
