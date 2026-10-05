import xml.etree.ElementTree as ET

import pytest

from armodel.models import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import Boolean, DateTime, Identifier, RefType, String
from armodel.models.M2.AUTOSARTemplates.GenericStructure.VariantHandling import VariationPoint
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.NetworkManagement import CanNmClusterCoupling
from armodel.parser.arxml_parser import ARXMLParser
from armodel.writer.arxml_writer import ARXMLWriter

NS = "http://autosar.org/schema/r4.0"


@pytest.fixture(autouse=True)
def reset_autosar():
    AUTOSAR.getInstance().new()
    yield
    AUTOSAR.getInstance().new()


class MockParent(ARObject):
    def __init__(self):
        super().__init__()


def _bool(value):
    boolean = Boolean()
    boolean.setValue(value)
    return boolean


def _ref(dest, value):
    ref = RefType()
    ref.setDest(dest)
    ref.setValue(value)
    return ref


def _vp(label):
    vp = VariationPoint()
    vp.setShortLabel(Identifier().setValue(label))
    return vp


def _new_coupling():
    coupling = CanNmClusterCoupling()
    coupling.addCoupledClusterRef(_ref("CAN-CLUSTER", "/Clusters/Can1"))
    coupling.setNmBusloadReductionEnabled(_bool(True))
    coupling.setNmImmediateRestartEnabled(_bool(False))
    return coupling


class TestWriteCanNmClusterCoupling:
    def test_write_can_nm_cluster_coupling_element_order(self):
        parent = ET.Element("PARENT")
        ARXMLWriter().writeCanNmClusterCoupling(parent, _new_coupling())
        coupling_element = parent.find("CAN-NM-CLUSTER-COUPLING")
        tags = [child.tag for child in coupling_element]
        assert tags == ["COUPLED-CLUSTER-REFS", "NM-BUSLOAD-REDUCTION-ENABLED", "NM-IMMEDIATE-RESTART-ENABLED"]

    def test_write_can_nm_cluster_coupling_round_trip_field_values(self):
        parent = ET.Element("PARENT")
        ARXMLWriter().writeCanNmClusterCoupling(parent, _new_coupling())
        wrapper = ET.Element("WRAPPER")
        wrapper.append(parent.find("CAN-NM-CLUSTER-COUPLING"))
        wrapper.set("xmlns", NS)
        coupling_element = ET.fromstring(ET.tostring(wrapper, encoding="unicode"))[0]
        parsed = CanNmClusterCoupling()
        ARXMLParser().readCanNmClusterCoupling(coupling_element, parsed)
        refs = parsed.getCoupledClusterRefs()
        assert [ref.getValue() for ref in refs] == ["/Clusters/Can1"]
        assert refs[0].getDest() == "CAN-CLUSTER"
        assert parsed.getNmBusloadReductionEnabled().getValue() is True
        assert parsed.getNmImmediateRestartEnabled().getValue() is False

    def test_write_can_nm_cluster_coupling_writes_checksum_and_timestamp(self):
        coupling = _new_coupling()
        coupling.setChecksum(String().setValue("1234"))
        coupling.setTimestamp(DateTime().setValue("2024-01-01T00:00:00Z"))
        parent = ET.Element("PARENT")
        ARXMLWriter().writeCanNmClusterCoupling(parent, coupling)
        coupling_element = parent.find("CAN-NM-CLUSTER-COUPLING")
        assert coupling_element.attrib["S"] == "1234"
        assert coupling_element.attrib["T"] == "2024-01-01T00:00:00Z"

    def test_write_can_nm_cluster_coupling_writes_variation_point_last(self):
        coupling = _new_coupling()
        coupling.setVariationPoint(_vp("VP1"))
        parent = ET.Element("PARENT")
        ARXMLWriter().writeCanNmClusterCoupling(parent, coupling)
        coupling_element = parent.find("CAN-NM-CLUSTER-COUPLING")
        assert [child.tag for child in coupling_element] == ["COUPLED-CLUSTER-REFS", "NM-BUSLOAD-REDUCTION-ENABLED", "NM-IMMEDIATE-RESTART-ENABLED", "VARIATION-POINT"]
        assert coupling_element.find("VARIATION-POINT/SHORT-LABEL").text == "VP1"

    def test_write_can_nm_cluster_coupling_round_trips_variation_point(self):
        coupling = _new_coupling()
        coupling.setVariationPoint(_vp("VP1"))
        parent = ET.Element("PARENT")
        ARXMLWriter().writeCanNmClusterCoupling(parent, coupling)
        wrapper = ET.Element("WRAPPER")
        wrapper.append(parent.find("CAN-NM-CLUSTER-COUPLING"))
        wrapper.set("xmlns", NS)
        coupling_element = ET.fromstring(ET.tostring(wrapper, encoding="unicode"))[0]
        parsed = CanNmClusterCoupling()
        ARXMLParser().readCanNmClusterCoupling(coupling_element, parsed)
        assert parsed.getVariationPoint() is not None
        assert parsed.getVariationPoint().getShortLabel().getValue() == "VP1"
