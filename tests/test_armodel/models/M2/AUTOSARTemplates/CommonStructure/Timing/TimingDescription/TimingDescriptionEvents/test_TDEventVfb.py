import pytest

from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.CommonStructure.Timing.TimingDescription import TimingDescriptionEvent
from armodel.models.M2.AUTOSARTemplates.CommonStructure.Timing.TimingDescription.TimingDescriptionEvents.TDEventVfb import (
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

    def test_vfb_direct_use_instantiable(self):
        event = TDEventVfb(self._parent(), "Event1")
        assert isinstance(event, TDEventVfb)
        assert event.getShortName() == "Event1"

    def test_vfb_port_abstract(self):
        with pytest.raises(TypeError, match="TDEventVfbPort is an abstract class"):
            TDEventVfbPort(self._parent(), "Event1")

    def test_direct_use_defaults(self):
        event = TDEventVfb(self._parent(), "Event1")
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


class TestTDEventVfbDirectUseSpecContract:
    """Direct-use spec contract for TDEventVfb: the meta-model permits the
    abstract TDEventVfb DIRECTLY as a choice member (TD-EVENT-VFB in the
    TD-EVENT-VFB--SUBTYPES-ENUM, AUTOSAR_00052.xsd line 122350, enum value
    "TD-EVENT-VFB" at line 122356; byte-identical enum in AUTOSAR_00044.xsd
    L85995-86005). Per the user decision of 2026-09-27 the direct-use form is
    carried by TDEventVfb itself (the former fabricated ConcreteTDEventVfb
    subclass was retired — no spec table and no XSD complexType/element
    declaration ever named it), so TDEventVfb is instantiable despite its
    spec-declared (abstract) marker; NOTE: no <TD-EVENT-VFB> element
    declaration exists in either XSD, so serializing a direct-use instance is
    a defensive/legacy-only path. Own body = the Table 3.14 attribute
    component (COMPONENT-IREF) only."""

    def _parent(self):
        document = AUTOSAR.getInstance()
        document.clear()
        document.setARRelease("R23-11")
        return document.createARPackage("AUTOSAR")

    def test_class_docstring_is_spec_note(self):
        """
        Test that the class docstring stays the Table 3.14 Note verbatim
        (R23-11 CP_TPS_TimingExtensions p.51) — the direct-use disposition is
        documented in the checklist comment, never by mutating the spec Note.
        """
        assert TDEventVfb.__doc__.strip() == ("This is the abstract parent class to describe timing events at Virtual Functional Bus (VFB) level.")

    def test_direct_use_instantiable(self):
        """
        Test that the direct-use form is carried by TDEventVfb itself: the
        former TypeError abstract guard is gone and instantiation yields a
        working instance (user decision 2026-09-27, ConcreteTDEventVfb
        retired).
        """
        event = TDEventVfb(self._parent(), "Event1")
        assert isinstance(event, TDEventVfb)
        assert event.getShortName() == "Event1"

    def test_bases_drop_abc(self):
        """
        Test that the ABC mixin was removed from the bases (instantiability is
        the direct-use contract) while TimingDescriptionEvent stays.
        """
        assert TDEventVfb.__bases__ == (TimingDescriptionEvent,)

    def test_no_fabricated_subclass(self):
        """
        Test that the fabricated ConcreteTDEventVfb class is gone from the
        module (the direct-use form must not resurrect under an invented
        name).
        """
        import armodel.models.M2.AUTOSARTemplates.CommonStructure.Timing.TimingDescription.TimingDescriptionEvents.TDEventVfb as module

        assert not hasattr(module, "ConcreteTDEventVfb")

    def test_inherited_component_iref_round_trip_and_none_noop(self):
        """
        Test that the componentIRef contract (Table 3.14 attribute, XSD
        COMPONENT-IREF of type COMPONENT-IN-COMPOSITION-INSTANCE-REF)
        round-trips on a direct-use instance with the None no-op.
        """
        event = TDEventVfb(self._parent(), "Event1")
        assert event.getComponentIRef() is None
        iref = ComponentInCompositionInstanceRef()
        iref.setTargetComponentRef(RefType().setValue("/Pkg/Comp/SwcProto").setDest("SW-COMPONENT-PROTOTYPE"))
        assert event.setComponentIRef(iref) is event
        assert event.getComponentIRef() is iref
        assert event.setComponentIRef(None) is event
        assert event.getComponentIRef() is iref
