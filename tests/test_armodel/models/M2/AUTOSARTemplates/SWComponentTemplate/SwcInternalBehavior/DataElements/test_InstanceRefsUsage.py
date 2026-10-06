"""
This module contains comprehensive tests for the InstanceRefsUsage module in SWComponentTemplate.SwcInternalBehavior.
Tests cover all classes and methods in the InstanceRefsUsage.py file to achieve 100% test coverage.
"""

from armodel.models.M2.AUTOSARTemplates.GenericStructure.AbstractStructure import AtpInstanceRef
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import RefType
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.SwcInternalBehavior.DataElements import (
    ArVariableInImplementationDataInstanceRef,
    AutosarParameterRef,
)
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.SwcInternalBehavior.DataElements.InstanceRefsUsage import (
    ParameterInAtomicSWCTypeInstanceRef,
    VariableInAtomicSWCTypeInstanceRef,
)


class TestArVariableInImplementationDataInstanceRef:
    """Test class for ArVariableInImplementationDataInstanceRef class."""

    def test_ar_variable_in_implementation_data_instance_ref_initialization(self):
        """Test ArVariableInImplementationDataInstanceRef initialization and methods."""
        iref = ArVariableInImplementationDataInstanceRef()

        assert iref.contextDataPrototypeRefs == []
        assert iref.portPrototypeRef is None
        assert iref.rootVariableDataPrototypeRef is None
        assert iref.targetDataPrototypeRef is None

    def test_table_5_37_model_shape_and_docstrings(self):
        iref = ArVariableInImplementationDataInstanceRef()
        assert iref.getContextDataPrototypeRefs() == []
        assert iref.addContextDataPrototypeRef(None) is iref
        assert iref.getContextDataPrototypeRefs() == []
        assert iref.setPortPrototypeRef(None) is iref
        assert iref.setRootVariableDataPrototypeRef(None) is iref
        assert iref.setTargetDataPrototypeRef(None) is iref
        assert iref.__init__.__doc__ is None
        assert iref.__class__.__doc__.strip() == (
            "This class represents the ability to navigate into a data element inside of an VariableDataPrototype "
            "which is typed by an ImplementationDatatype. Note that it shall not be used if the target is the "
            "VariableDataPrototype itself (e.g. if its a primitive). Note that this class follows the pattern of "
            "an InstanceRef but is not implemented based on the abstract classes because the ImplementationDataType "
            "isn't either, especially because ImplementationDataType Element isn't derived from AtpPrototype."
        )
        context_note = "This is a context in case there are subelements with explicit types. The reference has to be ordered to properly reflect the nested structure."
        assert iref.getContextDataPrototypeRefs.__doc__.strip() == context_note
        assert iref.addContextDataPrototypeRef.__doc__.strip() == context_note + " A None value is a no-op and does not append anything."

        # Test contextDataPrototypeRefs methods
        from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import RefType

        ref = RefType()
        ref.setValue("/Test/Ref")
        iref.addContextDataPrototypeRef(ref)
        assert ref in iref.getContextDataPrototypeRefs()

        # Test portPrototypeRef methods
        port_ref = RefType()
        port_ref.setValue("/Port/Ref")
        iref.setPortPrototypeRef(port_ref)
        assert iref.getPortPrototypeRef() == port_ref

        # Test rootVariableDataPrototypeRef methods
        root_ref = RefType()
        root_ref.setValue("/Root/Variable")
        iref.setRootVariableDataPrototypeRef(root_ref)
        assert iref.getRootVariableDataPrototypeRef() == root_ref

        # Test targetDataPrototypeRef methods
        target_ref = RefType()
        target_ref.setValue("/Target/Data")
        iref.setTargetDataPrototypeRef(target_ref)
        assert iref.getTargetDataPrototypeRef() == target_ref


class TestVariableInAtomicSWCTypeInstanceRef:
    """Test class for VariableInAtomicSWCTypeInstanceRef class."""

    def test_variable_in_atomic_swc_type_instance_ref_initialization(self):
        """Test VariableInAtomicSWCTypeInstanceRef initialization and methods."""
        iref = VariableInAtomicSWCTypeInstanceRef()

        assert iref.targetDataPrototypeRef is None

    def test_table_d18_shape(self):
        iref = VariableInAtomicSWCTypeInstanceRef()
        assert isinstance(iref, AtpInstanceRef)
        assert iref.getTargetDataPrototypeRef() is None

        # Test targetDataPrototypeRef methods
        from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import RefType

        target_ref = RefType()
        target_ref.setValue("/Target/Data")
        iref.setTargetDataPrototypeRef(target_ref)
        assert iref.getTargetDataPrototypeRef() == target_ref


class TestParameterInAtomicSWCTypeInstanceRef:
    """Test class for ParameterInAtomicSWCTypeInstanceRef class (Table 5.36, p.319, R23-11)."""

    def _make_ref(self, value: str) -> RefType:
        ref = RefType()
        ref.setValue(value)
        return ref

    def test_initialization(self):
        """Test that all fields start at their spec-multiplicity defaults."""
        iref = ParameterInAtomicSWCTypeInstanceRef()

        assert isinstance(iref, AtpInstanceRef)
        assert iref.baseRef is None
        assert iref.contextDataPrototypeRefs == []
        assert iref.portPrototypeRef is None
        assert iref.rootParameterDataPrototypeRef is None
        assert iref.targetDataPrototypeRef is None

    def test_get_set_base_ref(self):
        """Test baseRef round-trip, chaining and the None no-op."""
        iref = ParameterInAtomicSWCTypeInstanceRef()
        base_ref = self._make_ref("/Base/Ref")

        assert iref.setBaseRef(base_ref) is iref
        assert iref.getBaseRef() == base_ref
        assert iref.setBaseRef(None) is iref
        assert iref.getBaseRef() == base_ref

    def test_add_get_context_data_prototype_refs(self):
        """Test contextDataPrototypeRefs append order, chaining and the None no-op."""
        iref = ParameterInAtomicSWCTypeInstanceRef()
        assert iref.getContextDataPrototypeRefs() == []

        first = self._make_ref("/Context/First")
        second = self._make_ref("/Context/Second")

        assert iref.addContextDataPrototypeRef(first) is iref
        iref.addContextDataPrototypeRef(second)
        assert iref.getContextDataPrototypeRefs() == [first, second]
        assert iref.addContextDataPrototypeRef(None) is iref
        assert iref.getContextDataPrototypeRefs() == [first, second]

    def test_get_set_port_prototype_ref(self):
        """Test portPrototypeRef round-trip, chaining and the None no-op."""
        iref = ParameterInAtomicSWCTypeInstanceRef()
        port_ref = self._make_ref("/Swc/Port")

        assert iref.setPortPrototypeRef(port_ref) is iref
        assert iref.getPortPrototypeRef() == port_ref
        assert iref.setPortPrototypeRef(None) is iref
        assert iref.getPortPrototypeRef() == port_ref

    def test_get_set_root_parameter_data_prototype_ref(self):
        """Test rootParameterDataPrototypeRef round-trip, chaining and the None no-op."""
        iref = ParameterInAtomicSWCTypeInstanceRef()
        root_ref = self._make_ref("/Swc/RootParameter")

        assert iref.setRootParameterDataPrototypeRef(root_ref) is iref
        assert iref.getRootParameterDataPrototypeRef() == root_ref
        assert iref.setRootParameterDataPrototypeRef(None) is iref
        assert iref.getRootParameterDataPrototypeRef() == root_ref

    def test_get_set_target_data_prototype_ref(self):
        """Test targetDataPrototypeRef round-trip, chaining and the None no-op."""
        iref = ParameterInAtomicSWCTypeInstanceRef()
        target_ref = self._make_ref("/Swc/TargetElement")

        assert iref.setTargetDataPrototypeRef(target_ref) is iref
        assert iref.getTargetDataPrototypeRef() == target_ref
        assert iref.setTargetDataPrototypeRef(None) is iref
        assert iref.getTargetDataPrototypeRef() == target_ref

    def test_table_5_36_docstrings(self):
        """Test that every docstring is the spec Note verbatim (Table 5.36)."""
        iref = ParameterInAtomicSWCTypeInstanceRef()

        assert iref.__class__.__doc__.strip() == ("This class implements an instance reference which can be applied for variables as well as for parameters.")
        assert iref.__init__.__doc__ is None

        base_note = "Stereotypes: atpDerived Tags: xml.sequenceOffset=10"
        assert iref.getBaseRef.__doc__.strip() == base_note
        assert iref.setBaseRef.__doc__.strip() == base_note + ". A None value is a no-op and does not overwrite an existing baseRef."

        context_note = "This ist the context in a compositeDataType."
        assert iref.getContextDataPrototypeRefs.__doc__.strip() == context_note
        assert iref.addContextDataPrototypeRef.__doc__.strip() == context_note + " A None value is a no-op and does not append anything."

        port_note = "This is the port providing the variable or the entry point to the variable structure."
        assert iref.getPortPrototypeRef.__doc__.strip() == port_note
        assert iref.setPortPrototypeRef.__doc__.strip() == port_note + " A None value is a no-op and does not overwrite an existing portPrototypeRef."

        root_note = "This represents the entry point for references into a CompositeDataType."
        assert iref.getRootParameterDataPrototypeRef.__doc__.strip() == root_note
        assert iref.setRootParameterDataPrototypeRef.__doc__.strip() == root_note + " A None value is a no-op and does not overwrite an existing rootParameterDataPrototypeRef."

        target_note = (
            "This is the target parameter element. Note that this must be nested in ParameterDataPrototype. "
            "The target must be one of ParameterDataPrototype, ApplicationCompositeElementDataPrototype."
        )
        assert iref.getTargetDataPrototypeRef.__doc__.strip() == target_note
        assert iref.setTargetDataPrototypeRef.__doc__.strip() == target_note + " A None value is a no-op and does not overwrite an existing targetDataPrototypeRef."


class TestAutosarParameterRef:
    """Test class for AutosarParameterRef class."""

    def test_autosar_parameter_ref_initialization(self):
        """Test AutosarParameterRef initialization and methods."""
        param_ref = AutosarParameterRef()

        assert param_ref.autosarParameterIRef is None
        assert param_ref.localParameterRef is None

        # Test autosarParameterIRef methods
        from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.SwcInternalBehavior.DataElements.InstanceRefsUsage import ParameterInAtomicSWCTypeInstanceRef

        iref = ParameterInAtomicSWCTypeInstanceRef()
        param_ref.setAutosarParameterIRef(iref)
        assert param_ref.getAutosarParameterIRef() == iref

        # Test localParameterRef methods
        from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import RefType

        local_ref = RefType()
        local_ref.setValue("/Local/Param")
        param_ref.setLocalParameterRef(local_ref)
        assert param_ref.getLocalParameterRef() == local_ref
