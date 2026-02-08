"""
This module contains comprehensive tests for the InstanceRefsUsage module in SWComponentTemplate.SwcInternalBehavior.
Tests cover all classes and methods in the InstanceRefsUsage.py file to achieve 100% test coverage.
"""

from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.SwcInternalBehavior.DataElements import (
    ArVariableInImplementationDataInstanceRef,
    AutosarParameterRef,
)
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.SwcInternalBehavior.DataElements.InstanceRefs import (
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

        # Test contextDataPrototypeRefs methods
        from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
            RefType,
        )
        ref = RefType()
        ref.setValue("/Test/Ref")
        iref.setContextDataPrototypeRefs([ref])
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

        assert iref.baseRef is None
        assert iref.contextDataPrototypeRefs == []
        assert iref.portPrototypeRef is None
        assert iref.rootVariableDataPrototypeRef is None
        assert iref.targetDataPrototypeRef is None

        # Test baseRef methods
        from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
            RefType,
        )
        base_ref = RefType()
        base_ref.setValue("/Base/Ref")
        iref.setBaseRef(base_ref)
        assert iref.getBaseRef() == base_ref

        # Test contextDataPrototypeRefs methods
        context_ref = RefType()
        context_ref.setValue("/Context/Ref")
        iref.addContextDataPrototypeRef(context_ref)
        assert context_ref in iref.getContextDataPrototypeRefs()

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


class TestParameterInAtomicSWCTypeInstanceRef:
    """Test class for ParameterInAtomicSWCTypeInstanceRef class."""

    def test_parameter_in_atomic_swc_type_instance_ref_initialization(self):
        """Test ParameterInAtomicSWCTypeInstanceRef initialization and methods."""
        iref = ParameterInAtomicSWCTypeInstanceRef()

        assert iref.baseRef is None
        assert iref.contextDataPrototypeRef is None
        assert iref.portPrototypeRef is None
        assert iref.rootParameterDataPrototypeRef is None
        assert iref.targetDataPrototypeRef is None

        # Test baseRef methods
        from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
            RefType,
        )
        base_ref = RefType()
        base_ref.setValue("/Base/Ref")
        iref.setBaseRef(base_ref)
        assert iref.getBaseRef() == base_ref

        # Test contextDataPrototypeRef methods
        context_ref = RefType()
        context_ref.setValue("/Context/Ref")
        iref.setContextDataPrototypeRef(context_ref)
        assert iref.getContextDataPrototypeRef() == context_ref

        # Test portPrototypeRef methods
        port_ref = RefType()
        port_ref.setValue("/Port/Ref")
        iref.setPortPrototypeRef(port_ref)
        assert iref.getPortPrototypeRef() == port_ref

        # Test rootParameterDataPrototypeRef methods
        root_ref = RefType()
        root_ref.setValue("/Root/Parameter")
        iref.setRootParameterDataPrototypeRef(root_ref)
        assert iref.getRootParameterDataPrototypeRef() == root_ref

        # Test targetDataPrototypeRef methods
        target_ref = RefType()
        target_ref.setValue("/Target/Data")
        iref.setTargetDataPrototypeRef(target_ref)
        assert iref.getTargetDataPrototypeRef() == target_ref


class TestAutosarParameterRef:
    """Test class for AutosarParameterRef class."""

    def test_autosar_parameter_ref_initialization(self):
        """Test AutosarParameterRef initialization and methods."""
        param_ref = AutosarParameterRef()

        assert param_ref.autosarParameterIRef is None
        assert param_ref.localParameterRef is None

        # Test autosarParameterIRef methods
        from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.SwcInternalBehavior.DataElements.InstanceRefs import (
            ParameterInAtomicSWCTypeInstanceRef,
        )
        iref = ParameterInAtomicSWCTypeInstanceRef()
        param_ref.setAutosarParameterIRef(iref)
        assert param_ref.getAutosarParameterIRef() == iref

        # Test localParameterRef methods
        from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
            RefType,
        )
        local_ref = RefType()
        local_ref.setValue("/Local/Param")
        param_ref.setLocalParameterRef(local_ref)
        assert param_ref.getLocalParameterRef() == local_ref
