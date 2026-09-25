"""
Tests for reading AUTOSAR-PARAMETER-REF elements — AutosarParameterRef, Table 5.34 (p.317, R23-11).

AutosarParameterRef (Base = ARObject) carries two own attributes whose reader element set
follows the XSD group AUTOSAR-PARAMETER-REF (AUTOSAR_00052.xsd): AUTOSAR-PARAMETER-IREF
(type PARAMETER-IN-ATOMIC-SWC-TYPE-INSTANCE-REF) and LOCAL-PARAMETER-REF (each 0..1,
order-independent on read). The ARObject base attributes (S checksum, T timestamp) belong
to the element set via the XSD AR-OBJECT attributeGroup. The class is aggregated by
InstantiationDataDefProps.parameterInstance, ParameterAccess.accessedParameter,
RoleBasedDataAssignment.usedParameterElement and SwCalprmRefProxy.arParameter, and read
through getAutosarParameterRef at each call site.

Round-trip counterpart: tests/test_armodel/writer/test_autosar_parameter_ref.py
"""

import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import RefType
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.SwcInternalBehavior.DataElements import AutosarParameterRef, ParameterAccess
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.SwcInternalBehavior.DataElements.InstanceRefsUsage import ParameterInAtomicSWCTypeInstanceRef
from tests.test_armodel.parser._helpers import NS

PARAMETER_REF_CONTENT = (
    "<AUTOSAR-PARAMETER-IREF>"
    "<PORT-PROTOTYPE-REF DEST='PORT-PROTOTYPE'>/Swc/Port</PORT-PROTOTYPE-REF>"
    "<ROOT-PARAMETER-DATA-PROTOTYPE-REF DEST='PARAMETER-DATA-PROTOTYPE'>/Swc/RootParameter</ROOT-PARAMETER-DATA-PROTOTYPE-REF>"
    "<TARGET-DATA-PROTOTYPE-REF DEST='APPLICATION-COMPOSITE-ELEMENT-DATA-PROTOTYPE'>/Swc/TargetElement</TARGET-DATA-PROTOTYPE-REF>"
    "</AUTOSAR-PARAMETER-IREF>"
    "<LOCAL-PARAMETER-REF DEST='PARAMETER-DATA-PROTOTYPE'>/Swc/LocalParameter</LOCAL-PARAMETER-REF>"
)

PARAMETER_REF_XML = f"<ACCESSED-PARAMETER>{PARAMETER_REF_CONTENT}</ACCESSED-PARAMETER>"


def _wrap(inner: str) -> ET.Element:
    """Wrap the AUTOSAR-PARAMETER-REF fragment in a namespaced parent element."""
    return ET.fromstring(f"<ROOT xmlns='{NS}'>{inner}</ROOT>")


class TestGetAutosarParameterRef:
    """Tests for getAutosarParameterRef — own element field values (Table 5.34)."""

    def test_own_element_field_values(self, parser):
        """Test that both attribute elements are read with their field values."""
        element = _wrap(PARAMETER_REF_XML)

        parameter = parser.getAutosarParameterRef(element, "ACCESSED-PARAMETER")

        assert parameter is not None
        assert isinstance(parameter, AutosarParameterRef)
        iref = parameter.getAutosarParameterIRef()
        assert isinstance(iref, ParameterInAtomicSWCTypeInstanceRef)
        assert iref.getPortPrototypeRef().getValue() == "/Swc/Port"
        assert iref.getPortPrototypeRef().getDest() == "PORT-PROTOTYPE"
        assert iref.getRootParameterDataPrototypeRef().getValue() == "/Swc/RootParameter"
        assert iref.getTargetDataPrototypeRef().getValue() == "/Swc/TargetElement"
        local_ref = parameter.getLocalParameterRef()
        assert isinstance(local_ref, RefType)
        assert local_ref.getValue() == "/Swc/LocalParameter"
        assert local_ref.getDest() == "PARAMETER-DATA-PROTOTYPE"

    def test_empty_element(self, parser):
        """Test that an empty element yields an instance with all fields unset."""
        element = _wrap("<ACCESSED-PARAMETER></ACCESSED-PARAMETER>")

        parameter = parser.getAutosarParameterRef(element, "ACCESSED-PARAMETER")

        assert parameter is not None
        assert parameter.getAutosarParameterIRef() is None
        assert parameter.getLocalParameterRef() is None

    def test_absent_autosar_parameter_iref(self, parser):
        """Test that an absent AUTOSAR-PARAMETER-IREF element leaves the iref unset while the local reference is read."""
        element = _wrap("<ACCESSED-PARAMETER><LOCAL-PARAMETER-REF DEST='PARAMETER-DATA-PROTOTYPE'>/Swc/LocalParameter</LOCAL-PARAMETER-REF></ACCESSED-PARAMETER>")

        parameter = parser.getAutosarParameterRef(element, "ACCESSED-PARAMETER")

        assert parameter.getAutosarParameterIRef() is None
        assert parameter.getLocalParameterRef().getValue() == "/Swc/LocalParameter"

    def test_absent_local_parameter_ref(self, parser):
        """Test that an absent LOCAL-PARAMETER-REF element leaves the reference unset while the iref is read."""
        element = _wrap("<ACCESSED-PARAMETER><AUTOSAR-PARAMETER-IREF><PORT-PROTOTYPE-REF DEST='PORT-PROTOTYPE'>/Swc/Port</PORT-PROTOTYPE-REF></AUTOSAR-PARAMETER-IREF></ACCESSED-PARAMETER>")

        parameter = parser.getAutosarParameterRef(element, "ACCESSED-PARAMETER")

        assert parameter.getAutosarParameterIRef().getPortPrototypeRef().getValue() == "/Swc/Port"
        assert parameter.getLocalParameterRef() is None

    def test_absent_element_returns_none(self, parser):
        """Test that an absent AUTOSAR-PARAMETER-REF element yields None."""
        element = _wrap("<OTHER></OTHER>")

        assert parser.getAutosarParameterRef(element, "ACCESSED-PARAMETER") is None

    def test_ar_object_attributes_read(self, parser):
        """Test that the ARObject base attributes (S checksum, T timestamp) are read."""
        element = ET.fromstring(f"<ROOT xmlns='{NS}'><ACCESSED-PARAMETER S='abc123' T='2024-01-01T12:00:00+00:00'></ACCESSED-PARAMETER></ROOT>")

        parameter = parser.getAutosarParameterRef(element, "ACCESSED-PARAMETER")

        assert parameter is not None
        assert parameter.getChecksum() is not None
        assert parameter.getChecksum().getValue() == "abc123"
        assert parameter.getTimestamp() is not None


class TestReadAutosarParameterRefDispatch:
    """Tests for the ParameterAccess.accessedParameter dispatch."""

    def test_dispatch_via_parameter_access(self, parser):
        """Test that readParameterAccess reads the accessed parameter with field values."""
        root = AUTOSAR.getInstance().createARPackage("Pkg")
        access = ParameterAccess(root, "Pa1")
        element = ET.fromstring(f"<ROOT xmlns='{NS}'><PARAMETER-ACCESS><SHORT-NAME>Pa1</SHORT-NAME><ACCESSED-PARAMETER>{PARAMETER_REF_CONTENT}</ACCESSED-PARAMETER></PARAMETER-ACCESS></ROOT>")

        parser.readParameterAccess(element[0], access)

        parameter = access.getAccessedParameter()
        assert isinstance(parameter, AutosarParameterRef)
        assert parameter.getAutosarParameterIRef().getPortPrototypeRef().getValue() == "/Swc/Port"
        assert parameter.getLocalParameterRef().getValue() == "/Swc/LocalParameter"

    def test_dispatch_absent_accessed_parameter(self, parser):
        """Test that a parameter access without ACCESSED-PARAMETER leaves the reference unset."""
        root = AUTOSAR.getInstance().createARPackage("Pkg")
        access = ParameterAccess(root, "Pa1")
        element = ET.fromstring(f"<ROOT xmlns='{NS}'><PARAMETER-ACCESS><SHORT-NAME>Pa1</SHORT-NAME></PARAMETER-ACCESS></ROOT>")

        parser.readParameterAccess(element[0], access)

        assert access.getAccessedParameter() is None
