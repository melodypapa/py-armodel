"""
Tests for reading the DdsCpServiceInstance group members — DdsCpServiceInstance, Table 6.152 (p.472, R23-11).

The class is an abstract nested Identifiable (spec Base chain
ARObject/AbstractServiceInstance/Identifiable/...; AbstractServiceInstance is
cycle-blocked from Identifiable.py — wave-1 DdsCp* precedent 0babf1fb0 — so the synced
base is Identifiable). There is no own complexType: the group content sits after the
IDENTIFIABLE group inside the subclass complexTypes (DDS-CP-CONSUMED-SERVICE-INSTANCE,
AUTOSAR_00052.xsd; group DDS-CP-SERVICE-INSTANCE l.29079), so the reusable helper
readDdsCpServiceInstance is exercised directly on a DDS-CP-CONSUMED-SERVICE-INSTANCE
subtree via the concrete stub subclass DdsCpConsumedServiceInstance.

Round-trip counterpart: tests/test_armodel/writer/test_writer_dds_cp_service_instance.py
"""

import xml.etree.ElementTree as ET

import pytest

from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable import (
    DdsCpConsumedServiceInstance,
    DdsCpServiceInstance,
)

NS = "http://autosar.org/schema/r4.0"


@pytest.fixture(autouse=True)
def reset_autosar():
    AUTOSAR.getInstance().new()
    AUTOSAR.getInstance().setARRelease("R23-11")
    yield
    AUTOSAR.getInstance().new()


def _snip(inner: str) -> ET.Element:
    return ET.fromstring(f"<DDS-CP-CONSUMED-SERVICE-INSTANCE xmlns='{NS}'>{inner}</DDS-CP-CONSUMED-SERVICE-INSTANCE>")


class TestReadDdsCpServiceInstance:
    """Tests for readDdsCpServiceInstance — group member field values (Table 6.152)."""

    def _read(self, parser, inner):
        instance = DdsCpConsumedServiceInstance(AUTOSAR.getInstance(), "DdsInstance1")
        parser.readDdsCpServiceInstance(_snip(inner), instance)
        return instance

    def test_read_sets_all_fields(self, parser):
        """Test that all seven group members are read with their values in XSD order."""
        instance = self._read(
            parser,
            "<SHORT-NAME>DdsInstance1</SHORT-NAME>"
            '<DDS-FIELD-REPLY-TOPIC-REF DEST="DDS-CP-TOPIC">/DdsCpConfig/Topics/FieldReplyTopic</DDS-FIELD-REPLY-TOPIC-REF>'
            '<DDS-FIELD-REQUEST-TOPIC-REF DEST="DDS-CP-TOPIC">/DdsCpConfig/Topics/FieldRequestTopic</DDS-FIELD-REQUEST-TOPIC-REF>'
            '<DDS-METHOD-REPLY-TOPIC-REF DEST="DDS-CP-TOPIC">/DdsCpConfig/Topics/MethodReplyTopic</DDS-METHOD-REPLY-TOPIC-REF>'
            '<DDS-METHOD-REQUEST-TOPIC-REF DEST="DDS-CP-TOPIC">/DdsCpConfig/Topics/MethodRequestTopic</DDS-METHOD-REQUEST-TOPIC-REF>'
            '<DDS-SERVICE-QOS-PROFILE-REF DEST="DDS-CP-QOS-PROFILE">/DdsCpConfig/QosProfiles/Profile1</DDS-SERVICE-QOS-PROFILE-REF>'
            "<SERVICE-INSTANCE-ID>42</SERVICE-INSTANCE-ID>"
            "<SERVICE-INTERFACE-ID>MyServiceInterface</SERVICE-INTERFACE-ID>",
        )
        assert instance.getShortName() == "DdsInstance1"

        assert instance.getDdsFieldReplyTopicRef() is not None
        assert instance.getDdsFieldReplyTopicRef().getDest() == "DDS-CP-TOPIC"
        assert instance.getDdsFieldReplyTopicRef().getValue() == "/DdsCpConfig/Topics/FieldReplyTopic"
        assert instance.getDdsFieldRequestTopicRef() is not None
        assert instance.getDdsFieldRequestTopicRef().getValue() == "/DdsCpConfig/Topics/FieldRequestTopic"
        assert instance.getDdsMethodReplyTopicRef() is not None
        assert instance.getDdsMethodReplyTopicRef().getValue() == "/DdsCpConfig/Topics/MethodReplyTopic"
        assert instance.getDdsMethodRequestTopicRef() is not None
        assert instance.getDdsMethodRequestTopicRef().getValue() == "/DdsCpConfig/Topics/MethodRequestTopic"
        assert instance.getDdsServiceQosProfileRef() is not None
        assert instance.getDdsServiceQosProfileRef().getDest() == "DDS-CP-QOS-PROFILE"
        assert instance.getDdsServiceQosProfileRef().getValue() == "/DdsCpConfig/QosProfiles/Profile1"

        assert instance.getServiceInstanceId() is not None
        assert instance.getServiceInstanceId().getValue() == 42
        assert instance.getServiceInterfaceId() is not None
        assert instance.getServiceInterfaceId().getValue() == "MyServiceInterface"

    def test_read_empty(self, parser):
        """Test that absent elements leave the fields None."""
        instance = self._read(parser, "<SHORT-NAME>DdsInstance1</SHORT-NAME>")
        assert instance.getDdsFieldReplyTopicRef() is None
        assert instance.getDdsFieldRequestTopicRef() is None
        assert instance.getDdsMethodReplyTopicRef() is None
        assert instance.getDdsMethodRequestTopicRef() is None
        assert instance.getDdsServiceQosProfileRef() is None
        assert instance.getServiceInstanceId() is None
        assert instance.getServiceInterfaceId() is None

    def test_helper_takes_abstract_base_annotation(self, parser):
        """Test that the helper accepts any DdsCpServiceInstance subclass instance."""
        assert issubclass(DdsCpConsumedServiceInstance, DdsCpServiceInstance)
