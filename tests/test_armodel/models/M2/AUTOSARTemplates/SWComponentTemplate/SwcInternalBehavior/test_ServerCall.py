"""
This module contains comprehensive tests for the ServerCall module in SWComponentTemplate.SwcInternalBehavior.
Tests cover all classes and methods in the ServerCall.py file to achieve 100% test coverage.
"""

import pytest
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.SwcInternalBehavior.ServerCall import (
    ServerCallPoint
)
from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR


class TestServerCallPoint:
    """Test class for ServerCallPoint abstract class."""

    def test_abstract_class_cannot_be_instantiated(self):
        """Test that ServerCallPoint abstract class cannot be instantiated directly."""
        document = AUTOSAR.getInstance()
        ar_root = document.createARPackage("AUTOSAR")
        with pytest.raises(TypeError, match="ServerCallPoint is an abstract class"):
            ServerCallPoint(ar_root, "TestServerCallPoint")

    def test_concrete_subclass_initialization(self):
        """Test that a concrete subclass of ServerCallPoint can be instantiated."""
        from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.SwcInternalBehavior import SynchronousServerCallPoint

        document = AUTOSAR.getInstance()
        ar_root = document.createARPackage("AUTOSAR")
        call_point = SynchronousServerCallPoint(ar_root, "TestServerCallPoint")

        assert call_point.parent == ar_root
        assert call_point.short_name == "TestServerCallPoint"
        assert call_point.returnValueProvision is None
        assert call_point.operationIRef is None
        assert call_point.timeout is None

        # Test getTimeout method to cover line 27 in ServerCall.py
        timeout_value = call_point.getTimeout()
        assert timeout_value is None
        assert timeout_value == call_point.getTimeout()

        # Test setTimeout method
        call_point.setTimeout(5.5)
        assert call_point.getTimeout() == 5.5

        # Test getOperationIRef and setOperationIRef to cover lines 20, 23-24
        assert call_point.getOperationIRef() is None

        from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.Composition.InstanceRefs import ROperationInAtomicSwcInstanceRef
        operation_ref = ROperationInAtomicSwcInstanceRef()
        call_point.setOperationIRef(operation_ref)
        assert call_point.getOperationIRef() == operation_ref
        assert call_point == call_point.setOperationIRef(operation_ref)  # Test method chaining
