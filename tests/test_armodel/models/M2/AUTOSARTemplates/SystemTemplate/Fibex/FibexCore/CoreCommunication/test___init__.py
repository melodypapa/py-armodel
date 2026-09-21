import inspect

from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable import Identifiable
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import RefType, String
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore import FibexElement
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore.CoreCommunication import PdurIPduGroup


class MockParent(ARObject):
    def __init__(self):
        super().__init__()


class Test_PdurIPduGroup:
    """Test cases for PdurIPduGroup (Table 6.34, p.352)."""

    MEMBERS = [
        "communicationMode",
        "iPduRefs",
    ]

    def test_inheritance(self):
        assert issubclass(PdurIPduGroup, FibexElement)
        assert issubclass(PdurIPduGroup, Identifiable)

    def test_class_docstring_note(self):
        expected = "The AUTOSAR PduR will enable and disable the sending of configurable groups of IPdus during runtime according to the AUTOSAR PduR specification. Tags: atp.recommendedPackage=PdurIPduGroups"
        assert inspect.cleandoc(PdurIPduGroup.__doc__) == expected

    def test_initialization_defaults(self):
        pkg = AUTOSAR.getInstance().createARPackage("PdurIPduGroupPkg")
        group = PdurIPduGroup(pkg, "PduGroup1")
        assert group.getCommunicationMode() is None
        assert group.getIPduRefs() == []

    def test_member_order(self):
        pkg = AUTOSAR.getInstance().createARPackage("PdurIPduGroupPkg")
        group = PdurIPduGroup(pkg, "PduGroup1")
        members = [k for k in vars(group) if k in set(self.MEMBERS)]
        assert members == self.MEMBERS

    def test_get_set_communication_mode(self):
        pkg = AUTOSAR.getInstance().createARPackage("PdurIPduGroupPkg")
        group = PdurIPduGroup(pkg, "PduGroup1")
        value = String()
        value.setValue("diagnostic")
        result = group.setCommunicationMode(value)
        assert result is group
        assert group.getCommunicationMode() is value
        group.setCommunicationMode(None)
        assert group.getCommunicationMode() is value

    def test_add_ipdu_ref(self):
        pkg = AUTOSAR.getInstance().createARPackage("PdurIPduGroupPkg")
        group = PdurIPduGroup(pkg, "PduGroup1")
        ref = RefType()
        ref.setValue("/System/Ecu1/PduTriggering1")
        result = group.addIPduRef(ref)
        assert result is group
        assert group.getIPduRefs() == [ref]
        group.addIPduRef(None)
        assert group.getIPduRefs() == [ref]

    def test_arpackage_create_pdur_ipdu_group(self):
        pkg = AUTOSAR.getInstance().createARPackage("PdurIPduGroupPkg")
        group = pkg.createPdurIPduGroup("PduGroup1")
        assert isinstance(group, PdurIPduGroup)
        assert pkg.getElement("PduGroup1", PdurIPduGroup) is group
        again = pkg.createPdurIPduGroup("PduGroup1")
        assert again is group
