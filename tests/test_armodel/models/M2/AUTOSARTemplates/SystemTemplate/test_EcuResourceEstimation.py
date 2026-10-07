import inspect
import typing

from armodel.models.M2.AUTOSARTemplates.CommonStructure.ResourceConsumption import ResourceConsumption
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import RefType
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.SWmapping import EcuResourceEstimation


class TestEcuResourceEstimation:
    """Test cases for EcuResourceEstimation (Table 5.43, p.260)."""

    MEMBERS = [
        "bswResourceEstimation",
        "ecuInstanceRef",
        "introduction",
        "rteResourceEstimation",
        "swCompToEcuMappingRefs",
    ]

    def test_inheritance(self):
        assert issubclass(EcuResourceEstimation, ARObject)

    def test_instantiable(self):
        EcuResourceEstimation()

    def test_class_docstring_note(self):
        expected = "Resource estimations for RTE and BSW of a single ECU instance."
        assert inspect.cleandoc(EcuResourceEstimation.__doc__) == expected

    def test_init_has_no_docstring(self):
        assert EcuResourceEstimation.__init__.__doc__ is None

    def test_initialization_defaults(self):
        estimation = EcuResourceEstimation()
        assert estimation.getBswResourceEstimation() is None
        assert estimation.getEcuInstanceRef() is None
        assert estimation.getIntroduction() is None
        assert estimation.getRteResourceEstimation() is None
        assert estimation.getSwCompToEcuMappingRefs() == []

    def test_member_order(self):
        estimation = EcuResourceEstimation()
        members = [k for k in vars(estimation) if k in set(self.MEMBERS)]
        assert members == self.MEMBERS

    def test_create_bsw_resource_estimation(self):
        estimation = EcuResourceEstimation()
        consumption = estimation.createBswResourceEstimation("BswConsumption")
        assert isinstance(consumption, ResourceConsumption)
        assert consumption.getShortName() == "BswConsumption"
        assert estimation.getBswResourceEstimation() is consumption
        duplicate = estimation.createBswResourceEstimation("BswConsumption")
        assert duplicate is consumption

    def test_create_rte_resource_estimation(self):
        estimation = EcuResourceEstimation()
        consumption = estimation.createRteResourceEstimation("RteConsumption")
        assert isinstance(consumption, ResourceConsumption)
        assert consumption.getShortName() == "RteConsumption"
        assert estimation.getRteResourceEstimation() is consumption
        duplicate = estimation.createRteResourceEstimation("RteConsumption")
        assert duplicate is consumption

    def test_get_set_ecu_instance_ref(self):
        estimation = EcuResourceEstimation()
        ref = RefType()
        ref.setValue("/Ecu/Ecu1")
        ref.setDest("ECU-INSTANCE")
        result = estimation.setEcuInstanceRef(ref)
        assert result is estimation
        assert estimation.getEcuInstanceRef() is ref
        estimation.setEcuInstanceRef(None)
        assert estimation.getEcuInstanceRef() is ref

    def test_add_sw_comp_to_ecu_mapping_ref(self):
        estimation = EcuResourceEstimation()
        ref1 = RefType()
        ref1.setValue("/Mapping/SwcToEcu1")
        ref2 = RefType()
        ref2.setValue("/Mapping/SwcToEcu2")
        result = estimation.addSwCompToEcuMappingRef(ref1)
        assert result is estimation
        estimation.addSwCompToEcuMappingRef(ref2)
        assert estimation.getSwCompToEcuMappingRefs() == [ref1, ref2]
        estimation.addSwCompToEcuMappingRef(None)
        assert len(estimation.getSwCompToEcuMappingRefs()) == 2

    def test_type_hints(self):
        hints = typing.get_type_hints(EcuResourceEstimation.getBswResourceEstimation)
        assert hints["return"] == typing.Optional[ResourceConsumption]
        hints = typing.get_type_hints(EcuResourceEstimation.createBswResourceEstimation)
        assert hints["return"] is ResourceConsumption
        hints = typing.get_type_hints(EcuResourceEstimation.getEcuInstanceRef)
        assert hints["return"] == typing.Optional[RefType]
        hints = typing.get_type_hints(EcuResourceEstimation.setEcuInstanceRef)
        assert hints["value"] == typing.Optional[RefType]
        hints = typing.get_type_hints(EcuResourceEstimation.getSwCompToEcuMappingRefs)
        assert hints["return"] == typing.List[RefType]
        hints = typing.get_type_hints(EcuResourceEstimation.addSwCompToEcuMappingRef)
        assert hints["value"] == typing.Optional[RefType]
