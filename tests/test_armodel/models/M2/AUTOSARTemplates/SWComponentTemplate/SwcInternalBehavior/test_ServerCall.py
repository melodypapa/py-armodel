"""
This module contains tests for the ServerCall module in SWComponentTemplate.SwcInternalBehavior.
"""

import pytest

from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import TimeValue
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.SwcInternalBehavior.ServerCall import ServerCallPoint

SPEC_NOTE = "If a RunnableEntity owns a ServerCallPoint it is entitled to invoke a particular ClientServerOperation of a specific RPortPrototype of the corresponding AtomicSwComponentType"


class TestServerCallPoint:
    """Test cases for the abstract ServerCallPoint class (Table 7.35)."""

    def test_abstract_class_cannot_be_instantiated(self):
        document = AUTOSAR.getInstance()
        ar_root = document.createARPackage("AUTOSAR")
        with pytest.raises(TypeError, match="ServerCallPoint is an abstract class"):
            ServerCallPoint(ar_root, "TestServerCallPoint")

    def test_initialization(self):
        from armodel.models.M2.AUTOSARTemplates.GenericStructure.AbstractStructure import AtpStructureElement
        from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.SwcInternalBehavior import SynchronousServerCallPoint
        from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.SwcInternalBehavior.AccessCount import AbstractAccessPoint

        document = AUTOSAR.getInstance()
        ar_root = document.createARPackage("AUTOSAR")
        call_point = SynchronousServerCallPoint(ar_root, "TestServerCallPoint")

        assert isinstance(call_point, AbstractAccessPoint)
        assert isinstance(call_point, AtpStructureElement)
        assert call_point.parent == ar_root
        assert call_point.short_name == "TestServerCallPoint"
        assert call_point.operationIRef is None
        assert call_point.timeout is None

    def test_class_docstring_verbatim(self):
        assert ServerCallPoint.__doc__.strip() == SPEC_NOTE

    def test_operation_iref_round_trip(self):
        from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.Components.InstanceRefs import ROperationInAtomicSwcInstanceRef
        from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.SwcInternalBehavior import SynchronousServerCallPoint

        document = AUTOSAR.getInstance()
        ar_root = document.createARPackage("AUTOSAR")
        call_point = SynchronousServerCallPoint(ar_root, "TestOperationIRef")

        assert call_point.getOperationIRef() is None

        operation_iref = ROperationInAtomicSwcInstanceRef()
        result = call_point.setOperationIRef(operation_iref)
        assert result is call_point
        assert call_point.getOperationIRef() is operation_iref

        call_point.setOperationIRef(None)
        assert call_point.getOperationIRef() is operation_iref

    def test_timeout_round_trip(self):
        from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.SwcInternalBehavior import SynchronousServerCallPoint

        document = AUTOSAR.getInstance()
        ar_root = document.createARPackage("AUTOSAR")
        call_point = SynchronousServerCallPoint(ar_root, "TestTimeout")

        assert call_point.getTimeout() is None

        timeout = TimeValue().setValue(0.005)
        result = call_point.setTimeout(timeout)
        assert result is call_point
        assert call_point.getTimeout() is timeout

        call_point.setTimeout(None)
        assert call_point.getTimeout() is timeout
