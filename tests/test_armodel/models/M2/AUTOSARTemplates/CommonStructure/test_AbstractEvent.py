import inspect
import typing

import pytest

from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.CommonStructure.InternalBehavior import AbstractEvent
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable import Identifiable
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import RefType
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.SwcInternalBehavior.RTEEvents import InitEvent


class TestAbstractEvent:
    def test_abstract_class_cannot_be_instantiated(self):
        document = AUTOSAR.getInstance()
        ar_root = document.createARPackage("AUTOSAR")
        with pytest.raises(TypeError, match="AbstractEvent is an abstract class"):
            AbstractEvent(ar_root, "event")

    def test_initialization_defaults_via_concrete_subclass(self):
        document = AUTOSAR.getInstance()
        ar_root = document.createARPackage("AUTOSAR")
        event = InitEvent(ar_root, "InitEvt")
        assert isinstance(event, AbstractEvent)
        assert isinstance(event, Identifiable)
        assert event.short_name == "InitEvt"
        assert event.activationReasonRepresentationRef is None
        assert event.getActivationReasonRepresentationRef() is None

    def test_class_docstring_is_spec_note_verbatim(self):
        assert inspect.getdoc(AbstractEvent) == "This meta-class represents the abstract ability to model an event that can be taken to implement application software or basic software in AUTOSAR."

    def test_get_set_activation_reason_representation_ref(self):
        document = AUTOSAR.getInstance()
        ar_root = document.createARPackage("AUTOSAR")
        event = InitEvent(ar_root, "InitEvt")
        ref = RefType()
        ref.setDest("EXECUTABLE-ENTITY-ACTIVATION-REASON")
        ref.setValue("/Pkg/Swc_IB/Cyclic/ReasonA")
        assert event.setActivationReasonRepresentationRef(ref) is event
        assert event.getActivationReasonRepresentationRef() is ref
        assert event.getActivationReasonRepresentationRef().getDest() == "EXECUTABLE-ENTITY-ACTIVATION-REASON"
        assert event.getActivationReasonRepresentationRef().getValue() == "/Pkg/Swc_IB/Cyclic/ReasonA"

    def test_set_activation_reason_representation_ref_none_noop(self):
        document = AUTOSAR.getInstance()
        ar_root = document.createARPackage("AUTOSAR")
        event = InitEvent(ar_root, "InitEvt")
        ref = RefType().setValue("/Pkg/Swc_IB/Cyclic/ReasonA")
        event.setActivationReasonRepresentationRef(ref)
        event.setActivationReasonRepresentationRef(None)
        assert event.getActivationReasonRepresentationRef() is ref

    def test_accessor_type_hints(self):
        event = InitEvent.__new__(InitEvent)
        assert typing.get_type_hints(event.getActivationReasonRepresentationRef).get("return") == typing.Optional[RefType]
        assert typing.get_type_hints(event.setActivationReasonRepresentationRef).get("value") == typing.Optional[RefType]
        assert typing.get_type_hints(event.setActivationReasonRepresentationRef).get("return") is AbstractEvent
