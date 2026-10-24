"""
This module contains tests for the ApplicationInterface class in the
AUTOSAR AbstractPlatform module.
"""

from armodel.models.M2.AUTOSARTemplates.AbstractPlatform import ApplicationInterface
from armodel.models.M2.AUTOSARTemplates.AdaptivePlatform.ApplicationDesign.PortInterface import Field
from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.Datatype.DataPrototypes import VariableDataPrototype
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.PortInterface import ClientServerOperation


class TestApplicationInterface:
    """
    Test class for ApplicationInterface functionality.
    """

    def _parent(self):
        document = AUTOSAR.getInstance()
        document.clear()
        document.setARRelease("R23-11")
        return document.createARPackage("AUTOSAR")

    def _interface(self):
        return ApplicationInterface(self._parent(), "AppInterface")

    def test_initialization(self):
        obj = self._interface()
        assert isinstance(obj, ApplicationInterface)
        assert obj.getAttributes() == []
        assert obj.getCommands() == []
        assert obj.getIndications() == []

    def test_get_set_attributes(self):
        obj = self._interface()
        field = Field(obj, "Field1")
        field.setHasGetter(True)
        assert obj.setAttributes([field]) is obj
        assert obj.getAttributes() == [field]

    def test_create_attribute(self):
        obj = self._interface()
        field = obj.createAttribute("Field1")
        field.setHasGetter(True)
        assert isinstance(field, Field)
        assert obj.getAttributes() == [field]
        field2 = obj.createAttribute("Field1")
        assert field2 is field
        field2.setHasGetter(True)
        assert obj.getAttributes() == [field]

    def test_get_set_commands(self):
        obj = self._interface()
        operation = ClientServerOperation(obj, "Operation1")
        assert obj.setCommands([operation]) is obj
        assert obj.getCommands() == [operation]

    def test_create_command(self):
        obj = self._interface()
        operation = obj.createCommand("Operation1")
        assert isinstance(operation, ClientServerOperation)
        assert obj.getCommands() == [operation]
        assert obj.createCommand("Operation1") is operation

    def test_get_set_indications(self):
        obj = self._interface()
        indication = VariableDataPrototype(obj, "Indication1")
        assert obj.setIndications([indication]) is obj
        assert obj.getIndications() == [indication]

    def test_create_indication(self):
        obj = self._interface()
        indication = obj.createIndication("Indication1")
        assert isinstance(indication, VariableDataPrototype)
        assert obj.getIndications() == [indication]
        assert obj.createIndication("Indication1") is indication
