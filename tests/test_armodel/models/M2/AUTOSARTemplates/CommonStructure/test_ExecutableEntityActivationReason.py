from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.CommonStructure.Implementation import ImplementationProps
from armodel.models.M2.AUTOSARTemplates.CommonStructure.InternalBehavior import ExecutableEntityActivationReason
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable import Referrable
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import PositiveInteger


class TestExecutableEntityActivationReason:
    def test_initialization(self):
        document = AUTOSAR.getInstance()
        ar_root = document.createARPackage("AUTOSAR")
        obj = ExecutableEntityActivationReason(ar_root, "act_reason")
        assert isinstance(obj, ARObject)
        assert isinstance(obj, Referrable)
        assert isinstance(obj, ImplementationProps)
        assert obj.short_name == "act_reason"
        assert obj.getBitPosition() is None
        assert obj.getSymbol() is None

    def test_get_set_bitPosition(self):
        document = AUTOSAR.getInstance()
        ar_root = document.createARPackage("AUTOSAR")
        obj = ExecutableEntityActivationReason(ar_root, "act_reason")
        value = PositiveInteger().setValue("4")
        assert obj.setBitPosition(value) is obj
        assert obj.getBitPosition().getValue() == 4
        obj.setBitPosition(None)
        assert obj.getBitPosition().getValue() == 4
