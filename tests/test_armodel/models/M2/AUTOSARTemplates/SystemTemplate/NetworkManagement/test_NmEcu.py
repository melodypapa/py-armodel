from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import Boolean, RefType, TimeValue
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.NetworkManagement import CanNmEcu, NmEcu


class MockParent(ARObject):
    def __init__(self):
        super().__init__()


def _bool(value):
    boolean = Boolean()
    boolean.setValue(value)
    return boolean


def _ref(dest, value):
    ref = RefType()
    ref.setDest(dest)
    ref.setValue(value)
    return ref


class TestNmEcu:
    def test_initialization(self):
        ecu = NmEcu(MockParent(), "NmEcu")
        assert ecu.getShortName() == "NmEcu"
        assert ecu.getBusDependentNmEcus() == []
        assert ecu.getEcuInstanceRef() is None
        assert ecu.getNmBusSynchronizationEnabled() is None
        assert ecu.getNmComControlEnabled() is None
        assert ecu.getNmCoordinator() is None
        assert ecu.getNmCycletimeMainFunction() is None
        assert ecu.getNmPduRxIndicationEnabled() is None
        assert ecu.getNmRemoteSleepIndEnabled() is None
        assert ecu.getNmStateChangeIndEnabled() is None
        assert ecu.getNmUserDataEnabled() is None

    def test_get_set_ecu_instance_ref(self):
        ecu = NmEcu(MockParent(), "NmEcu")
        ref = _ref("ECU-INSTANCE", "/Topology/Ecu1")
        assert ecu.setEcuInstanceRef(ref) is ecu
        assert ecu.getEcuInstanceRef() is ref
        assert ecu.setEcuInstanceRef(None) is ecu
        assert ecu.getEcuInstanceRef() is ref

    def test_get_set_nm_booleans(self):
        ecu = NmEcu(MockParent(), "NmEcu")
        pairs = [
            (ecu.setNmBusSynchronizationEnabled, ecu.getNmBusSynchronizationEnabled),
            (ecu.setNmComControlEnabled, ecu.getNmComControlEnabled),
            (ecu.setNmPduRxIndicationEnabled, ecu.getNmPduRxIndicationEnabled),
            (ecu.setNmRemoteSleepIndEnabled, ecu.getNmRemoteSleepIndEnabled),
            (ecu.setNmStateChangeIndEnabled, ecu.getNmStateChangeIndEnabled),
            (ecu.setNmUserDataEnabled, ecu.getNmUserDataEnabled),
        ]
        for setter, getter in pairs:
            value = _bool(True)
            assert setter(value) is ecu
            assert getter() is value
            setter(None)
            assert getter() is value

    def test_get_set_nm_cycletime_main_function(self):
        ecu = NmEcu(MockParent(), "NmEcu")
        value = TimeValue()
        value.setValue("0.05")
        assert ecu.setNmCycletimeMainFunction(value) is ecu
        assert ecu.getNmCycletimeMainFunction() is value
        ecu.setNmCycletimeMainFunction(None)
        assert ecu.getNmCycletimeMainFunction() is value

    def test_get_set_nm_coordinator(self):
        ecu = NmEcu(MockParent(), "NmEcu")
        coordinator = CanNmEcu()
        assert ecu.setNmCoordinator(coordinator) is ecu
        assert ecu.getNmCoordinator() is coordinator
        ecu.setNmCoordinator(None)
        assert ecu.getNmCoordinator() is coordinator

    def test_add_bus_dependent_nm_ecu(self):
        ecu = NmEcu(MockParent(), "NmEcu")
        can_ecu = CanNmEcu()
        assert ecu.addBusDependentNmEcu(can_ecu) is ecu
        assert ecu.getBusDependentNmEcus() == [can_ecu]
        ecu.addBusDependentNmEcu(None)
        assert ecu.getBusDependentNmEcus() == [can_ecu]
