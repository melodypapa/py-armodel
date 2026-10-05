"""
Spec-contract tests for InstantiationRTEEventProps (SWC TPS Table 3.17, p.85).
"""

import inspect

import pytest

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import Identifier
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.Composition import (
    InstantiationRTEEventProps,
    InstantiationTimingEventProps,
)
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.Composition.InstanceRefs import InstanceEventInCompositionInstanceRef

INSTANTIATION_RTE_EVENT_PROPS_CLASS_NOTE = "This meta-class represents the ability to refine the properties of RTEEvents for particular instances of a software component."

INSTANTIATION_RTE_EVENT_PROPS_MEMBER_NOTES = {
    "refinedEvent": "This instance ref denotes the Timing Event for which the period shall be refined on an instance level. InstanceRef implemented by: InstanceEventInCompositionInstanceRef",
    "shortLabel": "The main purpose of the shortLabel is to contribute to the splitkey of aggregations that are <<atpSplitable>>.",
}


class TestInstantiationRTEEventProps:
    """Spec-contract tests for InstantiationRTEEventProps."""

    def _make(self):
        return InstantiationTimingEventProps()

    def test_abstract_guard(self):
        with pytest.raises(TypeError, match="InstantiationRTEEventProps is an abstract class"):
            InstantiationRTEEventProps()

    def test_class_docstring_note(self):
        assert inspect.cleandoc(InstantiationRTEEventProps.__doc__) == INSTANTIATION_RTE_EVENT_PROPS_CLASS_NOTE

    def test_init_docless(self):
        assert InstantiationRTEEventProps.__init__.__doc__ is None

    def test_initialization_defaults(self):
        props = self._make()
        assert props.getRefinedEventIRef() is None
        assert props.getShortLabel() is None

    def test_not_variation_point_capable(self):
        assert not hasattr(InstantiationRTEEventProps, "setVariationPoint")

    def test_member_order(self):
        props = self._make()
        members = [k for k in vars(props) if k in ("refinedEventIRef", "shortLabel")]
        assert members == ["refinedEventIRef", "shortLabel"]

    def test_get_set_refined_event_iref(self):
        props = self._make()
        iref = InstanceEventInCompositionInstanceRef()
        assert props.setRefinedEventIRef(iref) is props
        assert props.getRefinedEventIRef() is iref
        assert props.setRefinedEventIRef(None) is props
        assert props.getRefinedEventIRef() is iref

    def test_get_set_short_label(self):
        props = self._make()
        label = Identifier().setValue("label")
        assert props.setShortLabel(label) is props
        assert props.getShortLabel() is label
        assert props.setShortLabel(None) is props
        assert props.getShortLabel() is label

    def test_docstrings_verbatim(self):
        getter_notes = {
            InstantiationRTEEventProps.getRefinedEventIRef: INSTANTIATION_RTE_EVENT_PROPS_MEMBER_NOTES["refinedEvent"],
            InstantiationRTEEventProps.getShortLabel: INSTANTIATION_RTE_EVENT_PROPS_MEMBER_NOTES["shortLabel"],
        }
        for getter, note in getter_notes.items():
            assert getter.__doc__ is not None, getter.__name__
            assert getter.__doc__.strip().split("\n")[0] == note, getter.__name__
        setter_notes = {
            InstantiationRTEEventProps.setRefinedEventIRef: INSTANTIATION_RTE_EVENT_PROPS_MEMBER_NOTES["refinedEvent"],
            InstantiationRTEEventProps.setShortLabel: INSTANTIATION_RTE_EVENT_PROPS_MEMBER_NOTES["shortLabel"],
        }
        for setter, note in setter_notes.items():
            assert setter.__doc__ is not None, setter.__name__
            assert setter.__doc__.strip().split("\n")[0] == note, setter.__name__

    def test_setter_none_noop_sentences(self):
        assert "A None value is a no-op and does not overwrite an existing reference." in InstantiationRTEEventProps.setRefinedEventIRef.__doc__
        assert "A None value is a no-op and does not overwrite an existing short label." in InstantiationRTEEventProps.setShortLabel.__doc__

    def test_type_hints(self):
        import typing

        hints = typing.get_type_hints(InstantiationRTEEventProps.setRefinedEventIRef)
        assert hints["value"] == typing.Optional[InstanceEventInCompositionInstanceRef]
        assert hints["return"] is InstantiationRTEEventProps
        hints = typing.get_type_hints(InstantiationRTEEventProps.getRefinedEventIRef)
        assert hints["return"] == typing.Optional[InstanceEventInCompositionInstanceRef]
        hints = typing.get_type_hints(InstantiationRTEEventProps.setShortLabel)
        assert hints["value"] == typing.Optional[Identifier]
        assert hints["return"] is InstantiationRTEEventProps
        hints = typing.get_type_hints(InstantiationRTEEventProps.getShortLabel)
        assert hints["return"] == typing.Optional[Identifier]
