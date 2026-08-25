"""Writer/reader round-trip tests for ConsumedServiceInstance (Table 6.167, p.501)."""

import xml.etree.ElementTree as ET

import pytest

from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import ARLiteral, Boolean, PositiveInteger, RefType, String
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Ethernet.EthernetTopology import SdClientConfig
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Ethernet.ServiceInstances import ConsumedServiceInstance, SomeipServiceVersion
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


def _bool(value):
    b = Boolean()
    b.setValue(value)
    return b


def _string(value):
    s = String()
    s.setValue(value)
    return s


def _version(major, minor):
    version = SomeipServiceVersion()
    version.setMajorVersion(_pos_int(major))
    version.setMinorVersion(_pos_int(minor))
    return version


def _full_instance():
    instance = ConsumedServiceInstance(MockParent(), "MyConsumedService")
    instance.addAllowedServiceProviderRef(_ref("NETWORK-ENDPOINT", "/Ether/NetworkEndpoint/NE1"))
    instance.setAutoRequire(_bool("true"))
    instance.addBlocklistedVersion(_version("1", "0"))
    instance.addBlocklistedVersion(_version("2", "5"))
    group = instance.createConsumedEventGroup("CEG1")
    group.setEventGroupIdentifier(_pos_int("7"))
    instance.setEventMulticastSubscriptionAddressRef(_ref("APPLICATION-ENDPOINT", "/Ether/ApplicationEndpoint/MC1"))
    instance.setInstanceIdentifier(_string("123"))
    instance.addLocalUnicastAddressRef(_ref("APPLICATION-ENDPOINT", "/Ether/ApplicationEndpoint/LU1"))
    instance.addLocalUnicastAddressRef(_ref("APPLICATION-ENDPOINT", "/Ether/ApplicationEndpoint/LU2"))
    instance.setMinorVersion(_string("ANY"))
    instance.setProvidedServiceInstanceRef(_ref("PROVIDED-SERVICE-INSTANCE", "/Ether/Provider/PSI1"))
    instance.addRemoteUnicastAddressRef(_ref("APPLICATION-ENDPOINT", "/Ether/ApplicationEndpoint/RU1"))
    config = SdClientConfig()
    config.setClientServiceMajorVersion(_pos_int("15"))
    config.setTtl(_pos_int("10"))
    instance.setSdClientConfig(config)
    instance.setSdClientTimerConfigRef(_ref("SOMEIP-SD-CLIENT-SERVICE-INSTANCE-CONFIG", "/SomeipSdTimingConfigs/InstanceTiming1"))
    instance.setServiceIdentifier(_pos_int("50"))
    behavior = ARLiteral()
    behavior.setValue("minimumMinorVersion")
    instance.setVersionDrivenFindBehavior(behavior)
    return instance


class TestWriteConsumedServiceInstance:
    def test_write_all_fields(self, writer):
        parent = _parent()
        writer.writeConsumedServiceInstance(parent, _full_instance())

        el = parent.find("CONSUMED-SERVICE-INSTANCE")
        assert el is not None
        assert el.find("SHORT-NAME").text == "MyConsumedService"
        asp = el.find("ALLOWED-SERVICE-PROVIDERS")
        assert asp is not None
        assert asp.find("NETWORK-ENDPOINT-REF-CONDITIONAL/NETWORK-ENDPOINT-REF").text == "/Ether/NetworkEndpoint/NE1"
        assert el.find("AUTO-REQUIRE").text == "true"
        blv = el.find("BLOCKLISTED-VERSIONS")
        assert blv is not None
        versions = blv.findall("SOMEIP-SERVICE-VERSION")
        assert len(versions) == 2
        assert versions[0].find("MAJOR-VERSION").text == "1"
        assert versions[0].find("MINOR-VERSION").text == "0"
        assert versions[1].find("MAJOR-VERSION").text == "2"
        assert versions[1].find("MINOR-VERSION").text == "5"
        cegs = el.find("CONSUMED-EVENT-GROUPS")
        assert cegs is not None
        assert cegs.find("CONSUMED-EVENT-GROUP/SHORT-NAME").text == "CEG1"
        assert cegs.find("CONSUMED-EVENT-GROUP/EVENT-GROUP-IDENTIFIER").text == "7"
        emsa = el.find("EVENT-MULTICAST-SUBSCRIPTION-ADDRESSS")
        assert emsa is not None
        assert emsa.find("APPLICATION-ENDPOINT-REF-CONDITIONAL/APPLICATION-ENDPOINT-REF").text == "/Ether/ApplicationEndpoint/MC1"
        assert el.find("INSTANCE-IDENTIFIER").text == "123"
        lua = el.find("LOCAL-UNICAST-ADDRESSS")
        assert lua is not None
        lua_refs = lua.findall("APPLICATION-ENDPOINT-REF-CONDITIONAL/APPLICATION-ENDPOINT-REF")
        assert [r.text for r in lua_refs] == ["/Ether/ApplicationEndpoint/LU1", "/Ether/ApplicationEndpoint/LU2"]
        assert el.find("MINOR-VERSION").text == "ANY"
        assert el.find("PROVIDED-SERVICE-INSTANCE-REF").text == "/Ether/Provider/PSI1"
        rua = el.find("REMOTE-UNICAST-ADDRESSS")
        assert rua is not None
        assert rua.find("APPLICATION-ENDPOINT-REF-CONDITIONAL/APPLICATION-ENDPOINT-REF").text == "/Ether/ApplicationEndpoint/RU1"
        sdc = el.find("SD-CLIENT-CONFIG")
        assert sdc is not None
        assert sdc.find("CLIENT-SERVICE-MAJOR-VERSION").text == "15"
        assert sdc.find("TTL").text == "10"
        sdtc = el.find("SD-CLIENT-TIMER-CONFIGS")
        assert sdtc is not None
        assert sdtc.find("SOMEIP-SD-CLIENT-SERVICE-INSTANCE-CONFIG-REF-CONDITIONAL/SOMEIP-SD-CLIENT-SERVICE-INSTANCE-CONFIG-REF").text == "/SomeipSdTimingConfigs/InstanceTiming1"
        assert el.find("SERVICE-IDENTIFIER").text == "50"
        assert el.find("VERSION-DRIVEN-FIND-BEHAVIOR").text == "minimumMinorVersion"

    def test_write_empty_fields_omits_optional_tags(self, writer):
        parent = _parent()
        writer.writeConsumedServiceInstance(parent, ConsumedServiceInstance(MockParent(), "EmptyService"))

        el = parent.find("CONSUMED-SERVICE-INSTANCE")
        assert el is not None
        assert el.find("ALLOWED-SERVICE-PROVIDERS") is None
        assert el.find("AUTO-REQUIRE") is None
        assert el.find("BLOCKLISTED-VERSIONS") is None
        assert el.find("CONSUMED-EVENT-GROUPS") is None
        assert el.find("EVENT-MULTICAST-SUBSCRIPTION-ADDRESSS") is None
        assert el.find("INSTANCE-IDENTIFIER") is None
        assert el.find("LOCAL-UNICAST-ADDRESSS") is None
        assert el.find("MINOR-VERSION") is None
        assert el.find("PROVIDED-SERVICE-INSTANCE-REF") is None
        assert el.find("REMOTE-UNICAST-ADDRESSS") is None
        assert el.find("SD-CLIENT-CONFIG") is None
        assert el.find("SD-CLIENT-TIMER-CONFIGS") is None
        assert el.find("SERVICE-IDENTIFIER") is None
        assert el.find("VERSION-DRIVEN-FIND-BEHAVIOR") is None


class TestConsumedServiceInstanceRoundTrip:
    def test_round_trip_preserves_all_values(self, writer, parser, tmp_path):
        instance = _full_instance()

        parent = _parent()
        writer.writeConsumedServiceInstance(parent, instance)

        out_file = str(tmp_path / "consumed_service_instance.arxml")
        with open(out_file, "w", encoding="utf-8") as f:
            f.write(ET.tostring(_namespaced_wrap(parent), encoding="unicode"))

        recovered = ConsumedServiceInstance(MockParent(), "MyConsumedService")
        tree = ET.parse(out_file)
        parser.readConsumedServiceInstance(tree.getroot(), recovered)

        assert recovered.getShortName() == "MyConsumedService"
        assert [r.getValue() for r in recovered.getAllowedServiceProviderRefs()] == ["/Ether/NetworkEndpoint/NE1"]
        assert recovered.getAutoRequire().getValue() is True
        versions = recovered.getBlocklistedVersions()
        assert len(versions) == 2
        assert versions[0].getMajorVersion().getValue() == 1
        assert versions[0].getMinorVersion().getValue() == 0
        assert versions[1].getMajorVersion().getValue() == 2
        assert versions[1].getMinorVersion().getValue() == 5
        groups = recovered.getConsumedEventGroups()
        assert len(groups) == 1
        assert groups[0].getShortName() == "CEG1"
        assert groups[0].getEventGroupIdentifier().getValue() == 7
        assert recovered.getEventMulticastSubscriptionAddressRef().getValue() == "/Ether/ApplicationEndpoint/MC1"
        assert recovered.getInstanceIdentifier().getValue() == "123"
        assert [r.getValue() for r in recovered.getLocalUnicastAddressRefs()] == ["/Ether/ApplicationEndpoint/LU1", "/Ether/ApplicationEndpoint/LU2"]
        assert recovered.getMinorVersion().getValue() == "ANY"
        assert recovered.getProvidedServiceInstanceRef().getValue() == "/Ether/Provider/PSI1"
        assert [r.getValue() for r in recovered.getRemoteUnicastAddressRefs()] == ["/Ether/ApplicationEndpoint/RU1"]
        re_config = recovered.getSdClientConfig()
        assert re_config is not None
        assert re_config.getClientServiceMajorVersion().getValue() == 15
        assert re_config.getTtl().getValue() == 10
        assert recovered.getSdClientTimerConfigRef().getValue() == "/SomeipSdTimingConfigs/InstanceTiming1"
        assert recovered.getServiceIdentifier().getValue() == 50
        assert recovered.getVersionDrivenFindBehavior().getValue() == "minimumMinorVersion"

    def test_reader_empty_fields(self, parser):
        element = ET.fromstring(f"<CONSUMED-SERVICE-INSTANCE xmlns='{NS}'><SHORT-NAME>EmptyService</SHORT-NAME></CONSUMED-SERVICE-INSTANCE>")

        recovered = ConsumedServiceInstance(MockParent(), "EmptyService")
        parser.readConsumedServiceInstance(element, recovered)

        assert recovered.getAllowedServiceProviderRefs() == []
        assert recovered.getAutoRequire() is None
        assert recovered.getBlocklistedVersions() == []
        assert recovered.getConsumedEventGroups() == []
        assert recovered.getEventMulticastSubscriptionAddressRef() is None
        assert recovered.getInstanceIdentifier() is None
        assert recovered.getLocalUnicastAddressRefs() == []
        assert recovered.getMinorVersion() is None
        assert recovered.getProvidedServiceInstanceRef() is None
        assert recovered.getRemoteUnicastAddressRefs() == []
        assert recovered.getSdClientConfig() is None
        assert recovered.getSdClientTimerConfigRef() is None
        assert recovered.getServiceIdentifier() is None
        assert recovered.getVersionDrivenFindBehavior() is None
