"""Tests for writer ServerCallPoint handlers."""

import xml.etree.ElementTree as ET

import pytest

from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import TimeValue
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.Components.InstanceRefs import ROperationInAtomicSwcInstanceRef
from armodel.writer.arxml_writer import ARXMLWriter


@pytest.fixture(autouse=True)
def reset_autosar():
    AUTOSAR.getInstance().new()
    yield
    AUTOSAR.getInstance().new()


@pytest.fixture
def writer():
    AUTOSAR.getInstance().new()
    return ARXMLWriter()


def _parent():
    return ET.Element("PARENT")


class TestServerCallPoint:

    def _make_entity(self):
        from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.SwcInternalBehavior import SwcInternalBehavior

        document = AUTOSAR.getInstance()
        ar_root = document.createARPackage("AUTOSAR")
        behavior = SwcInternalBehavior(ar_root, "MyIB")
        return behavior.createRunnableEntity("re_main")

    def test_write_field_values(self, writer):
        entity = self._make_entity()
        sync_point = entity.createSynchronousServerCallPoint("scp_sync")
        operation_iref = ROperationInAtomicSwcInstanceRef()
        operation_iref.setContextRPortRef(_ref_stub("R-PORT-PROTOTYPE", "/MyComponents/rp_cs"))
        operation_iref.setTargetRequiredOperationRef(_ref_stub("CLIENT-SERVER-OPERATION", "/MyComponents/IfCs/op1"))
        sync_point.setOperationIRef(operation_iref)
        sync_point.setTimeout(TimeValue().setValue(0.005))
        async_point = entity.createAsynchronousServerCallPoint("scp_async")
        async_operation_iref = ROperationInAtomicSwcInstanceRef()
        async_operation_iref.setTargetRequiredOperationRef(_ref_stub("CLIENT-SERVER-OPERATION", "/MyComponents/IfCs/op2"))
        async_point.setOperationIRef(async_operation_iref)

        parent = _parent()
        writer.writeRunnableEntityServerCallPoints(parent, entity)

        points_tag = parent.find("SERVER-CALL-POINTS")
        assert points_tag is not None

        sync_elem = points_tag.find("SYNCHRONOUS-SERVER-CALL-POINT")
        assert sync_elem is not None
        assert sync_elem.find("SHORT-NAME").text == "scp_sync"

        operation_iref_elem = sync_elem.find("OPERATION-IREF")
        assert operation_iref_elem is not None
        context_ref = operation_iref_elem.find("CONTEXT-R-PORT-REF")
        assert context_ref is not None
        assert context_ref.attrib["DEST"] == "R-PORT-PROTOTYPE"
        assert context_ref.text == "/MyComponents/rp_cs"
        target_ref = operation_iref_elem.find("TARGET-REQUIRED-OPERATION-REF")
        assert target_ref is not None
        assert target_ref.attrib["DEST"] == "CLIENT-SERVER-OPERATION"
        assert target_ref.text == "/MyComponents/IfCs/op1"

        timeout_elem = sync_elem.find("TIMEOUT")
        assert timeout_elem is not None
        assert timeout_elem.text == "0.005"

        async_elem = points_tag.find("ASYNCHRONOUS-SERVER-CALL-POINT")
        assert async_elem is not None
        assert async_elem.find("SHORT-NAME").text == "scp_async"
        assert async_elem.find("OPERATION-IREF/TARGET-REQUIRED-OPERATION-REF").text == "/MyComponents/IfCs/op2"
        assert async_elem.find("TIMEOUT") is None

    def test_write_empty_server_call_points(self, writer):
        entity = self._make_entity()

        parent = _parent()
        writer.writeRunnableEntityServerCallPoints(parent, entity)

        assert parent.find("SERVER-CALL-POINTS") is None


def _ref_stub(dest, value):
    from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import RefType

    ref = RefType()
    ref.setDest(dest)
    ref.setValue(value)
    return ref
