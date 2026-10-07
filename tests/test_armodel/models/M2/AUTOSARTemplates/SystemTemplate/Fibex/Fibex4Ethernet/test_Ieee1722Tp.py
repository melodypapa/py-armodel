import inspect

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import PositiveInteger, TimeValue
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Ethernet.EthernetTopology import Ieee1722Tp

CLASS_NOTE = "Content Model for IEEE 1722 configuration. Tags: atp.Status=obsolete"


class TestIeee1722Tp:
    """Test cases for Ieee1722Tp (Table 6.131, p.461)."""

    def _obj(self):
        return Ieee1722Tp()

    def test_initialization_defaults(self):
        obj = self._obj()
        assert obj.getRelativeRepresentationTime() is None
        assert obj.getStreamIdentifier() is None
        assert obj.getSubType() is None
        assert obj.getVersion() is None

    def test_get_set_relative_representation_time(self):
        obj = self._obj()
        value = TimeValue().setValue("0.5")
        assert obj.setRelativeRepresentationTime(value) is obj
        assert obj.getRelativeRepresentationTime() is value
        obj.setRelativeRepresentationTime(None)
        assert obj.getRelativeRepresentationTime() is value

    def test_get_set_stream_identifier(self):
        obj = self._obj()
        value = PositiveInteger().setValue("1712384")
        assert obj.setStreamIdentifier(value) is obj
        assert obj.getStreamIdentifier() is value
        obj.setStreamIdentifier(None)
        assert obj.getStreamIdentifier() is value

    def test_get_set_sub_type(self):
        obj = self._obj()
        value = PositiveInteger().setValue("0")
        assert obj.setSubType(value) is obj
        assert obj.getSubType() is value
        obj.setSubType(None)
        assert obj.getSubType() is value

    def test_get_set_version(self):
        obj = self._obj()
        value = PositiveInteger().setValue("2")
        assert obj.setVersion(value) is obj
        assert obj.getVersion() is value
        obj.setVersion(None)
        assert obj.getVersion() is value

    def test_class_docstring_note(self):
        assert inspect.cleandoc(Ieee1722Tp.__doc__) == CLASS_NOTE

    def test_accessor_docstrings_verbatim(self):
        obj = self._obj()
        assert (
            inspect.cleandoc(obj.getRelativeRepresentationTime.__doc__)
            == "Defines the time when content shall be presented (in seconds). The actual absolute time is creation time plus relative presentation time. Tags: atp.Status=obsolete"
        )
        assert (
            inspect.cleandoc(obj.setRelativeRepresentationTime.__doc__).split("\n")[0]
            == "Defines the time when content shall be presented (in seconds). The actual absolute time is creation time plus relative presentation time. Tags: atp.Status=obsolete"
        )
        assert inspect.cleandoc(obj.getStreamIdentifier.__doc__) == "IEEE 1722 stream identifier Tags: atp.Status=obsolete"
        assert inspect.cleandoc(obj.getSubType.__doc__) == "Protocol type. Tags: atp.Status=obsolete"
        assert inspect.cleandoc(obj.getVersion.__doc__) == "Revision of Ieee1722 standard Tags: atp.Status=obsolete"
