import xml.etree.ElementTree as ET

import pytest

from armodel.models import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import DateTime, RefType, String
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.NetworkManagement import FlexrayNmClusterCoupling, FlexrayNmScheduleVariant, NmConfig
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


def _ref(dest, value):
    ref = RefType()
    ref.setDest(dest)
    ref.setValue(value)
    return ref


def _schedule_variant(member):
    variant = FlexrayNmScheduleVariant()
    variant.setValue(member)
    return variant


def _new_config():
    config = NmConfig(MockParent(), "NmConfig")
    coupling = FlexrayNmClusterCoupling()
    coupling.addCoupledClusterRef(_ref("FLEXRAY-CLUSTER", "/Clusters/Fr1"))
    coupling.setNmScheduleVariant(_schedule_variant(FlexrayNmScheduleVariant.SCHEDULE_VARIANT_2))
    config.addNmClusterCouplings(coupling)
    return config


class TestWriteFlexrayNmClusterCoupling:
    def test_write_flexray_nm_cluster_coupling_element_order(self):
        parent = ET.Element("PARENT")
        ARXMLWriter().writeNmConfigNmClusterCouplings(parent, _new_config())
        couplings_wrapper = parent.find("NM-CLUSTER-COUPLINGS")
        coupling_element = couplings_wrapper.find("FLEXRAY-NM-CLUSTER-COUPLING")
        assert coupling_element is not None
        tags = [child.tag for child in coupling_element]
        assert tags == ["COUPLED-CLUSTER-REFS", "NM-SCHEDULE-VARIANT"]

    def test_write_flexray_nm_cluster_coupling_round_trip_field_values(self):
        parent = ET.Element("PARENT")
        ARXMLWriter().writeNmConfigNmClusterCouplings(parent, _new_config())
        parent.set("xmlns", NS)
        root = ET.fromstring(ET.tostring(parent, encoding="unicode"))
        config = NmConfig(MockParent(), "NmConfig")
        ARXMLParser().readNmConfigNmClusterCouplings(root, config)
        couplings = config.getNmClusterCouplings()
        assert len(couplings) == 1
        coupling = couplings[0]
        assert isinstance(coupling, FlexrayNmClusterCoupling)
        refs = coupling.getCoupledClusterRefs()
        assert [ref.getValue() for ref in refs] == ["/Clusters/Fr1"]
        assert refs[0].getDest() == "FLEXRAY-CLUSTER"
        assert coupling.getNmScheduleVariant().getValue() == "scheduleVariant2"

    def test_write_flexray_nm_cluster_coupling_writes_checksum_and_timestamp(self):
        config = _new_config()
        coupling = config.getNmClusterCouplings()[0]
        coupling.setChecksum(String().setValue("9012"))
        coupling.setTimestamp(DateTime().setValue("2024-01-01T00:00:00Z"))
        parent = ET.Element("PARENT")
        ARXMLWriter().writeNmConfigNmClusterCouplings(parent, config)
        coupling_element = parent.find("NM-CLUSTER-COUPLINGS").find("FLEXRAY-NM-CLUSTER-COUPLING")
        assert coupling_element.attrib["S"] == "9012"
        assert coupling_element.attrib["T"] == "2024-01-01T00:00:00Z"
