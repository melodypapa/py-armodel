"""
This module contains tests for the SynchronizationPointConstraint class in the
AUTOSAR CommonStructure.Timing.TimingConstraint module.
"""

from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.CommonStructure.Timing.TimingConstraint.SynchronizationPointConstraint import (
    SynchronizationPointConstraint,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    RefType,
)


class TestSynchronizationPointConstraint:
    """
    Test class for SynchronizationPointConstraint functionality.
    """

    def _parent(self):
        document = AUTOSAR.getInstance()
        document.clear()
        document.setARRelease("R23-11")
        return document.createARPackage("AUTOSAR")

    def _ref(self, value: str, dest: str) -> RefType:
        return RefType().setValue(value).setDest(dest)

    def test_initialization(self):
        constraint = SynchronizationPointConstraint(self._parent(), "Sync1")
        assert isinstance(constraint, SynchronizationPointConstraint)
        assert constraint.getShortName() == "Sync1"
        assert constraint.getTimingConditionRef() is None
        assert constraint.getSourceEecRefs() == []
        assert constraint.getSourceEventRefs() == []
        assert constraint.getTargetEecRefs() == []
        assert constraint.getTargetEventRefs() == []

    def test_add_source_eec_ref(self):
        constraint = SynchronizationPointConstraint(self._parent(), "Sync1")
        ref1 = self._ref("/AUTOSAR/Group1", "EOC-EXECUTABLE-ENTITY-REF-GROUP")
        ref2 = self._ref("/AUTOSAR/Group2", "EOC-EXECUTABLE-ENTITY-REF-GROUP")
        assert constraint.addSourceEecRef(ref1) is constraint
        assert constraint.addSourceEecRef(ref2) is constraint
        refs = constraint.getSourceEecRefs()
        assert len(refs) == 2
        assert refs[0] is ref1
        assert refs[1] is ref2

    def test_add_source_eec_ref_none_is_no_op(self):
        constraint = SynchronizationPointConstraint(self._parent(), "Sync1")
        assert constraint.addSourceEecRef(None) is constraint
        assert constraint.getSourceEecRefs() == []

    def test_add_source_event_ref(self):
        constraint = SynchronizationPointConstraint(self._parent(), "Sync1")
        ref1 = self._ref("/AUTOSAR/Evt1", "TIMING-DESCRIPTION-EVENT")
        ref2 = self._ref("/AUTOSAR/Evt2", "TIMING-DESCRIPTION-EVENT")
        assert constraint.addSourceEventRef(ref1) is constraint
        assert constraint.addSourceEventRef(ref2) is constraint
        refs = constraint.getSourceEventRefs()
        assert len(refs) == 2
        assert refs[0] is ref1
        assert refs[1] is ref2

    def test_add_source_event_ref_none_is_no_op(self):
        constraint = SynchronizationPointConstraint(self._parent(), "Sync1")
        assert constraint.addSourceEventRef(None) is constraint
        assert constraint.getSourceEventRefs() == []

    def test_add_target_eec_ref(self):
        constraint = SynchronizationPointConstraint(self._parent(), "Sync1")
        ref1 = self._ref("/AUTOSAR/Group3", "EOC-EXECUTABLE-ENTITY-REF-GROUP")
        ref2 = self._ref("/AUTOSAR/Group4", "EOC-EXECUTABLE-ENTITY-REF-GROUP")
        assert constraint.addTargetEecRef(ref1) is constraint
        assert constraint.addTargetEecRef(ref2) is constraint
        refs = constraint.getTargetEecRefs()
        assert len(refs) == 2
        assert refs[0] is ref1
        assert refs[1] is ref2

    def test_add_target_eec_ref_none_is_no_op(self):
        constraint = SynchronizationPointConstraint(self._parent(), "Sync1")
        assert constraint.addTargetEecRef(None) is constraint
        assert constraint.getTargetEecRefs() == []

    def test_add_target_event_ref(self):
        constraint = SynchronizationPointConstraint(self._parent(), "Sync1")
        ref1 = self._ref("/AUTOSAR/Evt3", "TIMING-DESCRIPTION-EVENT")
        ref2 = self._ref("/AUTOSAR/Evt4", "TIMING-DESCRIPTION-EVENT")
        assert constraint.addTargetEventRef(ref1) is constraint
        assert constraint.addTargetEventRef(ref2) is constraint
        refs = constraint.getTargetEventRefs()
        assert len(refs) == 2
        assert refs[0] is ref1
        assert refs[1] is ref2

    def test_add_target_event_ref_none_is_no_op(self):
        constraint = SynchronizationPointConstraint(self._parent(), "Sync1")
        assert constraint.addTargetEventRef(None) is constraint
        assert constraint.getTargetEventRefs() == []
