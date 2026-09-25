"""
Tests for reading AUTOSAR-VARIABLE-REF elements — AutosarVariableRef, Table 5.33 (p.316, R23-11).

AutosarVariableRef (Base = ARObject) carries three own attributes whose reader element
set follows the XSD group AUTOSAR-VARIABLE-REF (AUTOSAR_00052.xsd): AUTOSAR-VARIABLE-IN-IMPL-DATATYPE,
AUTOSAR-VARIABLE-IREF, LOCAL-VARIABLE-REF (each 0..1, order-independent on read). It is
aggregated by VariableAccess.accessedVariable (among others) and read through
readVariableAccess → getAutosarVariableRef.

Round-trip counterpart: tests/test_armodel/writer/test_autosar_variable_ref.py
"""

import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import RefType
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.SwcInternalBehavior.DataElements import (
    ArVariableInImplementationDataInstanceRef,
    AutosarVariableRef,
    VariableAccess,
)
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.SwcInternalBehavior.DataElements.InstanceRefsUsage import (
    VariableInAtomicSWCTypeInstanceRef,
)
from tests.test_armodel.parser._helpers import NS, _snip

IMPL_DATATYPE_XML = (
    "<AUTOSAR-VARIABLE-IN-IMPL-DATATYPE>"
    "<PORT-PROTOTYPE-REF DEST='PORT-PROTOTYPE'>/ImplPort</PORT-PROTOTYPE-REF>"
    "<ROOT-VARIABLE-DATA-PROTOTYPE-REF DEST='VARIABLE-DATA-PROTOTYPE'>/RootVariable</ROOT-VARIABLE-DATA-PROTOTYPE-REF>"
    "<CONTEXT-DATA-PROTOTYPE-REF DEST='IMPLEMENTATION-DATA-TYPE-ELEMENT'>/Ctx1</CONTEXT-DATA-PROTOTYPE-REF>"
    "<CONTEXT-DATA-PROTOTYPE-REF DEST='IMPLEMENTATION-DATA-TYPE-ELEMENT'>/Ctx2</CONTEXT-DATA-PROTOTYPE-REF>"
    "<TARGET-DATA-PROTOTYPE-REF DEST='IMPLEMENTATION-DATA-TYPE-ELEMENT'>/ImplTarget</TARGET-DATA-PROTOTYPE-REF>"
    "</AUTOSAR-VARIABLE-IN-IMPL-DATATYPE>"
)

IREF_XML = (
    "<AUTOSAR-VARIABLE-IREF>"
    "<PORT-PROTOTYPE-REF DEST='PORT-PROTOTYPE'>/VarPort</PORT-PROTOTYPE-REF>"
    "<TARGET-DATA-PROTOTYPE-REF DEST='VARIABLE-DATA-PROTOTYPE'>/VarTarget</TARGET-DATA-PROTOTYPE-REF>"
    "</AUTOSAR-VARIABLE-IREF>"
)

LOCAL_VARIABLE_XML = "<LOCAL-VARIABLE-REF DEST='VARIABLE-DATA-PROTOTYPE'>/LocalVariable</LOCAL-VARIABLE-REF>"


def _wrap(inner: str) -> ET.Element:
    """Wrap the AUTOSAR-VARIABLE-REF fragment in a namespaced parent element."""
    return ET.fromstring(f"<ROOT xmlns='{NS}'>{inner}</ROOT>")


class TestGetAutosarVariableRef:
    """Tests for getAutosarVariableRef — own element field values (Table 5.33)."""

    def test_own_element_field_values(self, parser):
        """Test that all three attribute elements are read with their field values."""
        element = _wrap("<AUTOSAR-VARIABLE-REF>" + IMPL_DATATYPE_XML + IREF_XML + LOCAL_VARIABLE_XML + "</AUTOSAR-VARIABLE-REF>")

        ref = parser.getAutosarVariableRef(element, "AUTOSAR-VARIABLE-REF")

        assert ref is not None
        assert isinstance(ref, AutosarVariableRef)
        impl = ref.getAutosarVariableInImplDatatype()
        assert isinstance(impl, ArVariableInImplementationDataInstanceRef)
        assert impl.getPortPrototypeRef().getValue() == "/ImplPort"
        assert impl.getRootVariableDataPrototypeRef().getValue() == "/RootVariable"
        contexts = impl.getContextDataPrototypeRefs()
        assert [ctx.getValue() for ctx in contexts] == ["/Ctx1", "/Ctx2"]
        assert impl.getTargetDataPrototypeRef().getValue() == "/ImplTarget"
        iref = ref.getAutosarVariableIRef()
        assert isinstance(iref, VariableInAtomicSWCTypeInstanceRef)
        assert iref.getPortPrototypeRef().getValue() == "/VarPort"
        assert iref.getTargetDataPrototypeRef().getValue() == "/VarTarget"
        local = ref.getLocalVariableRef()
        assert isinstance(local, RefType)
        assert local.getValue() == "/LocalVariable"
        assert local.getDest() == "VARIABLE-DATA-PROTOTYPE"

    def test_empty_element(self, parser):
        """Test that an empty element yields an instance with all fields unset."""
        element = _wrap("<AUTOSAR-VARIABLE-REF></AUTOSAR-VARIABLE-REF>")

        ref = parser.getAutosarVariableRef(element, "AUTOSAR-VARIABLE-REF")

        assert ref is not None
        assert ref.getAutosarVariableInImplDatatype() is None
        assert ref.getAutosarVariableIRef() is None
        assert ref.getLocalVariableRef() is None

    def test_absent_iref_element(self, parser):
        """Test that an absent AUTOSAR-VARIABLE-IREF element leaves the iref unset while the others are read."""
        element = _wrap("<AUTOSAR-VARIABLE-REF>" + IMPL_DATATYPE_XML + LOCAL_VARIABLE_XML + "</AUTOSAR-VARIABLE-REF>")

        ref = parser.getAutosarVariableRef(element, "AUTOSAR-VARIABLE-REF")

        assert ref.getAutosarVariableIRef() is None
        assert ref.getAutosarVariableInImplDatatype().getTargetDataPrototypeRef().getValue() == "/ImplTarget"
        assert ref.getLocalVariableRef().getValue() == "/LocalVariable"

    def test_absent_local_variable_ref(self, parser):
        """Test that an absent LOCAL-VARIABLE-REF element leaves the reference unset while the iref is read."""
        element = _wrap("<AUTOSAR-VARIABLE-REF>" + IREF_XML + "</AUTOSAR-VARIABLE-REF>")

        ref = parser.getAutosarVariableRef(element, "AUTOSAR-VARIABLE-REF")

        assert ref.getLocalVariableRef() is None
        assert ref.getAutosarVariableIRef().getTargetDataPrototypeRef().getValue() == "/VarTarget"
        assert ref.getAutosarVariableInImplDatatype() is None

    def test_ar_object_attributes_read(self, parser):
        """Test that the ARObject base attributes (S checksum, T timestamp) are read."""
        element = ET.fromstring(f"<ROOT xmlns='{NS}'><AUTOSAR-VARIABLE-REF S='abc123' T='2024-01-01T12:00:00+00:00'></AUTOSAR-VARIABLE-REF></ROOT>")

        ref = parser.getAutosarVariableRef(element, "AUTOSAR-VARIABLE-REF")

        assert ref is not None
        assert ref.getChecksum() is not None
        assert ref.getChecksum().getValue() == "abc123"
        assert ref.getTimestamp() is not None


class TestReadVariableAccessDispatch:
    """Tests for the VariableAccess.accessedVariable aggregation dispatch."""

    def test_dispatch_via_read_variable_access(self, parser):
        """Test that readVariableAccess reads the accessed variable reference with field values."""
        root = AUTOSAR.getInstance().createARPackage("Pkg")
        access = VariableAccess(root, "VarAccess")
        element = _snip(
            "<SHORT-NAME>VarAccess</SHORT-NAME>" "<ACCESSED-VARIABLE>" + IREF_XML + LOCAL_VARIABLE_XML + "</ACCESSED-VARIABLE>",
            root_tag="VARIABLE-ACCESS",
        )

        parser.readVariableAccess(element, access)

        ref = access.getAccessedVariable()
        assert isinstance(ref, AutosarVariableRef)
        assert ref.getAutosarVariableIRef().getTargetDataPrototypeRef().getValue() == "/VarTarget"
        assert ref.getLocalVariableRef().getValue() == "/LocalVariable"

    def test_dispatch_absent_accessed_variable(self, parser):
        """Test that a VariableAccess without ACCESSED-VARIABLE leaves the reference unset."""
        root = AUTOSAR.getInstance().createARPackage("Pkg")
        access = VariableAccess(root, "VarAccess")
        element = _snip("<SHORT-NAME>VarAccess</SHORT-NAME>", root_tag="VARIABLE-ACCESS")

        parser.readVariableAccess(element, access)

        assert access.getAccessedVariable() is None
