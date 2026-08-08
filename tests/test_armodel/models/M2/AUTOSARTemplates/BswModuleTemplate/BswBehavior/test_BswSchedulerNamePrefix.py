"""
This module contains tests for the BswSchedulerNamePrefix class in the
AUTOSAR BswModuleTemplate.BswBehavior module.
"""

from armodel.models.M2.AUTOSARTemplates.BswModuleTemplate.BswBehavior.BswSchedulerNamePrefix import (
    BswSchedulerNamePrefix,
)


class TestBswSchedulerNamePrefix:
    """
    Test class for BswSchedulerNamePrefix functionality.
    """

    def test_initialization(self):
        obj = BswSchedulerNamePrefix()
        assert isinstance(obj, BswSchedulerNamePrefix)

    def test_prefix_setter_chaining(self):
        obj = BswSchedulerNamePrefix().setPrefix("pre_")
        assert obj.getPrefix() == "pre_"
