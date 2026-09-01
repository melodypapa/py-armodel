from armodel.models.M2.AUTOSARTemplates.AdaptivePlatform.PlatformModuleDeployment.Firewall import (
    DdsRule,
)


class TestDdsRule:
    def test_defaults(self):
        obj = DdsRule()
        assert obj.getAppId() is None
        assert obj.getHostId() is None
        assert obj.getInstanceId() is None
        assert obj.getMajorProtocolVersion() is None
        assert obj.getMinorProtocolVersion() is None
        assert obj.getProductId() is None
        assert obj.getReaderEntityId() is None
        assert obj.getSubmessageType() is None
        assert obj.getVendorId() is None
        assert obj.getWriterEntityId() is None

    def test_set_get_header_ids(self):
        obj = DdsRule()
        assert obj.setAppId("1") is obj
        assert obj.getAppId() == "1"
        assert obj.setHostId("2") is obj
        assert obj.getHostId() == "2"
        assert obj.setInstanceId("3") is obj
        assert obj.getInstanceId() == "3"
        assert obj.setProductId("4") is obj
        assert obj.getProductId() == "4"
        assert obj.setVendorId("5") is obj
        assert obj.getVendorId() == "5"

    def test_set_get_protocol_versions(self):
        obj = DdsRule()
        assert obj.setMajorProtocolVersion("2") is obj
        assert obj.getMajorProtocolVersion() == "2"
        assert obj.setMinorProtocolVersion("5") is obj
        assert obj.getMinorProtocolVersion() == "5"

    def test_set_get_entity_ids_and_submessage_type(self):
        obj = DdsRule()
        assert obj.setReaderEntityId("6") is obj
        assert obj.getReaderEntityId() == "6"
        assert obj.setWriterEntityId("7") is obj
        assert obj.getWriterEntityId() == "7"
        assert obj.setSubmessageType("0x0E") is obj
        assert obj.getSubmessageType() == "0x0E"

    def test_overwrite(self):
        obj = DdsRule()
        obj.setAppId("1")
        obj.setAppId("2")
        assert obj.getAppId() == "2"

    def test_class_docstring_is_template_description_verbatim(self):
        assert DdsRule.__doc__ == "Configuration of a DDS firewall rule"
