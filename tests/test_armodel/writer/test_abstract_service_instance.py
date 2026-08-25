"""Writer/reader round-trip tests for AbstractServiceInstance base attributes (Table 6.158, p.477)."""

import xml.etree.ElementTree as ET

import pytest

from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import ARLiteral, PositiveInteger, RefType, String
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.TagWithOptionalValue import TagWithOptionalValue
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Ethernet.ServiceInstances import ConsumedServiceInstance, PduActivationRoutingGroup, ProvidedServiceInstance
from armodel.parser.arxml_parser import ARXMLParser
from armodel.writer.arxml_writer import ARXMLWriter

NS = "http://autosar.org/schema/r4.0"


@pytest.fixture(autouse=True)
def reset_autosar():
    AUTOSAR.getInstance().new()
    yield
    AUTOSAR.getInstance().new()


@pytest.fixture
def writer():
    AUTOSAR.getInstance().new()
    document = AUTOSAR.getInstance()
    document.setARRelease("R23-11")
    return ARXMLWriter()


@pytest.fixture
def parser():
    AUTOSAR.getInstance().new()
    document = AUTOSAR.getInstance()
    document.setARRelease("R23-11")
    return ARXMLParser()


def _parent():
    return ET.Element("ROOT")


def _namespaced_wrap(element: ET.Element) -> ET.Element:
    inner = ET.tostring(element).decode("utf-8")
    root = ET.fromstring(f"<AUTOSAR xmlns='{NS}'>{inner}</AUTOSAR>")
    return root[0][0]


class MockParent(ARObject):
    def __init__(self):
        super().__init__()


def _ref(dest, value):
    ref = RefType()
    ref.setDest(dest)
    ref.setValue(value)
    return ref


def _pos_int(text):
    val = PositiveInteger()
    val.setValue(text)
    return val


def _tag(key, value):
    tag = TagWithOptionalValue()
    tag.setKey(_string(key))
    if value is not None:
        tag.setValue(_string(value))
    return tag


def _string(value):
    s = String()
    s.setValue(value)
    return s


def _full_consumed_instance():
    instance = ConsumedServiceInstance(MockParent(), "MyConsumedService")
    instance.addCapabilityRecord(_tag("service", "someip"))
    instance.addCapabilityRecord(_tag("passreq", None))
    instance.setMajorVersion(_pos_int("33"))
    instance.addRoutingGroupRef(_ref("SO-AD-ROUTING-GROUP", "/Ether/RoutingGroup/RG1"))
    instance.addRoutingGroupRef(_ref("SO-AD-ROUTING-GROUP", "/Ether/RoutingGroup/RG2"))
    return instance


def _full_provided_instance():
    instance = ProvidedServiceInstance(MockParent(), "MyProvidedService")
    instance.addCapabilityRecord(_tag("config", "v1"))
    instance.setMajorVersion(_pos_int("7"))
    instance.addRoutingGroupRef(_ref("SO-AD-ROUTING-GROUP", "/Ether/RoutingGroup/RG3"))
    return instance


class TestWriteAbstractServiceInstanceBaseAttrs:
    def test_write_all_fields(self, writer):
        parent = _parent()
        writer.writeConsumedServiceInstance(parent, _full_consumed_instance())

        el = parent.find("CONSUMED-SERVICE-INSTANCE")
        assert el is not None
        assert el.find("SHORT-NAME").text == "MyConsumedService"
        records = el.find("CAPABILITY-RECORDS")
        assert records is not None
        tags = records.findall("TAG-WITH-OPTIONAL-VALUE")
        assert len(tags) == 2
        assert tags[0].find("KEY").text == "service"
        assert tags[0].find("VALUE").text == "someip"
        assert tags[1].find("KEY").text == "passreq"
        assert tags[1].find("VALUE") is None
        assert el.find("MAJOR-VERSION").text == "33"
        refs = el.find("ROUTING-GROUP-REFS")
        assert refs is not None
        ref_els = refs.findall("ROUTING-GROUP-REF")
        assert [r.text for r in ref_els] == ["/Ether/RoutingGroup/RG1", "/Ether/RoutingGroup/RG2"]
        assert ref_els[0].get("DEST") == "SO-AD-ROUTING-GROUP"

    def test_write_empty_fields_omits_optional_tags(self, writer):
        parent = _parent()
        writer.writeConsumedServiceInstance(parent, ConsumedServiceInstance(MockParent(), "EmptyService"))

        el = parent.find("CONSUMED-SERVICE-INSTANCE")
        assert el is not None
        assert el.find("CAPABILITY-RECORDS") is None
        assert el.find("MAJOR-VERSION") is None
        assert el.find("ROUTING-GROUP-REFS") is None


class TestAbstractServiceInstanceRoundTrip:
    def test_round_trip_preserves_all_values(self, writer, parser, tmp_path):
        instance = _full_consumed_instance()

        parent = _parent()
        writer.writeConsumedServiceInstance(parent, instance)

        out_file = str(tmp_path / "abstract_service_instance.arxml")
        with open(out_file, "w", encoding="utf-8") as f:
            f.write(ET.tostring(_namespaced_wrap(parent), encoding="unicode"))

        recovered = ConsumedServiceInstance(MockParent(), "MyConsumedService")
        tree = ET.parse(out_file)
        parser.readConsumedServiceInstance(tree.getroot(), recovered)

        records = recovered.getCapabilityRecords()
        assert len(records) == 2
        assert records[0].getKey().getValue() == "service"
        assert records[0].getValue().getValue() == "someip"
        assert records[1].getKey().getValue() == "passreq"
        assert records[1].getValue() is None
        assert recovered.getMajorVersion().getValue() == 33
        refs = recovered.getRoutingGroupRefs()
        assert [r.getValue() for r in refs] == ["/Ether/RoutingGroup/RG1", "/Ether/RoutingGroup/RG2"]
        assert refs[0].getDest() == "SO-AD-ROUTING-GROUP"

    def test_reader_empty_fields(self, parser):
        element = ET.fromstring(f"<CONSUMED-SERVICE-INSTANCE xmlns='{NS}'><SHORT-NAME>EmptyService</SHORT-NAME></CONSUMED-SERVICE-INSTANCE>")

        recovered = ConsumedServiceInstance(MockParent(), "EmptyService")
        parser.readConsumedServiceInstance(element, recovered)

        assert recovered.getCapabilityRecords() == []
        assert recovered.getMajorVersion() is None
        assert recovered.getRoutingGroupRefs() == []

    def test_provided_service_instance_base_attrs_round_trip(self, writer, parser, tmp_path):
        instance = _full_provided_instance()

        parent = _parent()
        writer.writeProvidedServiceInstance(parent, instance)

        out_file = str(tmp_path / "provided_service_instance.arxml")
        with open(out_file, "w", encoding="utf-8") as f:
            f.write(ET.tostring(_namespaced_wrap(parent), encoding="unicode"))

        recovered = ProvidedServiceInstance(MockParent(), "MyProvidedService")
        tree = ET.parse(out_file)
        parser.readProvidedServiceInstance(tree.getroot(), recovered)

        records = recovered.getCapabilityRecords()
        assert len(records) == 1
        assert records[0].getKey().getValue() == "config"
        assert records[0].getValue().getValue() == "v1"
        assert recovered.getMajorVersion().getValue() == 7
        refs = recovered.getRoutingGroupRefs()
        assert [r.getValue() for r in refs] == ["/Ether/RoutingGroup/RG3"]


def _activation_group():
    group = PduActivationRoutingGroup(MockParent(), "MARG1")
    literal = ARLiteral()
    literal.setValue("deactivateAndTriggerUnicast")
    group.setEventGroupControlType(literal)
    ref = RefType()
    ref.setValue("/SoCon/IPduUdp9")
    group.addIPduIdentifierUdpRef(ref)
    return group


class TestMethodActivationRoutingGroupRoundTrip:
    def test_write_method_activation_routing_group_consumed_side(self, writer):
        parent = _parent()
        instance = ConsumedServiceInstance(MockParent(), "CSI")
        instance.setMethodActivationRoutingGroup(_activation_group())
        writer.writeConsumedServiceInstance(parent, instance)

        el = parent.find("CONSUMED-SERVICE-INSTANCE")
        wrapper = el.find("METHOD-ACTIVATION-ROUTING-GROUPS")
        assert wrapper is not None
        entry = wrapper.find("PDU-ACTIVATION-ROUTING-GROUP")
        assert entry is not None
        assert entry.find("SHORT-NAME").text == "MARG1"
        assert entry.find("EVENT-GROUP-CONTROL-TYPE").text == "deactivateAndTriggerUnicast"

    def test_round_trip_preserves_method_activation_routing_group(self, writer, parser, tmp_path):
        parent = _parent()
        instance = ConsumedServiceInstance(MockParent(), "CSI")
        instance.setMethodActivationRoutingGroup(_activation_group())
        writer.writeConsumedServiceInstance(parent, instance)

        element = _namespaced_wrap(parent)
        recovered = ConsumedServiceInstance(MockParent(), "CSI")
        parser.readConsumedServiceInstance(element, recovered)

        group = recovered.getMethodActivationRoutingGroup()
        assert isinstance(group, PduActivationRoutingGroup)
        assert group.getShortName() == "MARG1"
        assert group.getEventGroupControlType().getValue() == "deactivateAndTriggerUnicast"
        assert group.getIPduIdentifierUdpRefs()[0].getValue() == "/SoCon/IPduUdp9"

    def test_provided_side_method_activation_routing_group_round_trip(self, writer, parser, tmp_path):
        parent = _parent()
        instance = ProvidedServiceInstance(MockParent(), "PSI")
        instance.setMethodActivationRoutingGroup(_activation_group())
        writer.writeProvidedServiceInstance(parent, instance)

        element = _namespaced_wrap(parent)
        recovered = ProvidedServiceInstance(MockParent(), "PSI")
        parser.readProvidedServiceInstance(element, recovered)

        group = recovered.getMethodActivationRoutingGroup()
        assert isinstance(group, PduActivationRoutingGroup)
        assert group.getShortName() == "MARG1"

    def test_reader_no_wrapper_leaves_none(self, parser):
        element = ET.fromstring(f"<CONSUMED-SERVICE-INSTANCE xmlns='{NS}'><SHORT-NAME>CSI</SHORT-NAME></CONSUMED-SERVICE-INSTANCE>")
        recovered = ConsumedServiceInstance(MockParent(), "CSI")
        parser.readConsumedServiceInstance(element, recovered)
        assert recovered.getMethodActivationRoutingGroup() is None
