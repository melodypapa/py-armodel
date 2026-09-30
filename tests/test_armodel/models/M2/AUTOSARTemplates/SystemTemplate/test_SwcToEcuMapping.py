import inspect
import typing

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable import Identifiable
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import RefType
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.StereotypeMixins import VariationPointCapable
from armodel.models.M2.AUTOSARTemplates.SystemTemplate import SwcToEcuMapping
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.InstanceRefs import ComponentInSystemInstanceRef


class MockParent(ARObject):
    def __init__(self):
        super().__init__()


class Test_SwcToEcuMapping:
    """Test cases for SwcToEcuMapping (Table 5.2, p.197)."""

    MEMBERS = [
        "componentIRefs",
        "controlledHwElementRef",
        "ecuInstanceRef",
        "processingUnitRef",
    ]

    def test_inheritance(self):
        assert issubclass(SwcToEcuMapping, Identifiable)
        assert issubclass(SwcToEcuMapping, VariationPointCapable)

    def test_class_docstring_note(self):
        expected = (
            "This meta-class is used: • to map SwComponentPrototypes to a specific ECU Instance unit, "
            "• optionally to map SwComponentPrototypes to a HwElement with category ProcessingUnit, "
            "• optionally to map SwComponentPrototypes typed by SensorActuatorSwComponentType to a Hw Element with category SensorActuator. "
            "For each combination of ECUInstance and the optional ProcessingUnit and the optional SensorActuator only one SwcToEcuMapping shall be used."
        )
        assert inspect.cleandoc(SwcToEcuMapping.__doc__).startswith(expected)

    def test_class_docstring_constraints(self):
        doc = inspect.cleandoc(SwcToEcuMapping.__doc__)
        assert (
            "[constr_3263] Restriction of usage of SwcToEcuMapping in a System: For all SwcToEcuMappings in a System the following restriction applies: No two SwcToEcuMappings shall have the exact same reference to SwComponentPrototype, EcuInstance, processingUnit, controlledHwElement."
            in doc
        )
        assert (
            "[constr_3021] Mapping of SensorActuatorSwComponents to SensorActuator HwElements: Only SwComponentPrototypes that are typed by SensorActuatorSwComponentType shall be mapped to a HwElement with category SensorActuator via the controlledHwElement relation."
            in doc
        )
        assert (
            '[constr_3249] Category of HwElement for SwcToEcuMapping: The HwElement which is referenced from SwcToEcuMapping in the role processingUnit shall be of category "ProcessingUnit".' in doc
        )

    def test_init_has_no_docstring(self):
        assert SwcToEcuMapping.__init__.__doc__ is None

    def test_initialization_defaults(self):
        parent = MockParent()
        mapping = SwcToEcuMapping(parent, "test_swc_to_ecu_mapping")
        assert mapping.getComponentIRefs() == []
        assert mapping.getControlledHwElementRef() is None
        assert mapping.getEcuInstanceRef() is None
        assert mapping.getProcessingUnitRef() is None

    def test_member_order(self):
        parent = MockParent()
        mapping = SwcToEcuMapping(parent, "test_swc_to_ecu_mapping")
        members = [k for k in vars(mapping) if k in set(self.MEMBERS)]
        assert members == self.MEMBERS

    def test_add_component_i_ref(self):
        parent = MockParent()
        mapping = SwcToEcuMapping(parent, "test_swc_to_ecu_mapping")
        iref = ComponentInSystemInstanceRef()
        result = mapping.addComponentIRef(iref)
        assert result is mapping
        assert mapping.getComponentIRefs() == [iref]
        iref2 = ComponentInSystemInstanceRef()
        mapping.addComponentIRef(iref2)
        assert mapping.getComponentIRefs() == [iref, iref2]
        mapping.addComponentIRef(None)
        assert mapping.getComponentIRefs() == [iref, iref2]

    def test_get_set_controlled_hw_element_ref(self):
        parent = MockParent()
        mapping = SwcToEcuMapping(parent, "test_swc_to_ecu_mapping")
        value = RefType()
        value.setValue("/HwElements/Hw")
        result = mapping.setControlledHwElementRef(value)
        assert result is mapping
        assert mapping.getControlledHwElementRef() is value
        mapping.setControlledHwElementRef(None)
        assert mapping.getControlledHwElementRef() is value

    def test_get_set_ecu_instance_ref(self):
        parent = MockParent()
        mapping = SwcToEcuMapping(parent, "test_swc_to_ecu_mapping")
        value = RefType()
        value.setValue("/System/ECUINSTANCES/EcuTestNode")
        result = mapping.setEcuInstanceRef(value)
        assert result is mapping
        assert mapping.getEcuInstanceRef() is value
        mapping.setEcuInstanceRef(None)
        assert mapping.getEcuInstanceRef() is value

    def test_get_set_processing_unit_ref(self):
        parent = MockParent()
        mapping = SwcToEcuMapping(parent, "test_swc_to_ecu_mapping")
        value = RefType()
        value.setValue("/HwElements/Core0")
        result = mapping.setProcessingUnitRef(value)
        assert result is mapping
        assert mapping.getProcessingUnitRef() is value
        mapping.setProcessingUnitRef(None)
        assert mapping.getProcessingUnitRef() is value

    def test_type_hints(self):
        hints = typing.get_type_hints(SwcToEcuMapping.getComponentIRefs)
        assert hints.get("return") is list or hints.get("return") == typing.List[ComponentInSystemInstanceRef]
        hints = typing.get_type_hints(SwcToEcuMapping.setControlledHwElementRef)
        assert hints.get("value") == typing.Optional[RefType]
        assert hints.get("return") is SwcToEcuMapping
        hints = typing.get_type_hints(SwcToEcuMapping.getEcuInstanceRef)
        assert hints.get("return") == typing.Optional[RefType]
