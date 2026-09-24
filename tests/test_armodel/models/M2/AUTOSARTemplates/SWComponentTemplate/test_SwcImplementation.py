from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.CommonStructure.Implementation import Implementation
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import RefType, String
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.SwcImplementation import SwcImplementation


class TestSwcImplementation:
    def test_spec_notes_are_verbatim(self):
        """Class and member docstrings must be the Table 8.7 Notes copied verbatim."""
        assert (
            SwcImplementation.__doc__.strip()
            == "This meta-class represents a specialization of the general Implementation meta-class with respect to the usage in application software. Tags: atp.recommendedPackage=SwcImplementations"
        )
        behavior_note = "The internal behavior implemented by this Implementation."
        assert SwcImplementation.getBehaviorRef.__doc__.strip() == behavior_note + " [constr_1969]"
        assert SwcImplementation.setBehaviorRef.__doc__.strip() == behavior_note + " [constr_1969] A None value is a no-op and does not overwrite an existing behaviorRef."
        per_instance_memory_size_note = (
            "Allows a definition of the size of the per-instance memory for this implementation. "
            "The aggregation of PerInstanceMemorySize is subject to variability with the purpose to support variability "
            "in the software components implementations. Typically different algorithms in the implementation are "
            "requiring different number of memory objects, in this case PerInstanceMemory."
        )
        assert SwcImplementation.getPerInstanceMemorySizes.__doc__.strip() == per_instance_memory_size_note
        assert SwcImplementation.addPerInstanceMemorySize.__doc__.strip() == per_instance_memory_size_note + " A None value is a no-op and does not append anything."
        required_rte_vendor_note = (
            "Identify a specific RTE vendor. This information is potentially important at the time of integrating "
            "(in particular: linking) the application code with the RTE. The semantics is that (if the association exists) "
            "the corresponding code has been created to fit to the vendor-mode RTE provided by this specific vendor. "
            "Attempting to integrate the code with another RTE generated in vendor mode is in general not possible."
        )
        assert SwcImplementation.getRequiredRTEVendor.__doc__.strip() == required_rte_vendor_note
        assert SwcImplementation.setRequiredRTEVendor.__doc__.strip() == required_rte_vendor_note + " A None value is a no-op and does not overwrite an existing requiredRTEVendor."

    def test_base_and_inheritance_shape(self):
        """Spec Base = ARElement, ..., Implementation, ... — Python base must be the most-derived Implementation; setter return annotations are bare names (PEP 563, Rule 0003)."""
        assert issubclass(SwcImplementation, Implementation)
        assert SwcImplementation.setBehaviorRef.__annotations__["return"] == "SwcImplementation"
        assert SwcImplementation.addPerInstanceMemorySize.__annotations__["return"] == "SwcImplementation"
        assert SwcImplementation.setRequiredRTEVendor.__annotations__["return"] == "SwcImplementation"

    def test_initialization_defaults(self):
        parent = AUTOSAR.getInstance()
        ar_root = parent.createARPackage("AUTOSAR")
        impl = SwcImplementation(ar_root, "TestSwcImplementation")
        assert impl.parent == ar_root
        assert impl.short_name == "TestSwcImplementation"
        assert impl.behaviorRef is None
        assert impl.perInstanceMemorySizes == []
        assert impl.requiredRTEVendor is None
        assert impl.getBehaviorRef() is None
        assert impl.getPerInstanceMemorySizes() == []
        assert impl.getRequiredRTEVendor() is None

    def test_get_set_behavior_ref(self):
        parent = AUTOSAR.getInstance()
        ar_root = parent.createARPackage("AUTOSAR")
        impl = SwcImplementation(ar_root, "TestSwcImplementation")
        behavior_ref = RefType()
        behavior_ref.setValue("/Pkg/SwcInternalBehavior")
        result = impl.setBehaviorRef(behavior_ref)
        assert result is impl
        assert impl.getBehaviorRef() is behavior_ref
        assert impl.getBehaviorRef().getValue() == "/Pkg/SwcInternalBehavior"
        assert impl.setBehaviorRef(None) is impl
        assert impl.getBehaviorRef() is behavior_ref

    def test_add_get_per_instance_memory_sizes(self):
        parent = AUTOSAR.getInstance()
        ar_root = parent.createARPackage("AUTOSAR")
        impl = SwcImplementation(ar_root, "TestSwcImplementation")
        value = object()
        result = impl.addPerInstanceMemorySize(value)
        assert result is impl
        assert impl.getPerInstanceMemorySizes() == [value]
        assert impl.addPerInstanceMemorySize(None) is impl
        assert impl.getPerInstanceMemorySizes() == [value]

    def test_get_set_required_rte_vendor(self):
        parent = AUTOSAR.getInstance()
        ar_root = parent.createARPackage("AUTOSAR")
        impl = SwcImplementation(ar_root, "TestSwcImplementation")
        test_value = String().setValue("Vector")
        result = impl.setRequiredRTEVendor(test_value)
        assert result is impl
        assert impl.getRequiredRTEVendor() is test_value
        assert impl.getRequiredRTEVendor().getValue() == "Vector"
        assert impl.setRequiredRTEVendor(None) is impl
        assert impl.getRequiredRTEVendor() is test_value
