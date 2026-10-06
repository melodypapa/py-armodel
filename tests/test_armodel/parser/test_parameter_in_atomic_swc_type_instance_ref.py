"""
Tests for reading AUTOSAR-PARAMETER-IREF elements — ParameterInAtomicSWCTypeInstanceRef, Table 5.36 (p.319, R23-11).

ParameterInAtomicSWCTypeInstanceRef (Base = ARObject, AtpInstanceRef) carries five own
attributes whose reader element set follows the XSD group PARAMETER-IN-ATOMIC-SWC-TYPE-INSTANCE-REF
(AUTOSAR_00052.xsd): PORT-PROTOTYPE-REF, ROOT-PARAMETER-DATA-PROTOTYPE-REF,
CONTEXT-DATA-PROTOTYPE-REF (0..*, ordered) and TARGET-DATA-PROTOTYPE-REF (each 0..1,
order-independent on read). The `base` attribute is atpDerived — the XSD skips it
("Association <<atpDerived>>base skipped"), so it has no XML element. The class is
aggregated by AutosarParameterRef.autosarParameter and read through
getParameterInAtomicSWCTypeInstanceRef at that call site.

Round-trip counterpart: tests/test_armodel/writer/test_parameter_in_atomic_swc_type_instance_ref.py
"""

import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.GenericStructure.AbstractStructure import AtpInstanceRef
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.SwcInternalBehavior.DataElements import AutosarParameterRef, ParameterAccess
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.SwcInternalBehavior.DataElements.InstanceRefsUsage import ParameterInAtomicSWCTypeInstanceRef
from tests.test_armodel.parser._helpers import NS

IREFS_CONTENT = (
    "<AUTOSAR-PARAMETER-IREF>"
    "<PORT-PROTOTYPE-REF DEST='PORT-PROTOTYPE'>/Swc/Port</PORT-PROTOTYPE-REF>"
    "<ROOT-PARAMETER-DATA-PROTOTYPE-REF DEST='PARAMETER-DATA-PROTOTYPE'>/Swc/RootParameter</ROOT-PARAMETER-DATA-PROTOTYPE-REF>"
    "<CONTEXT-DATA-PROTOTYPE-REF DEST='APPLICATION-COMPOSITE-ELEMENT-DATA-PROTOTYPE'>/Swc/ContextFirst</CONTEXT-DATA-PROTOTYPE-REF>"
    "<CONTEXT-DATA-PROTOTYPE-REF DEST='APPLICATION-COMPOSITE-ELEMENT-DATA-PROTOTYPE'>/Swc/ContextSecond</CONTEXT-DATA-PROTOTYPE-REF>"
    "<TARGET-DATA-PROTOTYPE-REF DEST='PARAMETER-DATA-PROTOTYPE'>/Swc/TargetElement</TARGET-DATA-PROTOTYPE-REF>"
    "</AUTOSAR-PARAMETER-IREF>"
)


def _wrap(inner: str) -> ET.Element:
    """Wrap the iref fragment in a namespaced parent element."""
    return ET.fromstring(f"<ROOT xmlns='{NS}'>{inner}</ROOT>")


class TestGetParameterInAtomicSWCTypeInstanceRef:
    """Tests for getParameterInAtomicSWCTypeInstanceRef — own element field values (Table 5.36)."""

    def test_own_element_field_values(self, parser):
        """Test that all four ref attributes are read with their field values."""
        element = _wrap(IREFS_CONTENT)

        iref = parser.getParameterInAtomicSWCTypeInstanceRef(element, "AUTOSAR-PARAMETER-IREF")

        assert isinstance(iref, ParameterInAtomicSWCTypeInstanceRef)
        assert isinstance(iref, AtpInstanceRef)
        assert iref.getPortPrototypeRef().getValue() == "/Swc/Port"
        assert iref.getPortPrototypeRef().getDest() == "PORT-PROTOTYPE"
        assert iref.getRootParameterDataPrototypeRef().getValue() == "/Swc/RootParameter"
        assert iref.getRootParameterDataPrototypeRef().getDest() == "PARAMETER-DATA-PROTOTYPE"
        context_refs = iref.getContextDataPrototypeRefs()
        assert [ref.getValue() for ref in context_refs] == ["/Swc/ContextFirst", "/Swc/ContextSecond"]
        assert all(ref.getDest() == "APPLICATION-COMPOSITE-ELEMENT-DATA-PROTOTYPE" for ref in context_refs)
        assert iref.getTargetDataPrototypeRef().getValue() == "/Swc/TargetElement"
        assert iref.getTargetDataPrototypeRef().getDest() == "PARAMETER-DATA-PROTOTYPE"

    def test_empty_wrapper(self, parser):
        """Test that an empty AUTOSAR-PARAMETER-IREF wrapper yields an instance with all fields unset."""
        element = _wrap("<AUTOSAR-PARAMETER-IREF></AUTOSAR-PARAMETER-IREF>")

        iref = parser.getParameterInAtomicSWCTypeInstanceRef(element, "AUTOSAR-PARAMETER-IREF")

        assert isinstance(iref, ParameterInAtomicSWCTypeInstanceRef)
        assert iref.getBaseRef() is None
        assert iref.getContextDataPrototypeRefs() == []
        assert iref.getPortPrototypeRef() is None
        assert iref.getRootParameterDataPrototypeRef() is None
        assert iref.getTargetDataPrototypeRef() is None

    def test_absent_wrapper_returns_none(self, parser):
        """Test that an absent AUTOSAR-PARAMETER-IREF element yields None."""
        element = _wrap("<OTHER></OTHER>")

        assert parser.getParameterInAtomicSWCTypeInstanceRef(element, "AUTOSAR-PARAMETER-IREF") is None

    def test_atp_derived_base_has_no_xml_element(self, parser):
        """Test that no BASE-REF element is expected or read (atpDerived)."""
        element = _wrap("<AUTOSAR-PARAMETER-IREF><BASE-REF DEST='ATOMIC-SWC-TYPE'>/Swc</BASE-REF></AUTOSAR-PARAMETER-IREF>")

        iref = parser.getParameterInAtomicSWCTypeInstanceRef(element, "AUTOSAR-PARAMETER-IREF")

        assert isinstance(iref, ParameterInAtomicSWCTypeInstanceRef)
        assert iref.getBaseRef() is None
        assert iref.getPortPrototypeRef() is None


class TestParameterInAtomicSWCTypeInstanceRefDispatch:
    """Tests for the AutosarParameterRef.autosarParameter aggregation dispatch."""

    def test_dispatch_via_autosar_parameter_ref(self, parser):
        """Test that getAutosarParameterRef reads the iref with field values."""
        root = AUTOSAR.getInstance().createARPackage("Pkg")
        access = ParameterAccess(root, "Pa1")
        element = ET.fromstring(f"<ROOT xmlns='{NS}'><PARAMETER-ACCESS><SHORT-NAME>Pa1</SHORT-NAME><ACCESSED-PARAMETER>{IREFS_CONTENT}</ACCESSED-PARAMETER></PARAMETER-ACCESS></ROOT>")

        parser.readParameterAccess(element[0], access)

        parameter = access.getAccessedParameter()
        assert isinstance(parameter, AutosarParameterRef)
        iref = parameter.getAutosarParameterIRef()
        assert isinstance(iref, ParameterInAtomicSWCTypeInstanceRef)
        assert iref.getPortPrototypeRef().getValue() == "/Swc/Port"
        assert [ref.getValue() for ref in iref.getContextDataPrototypeRefs()] == ["/Swc/ContextFirst", "/Swc/ContextSecond"]
        assert iref.getTargetDataPrototypeRef().getValue() == "/Swc/TargetElement"

    def test_dispatch_absent_accessed_parameter(self, parser):
        """Test that a parameter access without ACCESSED-PARAMETER leaves the reference unset."""
        root = AUTOSAR.getInstance().createARPackage("Pkg")
        access = ParameterAccess(root, "Pa1")
        element = ET.fromstring(f"<ROOT xmlns='{NS}'><PARAMETER-ACCESS><SHORT-NAME>Pa1</SHORT-NAME></PARAMETER-ACCESS></ROOT>")

        parser.readParameterAccess(element[0], access)

        assert access.getAccessedParameter() is None
