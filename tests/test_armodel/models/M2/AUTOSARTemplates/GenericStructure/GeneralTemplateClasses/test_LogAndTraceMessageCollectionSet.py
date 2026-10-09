"""
This module contains tests for the LogAndTraceMessageCollectionSet class in the
AUTOSAR GenericStructure.GeneralTemplateClasses module.
"""

from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ARPackage import LogAndTraceMessageCollectionSet
from armodel.models.M2.AUTOSARTemplates.LogAndTraceExtract import DltMessage


class TestLogAndTraceMessageCollectionSet:
    """
    Test class for LogAndTraceMessageCollectionSet functionality.
    """

    def _parent(self):
        document = AUTOSAR.getInstance()
        document.clear()
        document.setARRelease("R23-11")
        return document.createARPackage("AUTOSAR")

    def _obj(self):
        return LogAndTraceMessageCollectionSet(self._parent(), "ValueSet")

    def test_initialization(self):
        obj = self._obj()
        assert isinstance(obj, LogAndTraceMessageCollectionSet)
        assert obj.getDltMessages() == []

    def test_add_get(self):
        obj = self._obj()
        value = DltMessage(obj, "Message")
        assert obj.addDltMessage(value) is obj
        assert obj.getDltMessages() == [value]
