from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import RefType
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.NetworkManagement import FlexrayNmClusterCoupling, FlexrayNmScheduleVariant


def _ref(dest, value):
    ref = RefType()
    ref.setDest(dest)
    ref.setValue(value)
    return ref


class TestFlexrayNmClusterCoupling:
    def test_initialization(self):
        coupling = FlexrayNmClusterCoupling()
        assert coupling.getCoupledClusterRefs() == []
        assert coupling.getNmScheduleVariant() is None

    def test_add_get_coupled_cluster_refs(self):
        coupling = FlexrayNmClusterCoupling()
        ref = _ref("FLEXRAY-CLUSTER", "/Clusters/Fr1")
        assert coupling.addCoupledClusterRef(ref) is coupling
        assert coupling.getCoupledClusterRefs() == [ref]

    def test_get_set_nm_schedule_variant(self):
        coupling = FlexrayNmClusterCoupling()
        value = FlexrayNmScheduleVariant()
        value.setValue(FlexrayNmScheduleVariant.SCHEDULE_VARIANT_2)
        assert coupling.setNmScheduleVariant(value) is coupling
        assert coupling.getNmScheduleVariant() is value
        coupling.setNmScheduleVariant(None)
        assert coupling.getNmScheduleVariant() is value


class TestFlexrayNmScheduleVariant:
    def test_members_and_values(self):
        assert FlexrayNmScheduleVariant.SCHEDULE_VARIANT_1 == "SCHEDULE-VARIANT-1"
        assert FlexrayNmScheduleVariant.SCHEDULE_VARIANT_2 == "SCHEDULE-VARIANT-2"
        assert FlexrayNmScheduleVariant.SCHEDULE_VARIANT_3 == "SCHEDULE-VARIANT-3"
        assert FlexrayNmScheduleVariant.SCHEDULE_VARIANT_4 == "SCHEDULE-VARIANT-4"
        assert FlexrayNmScheduleVariant.SCHEDULE_VARIANT_5 == "SCHEDULE-VARIANT-5"
        assert FlexrayNmScheduleVariant.SCHEDULE_VARIANT_6 == "SCHEDULE-VARIANT-6"
        assert FlexrayNmScheduleVariant.SCHEDULE_VARIANT_7 == "SCHEDULE-VARIANT-7"

    def test_instantiable(self):
        enum = FlexrayNmScheduleVariant()
        enum.setValue(FlexrayNmScheduleVariant.SCHEDULE_VARIANT_7)
        assert enum.getValue() == FlexrayNmScheduleVariant.SCHEDULE_VARIANT_7
