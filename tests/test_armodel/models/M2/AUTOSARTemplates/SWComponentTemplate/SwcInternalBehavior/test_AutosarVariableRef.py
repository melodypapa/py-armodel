"""
This module contains comprehensive tests for the AutosarVariableRef module in SWComponentTemplate.SwcInternalBehavior.
Tests cover all classes and methods in the AutosarVariableRef.py file to achieve 100% test coverage.
"""

from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.SwcInternalBehavior.DataElements import (
    AutosarVariableRef,
)


class TestAutosarVariableRef:
    """Test class for AutosarVariableRef class."""

    def test_autosar_variable_ref_initialization(self):
        """Test AutosarVariableRef initialization and methods."""
        var_ref = AutosarVariableRef()

        assert var_ref.autosarVariableIRef is None
        assert var_ref.autosarVariableInImplDatatype is None
        assert var_ref.localVariableRef is None

        # Test autosarVariableIRef methods
        from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.SwcInternalBehavior.DataElements.InstanceRefs import (
            VariableInAtomicSWCTypeInstanceRef,
        )
        iref = VariableInAtomicSWCTypeInstanceRef()
        var_ref.setAutosarVariableIRef(iref)
        assert var_ref.getAutosarVariableIRef() == iref

        # Test autosarVariableInImplDatatype methods
        from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.SwcInternalBehavior.DataElements import (
            ArVariableInImplementationDataInstanceRef,
        )
        impl_datatype = ArVariableInImplementationDataInstanceRef()
        var_ref.setAutosarVariableInImplDatatype(impl_datatype)
        assert var_ref.getAutosarVariableInImplDatatype() == impl_datatype

        # Test localVariableRef methods
        local_ref = VariableInAtomicSWCTypeInstanceRef()
        var_ref.setLocalVariableRef(local_ref)
        assert var_ref.getLocalVariableRef() == local_ref
