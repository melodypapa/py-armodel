"""
Spec-contract tests for InstantiationTimingEventProps (SWC TPS Table 3.16, p.85).
"""

import inspect

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import TimeValue
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.Composition import (
    InstantiationRTEEventProps,
    InstantiationTimingEventProps,
)

INSTANTIATION_TIMING_EVENT_PROPS_CLASS_NOTE = (
    "This meta-class represents the ability to refine a timing event for particular instances of a software component. This approach supports an instance specific timing."
)

INSTANTIATION_TIMING_EVENT_PROPS_MEMBER_NOTES = {
    "period": "This attribute represents the value of the refined activation period.",
}


class TestInstantiationTimingEventProps:
    """Spec-contract tests for InstantiationTimingEventProps."""

    def test_is_instantiable_subclass_of_base(self):
        props = InstantiationTimingEventProps()
        assert isinstance(props, InstantiationRTEEventProps)

    def test_class_docstring_note(self):
        assert inspect.cleandoc(InstantiationTimingEventProps.__doc__) == INSTANTIATION_TIMING_EVENT_PROPS_CLASS_NOTE

    def test_init_docless(self):
        assert InstantiationTimingEventProps.__init__.__doc__ is None

    def test_initialization_defaults(self):
        props = InstantiationTimingEventProps()
        assert props.getPeriod() is None
        assert props.getRefinedEventIRef() is None
        assert props.getShortLabel() is None

    def test_member_order(self):
        props = InstantiationTimingEventProps()
        members = [k for k in vars(props) if k in ("refinedEventIRef", "shortLabel", "period")]
        assert members == ["refinedEventIRef", "shortLabel", "period"]

    def test_get_set_period(self):
        props = InstantiationTimingEventProps()
        period = TimeValue().setValue("0.02")
        assert props.setPeriod(period) is props
        assert props.getPeriod() is period
        assert props.setPeriod(None) is props
        assert props.getPeriod() is period

    def test_docstrings_verbatim(self):
        note = INSTANTIATION_TIMING_EVENT_PROPS_MEMBER_NOTES["period"]
        for method in (InstantiationTimingEventProps.getPeriod, InstantiationTimingEventProps.setPeriod):
            assert method.__doc__ is not None, method.__name__
            assert method.__doc__.strip().split("\n")[0] == note, method.__name__
        assert "A None value is a no-op and does not overwrite an existing period." in InstantiationTimingEventProps.setPeriod.__doc__

    def test_type_hints(self):
        import typing

        hints = typing.get_type_hints(InstantiationTimingEventProps.setPeriod)
        assert hints["value"] == typing.Optional[TimeValue]
        assert hints["return"] is InstantiationTimingEventProps
        hints = typing.get_type_hints(InstantiationTimingEventProps.getPeriod)
        assert hints["return"] == typing.Optional[TimeValue]
